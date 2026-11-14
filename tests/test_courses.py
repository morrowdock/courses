# SPDX-License-Identifier: Apache-2.0
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.validate import ROOT, load_json, validate


class CourseTests(unittest.TestCase):
    def test_original_and_open_course(self):
        self.assertEqual(validate(), (3, 4))


class SwiftCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.exe = Path(cls.tmp.name) / "validator"
        subprocess.run(["swiftc", str(ROOT / "validator/CourseBundle.swift"), str(ROOT / "validator/main.swift"),
                        "-o", str(cls.exe)], check=True)

    def setUp(self):
        self.bundle = load_json(ROOT / "demo/bundle.json")

    def rejected(self):
        path = Path(self.tmp.name) / "invalid.json"
        path.write_text(json.dumps(self.bundle))
        # Swift top-level error diagnostics may include a backtrace; suppress expected failures.
        result = subprocess.run([str(self.exe), str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertNotEqual(result.returncode, 0)

    def test_extra_bundle_metadata_rejected(self):
        self.bundle["creators"] = []
        self.rejected()

    def test_semver_cannot_replace_bundle_integer_version(self):
        self.bundle["version"] = "1.0.0"
        self.rejected()

    def test_dangling_question_topic_rejected(self):
        self.bundle["questions"][0]["topicID"] = "unknown"
        self.rejected()

    def test_out_of_range_answer_rejected(self):
        self.bundle["questions"][0]["answer"] = 7
        self.rejected()

    def test_unsafe_material_path_rejected(self):
        self.bundle["materials"][0]["ref"] = "attachments/../secret.txt"
        self.rejected()

    def test_duplicate_question_id_rejected(self):
        self.bundle["questions"].append(self.bundle["questions"][0])
        self.rejected()
