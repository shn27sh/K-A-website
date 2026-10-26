#!/usr/bin/env python3
"""Check that relative links and heading anchors in the repository's Markdown files resolve.

Scans every .md and .mdc file in the repository. External links (http:, https:,
mailto:, tel:, ...) are not checked. Links inside fenced code blocks and inline
code are ignored. Anchors follow GitHub's heading slug rules.

Usage:  python scripts/check-doc-links.py
Exit status: 0 when every link resolves, 1 when any link is broken or no files are found.
Uses only the Python standard library (3.9+).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
EXTENSIONS = {".md", ".mdc"}
SKIP_DIRS = {".git", "node_modules"}

SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
HTML_ANCHOR = re.compile(r"<a\s+[^>]*(?:id|name)=\"([^\"]+)\"", re.IGNORECASE)
FENCE = re.compile(r"^ {0,3}(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
IN_GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"


def markdown_files() -> list[Path]:
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        files.extend(Path(dirpath, name) for name in sorted(filenames) if Path(name).suffix in EXTENSIONS)
    return files


def lines_outside_code(path: Path):
    """Yield (line number, text) for lines outside fenced code blocks, with inline code removed."""
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield number, INLINE_CODE.sub("", line)


def slugify(heading: str) -> str:
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


_anchor_cache: dict[Path, set[str]] = {}


def anchors(path: Path) -> set[str]:
    if path not in _anchor_cache:
        found: set[str] = set()
        seen: dict[str, int] = {}
        for _, line in lines_outside_code(path):
            found.update(a.lower() for a in HTML_ANCHOR.findall(line))
            match = HEADING.match(line)
            if match:
                slug = slugify(match.group(1))
                count = seen.get(slug, 0)
                seen[slug] = count + 1
                found.add(slug if count == 0 else f"{slug}-{count}")
        _anchor_cache[path] = found
    return _anchor_cache[path]


def check(path: Path) -> tuple[int, list[tuple[int, str]]]:
    checked, errors = 0, []
    for number, line in lines_outside_code(path):
        for target in LINK.findall(line):
            if SCHEME.match(target):
                continue
            checked += 1
            file_part, _, fragment = target.partition("#")
            if not file_part:
                resolved = path
            elif file_part.startswith("/"):
                resolved = ROOT / unquote(file_part.lstrip("/"))
            else:
                resolved = path.parent / unquote(file_part)
            if not resolved.exists():
                errors.append((number, f"link target not found: {target}"))
            elif fragment and resolved.is_file() and resolved.suffix in EXTENSIONS:
                if unquote(fragment).lower() not in anchors(resolved):
                    errors.append((number, f"anchor not found: {target}"))
    return checked, errors


def escape(value: str, is_property: bool = False) -> str:
    value = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return value.replace(":", "%3A").replace(",", "%2C") if is_property else value


def main() -> int:
    sys.stdout.reconfigure(errors="backslashreplace")
    files = markdown_files()
    if not files:
        print("No Markdown files found; nothing was checked.")
        return 1

    total_checked, broken = 0, []
    for path in files:
        checked, errors = check(path)
        total_checked += checked
        relative = path.relative_to(ROOT).as_posix()
        for number, message in errors:
            broken.append((relative, number, message))
            if IN_GITHUB_ACTIONS:
                print(f"::error file={escape(relative, True)},line={number}::{escape(message)}")
            else:
                print(f"{relative}:{number}: {message}")

    result = f"Checked {total_checked} relative links in {len(files)} files: {len(broken)} broken."
    print(result)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(f"### Documentation links\n\n{result}\n")
            if broken:
                summary.write("\n| File | Line | Problem |\n|---|---|---|\n")
                summary.writelines(f"| `{f}` | {n} | {m.replace('|', '&#124;')} |\n" for f, n, m in broken)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
