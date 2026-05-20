#!/usr/bin/env python3
"""Validate cross-references between archive documents."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import re
from scripts.verify.config import AUDIT_DIR, ANALYSES_DIR, EVIDENCE_DIR, PROJECT_ROOT
from scripts.verify.utils import read_file, write_json, slugify, get_all_audit_files, extract_markdown_links


STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "can", "could", "shall", "should", "may", "might", "this",
    "that", "these", "those", "it", "its", "see", "also", "not", "no",
    "source", "audit", "synthesis", "analysis", "document", "section",
    "chapter", "figure", "table", "note", "reference", "regarding",
    "according", "based", "which", "where", "when", "what", "who",
}


def extract_keywords(text: str) -> list:
    words = set(re.sub(r"[^a-zA-Z\s]", "", text).lower().split())
    return [w for w in words if w not in STOP_WORDS and len(w) > 3]


def resolve_target(source_file: Path, link_path: str) -> tuple:
    source_dir = source_file.resolve().parent

    if link_path.startswith("../"):
        resolved = AUDIT_DIR / link_path.replace("../", "")
    else:
        resolved = (source_dir / link_path).resolve()

    if not resolved.exists() or not resolved.is_file():
        return None, "target_not_found"

    if resolved.suffix and resolved.suffix != ".md":
        return None, "not_markdown"

    return resolved, None


def search_target_for_context(target_path: Path, keywords: list) -> tuple:
    text = read_file(target_path)
    if not text:
        return "LOW", 0, []

    text_lower = text.lower()
    found_keywords = [kw.lower() for kw in keywords if kw.lower() in text_lower]
    count = len(found_keywords)

    if count >= 3:
        return "HIGH", count, found_keywords
    elif count >= 1:
        return "MEDIUM", count, found_keywords
    else:
        return "LOW", 0, []


def find_line_number(lines: list, link_path: str) -> int:
    for i, line in enumerate(lines):
        if f"]({link_path})" in line:
            return i + 1
    return 0


def extract_context(lines: list, line_idx: int, window: int = 3) -> str:
    start = max(0, line_idx - window)
    end = min(len(lines), line_idx + window + 1)
    return " ".join(lines[start:end]).strip()


def extract_paren_refs(text: str) -> list:
    patterns = []

    refs = re.finditer(
        r'\(\s*(?:see|cf\.|see also|source:)\s*(?:\[([^\]]*)\]\([^)]+\)|([^\)]+))\s*(?::\s*([^)]*))?\)',
        text, re.IGNORECASE
    )
    for m in refs:
        link_text = m.group(1) or m.group(2) or ""
        context = m.group(3) or ""
        link_match = re.search(r'\[([^\]]*)\]\(([^)]+)\)', m.group(0))
        if link_match:
            patterns.append(("paren", link_match.group(1), link_match.group(2), context))
        elif m.group(2):
            path = m.group(2).strip()
            if path.endswith(".md"):
                patterns.append(("paren", link_text.strip(), path, context))

    source_refs = re.finditer(r'\(\s*source:\s*([^\)]+\.md)\s*\)', text, re.IGNORECASE)
    for m in source_refs:
        path = m.group(1).strip()
        patterns.append(("source", "", path, ""))

    return patterns


def process_file(filepath: Path) -> list:
    text = read_file(filepath)
    if not text:
        return []

    lines = text.split("\n")
    results = []
    seen_refs = set()

    for link_text, link_path in extract_markdown_links(text):
        if link_path.startswith(("http://", "https://", "ftp://", "#", "mailto:")):
            continue

        ref_key = f"{link_text}:{link_path}"
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)

        line_num = find_line_number(lines, link_path)
        context = extract_context(lines, line_num - 1) if line_num > 0 else ""

        target, issue = resolve_target(filepath, link_path)
        target_exists = target is not None

        if issue is None:
            keywords = extract_keywords(context)
            if keywords:
                score, kw_found, _ = search_target_for_context(target, keywords)
            else:
                score, kw_found = "MEDIUM", 0
            issue = None
        else:
            score, kw_found = "LOW", 0

        results.append({
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": line_num,
            "link_text": link_text[:200] if link_text else "",
            "link_target": link_path,
            "context": context[:200] if context else "",
            "target_exists": target_exists,
            "score": score,
            "issue": issue,
        })

    for ref_type, link_text, link_path, extra_context in extract_paren_refs(text):
        ref_key = f"{ref_type}:{link_text}:{link_path}"
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)

        target, issue = resolve_target(filepath, link_path)
        target_exists = target is not None

        search_text = extra_context or link_text
        if issue is None:
            keywords = extract_keywords(search_text)
            if keywords:
                score, kw_found, _ = search_target_for_context(target, keywords)
            else:
                score, kw_found = "MEDIUM", 0
            issue = None
        else:
            score, kw_found = "LOW", 0

        ctx_str = f"({ref_type} {link_text}: {extra_context})" if extra_context else f"({ref_type} {link_text})"
        results.append({
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": 0,
            "link_text": link_text[:200] if link_text else "",
            "link_target": link_path,
            "context": ctx_str[:200],
            "target_exists": target_exists,
            "score": score,
            "issue": issue,
        })

    return results


def main():
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    print("Verifying cross-references...")
    all_results = []
    file_counts = {}

    for filepath in get_all_audit_files():
        file_results = process_file(filepath)
        if not file_results:
            continue

        all_results.extend(file_results)
        file_counts[str(filepath.relative_to(PROJECT_ROOT))] = len(file_results)

        out_path = EVIDENCE_DIR / f"{slugify(str(filepath))}-cross-refs.json"
        write_json(out_path, file_results)

    master = EVIDENCE_DIR / "cross-refs-master.json"
    write_json(master, all_results)

    broken = sum(1 for r in all_results if r["issue"] == "target_not_found")
    not_markdown = sum(1 for r in all_results if r["issue"] == "not_markdown")
    low_conf = sum(1 for r in all_results if r["target_exists"] and r["score"] == "LOW")
    medium_conf = sum(1 for r in all_results if r["target_exists"] and r["score"] == "MEDIUM")
    high_conf = sum(1 for r in all_results if r["target_exists"] and r["score"] == "HIGH")

    print(f"\nProcessed {len(file_counts)} files, {len(all_results)} total cross-refs")
    print(f"  - Broken links: {broken}")
    print(f"  - Non-markdown targets: {not_markdown}")
    print(f"  - High confidence: {high_conf}")
    print(f"  - Medium confidence: {medium_conf}")
    print(f"  - Low confidence (content mismatch): {low_conf}")
    print(f"\nMaster report: {master}")
    print(f"Per-file reports in: {EVIDENCE_DIR}")

    return all_results


if __name__ == "__main__":
    main()