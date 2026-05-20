"""Shared utility functions for the verification toolkit."""

import json
import re
from pathlib import Path
from typing import List, Tuple


def read_file(path: Path) -> str:
    """Safely read a text file, returning empty string on error."""
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, UnicodeDecodeError):
        return ""


def write_report(path: Path, content: str) -> None:
    """Write structured report content to a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    """Write JSON data to a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")


def slugify(filename: str) -> str:
    """Convert a filename to a clean slug for report naming."""
    name = Path(filename).stem.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    """Extract all [text](path) markdown links from text.

    Returns list of (link_text, link_path) tuples.
    """
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    return re.findall(pattern, text)


def get_all_audit_files() -> List[Path]:
    """Get all archive markdown files to audit."""
    from .config import AUDIT_DIR, ANALYSES_DIR

    files = []
    # Synthesis documents
    for f in sorted(AUDIT_DIR.glob("[0-9]*.md")):
        files.append(f)
    # Per-text analyses
    for f in sorted(ANALYSES_DIR.glob("*.md")):
        files.append(f)
    # README and INDEX
    readme = AUDIT_DIR.parent / "README.md"
    if readme.exists():
        files.append(readme)
    return files
