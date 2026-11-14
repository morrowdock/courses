# Changelog

All notable changes to this project are documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Course versions use [Semantic Versioning](https://semver.org/spec/v2.0.0.html); format versioning is described in [FORMAT.md](docs/FORMAT.md).

## [Unreleased]

Implementation work dated 2026-11-14.

### Added

- Open course v1 manifest and JSON Schemas for authored lessons, steps, five activity kinds, answer checks, hashed media and per-item provenance, preserving the existing Swift bundle format.
- Optional platform-neutral activity input needs for touch, pointer, keyboard and remote-only use across iPad, iPhone, Mac and Apple TV.
- Registry v1 schema with creator credits, explicit content licences, pinned locations and draft/in-review/reviewed records; only the synthetic draft demo is listed.
- Submission template, review/status labels and a review process requiring two independent external AI fact-check files followed by human maintainer approval.
- Linux CI schema, provenance/licence, media-integrity, registry/review and regression checks, plus a PR changelog gate with a maintainer `no-changelog` exception.
- Format, review, versioning and dependency documentation and regression tests. No app ingestion, independent factual approval or public launch is claimed.

### Fixed

- Support maintainer withdrawal/restoration with a recorded reason and preserved review evidence; require fresh review whenever the course content digest changes.
- Reject credentials in CI using checksum-pinned Gitleaks 8.24.3, with clearly synthetic detection/clean-course regression fixtures.
- Require a new non-empty parsed Unreleased changelog entry rather than accepting any change to CHANGELOG.md.
- Keep existing changelog entries: editing an old entry no longer counts as a new one.
