# Open course format v1

Status: public format v1 implementation, 2026-11-14. Compatibility baseline: this repository's `validator/CourseBundle.swift` at `89e7fe9ad42fbff632640e58e4dc36b1146fc7a3`. That validator and the original `demo/` bytes are unchanged. The authored-course concepts requested on 2026-11-14 inform this public design; compatibility with any private app projection is **pending**, not verified. No private app internals or content were inspected or copied.

Morrowdock is an open learning studio where anyone can learn and teach anything. Courses credit their creators. The format is subject-neutral: `level` is descriptive text, prerequisites are statements, and language is a BCP 47-style tag (the syntax check does not validate the IANA subtag registry).

## Package and schema

A local submission lives at `courses/<id>/<version>/course.json`. Its directory contains exactly the manifest, `bundle.json`, declared files under `attachments/`, and referenced AI reports under `reviews/`. Files use safe relative paths; absolute paths, traversal, empty segments, backslashes, percent escapes and symlinks are rejected. Case is significant. Do not submit archives, executable payloads, private URLs, credentials or learner data. Code snippets are text: validation never executes them. This is a source format, not a sandbox or media renderer.

The normative JSON Schemas use Draft 7:

- [course.schema.json](../schema/course.schema.json): manifest and authored activities.
- [bundle.schema.json](../schema/bundle.schema.json): the existing Swift bundle's exact object shape.
- [registry.schema.json](../schema/registry.schema.json): catalog entries and review state.
- [ai-review.schema.json](../schema/ai-review.schema.json): externally produced fact-check records.

The Python semantic checks and existing Swift validator also apply. JSON must be UTF-8 without duplicate keys or non-finite numbers; each JSON document is limited to 8,000,000 bytes. Unknown object fields are rejected. Schema defaults are documentation only and never silently inserted. Every required field, including `licence`, must be present.

## Course manifest

| Field | Meaning |
| --- | --- |
| `format`, `formatVersion` | Exactly `morrowdock-open-course` and integer `1`. |
| `id`, `version` | Stable identifier (`[A-Za-z0-9_-]`, 1–80 characters) and SemVer 2.0.0 course version. |
| `title`, `summary`, `level` | Nonblank text; title is at most 200 characters. |
| `prerequisites` | Array of prerequisite statements, empty when none. |
| `creators` | Nonempty array of `{displayName, url?}`. HTTPS public URLs only; no emails. |
| `licence` | SPDX `CC-BY-SA-4.0` (authoring default), `CC-BY-4.0`, or `CC0-1.0`. |
| `language` | Language tag, such as `en` or `pt-BR`. |
| `bundle` | `{path: "bundle.json", sha256, size}`; size is bytes, SHA-256 is lowercase hex. |
| `sources`, `provenance` | Rights/source declarations and complete per-item mappings. |
| `lessons`, `activities`, `answerChecks`, `media` | Authored structure described below; arrays may be empty except lessons. |
| `review` | `{status, reviewedAt, reviewers, withdrawal?}`; see [REVIEW.md](REVIEW.md). |

### Bundle compatibility

`bundle.json` retains **all** existing required keys: `format`, integer `version`, `course`, `topics`, `materials`, `assignments`, `questions`, `examBlueprint`, `equationSheet`. Even optional content uses an explicit `equationSheet: null`. Do not add creators, review status or SemVer to this object. Its `course.id` and `course.title` must equal the manifest's ID and title.

Topics have `id,title`; materials have `id,title,ref`; assignments have `id,title,topicID,due`; questions have `id,topicID,prompt,choices,answer,explanation,materialID`. `answer` is a zero-based choice index. Each question has 2–8 distinct choices, an existing topic and material. `examBlueprint` retains `questionCount,minutes,points`; it is required for compatibility even when a course has no questions. The Swift validator remains authoritative for bundle semantics and limits. The JSON Schema adds stricter ISO date-time validation to the public submission profile.

Existing HTTPS material references remain supported, without credentials. They are reference links, not downloaded or integrity-verified media. A local `attachments/...` reference must also be in `media`. The legacy Swift **importer** rejects local attachments; passing validation does not imply the app can import this new package.

### Lessons, steps, activities and answers

Each lesson is `{id,title,steps}` with at least one step. Step IDs are unique across the course. Steps are discriminated objects:

- `{id,kind:"reading",materialID}` references a bundle material.
- `{id,kind:"activity",activityID}` references a manifest activity.
- `{id,kind:"question",questionID}` references a bundle question.

Every activity has `id,kind,prompt,explanation`, plus the fields below. Strings and arrays are authored reference answers, never executable grading code.

| Kind | Additional required fields | Check meaning |
| --- | --- | --- |
| `trace` | `code,language,expectedTrace` (nonempty string array) | Ordered expected observations. |
| `prediction` | `code,language,expected` | Expected textual result. |
| `fix` | `code,language,solution` | Reference correction for review; no runtime execution. |
| `parsons` | `blocks,order` | `order` must be a permutation of every zero-based block index. |
| `explanation` | None | Reference explanation for human/self review, no automatic mastery judgment. |

`answerChecks` contains exactly one `{questionID,kind:"choice-index",expectedIndex}` per bundle question. The index must match the bundle's `answer` and fit its choices. This intentionally retains the public multiple-choice model; other question check types require a future format change. Questions, activities, lessons, media and bundle collections have unique IDs within their own namespace.

### Platform-neutral input capabilities

The content format targets iPad, iPhone, Mac and Apple TV without device names, screen-size assumptions or platform-specific APIs in the wire format. An activity may optionally declare:

```json
"inputNeeds": {
  "alternatives": ["touch", "pointer", "keyboard", "remote"],
  "remoteOnlyOK": true
}
```

Each alternative is a **complete independent input method**, not one part of a required combination. `remoteOnlyOK: true` means that the entire activity can be completed using only directional navigation, selection and back controls; `remote` must appear among the alternatives. When false, `remote` must be absent. Omitting `inputNeeds` means capabilities are unspecified, not that every device is supported. Authors must not declare remote-only support for code editing or long reading; use `keyboard` for editing, and keep TV interactions short. The synthetic prediction illustrates remote-only intent; the fix example declares keyboard input.

Clients choose a compatible renderer and explain unsupported input requirements rather than assume touch or a keyboard. A TV can present short quizzes and remote-operated minigames; long reading and code editing should be offered on a compatible device. This metadata does not implement a TV renderer, input focus engine or minigame runtime. Bundle quizzes retain their existing choice-index representation, which clients can render with a remote. Reviewers must verify declared input needs against the complete activity. Device behavior and cross-device compatibility remain pending app acceptance checks.

### Media and provenance

Each media declaration has `id,path,sha256,size,mimeType`. `path` starts with `attachments/`. CI checks the actual SHA-256 and byte count (maximum 100,000,000 per media file), and rejects undeclared files. MIME type is a declared value, not content sniffing or a guarantee of safe rendering. Remote media must be vendored with redistribution rights before inclusion as media.

Each source declares `id,title,origin,rightsHolder,licence,changes` and optional `url,permission`. `origin` is `original`, `adapted` or `generated`. Adapted sources require an HTTPS source URL and a public permission/licensing basis. Keep private permission documents out of the PR. Disclose generated material and its review limitations. Attribution alone is not permission.

`provenance` maps `{item,sources}` to source IDs. Exactly one mapping is required for every `course:<id>`, `topic:<id>`, `material:<id>`, `assignment:<id>`, `question:<id>`, `lesson:<id>`, `step:<id>`, `activity:<id>` and `media:<id>`. Unknown, duplicate or missing items and unused sources fail validation. The containing item's provenance covers its text, answer and explanation. Media inherit the declared source rights and record their own byte hashes. Multiple sources may apply to one item.

The v1 profile accepts only the three declared content licences. A CC-BY-SA-4.0 source requires a CC-BY-SA-4.0 course; CC-BY-4.0 cannot become CC0-1.0. This conservative structural rule does not adjudicate ownership or legal compatibility. Reviewers must assess rights and preserve source attribution. Tooling remains Apache-2.0.

## Registry v1

`registry.json` is `{format:"morrowdock-registry-v1",entries:[...]}`. An entry requires `id,version,creators,licence,status,reviewedAt,reviewers`, with `status` in `draft`, `in-review`, `reviewed`, `withdrawn`. Withdrawn entries also require a matching `withdrawal` record and retain previous review evidence; see [REVIEW.md](REVIEW.md). Each entry has exactly one location:

- `path`: repository-relative `courses/<id>/<version>/course.json`. All identity, creator, licence and review fields must match the manifest. Git pins local source bytes; the manifest pins bundle/media bytes.
- `url` and `sha256`: an HTTPS URL for the manifest bytes and their lowercase SHA-256. No `path` is allowed alongside them. Use an immutable full-commit URL, not a moving tag, where the host supports it.

Identity/version pairs are unique. Every local course version must have one entry. Remote entries are **draft proposals only** (which a maintainer may withdraw and restore as drafts) in this stage; CI does not fetch URLs or claim to verify their bytes. Vendor the package into `courses/` and replace its location with `path` for review. This avoids an untrusted network fetch and makes all evidence reviewable in the PR. Hosted retrieval, digest-checked downloading, archive ingestion and catalog ingestion are pending; a future consumer must fail closed on digest mismatch. The only current entry is the synthetic draft demo.

## Versioning

`formatVersion: 1`, legacy bundle `version: 1`, and course SemVer are separate namespaces. v1 schemas are strict: a change that makes a previously accepted document invalid, adds a field to the wire format, or changes interpretation requires a new format major version and migration guidance. Clarifications and fixes that enforce already documented constraints can update the v1 tooling with a changelog entry and regression tests. Schema files and tooling are versioned by Git commits; no stable tooling release is asserted.

For course SemVer, increment MAJOR for incompatible structure/prerequisites or changed learning contracts, MINOR for compatible additions, and PATCH for corrections that preserve the learning contract. SemVer prerelease/build syntax is accepted. Do not reuse a reviewed identity/version for different content: add a new directory/version and retain previous pins for rollback. Unreviewed draft iterations may reuse their version. Any content change invalidates fact-check digests and requires fresh review, even a typo. Review-only metadata updates retain the content version. Maintainers review version immutability in the PR; CI checks identity uniqueness and review-byte consistency, not historical publication state.

See the [synthetic manifest](../courses/demo/1.0.0/course.json) for all five activity kinds and hashed media. Its `example.invalid` material URL deliberately does not claim a live source.
