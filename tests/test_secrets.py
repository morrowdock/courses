# SPDX-License-Identifier: Apache-2.0
"""Synthetic scanner tests; no real credentials or network calls."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.validate import ROOT


class SecretScannerTests(unittest.TestCase):
    def scan(self, directory, config=True):
        scanner = os.environ.get("GITLEAKS_BIN", "gitleaks")
        # Missing scanner is an error, not a skipped credential gate.
        command = [scanner, "dir", str(directory), "--redact", "--no-banner", "--exit-code", "1"]
        if config:
            command.extend(["--config", str(ROOT / ".gitleaks.toml")])
        with tempfile.TemporaryDirectory() as reports:
            report = Path(reports) / "report.json"
            command.extend(["--report-format", "json", "--report-path", str(report)])
            result = subprocess.run(command, capture_output=True, text=True)
            findings = json.loads(report.read_text()) if report.exists() else []
            return result, findings

    def test_synthetic_token_in_course_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "courses" / "synthetic"
            target.mkdir(parents=True)
            shutil.copyfile(ROOT / "tests/fixtures/secrets/synthetic-positive.txt", target / "course.txt")
            result, findings = self.scan(Path(tmp))
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("github-pat", {finding["RuleID"] for finding in findings})

    def test_normal_course_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(ROOT / "courses/demo", Path(tmp) / "courses/demo")
            result, findings = self.scan(Path(tmp))
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_only_named_synthetic_fixture_is_allowlisted(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "tests/fixtures/secrets"
            target.mkdir(parents=True)
            shutil.copyfile(ROOT / "tests/fixtures/secrets/synthetic-positive.txt", target / "synthetic-positive.txt")
            result, findings = self.scan(Path(tmp))
            self.assertEqual(result.returncode, 0, result.stderr)
            (target / "synthetic-positive.txt").rename(target / "not-allowlisted.txt")
            self.assertEqual(self.scan(Path(tmp))[0].returncode, 1)
