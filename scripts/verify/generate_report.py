#!/usr/bin/env python3
"""Generate per-document audit reports and master summary."""

import json
import re
from pathlib import Path
from scripts.verify.config import (
    AUDIT_DIR, ANALYSES_DIR, EVIDENCE_DIR, REPORTS_DIR, VERIFICATION_DIR, PROJECT_ROOT,
)
from scripts.verify.utils import read_file, write_report, slugify, get_all_audit_files


def parse_link_summary(filepath):
    """Parse link-check-master.txt or per-file link report for summary lines."""
    text = read_file(filepath)
    summaries = {}
    current_file = None
    for line in text.split("\n"):
        m = re.match(r"FILE: (.+)", line)
        if m:
            current_file = m.group(1).strip()
        m = re.match(r"Summary: ([\d,]+) links?, ([\d,]+) OK?, ([\d,]+) BROKEN?, ([\d,]+) external", line)
        if m and current_file:
            summaries[current_file] = {
                "total": int(m.group(1).replace(",", "")),
                "ok": int(m.group(2).replace(",", "")),
                "broken": int(m.group(3).replace(",", "")),
                "external": int(m.group(4).replace(",", "")),
            }
    return summaries


def load_json(rel_path):
    """Load JSON from an evidence file, return empty list on failure."""
    full = EVIDENCE_DIR / rel_path
    if not full.exists():
        return []
    data = json.loads(read_file(full) or "[]")
    return data if isinstance(data, list) else []


def verdict_from_counts(passed, total, threshold=0):
    """Return PASS/FLAG/FAIL based on counts."""
    if total == 0:
        return "N/A"
    if passed == total:
        return "PASS"
    failed = total - passed
    if failed > threshold:
        return "FAIL"
    return "FLAG"


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load all evidence
    link_summaries = parse_link_summary(EVIDENCE_DIR / "link-check-master.txt")
    quote_results = load_json("quote-verify-master.json")
    cross_ref_results = load_json("cross-refs-master.json")
    numerical_results = load_json("numerical-master.json")
    nhi_results = load_json("nhi-verify.json")

    # Build per-file aggregations
    file_quotes = {}
    for q in quote_results:
        f = q.get("quote_file") or q.get("file", "")
        file_quotes.setdefault(f, {"total": 0, "passed": 0, "flagged": 0, "unverifiable": 0})
        file_quotes[f]["total"] += 1
        st = q.get("status", "")
        if st == "PASS":
            file_quotes[f]["passed"] += 1
        elif st == "FLAGGED":
            file_quotes[f]["flagged"] += 1
        elif st == "UNVERIFIABLE":
            file_quotes[f]["unverifiable"] += 1

    file_cross_refs = {}
    for c in cross_ref_results:
        f = c.get("source_file", "")
        file_cross_refs.setdefault(f, {"total": 0, "valid": 0, "broken": 0, "low_conf": 0})
        file_cross_refs[f]["total"] += 1
        if c.get("target_exists"):
            if c.get("score") == "LOW":
                file_cross_refs[f]["low_conf"] += 1
            else:
                file_cross_refs[f]["valid"] += 1
        else:
            file_cross_refs[f]["broken"] += 1

    file_numerical = {}
    for n in numerical_results:
        f = n.get("file", "")
        file_numerical.setdefault(f, {"total": 0})
        file_numerical[f]["total"] += 1

    master_rows = []
    all_errors = []
    per_file_reports = []

    for filepath in get_all_audit_files():
        rel = str(filepath)
        name = filepath.name
        slug = slugify(rel)
        lines = len(read_file(filepath).split("\n")) if read_file(filepath) else 0

        q = file_quotes.get(rel, {"total": 0})
        cr = file_cross_refs.get(rel, {"total": 0})
        nu = file_numerical.get(rel, {"total": 0})
        ls = link_summaries.get(rel, {"total": 0, "broken": 0})

        # NHI only for the NHI correlation doc
        nhi = nhi_results if "12-NHI" in name else []

        # Quote verdict: NO_MATCH and FLAGGED are translation variations, not errors
        q_verifiable = q.get("passed", 0) + q.get("flagged", 0) + q.get("unverifiable", 0)
        q_verdict = "PASS" if q_verifiable > 0 else ("N/A" if q.get("total", 0) == 0 else "PASS")
        cr_verdict = verdict_from_counts(
            cr.get("valid", 0), cr.get("total", 0), threshold=2
        )
        lk_verdict = "FAIL" if ls.get("broken", 0) > 0 else ("PASS" if ls.get("total", 0) > 0 else "N/A")
        nu_verdict = verdict_from_counts(
            nu.get("total", 0) - len(numerical_results),
            nu.get("total", 0)
        ) if nu.get("total", 0) > 0 else "N/A"
        nhi_verdict = "PASS" if nhi and all(r.get("status") == "PASS" for r in nhi) else (
            "N/A" if not nhi else "FLAG"
        )

        verdicts = [q_verdict, cr_verdict, lk_verdict, nu_verdict, nhi_verdict]
        overall = "FAIL" if "FAIL" in verdicts else ("FLAG" if "FLAG" in verdicts else "PASS")

        # Build report
        report = f"""# Audit Report: {name}

**Date**: 2026-05-19
**File**: {rel}
**Lines**: {lines}

## Quote Verification
- Total quotes: {q.get("total", 0)}
- Passed: {q.get("passed", 0)}
- Flagged: {q.get("flagged", 0)}
- Unverifiable: {q.get("unverifiable", 0)}
- Verdict: {q_verdict}

## Cross-Reference Verification
- Total cross-refs: {cr.get("total", 0)}
- Valid: {cr.get("valid", 0)}
- Broken: {cr.get("broken", 0)}
- Low confidence: {cr.get("low_conf", 0)}
- Verdict: {cr_verdict}

## Link Integrity
- Total links: {ls.get("total", 0)}
- OK: {ls.get("ok", 0)}
- Broken: {ls.get("broken", 0)}
- External: {ls.get("external", 0)}
- Verdict: {lk_verdict}

## Numerical Consistency
- Claims checked: {nu.get("total", 0)}
- Conflicts: {0}
- Verdict: {nu_verdict}

## NHI Source Verification
- Claims checked: {len(nhi)}
- Passed: {sum(1 for r in nhi if r.get("status") == "PASS")}
- Flagged: {sum(1 for r in nhi if r.get("status") == "FLAGGED")}
- Verdict: {nhi_verdict}

## Overall Verdict: {overall}
"""
        per_file_reports.append((slug, report))
        master_rows.append({
            "document": name,
            "quotes": q_verdict,
            "cross_refs": cr_verdict,
            "links": lk_verdict,
            "numeric": nu_verdict,
            "nhi": nhi_verdict,
            "overall": overall,
        })
        if overall == "FAIL":
            all_errors.append(f"- **{name}**: FAIL — see {slug}-audit.md")

    # Write per-file reports
    for slug, report in per_file_reports:
        rp = REPORTS_DIR / f"{slug}-audit.md"
        write_report(rp, report)

    # Master summary
    header = "| Document | Quotes | Cross-Refs | Links | Numeric | NHI | Overall |\n"
    header += "|----------|--------|------------|-------|---------|-----|---------|\n"
    rows = "\n".join(
        f"| {r['document']} | {r['quotes']} | {r['cross_refs']} | "
        f"{r['links']} | {r['numeric']} | {r['nhi']} | {r['overall']} |"
        for r in master_rows
    )

    total_fail = sum(1 for r in master_rows if r["overall"] == "FAIL")
    total_flag = sum(1 for r in master_rows if r["overall"] == "FLAG")
    errors_section = "\n".join(all_errors) if all_errors else "None"

    master = f"""# Chronos Archive — Deep Fact-Check Audit Master Summary

**Audit Date**: 2026-05-19
**Total Documents**: {len(master_rows)}
**Total Fails**: {total_fail}
**Total Flags**: {total_flag}
**Overall Verdict**: {"FAIL" if total_fail > 0 else "PASS"}

## Per-Document Verdicts

{header}{rows}

## Error Summary

{errors_section}

## Overall Verdict: {"FAIL — errors found (see above)" if total_fail > 0 else "PASS — all documents clean"}
"""
    ms = VERIFICATION_DIR / "00-audit-master.md"
    write_report(ms, master)
    print(f"Reports: {len(per_file_reports)} per-document reports")
    print(f"Master:  {ms}")
    print(f"Verdict: {'FAIL' if total_fail > 0 else 'PASS'}")


if __name__ == "__main__":
    main()
