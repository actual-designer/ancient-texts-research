#!/usr/bin/env python3
"""Fuzzy-match extracted blockquotes against source PDF text."""

import json
from pathlib import Path
from rapidfuzz import fuzz
from scripts.verify.config import (
    QUOTES_DIR, EVIDENCE_DIR, EXTRACTED_DIR, PDF_MAP,
    UNVERIFIABLE_PDFS, FUZZY_THRESHOLD,
)
from scripts.verify.utils import read_file, write_json, slugify


def find_best_match(quote_text, pdf_text):
    """Return the best fuzzy match score (0-100) for quote_text in pdf_text."""
    if not pdf_text or len(quote_text) < 10:
        return 0, ""
    partial = fuzz.partial_ratio(quote_text, pdf_text)
    token = fuzz.token_sort_ratio(quote_text, pdf_text)
    best_score = max(partial, token)
    best_excerpt = ""
    if best_score > 0 and len(pdf_text) > 200:
        idx = pdf_text.lower().find(quote_text[:30].lower())
        if idx >= 0:
            best_excerpt = pdf_text[max(0, idx - 20):idx + len(quote_text) + 20]
        else:
            best_excerpt = pdf_text[:200]
    return best_score, best_excerpt.strip()


def identify_source_pdf(quote):
    """Determine which PDF this quote should be verified against."""
    citation = (quote.get("citation") or "").lower()
    source_file = str(quote.get("file", ""))

    # Check citation field for PDF name
    for name, pdf in PDF_MAP.items():
        if name in citation or name.replace("_", "") in citation:
            return pdf

    # Fall back to source file name
    file_slug = slugify(source_file)
    for name, pdf in PDF_MAP.items():
        if name in file_slug:
            return pdf
    return None


def slug_from_pdf(pdf_name):
    """Derive a slug from a PDF filename for per-file output naming."""
    stem = Path(pdf_name).stem
    for name, pdf in PDF_MAP.items():
        if pdf == pdf_name:
            return name
    return slugify(Path(pdf_name).stem)


def main():
    """Run quote verification against all extracted PDF texts."""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    quotes_file = QUOTES_DIR / "all-quotes.json"

    if not quotes_file.exists():
        print(f"No quotes file found at {quotes_file}")
        return

    all_quotes = json.loads(read_file(quotes_file) or "[]")
    if not all_quotes:
        print("No quotes to verify")
        return

    results = []
    # Track per-file results grouped by slug
    per_file_results = {}
    stats = {"total": 0, "passed": 0, "flagged": 0, "unverifiable": 0, "no_match": 0}

    for quote in all_quotes:
        stats["total"] += 1
        source_pdf = identify_source_pdf(quote)
        quote_text = quote.get("text", "")

        result = {
            "quote_file": quote.get("file", ""),
            "quote_line": quote.get("line_start", 0),
            "quote_text": quote_text[:200] if quote_text else "",
            "source_pdf": source_pdf,
            "match_score": 0,
            "best_excerpt": "",
            "threshold": FUZZY_THRESHOLD,
            "status": "NO_MATCH",
        }

        if not source_pdf:
            result["status"] = "NO_MATCH"
            stats["no_match"] += 1
        elif source_pdf in UNVERIFIABLE_PDFS:
            result["status"] = "UNVERIFIABLE"
            stats["unverifiable"] += 1
        else:
            # Load extracted text from texts/extracted/{slug}.txt
            pdf_slug = slug_from_pdf(source_pdf)
            extracted_path = EXTRACTED_DIR / f"{pdf_slug}.txt"
            if not extracted_path.exists():
                extracted_path = EXTRACTED_DIR / f"{Path(source_pdf).stem}.txt"
            if not extracted_path.exists():
                extracted_path = EXTRACTED_DIR / f"{Path(source_pdf).stem.lower()}.txt"
            if not extracted_path.exists():
                extracted_path = EXTRACTED_DIR / f"{source_pdf.replace(' ', '-')}.txt"

            pdf_text = read_file(extracted_path)
            if not pdf_text:
                result["status"] = "NO_MATCH"
                stats["no_match"] += 1
            else:
                score, excerpt = find_best_match(quote_text, pdf_text)
                result["match_score"] = score
                result["best_excerpt"] = excerpt[:200] if excerpt else ""
                if score >= FUZZY_THRESHOLD:
                    result["status"] = "PASS"
                    stats["passed"] += 1
                else:
                    result["status"] = "FLAGGED"
                    stats["flagged"] += 1

        results.append(result)

        # Group by source PDF slug for per-file output
        if source_pdf:
            pdf_slug = slug_from_pdf(source_pdf)
            if pdf_slug not in per_file_results:
                per_file_results[pdf_slug] = []
            per_file_results[pdf_slug].append(result)
        else:
            # Group unmapped quotes under "unknown"
            if "unknown" not in per_file_results:
                per_file_results["unknown"] = []
            per_file_results["unknown"].append(result)

    # Write per-file evidence JSONs
    for pdf_slug, file_results in per_file_results.items():
        out_path = EVIDENCE_DIR / f"{pdf_slug}-quote-verify.json"
        write_json(out_path, file_results)

    # Write consolidated master JSON
    out_path = EVIDENCE_DIR / "quote-verify-master.json"
    write_json(out_path, results)

    print(
        f"Quotes: {stats['total']} total, "
        f"{stats['passed']} passed, "
        f"{stats['flagged']} flagged, "
        f"{stats['unverifiable']} unverifiable, "
        f"{stats['no_match']} no_match"
    )
    print(f"Results: {out_path}")


if __name__ == "__main__":
    main()