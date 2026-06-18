# Broadsheet Celestial Events — Gap Evidence Analysis

## TL;DR

> **Quick Summary**: Analyze 7 historical celestial phenomenon events (1535–1917 CE) through the Chronos Archive's literalist/technological lens, applying the Archive's own correlation criteria as a signal/noise filter. These events populate the Archive's most vulnerable gap — the "Reduced Contact / Silent Period" (573 BCE – 1975 CE) — providing the first witness-account evidence for that interval.
>
> **Deliverables**:
> - `audit/14-broadsheet-celestial-events.md` — new synthesis addendum (800–1,500 lines) with signal/noise methodology, per-event incident breakdowns, and integration synthesis
> - Updated `audit/00-INDEX.md` — new doc registered
> - Updated `audit/03-event-timeline.md` — 6 gap-period entries (1535, 1554×2, 1561, 1566, 1665, 1917)
> - Updated `audit/12-NHI-correlation.md` — cross-reference in §3.5 (Timeline Tension)
> - Updated `audit/04-cross-references.md` — parallels to ancient celestial battle accounts
> - Updated `README.md` — new doc in architecture + First Doorways
> - Updated `audit/10-correlation-map.md` — new doc in linking blueprint
> - Updated `audit/11-unified-hypothesis.md` — cross-reference only (no rewriting of Finding 7)
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 4 waves
> **Critical Path**: Research (Wave 1) → Document Creation (Wave 2) → Integration (Wave 3) → Verification (Final)

---

## Context

### Original Request

The user provided 7 historical celestial phenomenon events that share similarities with the 1561 Nuremberg celestial phenomenon, asking the Chronos Archive to consider analyzing them. The user explicitly requested "reasons against analyzing any of the events" — a signal/noise filter — stating the goal is "searching for signal in the noise."

The events:
1. **Vädersolstavlan** — Stockholm, 1535 (sun dog display, painted with geometric accuracy)
2. **Miracle Sign above Waldeck Castle** — Kemnath, Germany, 1554 (Hans Glaser broadsheet)
3. **The Plech Sky Spectacular** — Germany, 1554 (broadsheet tradition)
4. **1561 Celestial Phenomenon over Nuremberg** (reference event, Glaser broadsheet)
5. **1566 Celestial Phenomenon over Basel** (black spheres fighting, crumbled and extinguished)
6. **1665 Celestial Phenomenon over Stralsund** (warships battling + hovering plate)
7. **The Miracle of the Sun — Fátima, Portugal, 1917** (30K–100K witnesses)

### Interview Summary

**Key Discussions**:
- **Signal/noise assessment**: Applied the Archive's own correlation criteria (12-NHI §2: structural overlap required, thematic resemblance excluded, "minimal counter-explanation test"). Categorized events as HIGH SIGNAL (Basel, Nuremberg, Stralsund), CONTROL BASELINE (Stockholm), SOURCE CREDIBILITY CONTEXT (Waldeck, Plech), and COMPLEX (Fátima).
- **Document structure**: User chose single synthesis addendum (`audit/14-broadsheet-celestial-events.md`) matching the 12-NHI / 13-NDE pattern, with per-event breakdowns inside.
- **Fátima treatment**: User chose genuine mass-sighting event (full literal reconstruction) with dedicated counter-explanation subsection.
- **Sources**: Web/scholarly only (Wikipedia + Vallée, Magin, Schwarte, Jaki). No new PDFs.
- **Integration scope**: Full integration across 7 existing documents.
- **Capstone impact**: 11-unified-hypothesis.md gets cross-reference only — broadsheet events are witness observations, not operator-to-human contacts. The "Silent Period" finding holds.

**Research Findings**:
- None of the 7 events appear anywhere in the repo (all searches returned zero matches).
- 13-NDE (2,039 lines, 13 thematic sections) is the structural template for modern-evidence addenda.
- 03-event-timeline.md explicitly labels 573 BCE → 1975 CE as "Reduced Contact / Silent Period" in its Mermaid Gantt chart. These events would be the FIRST entries in this gap.
- 12-NHI §3.5 ("How NHI Evidence Might Resolve the Ambiguity") provides a 6-row discrimination framework. These events map directly onto it.
- 12-NHI scope is post-1947; no pre-1947 historical sightings are currently documented.

### Metis Review

**Identified Gaps** (addressed):
- **11-unified-hypothesis.md omission**: Metis flagged that the capstone references "SILENCE (Post-573 BCE → Present)" 6+ times. Resolved: cross-reference only, no rewriting. Finding 7 ("autonomous test phase") holds because these are witness accounts, not operator contacts.
- **README.md + 10-correlation-map.md omission**: Metis flagged navigation rot. Resolved: added to integration list.
- **Filename convention deviation**: Metis noted 12/13 use `-correlation.md` suffix. Resolved: `14-broadsheet-celestial-events.md` is acceptable — these are historical events, not a "correlation" analysis.
- **Stockholm 4-part framework treatment**: Metis flagged ambiguity. Resolved: modified 4-part treatment where Literal Reconstruction = atmospheric optics analysis (establishing the noise baseline).
- **Fátima scope creep risk**: Metis flagged Marian theology/secrets expansion. Resolved: locked to October 13 aerial phenomenon. Prior visions max 2 sentences. Three secrets max 1 paragraph.
- **Citation standard for web sources**: Metis flagged inconsistency risk. Resolved: `(Source Title, URL, accessed YYYY-MM-DD)` for web; `(Author, Work, Year, Page)` for books.
- **Line count ceiling**: Metis flagged padding risk. Resolved: 800–1,500 lines hard limit.
- **Source availability uncertainty**: Metis flagged thin sourcing for some events. Resolved: cite what's available, flag thin sourcing explicitly, reduce Waldeck/Plech to footnote if sources don't establish Glaser's commercial pattern.

---

## Work Objectives

### Core Objective

Analyze 7 historical celestial phenomenon events (1535–1917 CE) through the Archive's literalist/technological lens, applying the Archive's own correlation criteria as a signal/noise filter, to provide the first witness-account evidence for the 573 BCE – 1975 CE "Silent Period" gap.

### Concrete Deliverables

- `audit/14-broadsheet-celestial-events.md` (new, 800–1,500 lines)
- 7 existing files updated with cross-references and timeline entries

### Definition of Done

- [x] `python3 scripts/validate-links.py` exits 0 with zero errors
- [x] `audit/14-broadsheet-celestial-events.md` exists, 800–1,500 lines
- [x] Every HIGH SIGNAL and COMPLEX event has all 4 framework sections (Source Material, Mainstream Interpretation, Literal Reconstruction, Plausible Mechanism)
- [x] Stockholm is tagged `CONTROL BASELINE` and NOT treated as anomalous
- [x] Waldeck/Plech appear ONLY in a "Source Credibility Context" subsection, NOT as standalone incidents
- [x] `audit/00-INDEX.md` contains entry for `14-broadsheet-celestial-events.md`
- [x] `audit/03-event-timeline.md` contains entries for 1535, 1554, 1561, 1566, 1665, 1917
- [x] `audit/12-NHI-correlation.md` §3.5 contains cross-reference to 14-broadsheet
- [x] `audit/04-cross-references.md` contains parallels to ancient celestial battle accounts
- [x] `README.md` lists the new doc in Project Architecture section
- [x] No unauthorized theological language outside quoted source material

### Must Have

- Signal/noise methodology section applying the Archive's own correlation criteria (12-NHI §2) to classify the 7 events
- Full 4-part framework analysis (Source → Mainstream → Literal Reconstruction → Plausible Mechanism) for HIGH SIGNAL events (Basel 1566, Nuremberg 1561, Stralsund 1665) and COMPLEX event (Fátima 1917)
- Stockholm 1535 as CONTROL BASELINE with atmospheric optics analysis
- Waldeck 1554 + Plech 1554 as Source Credibility Context (Glaser broadsheet pattern)
- Fátima counter-explanation subsection (Jaki's atmospheric optics, expectation bias)
- Classification header (`**Classification:** SPECIES WITH AMNESIA -- Working Hypothesis` + `**Analyst:** The Chronos Archive, Lead Investigator`)
- Signal-strength tag on every event section (`**Signal Strength:** HIGH | CONTROL | CONTEXT ONLY | COMPLEX`)
- Cross-references to existing Archive documents (12-NHI §3.5, 03-timeline, 04-cross-refs, ancient celestial battle accounts)
- Executive Summary with numbered findings (matching 12-NHI / 13-NDE pattern)
- Every factual claim cited (web sources with URL + access date; books with author/work/year/page)

### Must NOT Have (Guardrails)

- NO new PDFs in `texts/` — these are historical witness events, not canonical source texts
- NO per-event standalone files in `audit/analyses/` — that directory is for source-text PDF deep dives only
- NO events beyond the 7 specified (no Tunguska, no Aurora 1897, no Kenneth Arnold)
- NO Fátima analysis beyond the October 13, 1917 aerial phenomenon (no Marian theology, no three secrets analysis, no prophetic interpretation beyond 1 paragraph context)
- NO Stockholm treated as anomalous — it is the CONTROL BASELINE
- NO Waldeck/Plech as standalone incidents with 4-part framework entries — they are Source Credibility Context only
- NO modern UFO comparisons beyond cross-references to 12-NHI (this is NOT a second NHI correlation document)
- NO rewriting of 11-unified-hypothesis.md Finding 7 ("autonomous test phase") — cross-reference only
- NO theological language outside quoted source material ("miracle," "divine intervention," "supernatural" only in quotes)
- NO Hans Glaser psychological speculation beyond what sources document — commercial broadsheet pattern only, with source attribution
- NO padding to match 13-NDE's 2,039 lines — density over length, 1,500 line hard ceiling
- NO Mermaid diagrams beyond 2 maximum (signal-strength classification + event timeline if useful)

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed. No exceptions.
> This is a markdown-only research repo — no code, no build system, no test runner.
> Verification = link integrity + framework compliance + structural format match.

### Test Decision
- **Infrastructure exists**: YES (`scripts/validate-links.py` — cross-reference link validator)
- **Automated tests**: None (no unit tests for markdown research)
- **Framework**: N/A
- **Agent QA**: ALWAYS — the primary verification method for all tasks

### QA Policy
Every task includes agent-executed QA scenarios. Evidence saved to `.omo/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Link integrity**: `python3 scripts/validate-links.py` → exit code 0, 0 errors
- **Framework compliance**: Grep verification that every HIGH/COMPLEX event has all 4 framework sections
- **Structural format**: Read document headers, verify classification + signal-strength tags
- **Integration completeness**: Grep each target file for expected cross-references
- **Tone check**: Grep for unauthorized theological language outside quotes
- **Line count**: `wc -l` verification within 800–1,500 range

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Research — 7 parallel tasks, gather source material):
├── Task 1: Research 1561 Nuremberg [deep]
├── Task 2: Research 1566 Basel [deep]
├── Task 3: Research 1535 Stockholm Vädersolstavlan [deep]
├── Task 4: Research 1554 Waldeck + Plech (Glaser pattern) [quick]
├── Task 5: Research 1665 Stralsund [deep]
├── Task 6: Research 1917 Fátima [deep]
└── Task 7: Research scholarly context (Vallée, Magin, Schwarte, broadsheet tradition) [deep]

Wave 2 (Document Creation — 1 task, assembles all research):
└── Task 8: Write audit/14-broadsheet-celestial-events.md [deep]
    (depends: ALL Wave 1 tasks)

Wave 3 (Integration — 5 parallel tasks, update existing docs):
├── Task 9: Update audit/00-INDEX.md [quick] (depends: 8)
├── Task 10: Update audit/03-event-timeline.md [quick] (depends: 8)
├── Task 11: Update audit/12-NHI-correlation.md §3.5 [quick] (depends: 8)
├── Task 12: Update audit/04-cross-references.md [quick] (depends: 8)
└── Task 13: Update README.md + 10-correlation-map.md + 11-unified-hypothesis.md [quick] (depends: 8)

Wave FINAL (Verification — 4 parallel reviews):
├── Task F1: Plan compliance audit [oracle]
├── Task F2: Code quality review (validate-links + framework) [unspecified-high]
├── Task F3: Manual QA (read doc, verify format) [unspecified-high]
└── Task F4: Scope fidelity check [deep]
→ Present results → Get explicit user okay

Critical Path: Task 1-7 (parallel) → Task 8 → Task 9-13 (parallel) → F1-F4 → user okay
Parallel Speedup: ~60% faster than sequential
Max Concurrent: 7 (Wave 1)
```

### Dependency Matrix

| Task | Depends On | Blocks |
|------|-----------|--------|
| 1-7 | None (start immediately) | 8 |
| 8 | 1, 2, 3, 4, 5, 6, 7 | 9, 10, 11, 12, 13 |
| 9 | 8 | F1-F4 |
| 10 | 8 | F1-F4 |
| 11 | 8 | F1-F4 |
| 12 | 8 | F1-F4 |
| 13 | 8 | F1-F4 |
| F1-F4 | 9, 10, 11, 12, 13 | user okay |

### Agent Dispatch Summary

- **Wave 1**: **7** — T1-T3, T5-T7 → `deep`, T4 → `quick`
- **Wave 2**: **1** — T8 → `deep`
- **Wave 3**: **5** — T9-T13 → `quick`
- **FINAL**: **4** — F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [x] 1. Research 1561 Nuremberg Celestial Phenomenon

  **What to do**:
  - Fetch the Wikipedia article: `https://en.wikipedia.org/wiki/1561_celestial_phenomenon_over_Nuremberg`
  - Extract: full event description, date (April 14, 1561), witness accounts, Hans Glaser's broadsheet text (the complete English translation if available), description of the woodcut illustration, objects reported (cylinders, crosses, globes, "blood-red" crescent, black spear, "sun and moon" signs), duration, reported "combat" or "aerial battle" behavior, reported crashes/falls
  - Search for scholarly analysis: search for "Ulrich Magin Nuremberg 1561", "Wiebke Schwarte Nuremberg broadsheet", "Jacques Vallée Nuremberg 1561" — extract their interpretations (atmospheric optics vs. anomaly vs. control system)
  - Extract the specific detail that "the Nuremberg broadsheet doesn't neatly fit a classic sun dog description" — find which scholar says this and why
  - Document the broadsheet's cultural context: Reformation-era Nuremberg, mass-produced woodcut news pamphlets, religious anxiety, omen interpretation
  - Note any discrepancies between the broadsheet text and the woodcut illustration

  **Must NOT do**:
  - Do NOT write the actual analysis document (that's Task 8)
  - Do NOT analyze the event through the Archive's lens yet — just gather raw source material
  - Do NOT add PDFs to texts/
  - Do NOT fetch post-1947 UFO sources

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Multi-source web research requiring synthesis of primary (broadsheet text) and secondary (scholarly analysis) sources. Needs judgment to identify which scholarly interpretations are relevant.
  - **Skills**: []
    - No skills needed — this is web research, not codebase or browser-automation work
  - **Skills Evaluated but Omitted**:
    - `playwright`: Not needed — webfetch/websearch tools suffice for Wikipedia + scholarly article retrieval
    - `git-master`: Not needed — no git operations in this task

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5, 6, 7)
  - **Blocks**: Task 8 (document creation depends on this research)
  - **Blocked By**: None (can start immediately)

  **References**:

  **Pattern References** (existing code to follow):
  - `audit/12-NHI-correlation.md:18-30` — How modern sources are cited (named scholars with parenthetical citations: "Vallée, Passport to Magonia (1969), Preface"). Follow this citation style for scholarly sources.
  - `audit/12-NHI-correlation.md:36-61` — Correlation methodology section. The research output should note which criteria (structural overlap, minimal counter-explanation test) apply to this event.

  **External References**:
  - Wikipedia: `https://en.wikipedia.org/wiki/1561_celestial_phenomenon_over_Nuremberg` — Primary event description, broadsheet translation, scholarly interpretations
  - Search targets: "Ulrich Magin Nuremberg 1561", "Wiebke Schwarte broadsheet", "Jacques Vallée Passport to Magonia Nuremberg", "Hans Glaser broadsheet Nuremberg"

  **WHY Each Reference Matters**:
  - 12-NHI citation style: Ensures research output is in a format Task 8 can directly use without reformatting
  - 12-NHI §2 methodology: Research should pre-classify which correlation criteria the event meets/fails, so Task 8's signal/noise section has the raw material
  - Wikipedia article: The most accessible comprehensive source for the event description and broadsheet text

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output contains required source material elements
    Tool: Bash (grep on research output file or session messages)
    Preconditions: Task 1 has completed its web research
    Steps:
      1. Verify research output contains the date "April 14, 1561" or "14 April 1561"
      2. Verify research output contains a description of at least 3 object types from the broadsheet (cylinders, crosses, globes, crescent, spear)
      3. Verify research output contains at least 1 scholarly interpretation citation (Magin, Schwarte, or Vallée)
      4. Verify research output contains the broadsheet's reported "combat" or "battle" description
      5. Verify research output notes the "doesn't neatly fit sun dog" scholarly observation
    Expected Result: All 5 elements present in research output
    Failure Indicators: Missing date, missing object types, no scholarly citations, no combat description
    Evidence: .omo/evidence/task-1-nuremberg-research-checks.txt

  Scenario: Citation format matches Archive convention
    Tool: Bash (grep)
    Preconditions: Research output exists
    Steps:
      1. Grep research output for citation patterns matching "(Author, Work, Year)" or "(Source Title, URL, accessed date)"
      2. Count citations — must be ≥3 (event description + scholarly interpretation + broadsheet text)
    Expected Result: ≥3 properly formatted citations
    Failure Indicators: Citations missing or in wrong format (e.g., bare URLs without source titles)
    Evidence: .omo/evidence/task-1-citation-format-check.txt
  ```

  **Commit**: NO (research output is internal — feeds into Task 8)

---

- [x] 2. Research 1566 Basel Celestial Phenomenon

  **What to do**:
  - Fetch the Wikipedia article: `https://en.wikipedia.org/wiki/1566_celestial_phenomenon_over_Basel`
  - Extract: full event description, dates (July 27-28 and August 7, 1566), witness accounts, the specific description of "large black spheres coming and going with great speed and precision before the sun" that "appeared to fight each other, turned fiery red, then crumbled and extinguished"
  - Search for scholarly analysis: "Ulrich Magin Basel 1566", "Basel 1566 broadsheet", "Basel celestial phenomenon Samuel Coccius" (the reported witness/illustrator)
  - Document the broadsheet provenance: who created it, when, where published
  - Extract the THREE distinct phases reported: (1) blood-red sun and moon (July 27-28), (2) black spheres fighting (August 7), (3) spheres turning red and crumbling/extinguishing
  - Compare the "crumbled and extinguished" detail to Nuremberg's "falls" and "crashes" — this is the highest-signal detail (discrete objects being destroyed)
  - Research why Basel is considered "the closest parallel" to Nuremberg — what structural similarities do scholars identify?

  **Must NOT do**:
  - Do NOT write the actual analysis document
  - Do NOT conflate Basel with Nuremberg — keep them as separate research outputs
  - Do NOT add PDFs to texts/

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Multi-source web research requiring extraction of specific witness-account details and scholarly cross-comparison with Nuremberg
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5, 6, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:18-30` — Citation style for modern sources
  - `audit/12-NHI-correlation.md:36-61` — Correlation methodology criteria for pre-classification

  **External References**:
  - Wikipedia: `https://en.wikipedia.org/wiki/1566_celestial_phenomenon_over_Basel`
  - Search targets: "Samuel Coccius Basel 1566", "Ulrich Magin Basel 1566 broadsheet", "Basel black spheres sun 1566"

  **WHY Each Reference Matters**:
  - The "crumbled and extinguished" detail is the highest-signal element in the entire dataset. Research must capture the exact source language and any scholarly attempts to explain it via atmospheric optics.
  - Basel is the closest parallel to Nuremberg — the research must document WHY scholars consider them parallel (structural similarity, not just thematic).

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output contains the highest-signal detail
    Tool: Bash (grep)
    Preconditions: Task 2 has completed
    Steps:
      1. Grep research output for "crumbled" or "crumbling" or "extinguish"
      2. Verify the exact source language is captured (blockquote or quotation)
      3. Verify the three phases are documented: blood-red sun/moon, black spheres fighting, spheres crumbling
    Expected Result: All three phases present, "crumbled/extinguished" detail in quotes
    Failure Indicators: Missing "crumbled" detail, phases conflated, no direct quotation
    Evidence: .omo/evidence/task-2-basel-research-checks.txt

  Scenario: Scholarly comparison with Nuremberg documented
    Tool: Bash (grep)
    Preconditions: Research output exists
    Steps:
      1. Grep for "Nuremberg" in the Basel research output — must contain structural comparison
      2. Verify at least 1 scholarly source is cited for the comparison
    Expected Result: Structural comparison with Nuremberg present and cited
    Failure Indicators: No Nuremberg comparison, or comparison without scholarly attribution
    Evidence: .omo/evidence/task-2-nuremberg-comparison-check.txt
  ```

  **Commit**: NO

---

- [x] 3. Research 1535 Stockholm Vädersolstavlan (CONTROL BASELINE)

  **What to do**:
  - Fetch the Wikipedia article on the Vädersolstavlan: `https://en.wikipedia.org/wiki/Vädersolstavlan` (or search "Vädersolstavlan Stockholm 1535 sun dog painting")
  - Extract: event description, date (April 20, 1535 or as documented), the painting's history (original by Urban målare, 1535; surviving copy by Jacob Elbfas, 1636), the atmospheric optics depicted (sun dogs / parhelia, halos, arcs)
  - CRITICAL: Document WHY this is the control baseline — the painting depicts atmospheric optics with "geometric accuracy" (per user's source). Extract the specific optical phenomena: parhelia (sun dogs), 22° halo, circumzenithal arc, parhelic circle
  - Research the scholarly consensus: this is a well-understood atmospheric optics event, NOT an anomaly. Document the meteorological explanation (ice crystal refraction in cirrus clouds)
  - Note the visual difference from Glaser's Nuremberg woodcut: Vädersolstavlan is geometrically accurate; Glaser's is stylized/sensationalized
  - This research establishes what "known noise" looks like — the baseline against which Nuremberg/Basel signal is measured

  **Must NOT do**:
  - Do NOT analyze Stockholm as an anomalous event — it IS the control baseline
  - Do NOT apply the Archive's literal reconstruction framework as if this were an anomaly
  - Do NOT add PDFs to texts/

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires understanding of atmospheric optics (parhelia, halos) and art-historical context to establish the baseline properly
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5, 6, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:54-60` — Confirmation bias guardrails: "A claimed correlation is rejected if... it can be more simply explained by known psychological phenomena, folklore evolution, or cultural diffusion." Stockholm IS the "more simple explanation" baseline.

  **External References**:
  - Wikipedia: `https://en.wikipedia.org/wiki/Vädersolstavlan`
  - Search targets: "Vädersolstavlan sun dog Stockholm 1535", "Urban målare 1535 painting", "Jacob Elbfas 1636 copy", "parhelia atmospheric optics", "sun dog 22 degree halo"

  **WHY Each Reference Matters**:
  - The atmospheric optics details (parhelia, halos, arcs) are the "known mechanism" that makes Stockholm the control. Task 8 will use this to show what a PROPERLY EXPLAINED event looks like vs. Nuremberg/Basel which "don't neatly fit."
  - The geometric accuracy vs. Glaser's stylization is the key contrast — it establishes that 16th-century artists COULD depict optics accurately, making Glaser's stylization a choice, not a limitation.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output establishes control baseline
    Tool: Bash (grep)
    Preconditions: Task 3 has completed
    Steps:
      1. Grep for "parhelia" or "sun dog" or "halo" — must identify the specific optical phenomena
      2. Grep for "ice crystal" or "cirrus" or "refraction" — must document the meteorological mechanism
      3. Grep for "geometric accuracy" or "accurately" or "precision" — must note the painting's accuracy vs Glaser's stylization
      4. Verify research output explicitly frames this as CONTROL BASELINE, not as anomalous
    Expected Result: All 4 elements present, framing as control baseline explicit
    Failure Indicators: No optical phenomena identified, no meteorological mechanism, no accuracy contrast, framed as anomaly
    Evidence: .omo/evidence/task-3-stockholm-baseline-checks.txt
  ```

  **Commit**: NO

---

- [x] 4. Research 1554 Waldeck Castle + Plech (Glaser Pattern — SOURCE CREDIBILITY CONTEXT)

  **What to do**:
  - Search for information on Hans Glaser's broadsheet output beyond Nuremberg: "Hans Glaser broadsheet Waldeck 1554", "Hans Glaser Nuremberg broadsheet printer", "Miracle Sign Waldeck Castle 1554", "Plech sky spectacular 1554"
  - Extract: event descriptions (brief — these are NOT full analysis targets), dates, locations, broadsheet provenance
  - CRITICAL: Document Glaser's PATTERN of producing sensational broadsheets. The user notes "Glaser had a pattern of producing these kinds of sensational broadsheets." Find scholarly sources (Magin, Schwarte, or others) that establish this pattern.
  - Determine source availability: if scholarly sources on Glaser's commercial pattern are thin (only Wikipedia), note this explicitly. If sources don't establish a commercial pattern, the Waldeck/Plech section must be reduced to a brief footnote in Task 8.
  - Research the broadsheet tradition more broadly: 16th-century German broadsheets as "sensational tabloids" vs. objective reporting (per user's source: "Historians like Ulrich Magin and Wiebke Schwarte argue these broadsheets functioned more like sensational tabloids")
  - This is SOURCE CREDIBILITY CONTEXT, not event analysis. The output should answer: "Can we trust Glaser as a source? What's his track record?"

  **Must NOT do**:
  - Do NOT write a full 4-part framework analysis for Waldeck or Plech — they are context, not incidents
  - Do NOT speculate about Glaser's psychological state or motivations beyond what sources document
  - Do NOT treat Waldeck/Plech as independent anomalous events
  - Do NOT add PDFs to texts/

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Lighter research task — these are context events, not full analysis targets. The goal is establishing a credibility pattern, not deep event analysis.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 5, 6, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:54-60` — Confirmation bias guardrails. The Glaser pattern is a potential disconfirmation vector — if Glaser was a commercial sensationalist, that weakens Nuremberg's evidentiary value. Research must present this honestly.

  **External References**:
  - Search targets: "Hans Glaser Nuremberg broadsheet", "Waldeck Castle 1554 miracle", "Plech 1554 sky", "16th century German broadsheet tradition", "Ulrich Magin broadsheet tabloid"

  **WHY Each Reference Matters**:
  - Glaser's pattern directly affects Nuremberg's signal strength. If Glaser routinely produced sensational broadsheets, Nuremberg's evidentiary value drops. Task 8's signal/noise section MUST address this.
  - The broadsheet-as-tabloid framing is the primary counter-explanation for the entire cluster. Task 8 needs this to present the "minimal counter-explanation test" honestly.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output establishes Glaser pattern or flags thin sourcing
    Tool: Bash (grep)
    Preconditions: Task 4 has completed
    Steps:
      1. Verify research output either (a) documents Glaser's broadsheet pattern with ≥1 scholarly source, OR (b) explicitly flags that sources are thin and recommends reducing to footnote
      2. Grep for "Waldeck" and "Plech" — both events documented (even if briefly)
      3. Verify research output frames these as SOURCE CREDIBILITY CONTEXT, not as anomalous events
    Expected Result: Glaser pattern documented OR thin-sourcing flagged; both events mentioned; framing as context not incident
    Failure Indicators: Neither pattern nor thin-sourcing noted; events treated as standalone incidents
    Evidence: .omo/evidence/task-4-glaser-pattern-checks.txt
  ```

  **Commit**: NO

---

- [x] 5. Research 1665 Stralsund Celestial Phenomenon

  **What to do**:
  - Search for the 1665 Stralsund event: "1665 Stralsund celestial phenomenon", "Stralsund sky warships 1665", "Stralsund broadsheet 1665", "Erasmus Francisci Stralsund" (Francisci was a compiler who documented such events)
  - Extract: event description, date (1665), location (Stralsund, Baltic coast, Germany), witness accounts (fishermen reported seeing warships battling in the sky), the "flat round shape like a plate hovering overhead" detail
  - Identify the TWO components: (1) apparent aerial engagement (warships battling), (2) a discrete hovering object ("flat round shape like a plate"). The hovering plate is the high-signal element — it's a discrete-object observation, not atmospheric optics
  - Research the broadsheet provenance: who recorded it, how was it published
  - Search for scholarly analysis: "Ulrich Magin Stralsund 1665", "1665 Stralsund broadsheet analysis"
  - Note that this is "one of the last major events in this European broadsheet tradition" (per user's source) — document the tradition's endpoint
  - Compare to Nuremberg/Basel: is the "warship" description a cultural-frame adaptation? (16th century saw "spheres and crosses"; 17th century saw "warships" — does this match Vallée's "transmogrification" thesis where the phenomenon adapts to cultural expectations?)

  **Must NOT do**:
  - Do NOT write the actual analysis document
  - Do NOT add PDFs to texts/
  - Do NOT analyze post-1665 events

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires web research + scholarly analysis + cross-comparison with Nuremberg/Basel for the "cultural frame adaptation" question
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4, 6, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:204-211` — Keel's "transmogrification" thesis: "seemingly material apparitions that might actually be composed of energies... controlled by a form of intelligent energy." The Stralsund "warships" may be a 17th-century cultural frame for the same phenomenon that 16th-century witnesses called "spheres and crosses."
  - `audit/12-NHI-correlation.md:36-61` — Correlation methodology for pre-classification

  **External References**:
  - Search targets: "1665 Stralsund celestial phenomenon", "Stralsund sky warships broadsheet", "Erasmus Francisci 1665", "Ulrich Magin Stralsund"

  **WHY Each Reference Matters**:
  - The "hovering plate" is a discrete-object observation that survives the sun-dog counter-explanation. Research must capture the exact source language.
  - The "warships" vs "spheres" cultural-frame shift is a key data point for Vallée's transmogrification thesis — if the phenomenon adapts its appearance to cultural expectations, that's a control-system signature, not atmospheric optics.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output captures both event components
    Tool: Bash (grep)
    Preconditions: Task 5 has completed
    Steps:
      1. Grep for "warship" or "ship" — must document the aerial engagement component
      2. Grep for "plate" or "flat" or "round" or "hover" — must document the discrete hovering object
      3. Verify research output notes this as "one of the last major events in the broadsheet tradition"
    Expected Result: Both components (warships + hovering plate) documented; tradition endpoint noted
    Failure Indicators: Missing either component, or no mention of the broadsheet tradition's endpoint
    Evidence: .omo/evidence/task-5-stralsund-research-checks.txt

  Scenario: Cultural-frame comparison documented
    Tool: Bash (grep)
    Preconditions: Research output exists
    Steps:
      1. Grep for "Nuremberg" or "Basel" — must contain comparison to earlier events
      2. Verify the "warships vs spheres" cultural-frame shift is noted
    Expected Result: Cross-comparison with Nuremberg/Basel present, cultural-frame shift noted
    Failure Indicators: No comparison to earlier events
    Evidence: .omo/evidence/task-5-cultural-frame-check.txt
  ```

  **Commit**: NO

---

- [x] 6. Research 1917 Fátima Miracle of the Sun

  **What to do**:
  - Fetch the Wikipedia article: `https://en.wikipedia.org/wiki/Miracle_of_the_Sun`
  - Extract: event description, date (October 13, 1917), location (Fátima, Portugal), witness count (30,000–100,000 — cite the RANGE, not a single number), the reported phenomena (sun "danced," changed colors, appeared to plunge toward earth)
  - Research the prior context: three shepherd children claimed visions of the Virgin Mary from May-September 1917, and predicted the October 13 "miracle." Document this in MAX 2 sentences — it's context, not the analysis target
  - Research the three secrets of Fátima: document in MAX 1 paragraph — context only, NOT analysis target
  - CRITICAL: Research Stanley Jaki's atmospheric optics explanation (ice crystals + temperature inversions). Extract his specific mechanism and scholarly reception
  - Research other scholarly explanations: mass hypnosis, retinal damage from staring at the sun, expectation bias / psychological priming
  - Research Vallée's interpretation: did he comment on Fátima? (He discusses Marian apparitions in "Passport to Magonia" — check if Fátima specifically is covered)
  - Note the POLITICAL context briefly: WWI, Portuguese Revolution of 1910, secularist government vs. Catholic population — this affects source reliability (both pro- and anti-clerical biases)
  - The research must support treating this as a GENUINE mass-sighting event (per user decision) while giving the counter-explanations full and fair treatment

  **Must NOT do**:
  - Do NOT write a theological analysis of the Marian apparitions
  - Do NOT analyze the three secrets as prophetic content
  - Do NOT limit research to the October 13 event only — the prior-vision context (2 sentences) and political context (brief) are needed for source-credibility assessment
  - Do NOT add PDFs to texts/
  - Do NOT treat the children's visions as the analysis target — the aerial phenomenon of Oct 13 is the target

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Most complex research task — requires balancing genuine mass-sighting evidence with multiple counter-explanations, plus political/religious context for source-credibility assessment
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4, 5, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:18-30` — Citation style
  - `audit/13-nde-correlation.md` (first 200 lines) — How 13-NDE handles the tension between genuine phenomena and skeptical counter-explanations. Fátima needs the same balanced treatment.
  - `audit/12-NHI-correlation.md:54-60` — "Minimal counter-explanation test": Jaki's atmospheric optics IS the minimal counter-explanation. Research must present it fairly, not dismissively.

  **External References**:
  - Wikipedia: `https://en.wikipedia.org/wiki/Miracle_of_the_Sun`
  - Search targets: "Stanley Jaki Fátima atmospheric optics", "Stanley Jaki Miracle of the Sun ice crystals", "Fátima mass hypnosis explanation", "Fátima retinal damage", "Jacques Vallée Passport to Magonia Fátima Marian apparition", "Fátima 1917 witness count estimates"

  **WHY Each Reference Matters**:
  - Jaki's explanation is the primary scientific counter-argument. Task 8's counter-explanation subsection depends on this research being thorough and fair.
  - The witness count range (30K–100K) is the strongest mass-sighting datum in the entire dataset. Research must cite the range, not pick a number (Metis edge case #3).
  - Vallée's possible commentary on Fátima would connect this event to the NHI control-system thesis — critical for the cross-reference to 12-NHI.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output contains required Fátima elements
    Tool: Bash (grep)
    Preconditions: Task 6 has completed
    Steps:
      1. Grep for "October 13, 1917" or "13 October 1917" — date present
      2. Grep for "30,000" or "100,000" or "30K" or "100K" — witness count RANGE present (not a single number)
      3. Grep for "Jaki" — Stanley Jaki's explanation documented
      4. Grep for "ice crystal" or "temperature inversion" — Jaki's specific mechanism present
      5. Grep for "expectation bias" or "psychological" or "hypnosis" — at least 1 alternative counter-explanation present
      6. Verify the three secrets are mentioned in ≤1 paragraph (not analyzed)
      7. Verify the children's visions are mentioned in ≤2 sentences (context only)
    Expected Result: All 7 elements present with correct scope (date, witness range, Jaki, mechanism, alternative explanation, secrets ≤1 para, visions ≤2 sentences)
    Failure Indicators: Missing Jaki, witness count as single number, secrets analyzed in depth, visions given more than 2 sentences
    Evidence: .omo/evidence/task-6-fatima-research-checks.txt

  Scenario: Balanced treatment of genuine event + counter-explanations
    Tool: Bash (grep)
    Preconditions: Research output exists
    Steps:
      1. Verify research output contains BOTH the witness-account evidence (supporting genuine event) AND the counter-explanations (Jaki + alternatives)
      2. Verify neither is dismissively treated — both get fair representation
    Expected Result: Both genuine-evidence and counter-explanation content present and balanced
    Failure Indicators: One-sided treatment (either dismissive of witnesses or dismissive of counter-explanations)
    Evidence: .omo/evidence/task-6-balance-check.txt
  ```

  **Commit**: NO

---

- [x] 7. Research Scholarly Context (Vallée, Magin, Schwarte, Broadsheet Tradition)

  **What to do**:
  - Research the scholarly framework for analyzing these events. This is the METHODOLOGY research that Task 8 will use for the signal/noise section.
  - Fetch/summarize: Jacques Vallée's "Passport to Magonia" (1969) — the cross-cultural visitation thesis and how it applies to pre-1947 aerial phenomena. Note: 12-NHI §4.3 already covers Vallée's Magonia thesis extensively — research should COMPLEMENT, not duplicate. Focus on what 12-NHI does NOT cover: Vallée's specific treatment of broadsheet events if any.
  - Research Ulrich Magin: "Ulrich Magin broadsheet celestial phenomenon", "Ulrich Magin Nuremberg Basel analysis" — extract his specific arguments about broadsheets as "sensational tabloids" vs. objective reporting
  - Research Wiebke Schwarte: "Wiebke Schwarte broadsheet tradition" — extract her arguments about the broadsheet tradition's cultural function
  - Research the "stock myth" / propaganda hypothesis: Vallée suggested broadsheets "may represent a 'stock myth' that was recycled and possibly commissioned by religious authorities as a form of propaganda" (per user's source). Find the exact source for this claim.
  - Research the broadsheet tradition as a cultural phenomenon: 16th-century mass-produced woodcut news pamphlets, Reformation-era religious anxiety, the reading public primed for omens. How does this context affect source reliability?
  - Research atmospheric optics as the primary scientific counter-explanation: sun dogs (parhelia), halos, light pillars, circumzenithal arcs. Which broadsheet events DO fit atmospheric optics, and which DON'T?
  - This research feeds Task 8's signal/noise methodology section AND the "minimal counter-explanation test" for each event

  **Must NOT do**:
  - Do NOT duplicate 12-NHI §4.3's coverage of Vallée — COMPLEMENT it with broadsheet-specific content
  - Do NOT write the methodology section itself — gather the raw scholarly material
  - Do NOT add PDFs to texts/
  - Do NOT analyze post-1947 UFO cases

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires synthesizing multiple scholarly perspectives and identifying the methodological framework for signal/noise classification. This is the intellectual foundation for the entire document.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4, 5, 6)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:36-61` — The Archive's EXISTING correlation methodology. Task 8's signal/noise section will ADAPT this for historical broadsheet events. Research must understand these criteria.
  - `audit/12-NHI-correlation.md:173-211` — Vallée's Magonia thesis (already covered). Research should identify what 12-NHI does NOT cover about Vallée's treatment of pre-1947 events.
  - `audit/12-NHI-correlation.md:663-686` — Disconfirmation conditions (§11). Research should identify which disconfirmation conditions apply to broadsheet events.

  **External References**:
  - Search targets: "Jacques Vallée Passport to Magonia broadsheet", "Ulrich Magin celestial phenomenon broadsheet tabloid", "Wiebke Schwarte broadsheet tradition", "16th century German broadsheet woodcut news", "Vallée stock myth religious propaganda broadsheet", "sun dog parhelia atmospheric optics explanation celestial phenomenon"

  **WHY Each Reference Matters**:
  - This research is the METHODOLOGICAL FOUNDATION for the entire document. Without rigorous scholarly context, the signal/noise classification becomes opinion, not analysis.
  - The "stock myth" / propaganda hypothesis is the strongest disconfirmation vector for the entire cluster. If these broadsheets were commissioned propaganda, the evidentiary value of ALL events drops. Task 8 must address this head-on.
  - The atmospheric-optics counter-explanation is the "minimal counter-explanation" per 12-NHI §2. Research must identify which events survive this test and which don't.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Research output covers all required scholarly perspectives
    Tool: Bash (grep)
    Preconditions: Task 7 has completed
    Steps:
      1. Grep for "Vallée" — present, but with note on what 12-NHI already covers vs. what this adds
      2. Grep for "Magin" — Ulrich Magin's broadsheet-as-tabloid argument documented
      3. Grep for "Schwarte" — Wiebke Schwarte's broadsheet tradition argument documented
      4. Grep for "stock myth" or "propaganda" — Vallée's stock-myth hypothesis documented
      5. Grep for "parhelia" or "sun dog" or "atmospheric optics" — the scientific counter-explanation documented
      6. Verify research identifies which events FIT atmospheric optics vs. which DON'T
    Expected Result: All 6 elements present
    Failure Indicators: Missing any scholar, missing stock-myth hypothesis, no atmospheric optics coverage
    Evidence: .omo/evidence/task-7-scholarly-context-checks.txt

  Scenario: Research complements rather than duplicates 12-NHI
    Tool: Bash (grep)
    Preconditions: Research output exists
    Steps:
      1. Verify research output contains a note on what 12-NHI §4.3 already covers about Vallée
      2. Verify research output focuses on broadsheet-specific content NOT in 12-NHI
    Expected Result: Explicit complement-not-duplicate framing
    Failure Indicators: Duplicates 12-NHI's Vallée coverage without adding new material
    Evidence: .omo/evidence/task-7-complement-check.txt
  ```

  **Commit**: NO

---

- [x] 8. Write audit/14-broadsheet-celestial-events.md (Main Document)

  **What to do**:
  - Assemble ALL research from Tasks 1-7 into the synthesis document `audit/14-broadsheet-celestial-events.md`
  - Follow the 13-NDE structural template: classification header, executive summary with numbered findings, thematic sections with per-event incident breakdowns, tables, cross-references, sources section at end
  - Target 800–1,500 lines. Density over padding. 13-NDE is 2,039 lines because it has medical scales and prevalence tables; broadsheet events have sparser data.

  **Document Structure** (follow this outline):

  ```
  # Broadsheet Celestial Events: Gap Evidence Analysis (1535-1917)

  **Classification:** SPECIES WITH AMNESIA -- Working Hypothesis
  **Scope:** Cross-cutting synthesis of historical celestial phenomenon events (1535-1917 CE) as gap evidence for the 573 BCE – 1975 CE "Silent Period"
  **Analyst:** The Chronos Archive, Lead Investigator

  ---

  ## Executive Summary
  {Numbered findings, 5-8 items, each with inline cross-reference to synthesis docs}
  {Format: "N. {finding} (see [file.md](file.md): context)"}
  {Key findings should address: signal/noise classification results, which events survive the minimal counter-explanation test, what the gap evidence suggests for Reading A vs Reading B (12-NHI §3), parallels to ancient celestial battle accounts}

  ---

  ## Section 1: Signal/Noise Methodology
  {Adapt 12-NHI §2 correlation methodology for historical broadsheet events}
  {Define: valid signal criteria, evidence quality tiers for broadsheet sources, confirmation bias guardrails, the "minimal counter-explanation test" (atmospheric optics), disconfirmation conditions}
  {Present the signal-strength classification table:}

  | Event | Date | Signal Strength | Classification Rationale |
  |-------|------|-----------------|-------------------------|
  | Stockholm Vädersolstavlan | 1535 | CONTROL | Known atmospheric optics (sun dogs), geometrically accurate painting |
  | Waldeck Castle | 1554 | CONTEXT ONLY | Glaser broadsheet; source-credibility data, not independent event |
  | Plech | 1554 | CONTEXT ONLY | Broadsheet tradition; same year as Waldeck |
  | Nuremberg | 1561 | HIGH | Objects in formation, engagement, crashes; doesn't fit sun dog |
  | Basel | 1566 | HIGH | Black spheres fighting, crumbling, extinguishing; highest signal |
  | Stralsund | 1665 | HIGH | Warships battling + discrete hovering plate |
  | Fátima | 1917 | COMPLEX | 30K-100K witnesses; religious frame; expectation bias counter |

  ---

  ## Section 2: The Broadsheet Tradition as Cultural Context
  {From Task 7 research: 16th-century mass-produced woodcut news pamphlets, Reformation-era anxiety, omen interpretation}
  {The "stock myth" / propaganda hypothesis (Vallée) — present fairly as the primary disconfirmation vector}
  {Glaser's broadsheet pattern (from Task 4) — Waldeck, Plech, Nuremberg all by same artist}
  {The broadsheet-as-tabloid argument (Magin, Schwarte)}
  {WHY this matters: source credibility assessment for the entire cluster}

  ---

  ## Section 3: CONTROL BASELINE — Stockholm Vädersolstavlan (1535)
  > **CONTROL BASELINE:** This event is documented as a known atmospheric optics phenomenon. It is NOT analyzed as anomalous. It establishes what "known noise" looks like for comparison with HIGH SIGNAL events.

  ### Source Material
  {Blockquote from research Task 3 — the event description, painting provenance}

  ### Mainstream Interpretation
  {Well-understood atmospheric optics: parhelia (sun dogs), 22° halo, circumzenithal arc, ice crystal refraction}

  ### Literal Reconstruction (Atmospheric Optics Analysis)
  {Document the specific optical phenomena depicted with geometric accuracy}
  {Contrast with Glaser's stylized Nuremberg woodcut — 16th-century artists COULD depict optics accurately}

  ### Plausible Mechanism (Known)
  {Ice crystal refraction in cirrus clouds — the established meteorological explanation}
  {This is the BASELINE: what a properly-explained event looks like}

  ---

  ## Section 4: HIGH SIGNAL — 1561 Nuremberg Celestial Phenomenon
  **Signal Strength: HIGH**

  ### Source Material
  {Blockquotes from Task 1 research — Glaser's broadsheet text, the woodcut description, object types}

  ### Mainstream Interpretation
  {The standard view: either atmospheric optics (sun dogs, halos) or sensational broadsheet}

  ### The Archive's Literal Reconstruction
  {Technological re-reading: objects in formation → structured deployment; "combat" → engagement; "falls/crashes" → objects destroyed or descending}
  {Apply the Amnesia Filter: what would a 1561 witness call a structured aerial deployment?}
  {Cross-reference: parallels to Revelation "war in heaven" (Rev 12:7-9), Mahābhārata vimāna combat}

  ### Plausible Mechanism
  {What technology could produce: structured objects, apparent combat, objects being destroyed?}
  {Address the "doesn't fit sun dog" scholarly observation — WHY doesn't it fit?}

  ### Counter-Explanation Assessment
  {Sun dogs: doesn't fit (scholarly consensus per Task 1)}
  {Sensational broadsheet: possible (Glaser pattern) — but doesn't explain Basel 1566 independent corroboration}
  {Stock myth / propaganda: possible — but the specific details (crumbling, extinguishing) are too precise for pure invention}

  ---

  ## Section 5: HIGH SIGNAL — 1566 Basel Celestial Phenomenon
  **Signal Strength: HIGH** (highest in dataset)

  ### Source Material
  {Blockquotes from Task 2 — the three phases, "black spheres fighting," "crumbled and extinguished"}

  ### Mainstream Interpretation
  {Atmospheric optics or broadsheet sensationalism}

  ### The Archive's Literal Reconstruction
  {Technological re-reading: three phases = three distinct phenomena or a single escalating event}
  {Phase 1 (blood-red sun/moon): atmospheric modification or optical effect}
  {Phase 2 (black spheres fighting): discrete objects in engagement — the highest-signal detail}
  {Phase 3 (crumbled and extinguished): objects being destroyed — NOT atmospheric optics behavior}
  {Cross-reference: Nuremberg "falls/crashes" — independent corroboration of objects being destroyed}

  ### Plausible Mechanism
  {What technology produces: discrete black spheres, apparent combat, destruction by crumbling?}
  {The "crumbling" detail is key — this is not how atmospheric optics terminate}

  ### Counter-Explanation Assessment
  {Sun dogs: does not explain "black spheres" or "crumbling/extinguishing"}
  {Broadsheet sensationalism: possible, but independently documented from Nuremberg}
  {Volcanic haze: could explain blood-red sun (Phase 1) but NOT spheres or crumbling}

  ---

  ## Section 6: HIGH SIGNAL — 1665 Stralsund Celestial Phenomenon
  **Signal Strength: HIGH**

  ### Source Material
  {Blockquotes from Task 5 — warships battling, hovering plate}

  ### Mainstream Interpretation
  {Broadsheet tradition; possibly atmospheric optics or mass suggestion}

  ### The Archive's Literal Reconstruction
  {Two components: (1) aerial engagement described as "warships" — cultural-frame adaptation per Vallée's transmogrification thesis (see 12-NHI §4.4, Keel)}
  {(2) "flat round shape like a plate hovering" — discrete object, NOT atmospheric optics}
  {The cultural-frame shift: 16th century saw "spheres and crosses," 17th century saw "warships" — does the phenomenon adapt its presentation to cultural expectations?}

  ### Plausible Mechanism
  {Transmogrification: the phenomenon presents in culturally calibrated forms (Keel/Vallée)}
  {The "hovering plate" is a discrete-object observation — consistent with modern UAP reports}

  ### Counter-Explanation Assessment
  {Atmospheric optics: does not explain "warships" or "hovering plate"}
  {Mass suggestion: possible for the "warships" but not for a discrete hovering object}

  ---

  ## Section 7: COMPLEX — 1917 Fátima Miracle of the Sun
  **Signal Strength: COMPLEX**

  ### Source Material
  {Blockquotes from Task 6 — October 13, 1917 event, witness accounts, reported phenomena}

  ### Mainstream Interpretation
  {Religious miracle (Catholic tradition) or mass hallucination/retinal damage (skeptical view)}

  ### The Archive's Literal Reconstruction
  {30K-100K witnesses is the strongest mass-sighting datum in the dataset}
  {The religious frame is the era's "amnesia filter" — per claude.md, witnesses use the vocabulary available to them}
  {The "sun dancing" and "plunging toward earth" — if taken literally, what technology could produce this?}
  {Cross-reference: the expectation bias (children predicted it) is a legitimate concern — address it}

  ### Plausible Mechanism
  {If genuine: atmospheric optics (Jaki's ice crystal + temperature inversion) + mass psychological amplification?}
  {Or: a projected/manifested phenomenon timed to the predicted hour?}
  {The Archive must hold both possibilities — the data doesn't discriminate}

  ### Counter-Explanation Assessment (DEDICATED SUBSECTION)
  {Stanley Jaki's atmospheric optics: ice crystals + temperature inversions — present fully and fairly}
  {Expectation bias: the children predicted the event; 30K+ people came EXPECTING a miracle}
  {Retinal damage: staring at the sun causes afterimages and perceived movement}
  {Mass hypnosis / collective suggestion: large crowds in heightened emotional states}
  {Archive Assessment: the counter-explanations are strong for Fátima. The expectation bias is a genuine disconfirmation vector that Nuremberg/Basel/Stralsund do NOT face (those were unanticipated). This is WHY Fátima is COMPLEX, not HIGH.}

  ---

  ## Section 8: Source Credibility Context — Hans Glaser's Broadsheet Pattern
  {From Task 4 research: Glaser produced multiple broadsheets (Nuremberg 1561, Waldeck 1554, possibly others)}
  {The commercial broadsheet pattern: Glaser was a professional broadsheet producer}
  {Impact on signal assessment: Glaser's pattern weakens Nuremberg's individual evidentiary value BUT Basel 1566 is independently documented (different artist, different city)}
  {If Task 4 found thin sourcing: reduce this to a brief footnote noting the pattern is suggested but not well-attested}

  ---

  ## Section 9: Cross-Source Correlation — Ancient Parallels
  {From 04-cross-references integration: parallels to ancient celestial battle accounts}
  {Revelation 12:7-9: "war in heaven" — Michael and angels fought against the dragon}
  {Mahābhārata: vimāna combat, astra exchanges in the sky}
  {Ezekiel 1: the Merkabah — structured aerial vehicle with discrete components}
  {Popol Vuh: Heart of Sky manifestations}
  {The structural parallel: ancient texts describe "gods fighting in the sky"; broadsheets describe "objects fighting in the sky"; modern NHI describes "craft performing maneuvers." Same operational signature, different cultural vocabulary.}

  ---

  ## Section 10: Gap Evidence and the Timeline Tension
  {Cross-reference 12-NHI-correlation.md §3 (Timeline Tension) and §3.5 (How NHI Evidence Might Resolve the Ambiguity)}
  {These 7 events are the FIRST witness-account evidence for the 573 BCE – 1975 CE "Silent Period" (see 03-event-timeline.md, Mermaid Gantt "Reduced Contact / Silent Period")}
  {Apply the 12-NHI §3.5 discrimination framework:}

  | Finding | Supports Reading A (continuous pipeline) | Supports Reading B (renewed contact) |
  |---------|------------------------------------------|--------------------------------------|
  | Events cluster in 16th-17th century broadsheet tradition | Weak: cultural phenomenon, not operational | Moderate: possible precursor to modern disclosure wave |
  | Events describe "combat" and discrete objects | Neutral: pipeline leakage doesn't explain combat | Strong: operational activity implies active presence |
  | No events between 1665 and 1917 (252-year gap) | Weak: continuous pipeline should produce continuous evidence | Neutral: withdrawal followed by limited re-engagement |
  | Fátima (1917) uses religious frame like ancient texts | Strong: same amnesia-filter pattern as always | Neutral: consistent with either reading |

  {Archive Assessment: the broadsheet evidence is AMBIGUOUS between Reading A and Reading B. It does not resolve the timeline tension. It does, however, establish that the "Silent Period" was NOT fully silent — witness accounts of anomalous aerial phenomena continued throughout. The "Silent Period" label should be revised to "Reduced Contact / Intermittent Witness Accounts" or similar.}
  {NOTE: This does NOT change 11-unified-hypothesis.md Finding 7 — these are witness observations, not operator-to-human contacts. The "autonomous test phase" finding holds.}

  ---

  ## Section 11: Numbered Findings and Predictions
  {Synthesize the document's findings into 5-8 numbered items}
  {Include falsifiable predictions: if X is found in future evidence, the assessment changes}

  ---

  ## Sources
  {Web sources: (Source Title, URL, accessed YYYY-MM-DD)}
  {Books/scholars: (Author, Work, Year, Page)}
  {List ALL sources used}
  ```

  **Must NOT do**:
  - Do NOT exceed 1,500 lines
  - Do NOT treat Stockholm as anomalous — it is CONTROL BASELINE
  - Do NOT give Waldeck/Plech full 4-part framework entries — they are Section 8 context only
  - Do NOT analyze Fátima beyond the October 13 aerial phenomenon
  - Do NOT use theological language outside quoted source material
  - Do NOT rewrite 11-unified-hypothesis.md's "SILENCE" claim — these are witness accounts, not operator contacts
  - Do NOT duplicate 12-NHI's Vallée coverage — complement it
  - Do NOT pad with speculation to match 13-NDE's length — density over padding
  - Do NOT create Mermaid diagrams beyond 2 maximum
  - Do NOT leave any factual claim uncited

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: This is the core analytical task — synthesizing 7 research outputs into a coherent synthesis document matching the Archive's most sophisticated format (13-NDE template). Requires deep analytical writing, cross-referencing, and methodological rigor. One goal + one deliverable.
  - **Skills**: []
    - No skills needed — this is markdown research writing, not codebase or browser work
  - **Skills Evaluated but Omitted**:
    - `playwright`: Not needed — no browser interaction
    - `git-master`: Not needed for the writing task (commits handled separately)
    - `frontend-ui-ux`: Not needed — markdown document, not UI

  **Parallelization**:
  - **Can Run In Parallel**: NO — this is the critical-path sequential task
  - **Parallel Group**: Wave 2 (alone)
  - **Blocks**: Tasks 9, 10, 11, 12, 13 (all integration tasks depend on the document existing)
  - **Blocked By**: Tasks 1, 2, 3, 4, 5, 6, 7 (all research must complete first)

  **References**:

  **Pattern References** (existing code to follow — CRITICAL):
  - `audit/13-nde-correlation.md:1-200` — PRIMARY TEMPLATE. Document header, classification, executive summary with numbered findings, section structure, table format, cross-reference style. Match this exactly.
  - `audit/12-NHI-correlation.md:1-70` — Secondary template. How an addendum introduces itself, scopes its relationship to the unified hypothesis, and establishes methodology.
  - `audit/12-NHI-correlation.md:36-61` — Correlation methodology (§2). Adapt for broadsheet events: valid signal criteria, evidence quality tiers, confirmation bias guardrails, disconfirmation.
  - `audit/12-NHI-correlation.md:140-155` — Timeline Tension §3.5 discrimination framework. Section 10 of the new doc applies this framework directly.
  - `audit/analyses/ezekiel-merkabah.md:20-104` — How a per-incident 4-part framework analysis is structured (Source Material blockquotes, Mainstream Interpretation, Literal Reconstruction with tables, Plausible Mechanism). Follow this format for each HIGH/COMPLEX event.
  - `audit/analyses/AGENTS.md` — Per-text analysis template (the `### Source Material` / `### Mainstream Interpretation` / `### Literal Reconstruction` / `### Plausible Mechanism` structure). Use this for each event's incident breakdown.
  - `claude.md:19-26` — The 4-part analysis framework definition. Every HIGH/COMPLEX event must have all 4 sections.

  **API/Type References**:
  - `audit/00-INDEX.md:9-27` — Source texts table format. The new doc will NOT add to this table (no new PDFs) but should reference existing texts where parallels exist.
  - `audit/00-INDEX.md:52-67` — Audit documents table format. Task 9 will add the new doc here.

  **Test References**:
  - `scripts/validate-links.py` — The link validator. After writing, run this to verify all cross-references resolve.

  **External References**:
  - Research outputs from Tasks 1-7 (in session messages / research files)
  - `https://en.wikipedia.org/wiki/1561_celestial_phenomenon_over_Nuremberg`
  - `https://en.wikipedia.org/wiki/1566_celestial_phenomenon_over_Basel`
  - `https://en.wikipedia.org/wiki/Miracle_of_the_Sun`

  **WHY Each Reference Matters**:
  - 13-NDE template: This is the established format for a modern-evidence addendum. Matching it ensures structural consistency across the Archive.
  - 12-NHI §2 methodology: The signal/noise section (Section 1) adapts this directly. Without it, the classification becomes opinion.
  - 12-NHI §3.5 discrimination framework: Section 10 applies this to determine whether broadsheet evidence supports Reading A or B. This is the document's payoff — it connects the historical events to the Archive's central open question.
  - Ezekiel analysis format: Each HIGH/COMPLEX event gets the same 4-part treatment as ancient text incidents. This ensures the broadsheet events are analyzed with the same rigor as Ezekiel's Merkabah.
  - claude.md framework: The 4-part framework is the Archive's core methodology. Every analyzed event must comply.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Document structure matches 13-NDE template
    Tool: Bash (grep + wc)
    Preconditions: audit/14-broadsheet-celestial-events.md exists
    Steps:
      1. grep "**Classification:** SPECIES WITH AMNESIA" audit/14-broadsheet-celestial-events.md → must return ≥1
      2. grep "**Analyst:** The Chronos Archive" audit/14-broadsheet-celestial-events.md → must return ≥1
      3. grep "## Executive Summary" audit/14-broadsheet-celestial-events.md → must return 1
      4. grep "## Section" audit/14-broadsheet-celestial-events.md → must return ≥10 (Sections 1-11)
      5. grep "## Sources" audit/14-broadsheet-celestial-events.md → must return 1
      6. wc -l audit/14-broadsheet-celestial-events.md → must be 800-1500
    Expected Result: All 6 checks pass
    Failure Indicators: Missing classification header, missing executive summary, wrong section count, out-of-line-count range
    Evidence: .omo/evidence/task-8-structure-checks.txt

  Scenario: 4-part framework present for all HIGH/COMPLEX events
    Tool: Bash (grep)
    Preconditions: Document exists
    Steps:
      1. grep -c "### Source Material" audit/14-broadsheet-celestial-events.md → must return 4 (Nuremberg, Basel, Stralsund, Fátima)
      2. grep -c "### Mainstream Interpretation" audit/14-broadsheet-celestial-events.md → must return 4
      3. grep -c "### Literal Reconstruction\|### The Archive's Literal Reconstruction" audit/14-broadsheet-celestial-events.md → must return 4
      4. grep -c "### Plausible Mechanism" audit/14-broadsheet-celestial-events.md → must return 4
    Expected Result: All counts = 4
    Failure Indicators: Any count ≠ 4 (missing framework section for an event)
    Evidence: .omo/evidence/task-8-framework-checks.txt

  Scenario: Signal-strength tags present on all events
    Tool: Bash (grep)
    Preconditions: Document exists
    Steps:
      1. grep -c "Signal Strength" audit/14-broadsheet-celestial-events.md → must return ≥5 (Stockholm, Nuremberg, Basel, Stralsund, Fátima; Waldeck/Plech may be in Section 8 context)
      2. grep "CONTROL BASELINE" audit/14-broadsheet-celestial-events.md → must return ≥1 (Stockholm)
      3. Verify Stockholm section does NOT contain "### Plausible Mechanism" for anomalous technology (it should have atmospheric optics as the "mechanism" — the KNOWN mechanism)
    Expected Result: ≥5 signal-strength tags, CONTROL BASELINE present, Stockholm not treated as anomalous
    Failure Indicators: Missing tags, Stockholm treated as anomalous
    Evidence: .omo/evidence/task-8-signal-tags-checks.txt

  Scenario: Waldeck/Plech NOT standalone incidents
    Tool: Bash (grep)
    Preconditions: Document exists
    Steps:
      1. Verify Waldeck and Plech do NOT have their own "### Source Material" / "### Mainstream Interpretation" / "### Literal Reconstruction" / "### Plausible Mechanism" sections
      2. Verify they appear in Section 8 (Source Credibility Context) or a footnote
      3. grep "Waldeck" audit/14-broadsheet-celestial-events.md → must return matches but NOT in a 4-part framework section
    Expected Result: Waldeck/Plech in context section only, no standalone 4-part framework
    Failure Indicators: Waldeck or Plech with their own ### Source Material section
    Evidence: .omo/evidence/task-8-waldeck-plech-checks.txt

  Scenario: Fátima scope locked to October 13 aerial phenomenon
    Tool: Bash (grep + wc)
    Preconditions: Document exists
    Steps:
      1. grep "three secrets\|Third Secret\|Marian theology\|Virgin Mary" audit/14-broadsheet-celestial-events.md → review hits; these should appear only in ≤1 paragraph of context, NOT as analysis sections
      2. Verify no ## or ### section header is dedicated to the three secrets or Marian theology
    Expected Result: Marian content limited to brief context, no dedicated analysis sections
    Failure Indicators: Dedicated section on three secrets or Marian theology
    Evidence: .omo/evidence/task-8-fatima-scope-checks.txt

  Scenario: No unauthorized theological language
    Tool: Bash (grep)
    Preconditions: Document exists
    Steps:
      1. grep -n "miracle\|divine\|supernatural\|holy\|sacred\|blessed" audit/14-broadsheet-celestial-events.md → review each hit
      2. For each hit, verify it is inside a blockquote (> ...) or in quotation marks — i.e., quoting source material, not the Archive's voice
      3. Exception: "Miracle of the Sun" is the event's proper name — acceptable in the event title
    Expected Result: All theological terms are in quotes/blockquotes or are proper names
    Failure Indicators: Theological language in the Archive's analytical voice
    Evidence: .omo/evidence/task-8-tone-checks.txt

  Scenario: Cross-references to existing Archive documents
    Tool: Bash (grep)
    Preconditions: Document exists
    Steps:
      1. grep "12-NHI-correlation\|12-nhi-correlation\|12-NHI" audit/14-broadsheet-celestial-events.md → must return ≥2 (methodology reference + timeline tension reference)
      2. grep "03-event-timeline\|03-timeline" audit/14-broadsheet-celestial-events.md → must return ≥1
      3. grep "04-cross-references\|04-cross" audit/14-broadsheet-celestial-events.md → must return ≥1
      4. grep "11-unified-hypothesis\|11-unified" audit/14-broadsheet-celestial-events.md → must return ≥1
      5. grep "revelation.md\|ezekiel-merkabah\|mahabharata" audit/14-broadsheet-celestial-events.md → must return ≥1 (ancient parallel cross-reference)
    Expected Result: All 5 cross-reference checks pass
    Failure Indicators: Missing any cross-reference category
    Evidence: .omo/evidence/task-8-cross-refs-checks.txt

  Scenario: Link integrity
    Tool: Bash (python3)
    Preconditions: Document exists
    Steps:
      1. Run: python3 scripts/validate-links.py
      2. Verify exit code is 0 and error count is 0
    Expected Result: Exit code 0, 0 link errors
    Failure Indicators: Any link errors (broken cross-references)
    Evidence: .omo/evidence/task-8-link-integrity.txt
  ```

  **Commit**: YES
  - Message: `docs(audit): add 14-broadsheet-celestial-events.md — gap evidence analysis (1535-1917)`
  - Files: `audit/14-broadsheet-celestial-events.md`
  - Pre-commit: `python3 scripts/validate-links.py` must pass

---

- [x] 9. Update audit/00-INDEX.md (Register New Document)

  **What to do**:
  - Read `audit/00-INDEX.md` to understand current structure
  - Add `audit/14-broadsheet-celestial-events.md` to the "Cross-Cutting Synthesis" table (lines 52-67 area) with description: "Broadsheet Celestial Events — Historical celestial phenomenon events (1535-1917 CE) as gap evidence for the Silent Period; signal/noise methodology; parallels to ancient celestial battle accounts"
  - Do NOT add to the "Source Texts" table (no new PDFs) or "Per-Text Deep Dives" table (no per-event files)
  - Ensure the markdown link format matches existing entries: `[14-broadsheet-celestial-events.md](14-broadsheet-celestial-events.md)`

  **Must NOT do**:
  - Do NOT modify any other entries in 00-INDEX
  - Do NOT add to the Source Texts table
  - Do NOT change the document's overall structure

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-file, small edit — adding one row to an existing table. Matches "quick" category (trivial modification).
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 10, 11, 12, 13)
  - **Blocks**: F1-F4 (final verification)
  - **Blocked By**: Task 8 (document must exist to be linked)

  **References**:

  **Pattern References**:
  - `audit/00-INDEX.md:52-67` — The Cross-Cutting Synthesis table. Match this format exactly: `| [NN-name.md](NN-name.md) | Description |`

  **WHY Each Reference Matters**:
  - The 00-INDEX is the Archive's master map. Without registration, the new doc is an orphan. The format must match existing entries for consistency.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: New document registered in 00-INDEX
    Tool: Bash (grep)
    Preconditions: Task 9 has completed
    Steps:
      1. grep "14-broadsheet-celestial-events" audit/00-INDEX.md → must return ≥1
      2. Verify the entry is in the Cross-Cutting Synthesis table, NOT the Source Texts table
    Expected Result: Entry present in correct table
    Failure Indicators: No entry, or entry in wrong table
    Evidence: .omo/evidence/task-9-index-registration.txt

  Scenario: Link integrity maintained
    Tool: Bash (python3)
    Preconditions: Edit complete
    Steps:
      1. Run: python3 scripts/validate-links.py
      2. Verify exit code 0, 0 errors
    Expected Result: Link validator passes
    Failure Indicators: Broken link to new document
    Evidence: .omo/evidence/task-9-link-check.txt
  ```

  **Commit**: YES (groups with Wave 3)
  - Message: `docs(audit): register 14-broadsheet-celestial-events in master index`
  - Files: `audit/00-INDEX.md`

---

- [x] 10. Update audit/03-event-timeline.md (Gap-Period Entries)

  **What to do**:
  - Read `audit/03-event-timeline.md` to understand the era structure (ERA 6: Historical Period, ERA X: Projected Terminal, ERA 7: Contemporary)
  - Add a NEW ERA section between ERA 6 and ERA 7 for the broadsheet events. Suggested title: "ERA 6.5: BROADSHEET ERA — Intermittent Witness Accounts (1535-1917 CE)" or insert entries into the existing chronological summary
  - Add entries for: 1535 Stockholm, 1554 Waldeck/Plech, 1561 Nuremberg, 1566 Basel, 1665 Stralsund, 1917 Fátima
  - Each entry: date, location, brief description (1-2 sentences), signal-strength tag, cross-reference to 14-broadsheet-celestial-events.md
  - Update the Mermaid Gantt chart: add event markers WITHIN the existing "Reduced Contact / Silent Period" block (Option B from Metis — don't break the block, add milestones within it). Use the `milestone` or `active` Mermaid syntax. Preserve the existing `dateFormat YYYY` constraint.
  - Update the "Reduced Contact / Silent Period" label if appropriate — Metis and the new document suggest "Reduced Contact / Intermittent Witness Accounts" is more accurate. However, do NOT remove the existing label entirely; add a note.

  **Must NOT do**:
  - Do NOT break the Mermaid Gantt chart's existing structure
  - Do NOT remove the "Reduced Contact / Silent Period" concept — these are witness accounts, not operator contacts; the period is still "reduced contact" relative to Ezekiel-era direct encounters
  - Do NOT add entries for events beyond the 7 specified
  - Do NOT change ERA 6 or ERA 7 content

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-file edit — adding entries to an existing timeline + Mermaid chart update. Bounded scope.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 11, 12, 13)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 8

  **References**:

  **Pattern References**:
  - `audit/03-event-timeline.md:338-350` — ERA 6: Historical Period format. Match this entry style (date, description, cross-reference).
  - `audit/03-event-timeline.md:480-506` — Chronological summary ASCII diagram. Add broadsheet entries in chronological order within the gap.
  - `audit/03-event-timeline.md:513-560` — Mermaid Gantt chart. The "Reduced Contact / Silent Period" block (line ~550: `Reduced Contact / Silent Period :done, e3, -573, 1975`). Add milestones within this block.

  **WHY Each Reference Matters**:
  - The timeline is the Archive's chronological backbone. Without these entries, the gap period remains "silent" in the visualization despite the new evidence.
  - The Mermaid chart is published to the live site (README links to actual-designer.github.io). Breaking it would break the published visualization.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Gap-period entries added
    Tool: Bash (grep)
    Preconditions: Task 10 has completed
    Steps:
      1. grep -E "1535|1554|1561|1566|1665|1917" audit/03-event-timeline.md → must return ≥6 matches (one per event, Waldeck/Plech can share a line)
      2. grep "14-broadsheet-celestial-events" audit/03-event-timeline.md → must return ≥1 (cross-reference to new doc)
    Expected Result: ≥6 date matches, ≥1 cross-reference
    Failure Indicators: Missing dates, no cross-reference to 14-broadsheet
    Evidence: .omo/evidence/task-10-timeline-entries.txt

  Scenario: Mermaid chart not broken
    Tool: Bash (python3 + grep)
    Preconditions: Edit complete
    Steps:
      1. grep "Reduced Contact" audit/03-event-timeline.md → must still return ≥1 (existing block preserved)
      2. Run: python3 scripts/validate-links.py → exit 0, 0 errors
      3. Verify the Mermaid chart section still has valid syntax (no unclosed quotes, no broken indentation)
    Expected Result: Existing block preserved, links valid, Mermaid syntax intact
    Failure Indicators: "Reduced Contact" removed, link errors, broken Mermaid
    Evidence: .omo/evidence/task-10-mermaid-check.txt
  ```

  **Commit**: YES (groups with Wave 3)
  - Message: `docs(audit): add broadsheet celestial events to event timeline (1535-1917 gap period)`
  - Files: `audit/03-event-timeline.md`

---

- [x] 11. Update audit/12-NHI-correlation.md (Cross-Reference in §3.5)

  **What to do**:
  - Read `audit/12-NHI-correlation.md` Section 3.5 ("How NHI Evidence Might Resolve the Ambiguity", approximately lines 138-155)
  - Add a cross-reference note in §3.5 (or immediately after it) stating that `14-broadsheet-celestial-events.md` provides the first witness-account evidence for the gap period, and applies the §3.5 discrimination framework to that evidence
  - The note should be brief (2-4 sentences) and point readers to the new document for the analysis
  - Suggested placement: at the end of §3.5, before the "---" separator, add a paragraph like: "The Archive's companion analysis ([14-broadsheet-celestial-events.md](14-broadsheet-celestial-events.md)) applies this discrimination framework to the first witness-account evidence from within the gap period itself — seven historical celestial phenomenon events (1535-1917 CE) documented in the European broadsheet tradition and modern mass-sighting records. The broadsheet evidence is assessed as ambiguous between Reading A and Reading B but establishes that the 'Silent Period' was not fully silent."

  **Must NOT do**:
  - Do NOT rewrite the "Two Readings" framework (§3.2, §3.3)
  - Do NOT change the §3.5 discrimination table
  - Do NOT add more than 4 sentences — this is a cross-reference, not a new section
  - Do NOT modify any other section of 12-NHI

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-file, small insertion — 2-4 sentences at the end of an existing section.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 10, 12, 13)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 8

  **References**:

  **Pattern References**:
  - `audit/12-NHI-correlation.md:138-155` — Section 3.5 discrimination framework. The cross-reference goes here because this is where gap evidence is discussed.

  **WHY Each Reference Matters**:
  - §3.5 is the ONLY place in 12-NHI that discusses gap evidence. The cross-reference must go here to connect the new document to the Timeline Tension discussion — the document's primary strategic value.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Cross-reference added to 12-NHI §3.5
    Tool: Bash (grep)
    Preconditions: Task 11 has completed
    Steps:
      1. grep "14-broadsheet-celestial-events\|14-broadsheet" audit/12-NHI-correlation.md → must return ≥1
      2. Verify the reference appears after the §3.5 discrimination table and before the next "---" separator
      3. grep -c "14-broadsheet" audit/12-NHI-correlation.md → must return ≤3 (cross-reference, not a new section)
    Expected Result: Cross-reference present in correct location, brief (≤3 mentions)
    Failure Indicators: No reference, reference in wrong section, excessive additions
    Evidence: .omo/evidence/task-11-nhi-crossref.txt

  Scenario: Existing 12-NHI structure preserved
    Tool: Bash (grep)
    Preconditions: Edit complete
    Steps:
      1. grep "Reading A" audit/12-NHI-correlation.md → must still return ≥1 (§3.2 preserved)
      2. grep "Reading B" audit/12-NHI-correlation.md → must still return ≥1 (§3.3 preserved)
      3. grep "How NHI Evidence Might Resolve" audit/12-NHI-correlation.md → must still return ≥1 (§3.5 preserved)
    Expected Result: All existing sections intact
    Failure Indicators: Any existing section modified or removed
    Evidence: .omo/evidence/task-11-structure-preserved.txt
  ```

  **Commit**: YES (groups with Wave 3)
  - Message: `docs(audit): cross-reference 14-broadsheet in 12-NHI timeline tension section`
  - Files: `audit/12-NHI-correlation.md`

---

- [x] 12. Update audit/04-cross-references.md (Ancient Parallels)

  **What to do**:
  - Read `audit/04-cross-references.md` to understand its structure (parallel accounts across traditions)
  - Add a new section or entries documenting parallels between the broadsheet celestial events and ancient celestial battle accounts:
    - **Revelation 12:7-9**: "war in heaven" — Michael and angels fought against the dragon. Parallel: Nuremberg/Basel "objects fighting in the sky"
    - **Mahābhārata**: vimāna combat, astra exchanges. Parallel: structured aerial engagement
    - **Ezekiel 1**: Merkabah — structured aerial vehicle with discrete components. Parallel: Nuremberg "cylinders, crosses, globes" as discrete structured objects
    - **Popol Vuh**: Heart of Sky manifestations. Parallel: atmospheric/celestial displays as operator activity
  - Each parallel entry should cite the SPECIFIC verse/incident (not vague references) and cross-reference both the ancient analysis file and 14-broadsheet-celestial-events.md
  - Frame the parallel as: "ancient texts describe 'gods fighting in the sky'; broadsheets describe 'objects fighting in the sky'; modern NHI describes 'craft performing maneuvers.' Same operational signature, different cultural vocabulary."

  **Must NOT do**:
  - Do NOT add parallels to events beyond the 7 specified
  - Do NOT cite vague references — use specific verses (e.g., "Revelation 12:7-9" not "Revelation war stuff")
  - Do NOT rewrite existing cross-reference entries
  - Do NOT duplicate 14-broadsheet's Section 9 content — this is a cross-reference entry, not a full analysis

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-file edit — adding cross-reference entries to an existing document.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 10, 11, 13)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 8

  **References**:

  **Pattern References**:
  - `audit/04-cross-references.md` — Existing structure for parallel accounts. Match this format.
  - `audit/analyses/revelation.md` — Revelation analysis for the "war in heaven" reference
  - `audit/analyses/mahabharata.md` — Mahābhārata analysis for vimāna combat reference
  - `audit/analyses/ezekiel-merkabah.md` — Ezekiel analysis for Merkabah reference

  **WHY Each Reference Matters**:
  - The cross-references document is where the Archive demonstrates convergence across geographically/temporally isolated traditions. Adding broadsheet-to-ancient parallels strengthens the convergence argument by extending it into the historical period.
  - Specific verse citations are required (Metis guardrail) — vague references weaken the cross-reference's evidentiary value.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Ancient parallels added with specific citations
    Tool: Bash (grep)
    Preconditions: Task 12 has completed
    Steps:
      1. grep "14-broadsheet-celestial-events\|14-broadsheet" audit/04-cross-references.md → must return ≥1
      2. grep -E "Revelation 12|Rev 12|12:7" audit/04-cross-references.md → must return ≥1 (specific verse)
      3. grep "broadsheet\|Nuremberg\|Basel\|Stralsund" audit/04-cross-references.md → must return ≥1 (broadsheet event referenced)
    Expected Result: Cross-reference present, specific verse cited, broadsheet event mentioned
    Failure Indicators: No cross-reference, vague citation, no broadsheet mention
    Evidence: .omo/evidence/task-12-cross-refs.txt

  Scenario: Link integrity
    Tool: Bash (python3)
    Preconditions: Edit complete
    Steps:
      1. Run: python3 scripts/validate-links.py → exit 0, 0 errors
    Expected Result: All links valid
    Failure Indicators: Broken links to 14-broadsheet or analysis files
    Evidence: .omo/evidence/task-12-link-check.txt
  ```

  **Commit**: YES (groups with Wave 3)
  - Message: `docs(audit): add broadsheet-to-ancient celestial battle parallels in cross-references`
  - Files: `audit/04-cross-references.md`

---

- [x] 13. Update README.md + audit/10-correlation-map.md + audit/11-unified-hypothesis.md (Navigation + Capstone Cross-Reference)

  **What to do**:
  This task updates THREE files for navigation and capstone consistency:

  **13a. README.md**:
  - Add `audit/14-broadsheet-celestial-events.md` to the "Cross-Cutting Syntheses" list (approximately lines 137-149)
  - Entry: `- [\`14-broadsheet-celestial-events.md\`](audit/14-broadsheet-celestial-events.md) — Historical celestial phenomenon events (1535-1917 CE) as gap evidence for the Silent Period; signal/noise methodology; parallels to ancient celestial battle accounts.`
  - Optionally add to "First Doorways" table if a compelling hook can be written (e.g., "The Gap Evidence → 14-broadsheet → 'The Silent Period wasn't silent. Witnesses kept reporting objects in the sky.'")
  - Add to "How to Explore" section if appropriate (e.g., "I want the historical gap evidence → 14-broadsheet → 12-NHI Timeline Tension")

  **13b. audit/10-correlation-map.md**:
  - Read `audit/10-correlation-map.md` to understand its structure (per-text perspective inventory, thematic clusters, linking blueprint)
  - Add 14-broadsheet to the linking blueprint / correlation map
  - Note its relationship to 12-NHI (gap evidence), 13-NDE (parallel modern-evidence track), 03-timeline (gap entries), 04-cross-references (ancient parallels)

  **13c. audit/11-unified-hypothesis.md** (CROSS-REFERENCE ONLY):
  - Read `audit/11-unified-hypothesis.md` to find where it discusses the "SILENCE (Post-573 BCE → Present)" or "autonomous test phase"
  - Add a brief cross-reference note (1-2 sentences) at that location: "See [14-broadsheet-celestial-events.md](14-broadsheet-celestial-events.md) for witness-account evidence from within the Silent Period (1535-1917 CE). These are ambient observations, not operator-to-human contacts; the 'autonomous test phase' finding holds."
  - Do NOT rewrite Finding 7 or the "SILENCE" claim
  - Do NOT change the capstone's narrative arc

  **Must NOT do**:
  - Do NOT rewrite 11-unified-hypothesis.md's Finding 7 or any "SILENCE" / "autonomous test phase" language
  - Do NOT change README's overall structure
  - Do NOT add 14-broadsheet to README's "Source Texts" table (it's not a source text)
  - Do NOT modify 10-correlation-map's existing entries

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Three small file edits — navigation list additions + one cross-reference sentence. All bounded, mechanical edits.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 9, 10, 11, 12)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 8

  **References**:

  **Pattern References**:
  - `README.md:137-149` — Cross-Cutting Syntheses list format
  - `README.md:151-164` — First Doorways table format
  - `audit/10-correlation-map.md` — Existing correlation map structure
  - `audit/11-unified-hypothesis.md` — Find the "SILENCE" / "autonomous test phase" / Finding 7 location (search for "573" or "silent" or "autonomous")

  **WHY Each Reference Matters**:
  - README is the project's front door. Without the new doc listed, visitors won't find it. The published site (actual-designer.github.io) renders from README.
  - 10-correlation-map is the internal linking blueprint. Without it, the doc is disconnected from the Archive's internal navigation graph.
  - 11-unified-hypothesis is the capstone. The cross-reference ensures the capstone acknowledges the gap evidence without being rewritten — maintaining consistency between "these are witness accounts" (14-broadsheet) and "autonomous test phase" (11-unified).

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: README updated with new document
    Tool: Bash (grep)
    Preconditions: Task 13 has completed
    Steps:
      1. grep "14-broadsheet-celestial-events" README.md → must return ≥1
      2. Verify it appears in the Cross-Cutting Syntheses list
    Expected Result: New doc listed in README
    Failure Indicators: Not listed, or listed in wrong section
    Evidence: .omo/evidence/task-13-readme-check.txt

  Scenario: 10-correlation-map updated
    Tool: Bash (grep)
    Preconditions: Edit complete
    Steps:
      1. grep "14-broadsheet-celestial-events\|14-broadsheet" audit/10-correlation-map.md → must return ≥1
    Expected Result: New doc in correlation map
    Failure Indicators: Not referenced
    Evidence: .omo/evidence/task-13-correlation-map-check.txt

  Scenario: 11-unified-hypothesis cross-reference added (NOT rewritten)
    Tool: Bash (grep)
    Preconditions: Edit complete
    Steps:
      1. grep "14-broadsheet-celestial-events\|14-broadsheet" audit/11-unified-hypothesis.md → must return ≥1
      2. grep -c "14-broadsheet" audit/11-unified-hypothesis.md → must return ≤2 (brief cross-reference, not a section)
      3. grep "autonomous test phase\|SILENCE" audit/11-unified-hypothesis.md → must still return ≥1 (existing language preserved)
    Expected Result: Cross-reference present, brief (≤2 mentions), existing language preserved
    Failure Indicators: No cross-reference, excessive additions, or existing language removed
    Evidence: .omo/evidence/task-13-capstone-crossref.txt

  Scenario: Link integrity across all three files
    Tool: Bash (python3)
    Preconditions: All edits complete
    Steps:
      1. Run: python3 scripts/validate-links.py → exit 0, 0 errors
    Expected Result: All links valid
    Failure Indicators: Broken links in any of the three files
    Evidence: .omo/evidence/task-13-link-check.txt
  ```

  **Commit**: YES (groups with Wave 3)
  - Message: `docs(audit): integrate broadsheet celestial events across README, correlation map, and unified hypothesis`
  - Files: `README.md`, `audit/10-correlation-map.md`, `audit/11-unified-hypothesis.md`

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
>
> **Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.**

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, grep for required sections). For each "Must NOT Have": search `audit/14-broadsheet-celestial-events.md` for forbidden patterns (theological language outside quotes, Waldeck/Plech as standalone incidents, Stockholm without CONTROL BASELINE tag, events beyond the 7). Check evidence files exist in `.omo/evidence/`. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Quality Review** — `unspecified-high`
  Run `python3 scripts/validate-links.py` → must exit 0 with 0 errors. Run `wc -l audit/14-broadsheet-celestial-events.md` → must be 800–1,500. Grep for `### Source Material`, `### Mainstream Interpretation`, `### Literal Reconstruction`, `### Plausible Mechanism` — count must equal number of HIGH + COMPLEX events (4: Basel, Nuremberg, Stralsund, Fátima). Grep for `**Signal Strength:**` — must return ≥5 (Stockholm, Waldeck/Plech, Nuremberg, Basel, Stralsund, Fátima). Grep for `**Classification:** SPECIES WITH AMNESIA` — must return ≥1. Grep for unauthorized theological terms (miracle, divine, supernatural) outside blockquote contexts. Check all 7 integration files contain expected cross-references.
  Output: `Links [PASS/FAIL] | LineCount [PASS/FAIL] | Framework [N/N] | Tags [N/N] | Tone [PASS/FAIL] | Integration [N/N] | VERDICT`

- [x] F3. **Manual QA** — `unspecified-high`
  Read `audit/14-broadsheet-celestial-events.md` end-to-end. Verify: (1) classification header present, (2) executive summary with numbered findings, (3) signal/noise methodology section applies 12-NHI §2 criteria, (4) each HIGH/COMPLEX event has all 4 framework sections with substantive content (not placeholders), (5) Stockholm is visually distinct as CONTROL BASELINE, (6) Waldeck/Plech are in a Source Credibility subsection NOT standalone incidents, (7) Fátima analysis stays on October 13 aerial phenomenon (no Marian theology deep-dive), (8) counter-explanations get space proportional to scholarly support, (9) every factual claim has a citation, (10) cross-references to 12-NHI, 03-timeline, 04-cross-refs, ancient accounts exist. Save reading notes to `.omo/evidence/final-qa/manual-read-checks.md`.
  Output: `Checks [N/N pass] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual file content (git diff if available). Verify 1:1 — everything in spec was built, nothing beyond spec was built. Check "Must NOT do" compliance: no new PDFs in texts/, no per-event files in audit/analyses/, no events beyond 7, no Fátima prophecy analysis, no Stockholm-as-anomalous treatment, no 11-unified-hypothesis rewriting. Detect cross-task contamination: did the document-writing task accidentally modify integration files? Did integration tasks accidentally modify the main document? Flag unaccounted changes.
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | Unaccounted [CLEAN/N files] | VERDICT`

---

## Commit Strategy

- **Wave 1**: No commits (research output is internal — feeds into Wave 2)
- **After Task 8**: `docs(audit): add 14-broadsheet-celestial-events.md — gap evidence analysis (1535-1917)` — `audit/14-broadsheet-celestial-events.md`
- **After Wave 3 (all integration)**: `docs(audit): integrate broadsheet celestial events across index, timeline, NHI correlation, cross-references, README` — `audit/00-INDEX.md`, `audit/03-event-timeline.md`, `audit/12-NHI-correlation.md`, `audit/04-cross-references.md`, `README.md`, `audit/10-correlation-map.md`, `audit/11-unified-hypothesis.md`
- **After Final Wave**: `docs(audit): verification evidence for broadsheet celestial events plan` — `.omo/evidence/` files
- Pre-commit: `python3 scripts/validate-links.py` must pass

---

## Success Criteria

### Verification Commands
```bash
python3 scripts/validate-links.py                    # Expected: exit 0, 0 errors
wc -l audit/14-broadsheet-celestial-events.md         # Expected: 800-1500
grep -c "### Source Material" audit/14-broadsheet-celestial-events.md      # Expected: 4 (Basel, Nuremberg, Stralsund, Fátima)
grep -c "### Plausible Mechanism" audit/14-broadsheet-celestial-events.md  # Expected: 4
grep -c "Signal Strength" audit/14-broadsheet-celestial-events.md          # Expected: ≥5
grep "14-broadsheet" audit/00-INDEX.md                                    # Expected: ≥1 match
grep -E "1535|1554|1561|1566|1665|1917" audit/03-event-timeline.md        # Expected: ≥1 match
grep "14-broadsheet\|broadsheet" audit/12-NHI-correlation.md              # Expected: ≥1 match
grep "14-broadsheet" README.md                                            # Expected: ≥1 match
```

### Final Checklist
- [x] All "Must Have" present
- [x] All "Must NOT Have" absent
- [x] `validate-links.py` passes with 0 errors
- [x] Document is 800–1,500 lines
- [x] 4 HIGH/COMPLEX events have complete 4-part framework
- [x] Stockholm tagged CONTROL BASELINE, not treated as anomalous
- [x] Waldeck/Plech in Source Credibility subsection only
- [x] All 7 integration files updated
- [x] No unauthorized theological language outside quotes
- [x] Every factual claim cited
