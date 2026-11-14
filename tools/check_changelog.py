# SPDX-License-Identifier: Apache-2.0
"""Require a new non-empty Keep a Changelog entry for course/schema/tool PRs."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CATEGORIES = {"added", "changed", "deprecated", "removed", "fixed", "security"}


def entries(document, *, unreleased_only=False):
    """Parse top-level bullets within release/category sections, ignoring comments/code.

    Compare normalized entry text across all base releases, so moving/reordering an
    old entry or changing its category/formatting cannot manufacture a new entry.
    """
    document = re.sub(r"<!--.*?(?:-->|\Z)", "", document, flags=re.S)
    result = set()
    release = None
    category = None
    bullet = []
    fence = None

    def finish():
        normalized = " ".join(re.sub(r"[*_`~]", "", " ".join(bullet)).split()).casefold()
        if any(character.isalnum() for character in normalized):
            result.add(normalized)
        bullet.clear()

    for line in document.splitlines():
        fenced = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fenced:
            finish()
            marker = fenced[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            finish()
            depth, title = len(heading[1]), heading[2]
            if depth <= 2:
                version = re.fullmatch(r"\[([^]]+)\](?:\s+-\s+\d{4}-\d{2}-\d{2})?", title)
                release = version[1].casefold() if depth == 2 and version else None
                category = None
            else:
                category = title.casefold() if depth == 3 and title.casefold() in CATEGORIES else None
            continue
        eligible = release is not None and category is not None and (not unreleased_only or release == "unreleased")
        if not eligible:
            continue
        item = re.match(r"^[-*+]\s+(.*)$", line)
        if item:
            finish()
            bullet.append(item[1])
        elif bullet and re.match(r"^ {2,}\S", line):
            bullet.append(line.strip())
        else:
            finish()
    finish()
    return result


def needs_changelog(paths, labels=(), *, base_text="", head_text=""):
    protected = any(path.startswith(("courses/", "schema/", "tools/")) for path in paths)
    if not protected or "no-changelog" in labels:
        return False
    new_entries = entries(head_text, unreleased_only=True) - entries(base_text)
    return "CHANGELOG.md" not in paths or not new_entries


def validate_shas(base, head):
    if any(not re.fullmatch(r"[0-9a-fA-F]{40}", sha) for sha in (base, head)):
        raise ValueError("full base and head commit SHAs required")


def changed_paths(base, head):
    validate_shas(base, head)
    # No rename detection: both source and destination must trigger the gate.
    result = subprocess.check_output(["git", "diff", "--name-only", "--no-renames", "-z", base + "..." + head])
    return [path.decode("utf-8") for path in result.split(b"\0") if path]


def changelog_at(commit):
    # Distinguish an absent file from unreadable/corrupt Git state. No working-tree reads.
    names = subprocess.check_output(["git", "ls-tree", "--name-only", commit, "--", "CHANGELOG.md"], text=True)
    if not names.strip():
        return ""
    return subprocess.check_output(["git", "show", commit + ":CHANGELOG.md"], text=True)


def changelog_versions(base, head):
    validate_shas(base, head)
    ancestor = subprocess.check_output(["git", "merge-base", base, head], text=True).strip()
    return changelog_at(ancestor), changelog_at(head)


def main(args):
    if len(args) != 2:
        print("Usage: check_changelog.py BASE_SHA HEAD_SHA", file=sys.stderr)
        return 2
    try:
        event_path = os.environ.get("GITHUB_EVENT_PATH")
        event = json.loads(Path(event_path).read_text()) if event_path else {}
        labels = [label["name"] for label in event.get("pull_request", {}).get("labels", [])]
        paths = changed_paths(*args)
        if any(path.startswith(("courses/", "schema/", "tools/")) for path in paths) and "no-changelog" not in labels:
            base_text, head_text = changelog_versions(*args)
            if needs_changelog(paths, labels, base_text=base_text, head_text=head_text):
                print("Add a NEW non-empty CHANGELOG.md bullet under [Unreleased] and a standard category, "
                      "or ask a maintainer for no-changelog.", file=sys.stderr)
                return 1
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Changelog check failed: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
