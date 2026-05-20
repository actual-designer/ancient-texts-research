#!/usr/bin/env python3
"""Check numerical consistency across all archive documents."""

import re
from pathlib import Path
from scripts.verify.config import EVIDENCE_DIR
from scripts.verify.utils import read_file, write_json, get_all_audit_files


CANONICAL = {
    "source_texts_count": 14,
    "per_text_analyses_count": 14,
    "synthesis_documents_count": 12,
    "total_audit_files": 28,
}


NUM_PATTERNS = [
    (r"(\d+)\s*source\s*texts?", "source_texts_count"),
    (r"(\d+)\s*per-text\s*analyses?", "per_text_analyses_count"),
    (r"(\d+)\s*synthesis\s*documents?", "synthesis_documents_count"),
    (r"(\d+)\s*foundational\s*texts?", "source_texts_count"),
    (r"(\d+)\s*analyses?", "per_text_analyses_count"),
    (r"all\s+(\d+)\s*texts?", "source_texts_count"),
    (r"(\d+)\s*pages?", None),
    (r"~?(\d{3,4})\s*BCE", None),
    (r"~?(\d{3,4})\s*CE", None),
]


def extract_numerical_claims(text, filepath):
    """Extract all numerical claims with context from text."""
    claims = []
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        for pattern, claim_type in NUM_PATTERNS:
            for m in re.finditer(pattern, line, re.IGNORECASE):
                try:
                    value = int(m.group(1).replace(",", ""))
                except ValueError:
                    continue
                context = line.strip()[:120]
                claims.append({
                    "file": str(filepath),
                    "line": i,
                    "text": context,
                    "value": value,
                    "claim_type": claim_type,
                })
    return claims


def main():
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    all_claims = []
    all_conflicts = []

    for filepath in get_all_audit_files():
        text = read_file(filepath)
        if not text:
            continue
        claims = extract_numerical_claims(text, filepath)
        if claims:
            all_claims.extend(claims)
            print(f"  {filepath.name}: {len(claims)} numerical claims", flush=True)

    # Check canonical values
    for claim in all_claims:
        ct = claim["claim_type"]
        if ct and ct in CANONICAL:
            canonical = CANONICAL[ct]
            if claim["value"] != canonical:
                conflict = {
                    "file": claim["file"],
                    "line": claim["line"],
                    "text": claim["text"],
                    "found_value": claim["value"],
                    "canonical_value": canonical,
                    "claim_type": ct,
                }
                all_conflicts.append(conflict)
                print(f"  CONFLICT: {Path(claim['file']).name}:{claim['line']} "
                      f"'{ct}' = {claim['value']} (expected {canonical})",
                      flush=True)

    out_claims = EVIDENCE_DIR / "numerical-claims.json"
    out_conflicts = EVIDENCE_DIR / "numerical-master.json"
    write_json(out_claims, all_claims)
    write_json(out_conflicts, all_conflicts)
    print(f"\nNumerical: {len(all_claims)} claims, {len(all_conflicts)} conflicts")
    print(f"Master: {out_conflicts}")


if __name__ == "__main__":
    main()
