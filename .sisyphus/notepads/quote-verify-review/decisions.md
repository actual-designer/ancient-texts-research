# Decisions

## 2026-05-20: Quote verification review

- **Classification scheme**: Three categories for non-PASS entries — TRANSLATION_VARIATION (different translation edition), NOT_A_QUOTE (archive analysis text), UNVERIFIABLE (scanned PDF)
- **Error threshold**: Very conservative — only classified as ERROR if the archive clearly fabricated or misattributed a quote. No such cases found.
- **Verification method**: Manual pdftotext extraction and comparison used for Gilgamesh and Enoch PDFs where verification tool failed to extract text
- **NO_MATCH null-PDF entries**: Classified as NOT_A_QUOTE or ANALYSIS_WITH_EMBEDDED_REFERENCES rather than TRANSLATION_VARIATION because these were never intended as verbatim PDF quote extracts
