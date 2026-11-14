# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.check_changelog import changed_paths, changelog_versions, entries, main, needs_changelog


class ChangelogTests(unittest.TestCase):
    def test_each_protected_directory(self):
        for path in ("courses/a/1.0.0/course.json", "schema/course.schema.json", "tools/check.py"):
            with self.subTest(path=path):
                self.assertTrue(needs_changelog([path]))

    def test_changelog_satisfies_policy(self):
        self.assertFalse(needs_changelog(["tools/check.py", "CHANGELOG.md"],
                                         head_text="## [Unreleased]\n### Added\n- A new course format.\n"))

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
                with patch("tools.check_changelog.changelog_versions", return_value=("", "")):
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


class ParsedChangelogTests(unittest.TestCase):
    baseline = "## [Unreleased]\n### Added\n- Existing feature.\n"
    paths = ["tools/example.py", "CHANGELOG.md"]

    def rejected(self, text):
        self.assertTrue(needs_changelog(self.paths, base_text=self.baseline, head_text=text))

    def test_new_nonempty_entry_passes(self):
        self.assertFalse(needs_changelog(self.paths, base_text=self.baseline,
                                        head_text=self.baseline + "- New regression coverage.\n"))

    def test_arbitrary_added_line_fails(self):
        self.rejected(self.baseline + "An unrelated added line.\n")

    def test_blank_and_empty_bullets_fail(self):
        for addition in ("\n", "- \n", "- ** **\n", "### Fixed\n", "## [1.0.0] - 2026-11-14\n"):
            with self.subTest(addition=addition):
                self.rejected(self.baseline + addition)

    def test_comment_or_fenced_fake_entry_fails(self):
        for addition in ("<!--\n- Fake entry\n-->", "```md\n- Fake entry\n```", "~~~\n- Fake entry\n~~~"):
            self.rejected(self.baseline + addition)

    def test_duplicate_reordered_or_cosmetic_entry_fails(self):
        self.rejected(self.baseline + "- Existing feature.\n")
        self.rejected("## [Unreleased]\n### Fixed\n* **Existing**   feature.\n")

    def test_moving_released_entry_to_unreleased_fails(self):
        old = "## [1.0.0] - 2026-11-14\n### Added\n- Existing feature.\n"
        self.assertTrue(needs_changelog(self.paths, base_text=old, head_text=self.baseline))

    def test_new_entry_outside_unreleased_fails(self):
        self.rejected(self.baseline + "## [1.0.0] - 2026-11-14\n### Fixed\n- New but already released.\n")

    def test_new_file_requires_real_entry(self):
        self.assertTrue(needs_changelog(self.paths, head_text="# Changelog\n## [Unreleased]\n"))
        self.assertFalse(needs_changelog(self.paths, head_text=self.baseline))

    def test_multiline_entry_is_normalized(self):
        self.assertEqual(entries("## [Unreleased]\n### Added\n- New feature\n  with details.\n"),
                         {"new feature with details."})

    def test_unrecognized_category_does_not_count(self):
        self.rejected(self.baseline + "### Random\n- New prose.\n")

    def test_reads_base_head_git_blobs_not_working_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", tmp, *args], text=True).strip()
            git("init", "-q")
            git("config", "user.name", "Synthetic test")
            git("config", "user.email", "synthetic@example.invalid")
            git("config", "commit.gpgsign", "false")
            (root / "CHANGELOG.md").write_text(self.baseline)
            git("add", "CHANGELOG.md")
            git("commit", "-qm", "Synthetic base", "-s")
            base = git("rev-parse", "HEAD")
            updated = self.baseline + "- New entry.\n"
            (root / "CHANGELOG.md").write_text(updated)
            git("add", "CHANGELOG.md")
            git("commit", "-qm", "Synthetic head", "-s")
            head = git("rev-parse", "HEAD")
            (root / "CHANGELOG.md").write_text("uncommitted junk")
            original = subprocess.check_output
            def in_repo(command, **kwargs):
                return original(command, cwd=tmp, **kwargs)
            with patch("tools.check_changelog.subprocess.check_output", side_effect=in_repo):
                self.assertEqual(changelog_versions(base, head), (self.baseline, updated))
