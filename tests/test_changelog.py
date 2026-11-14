# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.check_changelog import changed_paths, main, needs_changelog


class ChangelogTests(unittest.TestCase):
    def test_each_protected_directory(self):
        for path in ("courses/a/1.0.0/course.json", "schema/course.schema.json", "tools/check.py"):
            with self.subTest(path=path):
                self.assertTrue(needs_changelog([path]))

    def test_changelog_satisfies_policy(self):
        self.assertFalse(needs_changelog(["tools/check.py", "CHANGELOG.md"]))

    def test_exact_label_exemption(self):
        self.assertFalse(needs_changelog(["schema/x.json"], ["no-changelog"]))
        self.assertTrue(needs_changelog(["schema/x.json"], ["NO-CHANGELOG"]))

    def test_unrelated_paths(self):
        self.assertFalse(needs_changelog(["README.md", "tests/test_example.py", "mytools/example.py"]))

    def test_rejects_non_sha_arguments(self):
        with self.assertRaises(ValueError):
            changed_paths("--option", "0" * 40)

    def test_cli_reads_event_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            event = Path(tmp) / "event.json"
            event.write_text('{"pull_request":{"labels":[{"name":"no-changelog"}]}}')
            with patch.dict(os.environ, {"GITHUB_EVENT_PATH": str(event)}), patch("tools.check_changelog.changed_paths", return_value=["tools/a.py"]):
                self.assertEqual(main(["a" * 40, "b" * 40]), 0)
                event.write_text('{"pull_request":{"labels":[]}}')
                self.assertEqual(main(["a" * 40, "b" * 40]), 1)

    def test_git_diff_includes_deletions_and_both_rename_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", tmp, *args], text=True).strip()
            git("init", "-q")
            git("config", "user.name", "Synthetic test")
            git("config", "user.email", "synthetic@example.invalid")
            git("config", "commit.gpgsign", "false")
            (root / "tools").mkdir()
            (root / "tools/deleted.py").write_text("synthetic deleted file")
            (root / "tools/renamed.py").write_text("synthetic renamed file")
            git("add", "tools/deleted.py", "tools/renamed.py")
            git("commit", "-qm", "Synthetic base", "-s")
            base = git("rev-parse", "HEAD")
            git("rm", "tools/deleted.py")
            git("mv", "tools/renamed.py", "renamed.py")
            git("commit", "-qm", "Synthetic change", "-s")
            head = git("rev-parse", "HEAD")
            original = subprocess.check_output
            def in_repository(command):
                return original(command, cwd=tmp)
            with patch("tools.check_changelog.subprocess.check_output", side_effect=in_repository):
                paths = changed_paths(base, head)
            self.assertEqual(set(paths), {"tools/deleted.py", "tools/renamed.py", "renamed.py"})
            self.assertTrue(needs_changelog(paths))
