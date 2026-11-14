# SPDX-License-Identifier: Apache-2.0
"""Synthetic format, provenance, byte-integrity and review regression tests."""
import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.validate import (ROOT, check_course, check_registry, check_schema, content_digest,
                            digest, load_json, safe_file, validate)


class FormatTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / "courses", self.root / "courses")
        shutil.copytree(ROOT / "demo", self.root / "demo")
        shutil.copyfile(ROOT / "registry.json", self.root / "registry.json")
        self.path = self.root / "courses/demo/1.0.0/course.json"
        self.course = load_json(self.path)

    def save(self):
        self.path.write_text(json.dumps(self.course, indent=2) + "\n")

    def check(self):
        self.save()
        return check_course(self.path)

    def reject(self, message=None):
        with self.assertRaisesRegex(ValueError, message or "."):
            self.check()

    def registry(self):
        return load_json(self.root / "registry.json")

    def check_registry_value(self, registry):
        (self.root / "registry.json").write_text(json.dumps(registry))
        return check_registry(self.root, {"courses/demo/1.0.0/course.json": self.course})

    def reviewed(self):
        """Fabricated test evidence only; never write to the repository fixture."""
        reports = []
        (self.path.parent / "reviews").mkdir(exist_ok=True)
        for i in (1, 2):
            receipt = {"format": "morrowdock-ai-review-v1", "courseId": "demo", "courseVersion": "1.0.0",
                       "contentSha256": content_digest(self.course), "reviewer": f"synthetic-{i}",
                       "provider": "test-provider", "model": "test-model", "runId": f"test-run-{i}",
                       "checkedAt": "2026-11-14T12:00:00Z", "verdict": "pass", "scope": "Synthetic test only",
                       "findings": [{"item": "question:one", "claim": "Synthetic claim",
                                     "assessment": "Synthetic assessment", "sources": ["https://example.invalid/evidence"]}],
                       "limitations": "Not a real fact-check"}
            path = self.path.parent / f"reviews/ai-{i}.json"
            path.write_text(json.dumps(receipt))
            reports.append({"reviewer": receipt["reviewer"], "path": f"reviews/ai-{i}.json", "sha256": digest(path)})
        self.course["review"] = {"status": "reviewed", "reviewedAt": "2026-11-14T13:00:00Z",
                                 "reviewers": {"aiChecks": reports, "humanApprover": {
                                     "displayName": "Synthetic human", "approvalUrl": "https://example.invalid/approval"}}}

    def edit_receipt(self, index, field, value):
        check = self.course["review"]["reviewers"]["aiChecks"][index]
        path = self.path.parent / check["path"]
        receipt = load_json(path)
        receipt[field] = value
        path.write_text(json.dumps(receipt))
        check["sha256"] = digest(path)

    def test_complete_repository_python_checks(self):
        self.assertEqual(validate(self.root, swift=False), (1, 2))

    def test_all_schema_documents_compile(self):
        from tools.validate import schema_validator
        for name in ("course", "bundle", "registry", "ai-review"):
            with self.subTest(schema=name):
                self.assertTrue(callable(schema_validator(name)))

    def test_all_required_manifest_fields(self):
        for key in self.course:
            with self.subTest(key=key):
                value = copy.deepcopy(self.course)
                del value[key]
                with self.assertRaises(ValueError):
                    check_schema("course", value)

    def test_unknown_manifest_field(self):
        self.course["privateState"] = {}
        self.reject()

    def test_semver_valid(self):
        for version in ("1.0.0", "0.1.0-alpha.1", "2.3.4+build.9", "1.0.0-0", "1.0.0-0a"):
            with self.subTest(version=version):
                self.course["version"] = version
                self.check()

    def test_semver_build_metadata_in_registry_path(self):
        version = "1.0.0+build.1"
        new_directory = self.path.parent.with_name(version)
        self.path.parent.rename(new_directory)
        self.path = new_directory / "course.json"
        self.course["version"] = version
        self.save()
        registry = self.registry()
        registry["entries"][0].update(version=version, path=f"courses/demo/{version}/course.json")
        (self.root / "registry.json").write_text(json.dumps(registry))
        self.assertEqual(validate(self.root, swift=False), (1, 2))

    def test_semver_invalid(self):
        for version in ("1", "v1.0.0", "01.0.0", "1.0.0-01", "1.0.0+", "1.2.3\n", "1.2.3-"):
            with self.subTest(version=version):
                self.course["version"] = version
                self.reject()

    def test_format_version_integer(self):
        self.course["formatVersion"] = True
        self.reject()

    def test_language_syntax(self):
        for language in ("en", "zh-Hant-TW", "pt-BR"):
            self.course["language"] = language
            self.check()
        self.course["language"] = "English language"
        self.reject()

    def test_creators_required_and_no_email_field(self):
        self.course["creators"] = []
        self.reject()
        self.course["creators"] = [{"displayName": "Example", "email": "fake@example.invalid"}]
        self.reject()
        self.course["creators"] = [{"displayName": "fake@example.invalid"}]
        self.reject()

    def test_creator_url_https_without_credentials(self):
        for url in ("http://example.invalid", "https://user:password@example.invalid", "https://example.invalid\\oops", "https://example.invalid:bad"):
            self.course["creators"][0]["url"] = url
            self.reject()

    def test_nonblank_metadata(self):
        self.course["summary"] = "   "
        self.reject()

    def test_supported_licences(self):
        for licence in ("CC-BY-SA-4.0", "CC-BY-4.0", "CC0-1.0"):
            self.course["licence"] = licence
            for source in self.course["sources"]:
                source["licence"] = licence
            self.check()

    def test_unsupported_licence(self):
        self.course["licence"] = "All-rights-reserved"
        self.reject()

    def test_missing_licence_not_defaulted(self):
        del self.course["licence"]
        self.reject()
        self.assertNotIn("licence", self.course)

    def test_incompatible_source_licence(self):
        self.course["licence"] = "CC0-1.0"
        self.reject("incompatible source licence")

    def test_adaptation_requires_permission_and_url(self):
        self.course["sources"][0]["origin"] = "adapted"
        self.reject("permission")
        self.course["sources"][0].update(url="https://example.invalid/source", permission="Synthetic permission basis")
        self.check()

    def test_missing_provenance_item(self):
        self.course["provenance"].pop()
        self.reject("coverage")

    def test_unknown_provenance_item(self):
        self.course["provenance"][0]["item"] = "course:unknown"
        self.reject("coverage")

    def test_duplicate_provenance(self):
        self.course["provenance"].append(self.course["provenance"][0])
        self.reject("duplicate")

    def test_unknown_source(self):
        self.course["provenance"][0]["sources"] = ["unknown"]
        self.reject("unknown provenance source")

    def test_duplicate_source(self):
        self.course["sources"].append(self.course["sources"][0])
        self.reject("duplicate")

    def test_unused_source(self):
        other = {**self.course["sources"][0], "id": "unused"}
        self.course["sources"].append(other)
        self.reject("unused")

    def test_dangling_step_reference(self):
        self.course["lessons"][0]["steps"][0]["materialID"] = "missing"
        self.reject("dangling")

    def test_duplicate_steps(self):
        self.course["lessons"][0]["steps"].append(self.course["lessons"][0]["steps"][0])
        self.reject("duplicate steps")

    def test_each_activity_shape_rejects_unknown_fields(self):
        for index in range(5):
            self.course["activities"][index]["unknown"] = "value"
            self.reject()
            del self.course["activities"][index]["unknown"]

    def test_optional_platform_neutral_input_needs(self):
        for activity in self.course["activities"]:
            activity.pop("inputNeeds", None)
        self.check()
        for method in ("touch", "pointer", "keyboard", "remote"):
            self.course["activities"][0]["inputNeeds"] = {"alternatives": [method], "remoteOnlyOK": method == "remote"}
            self.check()

    def test_input_needs_reject_unknown_or_duplicate_methods(self):
        for methods in (["gamepad"], ["remote", "remote"], []):
            self.course["activities"][0]["inputNeeds"] = {"alternatives": methods, "remoteOnlyOK": False}
            self.reject()

    def test_remote_only_metadata_must_agree(self):
        for methods, remote in ((["keyboard"], True), (["remote"], False)):
            self.course["activities"][0]["inputNeeds"] = {"alternatives": methods, "remoteOnlyOK": remote}
            self.reject("remote-only")

    def test_parsons_order_permutation(self):
        for order in ([0, 0], [0, 2], [0], [0, 1, 2]):
            self.course["activities"][3]["order"] = order
            self.reject()

    def test_answer_check_coverage(self):
        self.course["answerChecks"] = []
        self.reject("coverage")

    def test_answer_check_mismatch(self):
        self.course["answerChecks"][0]["expectedIndex"] = 1
        self.reject("mismatch")

    def test_bundle_hash_and_size(self):
        for field, value in (("sha256", "0" * 64), ("size", 1)):
            old = self.course["bundle"][field]
            self.course["bundle"][field] = value
            self.reject("mismatch")
            self.course["bundle"][field] = old

    def test_bundle_unknown_field(self):
        bundle = load_json(self.path.parent / "bundle.json")
        bundle["creators"] = []
        with self.assertRaises(ValueError):
            check_schema("bundle", bundle)

    def test_bundle_shape_matches_legacy(self):
        check_schema("bundle", load_json(ROOT / "demo/bundle.json"))
        self.assertEqual((self.path.parent / "bundle.json").read_bytes(), (ROOT / "demo/bundle.json").read_bytes())

    def test_media_hash_and_size(self):
        for field, value in (("sha256", "0" * 64), ("size", 1)):
            old = self.course["media"][0][field]
            self.course["media"][0][field] = value
            self.reject("mismatch")
            self.course["media"][0][field] = old

    def test_media_byte_tampering(self):
        (self.path.parent / self.course["media"][0]["path"]).write_bytes(b"unexpected")
        self.reject("mismatch")

    def test_missing_media(self):
        (self.path.parent / self.course["media"][0]["path"]).unlink()
        self.reject("missing file")

    def test_unlisted_file(self):
        (self.path.parent / "extra.txt").write_text("synthetic")
        self.reject("unlisted")

    def test_orphan_course_file(self):
        (self.root / "courses/orphan.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "orphan"):
            validate(self.root, swift=False)

    def test_path_traversal(self):
        for path in ("../bundle.json", "attachments/../bundle.json", "/absolute", "attachments//file", "attachments/%2e%2e/file", "attachments/./file", "attachments\\file"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_file(self.path.parent, path)

    def test_symlink_media(self):
        media = self.path.parent / self.course["media"][0]["path"]
        media.unlink()
        media.symlink_to(self.path.parent / "bundle.json")
        self.reject("symlink")

    def test_symlink_course_directory(self):
        (self.root / "courses/linked").symlink_to(self.path.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            validate(self.root, swift=False)

    def test_duplicate_json_keys(self):
        self.path.write_text('{"id":"one","id":"two"}')
        with self.assertRaisesRegex(ValueError, "duplicate JSON"):
            load_json(self.path)

    def test_non_finite_json(self):
        self.path.write_text('{"value":NaN}')
        with self.assertRaisesRegex(ValueError, "invalid JSON number"):
            load_json(self.path)

    def test_reviewed_requires_evidence_and_human(self):
        self.course["review"]["status"] = "reviewed"
        self.reject()

    def test_synthetic_complete_review_record(self):
        self.reviewed()
        self.check()

    def test_in_review_with_reports_without_human(self):
        self.reviewed()
        self.course["review"].update(status="in-review", reviewedAt=None)
        self.course["review"]["reviewers"]["humanApprover"] = None
        self.check()

    def test_draft_cannot_claim_approval(self):
        self.reviewed()
        self.course["review"]["status"] = "draft"
        self.reject()

    def test_stale_review(self):
        self.reviewed()
        self.course["summary"] += " Changed."
        self.reject("stale")

    def test_review_digest_excludes_metadata_only(self):
        before = content_digest(self.course)
        self.course["review"]["status"] = "in-review"
        self.assertEqual(before, content_digest(self.course))
        self.course["bundle"]["sha256"] = "0" * 64
        self.assertNotEqual(before, content_digest(self.course))

    def test_report_hash_tampering(self):
        self.reviewed()
        report = self.path.parent / "reviews/ai-1.json"
        report.write_text(report.read_text() + "\n")
        self.reject("hash")

    def test_report_identity(self):
        self.reviewed()
        self.edit_receipt(0, "courseVersion", "2.0.0")
        self.reject("identity/version")

    def test_independent_runs_required(self):
        self.reviewed()
        self.edit_receipt(1, "runId", "test-run-1")
        self.reject("independent")

    def test_independent_names_required(self):
        self.reviewed()
        checks = self.course["review"]["reviewers"]["aiChecks"]
        checks[1]["reviewer"] = checks[0]["reviewer"]
        self.reject("duplicate AI reviewer")

    def test_failed_fact_check_blocks_reviewed(self):
        self.reviewed()
        self.edit_receipt(0, "verdict", "changes-requested")
        self.reject("passing")

    def test_approval_must_follow_fact_checks(self):
        self.reviewed()
        self.course["review"]["reviewedAt"] = "2026-11-14T06:00:00-05:00"
        self.reject("predates")

    def test_unknown_finding_item(self):
        self.reviewed()
        self.edit_receipt(0, "findings", [{"item": "question:missing", "claim": "Test", "assessment": "Test", "sources": ["https://example.invalid"]}])
        self.reject("unknown reviewed item")

    def test_registry_duplicate(self):
        registry = self.registry()
        registry["entries"].append(registry["entries"][0])
        with self.assertRaisesRegex(ValueError, "duplicate registry"):
            self.check_registry_value(registry)

    def test_registry_metadata_mismatches(self):
        for field, value in (("id", "other"), ("version", "9.0.0"), ("creators", [{"displayName": "Other"}]),
                             ("licence", "CC0-1.0"), ("status", "in-review")):
            registry = self.registry()
            registry["entries"][0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "mismatch"):
                self.check_registry_value(registry)

    def test_registry_missing_local_entry(self):
        registry = self.registry()
        registry["entries"] = []
        with self.assertRaisesRegex(ValueError, "every local course"):
            self.check_registry_value(registry)

    def test_registry_missing_file(self):
        registry = self.registry()
        registry["entries"][0]["path"] = "courses/missing/1.0.0/course.json"
        with self.assertRaisesRegex(ValueError, "missing file"):
            self.check_registry_value(registry)

    def test_registry_location_exclusive(self):
        registry = self.registry()
        registry["entries"][0].update(url="https://example.invalid/course.json", sha256="0" * 64)
        with self.assertRaises(ValueError):
            self.check_registry_value(registry)

    def test_registry_remote_digest_required(self):
        registry = self.registry()
        entry = registry["entries"][0]
        del entry["path"]
        entry["url"] = "https://example.invalid/course.json"
        with self.assertRaises(ValueError):
            check_schema("registry", registry)

    def test_registry_remote_draft_no_network(self):
        registry = self.registry()
        remote = copy.deepcopy(registry["entries"][0])
        del remote["path"]
        remote.update(id="remote", url="https://example.invalid/course.json", sha256="a" * 64)
        registry["entries"].append(remote)
        self.check_registry_value(registry)
        remote["status"] = "in-review"
        with self.assertRaisesRegex(ValueError, "remote entries remain draft"):
            self.check_registry_value(registry)


if __name__ == "__main__":
    unittest.main()
