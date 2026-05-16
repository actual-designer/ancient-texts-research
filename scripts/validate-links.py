#!/usr/bin/env python3
"""Cross-reference link validator for the Chronos Archive.

Scans all Markdown files in audit/ for relative Markdown links like
[text](path/to/file.md) and reports any that point to non-existent files.

Usage:
    python3 scripts/validate-links.py          # full scan
    python3 scripts/validate-links.py --fix    # attempt automatic fixes (WIP)
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO_ROOT / "audit"
TEXTS_DIR = REPO_ROOT / "texts"


def find_markdown_files(root: Path) -> list[Path]:
    """Return all .md files under root recursively."""
    if not root.exists():
        return []
    return sorted(root.rglob("*.md"))


def extract_links(filepath: Path) -> list[tuple[int, str, str]]:
    """Extract relative markdown links from a file.

    Returns list of (line_number, full_link_text, target_path).
    Only captures links to .md files (cross-references).
    """
    links = []
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    try:
        lines = filepath.read_text(encoding="utf-8").splitlines()
    except Exception as exc:
        print(f"  [SKIP] Cannot read {filepath}: {exc}")
        return links

    for i, line in enumerate(lines, 1):
        for match in link_pattern.finditer(line):
            text, target = match.groups()
            target = target.strip()
            if not target.endswith(".md"):
                continue
            if target.startswith("http://") or target.startswith("https://"):
                continue
            if target.startswith("#"):
                continue
            links.append((i, f"[{text}]({target})", target))

    return links


def resolve_target(source_file: Path, target_path: str) -> Path | None:
    """Resolve a relative link target to an absolute path.

    Links may be:
    1. Relative to the source file's directory (e.g., analyses/gilgamesh.md)
    2. Relative to the repo root (treated as relative to source file's dir)
    3. Absolute-like paths (starting with /) — not expected in this repo
    """
    # Try resolving relative to the source file's directory first
    candidate = (source_file.parent / target_path).resolve()
    if candidate.exists():
        return candidate

    # Try resolving relative to repo root
    candidate = (REPO_ROOT / target_path).resolve()
    if candidate.exists():
        return candidate

    # Try resolving relative to audit dir
    candidate = (AUDIT_DIR / target_path).resolve()
    if candidate.exists():
        return candidate

    return None


def check_toc_anchor(filepath: Path, anchor: str) -> bool:
    """Check if a given anchor (heading) exists in a file.

    Anchors from markdown links are lowercase, hyphenated, and stripped
    of non-alphanumeric characters. We do a simple check: the anchor
    text should appear in the file as a heading anchor or heading text.
    """
    anchor = anchor.lstrip("#")
    if not anchor:
        return True

    try:
        content = filepath.read_text(encoding="utf-8").lower()
    except Exception:
        return False

    # Common patterns for heading anchors in markdown:
    # 1. {#custom-anchor} syntax
    # 2. The heading text itself (which generates an anchor like #heading-text)
    search_anchor = anchor.replace("-", " ").replace("_", " ")
    for line in content.splitlines():
        if line.startswith("#") and search_anchor in line.lower():
            return True
        if "{#" + anchor + "}" in line:
            return True

    return False


def main():
    fix_mode = "--fix" in sys.argv

    all_md_files = find_markdown_files(AUDIT_DIR)
    all_md_files += find_markdown_files(TEXTS_DIR)

    print(f"Scanning {len(all_md_files)} markdown files for cross-reference links...")
    print()

    total_broken = 0
    total_links = 0

    for filepath in all_md_files:
        rel_path = filepath.relative_to(REPO_ROOT)
        links = extract_links(filepath)

        if not links:
            continue

        file_broken = 0
        for line_num, link_text, target_path in links:
            total_links += 1

            # Split target into path and anchor
            anchor = None
            if "#" in target_path:
                idx = target_path.index("#")
                anchor = target_path[idx + 1 :]
                target_path_clean = target_path[:idx]
            else:
                target_path_clean = target_path

            target_file = resolve_target(filepath, target_path_clean)

            if target_file is None:
                print(f"  [BROKEN] {rel_path}:{line_num}  {link_text}  ->  {target_path} NOT FOUND")
                total_broken += 1
                file_broken += 1
                continue

            if anchor:
                if not check_toc_anchor(target_file, anchor):
                    print(f"  [ANCHOR] {rel_path}:{line_num}  {link_text}  ->  anchor '{anchor}' not found in {target_file.relative_to(REPO_ROOT)}")
                    total_broken += 1
                    file_broken += 1

        if file_broken:
            print(f"  ({file_broken} broken in {rel_path})")
            print()

    print(f"\n{'=' * 60}")
    print(f"Total links checked: {total_links}")
    print(f"Broken links found:  {total_broken}")

    if total_broken == 0:
        print("All cross-references are valid.")
    else:
        print("Broken links need fixing.")

    return 1 if total_broken > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
