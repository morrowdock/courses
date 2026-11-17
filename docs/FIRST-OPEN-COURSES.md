# First open courses: format-v1 drafts

Status: proposed public courses; structural and review checks do not confer approval.
Checked: 2026-11-14 UTC.
Source baseline: `cc40e0a6315a9f86d21496f268b34aa8547786d3` (owner-authorized private source).
Format authority: [open course v1](FORMAT.md), schema and shared validator from `format-v1-and-review-20261114`.

| Course | Manifest | Lessons | Included tasks/activities | Whole learning items excluded |
| --- | --- | --- | --- | --- |
| Git Lab | [course.json](../courses/git-course-v1/1.0.0-draft/course.json) | 6 | 29 tasks | 1 exercise with an unresolved-origin password-like example; 1 export-withheld capstone |
| Code Gym foundations | [course.json](../courses/cg-foundations-v1/1.0.0-draft/course.json) | 6 | 96 activities | 0 |

Both versions are `1.0.0-draft`, language `en`, licence `CC-BY-SA-4.0`. Creator: `{ "displayName": "Collin Craig" }`. Both review records remain `draft`, with null reviewedAt/humanApprover and empty aiChecks. No external review receipts or human approval are fabricated. The original synthetic demo registry entry remains present.

## Learner boundary and review corrections

The private exporter's `project_git` and `build_code_gym` allowlists define the starting projection. The initial public changes removed Git task `git-course-reset-v1.g1`, corrected recovery feedback, and added input declarations. The 2026-11-17 draft revision also corrects facts, safety guidance, assessment choices and teaching gaps identified by three content reviews; the public learner attachments remain the source for regenerated wrappers. Source README, tests, tools, author-only metadata, Git capstone and withheld reference answers remain excluded. The complete [Git Lab](provenance/git-lab-v1.md) and [Code Gym](provenance/code-gym-foundations-v1.md) ledgers retain original origin evidence and exclusions; structured `sources` and exhaustive per-item `provenance` mappings are in each course.json.

Recovery correction: after topic has been rebased onto main, main is an ancestor. `git merge main` reports “Already up to date.” and leaves HEAD unchanged; it does not add a merge or undo the rebase. A regression test constructs this state in a synthetic real Git repository and verifies it.

All eight projection attachments (one Git JSON, one Code Gym index and six Code Gym lesson JSONs) are declared as `media` with ID, path, SHA-256, size and `application/json` MIME type. The old package-level provenance.json and provisional manifest.json files are removed. Bundle pins are objects with path/hash/size. Registry local paths name course.json and match identity, creators, licence and review metadata. No remote release pin is invented.

## Activities and input requirements

All 29 Git tasks and 96 Code Gym activities have corresponding format-v1 activities and explicit `inputNeeds`. Git lessons include reading, activity and question steps. Code Gym lessons use reading and activity steps; their 12 bundle questions remain available for standalone quizzes without repeating the same questions in each lesson. Source mappings cover all retained steps. The 24 already learner-visible multiple-choice checks retain matching `answerChecks`; no private answer key is restored.

- Git tasks require keyboard commands. Their format-v1 activities are explanation/self-check plans against existing learner-visible goals; they do not pretend to run or grade Git.
- Code Gym predictions, trace frames and fixes map to the corresponding v1 activity types using only already admitted recorded data. Written explanations remain self-check activities.
- The 18 Parsons exercises retain distractors and every accepted order in the reading projection. Format v1 only supports a single permutation of all blocks, so these use explicitly labelled explanation/self-check activities, with the original pool and accepted line-ID orders. Nothing silently removes distractors or marks alternative valid solutions wrong.
- Finite-choice predictions, fix choices, reading-based Parsons and checkpoint-free traces declare touch, pointer, keyboard and remote alternatives. Focus/select, optional move controls and a text-reader fallback replace drag/tap-only instructions.
- Exact typed predictions, trace checkpoints and written explanations require a keyboard; `remoteOnlyOK` is false. Remote alternatives are not claimed for these inputs.

These are content input requirements and alternative interaction designs, **not evidence that any app implements these controls**. In text-only readers, learners record responses separately and self-check. The public validator never executes lesson programs.

## Bundle and player limits

Each strict CourseBundle keeps integer `version: 1`, its six topics/materials and twelve multiple-choice checks, examBlueprint and equationSheet. The 30-minute blueprint remains a compatibility placeholder, not an authored exam claim. No assignments, due dates or learner data are invented.

The extracted `CourseBundleImporter` rejects local attachments. Successful shared schema and Swift decoding checks establish structural validity, not app importability or playback. Git needs its virtual-shell player; Code Gym needs its recorded-frame player. Prerequisites use plain skill statements; unpublished Terminal Lab and SWE-track references are removed. AI-written content needs independent factual/provenance review.

## Verification

Run the shared validator and complete test suite using the repository's pinned dependency and Swift 6. Keep commands at low priority (`nice -n 10`) on the Omarchy laptop. For this revision the owner prohibits deletion commands, so do not invoke helpers that remove their own temporary files. No home-service containers are changed.

The full public repository now contains three open-format manifests and four bundles, including the unchanged legacy demo. Course-specific tests check the 12 lessons, 125 activities, eight media assets, answer boundary, declared input alternatives, rich Parsons preservation, recorded-answer conversion, provenance coverage and the real-Git recovery correction. The PR records actual command results at its head.

The 2026-11-17 revision replays the public Git and Python content locally; results and every content-review finding are recorded in [the disposition](reviews/course-draft-fixes-20261117.md). These implementation checks are not approval receipts. NOT RUN: private author-host suites, native/device/player acceptance and owner approval. **Owner approval is required before any status change or announcement.**

## Regenerating the public drafts

Verified workflow for the 2026-11-17 correction branch: edit the admitted JSON files under each course's `attachments/`, then run `nice -n 10 python3 tools/export_drafts.py`. This repository-owned tool rebuilds `bundle.json`, format-v1 activity wrappers, answer checks, bundle pins and media hashes/sizes using public files only. It never changes review status. There are no other public export outputs.

Format v1 has no structured checkpoint field. The exporter includes checkpoint questions, their 1-based frame numbers, variable names, stack depth when specified, and choices in each trace prompt; reference answers live in the explanation. `expectedTrace` contains readable frame observations. Multiple-choice predictions ask for a choice number and store that number in `expected`; each option has a labelled, indented block so multiline output stays unambiguous. The rich learner attachments retain structured frames and checkpoints for a future player.

After staging explicitly selected new files, `nice -n 10 python3 tools/export_drafts.py --inventory` also refreshes `FILES.json` for the tracked/staged file set (excluding itself). Run the validator and unit tests after regeneration. Source bytes outside the corrected drafts and publication tooling are preserved.
