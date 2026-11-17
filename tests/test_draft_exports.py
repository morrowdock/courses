# SPDX-License-Identifier: Apache-2.0
"""Regression checks for content corrections and usable format-v1 exports."""
import collections
import contextlib
import io
import unittest

from tools.export_drafts import choices_text, gym_activity
from tools.validate import ROOT, load_json

GYM = ROOT / 'courses/cg-foundations-v1/1.0.0-draft'
GIT = ROOT / 'courses/git-course-v1/1.0.0-draft'


def gym_sources():
    return [a for path in sorted((GYM / 'attachments').glob('cg-foundations-*.json'))
            for a in load_json(path)['activities']]


class DraftExportTests(unittest.TestCase):
    def test_choice_keys_and_bundle_positions(self):
        positions = []
        sources = {a['id']: a for a in gym_sources()}
        for source in sources.values():
            lists = []
            if source['kind'] == 'predict' and source['answer']['type'] == 'choice':
                lists.append(source['answer']['choices'])
            lists.extend(cp['answer']['choices'] for cp in source.get('checkpoints', [])
                         if cp['answer']['type'] == 'choice')
            if source['kind'] == 'fix':
                lists.append(source['fixes'])
            for choices in lists:
                correct = [i for i, c in enumerate(choices) if c.get('correct')]
                self.assertEqual(len(correct), 1)
                positions.extend(correct)
        self.assertEqual(len(positions), 52)
        self.assertEqual(set(positions), {0, 1, 2})
        bundle = load_json(GYM / 'bundle.json')
        for q in bundle['questions']:
            choices = sources[q['id']]['answer']['choices']
            self.assertTrue(choices[q['answer']].get('correct'))
            self.assertEqual(q['choices'], [c['text'] for c in choices])
        self.assertEqual(collections.Counter(q['answer'] for q in bundle['questions']), {0: 4, 1: 4, 2: 4})

    def test_checkpoints_survive_export_without_revealing_answers_in_prompt(self):
        public = {a['id']: a for a in load_json(GYM / 'course.json')['activities']}
        count = 0
        for source in gym_sources():
            if source['kind'] != 'trace':
                continue
            exported = public[source['id']]
            for i, cp in enumerate(source.get('checkpoints', []), 1):
                self.assertIn(cp['ask'], exported['prompt'])
                self.assertIn(f'Checkpoint {i}, frame {cp["frame"] + 1}', exported['prompt'])
                self.assertIn(f'Checkpoint {i}:', exported['explanation'])
                self.assertNotIn('"stack":', '\n'.join(exported['expectedTrace']))
                count += 1
        self.assertEqual(count, 37)

    def test_multiline_options_and_choice_number_expected(self):
        self.assertEqual(choices_text(['0\n1\n2', '1\\n2']),
                         'Choice 1:\n    0\n    1\n    2\n\nChoice 2:\n    1\n    2')
        for source in gym_sources():
            if source.get('answer', {}).get('type') != 'choice':
                continue
            exported = gym_activity(source)
            index = int(exported['expected']) - 1
            self.assertTrue(source['answer']['choices'][index].get('correct'))
            self.assertIn(f'Choice {index + 1}:', exported['prompt'])

    def test_average_handles_an_odd_total(self):
        source = next(a for a in gym_sources() if a['id'] == 'fn-i-fix')
        solution = gym_activity(source)['solution']
        namespace = {}
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            exec(compile(solution, '<average-regression>', 'exec'), namespace)
        self.assertEqual(stdout.getvalue(), '6.0\n')
        self.assertEqual(namespace['avg'](4, 7), 5.5)

    def test_parsons_decoy_changes_the_answer(self):
        source = next(a for a in gym_sources() if a['id'] == 'ld-i-parsons-cb')
        pool = {x['id']: x['line'] for x in source['lines'] + source['distractors']}
        def output(order):
            with contextlib.redirect_stdout(io.StringIO()) as stdout:
                exec(compile('\n'.join(pool[k] for k in order), '<decoy-regression>', 'exec'), {})
            return stdout.getvalue()
        accepted = source['accepted'][0]
        self.assertEqual(output(accepted), '6\n')
        for at in range(len(accepted) + 1):
            order = accepted[:at] + ['x'] + accepted[at:]
            try:
                printed = output(order)
            except SyntaxError:
                continue
            self.assertNotEqual(printed, '6\n', order)

    def test_line_feedback_and_python_only_core_explanations(self):
        for source in gym_sources():
            if source['kind'] == 'fix':
                self.assertEqual(set(range(1, len(source['code']) + 1)) - {source['bugLine']},
                                 set(map(int, source['lineReactions'])))
            if source['kind'] == 'explain':
                self.assertNotIn('Lua', source['prompt'])
                self.assertNotIn('Lua', str(source['rubric']))

    def test_lesson_path_does_not_duplicate_bundle_questions(self):
        course = load_json(GYM / 'course.json')
        self.assertEqual(len(course['answerChecks']), 12)
        for lesson in course['lessons']:
            self.assertFalse(any(s['kind'] == 'question' for s in lesson['steps']))

    def test_git_goals_are_readable_and_recovery_does_not_leak_answer(self):
        course = load_json(GIT / 'course.json')
        for activity in course['activities']:
            self.assertNotIn('Reference solutions remain withheld', activity['explanation'])
            self.assertNotIn('/home/', activity['explanation'])
            self.assertNotIn('{"', activity['explanation'])
        bundle = load_json(GIT / 'bundle.json')
        q = next(q for q in bundle['questions'] if q['id'] == 'git-course-recovery-v1-predict')
        self.assertNotIn('Then run:', q['prompt'])
        self.assertNotIn(q['choices'][q['answer']], q['prompt'])
