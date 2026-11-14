"""Publication boundaries and corrupt-artifact rejection for the two drafts."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from tools.validate import ROOT, safe_asset, validate_registry


class OpenCoursesTests(unittest.TestCase):
    def test_git_answer_boundary_and_inventory(self):
        course = json.loads((ROOT / 'git-lab-v1/attachments/learner.json').read_text())
        self.assertEqual(len(course['lessons']), 6)
        tasks = [t for l in course['lessons'] for t in l['tasks']]
        self.assertEqual(len(tasks), 29)
        self.assertNotIn('git-course-reset-v1.g1', {t['id'] for t in tasks})
        forbidden = {'reference', 'mutants', 'fixed', 'brokenResult', 'expect', 'reveal', 'observed', 'parity', 'capstone'}
        def check(value):
            if isinstance(value, dict):
                self.assertFalse(forbidden & value.keys())
                for child in value.values(): check(child)
            elif isinstance(value, list):
                for child in value: check(child)
        check(course)

    def test_code_gym_answer_contract_and_counts(self):
        folder = ROOT / 'code-gym-foundations-v1/attachments'
        manifest = json.loads((folder / 'authored-code-gym-foundations-v1.json').read_text())
        lessons = [json.loads((folder / r['resource']).read_text()) for r in manifest['lessons']]
        self.assertEqual(len(lessons), 6)
        activities = [a for l in lessons for a in l['activities']]
        self.assertEqual(len(activities), 96)
        self.assertEqual(len({a['id'] for a in activities}), 96)
        for lesson in lessons:
            self.assertNotIn('provenance', lesson)
            self.assertNotIn('relatedNative', lesson)
        for activity in activities:
            if activity['kind'] == 'trace': self.assertIn('frames', activity)
            if activity['kind'] == 'parsons': self.assertTrue(activity['accepted'])
            if activity['kind'] == 'explain': self.assertEqual(activity['grading'], 'self-check')

    def test_reject_unsafe_paths(self):
        for path in ('../secret', '/home/user', 'a/../b', 'a\\b', 'a//b'):
            with self.subTest(path=path), self.assertRaises(ValueError): safe_asset(path)

    def test_reject_corruption_extra_files_and_promotion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('git-lab-v1', 'code-gym-foundations-v1', 'docs'):
                shutil.copytree(ROOT / name, root / name)
            shutil.copy(ROOT / 'registry.json', root / 'registry.json')
            validate_registry(root)
            asset = root / 'git-lab-v1/attachments/learner.json'
            original = asset.read_bytes()
            asset.write_bytes(original + b' ')
            with self.assertRaises(AssertionError): validate_registry(root)
            asset.write_bytes(original)
            extra = asset.parent / 'private-notes.txt'
            extra.write_text('synthetic forbidden extra file')
            with self.assertRaises(AssertionError): validate_registry(root)
            extra.unlink()
            registry = json.loads((root / 'registry.json').read_text())
            registry['entries'][0]['status'] = 'reviewed'
            (root / 'registry.json').write_text(json.dumps(registry))
            with self.assertRaises(AssertionError): validate_registry(root)
