# Numerical Consistency Review Summary

**Date:** 2026-05-20

## 1. Overview

| Category | Count |
|----------|-------|
| **Total numerical claims extracted** | 82 |
| **Conflicts found** | 3 |
| **Documents with claims** | 22 |

## 2. Conflict Analysis

### Conflict 1: 09-location-registry.md line 4
- **Context**: `"synthesis of 13 source texts..."`
- **Found value**: 13 source texts
- **Canonical value**: 14 source texts 
- **Classification**: ERROR
- **Cause**: The archive has 14 source PDFs, but this document says 13. Likely the document was written before the last source was added.
- **Fix**: Change `13` to `14`

### Conflict 2: 10-correlation-map.md line 390
- **Context**: `"...across all 13 source texts..."`
- **Found value**: 13 source texts
- **Canonical value**: 14 source texts
- **Classification**: ERROR
- **Cause**: Same as above — document says 13 when there are 14 source texts.
- **Fix**: Change `13` to `14`

### Conflict 3: README.md line 156
- **Context**: `"...following a review of all 15 per-text analyses..."`
- **Found value**: 15 per-text analyses
- **Canonical value**: 14 per-text analyses
- **Classification**: ERROR
- **Cause**: There are 14 per-text analyses (not 15). The README counts incorrectly or includes a non-analysis document.
- **Fix**: Change `15` to `14`

## 3. External Source Verification Discrepancies

From Task 18 external source verification:

### Discrepancy A: Atrahasis dating
- **Claim**: "c. 2450 BCE cuneiform tablet"
- **Verification**: DISPUTED — oldest known copies are Old Babylonian (~1700 BCE)
- **Action**: Clarify whether date refers to narrative setting or manuscript

### Discrepancy B: Rig Veda hymn count
- **Claim**: "1,205 hymns"
- **Verification**: ERROR — correct count is 1,028
- **Action**: Fix hymn count in rig-veda.md

### Discrepancy C: Book of the Dead
- **Claim**: "trans. E. A. Wallis Budge (1920); 22 pages, 190 chapters"
- **Verification**: PARTIALLY DISPUTED — Budge translation date is 1895/1913, not 1920; "22 pages" refers to archive's PDF, not the Budge edition
- **Action**: Verify and correct the date

### Discrepancy D: Popol Vuh page count
- **Claim**: "285 pp."
- **Verification**: PARTIALLY DISPUTED — published OU Press edition is 327-328 pages
- **Action**: Clarify page count source

## 4. Remediation List

| # | File | Line | Current Value | Correct Value | Confidence |
|---|------|------|--------------|---------------|------------|
| 1 | audit/09-location-registry.md | 4 | 13 source texts | 14 source texts | HIGH |
| 2 | audit/10-correlation-map.md | 390 | 13 source texts | 14 source texts | HIGH |
| 3 | README.md | 156 | 15 per-text analyses | 14 per-text analyses | HIGH |
| 4 | audit/analyses/rig-veda.md | ? | 1,205 hymns | 1,028 hymns | HIGH |
| 5 | audit/analyses/book-of-the-dead.md | ? | 1920 | 1895 or 1913 | MEDIUM |
| 6 | audit/analyses/atrahasis.md | ? | 2450 BCE | ~1700 BCE | MEDIUM |
| 7 | audit/analyses/popol-vuh.md | ? | 285 pp. | 327-328 pp. | LOW |

## 5. Verdict

3 numerical conflicts confirmed as errors. 4 additional discrepancies from external verification. Total items requiring fixes: **7**.
