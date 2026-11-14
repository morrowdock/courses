# SPDX-License-Identifier: Apache-2.0
"""Offline format, registry, provenance, review and byte-integrity validation."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlsplit

import fastjsonschema

ROOT = Path(__file__).resolve().parents[1]
MAX_JSON = 8_000_000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path):
    require(path.stat().st_size <= MAX_JSON, f"JSON exceeds {MAX_JSON} bytes: {path}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs,
                      parse_constant=lambda value: require(False, f"invalid JSON number: {value}"))


@lru_cache(maxsize=None)
def schema_validator(name):
    # Schemas are repository-owned; course documents cannot select a schema or fetch URLs.
    return fastjsonschema.compile(load_json(ROOT / "schema" / f"{name}.schema.json"), use_default=False)


def check_schema(name, value):
    schema_validator(name)(value)


def safe_file(root, relative):
    require(isinstance(relative, str) and re.fullmatch(r"[A-Za-z0-9_-][A-Za-z0-9_./+-]*", relative),
            f"unsafe relative path: {relative}")
    require(all(part not in ("", ".", "..") for part in relative.split("/")), f"unsafe path: {relative}")
    current = root
    for part in relative.split("/"):
        current = current / part
        require(not current.is_symlink(), f"symlink forbidden: {current}")
    require(current.is_file(), f"missing file: {current}")
    require(current.resolve().is_relative_to(root.resolve()), f"path escapes root: {relative}")
    return current


def check_url(url):
    parsed = urlsplit(url)
    require(parsed.scheme == "https" and parsed.hostname and not parsed.username and not parsed.password,
            f"HTTPS URL without credentials required: {url}")
    require(not any(c.isspace() for c in url) and "\\" not in url, "unsafe HTTPS URL")
    try:
        parsed.port
    except ValueError as error:
        raise ValueError("invalid HTTPS port") from error


def check_urls(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in ("url", "approvalUrl"):
                check_url(child)
            check_urls(child)
    elif isinstance(value, list):
        for child in value:
            check_urls(child)


def digest(path):
    sha = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(chunk)
    return sha.hexdigest()


def checked_asset(root, asset):
    path = safe_file(root, asset["path"])
    require(path.stat().st_size == asset["size"], f"size mismatch: {path}")
    require(digest(path) == asset["sha256"], f"sha256 mismatch: {path}")
    return path


def unique(rows, field, label):
    values = [row[field] for row in rows]
    require(len(set(values)) == len(values), f"duplicate {label}")
    return set(values)


def content_digest(course):
    """Review scope excludes only mutable review metadata; all content pins remain."""
    payload = {key: value for key, value in course.items() if key != "review"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def check_review(root, course):
    review = course["review"]
    checks = review["reviewers"]["aiChecks"]
    unique(checks, "reviewer", "AI reviewer identity")
    unique(checks, "path", "AI review file")
    run_ids = set()
    paths = set()
    for check in checks:
        require(check["path"].startswith("reviews/") and check["path"].endswith(".json"),
                "AI review files must be reviews/*.json")
        path = safe_file(root, check["path"])
        require(digest(path) == check["sha256"], "AI review file hash mismatch")
        receipt = load_json(path)
        check_schema("ai-review", receipt)
        require(receipt["reviewer"] == check["reviewer"], "AI reviewer mismatch")
        require(receipt["courseId"] == course["id"] and receipt["courseVersion"] == course["version"],
                "AI review identity/version mismatch")
        require(receipt["contentSha256"] == content_digest(course), "stale AI review content digest")
        run = (receipt["provider"], receipt["runId"])
        require(run not in run_ids, "AI checks must come from independent runs")
        run_ids.add(run)
        for finding in receipt["findings"]:
            require(finding["item"] in {p["item"] for p in course["provenance"]}, "unknown reviewed item")
            for url in finding["sources"]:
                check_url(url)
        if review["status"] == "reviewed":
            require(receipt["verdict"] == "pass", "reviewed requires two passing AI checks")
            require(datetime.fromisoformat(receipt["checkedAt"].replace("Z", "+00:00"))
                    <= datetime.fromisoformat(review["reviewedAt"].replace("Z", "+00:00")),
                    "human approval predates AI check")
        paths.add(check["path"])
    return paths


def check_course(manifest):
    root = manifest.parent
    require(not root.is_symlink() and not manifest.is_symlink(), "symlink course forbidden")
    course = load_json(manifest)
    check_schema("course", course)
    check_urls(course)
    bundle_path = checked_asset(root, course["bundle"])
    bundle = load_json(bundle_path)
    check_schema("bundle", bundle)
    require(bundle["course"] == {"id": course["id"], "title": course["title"]}, "bundle identity/title mismatch")
    expected_items = {"course:" + course["id"]}
    sets = {}
    for collection, singular in (("topics", "topic"), ("materials", "material"), ("assignments", "assignment"),
                                 ("questions", "question")):
        sets[collection] = unique(bundle[collection], "id", collection)
        expected_items.update(singular + ":" + ident for ident in sets[collection])
    for collection, singular in (("lessons", "lesson"), ("activities", "activity"), ("media", "media")):
        sets[collection] = unique(course[collection], "id", collection)
        expected_items.update(singular + ":" + ident for ident in sets[collection])
    steps = [step for lesson in course["lessons"] for step in lesson["steps"]]
    expected_items.update("step:" + ident for ident in unique(steps, "id", "steps"))
    for step in steps:
        field, target = {"reading": ("materialID", "materials"), "activity": ("activityID", "activities"),
                         "question": ("questionID", "questions")}[step["kind"]]
        require(step[field] in sets[target], f"dangling step reference: {step[field]}")
    for activity in course["activities"]:
        if "inputNeeds" in activity:
            inputs = activity["inputNeeds"]
            require(inputs["remoteOnlyOK"] == ("remote" in inputs["alternatives"]),
                    "remote-only declaration must match remote input alternative")
        if activity["kind"] == "parsons":
            require(sorted(activity["order"]) == list(range(len(activity["blocks"]))),
                    "Parsons order must be a permutation of all block indices")
    checks = course["answerChecks"]
    require(unique(checks, "questionID", "answer checks") == sets["questions"], "answer check coverage mismatch")
    questions = {q["id"]: q for q in bundle["questions"]}
    for check in checks:
        question = questions[check["questionID"]]
        require(check["expectedIndex"] == question["answer"] < len(question["choices"]), "answer check mismatch")
    source_ids = unique(course["sources"], "id", "sources")
    compatible = {"CC-BY-SA-4.0": {"CC-BY-SA-4.0", "CC-BY-4.0", "CC0-1.0"},
                  "CC-BY-4.0": {"CC-BY-4.0", "CC0-1.0"}, "CC0-1.0": {"CC0-1.0"}}
    for source in course["sources"]:
        require(source["licence"] in compatible[course["licence"]], "incompatible source licence")
        if source["origin"] == "adapted":
            require(source.get("url") and source.get("permission"), "adapted source needs URL and permission basis")
    require(unique(course["provenance"], "item", "provenance items") == expected_items, "per-item provenance coverage mismatch")
    used_sources = set()
    for item in course["provenance"]:
        require(set(item["sources"]) <= source_ids, "unknown provenance source")
        used_sources.update(item["sources"])
    require(used_sources == source_ids, "unused provenance source")
    media_paths = unique(course["media"], "path", "media paths")
    for media in course["media"]:
        checked_asset(root, media)
    for material in bundle["materials"]:
        if material["ref"].startswith("https://"):
            check_url(material["ref"])
        else:
            require(material["ref"] in media_paths, "local material missing media hash/size")
    allowed = {"course.json", "bundle.json"} | media_paths | check_review(root, course)
    actual = set()
    for path in root.rglob("*"):
        require(not path.is_symlink(), f"symlink forbidden: {path}")
        if path.is_file():
            actual.add(path.relative_to(root).as_posix())
    require(actual == allowed, f"unlisted/missing course files: {sorted(actual ^ allowed)}")
    return course, bundle_path


def check_registry(root, courses):
    registry = load_json(root / "registry.json")
    check_schema("registry", registry)
    check_urls(registry)
    identities = set()
    paths = set()
    for entry in registry["entries"]:
        identity = (entry["id"], entry["version"])
        require(identity not in identities, "duplicate registry identity/version")
        identities.add(identity)
        if "path" not in entry:
            # Remote pins are declarations only. CI never fetches contributor-controlled URLs.
            require(entry["status"] == "draft" and not entry["reviewers"]["aiChecks"],
                    "remote entries remain draft until locally vendored for review")
            continue
        path = safe_file(root, entry["path"])
        require(entry["path"] in courses, "registry path must name a discovered course.json")
        course = courses[entry["path"]]
        for field in ("id", "version", "creators", "licence"):
            require(entry[field] == course[field], f"registry {field} mismatch: {path}")
        for field in ("status", "reviewedAt", "reviewers"):
            require(entry[field] == course["review"][field], f"registry review mismatch: {path}")
        paths.add(entry["path"])
    require(paths == set(courses), "every local course must have exactly one registry entry")
    return registry


def check_legacy(root):
    """Preserve the original public fixture and its provenance, byte for byte."""
    path = root / "demo" / "bundle.json"
    p = load_json(root / "demo" / "provenance.json")
    require(p["license"] == "CC-BY-SA-4.0" and p["author"] and p["sources"], "legacy provenance missing")
    require(len(p["assets"]) == 1, "unexpected legacy assets")
    asset = p["assets"][0]
    require(asset["path"] == "bundle.json" and asset["origin"] and asset["rightsHolder"]
            and asset["license"] == "CC-BY-SA-4.0", "legacy asset provenance missing")
    require(digest(path) == asset["sha256"], "legacy bundle hash mismatch")
    check_schema("bundle", load_json(path))
    return path


def validate(root=ROOT, *, swift=True):
    courses = {}
    bundles = [check_legacy(root)]
    course_root = root / "courses"
    require(not course_root.is_symlink(), "symlink courses root forbidden")
    for path in sorted(course_root.rglob("*")):
        require(not path.is_symlink(), f"symlink forbidden: {path}")
        if path.name == "course.json":
            course, bundle = check_course(path)
            relative = path.relative_to(root).as_posix()
            require(relative == f"courses/{course['id']}/{course['version']}/course.json", "course directory must match id/version")
            courses[relative] = course
            bundles.append(bundle)
        elif path.is_file():
            require(any(parent.joinpath("course.json").is_file() for parent in path.parents
                        if parent != root and parent.is_relative_to(course_root)), f"orphan course file: {path}")
    check_registry(root, courses)
    if swift:
        with tempfile.TemporaryDirectory() as tmp:
            exe = Path(tmp) / "validate"
            subprocess.run(["swiftc", str(ROOT / "validator/CourseBundle.swift"),
                            str(ROOT / "validator/main.swift"), "-o", str(exe)], check=True)
            for bundle in bundles:
                subprocess.run([str(exe), str(bundle)], check=True)
    return len(courses), len(bundles)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python-only", action="store_true", help="diagnostic only: skip Swift; not the CI gate")
    parser.add_argument("--content-digest", type=Path, help="print the digest for an external AI fact-check")
    args = parser.parse_args()
    try:
        if args.content_digest:
            print(content_digest(load_json(args.content_digest)))
        else:
            courses, bundles = validate(swift=not args.python_only)
            print(f"Validated {courses} open courses and {bundles} bundles" + (" (Swift NOT RUN)" if args.python_only else ""))
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
