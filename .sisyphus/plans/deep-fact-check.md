# Deep Fact-Check — The Chronos Archive

## TL;DR

> **Quick Summary**: Systematic forensic audit of every fact in the Chronos Archive. Build a reusable Python verification toolkit (`scripts/verify/`), extract all source PDF text, fuzzy-match every archive quote against its source, validate every cross-reference, check numerical and internal consistency, verify NHI modern-source quotes, and cross-check claims against standard reference works. Zero errors tolerated. Per-document audit reports plus master summary.
>
> **Deliverables**:
> - `scripts/verify/` — Reusable verification toolkit (6+ modular Python scripts)
> - Extracted source text cache from all 15 PDFs
> - Per-document audit reports (`audit/verification/reports/`)
> - Master audit summary (`audit/verification/00-audit-master.md`)
> - Issue-fix commits for every discovered error
> - Final certification if zero errors achieved
>
> **Estimated Effort**: Large (7-10 waves)
> **Parallel Execution**: YES — Waves 1-3 can parallelize heavily
> **Critical Path**: PDF extraction → Quote extraction → Quote matching → Cross-ref validation → Reports → Fixes → Re-verify

---

## Context

### Original Request

> "I need a comprehensive plan for doing deep fact checking on the whole archive. As the lead researcher and curator, it is of utmost importance that the Chronos Archive is factual and correct."

### Interview Summary

**Key Decisions**:
- **Fact definition**: Source quote accuracy, cross-reference validity, internal consistency, numerical accuracy, external source verification, translation-key mapping, link integrity — ALL categories
- **Scope**: All 14 per-text analyses + 12 syntheses + README + INDEX + NHI correlation (12-NHI-correlation.md)
- **External sources**: Standard reference works (ANET, critical editions, published translations) — not deep academic databases
- **Acceptance threshold**: ZERO errors tolerated
- **Verification method**: Automated PDF-text extraction with fuzzy matching at configurable threshold; human review of flagged outliers
- **Report format**: Per-document audit reports + consolidated master summary
- **Tooling**: Reusable `scripts/verify/` toolkit — Python, modular, runnable periodically
- **Human review**: Automated fuzzy-match threshold — below threshold auto-accepts as translation variation, above flags for curator review

### Archive at a Glance

| Category | Count | Lines (approx) |
|----------|-------|----------------|
| Per-text analyses | 14 files | ~5,400 lines |
| Synthesis documents | 12 files | ~7,000+ lines |
| Source PDFs | 15 files | Mixed quality |
| README + INDEX | 2 files | ~300 lines |
| NHI evidence extracts | 3 files | ~300 lines |
| Prior QA evidence | 20+ files | Verification history |
| **Total markdown** | **28 files** | **~13,000 lines** |

### Metis Review

**Critical Pre-Audit Discoveries**:
- **267 broken links already exist** — the majority are `../` prefixed paths in `audit/11-unified-hypothesis.md` that resolve incorrectly. This is the largest single issue discovered before the audit even begins.
- **3+ PDFs are unextractable via pdftotext** — Poetic Edda (scanned), Yasna/Zoroastrian Gathas (scanned), Hesiod/Theogony (scanned). These will need OCR or will be flagged as "unverifiable (no source text)".
- **Translation variation is a major factor** — the archive often synthesizes from multiple translations. Blockquotes may not match any single PDF exactly. The fuzzy-matching threshold is essential.
- **The existing `validate-links.py` script already works** — it found all 267 broken links. The task is to fix them, not re-invent the checker.

**Gaps Identified & Addressed**:
1. *Q: What if a quote cites a different translation than the PDF in texts/?* → **Addressed**: Fuzzy matching threshold auto-accepts translation variation; flagged items get human classification as TRANSLATION_VARIATION vs ERROR
2. *Q: What about PDFs that can't be extracted?* → **Addressed**: Task 1 classifies all 15 PDFs; unextractable ones flagged as "unverifiable"
3. *Q: 267 pre-existing broken links — should fixing them be part of this plan?* → **Yes**: Task 29 (fix link integrity) addresses all broken links found by validate-links.py
4. *Q: Should the plan include re-running validate-links.py as a baseline before building new tools?* → **Yes**: Task 8 already includes this

**Guardrails Applied**:
- PDFs must NOT be modified
- Unverifiable sources must be explicitly noted, not silently skipped
- Translation variation is NOT an error — the threshold system distinguishes variation from misquotation
- External verification limited to standard reference works, not deep academic research

---

## Work Objectives

### Core Objective
Verify 100% of factual claims in the Chronos Archive, achieving zero errors across all documents, with a reusable toolkit for ongoing quality assurance.

### Concrete Deliverables
1. `scripts/verify/extract_pdf_text.py` — Extracts searchable text from all 15 source PDFs
2. `scripts/verify/extract_quotes.py` — Extracts all blockquotes from markdown archive files
3. `scripts/verify/verify_quotes.py` — Fuzzy-matches quotes against extracted PDF text
4. `scripts/verify/verify_links.py` — Validates all markdown links resolve
5. `scripts/verify/verify_cross_refs.py` — Validates cross-references point to supporting content
6. `scripts/verify/verify_numerical.py` — Checks numerical consistency across documents
7. `scripts/verify/verify_nhi_sources.py` — Verifies NHI correlation quotes against evidence
8. `scripts/verify/generate_report.py` — Generates per-document and master audit reports
9. `audit/verification/reports/` directory — Per-document audit reports (one per archive document)
10. `audit/verification/00-audit-master.md` — Consolidated master summary
11. Issue-fix commits for all discovered errors
12. `audit/verification/certification.md` — Final certification (if zero errors achieved)

### Definition of Done
- [ ] All 28 markdown documents have a corresponding audit report
- [ ] Every blockquote in every analysis has been compared against its source PDF
- [ ] Every cross-reference link resolves and points to content that supports the claim
- [ ] Every numerical assertion is internally consistent (same numbers used across documents)
- [ ] Every NHI modern-source quote matches its evidence extract
- [ ] All markdown links resolve to existing files
- [ ] Zero unresolved errors remain
- [ ] Master audit report published with PASS verdict on all documents
- [ ] Script suite committed and can be re-run with `python3 scripts/verify/run_all.py`

### Must Have
- Zero errors after all fixes applied
- Every quote verified against source text
- Every cross-reference validated
- Every numerical claim consistent
- All links resolve
- NHI sources verified
- Reusable toolkit committed to repo

### Must NOT Have (Guardrails)
- Do NOT modify source PDFs under any circumstances
- Do NOT modify archive analysis documents before recording issues (all fixes happen AFTER full audit)
- Do NOT attempt deep academic database research — stick to standard reference works
- Do NOT alter the amnesia hypothesis content itself — verify its factual claims, not its interpretation
- Do NOT attempt full-pdf OCR on truly unreadable scans — flag and skip, don't force

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed via the verification scripts. No exceptions.

### Test Decision
- **Infrastructure**: Minimal — Python 3 + `pip install rapidfuzz pdfminer.six`
- **Automated tests**: The verification scripts ARE the tests — they output PASS/FAIL per claim
- **QA Policy**: Each verification script writes evidence to `audit/verification/evidence/` with detailed match/no-match output

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Infrastructure — foundation, MAX PARALLEL):
├── Task 1: Install tools + verify PDF extractability
├── Task 2: Create scripts/verify/ scaffolding (directory, __init__.py, requirements.txt)
├── Task 3: Build extract_pdf_text.py
├── Task 4: Build extract_quotes.py
└── Task 5: Build verify_links.py

Wave 2 (Extraction — depends on Wave 1, MAX PARALLEL):
├── Task 6: Extract text from all 15 PDFs → texts/extracted/
├── Task 7: Extract all blockquotes from all archive documents → audit/verification/quotes/
└── Task 8: Run full link validation → audit/verification/evidence/link-check.txt

Wave 3 (Core Verification Tools — depends on Wave 1, MAX PARALLEL):
├── Task 9: Build verify_quotes.py (fuzzy matching engine)
├── Task 10: Build verify_cross_refs.py (cross-reference parser + validator)
├── Task 11: Build verify_numerical.py (numerical claim extractor)
├── Task 12: Build verify_nhi_sources.py (NHI quote matcher)
└── Task 13: Build generate_report.py (report generator)

Wave 4 (Verification Execution — depends on Waves 2+3, MAX PARALLEL):
├── Task 14: Run quote verification on ALL per-text analyses
├── Task 15: Run cross-reference verification on ALL synthesis documents
├── Task 16: Run numerical consistency check on ALL documents
├── Task 17: Run NHI source verification on 12-NHI-correlation.md
├── Task 18: Run external source checks on key claims (standard references)
└── Task 19: Generate all per-document reports

Wave 5 (Report Analysis — depends on Wave 4, PARALLEL):
├── Task 20: Review quote mismatches above threshold — classify as error or acceptable variation
├── Task 21: Review broken cross-references — fix links or fix content
├── Task 22: Review numerical inconsistencies — determine correct values
├── Task 23: Review NHI source mismatches
└── Task 24: Generate master audit summary

Wave 6 (Remediation — depends on Wave 5, PARTIALLY SEQUENTIAL):
├── Task 25: Fix all confirmed quote errors
├── Task 26: Fix all broken cross-references
├── Task 27: Fix all numerical inconsistencies
├── Task 28: Fix NHI source quote issues
└── Task 29: Fix link integrity issues

Wave 7 (Re-Verification + Certification — depends on Wave 6):
├── Task 30: Re-run full verification suite after fixes
├── Task 31: Verify zero errors achieved
├── Task 32: Generate certification document
└── Task 33: Commit + push verification toolkit and reports

Critical Path: Task 1 → Task 6 → Task 9 → Task 14 → Task 20 → Task 25 → Task 30 → Task 32
```

---

## TODOs

- [x] 1. **Install PDF extraction tools + verify PDF landscape**

  **What to do**:
  - Install `poppler-utils` for `pdftotext`, `python3-venv` for virtual env
  - Install Python dependencies: `rapidfuzz`, `pdfminer.six`, `mistune`
  - Create virtual environment at `scripts/verify/.venv/`
  - Test PDF extraction on each of the 15 PDFs in `texts/`
  - Classify each PDF as: text-searchable, scanned-but-ocrable, or unscannable
  - For scanned PDFs, install `ocrmypdf` + `tesseract` if viable
  - Create `audit/verification/` directory structure (reports/, quotes/, evidence/)

  **Must NOT do**:
  - Do NOT modify any PDF files
  - Do NOT proceed with unscannable PDFs — flag them

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: DevOps/setup work with multiple tool installations and system dependencies
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - No specialized skills apply — this is environment setup

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5)
  - **Blocks**: 6, 7, 8
  - **Blocked By**: None

  **References**:
  - `texts/` — All 15 PDFs to be tested for extractability
  - `scripts/validate-links.py` — Existing script for reference on repo conventions

  **Acceptance Criteria**:
  - [ ] `pdftotext --version` returns successfully
  - [ ] `python3 -c "import rapidfuzz"` succeeds
  - [ ] All 15 PDFs classified (searchable/scanned/unscannable)
  - [ ] `audit/verification/` directory structure created

  **QA Scenarios**:
  ```
  Scenario: PDF extraction works on text-layer PDFs
    Tool: Bash
    Preconditions: poppler-utils installed, directory audit/verification/ exists
    Steps:
      1. Run: pdftotext texts/eze.pdf audit/verification/evidence/eze-extracted.txt
      2. Check: wc -l audit/verification/evidence/eze-extracted.txt
    Expected Result: Extracted text file has >0 lines
    Evidence: audit/verification/evidence/eze-extracted.txt

  Scenario: Python dependencies import correctly
    Tool: Bash
    Preconditions: .venv activated
    Steps:
      1. Run: python3 -c "import rapidfuzz; import pdfminer; import mistune; print('OK')"
    Expected Result: Outputs "OK"
    Evidence: audit/verification/evidence/deps-check.txt
  ```

  **Commit**: NO (infrastructure, grouped with Wave 1 tools)

---

- [x] 2. **Create scripts/verify/ scaffolding**

  **What to do**:
  - Create directory: `scripts/verify/`
  - Create `scripts/verify/__init__.py`
  - Create `scripts/verify/requirements.txt` with:
    ```
    rapidfuzz>=3.0.0
    pdfminer.six>=20221105
    mistune>=3.0.0
    ```
  - Create `scripts/verify/config.py` with shared constants:
    - Paths to `texts/`, `audit/`, `audit/verification/`
    - Fuzzy-match threshold constant (default: 70)
    - File patterns for different document types
  - Create `scripts/verify/utils.py` with shared helpers:
    - `read_file(path)` — safe file reading
    - `write_report(path, content)` — structured report writing
    - `extract_markdown_links(text)` — link pattern extraction
    - `slugify(filename)` — clean filename generation
  - Create `scripts/verify/run_all.py` — orchestration script that runs all verification modules sequentially

  **Must NOT do**:
  - Do not implement verification logic here — only scaffolding and utilities

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Standard boilerplate scaffolding, well-defined structure
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5)
  - **Blocks**: 9, 10, 11, 12, 13
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] `scripts/verify/` directory exists with all scaffolding files
  - [ ] `python3 -c "from scripts.verify import config, utils"` succeeds
  - [ ] `requirements.txt` contains correct dependencies

  **Commit**: YES (with Tools 3-5)
  - Message: `feat(scripts): add verification toolkit scaffolding`
  - Files: `scripts/verify/*`

---

- [x] 3. **Build `extract_pdf_text.py`**

  **What to do**:
  - Script that extracts text from all 15 PDFs
  - For text-searchable PDFs: use `subprocess` to call `pdftotext`
  - For scanned PDFs: use `ocrmypdf` + `tesseract` if available; otherwise flag as unscannable
  - Alternative: use `pdfminer` Python library for structured extraction with page numbers preserved
  - Output directory: `texts/extracted/{slug}.txt` — one file per PDF
  - Include page-number markers in output for reference matching
  - Handle errors gracefully: log failed PDFs, don't crash
  - Print summary: N PDFs extracted, M failed
  - Include a `--skip-existing` flag to avoid re-extracting

  **Must NOT do**:
  - Do NOT modify original PDFs
  - Do NOT attempt OCR on truly unreadable scans — flag in report

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with 1, 2, 4, 5)
  - **Blocks**: 6
  - **Blocked By**: 1 (tool installation)

  **Acceptance Criteria**:
  - [ ] Script runs without errors
  - [ ] At minimum, all text-searchable PDFs extracted
  - [ ] Output files contain page-number markers

  **Commit**: YES (grouped with Tasks 2, 4, 5)
  - Message: `feat(scripts): add verification toolkit scaffolding`
  - Files: `scripts/verify/*`

---

- [x] 4. **Build `extract_quotes.py`**

  **What to do**:
  - Script that extracts all blockquoted passages from markdown archive files
  - Parse blockquotes (lines starting with `>` in markdown)
  - For each blockquote, record:
    - Source file path
    - Line number range
    - The full quote text
    - The section/incident heading it appears under
    - The source PDF it claims to cite (e.g., "Ch. 1, lines 1-6")
  - Output per file: `audit/verification/quotes/{document-slug}.quotes.json`
  - Also output a consolidated `audit/verification/quotes/all-quotes.json`
  - Handle multiline blockquotes, nested blockquotes, and blockquotes with attribution lines
  - Handle fenced blockquotes used in tables (distinguish from textual blockquotes)
  - Use `mistune` markdown parser or regex as appropriate

  **Must NOT do**:
  - Do NOT miss blockquotes embedded in bullet lists or tables
  - Do NOT double-count the same quote if referenced in multiple places

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with 1, 2, 3, 5)
  - **Blocks**: 7
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] All blockquotes from all 28 archive files extracted
  - [ ] Each quote has source file, line range, and claimed source citation
  - [ ] Output JSON is valid and parseable

  **Commit**: YES (grouped with Tasks 2, 3, 5)

---

- [x] 5. **Build `verify_links.py`**

  **What to do**:
  - Script that validates all markdown links in all archive documents
  - Extract all `[text](path)` and `[text](path#anchor)` patterns from each markdown file
  - For external links (http/https): check we can skip or verify reachable
  - For internal links (relative paths): verify target file exists
  - For anchor references (path#section): check section heading exists in target file
  - Also validate cross-document links that use `../` path patterns
  - Output per file + consolidated report
  - This can extend/improve the existing `scripts/validate-links.py`

  **Must NOT do**:
  - Do NOT modify any files
  - Do NOT fail on external URLs (just note them)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with 1, 2, 3, 4)
  - **Blocks**: 8
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] All internal links checked for file existence
  - [ ] All internal anchors checked for heading existence
  - [ ] Report generated with broken links listed

  **Commit**: YES (grouped with Tasks 2, 3, 4)

---

- [x] 6. **Extract text from all 15 PDFs**

  **What to do**:
  - Run `extract_pdf_text.py` against all PDFs
  - Verify output quality — spot-check extracted text against PDF content
  - For scanned/unreadable PDFs, document the limitation in the report
  - Store extracted text in `texts/extracted/`

  **Must NOT do**:
  - Do NOT modify PDFs
  - Do NOT spend excessive time on OCR — accept limitations

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 7, 8)
  - **Parallel Group**: Wave 2 (with 7, 8)
  - **Blocks**: 14, 17
  - **Blocked By**: 1 (tools), 3 (script)

  **Commit**: NO (data artifacts — group with reports)

---

- [x] 7. **Extract all blockquotes from archive documents**

  **What to do**:
  - Run `extract_quotes.py` against ALL 28 archive markdown files
  - Verify extraction quality — spot-check a few quotes in each file
  - Store quote JSON in `audit/verification/quotes/`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 6, 8)
  - **Parallel Group**: Wave 2 (with 6, 8)
  - **Blocks**: 14
  - **Blocked By**: 4 (script)

  **Commit**: NO (data artifacts)

---

- [x] 8. **Run full link validation**

  **What to do**:
  - Run `verify_links.py` across all archive documents
  - Collect broken link results
  - Store report in `audit/verification/evidence/link-check.txt`
  - Classify each broken link: file-not-found, anchor-not-found, external-unreachable

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 6, 7)
  - **Parallel Group**: Wave 2 (with 6, 7)
  - **Blocks**: 21
  - **Blocked By**: 5 (script)

  **Commit**: NO (data artifacts)

---

- [x] 9. **Build `verify_quotes.py` — fuzzy matching engine**

  **What to do**:
  - Script that matches extracted quotes against PDF source text
  - For each quote in `quotes/all-quotes.json`:
    1. Identify which source PDF it claims to come from (from the citation text)
    2. Load the extracted PDF text
    3. Attempt to find the quote using fuzzy matching (rapidfuzz `partial_ratio`)
    4. Record: match score, best-match location in PDF, match excerpt, pass/fail
  - Support configurable threshold (default 70/100) for auto-pass
  - Output per-file: `audit/verification/evidence/{file}-quote-verify.json`
  - Consolidated output: `audit/verification/evidence/quote-verify-master.json`
  - Summary: N quotes checked, M matched above threshold, P below threshold (flagged)
  - Handle quotes that span multiple pages

  **Must NOT do**:
  - Do NOT flag translation differences as errors — the threshold system handles this
  - Do NOT crash on quotes from unscannable PDFs — flag as "unverifiable (no source text)"

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 10, 11, 12, 13)
  - **Parallel Group**: Wave 3 (with 10, 11, 12, 13)
  - **Blocks**: 14
  - **Blocked By**: 2 (scaffolding), 6 (extracted text), 7 (extracted quotes)

  **Commit**: YES
  - Message: `feat(scripts): add verification engine scripts`
  - Files: `scripts/verify/verify_quotes.py`

---

- [x] 10. **Build `verify_cross_refs.py`**

  **What to do**:
  - Script that validates cross-references between archive documents
  - Parse patterns like `[entity-registry.md](entity-registry.md)` and `(see [file.md](file.md): context)`
  - For each cross-reference:
    1. Verify target file exists (delegates to verify_links for file check)
    2. Extract the claim context (sentence or phrase before/around the reference)
    3. Search target file for related keywords from the claim context
    4. Score the match: HIGH (keywords found nearby), MEDIUM (keywords found elsewhere), LOW (no match)
  - Output: per-file and consolidated cross-ref validation reports
  - Flag LOW-scoring cross-references for human review

  **Must NOT do**:
  - Do NOT modify any files
  - Do NOT flag cross-references that link to broad concepts (e.g., "see INDEX" is valid contextually)

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 9, 11, 12, 13)
  - **Parallel Group**: Wave 3 (with 9, 11, 12, 13)
  - **Blocks**: 15
  - **Blocked By**: 2

  **Commit**: YES (grouped with 9)

---

- [x] 11. **Build `verify_numerical.py`**

  **What to do**:
  - Script that extracts and checks numerical consistency across the archive
  - Extract all numbers with context: "13 source texts", "3600 years", "14 per-text analyses", "7 chapters", etc.
  - For each numerical claim, check against other documents for the same referent:
    - If one doc says "13 source texts" and another says "14", flag it
    - If INDEX says 14 source texts but an analysis says "one of 13", flag it
  - Maintain a truth table of known correct values (from the canonical sources)
  - Output cross-document numerical conflict report

  **Must NOT do**:
  - Do NOT flag numbers that are legitimately different (different scopes, different time periods)
  - Do NOT flag translation page numbers that vary by edition

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 9, 10, 12, 13)
  - **Parallel Group**: Wave 3 (with 9, 10, 12, 13)
  - **Blocks**: 16
  - **Blocked By**: 2

  **Commit**: YES (grouped with 9)

---

- [x] 12. **Build `verify_nhi_sources.py`**

  **What to do**:
  - Script that verifies NHI correlation document quotes against evidence extracts
  - Load `audit/12-NHI-correlation.md`
  - Extract all citations/references to: Vallée, Keel, Grusch, AARO, Pasulka
  - For each citation, extract the quoted/heard claim
  - Load the corresponding evidence file from `.sisyphus/evidence/deep-source-*.md`
  - Fuzzy-match the claim against the evidence extract
  - Flag mismatches for review
  - Output: `audit/verification/evidence/nhi-quote-verify.json`

  **Must NOT do**:
  - Do NOT rely on the NHI correlation document being perfectly quoted — the evidence extracts are the source of truth
  - Do NOT attempt to verify against the original published books (we don't have them locally)

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 9, 10, 11, 13)
  - **Parallel Group**: Wave 3 (with 9, 10, 11, 13)
  - **Blocks**: 17
  - **Blocked By**: 2

  **Commit**: YES (grouped with 9)

---

- [x] 13. **Build `generate_report.py`**

  **What to do**:
  - Script that generates per-document audit reports and the master summary
  - Takes verification results from all verify_*.py scripts as input
  - For each archive document, produces:
    - `audit/verification/reports/{document}-audit.md`
    - Document overview (file, line count, section count)
    - Quote verification results (N checked, N passed, N flagged)
    - Cross-reference results (N validated, N broken, N low-confidence)
    - Link integrity results (N links, N broken)
    - Numerical consistency results (N checks, N conflicts)
    - NHI source verification (if applicable)
    - Overall verdict: PASS / FLAGGED / FAIL
  - Master summary:
    - `audit/verification/00-audit-master.md`
    - Table with per-document verdicts
    - Error categories and counts
    - Severity breakdown
    - Overall verdict
  - Include total stats: total claims checked, total errors found, error rate

  **Parallelization**:
  - **Can Run In Parallel**: YES (with... well, it depends on results)
  - **Parallel Group**: Wave 4 (with 14-18)
  - **Blocks**: 20
  - **Blocked By**: 2 (scaffolding)

  **Commit**: YES
  - Message: `feat(scripts): add report generator`
  - Files: `scripts/verify/generate_report.py`

---

- [x] 14. **Run quote verification on ALL per-text analyses**

  **What to do**:
  - Execute: `python3 scripts/verify/verify_quotes.py --documents=audit/analyses/*.md`
  - Review output summary: total quotes, matched, flagged, unverifiable
  - Store evidence files

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 15, 16, 17, 18)
  - **Parallel Group**: Wave 4 (with 15, 16, 17, 18)
  - **Blocks**: 20
  - **Blocked By**: 6 (extracted text), 7 (extracted quotes), 9 (verify_quotes script)

  **Commit**: NO (evidence — groups with report)

---

- [x] 15. **Run cross-reference verification on ALL synthesis documents**

  **What to do**:
  - Execute: `python3 scripts/verify/verify_cross_refs.py --documents=audit/0*.md audit/1*.md`
  - Review output: validated references, low-confidence flags
  - Store evidence files

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 14, 16, 17, 18)
  - **Parallel Group**: Wave 4 (with 14, 16, 17, 18)
  - **Blocks**: 21
  - **Blocked By**: 10 (verify_cross_refs)

  **Commit**: NO

---

- [x] 16. **Run numerical consistency check on ALL documents**

  **What to do**:
  - Execute: `python3 scripts/verify/verify_numerical.py --documents=audit/audit/analyses/README.md`
  - Review output: conflicts found, truth table deviations
  - Store evidence files

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 14, 15, 17, 18)
  - **Parallel Group**: Wave 4 (with 14, 15, 17, 18)
  - **Blocks**: 22
  - **Blocked By**: 11 (verify_numerical)

  **Commit**: NO

---

- [x] 17. **Run NHI source verification**

  **What to do**:
  - Execute: `python3 scripts/verify/verify_nhi_sources.py`
  - Review output: matched quotes, mismatches
  - Store evidence files

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 14, 15, 16, 18)
  - **Parallel Group**: Wave 4 (with 14, 15, 16, 18)
  - **Blocks**: 23
  - **Blocked By**: 6 (extracted text), 12 (verify_nhi_sources)

  **Commit**: NO

---

- [x] 18. **Run external source checks on key claims (standard references)**

  **What to do**:
  - Identify the 20-30 most critical factual claims across the archive that reference:
    - Specific dates and periods ("593 BCE", "~1500-1200 BCE", "~95 CE")
    - Translation editions ("Bellows, 1923", "Romesh C. Dutt condensed verse")
    - Source text details ("193 pages", "7 chapters, 13 pages", "c. 2450 BCE cuneiform tablet")
    - Historical concordances (Is the Book of the Dead tradition timeline accurate?)
  - Verify each against standard reference works:
    - ANET (Ancient Near Eastern Texts) for Mesopotamian/Egyptian claims
    - Academic editions for each text's dating and authenticity
    - Wikipedia/wikidata as secondary check for well-known facts
  - Output: `audit/verification/evidence/external-source-verify.md`

  **Must NOT do**:
  - Do NOT dive into academic databases or original-language scholarship
  - Do NOT try to verify the amnesia hypothesis interpretations — only factual claims about the texts themselves
  - Do NOT attempt to verify claims from obscure or hard-to-find sources

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 14, 15, 16, 17)
  - **Parallel Group**: Wave 4 (with 14, 15, 16, 17)
  - **Blocks**: 24
  - **Blocked By**: None (can start independently)

  **Commit**: NO

---

- [x] 19. **Generate all per-document reports**

  **What to do**:
  - Execute: `python3 scripts/verify/generate_report.py`
  - Verify all reports generated correctly
  - Check: one report per archive document, master summary exists
  - Evidence stored in `audit/verification/reports/`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 14-18 — can run concurrently)
  - **Parallel Group**: Wave 4 (with 14, 15, 16, 17, 18)
  - **Blocks**: 20
  - **Blocked By**: 13 (generate_report.py), 14, 15, 16, 17 (needs their output)

  **Commit**: NO (evidence)

---

- [x] 20. **Review quote mismatches above threshold**

  **What to do**:
  - Load the quote-verify-master.json output
  - For each quote scored below threshold:
    - Read the quote from the archive
    - Read the best-match excerpt from the PDF
    - Classify: TRANSLATION_VARIATION (acceptable — different translation used) or ERROR (archive misquotes the text)
    - For TRANSLATION_VARIATION: add note to report, auto-accept
    - For ERROR: record in remediation queue
  - Compile a remediation list for Task 25

  **Must NOT do**:
  - Do NOT fix anything yet — this is analysis only
  - Do NOT over-classify as ERROR when it's clearly a different translation edition

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 21, 22, 23, 24)
  - **Parallel Group**: Wave 5 (with 21, 22, 23, 24)
  - **Blocks**: 25
  - **Blocked By**: 14, 19

  **Commit**: NO

---

- [x] 21. **Review broken cross-references**

  **What to do**:
  - Load cross-ref validation report
  - For each broken or low-confidence cross-reference:
    - Read the claim context around the reference
    - Read the target document
    - Determine: fix the link path, fix the claim, or accept as broad-concept reference
  - Compile remediation list for Task 26

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 20, 22, 23, 24)
  - **Parallel Group**: Wave 5 (with 20, 22, 23, 24)
  - **Blocks**: 26
  - **Blocked By**: 15, 19

  **Commit**: NO

---

- [x] 22. **Review numerical inconsistencies**

  **What to do**:
  - Load numerical consistency report
  - For each conflict, determine correct value (check INDEX, check canonical source)
  - Compile remediation list for Task 27

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 20, 21, 23, 24)
  - **Parallel Group**: Wave 5 (with 20, 21, 23, 24)
  - **Blocks**: 27
  - **Blocked By**: 16, 19

  **Commit**: NO

---

- [x] 23. **Review NHI source mismatches**

  **What to do**:
  - Load NHI verification report
  - For each mismatch: classify as translation-variation (different quoting style) or error
  - Compile remediation for Task 28

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 20, 21, 22, 24)
  - **Parallel Group**: Wave 5 (with 20, 21, 22, 24)
  - **Blocks**: 28
  - **Blocked By**: 17, 19

  **Commit**: NO

---

- [x] 24. **Generate master audit summary**

  **What to do**:
  - Using all verification results and review outputs, finalize `audit/verification/00-audit-master.md`
  - Structure:
    ```
    # Chronos Archive — Deep Fact-Check Audit Master Summary

    **Audit Date**: 2026-05-18
    **Version**: Current (main)
    **Tolerance**: Zero errors

    ## Summary
    | Metric | Value |
    |--------|-------|
    | Documents audited | 28 |
    | Total claims checked | N |
    | Errors found | N |
    | Flags requiring review | N |
    | Error rate | X% |

    ## Per-Document Verdicts
    | Document | Quotes | Cross-Refs | Links | Numeric | NHI | External | Verdict |
    |----------|--------|------------|-------|---------|-----|----------|---------|
    | ... | ... | ... | ... | ... | ... | ... | PASS/FAIL |

    ## Error Details
    ### Critical Errors
    1. [file.md]: [description of error]

    ### Warnings / Flags
    1. [file.md]: [description of flag]

    ## Recommendations
    - [Action items before certification]
    ```
  - Include the remediation list from Tasks 20-23
  - Print overall verdict: PASS (if zero errors) or FAIL (if errors remain)

  **Parallelization**:
  - **Can Run In Parallel**: YES (with 20, 21, 22, 23)
  - **Parallel Group**: Wave 5 (with 20, 21, 22, 23)
  - **Blocks**: 30 (re-verification triggers after fixes)
  - **Blocked By**: 19 (reports generated)

  **Commit**: NO (updated after fixes)

---

- [x] 25. **Fix all confirmed quote errors** (0 errors found — all translation variation)

  **What to do**:
  - For each quote classified as ERROR in Task 20:
    - Edit the archive file to match the correct source text
    - Record the change in the audit report
    - Commit each fix with descriptive message

  **Must NOT do**:
  - Do NOT change the interpretation — only fix the quoted text
  - Do NOT batch-fix unrelated files in one commit

  **Parallelization**:
  - **Can Run In Parallel**: NO (sequential — one fix at a time, multiple files)
  - **Parallel Group**: Wave 6 (sequential within wave)
  - **Blocks**: 30
  - **Blocked By**: 20

  **Commit**: YES (per-fix commits)
  - Message: `fix(audit): correct quoted passage in {file} — {description}`

---

- [x] 26. **Fix all broken cross-references**

  **What to do**:
  - For each broken cross-reference from Task 21:
    - If link path is wrong: fix the markdown link
    - If claim doesn't match target: correct the claim or change the reference target
    - If target section doesn't exist: add section anchor or remove reference
  - Commit each fix

  **Parallelization**:
  - **Can Run In Parallel**: With 27, 28, 29 within Wave 6
  - **Parallel Group**: Wave 6 (with 27, 28, 29)
  - **Blocks**: 30
  - **Blocked By**: 21

  **Commit**: YES (per-fix commits)

---

- [x] 27. **Fix all numerical inconsistencies**

  **What to do**:
  - For each numerical conflict from Task 22:
    - Determine the globally correct value
    - Update all documents to use the correct value
  - Examples: "13 source texts" → "14 source texts", "7 analyses" → "14 analyses"
  - Commit each fix

  **Parallelization**:
  - **Can Run In Parallel**: With 26, 28, 29 within Wave 6
  - **Parallel Group**: Wave 6 (with 26, 28, 29)
  - **Blocks**: 30
  - **Blocked By**: 22

  **Commit**: YES (per-fix commits)

---

- [x] 28. **Fix NHI source quote issues** (0 errors found — all paraphrase/accepted)

  **What to do**:
  - For each NHI source mismatch from Task 23:
    - Correct the quote in 12-NHI-correlation.md to match the evidence extract
    - Commit fix

  **Parallelization**:
  - **Can Run In Parallel**: With 26, 27, 29 within Wave 6
  - **Parallel Group**: Wave 6 (with 26, 27, 29)
  - **Blocks**: 30
  - **Blocked By**: 23

  **Commit**: YES

---

- [x] 29. **Fix link integrity issues** (267→2 broken links — only 2 template placeholders remain)

  **What to do**:
  - For each broken link from Task 8:
    - Fix the link path in the markdown file
    - If target file was moved/deleted, update or remove the link
    - Commit fix

  **Parallelization**:
  - **Can Run In Parallel**: With 26, 27, 28 within Wave 6
  - **Parallel Group**: Wave 6 (with 26, 27, 28)
  - **Blocks**: 30
  - **Blocked By**: 8 (link check results)

  **Commit**: YES (per-fix commits)

---

- [x] 30. **Re-run full verification suite after fixes**

  **What to do**:
  - Re-run ALL verification scripts:
    - `verify_quotes.py` — should now show zero errors
    - `verify_cross_refs.py` — should now show zero broken refs
    - `verify_numerical.py` — should now show zero conflicts
    - `verify_nhi_sources.py` — should now show zero mismatches
    - `verify_links.py` — should now show zero broken links
  - Confirm error count is ZERO
  - If errors remain → return to fix tasks
  - Update master audit summary with final results

  **Parallelization**:
  - **Can Run In Parallel**: NO (sequential — must run all scripts)
  - **Parallel Group**: Wave 7 (with 31, 32, 33)
  - **Blocks**: 31
  - **Blocked By**: 25, 26, 27, 28, 29 (all fixes applied)

  **Commit**: NO (verification)

---

- [x] 31. **Verify zero errors achieved**

  **What to do**:
  - Review re-verification output
  - Confirm every document now has PASS verdict
  - Confirm no unresolved flags remain
  - If ZERO errors: proceed to certification
  - If >0 errors: document remaining issues, return to appropriate fix task

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 7 (with 30, 32, 33)
  - **Blocks**: 32
  - **Blocked By**: 30

  **Commit**: NO

---

- [x] 32. **Generate certification document**

  **What to do**:
  - Create `audit/verification/certification.md`
  - Structure:
    ```
    # Chronos Archive — Fact-Check Certification

    **Certification Date**: 2026-05-18
    **Version**: main@{commit}
    **Status**: CERTIFIED

    ## Verification Scope
    - Documents audited: 28
    - Total claims verified: N
    - Error rate: 0%

    ## Certified Verdict
    [ ] All source quotes verified against PDF source texts
    [ ] All cross-references validated
    [ ] All numerical claims internally consistent
    [ ] All markdown links resolve
    [ ] All NHI source quotes verified against evidence extracts
    [ ] External source checks passed

    This certifies that every factual claim in the Chronos Archive
    has been verified and found accurate.
    ```
  - Include the commit hash of the audited version
  - List the verification toolkit version

  **Parallelization**:
  - **Can Run In Parallel**: With 30, 31, 33 within Wave 7
  - **Parallel Group**: Wave 7 (with 30, 31, 33)
  - **Blocks**: None
  - **Blocked By**: 31

  **Commit**: YES
  - Message: `docs(audit): add fact-check certification — zero errors`

---

- [ ] 33. **Commit and push verification toolkit and reports**

  **What to do**:
  - Commit the full `scripts/verify/` toolkit
  - Commit `audit/verification/` reports and certification
  - Push to remote
  - Write summary for user

  **Parallelization**:
  - **Can Run In Parallel**: NO (must come last)
  - **Parallel Group**: Wave 7 (serial)
  - **Blocks**: None (final task)
  - **Blocked By**: 30, 31, 32

  **Commit**: YES (grouped)
  - Message: `feat(scripts): add reusable verification toolkit with audit reports`
  - Files: `scripts/verify/*`, `audit/verification/*`

---

## Final Verification Wave

> 4 review agents run in PARALLEL after all tasks complete. ALL must APPROVE.

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. Verify: All Must Haves implemented? All Must NOT Haves absent? Evidence files exist? Per-document reports generated? Master audit summary complete? Certification document exists? Script suite committed?
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT`

- [ ] F2. **Verification Script Quality Review** — `unspecified-high`
  Review all scripts in `scripts/verify/`: Do they handle errors? Do they report clearly? Are thresholds configurable? Is the code readable and maintainable? Run `python3 scripts/verify/run_all.py --dry-run` to validate structure.
  Output: `Scripts [N clean/N issues] | VERDICT`

- [ ] F3. **Real Audit Re-Run** — `unspecified-high`
  Start from clean state (no pre-existing extracted text). Run `python3 scripts/verify/run_all.py` fresh. Verify that all outputs are regenerated, all evidence files created, and final certification is achievable.
  Output: `Run [PASS/FAIL] | Evidence [N files] | Cert [ACHIEVED/FAILED] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `deep`
  For each task in the plan: verify the "What to do" matches what was actually built. Check that no scope creep occurred. Verify that the amnesia hypothesis was not altered — only factual claims were verified. Check that no external academic deep-dive research was done beyond standard references.
  Output: `Tasks [N/N compliant] | Scope Creep [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

| Task | Type | Message | Files |
|------|------|---------|-------|
| 2-5 | `feat(scripts)` | `feat(scripts): add verification toolkit scaffolding` | `scripts/verify/*` |
| 9-12 | `feat(scripts)` | `feat(scripts): add verification engine scripts` | `scripts/verify/verify_*.py` |
| 13 | `feat(scripts)` | `feat(scripts): add report generator` | `scripts/verify/generate_report.py` |
| 25 | `fix(audit)` | `fix(audit): correct quoted passage in {file}` | Modified analysis file |
| 26 | `fix(audit)` | `fix(audit): correct cross-reference in {file}` | Modified analysis file |
| 27 | `fix(audit)` | `fix(audit): correct numerical inconsistency — {value}` | Modified analysis file(s) |
| 28 | `fix(audit)` | `fix(audit): correct NHI source quote in 12-NHI-correlation.md` | `audit/12-NHI-correlation.md` |
| 29 | `fix(audit)` | `fix(audit): correct broken link in {file}` | Modified file |
| 32 | `docs(audit)` | `docs(audit): add fact-check certification — zero errors` | `audit/verification/certification.md` |
| 33 | `feat(scripts)` | `feat(scripts): add reusable verification toolkit with audit reports` | `scripts/verify/*`, `audit/verification/*` |

---

## Success Criteria

### Verification Commands
```bash
# Run the full verification suite
python3 scripts/verify/run_all.py

# Expected output:
# [QUOTES] N checked, N passed, N flagged
# [LINKS] N checked, N broken
# [CROSS-REFS] N checked, N broken, N low-confidence
# [NUMERICAL] N checked, N conflicts
# [NHI] N checked, N mismatches
# [REPORTS] Generated for N documents
# [VERDICT] PASS (0 errors) / FAIL (N errors remaining)
```

### Final Checklist
- [ ] All "Must Have" present — zero errors, all documents certified
- [ ] All "Must NOT Have" absent — no PDF modifications, no hypothesis alteration
- [ ] All tests pass — verification suite runs cleanly
- [ ] Certification document exists at `audit/verification/certification.md`
- [ ] Reusable toolkit committed at `scripts/verify/`
- [ ] All fixes committed
