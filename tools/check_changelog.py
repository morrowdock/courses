# SPDX-License-Identifier: Apache-2.0
"""Require a changelog entry for course/schema/tool changes in a PR."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def needs_changelog(paths, labels=()):
    return (any(path.startswith(("courses/", "schema/", "tools/")) for path in paths)
            and "CHANGELOG.md" not in paths and "no-changelog" not in labels)


def changed_paths(base, head):
    if any(not re.fullmatch(r"[0-9a-fA-F]{40}", sha) for sha in (base, head)):
        raise ValueError("full base and head commit SHAs required")
    # No rename detection: both the source and destination must trigger the gate.
    result = subprocess.check_output(["git", "diff", "--name-only", "--no-renames", "-z", base + "..." + head])
    return [path.decode("utf-8") for path in result.split(b"\0") if path]


def main(args):
    if len(args) != 2:
        print("Usage: check_changelog.py BASE_SHA HEAD_SHA", file=sys.stderr)
        return 2
    try:
        event_path = os.environ.get("GITHUB_EVENT_PATH")
        event = json.loads(Path(event_path).read_text()) if event_path else {}
        labels = [label["name"] for label in event.get("pull_request", {}).get("labels", [])]
        if needs_changelog(changed_paths(*args), labels):
            print("Change CHANGELOG.md or ask a maintainer for the no-changelog label.", file=sys.stderr)
            return 1
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Changelog check failed: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
