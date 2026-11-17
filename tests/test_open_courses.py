# SPDX-License-Identifier: Apache-2.0
"""Course-specific publication boundaries, feedback and input requirements."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from tools.validate import ROOT, check_course, load_json, validate
from tools.export_drafts import frame_text

GIT = ROOT / 'courses/git-course-v1/1.0.0-draft'
GYM = ROOT / 'courses/cg-foundations-v1/1.0.0-draft'


def gym_lessons():
    manifest = load_json(GYM / 'attachments/authored-code-gym-foundations-v1.json')
    return [load_json(GYM / 'attachments' / r['resource']) for r in manifest['lessons']]


class OpenCoursesTests(unittest.TestCase):
    def test_complete_public_registry(self):
        self.assertEqual(validate(swift=False), (3, 4))
        registry = load_json(ROOT / 'registry.json')
        self.assertEqual({e['id'] for e in registry['entries']}, {'demo', 'git-course-v1', 'cg-foundations-v1'})
        for root, count, media in ((GIT, 29, 1), (GYM, 96, 7)):
            course = load_json(root / 'course.json')
            self.assertEqual(len(course['lessons']), 6)
            self.assertEqual(len(course['activities']), count)
            self.assertEqual(len(course['media']), media)
            self.assertEqual(len(course['answerChecks']), 12)
            self.assertEqual(course['review'], {'status': 'draft', 'reviewedAt': None, 'reviewers': {'aiChecks': [], 'humanApprover': None}})
            self.assertEqual(course['creators'], [{'displayName': 'Collin Craig'}])
            self.assertFalse((root / 'manifest.json').exists())
            self.assertFalse((root / 'provenance.json').exists())

    def test_git_answer_boundary(self):
        course = load_json(GIT / 'attachments/learner.json')
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
        for task in tasks:
            self.assertEqual(task['inputNeeds'], {'alternatives': ['keyboard'], 'remoteOnlyOK': False})

    def test_code_gym_answer_contract(self):
        lessons = gym_lessons()
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

    def test_input_declarations_and_alternatives(self):
        manifest = load_json(GYM / 'course.json')
        public = {a['id']: a for a in manifest['activities']}
        for lesson in gym_lessons():
            for activity in lesson['activities']:
                inputs = activity['inputNeeds']
                self.assertEqual(inputs, public[activity['id']]['inputNeeds'])
                self.assertIn('keyboard', inputs['alternatives'])
                self.assertEqual(inputs['remoteOnlyOK'], 'remote' in inputs['alternatives'])
                self.assertIn('keyboard', activity['prompt'].lower())
                if activity['kind'] in ('parsons', 'fix'):
                    self.assertTrue(inputs['remoteOnlyOK'])
                    self.assertNotRegex(activity['prompt'], r'Tap the (wrong )?line')
                    self.assertNotIn('Pencil', activity['prompt'])
                    self.assertNotIn('Drag the lines', activity['prompt'])
                if activity.get('answer', {}).get('type') == 'typed':
                    self.assertFalse(inputs['remoteOnlyOK'])
                    self.assertEqual(inputs['alternatives'], ['keyboard'])

    def test_parsons_keeps_all_recorded_variants(self):
        public = {a['id']: a for a in load_json(GYM / 'course.json')['activities']}
        count = 0
        for lesson in gym_lessons():
            for activity in lesson['activities']:
                if activity['kind'] != 'parsons': continue
                count += 1
                converted = public[activity['id']]
                self.assertEqual(converted['kind'], 'explanation')
                self.assertIn('Self-check only', converted['explanation'])
                self.assertIn(json.dumps(activity['accepted']), converted['explanation'])
                for line in activity['lines'] + activity.get('distractors', []):
                    self.assertIn(line['id'] + ': ' + line['line'], converted['prompt'])
        self.assertEqual(count, 18)

    def test_generated_activity_answers_match_admitted_projection(self):
        public = {a['id']: a for a in load_json(GYM / 'course.json')['activities']}
        for lesson in gym_lessons():
            for source in lesson['activities']:
                activity = public[source['id']]
                if source['kind'] == 'fix':
                    correct = next(f for f in source['fixes'] if f.get('correct'))
                    expected = source['code'].copy()
                    expected[source['bugLine'] - 1] = correct['fixLine']
                    self.assertEqual(activity['solution'], '\n'.join(expected))
                elif source['kind'] == 'trace':
                    self.assertEqual(activity['expectedTrace'], [frame_text(f, i) for i, f in enumerate(source['frames'])])
                elif source['kind'] == 'predict':
                    answer = source['answer']
                    expected = (answer['expected'] if answer['type'] == 'typed' else
                                str(next(i for i, c in enumerate(answer['choices']) if c.get('correct')) + 1))
                    self.assertEqual(activity['expected'], expected)

    def test_recovery_merge_ancestor_feedback_with_real_git(self):
        lesson = next(l for l in load_json(GIT / 'attachments/learner.json')['lessons'] if l['id'] == 'git-course-recovery-v1')
        prediction = lesson['learn']['questions'][0]
        feedback = prediction['why'][prediction['choices'].index('git merge main')]
        self.assertIn('Already up to date.', feedback)
        self.assertIn('does not undo the rebase', feedback)
        with tempfile.TemporaryDirectory() as tmp:
            def git(*args):
                return subprocess.check_output(['git', '-c', 'user.name=Synthetic test', '-c', 'user.email=test@example.invalid', *args], cwd=tmp, env={**os.environ, 'LC_ALL': 'C'}, stderr=subprocess.PIPE, text=True).strip()
            git('init', '-b', 'main'); git('commit', '--allow-empty', '-m', 'Base')
            git('branch', 'topic'); git('commit', '--allow-empty', '-m', 'Main work')
            git('switch', 'topic'); git('commit', '--allow-empty', '-m', 'Topic work')
            git('rebase', 'main'); before = git('rev-parse', 'HEAD')
            self.assertEqual(git('merge', 'main'), 'Already up to date.')
            self.assertEqual(git('rev-parse', 'HEAD'), before)
            self.assertEqual(git('rev-list', '--count', 'main..HEAD'), '1')

    def test_missing_public_provenance_mapping_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'course'
            shutil.copytree(GYM, folder)
            course = load_json(folder / 'course.json')
            course['provenance'] = [p for p in course['provenance'] if p['item'] != 'activity:nv-g-parsons']
            (folder / 'course.json').write_text(json.dumps(course))
            with self.assertRaisesRegex(ValueError, 'provenance coverage'):
                check_course(folder / 'course.json')
