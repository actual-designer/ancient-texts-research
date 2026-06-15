
## 2026-05-20: Cross-reference link fixes

### Files modified
- `audit/10-correlation-map.md`: Fixed 177 links — added `analyses/` prefix to all per-text analysis file targets (e.g., `](gilgamesh.md)` → `](analyses/gilgamesh.md)`)
- `audit/12-NHI-correlation.md`: Fixed 5 links — cleaned up ugly `[audit/...]` link text to human-readable text while keeping correct targets
- `audit/00-INDEX.md`: Fixed 1 link — `../claude.md` → `claude.md`

### Method
Used Python script with negative lookbehind regex to avoid double-prefixing `](analyses/target.md)` or `](../target.md)` patterns. Per-text filenames were targetted specifically to avoid affecting synthesis doc links.

### Verification
Dynamic check confirmed zero remaining broken per-text analysis links in all three files.
