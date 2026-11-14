# Contributing

Fork → set up Python dependencies and Swift 6 ([README](README.md)) → `python tools/validate.py` and `python -m unittest discover -s tests -v` → PR → CI → two independent external AI fact-check files → human maintainer approval. Follow [FORMAT.md](docs/FORMAT.md) and [REVIEW.md](docs/REVIEW.md). Only a maintainer can mark a course reviewed; merge is manual. App-catalog ingestion remains pending. This is an early preview; focused issues and pull requests are welcome.

Sign every commit with `git commit -s`, certifying the [Developer Certificate of Origin 1.1](DCO) ([source](https://developercertificate.org/)). CI rejects pull-request commits without a `Signed-off-by:` line. Sign-off must match the contributor; do not sign on another person's behalf. Inbound equals outbound: Apache-2.0 tooling/schemas, course content under the manifest’s explicit SPDX licence (CC-BY-SA-4.0 by default; CC-BY-4.0 and CC0-1.0 also accepted). No CLA or assignment. A DCO is an origin attestation, not blanket relicensing permission.

Use synthetic tests only. No keys, private URLs, owner configuration, instructor originals, textbook banks, Canvas exports, personal documents or learner records. Include per-asset sources, hashes, licenses, rights holder and change attribution; attest redistribution rights and employer/university permissions. Identify generated content. Attribution alone is not permission.

Dependencies require exact version/source/hash/license and transitive distribution review. No GPL/AGPL/LGPL/MPL/custom-license runtimes; Pyodide and CheerpJ are excluded. CPython/PSF is a future permissive Python option subject to binary review. Preserve vendor notices. Never auto-merge or auto-publish. AI does not verify rights, award quality labels or merge.

Every merged user-facing change needs a new non-empty Keep a Changelog entry under `[Unreleased]` in this repository’s CHANGELOG.md. CI compares parsed base/head entries for course, schema and tooling changes; arbitrary added lines do not count. A maintainer may apply `no-changelog` for a justified exception. The synthetic-only restriction applies to tests and examples; actual submissions may contain original or appropriately licensed public educational content with per-item provenance. Never include private course material.

Release tags require an appropriate changelog entry and maintainer review; no release/deployment automation is introduced here. Batch releases rather than publishing each change.
