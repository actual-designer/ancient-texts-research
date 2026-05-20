#!/usr/bin/env python3
"""Verify NHI correlation quotes against evidence extracts."""

import re
from rapidfuzz import fuzz
from scripts.verify.config import AUDIT_DIR, SISYPHUS_EVIDENCE_DIR, EVIDENCE_DIR, FUZZY_THRESHOLD
from scripts.verify.utils import read_file, write_json


NHI_AUTHORS = {
    "vallee": "deep-source-vallee.md",
    "vallée": "deep-source-vallee.md",
    "keel": "deep-source-keel-grusch.md",
    "grusch": "deep-source-keel-grusch.md",
    "aaro": "deep-source-aaro-pasulka.md",
    "pasulka": "deep-source-aaro-pasulka.md",
}


def extract_nhi_claims(text):
    """Extract sentences containing NHI author references."""
    claims = []
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        line_lower = line.lower()
        for author, _ in NHI_AUTHORS.items():
            if author in line_lower and len(line.strip()) > 30:
                claims.append({
                    "line": i,
                    "text": line.strip()[:300],
                    "author": author,
                })
                break
    return claims


def main():
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    nhi_doc = AUDIT_DIR / "12-NHI-correlation.md"
    if not nhi_doc.exists():
        print("NHI correlation document not found")
        return

    text = read_file(nhi_doc)
    claims = extract_nhi_claims(text)
    if not claims:
        print("No NHI claims found in 12-NHI-correlation.md")
        return

    results = []
    for claim in claims:
        author_key = claim["author"]
        evidence_file = SISYPHUS_EVIDENCE_DIR / NHI_AUTHORS[author_key]
        evidence_text = read_file(evidence_file)
        score = 0
        if evidence_text:
            score = fuzz.partial_ratio(claim["text"], evidence_text)
        status = "PASS" if score >= FUZZY_THRESHOLD else "FLAGGED"
        if not evidence_text:
            status = "NO_EVIDENCE"
        results.append({
            "source": str(nhi_doc),
            "line": claim["line"],
            "claim": claim["text"][:200],
            "cited_author": author_key.capitalize(),
            "evidence_file": str(evidence_file),
            "match_score": score,
            "threshold": FUZZY_THRESHOLD,
            "status": status,
        })

    out_path = EVIDENCE_DIR / "nhi-verify.json"
    write_json(out_path, results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    flagged = sum(1 for r in results if r["status"] == "FLAGGED")
    print(f"NHI: {len(results)} claims, {passed} passed, {flagged} flagged")
    print(f"Results: {out_path}")


if __name__ == "__main__":
    main()
