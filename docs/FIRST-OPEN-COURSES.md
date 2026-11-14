# First open courses: draft import

Status: proposed public courses; verified export/structure checks; human review pending.
Checked: 2026-11-14 UTC.
Public baseline: `89e7fe9ad42fbff632640e58e4dc36b1146fc7a3`.
Source baseline: `cc40e0a6315a9f86d21496f268b34aa8547786d3` (owner-authorized private source).

| Course | Manifest | Lessons | Included tasks/activities | Whole learning items excluded |
| --- | --- | --- | --- | --- |
| Git Lab | [manifest](../git-lab-v1/manifest.json) | 6 | 29 tasks | 1 exercise with an unresolved-origin password-like string; 1 export-withheld capstone |
| Code Gym foundations | [manifest](../code-gym-foundations-v1/manifest.json) | 6 | 96 activities | 0 |

Creator: Collin Craig (display name only). Both versions are `1.0.0-draft`, language `en`, licence `CC-BY-SA-4.0`, status `draft`. AI-written content requires human review. See the complete [Git Lab](provenance/git-lab-v1.md) and [Code Gym](provenance/code-gym-foundations-v1.md) inventories and exclusions. Attribution and redistribution use the existing root LICENSE; this import changes no trademark grant.

## What is usable today

Each `bundle.json` is a strict CourseBundle v1 index with six topics, six material references and twelve already learner-visible multiple-choice checks. Check prompts include their source code/command context. No new answer key is inferred. The 30-minute blueprint is a compatibility placeholder, not an authored examination or assessment claim; no assignments, dates or learner records are invented.

`attachments/` holds the richer learner projection. Git uses one course JSON; Code Gym uses a manifest and six lesson JSONs. JSON is indented for review without changing admitted values. The only content exclusion beyond the private exporter is Git task `git-course-reset-v1.g1`. Stable identities, hints, goals, frames and allowed runtime-free checking fields are preserved. These files are reading/review resources; public repo tooling does not execute them.

**Current importer limitation:** the extracted `CourseBundleImporter` rejects local attachments. Passing `CourseBundle.decode` does not establish that these rich courses can be imported or played in the public app. Git needs its virtual-shell player; Code Gym needs its recorded-frame player. No renderer, simulator or end-to-end player acceptance is claimed. Follow-on references to other courses are retained source text, not claims that those courses are available publicly.

## Reproducible conversion boundary

At the source baseline above, call `project_git(course_dir)` from `native-study/scripts/export_courses.py` for `content/git-lab/course-v1`, then exclude the task with ID `git-course-reset-v1.g1`. Call `build_code_gym(content_dir)` for `content/code-gym/foundations-v1`. Compare decoded JSON values with the public attachments; never copy the private course tree or the exporter wholesale. Source README, tools, tests, author metadata and Git capstone do not enter this repository. The provenance ledgers identify admitted units and withheld subtrees with hashes without disclosing withheld values.

The public CourseBundle maps lesson IDs/titles into topics and points materials to the appropriate attachment. Git maps its two learner questions per lesson and their indexed `why` feedback. Code Gym maps only `predict` activities with choice answers, incorporating their code into the prompt and the correct choice's reaction into the explanation. Other activity kinds remain in the projection.

Per-asset provenance pins every course file except `provenance.json` itself. Manifest asset hashes pin the bundle and all projection files. Registry `sha256` pins `bundle.json`; `manifestSHA256` pins the manifest and transitively the rich assets. This is a provisional local draft entry, **not a remotely installable immutable release receipt**.

## Migration when format v1 lands

`git ls-remote` at task start found `origin/main` but no `format-v1-and-review-20261114` branch. This branch therefore uses the existing CourseBundle schema, unchanged. Its supplemental manifests and registry entries are deliberately provisional; they do not claim compatibility with the parallel format/review proposal.

Before integration with that proposal:

1. Reconcile directory layout, IDs, manifests, creators/licence fields, registry digest scope and schema identifiers with the landed format; regenerate every affected hash.
2. Choose how the richer family projections and local material references are represented. Preserve the learner export boundary; never restore private answer/reference fields to satisfy a schema without a reviewed format rule.
3. Replace the draft-only local registry checks in `tools/validate.py` with the shared registry/review validator. Add the final immutable public commit/URL and compatibility metadata through that pipeline; do not fabricate a self-referential commit pin.
4. Run the landed validator, review pipeline and real player tests. Remove the compatibility-only exam blueprint if the richer schema no longer requires it.
5. Obtain human provenance and factual review at the final exact bytes. **Owner approval required before status in-review/reviewed and before any announcement.** No automatic promotion, merge or announcement is authorized by this draft.

## Validation scope

Run `python3 tools/validate.py` and `python3 -m unittest discover -s tests -v` with Swift 6 and Python 3.12. The suite checks all three bundles (including the existing synthetic demo), asset/registry integrity, export answer boundaries, counts and rejection of corruption, extra files and premature promotion.

The PR records actual run results. Private author-host replay/parity tests, Python trace regeneration, native UI/device tests, future format-v1 pipeline, independent legal/factual review and owner approval are not covered by these public structural checks.
