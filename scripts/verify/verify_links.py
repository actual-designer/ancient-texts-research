#!/usr/bin/env python3
"""Link validator for the Chronos Archive.

Scans all archive markdown files for [text](path) patterns and validates
that internal links resolve to existing files and anchors.

Usage:
    python3 -c "from scripts.verify.verify_links import main; main()"
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

from scripts.verify.config import AUDIT_DIR, ANALYSES_DIR, EVIDENCE_DIR, PROJECT_ROOT
from scripts.verify.utils import (
    extract_markdown_links,
    get_all_audit_files,
    read_file,
    write_report,
    slugify,
)


def _heading_to_anchor(heading: str) -> str:
    slug = heading.lower().strip()
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"[^a-z0-9\-]", "", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def extract_headings(text: str) -> set[str]:
    headings = set()
    for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        headings.add(_heading_to_anchor(match.group(1)))
    return headings


def resolve_link(source_file: Path, link_path: str) -> Path | None:
    path_part = link_path.split("#", 1)[0]
    if not path_part:
        return None

    candidate = (source_file.parent / path_part).resolve()
    if candidate.exists():
        return candidate

    candidate = (AUDIT_DIR / path_part).resolve()
    if candidate.exists():
        return candidate

    candidate = (PROJECT_ROOT / path_part).resolve()
    if candidate.exists():
        return candidate

    return None


def check_anchor(target_file: Path, anchor: str) -> bool:
    text = read_file(target_file)
    if not text:
        return False
    return _heading_to_anchor(anchor) in extract_headings(text)


def verify_file_links(source_file: Path) -> Tuple[List[str], dict]:
    text = read_file(source_file)
    if not text:
        return [], {
            "total": 0, "ok": 0, "broken": 0,
            "external": 0, "anchor_ok": 0, "anchor_broken": 0,
        }

    links = extract_markdown_links(text)
    lines: List[str] = []
    stats = {
        "total": 0, "ok": 0, "broken": 0,
        "external": 0, "anchor_ok": 0, "anchor_broken": 0,
    }

    rel_path = source_file.relative_to(PROJECT_ROOT)
    lines.append(f"FILE: {rel_path}")

    for link_text, raw_path in links:
        raw_path = raw_path.strip()
        stats["total"] += 1

        if not raw_path:
            lines.append(f"  [BROKEN] [{link_text}]({raw_path}) -> EMPTY PATH")
            stats["broken"] += 1
            continue

        if "://" in raw_path:
            lines.append(f"  [EXTERNAL] [{link_text}]({raw_path}) (not checked)")
            stats["external"] += 1
            continue

        if "#" in raw_path:
            path_part, anchor = raw_path.split("#", 1)
        else:
            path_part, anchor = raw_path, None

        if not path_part and anchor:
            if check_anchor(source_file, anchor):
                lines.append(f"  [ANCHOR OK] [{link_text}]({raw_path})")
                stats["anchor_ok"] += 1
            else:
                lines.append(
                    f"  [ANCHOR BROKEN] [{link_text}]({raw_path}) -> ANCHOR NOT FOUND"
                )
                stats["anchor_broken"] += 1
            continue

        resolved = resolve_link(source_file, raw_path)
        if resolved is None:
            lines.append(f"  [BROKEN] [{link_text}]({raw_path}) -> NOT FOUND")
            stats["broken"] += 1
            continue

        if anchor:
            if check_anchor(resolved, anchor):
                lines.append(f"  [ANCHOR OK] [{link_text}]({raw_path})")
                stats["anchor_ok"] += 1
            else:
                lines.append(
                    f"  [ANCHOR BROKEN] [{link_text}]({raw_path}) -> ANCHOR NOT FOUND"
                )
                stats["anchor_broken"] += 1
        else:
            lines.append(f"  [OK]    [{link_text}]({raw_path})")
            stats["ok"] += 1

    ok_total = stats["ok"] + stats["anchor_ok"]
    broken_total = stats["broken"] + stats["anchor_broken"]
    lines.append(
        f"Summary: {stats['total']} links, {ok_total} OK, {broken_total} BROKEN, "
        f"{stats['external']} external"
    )
    lines.append("")
    return lines, stats


def main() -> int:
    files = get_all_audit_files()

    master_lines: List[str] = [
        "=" * 60,
        "Chronos Archive — Link Verification Report",
        "=" * 60,
        "",
    ]

    global_stats = {
        "total": 0, "ok": 0, "broken": 0,
        "external": 0, "anchor_ok": 0, "anchor_broken": 0,
    }

    for source_file in files:
        file_lines, stats = verify_file_links(source_file)
        if not file_lines:
            continue

        report_path = EVIDENCE_DIR / f"{slugify(source_file.name)}-links.txt"
        write_report(report_path, "\n".join(file_lines))

        master_lines.extend(file_lines)
        for key in global_stats:
            global_stats[key] += stats[key]

    ok_total = global_stats["ok"] + global_stats["anchor_ok"]
    broken_total = global_stats["broken"] + global_stats["anchor_broken"]

    master_lines.extend([
        "=" * 60,
        "GLOBAL SUMMARY",
        "=" * 60,
        f"Total files scanned: {len(files)}",
        f"Total links: {global_stats['total']}",
        f"OK: {ok_total}",
        f"BROKEN: {broken_total}",
        f"External (not checked): {global_stats['external']}",
        "",
    ])

    master_path = EVIDENCE_DIR / "link-check-master.txt"
    write_report(master_path, "\n".join(master_lines))

    print("Link verification complete.")
    print(f"  Total links: {global_stats['total']}")
    print(f"  OK: {ok_total}")
    print(f"  BROKEN: {broken_total}")
    print(f"  External: {global_stats['external']}")
    print(f"  Reports written to: {EVIDENCE_DIR.relative_to(PROJECT_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
