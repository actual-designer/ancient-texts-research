# Writing Style Audit — Chronos Archive

## TL;DR

> **Quick Summary**: Audit all audit markdown documents for two specific writing-style issues: (1) overuse of em dashes (—) in prose passages, and (2) presence of AI-ism vocabulary. Propose targeted fixes that preserve factual content and the project's distinctive methodological voice.
>
> **Deliverables**:
> - Em dash audit report per file with recommended reductions
> - AI-ism sweep with classification (found / not found / context-appropriate)
> - Targeted edits across ~8 files with highest em dash density
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: Em dash context analysis → file-by-file prose edits → verification

---

## Context

### Original Request
Analyse the audits and plan fixes for the writing style with feedback:
1. Too much use of em dashes — reduce usage (looks like an AI-ism)
2. Search for typical AI-isms, words and expressions, and plan for replacement
3. Only propose necessary changes — this is an audit, not a demand
4. Goal: tweak style of prose, not impact quality of text
5. "Utmost care for the original texts" — truth-seeking mission

### Interview Summary
**Research Conducted**:
- Read representative samples from all 26 markdown files across `audit/` and `audit/analyses/`
- Counted em dashes per file (total 969 across corpus)
- Searched for 25+ common AI-ism patterns across entire corpus
- Distinguished between em dash usage categories (table cells vs. titles vs. prose)

**Key Discoveries**:
- **Em dashes are genuinely overused** in prose passages across 5 high-density files (yoga-sutras, unified-hypothesis, theogony, zoroastrian-gathas, poetic-edda)
- **AI-isms are essentially absent** — the writing has a distinctive, original voice. Zero occurrences of: delve, unpack, leverage, myriad, plethora, testament, tapestry, nuanced, multifaceted, paramount, cornerstone, and 15+ other common AI-ism patterns
- The "This is not... This is..." and "reads as" patterns are the project's **deliberate methodological voice**, not AI-isms — these must be preserved
- 8 analysis files already have **zero em dashes** — no changes needed

### Metis Review
**Gaps Identified** (addressed):
- Need clear guardrails around what NOT to change (blockquotes, table cells, titles, source text)
- Need replacement strategy for prose em dashes (colon vs. semicolon vs. comma vs. rewrite)
- Need aggressive threshold defined — conservative vs. thorough
- Need to verify em dashes in entity-registry table cells vs. prose before committing
- Edge case: em dashes in classification headers (`SPECIES WITH AMNESIA -- Working Hypothesis` use double-hyphens, not em dashes, so they're fine)

---

## Work Objectives

### Core Objective
Audit and clean up prose style across all audit documents: reduce em dash overuse and flag any AI-isms, while preserving factual content and the project's distinctive analytical voice.

### Concrete Deliverables
- Per-file em dash audit with counts and recommended reduction plan
- AI-ism sweep report (verification that none exist)
- Targeted prose edits across ~8 files (replacing em dashes with colons/commas/semicolons or restructuring sentences)
- Final verification that source text quotations were never modified

### Definition of Done
- [ ] All prose em dashes in target files reviewed and selectively replaced
- [ ] Zero source-text quotations modified
- [ ] Zero table-cell "—" markers removed
- [ ] Zero title/heading em dashes changed
- [ ] Zero methodological vocabulary harmed ("reads as", "this is not... this is...")
- [ ] AI-ism sweep confirms none found across corpus

### Must Have
- Reduce em dash count in prose by 50-70% across the 5 highest-density files
- Preserve ALL source text quotations exactly
- Preserve the project's distinctive voice and methodology

### Must NOT Have (Guardrails)
- Do NOT modify blockquotes / source text excerpts
- Do NOT modify table cell "—" markers (meaning "no cross-reference")
- Do NOT modify title or heading em dashes (`# Title — Subtitle`)
- Do NOT modify tier labels using "—" for formatting (`Tier 2 — Security/operations`)
- Do NOT change "This is not... This is..." reframing pattern
- Do NOT change "reads as" / "reads like" analytical vocabulary
- Do NOT touch the 8 files with zero em dashes
- Do NOT change any factual, technical, or interpretive content
- Do NOT introduce new AI-isms while removing existing patterns

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### QA Policy
Every task MUST include agent-executed verification. Primary verification is reading diffs and confirming patterns.

**Verification approach**:
- **Post-edit diff review**: Read all changed lines and confirm only em dashes changed, not content
- **Grep verification**: After edits, grep target files for remaining prose em dashes to confirm reduction target met
- **Blockquote guard**: Grep for em dashes in blockquoted lines — confirm zero changes there
- **Table guard**: Confirm table-cell "—" markers untouched

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation — can all run in parallel):
├── Task 1: Audit yoga-sutras.md prose em dashes
├── Task 2: Audit 11-unified-hypothesis.md prose em dashes
├── Task 3: Audit theogony-works-and-days.md prose em dashes
├── Task 4: Audit zoroastrian-gathas.md prose em dashes

Wave 2 (Independent — can all run in parallel):
├── Task 5: Audit poetic-edda.md prose em dashes
├── Task 6: Audit 01-entity-registry.md (verify table vs. prose distinction)
├── Task 7: Audit 09-location-registry.md (verify table vs. prose distinction)
├── Task 8: Audit 04-cross-references.md prose em dashes
├── Task 9: Audit 10-correlation-map.md (verify table vs. prose distinction)

Wave 3 (Auxiliary — can all run in parallel):
├── Task 10: Audit remaining low-density files (03-event-timeline, 08-translation-key, 02-technology-catalog)
├── Task 11: AI-ism sweep report (formal verification)
├── Task 12: Final verification pass — em dash reduction targets + guardrails

Max Concurrent: 5
```

---

## TODOs

- [ ] 1. **Audit prose em dashes — `analyses/yoga-sutras.md`** (HIGH priority — 85 em dashes in 298 lines)

  **What to do**:
  - Read `audit/analyses/yoga-sutras.md` in full
  - Identify every prose em dash that replaces a colon, parenthetical, or clause break
  - Replace with appropriate punctuation: colon (`:`) for explanations/appositives, semicolon (`;`) for related independent clauses, comma (`,`) for mild interruptions, or full stop (`.`) + new sentence
  - For the densest passages (Executive Summary headings 1-6, lines 15-20), consider sentence restructuring
  - Do NOT touch em dashes in: section headings (`# Title — Forensic Analysis`), `## INCIDENT N: Title — Subtitle`, blockquoted source material, inline Sanskrit terms in regular context

  **Must NOT do**:
  - Do not modify any source text in blockquotes
  - Do not change "This is not... This is..." pattern
  - Do not change "reads as" / "reads like" vocabulary
  - Do not change factual content — only punctuation and sentence structure

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Prose editing, punctuation replacement, sentence restructuring — pure textual refinement
  - **Skills**: `[]`
    - No specialized skills needed — this is careful prose editing with strict guardrails

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4)
  - **Blocks**: Task F1 (reduction verification)
  - **Blocked By**: None (can start immediately)

  **References**:
  - `audit/analyses/yoga-sutras.md` — The target file itself
  - Draft at `.sisyphus/drafts/writing-style-audit.md` — Em dash usage categories and guardrails

  **Acceptance Criteria**:
  - [ ] Prose em dash count reduced by 50-70% (from ~85 to ~25-42)
  - [ ] Zero blockquoted source texts modified
  - [ ] Zero table cells changed
  - [ ] Zero title/heading em dashes changed
  - [ ] All factual content preserved identically

  **QA Scenarios**:
  ```
  Scenario: Verify em dash reduction
    Tool: Bash (grep)
    Steps:
      1. Run: grep -c '—' audit/analyses/yoga-sutras.md
      2. Verify count is between 25 and 42 (50-70% reduction from ~85)
    Expected Result: Count is 25-42
    Failure Indicators: Count > 42 (insufficient reduction) or < 25 (over-aggressive)
    Evidence: .sisyphus/evidence/task-1-reduction-count.txt

  Scenario: Verify guardrails
    Tool: Bash (grep)
    Steps:
      1. Run: grep '^>' audit/analyses/yoga-sutras.md | grep '—'
         (should return zero lines — no blockquote dashes changed, but none existed before either)
      2. Run: grep '^##.*—' audit/analyses/yoga-sutras.md
         (verify heading dashes are preserved)
    Expected Result: No evidence of guardrail violations
    Evidence: .sisyphus/evidence/task-1-guardrails.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in yoga-sutras.md`
  - Files: `audit/analyses/yoga-sutras.md`


- [ ] 2. **Audit prose em dashes — `audit/11-unified-hypothesis.md`** (HIGH priority — 85 em dashes in 618 lines)

  **What to do**:
  - Read `audit/11-unified-hypothesis.md` in full
  - Identify all prose em dashes and replace with colons, semicolons, commas, or sentence breaks
  - Key passages with concentrated usage: Section 1 (Labor Problem), Section 5 (Operator Withdrawal)
  - Pay special attention to lines with multiple em dashes per sentence
  - Preserve all "This is not... This is..." reframing pattern and "reads as" analytical vocabulary

  **Must NOT do**:
  - Do not touch the "This is not... This is..." reframings
  - Do not touch source text blockquotes
  - Do not change factual content

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Prose em dash count reduced by 50-70% (from ~85 to ~25-42)
  - [ ] Zero guardrail violations

  **QA Scenarios**:
  ```
  Scenario: Em dash reduction verification
    Tool: Bash (grep)
    Steps:
      1. grep -c '—' audit/11-unified-hypothesis.md
    Expected Result: 25-42 remaining em dashes
    Evidence: .sisyphus/evidence/task-2-reduction-count.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in unified-hypothesis.md`
  - Files: `audit/11-unified-hypothesis.md`


- [ ] 3. **Audit prose em dashes — `analyses/theogony-works-and-days.md`** (HIGH priority — 44 em dashes in 261 lines)

  **What to do**:
  - Read `audit/analyses/theogony-works-and-days.md` in full
  - Replace prose em dashes with colons/semicolons/commas or sentence restructuring
  - Focus on the numbered findings in the Executive Summary (lines 13-20), which use "—" for each item
  - Also audit the prose passages in Incidents 1-8

  **Must NOT do**: Same guardrails as Tasks 1-2

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Prose em dash count reduced by 50-70% (from ~44 to ~13-22)
  - [ ] Zero guardrail violations

  **QA Scenarios**:
  ```
  Scenario: Em dash reduction verification
    Tool: Bash (grep)
    Steps:
      1. grep -c '—' audit/analyses/theogony-works-and-days.md
    Expected Result: 13-22 remaining em dashes
    Evidence: .sisyphus/evidence/task-3-reduction-count.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in theogony-works-and-days.md`
  - Files: `audit/analyses/theogony-works-and-days.md`


- [ ] 4. **Audit prose em dashes — `analyses/zoroastrian-gathas.md`** (HIGH priority — 41 em dashes in 189 lines)

  **What to do**:
  - Read `audit/analyses/zoroastrian-gathas.md` in full
  - Replace prose em dashes with appropriate punctuation
  - Focus on Executive Summary numbered findings (lines 13-18) and Incidents 1-6
  - Preserve the distinct analytical voice

  **Must NOT do**: Same guardrails as above

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Prose em dash count reduced by 50-70% (from ~41 to ~12-20)
  - [ ] Zero guardrail violations

  **QA Scenarios**:
  ```
  Scenario: Em dash reduction verification
    Tool: Bash (grep)
    Steps:
      1. grep -c '—' audit/analyses/zoroastrian-gathas.md
    Expected Result: 12-20 remaining em dashes
    Evidence: .sisyphus/evidence/task-4-reduction-count.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in zoroastrian-gathas.md`
  - Files: `audit/analyses/zoroastrian-gathas.md`


- [ ] 5. **Audit prose em dashes — `analyses/poetic-edda.md`** (HIGH priority — 40 em dashes in 321 lines)

  **What to do**:
  - Read `audit/analyses/poetic-edda.md` in full
  - Replace prose em dashes with colon/semicolon/commas or sentence restructuring
  - Focus on Executive Summary numbered findings (lines 13-20) and Incidents 1-7

  **Must NOT do**: Same guardrails as above

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7, 8, 9)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Prose em dash count reduced by 50-70% (from ~40 to ~12-20)
  - [ ] Zero guardrail violations

  **QA Scenarios**:
  ```
  Scenario: Em dash reduction verification
    Tool: Bash (grep)
    Steps:
      1. grep -c '—' audit/analyses/poetic-edda.md
    Expected Result: 12-20 remaining em dashes
    Evidence: .sisyphus/evidence/task-5-reduction-count.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in poetic-edda.md`
  - Files: `audit/analyses/poetic-edda.md`


- [ ] 6. **Verify table vs. prose em dashes — `audit/01-entity-registry.md`**

  **What to do**:
  - Read `audit/01-entity-registry.md`
  - Distinguish: most of the 108 em dashes are in table cells as "—" (no data) markers — these MUST NOT be changed
  - Identify the prose/tier-label em dashes (e.g., `Tier 2 — Security/operations`, `"—" associated with storms`)
  - For tier labels: replace "—" with `:` (e.g., `Tier 2: Security/operations`)
  - For prose em dashes in paragraph text: replace with colons or restructure
  - The actual count of changeable em dashes is likely ~15-20, not 108

  **Must NOT do**:
  - Do NOT touch any `| — |` table cell pattern (meaning "no cross-reference")
  - Do NOT touch the entity comparison table formatting

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 7, 8, 9)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Table cell "—" markers completely preserved (grep `| — |` shows same count)
  - [ ] Tier labels and prose em dashes appropriately reduced
  - [ ] Zero table formatting broken

  **QA Scenarios**:
  ```
  Scenario: Table cell marker preservation
    Tool: Bash (grep)
    Steps:
      1. grep -c '| — |' audit/01-entity-registry.md
      2. Compare with pre-edit count
    Expected Result: Same count as before edits
    Evidence: .sisyphus/evidence/task-6-table-markers.txt

  Scenario: Prose em dash reduction
    Tool: Bash (grep)
    Steps:
      1. Run grep -c '—' audit/01-entity-registry.md
      2. Subtract table cell counts from total
    Expected Result: Non-table em dashes reduced by 50%
    Evidence: .sisyphus/evidence/task-6-prose-reduction.txt
  ```

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in entity-registry.md`
  - Files: `audit/01-entity-registry.md`


- [ ] 7. **Verify table vs. prose em dashes — `audit/09-location-registry.md`**

  **What to do**: Same approach as Task 6. Most of the 95 em dashes are table cell "—" markers and table separator dashes. Identify and fix the small number of prose em dashes.

  **Must NOT do**: Do not touch table cell markers or table formatting.

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 6, 8, 9)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Table cell markers preserved
  - [ ] Prose em dashes reduced

  **QA Scenarios**: Same pattern as Task 6

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in location-registry.md`
  - Files: `audit/09-location-registry.md`


- [ ] 8. **Audit prose em dashes — `audit/04-cross-references.md`** (MODERATE priority — 50 em dashes, mixed)

  **What to do**:
  - Read `audit/04-cross-references.md`
  - Some em dashes are in table cells, some in prose
  - For table-based cross-references, leave as-is
  - For prose passages (e.g., cross-reference analyses), replace with colons or restructure sentences

  **Must NOT do**: Do not touch table cells.

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 6, 7, 9)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**: Prose em dashes reduced by 50-70%

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in cross-references.md`
  - Files: `audit/04-cross-references.md`


- [ ] 9. **Verify table vs. prose em dashes — `audit/10-correlation-map.md`** (MODERATE — 74 em dashes, mixed)

  **What to do**: Same approach as Task 6/7. Many em dashes are in correlation table structures. Identify and fix prose em dashes in analytical text passages.

  **Must NOT do**: Do not touch table cells.

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5, 6, 7, 8)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**: Prose em dashes reduced by 50-70%

  **Commit**: YES
  - Message: `style(audit): reduce em dash usage in correlation-map.md`
  - Files: `audit/10-correlation-map.md`


- [ ] 10. **Audit low-density files** (LOW priority — minor cleanup)

  **What to do**:
  - Review `audit/03-event-timeline.md` (31 em dashes), `audit/08-translation-key.md` (69 — mostly table), `audit/02-technology-catalog.md` (13 — mostly table)
  - For `event-timeline.md`: the dashes are in event descriptions — replace explanatory dashes with colons
  - For `translation-key.md` and `technology-catalog.md`: most are in tables — leave untouched. Only fix any prose paragraphs found outside tables.

  **Must NOT do**: Do not touch table cells

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 11, 12)
  - **Blocks**: Task F1
  - **Blocked By**: None

  **Acceptance Criteria**: Modest reduction in prose em dashes; table dashes untouched

  **Commit**: PER FILE
  - Message: `style(audit): reduce em dash usage in event-timeline.md`
  - Files: respective files


- [ ] 11. **AI-ism sweep — formal verification report**

  **What to do**:
  - Run comprehensive grep searches across entire `audit/` directory for ALL common AI-ism patterns
  - Generate a formal report confirming zero AI-isms found
  - Patterns to sweep: delve, unpack, leverage, myriad, plethora, testament, tapestry, nuanced, multifaceted, paramount, cornerstone, "it is worth noting", "it bears mentioning", "in order to", "in the context of", "having said that", "not only...but also", "essentially", "a myriad of", "a plethora of", "in essence" (as filler, not as source quote)
  - For any matches found: verify they are either source quotations or context-appropriate. If any true AI-ism is found, flag it for replacement.

  **Must NOT do**:
  - Do not change "This is not... This is..." — this is the project's core rhetorical device
  - Do not change "reads as" — core analytical vocabulary
  - Do not change "serves as" — functional descriptions
  - Do not change "ultimately" — narrative sequencing

  **Recommended Agent Profile**:
  - **Category**: `quick` (pure search task)
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 10, 12)
  - **Blocks**: Nothing
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Comprehensive sweep across all 26 markdown files
  - [ ] Report documenting which patterns were checked and results
  - [ ] Any actual AI-isms flagged with file:line and replacement suggestion

  **Commit**: NO (report only)
  - Evidence: `.sisyphus/evidence/task-11-ai-ism-sweep.txt`


- [ ] 12. **Final guardrail verification pass**

  **What to do**:
  - After ALL Tasks 1-10 are complete, run a comprehensive verification across all modified files
  1. Grep for em dashes in blockquoted lines — confirm zero
  2. Grep for `| — |` pattern — confirm same count as pre-edit (table cells untouched)
  3. Grep for `^#.*—` and `^##.*—` — confirm title/heading dashes preserved
  4. Grep for "This is not" and "reads as" — confirm patterns intact
  5. For each modified file, do an em dash count and verify reduction target met

  **Must NOT do**: Do not make any further changes — this is verification only

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 10, 11)
  - **Blocks**: Task F2
  - **Blocked By**: Tasks 1-10

  **Acceptance Criteria**:
  - [ ] All guardrails verified across all modified files
  - [ ] Report generated listing each guardrail check and result

  **Commit**: NO (verification only)
  - Evidence: `.sisyphus/evidence/task-12-guardrail-verification.txt`

---

## Final Verification Wave (MANDATORY)

- [ ] F1. **Em Dash Reduction Audit** — Verify em dash counts per file before/after. Confirm each target file achieved 50-70% reduction in prose em dashes. Confirm zero changes to table cells, blockquotes, titles, or headings.

- [ ] F2. **Guardrail Compliance** — Run grep for each guardrail: confirm no blockquotes modified, no table cells modified, no "This is not..." patterns altered, no "reads as" patterns altered.

- [ ] F3. **Accuracy Verification** — Spot-check 3-5 random changes per file: read original context, read new context, confirm no meaning changed, no factual error introduced.

- [ ] F4. **AI-ism Re-sweep** — Re-run all AI-ism searches post-edits to confirm no new AI-isms were introduced.

---

## Commit Strategy

- **Groups by file**: One commit per file to keep changes atomic and reviewable
- **Message format**: `style(audit): reduce em dash usage in [file]`
- **Pre-commit**: Diff review to confirm content accuracy

---

## Success Criteria

### Verification Commands
```bash
# Before/after em dash counts per file
grep -c '—' audit/analyses/yoga-sutras.md
grep -c '—' audit/11-unified-hypothesis.md
# etc.

# Confirm no table cell em dashes were changed
grep '| — |' audit/01-entity-registry.md | wc -l

# Confirm no blockquote em dashes were changed
grep '^>.*—' audit/11-unified-hypothesis.md

# AI-ism sweep
grep -rnw 'delve\|unpack\|leverage\|myriad\|plethora\|testament\|tapestry\|nuanced\|multifaceted\|paramount\|cornerstone' audit/
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] All em dash reductions verified
- [ ] Zero source text alterations
