# Third-party inventory

Status: verified source-only dependency declarations, 2026-11-02; binary/transitive release review pending.
No external runtime packages or binary assets are bundled in this candidate. Swift Foundation/XCTest and Apple SDKs are platform build dependencies, not redistributed. Python uses the installed standard library (PSF terms); Actions use checkout (MIT), pinned to 11d5960a326750d5838078e36cf38b85af677262 in CI, fetched by CI rather than vendored. Swift 6 build-container/base-system distribution notices remain a release review item.

validator/CourseBundle.swift is byte-identical (sha256 94e11ba7…83fd18b7) to morrowdock/core Sources/MorrowdockCore/CourseBundle.swift; its source commit is recorded in core's EXTRACTION.json. The other files were newly authored for this repository. Source ownership checked 2026-11-11: the private-repository history of the extracted validator shows only the owner as author; no outside human contributor was found. The owner approved publication on 2026-11-11. The license does not override third-party rights. Excluded: Pyodide/MPL, CheerpJ/custom, Linux/SeaBIOS GPL/LGPL guests, PDFium wheels, NumPy/cryptography/Torch/Pillow extras, models, fonts, SDK binaries and mascot art. Embedded CPython under PSF terms is a proposed permissive Python path, not included here.

## Format v1 validation dependency — 2026-11-14

Status: **verified** wheel metadata, licence text, SHA-256 and normal runtime dependency list on 2026-11-14. `requirements.txt` pins the only added third-party Python runtime dependency; it is installed for validation, not vendored or included in a course.

| Package | Source / artifact | SHA-256 | Licence / dependencies |
| --- | --- | --- | --- |
| fastjsonschema 2.21.2 | [PyPI release](https://pypi.org/project/fastjsonschema/2.21.2/), [upstream source](https://github.com/horejsek/python-fastjsonschema/tree/4f1ed6d9c0462f3522a66f49c8f3dc482300101b); `fastjsonschema-2.21.2-py3-none-any.whl` | `1c797122d0a86c5cace2e54bf4e819c36223b552017172f32c5c024a6b77e463` | BSD-3-Clause; pure Python; no normal runtime dependencies. Optional development extras are not installed. |

The wheel retains its copyright, licence and author notices in its `.dist-info/licenses/` directory. Hash-locked installation allows only this wheel. No new compiled runtime, model, API client, font or binary asset is bundled. CI continues to fetch the previously pinned MIT `actions/checkout` revision and a Swift 6 container; platform/container transitive distribution review remains a release task. JSON Schemas and authored validation code in this repository are Apache-2.0. The earlier source-only inventory above describes the 2026-11-02 baseline; the Python dependency is new in this change.
