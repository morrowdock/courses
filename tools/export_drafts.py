# SPDX-License-Identifier: Apache-2.0
"""Rebuild public draft wrappers and pins from the admitted learner attachments.

Uses only this repository's public data. Does not execute course programs or
change review status. Format v1 has no structured checkpoint field, so questions
go in the prompt and their reference answers in the explanation.
"""
import hashlib
import json
import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def pin(path):
    data = path.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'size': len(data)}


def choices_text(choices):
    # Recorded stdout uses escaped newlines in the learner projection. Make each
    # option a separate labelled block, including its indented continuation lines.
    return '\n\n'.join(
        f'Choice {i}:\n' + '\n'.join('    ' + line for line in text.replace('\\n', '\n').split('\n'))
        for i, text in enumerate(choices, 1)
    )


def goal_text(goal):
    key, value = next(iter(goal.items()))
    if key == 'log':
        return 'History, newest first: ' + ' → '.join(value) + '.'
    if key in ('file', 'committed', 'staged'):
        where = {'file': 'Working file', 'committed': 'Last committed version of', 'staged': 'Staged version of'}[key]
        return f'{where} {Path(value[0]).name}: {value[1].rstrip()!r} (ending with a newline).'
    if key in ('untracked', 'unstaged', 'absent'):
        return f'{Path(value).name} ' + {'untracked': 'is untracked.', 'unstaged': 'has an unstaged edit.', 'absent': 'is absent from the working folder.'}[key]
    if key == 'headMessage':
        return f'The current commit is named “{value}”.'
    if key == 'branch':
        return f'Finish on branch {value}.'
    if key in ('tipMessage', 'tipIs'):
        return f'{value[0]} points at ' + (f'the commit named “{value[1]}”.' if key == 'tipMessage' else f'the original commit {value[1]}.')
    if key in ('in', 'notIn'):
        return f'{value[0]} history ' + ('contains' if key == 'in' else 'does not contain') + f' “{value[1]}”.'
    if key == 'parentsOf':
        return f'On {value[0]}, “{value[1]}” has these parent commit(s): ' + ', '.join(value[2]) + '.'
    if key == 'linear':
        return f'{value} has a straight-line history without merge commits.'
    if key == 'mergeTip':
        return f'{value} ends at a merge commit with two parents.'
    if key == 'clean':
        return 'No staged changes, unstaged changes or untracked files remain.'
    if key == 'trackedClean':
        return 'All tracked files match the staging area and last commit; untracked files may remain.'
    raise ValueError(f'Unrendered goal: {goal}')


def frame_text(frame, index):
    event = frame['event']
    where = f'Line {frame["line"]} next' if event == 'line' else ('Program ended' if event == 'end' else f'Return from line {frame["line"]}')
    stack = []
    for call in frame['stack']:
        values = ', '.join(f'{k} = {v}' for k, v in call['vars'].items()) or '(no names yet)'
        stack.append(f'{call["fn"]}: {values}')
    result = f'Frame {index + 1} · {where} · ' + ' | '.join(stack)
    result += ' · cumulative output: ' + (frame['out'].replace('\n', '\\n') or '(none)')
    if 'returns' in frame:
        result += f' · returns {frame["returns"]}'
    return result


def gym_activity(source):
    a = {'id': source['id'], 'kind': {'predict': 'prediction', 'explain': 'explanation', 'parsons': 'explanation'}.get(source['kind'], source['kind']),
         'prompt': source['prompt'], 'explanation': '', 'inputNeeds': source['inputNeeds']}
    if 'code' in source:
        a.update(code='\n'.join(source['code']), language='python')
    if source['kind'] == 'predict':
        answer = source['answer']
        if answer['type'] == 'choice':
            correct = next(i for i, c in enumerate(answer['choices']) if c.get('correct'))
            a['prompt'] += '\n\nSelect a choice number.\n\n' + choices_text([c['text'] for c in answer['choices']])
            a['expected'] = str(correct + 1)
            a['explanation'] = f'Choice {correct + 1}. ' + answer['choices'][correct]['reaction']
        else:
            a['expected'] = answer['expected']
            a['explanation'] = source.get('reveal', 'Compare with the recorded output.')
    elif source['kind'] == 'trace':
        checkpoints = source.get('checkpoints', [])
        if checkpoints:
            a['prompt'] += '\n\nCheckpoints (frame numbers below start at 1). Answer separately before revealing the recorded observations:'
            answers = []
            for i, cp in enumerate(checkpoints, 1):
                a['prompt'] += f'\n\nCheckpoint {i}, frame {cp["frame"] + 1}, {cp["var"]}: {cp["ask"]}'
                if 'depth' in cp:
                    a['prompt'] += f' (Call stack depth {cp["depth"]}, counting from the main program at 0.)'
                answer = cp['answer']
                if answer['type'] == 'choice':
                    a['prompt'] += '\nSelect a choice number.\n' + choices_text([c['text'] for c in answer['choices']])
                    correct = next(j for j, c in enumerate(answer['choices']) if c.get('correct'))
                    answers.append(f'Checkpoint {i}: choice {correct + 1} ({answer["choices"][correct]["text"]}). ' + answer['choices'][correct]['reaction'])
                else:
                    answers.append(f'Checkpoint {i}: {answer["expected"]}.')
            a['explanation'] = '\n'.join(answers) + '\n\n'
        a['explanation'] += 'Read the recorded observations in order.\n' + '\n'.join(source.get('narration', []))
        a['expectedTrace'] = [frame_text(f, i) for i, f in enumerate(source['frames'])]
    elif source['kind'] == 'fix':
        correct = next(i for i, f in enumerate(source['fixes']) if f.get('correct'))
        a['prompt'] += '\n\nRepair choices:\n' + choices_text([f['fixLine'] for f in source['fixes']])
        code = source['code'].copy()
        code[source['bugLine'] - 1] = source['fixes'][correct]['fixLine']
        a['solution'] = '\n'.join(code)
        a['explanation'] = f'Line {source["bugLine"]}, choice {correct + 1}. ' + source['fixes'][correct]['reaction']
    elif source['kind'] == 'explain':
        a['explanation'] = source['model'] + '\n\nSelf-check:\n' + '\n'.join('- ' + r['idea'] for r in source['rubric'])
    elif source['kind'] == 'parsons':
        a['prompt'] += f'\n\nReading-based Parsons exercise (exactly {len(source["accepted"][0])} lines):\n'
        a['prompt'] += '\n'.join(x['id'] + ': ' + x['line'] for x in source['lines'] + source.get('distractors', []))
        a['explanation'] = 'Self-check only. Preserve indentation and choose exactly the required number of lines. Recorded accepted line-ID orders: ' + json.dumps(source['accepted']) + '. These include every admitted alternative; the format-v1 single-permutation checker cannot represent this exercise faithfully.'
    return a


def export_course(course_id):
    folder = ROOT / 'courses' / course_id / '1.0.0-draft'
    course = load(folder / 'course.json')
    bundle = load(folder / 'bundle.json')
    assert course['review']['status'] == 'draft', 'Only unreviewed drafts may be regenerated'
    if course_id == 'git-course-v1':
        source = load(folder / 'attachments/learner.json')
        course['prerequisites'] = source['startingKnowledge']
        tasks = {t['id'].replace('.', '-'): t for l in source['lessons'] for t in l['tasks']}
        for a in course['activities']:
            t = tasks[a['id']]
            a['prompt'] = t['instruction'] + '\n\nStarting commands:\n' + '\n'.join(t['setup'])
            if t.get('broken'):
                a['prompt'] += '\n\nBroken commands:\n' + '\n'.join(t['broken'])
            a['explanation'] = 'Self-check your proposed final state:\n' + '\n'.join('- ' + goal_text(g) for g in t['goals'])
            a['explanation'] += '\n' + t.get('explain', 'Explain why your commands reach these goals. Worked answers, when supplied, are in the lesson reading’s final hint.')
        questions = {q['id'].replace('.', '-'): q for l in source['lessons'] for q in l['learn']['questions']}
        for q in bundle['questions']:
            s = questions[q['id']]
            q.update(prompt=s['prompt'], choices=s['choices'], answer=s['answer'], explanation=s['why'][s['answer']])
            for key, label in [('setup', 'Starting commands'), ('commands', 'Then run')]:
                if s.get(key):
                    q['prompt'] += '\n\n' + label + ':\n' + '\n'.join(s[key])
    else:
        index = load(folder / 'attachments/authored-code-gym-foundations-v1.json')
        lessons = [load(folder / 'attachments' / l['resource']) for l in index['lessons']]
        sources = {a['id']: a for l in lessons for a in l['activities']}
        course['activities'] = [gym_activity(a) for l in lessons for a in l['activities']]
        for q in bundle['questions']:
            s = sources[q['id']]
            options = s['answer']['choices']
            correct = next(i for i, c in enumerate(options) if c.get('correct'))
            q.update(prompt=s['prompt'] + '\n\n' + '\n'.join(s['code']), choices=[c['text'] for c in options], answer=correct, explanation=options[correct]['reaction'])
        # Activities keep checkpoints/hints; bundle copies remain available for
        # standalone quizzes but are not asked a second time in the lesson path.
        for lesson in course['lessons']:
            lesson['steps'] = [s for s in lesson['steps'] if s['kind'] != 'question']
        step_ids = {s['id'] for l in course['lessons'] for s in l['steps']}
        course['provenance'] = [p for p in course['provenance'] if not p['item'].startswith('step:') or p['item'][5:] in step_ids]
    course['answerChecks'] = [{'questionID': q['id'], 'kind': 'choice-index', 'expectedIndex': q['answer']} for q in bundle['questions']]
    save(folder / 'bundle.json', bundle)
    course['bundle'].update(pin(folder / 'bundle.json'))
    for media in course['media']:
        media.update(pin(folder / media['path']))
    save(folder / 'course.json', course)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', action='store_true', help='also refresh FILES.json for the current tracked/staged file set')
    args = parser.parse_args()
    for course_id in ('git-course-v1', 'cg-foundations-v1'):
        export_course(course_id)
    if args.inventory:
        inventory = load(ROOT / 'FILES.json')
        paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT, text=True).split('\0')
        inventory['date'] = '2026-11-17'
        inventory['files'] = [{'path': p, 'sha256': pin(ROOT / p)['sha256']}
                              for p in sorted(paths) if p and p != 'FILES.json']
        save(ROOT / 'FILES.json', inventory)


if __name__ == '__main__':
    main()
