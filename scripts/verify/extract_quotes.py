#!/usr/bin/env python3
"""Extract blockquoted passages from markdown archive files as JSON for fuzzy-matching."""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from scripts.verify.config import ALL_AUDIT_GLOBS, PROJECT_ROOT, QUOTES_DIR
from scripts.verify.utils import read_file, write_json, slugify


# Regex patterns
RE_BLOCKQUOTE_LINE = re.compile(r"^(>\s?)(.*)$")
RE_SECTION_HEADING = re.compile(r"^(#{2,3})\s+(.+)$")
RE_CITATION_CHAPTER = re.compile(r"\(Ch\.\s*\d+,\s*lines?\s*\d+(-\d+)?\)", re.IGNORECASE)
RE_CITATION_SOURCE = re.compile(r"\(([^)]+\.pdf)[^)]*\)", re.IGNORECASE)
RE_BLANK_BLOCKQUOTE = re.compile(r"^>\s*$")


def is_in_code_block(lines: List[str], line_idx: int) -> bool:
    """Check if line_idx is inside a fenced code block (````` blocks)."""
    in_code_block = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True
        if i == line_idx:
            return in_code_block
    return False


def is_in_table(lines: List[str], line_idx: int) -> bool:
    """Check if line_idx is inside a markdown table row (|...| cells).

    Blockquotes inside table cells are ignored — only paragraph-level
    blockquotes are extracted.
    """
    in_table = False
    table_row_active = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_table = False
            table_row_active = False
            continue
        if stripped.startswith("|"):
            table_row_active = True
            in_table = True
        elif table_row_active and not stripped.startswith("|"):
            in_table = False
            table_row_active = False

        if i == line_idx:
            return in_table
    return False


def find_current_section(lines: List[str], line_idx: int) -> str:
    """Find the nearest ## or ### heading above the given line index."""
    section = ""
    for i in range(line_idx - 1, -1, -1):
        line = lines[i]
        match = RE_SECTION_HEADING.match(line)
        if match:
            section = match.group(2).strip()
            break
    return section


def extract_citation(text: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract citation info from quote text.

    Returns (citation_string, citation_source) — e.g.
    ("Ch. 1, lines 1-6", "EpicofAtrahasis.pdf") or (None, None).
    """
    citation: Optional[str] = None
    citation_source: Optional[str] = None

    chapter_match = RE_CITATION_CHAPTER.search(text)
    if chapter_match:
        citation = chapter_match.group(0).strip("()")

    source_match = RE_CITATION_SOURCE.search(text)
    if source_match:
        citation_source = source_match.group(1)

    return citation, citation_source


def extract_quotes_from_content(content: str, file_path: Path) -> List[Dict]:
    """Parse blockquotes from markdown content.

    Returns list of quote dicts with keys:
      file, line_start, line_end, text, section, citation, citation_source.
    """
    lines = content.splitlines()
    quotes: List[Dict] = []

    current_quote_lines: List[Tuple[int, str]] = []
    blockquote_start_idx: Optional[int] = None

    def flush_quote():
        """Emit the current accumulated blockquote and reset state."""
        nonlocal current_quote_lines, blockquote_start_idx
        if not current_quote_lines:
            return

        line_start = current_quote_lines[0][0]
        line_end = current_quote_lines[-1][0]

        full_text = "\n".join(
            re.sub(r"^>\s?", "", line) for _, line in current_quote_lines
        ).strip()

        if not full_text:
            current_quote_lines = []
            blockquote_start_idx = None
            return

        section = find_current_section(lines, line_start)
        citation, citation_source = extract_citation(full_text)

        quotes.append({
            "file": str(file_path),
            "line_start": line_start,
            "line_end": line_end,
            "text": full_text,
            "section": section,
            "citation": citation,
            "citation_source": citation_source,
        })

        current_quote_lines = []
        blockquote_start_idx = None

    for idx, line in enumerate(lines):
        line_num = idx + 1

        bq_match = RE_BLOCKQUOTE_LINE.match(line)
        blank_bq_match = RE_BLANK_BLOCKQUOTE.match(line)

        if bq_match:
            # Skip blockquotes inside code blocks or tables
            if is_in_code_block(lines, idx) or is_in_table(lines, idx):
                flush_quote()
                continue

            if blockquote_start_idx is None:
                blockquote_start_idx = idx

            current_quote_lines.append((line_num, line))
        elif blank_bq_match:
            # Empty blockquote line (e.g. ">") — could be paragraph break.
            # Include it in the span but don't flush yet.
            current_quote_lines.append((line_num, line))
        else:
            flush_quote()

    flush_quote()
    return quotes


def collect_files() -> List[Path]:
    """Collect all archive markdown files matching ALL_AUDIT_GLOBS."""
    files: List[Path] = []
    for pattern in ALL_AUDIT_GLOBS:
        if "*" in pattern:
            from pathlib import Path
            root = PROJECT_ROOT
            parts = pattern.split("/")
            for part in parts[:-1]:
                root = root / part
            files.extend(sorted(root.glob(parts[-1])))
        else:
            p = PROJECT_ROOT / pattern
            if p.exists():
                files.append(p)
    return sorted(set(files))


def process_file(file_path: Path, skip_existing: bool = False) -> List[Dict]:
    """Extract quotes from a single file and write per-file JSON to QUOTES_DIR."""
    slug = slugify(file_path.name)
    output_path = QUOTES_DIR / f"{slug}.quotes.json"

    if skip_existing and output_path.exists():
        return []

    content = read_file(file_path)
    if not content:
        return []

    quotes = extract_quotes_from_content(content, file_path)

    if quotes:
        write_json(output_path, quotes)

    return quotes


def main():
    """Main entry point: extract quotes from all archive markdown files."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract blockquoted passages from Chronos Archive markdown files."
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip files that already have a quotes JSON output.",
    )
    args = parser.parse_args()

    files = collect_files()
    all_quotes: List[Dict] = []

    for file_path in files:
        quotes = process_file(file_path, skip_existing=args.skip_existing)
        all_quotes.extend(quotes)

    QUOTES_DIR.mkdir(parents=True, exist_ok=True)
    write_json(QUOTES_DIR / "all-quotes.json", all_quotes)

    print(f"Extracted {len(all_quotes)} quotes from {len(files)} files.")
    print(f"Output: {QUOTES_DIR}")
    sys.exit(0)


if __name__ == "__main__":
    main()