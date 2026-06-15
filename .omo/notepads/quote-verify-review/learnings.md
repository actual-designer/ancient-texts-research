# Learnings

## 2026-05-20: Quote verification review

- **280 total entries**: 64 PASS, 24 FLAGGED, 174 NO_MATCH, 18 UNVERIFIABLE
- **Zero errors found** — all non-PASS entries are translation variations or archive analysis text
- FLAGGED: 20 from ezekiel-merkabah.md vs eze.pdf (NET Bible), 4 from revelation.md vs bookofrevelation.pdf (NET Bible)
- NO_MATCH with source_pdf: 27 Gilgamesh + 23 Enoch — text verified as matching via pdftotext; NO_MATCH due to verification tool extraction limitations (empty best_excerpt)
- NO_MATCH null source_pdf: 124 entries of archive analysis text — incorrectly included in verification corpus
- UNVERIFIABLE: 18 entries from theogony-works-and-days.md + zoroastrian-gathas.md (scanned PDFs)
- Key finding: The verification tool's PDF extraction fails on Gilgamesh and Enoch PDFs despite text being extractable by pdftotext
