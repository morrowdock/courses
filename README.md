# Morrowdock courses

Morrowdock is an open learning studio where anyone can learn and teach anything. Creators can submit courses to a catalog that credits them. Content is platform-neutral for iPad, iPhone, Mac and Apple TV; optional activity input metadata declares touch, pointer, keyboard and remote-only support.

**As of 2026-11-14:** Stage 1+2 provides an open course v1 format, a registry, submission/review documentation and Linux CI checks. This is an early preview, not a stable tooling release or a public app launch. The catalog contains only the original synthetic demo, marked **draft**. No course has completed independent AI fact-checks and human approval. App ingestion, hosted course downloads, Apple UI/device acceptance and App Store/public-launch work are pending.

## Format and catalog

[FORMAT.md](docs/FORMAT.md) defines the [JSON Schemas](schema/), versioning, creator credits, provenance, lessons, steps, activities, answer checks and hashed media. The new manifest wraps the existing Swift `CourseBundle` without changing its wire format. Private app compatibility is not asserted. [registry.json](registry.json) contains the one synthetic course; [its manifest](courses/demo/1.0.0/course.json) illustrates all five activity kinds. Remote URLs plus SHA-256 are accepted as draft proposals, with no CI downloads.

## Validate locally

Use Swift 6 and Python 3.12+ on Linux. The scanner installer below targets Linux x64; macOS requires a separately verified Gitleaks 8.24.3 binary on PATH (not provided by this installer):

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
bash tools/install_gitleaks.sh .venv/bin  # Linux x64; version/checksum pinned
python tools/validate.py
python -m unittest discover -s tests -v
```

CI uses a Swift 6 Linux container. It checks all local courses, including changed courses, with schemas, provenance/licence rules, media hashes, registry consistency and the original Swift validator, plus checksum-pinned Gitleaks credential scanning. Maintainers can withdraw and restore catalog entries with a recorded reason while retaining review evidence. `python tools/validate.py --python-only` is a diagnostic when Swift is unavailable; it does **not** replace the full CI gate. Dependency versions, source and hashes are recorded in [THIRD-PARTY.md](THIRD-PARTY.md).

## Submit a course

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [REVIEW.md](docs/REVIEW.md). Create `courses/<id>/<version>/course.json`, declare creator credits and redistribution rights, add a draft registry entry, update [CHANGELOG.md](CHANGELOG.md), sign off every commit and open a PR using the template. The review path is: validator green → two independent AI fact-check files produced outside CI → human maintainer approval → `reviewed`. AI cannot approve or merge. No model API keys belong in CI.

Course content defaults to CC BY-SA 4.0 ([LICENSE](LICENSE)); individual course manifests may explicitly choose CC-BY-4.0 or CC0-1.0. Validation tooling and schemas are Apache-2.0 ([LICENSE-CODE](LICENSE-CODE)); see [NOTICE](NOTICE), [COPYRIGHT.md](COPYRIGHT.md) and [QUALITY.md](QUALITY.md). Names, mascot and logos are reserved ([TRADEMARKS.md](TRADEMARKS.md)). No trademark rights or university endorsements are granted.

Public contact, Code of Conduct concerns and privacy/deletion requests: [hello@morrowdock.app](mailto:hello@morrowdock.app). For vulnerability reporting, see [SECURITY.md](SECURITY.md).

The first owner-authored course drafts are [Git Lab and Code Gym foundations](docs/FIRST-OPEN-COURSES.md): 12 lessons, 29 Git tasks and 96 Code Gym activities, by Collin Craig under CC-BY-SA-4.0. Both remain draft with empty review receipts. Owner approval is required before any status change or announcement.
