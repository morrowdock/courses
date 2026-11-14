# Submission and review

Status: implemented repository checks and documented human review process, 2026-11-14. No course is approved by this implementation. AI factual review, rights review and human approval for the demo are **pending**. App ingestion and public launch remain outside this work.

1. Fork or branch, create a course using [FORMAT.md](FORMAT.md), credit its creators and add its registry entry with `draft`. Submit only content you may redistribute. Sign every commit with your own DCO (`git commit -s`). Use the PR template and update the changelog.
2. Run `python tools/validate.py` and `python -m unittest discover -s tests -v` in the configured environment. CI on Linux runs the unchanged Swift bundle validator, JSON Schemas, per-item provenance/licence compatibility checks, media hashes/sizes, registry and review-record checks. All local courses are checked, including changed courses and courses affected by schema/tool changes. A green check establishes structure and declared byte integrity, not factual correctness or rights.
3. Ask a maintainer to apply `in-review`, and set both manifest and registry status to `in-review`. Produce **two independent AI fact-checks outside CI**, using separate reviewer identities and independent runs. Each reviewer receives the pinned course/source material and independently checks facts, answers, explanations, traces, predictions, fixes, Parsons ordering and source attribution. Do not seed the second review with the first review's conclusions. Different models/providers are encouraged; independence cannot be proved by metadata alone.
4. Commit the two reports as JSON files under the course's `reviews/` directory, visible in the PR diff. Reports must satisfy [ai-review.schema.json](../schema/ai-review.schema.json); each needs reviewer identity, provider, model, distinct run ID, time, scope, item-specific findings with public HTTPS evidence links, limitations and verdict (`pass` or `changes-requested`). Include enough detail for a human to inspect claims; a bare success label is insufficient. Add `{reviewer,path,sha256}` records to `reviewers.aiChecks` in both manifest and registry. No model keys, chat transcripts or private material belong in these files or CI.
5. Resolve findings and regenerate both reports when content changes. A maintainer reviews the actual bytes, factual evidence, accessibility and declared input capabilities (including genuinely remote-only TV interactions), rights/permissions, creator attribution and safety. The maintainer confirms independence and scope, runs CI and leaves an explicit **human GitHub PR approval**. AI cannot approve, merge or award a quality label. Maintainers should configure protected branches to require this CI job and a human review; this change does not configure branch protection.
6. Only after the two passing reports and human approval, the maintainer sets both records to `reviewed`, fills `reviewedAt` (RFC 3339 timestamp) and `reviewers.humanApprover` with `{displayName,approvalUrl}` pointing to that approval. The approval must identify the exact content digest it covers. CI reruns on this metadata change. Require final human approval of the final PR head through branch protection; never auto-merge. The submitted approval URL is an attestation, **not authenticated by the offline validator**. Maintainers must verify that it is a real authorized human approval for this content.

`draft` and `in-review` use `reviewedAt: null`, `humanApprover: null` and zero to two reports. Reports can record unresolved findings. `reviewed` requires exactly two reports with passing verdicts, distinct reviewer names and provider/run pairs, matching course ID/version/content digest, checked no later than the approval time, and a human approval record. The review fields must agree in manifest and registry. These requirements are enforced structurally; a fabricated report can only be rejected by review and repository protections.

## Withdrawal and restoration

Only a **human maintainer** may withdraw or restore an entry, through a reviewed PR. Record the decision and its reason in the PR, including the affected course ID/version and content digest. Withdrawal is a catalog-availability decision, not a deletion or revocation of a valid CC grant. Consumers must exclude `withdrawn` entries from the active catalog.

To withdraw, set both manifest and registry status to `withdrawn` and add matching `withdrawal` records: `{by, reason, at, previousStatus}`. `by` is the maintainer's public display name (no email), `reason` is nonblank public text, `at` is an RFC 3339 timestamp, and `previousStatus` is `draft`, `in-review` or `reviewed`. Keep private takedown details out of the public reason. Retain the existing bundle/media pins, report files, report hashes, `reviewedAt` and human approval record unchanged. A previously reviewed entry must still have its two passing reports and human approval; a draft or in-review entry keeps null approval fields. Schema/semantic checks enforce the shape and digest consistency; maintainers verify authority and preservation against the PR base.

A maintainer may restore unchanged content to its previous status after resolving the withdrawal reason and explicitly approving restoration in the PR. Remove the current `withdrawal` record from manifest and registry together; the withdrawal/restoration reasons and earlier evidence remain in Git/PR history. Preserve all existing review evidence. Restoring unchanged reviewed content does not require new AI reports, but requires a new human restoration decision with a recorded reason.

**Any content digest change requires fresh review**, including corrections, media replacements or changed answers. Never reuse old reports to restore changed content as reviewed. Preserve the withdrawn version and its evidence, submit the changed content as a new version starting at `draft` or `in-review`, and obtain two fresh independent fact-checks plus human approval. Withdrawal and restoration metadata alone do not change the content digest. Evidence in deleted/unsafe content cases remains in reviewed repository history; follow the private takedown process rather than republishing sensitive evidence.

## Pinning review content

Print the report's `contentSha256` with:

```sh
python tools/validate.py --content-digest courses/demo/1.0.0/course.json
```

The digest is SHA-256 of UTF-8 JSON for the manifest **excluding only `review`**, with keys sorted, separators `,` and `:`, non-ASCII characters preserved, no trailing newline and no Unicode normalization (Python `json.dumps(..., sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)`). Bundle and media hashes/sizes are inside this scope. This is the v1 canonicalization algorithm, not a claim of RFC 8785 compatibility. Use the supplied command as the reference implementation. Review metadata is excluded to avoid circular report hashes. The report file's own SHA-256 covers its exact bytes, including whitespace.

A report has this shape (placeholders below are **not** valid evidence):

```json
{
  "format": "morrowdock-ai-review-v1",
  "courseId": "demo",
  "courseVersion": "1.0.0",
  "contentSha256": "<digest from the command>",
  "reviewer": "independent-reviewer-1",
  "provider": "<provider>",
  "model": "<model/version>",
  "runId": "<unique external run identifier>",
  "checkedAt": "2026-11-14T12:00:00Z",
  "verdict": "pass",
  "scope": "<items and facts actually checked>",
  "findings": [{
    "item": "question:one",
    "claim": "<specific claim>",
    "assessment": "<reasoned result>",
    "sources": ["https://example.org/public-evidence"]
  }],
  "limitations": "<uncertainties and checks not performed>"
}
```

Reports in automated unit tests are synthetic fixtures, never real reviews. No report is attached to the demo because no independent fact-check was performed for this PR.

## Labels and changelog

The repository labels are declared in [.github/labels.json](../.github/labels.json): `draft`, `in-review`, `reviewed` and `no-changelog`. Maintainers apply them to issues/PRs and remove obsolete status labels. Labels are workflow signals; they do not automatically change catalog status. Do not infer approval from a label alone.

The PR CI job fails when any added, modified, deleted or renamed path under `courses/`, `schema/` or `tools/` changes without a **new non-empty bullet entry** in `CHANGELOG.md` under `[Unreleased]` and a standard category (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`), unless a maintainer applies `no-changelog`. The check parses merge-base and head Git blobs and compares normalized entry text across all base releases. Blank lines, headings, arbitrary prose, comments, fenced examples, duplicate entries, cosmetic changes and moving an old entry do not count. Label addition/removal reruns the check. Maintainers review the substance of the changelog and exceptions. The check uses the pinned PR base/head merge-base diff; filenames and PR text are not interpolated as shell commands. It needs no model API key or write token and runs on fork PRs through `pull_request`, never `pull_request_target`.

Keep a Changelog entries should describe meaningful content/tooling changes under `Unreleased`. A human maintainer owns release dates and versions. Never auto-publish or merge. Copyright concerns follow [COPYRIGHT.md](../COPYRIGHT.md), including private reporting and delisting; preserve prior safe version pins for rollback.

## Credential scanning

CI installs Gitleaks **8.24.3** using the exact Linux x64 archive SHA-256 pinned in `tools/install_gitleaks.sh`; checksum failure aborts installation. It scans tracked Git history with default rules and fails on detected credentials, with findings redacted. No moving release, model key or secret-scanning service token is used. This is detection, not a guarantee that every secret format is recognized.

`.gitleaks.toml` allowlists only `tests/fixtures/secrets/synthetic-positive.txt`, a clearly marked deterministic fake token fixture. The scanner tests copy it into an ordinary course path and require detection; a normal course must pass. Another fixture filename is not allowlisted. Do not expand the exception to course content or the entire test directory. The full unit suite requires the pinned scanner on PATH or an explicit `GITLEAKS_BIN` path; absence is an error, never a skipped test.
