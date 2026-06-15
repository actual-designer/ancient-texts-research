# Plan: Addendum 12 — NHI Correlation Analysis (Revised)

## TL;DR

> **Quick Summary**: Write `audit/12-NHI-correlation.md` — a synthesis document correlating the modern UFO/NHI disclosure discourse with the Archive's unified hypothesis. The thesis is that the NHI conversation describes (via testimony, government acknowledgment, and pattern analysis) the same underlying reality the Archive documents from ancient textual records. The existing plan at `audit/12-NHI-correlation.plan.md` has a sound thesis but needs structural fixes: a methodology section, the timeline tension front-loaded, the "adaptation to expectation" objection addressed, and falsification criteria added.
>
> **Deliverables**:
> - New synthesis document: `audit/12-NHI-correlation.md`
> - Deep sourcing extracts: Key passages from Vallée, Keel, Grusch, AARO, Pasulka
> - Updated `audit/00-INDEX.md` with new entry
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES — 4 waves
> **Critical Path**: Deep sourcing (Tasks 1-3) → Section drafting (Tasks 4-14) → Assembly (Task 15) → INDEX update (Task 16) → Verification (F1-F4)

---

## Context

### Original Request

Analyze `audit/12-NHI-correlation.plan.md` for soundness and produce a revised Sisyphus-ready execution plan. The original plan proposes a document that maps modern NHI discourse terms ("psychic veil," "they see everything," "interdimensional") to Archive equivalents (amnesia architecture, Varuna/Watcher surveillance, three-tier operational tiers).

### Interview/Analysis Summary

**Key analysis findings** (see `.sisyphus/drafts/12-NHI-plan-review.md` for full version):
- **Thesis sound**: NHI as independent evidentiary track converging on Archive's hypothesis is original and defensible.
- **Four gaps found**: (1) No correlation methodology → looks like pattern-seeking bias. (2) 2,500-year timeline gap buried in Section 7 — should be Section 3. (3) Vallée's "adaptation to expectation" objection not addressed. (4) No falsification criteria.
- **Zero existing NHI groundwork**: No NHI/Vallée/Keel references in any existing archive file.
- **Reordered to 12 sections** with 2 new ones (Methodology, Falsification) and Timeline Tension moved up.

**Research findings from explore agents**:
- Archive conventions: classification headers, numbered executive summaries, relative Markdown cross-references, clinical/forensic tone, cross-reference tables matching format in `04-cross-references.md`.
- Key archive documents to cite: `01-entity-registry.md`, `02-technology-catalog.md`, `05-great-reset.md`, `07-the-human-project.md`, `08-translation-key.md`, `09-location-registry.md`, `10-correlation-map.md`, `11-unified-hypothesis.md`.

**Key findings from oracle evaluation**:
- "Methodology gap is the single biggest vulnerability — the plan has no section defining what constitutes a valid correlation vs. coincidence."
- "The 2,500-year gap is structurally underweighted and needs its own section explaining WHY the gap exists."
- "The conflation risk between NHI discourse claims (modern, contested) and Archive textual evidence (ancient, primary source) must be explicitly addressed."

### Metis Review

**Additional considerations raised**:
- Source access: Are Vallée, Keel, Grusch, AARO, Pasulka sources available as PDFs or web-accessible? If not, sourcing tasks need web search / fetch.
- Document relationship: Is `12-NHI-correlation.md` an addendum to the unified hypothesis, a standalone document, or both? Plan treats it as a standalone addendum that cross-references `11-unified-hypothesis.md`.
- Tone calibration: Archive tone is clinical/forensic for ancient texts. NHI discourse includes government testimony, disinformation, and speculative claims. Document must calibrate: modern sources get "cited as testimony, not confirmed fact."
- Scope boundary: This document does NOT update existing synthesis docs — only cross-references them. Scope creep prevention: no revision of 01-11.

---

## Work Objectives

### Core Objective
Produce `audit/12-NHI-correlation.md` — a rigorous, structured synthesis document that maps the modern NHI/UFO disclosure discourse to the Archive's unified hypothesis, following the Archive's established conventions and adding the correlation methodology, timeline analysis, falsification criteria, and counterargument treatment that the original plan lacked.

### Concrete Deliverables
- `audit/12-NHI-correlation.md` — full 12-section synthesis document
- Deep sourcing extracts (working notes, saved to `.sisyphus/evidence/`)
- `audit/00-INDEX.md` updated with new entry

### Definition of Done
- [x] `audit/12-NHI-correlation.md` exists with all 12 sections populated
- [x] Classification header present and correct
- [x] All cross-references verified (relative links to existing `.md` files resolve)
- [x] `audit/00-INDEX.md` updated with new document entry
- [x] F1-F4 verification agents all approve

### Must Have
- Correlation methodology section (what counts, what doesn't, evidence quality tiers)
- Timeline tension as Section 3 (post-Ezekiel gap owned from the start)
- Vallée "control system" section with explicit "adaptation to expectation" counterargument
- Falsification / disconfirmation criteria section
- Correlation table (NHI encounter types → Archive parallels with mechanisms)
- All existing Archive documents cited via relative links

### Must NOT Have (Guardrails)
- No revision of existing synthesis documents (01-11). Cross-reference only.
- No claims that NHI entities ARE Archive entities. "Correlation noted, not claimed."
- No speculative identification of specific modern UFO cases with specific ancient events.
- No tone shift — maintain clinical/forensic register throughout, even when discussing modern sources.
- No evaluation of NHI witness credibility. Report the pattern, don't validate individuals.

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: N/A (this is a Markdown-only research project; no test runner)
- **Automated tests**: None
- **Verification method**: Agent-executed QA scenarios using Read, Grep, and Glob tools to verify document structure, content, and cross-references

### QA Policy
Every task MUST include agent-executed QA scenarios. Since this is a research/writing project:
- **Document verification**: Read output file, verify headings exist, check structure
- **Cross-reference verification**: Grep for `*.md` link patterns, verify target files exist with Glob
- **Content verification**: Grep for required terms (key entities, concepts, source names)
- **Source verification**: Web fetch or PDF reading to confirm key passages

Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.txt`.

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — deep sourcing, MAX PARALLEL):
├── Task 1: Deep source Vallée (Passport to Magonia, Five Arguments, 6-layer model) [writing]
├── Task 2: Deep source Keel + Grusch (Operation Trojan Horse, 2023 testimony) [writing]
└── Task 3: Deep source AARO + Pasulka (official reports, American Cosmic) [writing]

Wave 2 (After Wave 1 — write all sections, MAX PARALLEL):
├── Task 4: Write Section 1 (Executive Summary) [writing]
├── Task 5: Write Section 2 (Correlation Methodology) [deep]
├── Task 6: Write Section 3 (Timeline Tension) [writing]
├── Task 7: Write Section 4 (NHI Discourse Lineage) [writing]
├── Task 8: Write Section 5 (Membrane = Amnesia Architecture) [writing]
├── Task 9: Write Section 6 (Surveillance + Cognitive Access) [writing]
├── Task 10: Write Section 7 (Three Tiers as "Other Dimension") [writing]
├── Task 11: Write Section 8 (Vallée Control System + adaptation counterargument) [deep]
├── Task 12: Write Section 9 (Correlation Table) [writing]
├── Task 13: Write Section 10 (What the Archive Adds) [writing]
├── Task 14: Write Sections 11-12 (Falsification + Open Questions) [deep]
└── Task 15: Update audit/00-INDEX.md [quick]

Wave 3 (After Wave 2 — assembly):
└── Task 16: Compose full document, resolve cross-references, polish tone [deep]

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── Task F1: Plan compliance audit [oracle]
├── Task F2: Cross-reference integrity check [unspecified-high]
├── Task F3: Thematic fidelity scan [deep]
└── Task F4: Source-footing verification [deep]

Critical Path: Tasks 1-3 → Tasks 4-15 → Task 16 → F1-F4 → user okay
Parallel Speedup: ~60% faster than sequential
Max Concurrent: 8 (Wave 2)
```

### Dependency Matrix
- Tasks 1-3: independent, parallel (Wave 1)
- Tasks 4-15: depend on Tasks 1-3 (need source material); independent of each other (Wave 2)
- Task 16: depends on Tasks 4-15 (all sections drafted) (Wave 3)
- F1-F4: depend on Task 16; parallel (Wave FINAL)

### Agent Dispatch Summary
- **Wave 1**: 3 agents (writing category — source extraction)
- **Wave 2**: 12 agents (10 writing + 2 deep — section drafting)
- **Wave 3**: 1 agent (deep — assembly)
- **Wave FINAL**: 4 agents (oracle, unspecified-high, deep, deep — review)

---

## TODOs

> **IMPORTANT**: Each task writes its assigned section(s) into a fragment file under `.sisyphus/evidence/fragments/task-{N}-section-{name}.md`. Task 16 (assembly) combines all fragments into the final document.
> 
> All tasks MUST include QA scenarios. A task without QA scenarios is INCOMPLETE.

---

- [x] 1. Deep Source Vallée

  **What to do**:
  - Locate and extract key passages from three Vallée sources:
    1. *Passport to Magonia* (1969) — parallel universe thesis, fairy/UFO connection, historical continuum argument
    2. "Five Arguments Against the Extraterrestrial Origin of UFOs" (1990 paper) — all five arguments
    3. Vallée & Davis 6-layer model (2003) — the six layers of UFO phenomenon
  - Sources may be available via web search/fetch or PDF in `texts/`. Use librarian agent or web search if PDFs not present.
  - Extract exact quotes with page/chapter references where possible.
  - Save extracts to `.sisyphus/evidence/deep-source-vallee.md`

  **Must NOT do**:
  - Do NOT rely on secondary summaries of Vallée — find primary text.
  - Do NOT include popular UFO culture references (von Däniken, ancient aliens TV show).

  **Recommended Agent Profile**:
  - **Category**: `writing` (research + technical writing)
  - **Skills**: None needed (general web research + document extraction)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3)
  - **Blocks**: Tasks 4-15
  - **Blocked By**: None

  **References**:
  - Archive framework: `claude.md` (literalist/technological lens methodology)
  - Existing plan: `audit/12-NHI-correlation.plan.md` (see lines 35-42 for Vallée context)
  - External: Passport to Magonia (ISBN 978-1568586732) — web search for accessible text
  - External: "Five Arguments Against the Extraterrestrial Origin of UFOs" — J. Scientific Exploration, 1990
  - External: Vallée & Davis, "Incommensurability, Orthodoxy and the Physics of Messiahs" — 2003

  **Acceptance Criteria**:
  - [ ] `.sisyphus/evidence/deep-source-vallee.md` created with extracts from all 3 sources
  - [ ] Each extract includes: source title, passage context, exact quote
  - [ ] At least 3 passages per source (9+ total)
  - [ ] Page/chapter references included where available

  **QA Scenarios**:
  ```
  Scenario: Vallée sourcing completeness
    Tool: Bash
    Preconditions: Task 1 complete
    Steps:
      1. Read `.sisyphus/evidence/deep-source-vallee.md`
      2. grep for "Passport to Magonia" — should have extracts
      3. grep for "Five Arguments" — should have extracts
      4. grep for "6-layer" or "six layer" — should have extracts
      5. Count extracts: at least 9 entries
    Expected Result: File exists with ≥3 sources and ≥9 passages
    Evidence: .sisyphus/evidence/task-1-vallee-qa.txt
  ```

- [x] 2. Deep Source Keel + Grusch

  **What to do**:
  - Locate and extract key passages from:
    1. John Keel, *Operation Trojan Horse* (1970) — "ultraterrestrial" concept, historical continuum of phenomena, control system thesis
    2. David Grusch congressional testimony (July 2023) — NHI vs extraterrestrial distinction, crash retrieval claims, legacy programs
  - Extract exact quotes with context.
  - Save extracts to `.sisyphus/evidence/deep-source-keel-grusch.md`

  **Must NOT do**:
  - Do NOT include Keel's more fringe claims (Mothman, specific prophecies) — focus on the structural thesis
  - Do NOT evaluate Grusch's credibility — extract the NHI framework claims only

  **Recommended Agent Profile**:
  - **Category**: `writing` (research)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3)
  - **Blocks**: Tasks 4-15
  - **Blocked By**: None

  **References**:
  - Existing plan: `audit/12-NHI-correlation.plan.md` lines 35-42
  - External: Keel, *Operation Trojan Horse* (1970) — web search for accessible text/key excerpts
  - External: Grusch testimony transcript — available via U.S. House Oversight Committee (July 26, 2023)

  **Acceptance Criteria**:
  - [ ] `.sisyphus/evidence/deep-source-keel-grusch.md` created
  - [ ] Keel: at least 3 passages on ultraterrestrial concept and historical continuum
  - [ ] Grusch: at least 3 passages on NHI/interdimensional distinction

  **QA Scenarios**:
  ```
  Scenario: Keel + Grusch sourcing completeness
    Tool: Bash
    Preconditions: Task 2 complete
    Steps:
      1. Read `.sisyphus/evidence/deep-source-keel-grusch.md`
      2. grep for "ultraterrestrial" — should have Keel passages
      3. grep for "Grusch" — should have testimony extracts
      4. Verify ≥6 passages total
    Expected Result: File exists, both sources present with ≥3 passages each
    Evidence: .sisyphus/evidence/task-2-keel-grusch-qa.txt
  ```

- [x] 3. Deep Source AARO + Pasulka

  **What to do**:
  - Locate and extract key passages from:
    1. AARO (All-domain Anomaly Resolution Office) public reports — current official U.S. posture, historical review findings, key conclusions
    2. Pasulka, *American Cosmic* (2019) — modern academic framing of UFO phenomenon, the "disclosure" movement as religious/philosophical event, technology and NHI convergence
    - Sources likely require web search/fetch. Use librarian agent if needed.
  - Save extracts to `.sisyphus/evidence/deep-source-aaro-pasulka.md`

  **Must NOT do**:
  - Do NOT include AARO's internal organizational details — focus on posture and findings
  - Do NOT treat AARO conclusions as authoritative — they are one data point

  **Recommended Agent Profile**:
  - **Category**: `writing` (research)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2)
  - **Blocks**: Tasks 4-15
  - **Blocked By**: None

  **References**:
  - External: AARO public reports — https://www.aaro.mil/public/
  - External: Pasulka, D.W. *American Cosmic: UFOs, Religion, Technology* (Oxford University Press, 2019)

  **Acceptance Criteria**:
  - [ ] `.sisyphus/evidence/deep-source-aaro-pasulka.md` created
  - [ ] AARO: at least 2 key conclusions from public reports
  - [ ] Pasulka: at least 3 passages on disclosure as cultural/philosophical phenomenon

  **QA Scenarios**:
  ```
  Scenario: AARO + Pasulka sourcing
    Tool: Bash
    Preconditions: Task 3 complete
    Steps:
      1. Read `.sisyphus/evidence/deep-source-aaro-pasulka.md`
      2. grep -i for "AARO" — should have passages
      3. grep -i for "Pasulka" or "American Cosmic" — should have passages
      4. Verify ≥5 passages total
    Expected Result: File exists, both sources present
    Evidence: .sisyphus/evidence/task-3-aaro-pasulka-qa.txt
  ```

---

- [x] 4. Write Section 1: Executive Summary

  **What to do**:
  - Write 5-8 numbered findings synthesizing the entire document's argument.
  - Each finding must be a standalone claim that the body sections support.
  - Must include the core thesis: NHI discourse = independent evidentiary track converging on Archive's unified hypothesis.
  - Use sourced passages from Tasks 1-3 to anchor key claims.
  - Save to `.sisyphus/evidence/fragments/task-4-executive-summary.md`

  **Must NOT do**:
  - Do NOT introduce new claims not supported by body sections
  - Do NOT exceed 8 findings

  **Recommended Agent Profile**:
  - **Category**: `writing` (synthesis writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 5-15)
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Existing executive summaries: `audit/07-the-human-project.md:1-15` — format and tone
  - Capstone findings: `audit/11-unified-hypothesis.md:9-40` — finding numbering pattern
  - Source extracts: `.sisyphus/evidence/deep-source-vallee.md`, `.sisyphus/evidence/deep-source-keel-grusch.md`, `.sisyphus/evidence/deep-source-aaro-pasulka.md`

  **Acceptance Criteria**:
  - [ ] Fragment file created with 5-8 numbered findings
  - [ ] Each finding references evidence from tasks 1-3
  - [ ] Tone matches existing archive documents (clinical/forensic)

  **QA Scenarios**:
  ```
  Scenario: Executive summary structure
    Tool: Bash
    Preconditions: Task 4 complete
    Steps:
      1. Read `.sisyphus/evidence/fragments/task-4-executive-summary.md`
      2. Count numbered findings (grep for "\d\.\s" or "^\d\.") — verify 5-8
      3. Check for classification header
      4. grep for "NHI" — should appear
    Expected Result: 5-8 numbered findings, clinical tone, NHI reference present
    Evidence: .sisyphus/evidence/task-4-exec-qa.txt
  ```

- [x] 5. Write Section 2: Correlation Methodology

  **What to do**:
  - Write the NEW methodology section that the original plan lacked.
  - Define:
    1. What constitutes a valid correlation: specific structural overlap between NHI claim and Archive evidence (same operational pattern, not vague thematic resemblance)
    2. What constitutes a negative correlation / disconfirmation: NHI pattern that contradicts Archive prediction
    3. Evidence quality tiers: distinguish (a) ancient textual evidence — curated primary sources, (b) modern NHI testimony — oral reports, government testimony, (c) secondary analysis — Pasulka, academic frameworks
    4. Guardrails against confirmation bias: explicit acknowledgment that the "everything maps" risk exists
  - Save to `.sisyphus/evidence/fragments/task-5-methodology.md`

  **Must NOT do**:
  - Do NOT make this section longer than 1/10 of the total document
  - Do NOT claim the correlation is proven — present it as a framework for evaluation

  **Recommended Agent Profile**:
  - **Category**: `deep` (analytical methodology writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Existing methodology: `audit/04-cross-references.md:9-12` — "Purpose" section for parallel account methodology
  - Existing falsification: `audit/11-unified-hypothesis.md:473-485` — falsification criteria format
  - Analysis findings: My evaluation identified this as the #1 gap (see `.sisyphus/drafts/12-NHI-plan-review.md`)

  **Acceptance Criteria**:
  - [ ] Fragment file created with all 4 methodology sub-parts
  - [ ] Evidence quality tiers explicitly defined
  - [ ] Confirmation bias guardrail explicitly stated

  **QA Scenarios**:
  ```
  Scenario: Methodology completeness
    Tool: Bash
    Preconditions: Task 5 complete
    Steps:
      1. Read fragment file
      2. grep for "valid correlation" or "correlation" — should be at least 5 lines
      3. grep for "evidence" — should discuss evidence tiers
      4. grep for "confirmation bias" or "guardrail" or "everything maps" — guardrail should exist
      5. Check length: ≥200 words, ≤600 words
    Expected Result: Methodology section with correlation criteria, evidence tiers, bias guardrail
    Evidence: .sisyphus/evidence/task-5-methodology-qa.txt
  ```

- [x] 6. Write Section 3: Timeline Tension

  **What to do**:
  - Write the timeline tension section (moved from original Section 7 to Section 3 per analysis recommendation).
  - Must cover:
    1. The gap: Archive's last direct contact is Ezekiel (~573 BCE). NHI discourse describes ongoing active phenomenon.
    2. Reading A — Post-mortem pipeline as continuous interface: operators shifted from direct surface contact to post-mortem integration model; modern NHI encounters represent leakage from processing pipeline or selective Tier 2 interventions
    3. Reading B — Renewed contact via contamination cycle: modern technological civilization (nuclear, AI, environmental) may be parameter exceedance event; current disclosure wave could be precursor
    4. Why Archive cannot distinguish readings
    5. How NHI evidence might resolve the ambiguity
  - Save to `.sisyphus/evidence/fragments/task-6-timeline-tension.md`

  **Must NOT do**:
  - Do NOT privilege one reading over the other
  - Do NOT claim the gap proves absence — state it honestly

  **Recommended Agent Profile**:
  - **Category**: `writing` (analytical writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Timeline data: `audit/03-event-timeline.md:480-506` — Ezekiel dates, post-Ezekiel gap, Revelation briefing
  - Unified hypothesis open questions: `audit/11-unified-hypothesis.md:489-495` — operator withdrawal ambiguity
  - Original plan: `audit/12-NHI-correlation.plan.md:88-101` — original timeline tension draft
  - Post-mortem pipeline: `audit/analyses/book-of-the-dead.md` — processing infrastructure
  - Source extracts: Tasks 1-3

  **Acceptance Criteria**:
  - [ ] Fragment file created with both readings fully developed
  - [ ] Each reading cites at least 2 Archive sources
  - [ ] Section explicitly states the Archive cannot distinguish readings
  - [ ] Discussion of how NHI evidence could break the tie

  **QA Scenarios**:
  ```
  Scenario: Timeline tension completeness
    Tool: Bash
    Preconditions: Task 6 complete
    Steps:
      1. Read fragment file
      2. grep for "573 BCE" or "Ezekiel" — gap should be explicitly stated
      3. grep for "Reading A" or "post-mortem" — Reading A present
      4. grep for "Reading B" or "contamination cycle" — Reading B present
      5. grep for "cannot distinguish" or "insufficient data" — ambiguity admitted
    Expected Result: Both readings present, gap acknowledged, ambiguity admitted
    Evidence: .sisyphus/evidence/task-6-timeline-qa.txt
  ```

---

- [x] 7. Write Section 4: The NHI Discourse — Independent Evidentiary Track

  **What to do**:
  - Write the intellectual lineage of NHI discourse:
    - Meade Layne (1947, "etheric" discs)
    - John Keel (1970, *Operation Trojan Horse*, ultraterrestrials)
    - Jacques Vallée (1969-2003, parallel universe, Five Arguments, 6-layer model)
    - Hynek (classification system, shift from ETH)
    - Modern disclosure: Grusch (2023, NHI/interdimensional), Elizondo, AARO
  - Use deep sourcing extracts from Tasks 1-3 for key quotes.
  - Save to `.sisyphus/evidence/fragments/task-7-nhi-lineage.md`

  **Must NOT do**:
  - Do NOT include fringe figures (Billy Meier, Bob Lazar) without explicit textual relevance
  - Do NOT turn this into a history of ufology — it's a focused intellectual lineage

  **Recommended Agent Profile**:
  - **Category**: `writing` (historical/expository writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Source extracts: `.sisyphus/evidence/deep-source-vallee.md`, `.sisyphus/evidence/deep-source-keel-grusch.md`, `.sisyphus/evidence/deep-source-aaro-pasulka.md`
  - Original plan: `audit/12-NHI-correlation.plan.md:34-43` — intellectual lineage draft

  **Acceptance Criteria**:
  - [ ] Fragment file created with all lineage figures covered
  - [ ] At least 3 direct quotes from source extracts
  - [ ] Lineage presented as chronological narrative

  **QA Scenarios**:
  ```
  Scenario: Lineage completeness
    Tool: Bash
    Preconditions: Task 7 complete
    Steps:
      1. Read fragment file
      2. grep -i for "Layne" — must appear
      3. grep -i for "Keel" — must appear
      4. grep -i for "Vallée" or "Vallee" — must appear
      5. grep -i for "Hynek" — must appear
      6. grep -i for "Grusch" — must appear
      7. Count direct quotes (lines beginning with ">"): ≥3
    Expected Result: All 5 key figures covered, 3+ direct quotes
    Evidence: .sisyphus/evidence/task-7-lineage-qa.txt
  ```

- [x] 8. Write Section 5: The Membrane Is the Amnesia Architecture

  **What to do**:
  - Write the core correlation: NHI "psychic veil" / "dimensional membrane" = Archive's engineered amnesia architecture
  - Must cover:
    1. What NHI discourse says: active limitation on human perception, co-located beings, diffusion filter
    2. What Archive documents: Popol Vuh "breath upon the face of a mirror" — engineered cognitive throttling
    3. Both frameworks describe active/permanent limitation, not passive barrier
    4. Neither claims the beings are "elsewhere" — both claim they are here, prevented from being perceived
  - Save to `.sisyphus/evidence/fragments/task-8-membrane-amnesia.md`

  **Must NOT do**:
  - Do NOT claim identity of mechanism — NHI calls it "psychic," Archive calls it "engineered"
  - Do NOT overstate — present correlation, not proof

  **Recommended Agent Profile**:
  - **Category**: `writing` (comparative analysis)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Popol Vuh amnesia: `audit/analyses/popol-vuh.md` — "breath upon mirror" passage
  - Amnesia architecture: `audit/07-the-human-project.md` — human project management arc
  - NHI membrane concept: `.sisyphus/evidence/deep-source-vallee.md` — Vallée's "psychic veil"
  - Translation key: `audit/08-translation-key.md` — vocabulary mapping methodology

  **Acceptance Criteria**:
  - [ ] Fragment file created
  - [ ] Popol Vuh "breath upon mirror" cited directly
  - [ ] NHI veil claims cited from at least 2 source extracts (Tasks 1-3)
  - [ ] Agnostic position on mechanism maintained

  **QA Scenarios**:
  ```
  Scenario: Membrane-Amnesia correlation
    Tool: Bash
    Preconditions: Task 8 complete
    Steps:
      1. Read fragment file
      2. grep for "breath upon" or "mirror" — Popol Vuh reference present
      3. grep for "psychic veil" or "membrane" — NHI reference present
      4. grep for "active" — both frameworks describe active limitation
      5. grep for "not claimed" or "agnostic" or "correlation" — appropriate epistemic caution
    Expected Result: Both frameworks described, Popol Vuh cited, epistemic caution present
    Evidence: .sisyphus/evidence/task-8-membrane-qa.txt
  ```

- [x] 9. Write Section 6: Total Surveillance and Cognitive Access

  **What to do**:
  - Write the "they see everything / they read our minds" correlation.
  - NHI claim: continuous surveillance and cognitive access by non-human intelligence
  - Archive documentation:
    1. Varuna's "thousand eyes" distributed sensor network — Rig Veda I.25, VII.86
    2. Shamash's real-time battlefield intelligence — Gilgamesh
    3. Watcher reporting system — Enoch (monitoring, logging)
    4. "Eyes of the Lord" motif — Hebrew prophetic literature
    5. Cognitive access: Yoga Sutras citta-vṛtti-nirodha (consciousness lockdown); operators knowing intentions across texts
  - Save to `.sisyphus/evidence/fragments/task-9-surveillance.md`

  **Must NOT do**:
  - Do NOT claim these are the same surveillance system — note structural parallel
  - Do NOT add modern surveillance state analogies (NSA, etc.)

  **Recommended Agent Profile**:
  - **Category**: `writing` (evidentiary synthesis)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Entity surveillance: `audit/01-entity-registry.md` — Watchers, Varuna, Shamash
  - Technology surveillance: `audit/02-technology-catalog.md` — "Eyes of the Lord" sensor network
  - Cognitive access: `audit/analyses/yoga-sutras.md` — citta-vṛtti-nirodha
  - NHI claims: `.sisyphus/evidence/deep-source-keel-grusch.md` — Grusch on advanced capabilities

  **Acceptance Criteria**:
  - [ ] Fragment file created
  - [ ] At least 3 Archive surveillance sources cited
  - [ ] At least 1 Yoga Sutras / cognitive access reference
  - [ ] NHI claim cited from source extracts

  **QA Scenarios**:
  ```
  Scenario: Surveillance section
    Tool: Bash
    Preconditions: Task 9 complete
    Steps:
      1. Read fragment file
      2. grep -i for "Varuna" — must appear
      3. grep -i for "Watcher" — must appear
      4. grep -i for "Yoga" or "citta" — cognitive access covered
      5. grep -i for "Shamash" — optional but preferred
    Expected Result: 3+ Archive sources, cognitive access covered, NHI claims present
    Evidence: .sisyphus/evidence/task-9-surveillance-qa.txt
  ```

---

- [x] 10. Write Section 7: Three Tiers as "Other Dimension"

  **What to do**:
  - Write the agnostic-position correlation between NHI "other dimension" and Archive's three-tier architecture.
  - Must cover:
    1. NHI: beings that "phase in and out of reality"
    2. Archive: transit between orbital, surface, subsurface tiers appears as dimensional shift to perception-limited observer
    3. NHI "other realm" maps structurally to subsurface tier (Duat, Xibalbá, Tartarus, Hel)
    4. NHI encounters in liminal states map to post-mortem integration pipeline interface
    5. Vallée's fifth argument (space/time manipulation) consistent with Archive's gated transit corridors and FTL-capable vehicles
  - **Position: Agnostic.** Explicitly state: "The Archive does not claim identity between 'dimensions' and 'tiers.' Structural correlation noted, not identity claimed."
  - Save to `.sisyphus/evidence/fragments/task-10-three-tiers.md`

  **Must NOT do**:
  - Do NOT claim identity — maintain agnostic position
  - Do NOT interpret NHI claim as confirming tier architecture — they are parallel descriptions

  **Recommended Agent Profile**:
  - **Category**: `writing` (careful epistemic positioning)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Tier architecture: `audit/09-location-registry.md` — three-tier system
  - NHI dimensional claims: `.sisyphus/evidence/deep-source-vallee.md` — Vallée on parallel universe
  - Subsurface facilities: `audit/analyses/book-of-the-dead.md`, `audit/analyses/popol-vuh.md`
  - Original plan: `audit/12-NHI-correlation.plan.md:67-74` — original draft

  **Acceptance Criteria**:
  - [ ] Fragment file created
  - [ ] Agnostic position stated explicitly
  - [ ] At least 3 Archive tier references
  - [ ] NHI dimensional claim cited from source extracts (Task 1-3)

  **QA Scenarios**:
  ```
  Scenario: Three Tiers section
    Tool: Bash
    Preconditions: Task 10 complete
    Steps:
      1. Read fragment file
      2. grep for "agnostic" or "not claim" or "correlation noted" — agnostic position present
      3. grep for "orbital" or "surface" or "subsurface" — tiers discussed
      4. grep for "Duat" or "Xibalbá" or "Tartarus" or "Hel" — subsurface mapping
      5. grep for "Vallée" — fifth argument addressed
    Expected Result: Agnostic, tiers discussed, subsurface mapped, Vallée cited
    Evidence: .sisyphus/evidence/task-10-tiers-qa.txt
  ```

- [x] 11. Write Section 8: Vallée's Control System vs. Archive's Institutional Management

  **What to do**:
  - Write the most intellectually complex section.
  - Must cover:
    1. Vallée's core insight: UFO phenomenon = control system modulating human belief, cognition, culture
    2. Evidence: appears in forms matching observer expectations, maintains "one step beyond" gap, adapts to frameworks (airships → rockets → orbs → tic-tacs)
    3. Archive's description: stratified command hierarchy with documented operational history, departmental portfolios, internal factionalism, amnesia architecture
    4. Synthesis: Vallée identified pattern but lacked historical record to identify operators
    5. **CRITICAL: Address the "adaptation to expectation" objection.** If phenomenon adapts to cultural expectations, the NHI-Archive correlation might mean the phenomenon is manifesting in forms shaped by cultural familiarity with ancient texts — which would undercut the "independent evidentiary track" claim.
    - Response: The specific operational details (hierarchy, portfolios, post-mortem processing) converge with ancient records that were **unknown** to most modern witnesses until recently. This is a stronger argument than simply claiming Vallée lacked operator history.
    6. Watcher punishment for unauthorized disclosure (Enoch) as evidence of controlled knowledge transfer
  - Save to `.sisyphus/evidence/fragments/task-11-control-system.md`

  **Must NOT do**:
  - Do NOT dismiss Vallée's framework — treat it as partial, not wrong
  - Do NOT straw-man the adaptation objection — address it fairly before responding

  **Recommended Agent Profile**:
  - **Category**: `deep` (counterargument-aware analytical writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Vallée extracts: `.sisyphus/evidence/deep-source-vallee.md`
  - Watcher punishment: `audit/analyses/enoch-watchers.md`
  - Archive institutional structure: `audit/01-entity-registry.md`, `audit/06-weapons-doctrine.md`
  - Original plan: `audit/12-NHI-correlation.plan.md:76-86` — original control system analysis

  **Acceptance Criteria**:
  - [ ] Fragment file created
  - [ ] Vallée's control system thesis summarized accurately
  - [ ] Archive institutional structure described
  - [ ] "Adaptation to expectation" objection stated and addressed
  - [ ] Watchers case cited

  **QA Scenarios**:
  ```
  Scenario: Control system section
    Tool: Bash
    Preconditions: Task 11 complete
    Steps:
      1. Read fragment file
      2. grep -i for "Vallée" or "Vallee" — control system discussed
      3. grep -i for "control system" — Vallée's insight present
      4. grep for "adapt" or "expectation" — objection addressed
      5. grep -i for "Watcher" — Enoch citation
      6. grep for "unknown" or "independent evidentiary" — response to objection
    Expected Result: Vallée's thesis, Archive counter, adaptation addressed, Watchers cited
    Evidence: .sisyphus/evidence/task-11-control-qa.txt
  ```

- [x] 12. Write Section 9: Correlation Table

  **What to do**:
  - Write the correlation table (NHI encounter type → Archive parallel → mechanism).
  - Table must cover these rows (from original plan with possible additions):
    - Craft sightings → Merkabah/vimānas/crystal houses → aerospace vehicles with field propulsion
    - Abduction / medical exam → Enoch's guided tours / Mahābhārata commissions → processing facility intake
    - Telepathic contact → Operator warnings (Enki, Shamash) → direct cognitive interface
    - Poltergeist / psychic → Watcher technology transfer → cross-tier interference
    - Missing time → Ezekiel transport / Tuat transit → tier transit time differential
    - Hybrid offspring → Nephilim / Gilgamesh / Pāṇḍavas → documented hybridization programs
    - Near-death / tunnel of light → Duat→Akhet→Sky processing → post-mortem extraction
    - Visitations in sleep / liminal → Enoch's journeys / dream oracles → cognitive interface mode
    - Screen memories → Engineered amnesia (Popol Vuh) → cognitive limitation filtering recall
  - Add a "Convergence Strength" column: HIGH / MEDIUM / LOW per correlation
  - Save to `.sisyphus/evidence/fragments/task-12-correlation-table.md`

  **Must NOT do**:
  - Do NOT inflate convergence strength — be honest about weaker correlations
  - Do NOT add rows beyond what the source material supports

  **Recommended Agent Profile**:
  - **Category**: `writing` (structured data writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Original table: `audit/12-NHI-correlation.plan.md:104-115` — NHI→Archive mapping
  - Archive technology: `audit/02-technology-catalog.md` — vimānas, cognitive tech
  - Archive locations: `audit/09-location-registry.md` — tier locations
  - Entity registry: `audit/01-entity-registry.md` — Watchers, Nephilim
  - Source extracts: Tasks 1-3

  **Acceptance Criteria**:
  - [ ] Fragment file created with valid Markdown table
  - [ ] All 9 rows present
  - [ ] Convergence Strength column included (HIGH/MEDIUM/LOW)
  - [ ] Each row has a mechanism
  - [ ] At least 2 rows marked MEDIUM or LOW (honest assessment)

  **QA Scenarios**:
  ```
  Scenario: Correlation table
    Tool: Bash
    Preconditions: Task 12 complete
    Steps:
      1. Read fragment file
      2. Count table rows (excluding header): ≥9
      3. grep for "HIGH" — must exist
      4. grep for "MEDIUM" or "LOW" — must exist (honest assessment)
      5. Verify valid Markdown table: lines contain "|" separators
    Expected Result: Complete 9-row table with convergence strength, valid Markdown
    Evidence: .sisyphus/evidence/task-12-table-qa.txt
  ```

---

- [x] 13. Write Section 10: What the Archive Adds

  **What to do**:
  - Write the "value add" section — what the Archive provides that NHI discourse lacks:
    1. Documented management history across 4,000+ years
    2. Specific mechanism for the membrane (engineered cognitive limitation)
    3. Institutional context (stratified organization, factionalism, coups)
    4. Return path (post-mortem integration pipeline)
    5. Specific, falsifiable predictions
  - Each point must be cross-referenced to existing Archive documents.
  - Save to `.sisyphus/evidence/fragments/task-13-archive-adds.md`

  **Must NOT do**:
  - Do NOT claim the Archive has "solved" the NHI mystery — it provides context
  - Do NOT diminish NHI discourse — present Archive as complementary, not superior

  **Recommended Agent Profile**:
  - **Category**: `writing` (comparative value writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Original plan: `audit/12-NHI-correlation.plan.md:117-127` — 5 value-adds
  - All existing synthesis documents (01-11)
  - Unified hypothesis predictions: `audit/11-unified-hypothesis.md:457-471`

  **Acceptance Criteria**:
  - [ ] Fragment file created
  - [ ] All 5 value-adds present
  - [ ] Each point cross-referenced to ≥1 Archive document
  - [ ] Unified hypothesis predictions cited under point 5

  **QA Scenarios**:
  ```
  Scenario: Archive adds section
    Tool: Bash
    Preconditions: Task 13 complete
    Steps:
      1. Read fragment file
      2. Count numbered points: 5
      3. grep for ".md" — cross-references present
      4. grep for "prediction" or "falsifiable" — predictions cited
    Expected Result: 5 points, all cross-referenced, predictions cited
    Evidence: .sisyphus/evidence/task-13-adds-qa.txt
  ```

- [x] 14. Write Sections 11-12: Falsification + Open Questions

  **What to do**:
  - Write **Section 11: Disconfirmation Conditions** (NEW section per analysis recommendations)
    - What would falsify the NHI-Archive correlation:
      1. NHI encounters reveal operational patterns NOT matching Archive hierarchy
      2. NHI physical evidence (craft, biological) shows no connection to described technologies
      3. NHI disclosure reveals entirely different ontological framework incompatible with Archive
      4. Archaeological evidence contradicts timeline predictions
    - Format: mirror the falsification criteria from `11-unified-hypothesis.md`
  - Write **Section 12: Open Questions** (expanded from original Section 10)
    - Amnesia architecture degradation over time
    - Disclosure movement drivers (human govt vs phenomenon itself)
    - NDE / NHI contact overlap
    - Parameter exceedance cycle prediction
    - NEW: Source quality and availability limitations
    - NEW: The "disclosure as control system operation" possibility (Vallée's concern)
  - Save to `.sisyphus/evidence/fragments/task-14-falsification-questions.md`

  **Must NOT do**:
  - Do NOT make falsification criteria impossible to satisfy
  - Do NOT frame open questions as rhetorical — they must be genuinely unresolved

  **Recommended Agent Profile**:
  - **Category**: `deep` (falsification framework writing)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 16
  - **Blocked By**: Tasks 1-3

  **References**:
  - Falsification model: `audit/11-unified-hypothesis.md:473-485` — 5 falsification conditions
  - Open questions model: `audit/11-unified-hypothesis.md:487-495` — open questions format
  - Original open questions: `audit/12-NHI-correlation.plan.md:129-134`
  - Analysis findings: `.sisyphus/drafts/12-NHI-plan-review.md`

  **Acceptance Criteria**:
  - [ ] Fragment file created with both sections
  - [ ] Section 11: ≥4 disconfirmation conditions
  - [ ] Section 12: ≥5 open questions
  - [ ] Falsification conditions are specific and testable

  **QA Scenarios**:
  ```
  Scenario: Falsification + questions
    Tool: Bash
    Preconditions: Task 14 complete
    Steps:
      1. Read fragment file
      2. grep for "Disconfirmation" or "falsifi" — Section 11 present
      3. grep for "Open Questions" — Section 12 present
      4. Count conditions in Section 11: ≥4
      5. Count questions in Section 12: ≥5
      6. Check conditions are specific (not vague like "if science proves otherwise")
    Expected Result: ≥4 conditions, ≥5 questions, specific criteria
    Evidence: .sisyphus/evidence/task-14-falsification-qa.txt
  ```

---

- [x] 15. Update `audit/00-INDEX.md`

  **What to do**:
  - Add a new entry to the Audit Documents table for `12-NHI-correlation.md`
  - Follow the existing table format in `00-INDEX.md`
  - Entry text: `| [12-nhi-correlation.md](12-nhi-correlation.md) | NHI/Archive correlation synthesis — maps modern UFO/NHI discourse to unified hypothesis; correlation methodology, timeline analysis, counterargument treatment, falsification criteria |`
  - Insert after the existing `11-unified-hypothesis.md` entry

  **Must NOT do**:
  - Do NOT alter any existing entries
  - Do NOT change formatting of existing table

  **Recommended Agent Profile**:
  - **Category**: `quick` (single targeted edit)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (independent)
  - **Blocks**: F1-F4
  - **Blocked By**: None

  **References**:
  - INDEX file: `audit/00-INDEX.md` — existing audit documents table at lines 54-65

  **Acceptance Criteria**:
  - [ ] New entry for `12-nhi-correlation.md` added to table
  - [ ] Table formatting preserved (valid Markdown table)
  - [ ] No existing entries modified

  **QA Scenarios**:
  ```
  Scenario: INDEX update
    Tool: Bash
    Preconditions: Task 15 complete
    Steps:
      1. Read `audit/00-INDEX.md`
      2. grep -A 15 for "| \\[11-" — find the unified hypothesis entry
      3. Verify new entry exists after it
      4. Check entry contains "12-nhi-correlation.md"
    Expected Result: New entry present, table valid, existing entries untouched
    Evidence: .sisyphus/evidence/task-15-index-qa.txt
  ```

---

- [x] 16. Compose Full Document

  **What to do**:
  - This is the **assembly task** — combine all fragments into final `audit/12-NHI-correlation.md`
  - Steps:
    1. Read all fragment files from `.sisyphus/evidence/fragments/task-{N}-*.md`
    2. Combine in section order: Executive Summary → Methodology → Timeline Tension → NHI Lineage → Membrane/Amnesia → Surveillance/Cognitive → Three Tiers → Control System → Correlation Table → Archive Adds → Falsification/Questions
    3. Add classification header: `**Classification:** SPECIES WITH AMNESIA -- Working Hypothesis` + `**Analyst:** The Chronos Archive, Lead Investigator`
    4. Add scope line: `**Scope:** Cross-cutting synthesis of NHI/UFO disclosure discourse (Keel, Vallée, Hynek, Grusch, AARO, Pasulka) correlated with Archive's unified hypothesis and all prior synthesis documents`
    5. Normalize cross-references: all `audit/*.md` links should be relative (e.g., `[01-entity-registry.md](01-entity-registry.md)`)
    6. Resolve any duplicate content between sections
    7. Ensure consistent clinical/forensic tone throughout
    8. Add the document header: `# NHI Correlation: An Addendum to the Unified Hypothesis`
    9. Save to `audit/12-NHI-correlation.md`

  **Must NOT do**:
  - Do NOT add new content not present in fragments — this is assembly only
  - Do NOT change meaning of any section
  - Do NOT remove citations or cross-references

  **Recommended Agent Profile**:
  - **Category**: `deep` (complex text assembly + normalization)
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (depends on all fragments)
  - **Blocks**: F1-F4
  - **Blocked By**: Tasks 4-15

  **References**:
  - All fragment files in `.sisyphus/evidence/fragments/`
  - Classification header format: any existing audit document (e.g., `audit/07-the-human-project.md:1-5`)
  - Cross-reference format: `audit/04-cross-references.md` — relative link style

  **Acceptance Criteria**:
  - [ ] `audit/12-NHI-correlation.md` exists
  - [ ] Classification header present
  - [ ] All 12 sections present and in order
  - [ ] All cross-references use relative links
  - [ ] Consistent clinical tone throughout
  - [ ] No duplicate content blocks

  **QA Scenarios**:
  ```
  Scenario: Full document structure
    Tool: Bash
    Preconditions: Task 16 complete
    Steps:
      1. Read `audit/12-NHI-correlation.md` (first 20 lines)
      2. grep "^## " — count section headings
      3. grep for "SPECIES WITH AMNESIA" — classification header present
      4. grep for "The Chronos Archive" — analyst credit present
      5. grep -oP "\\[.+?\\]\\([^)]+\\.md\\)" | head -5 — verify relative cross-references
      6. Check tone: grep for "speculative" or "suggests" or "indicates" — appropriate epistemic language
    Expected Result: 12 sections, header present, relative links, clinical tone
    Evidence: .sisyphus/evidence/task-16-assembly-qa.txt
  ```

---

## Final Verification Wave

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results and get explicit user okay.

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the final `audit/12-NHI-correlation.md` end-to-end. Verify:
  - All "Must Have" items present (methodology, timeline tension front-loaded, adaptation counterargument, falsification, correlation table)
  - All "Must NOT Have" absent (no revision of 01-11, no identity claims, no tone shift)
  - Classification header correct, scope line present
  - All 12 sections present and in correct order
  - Compare deliverables against plan: does the document deliver everything promised?
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Sections [N/12] | VERDICT: APPROVE/REJECT`

- [x] F2. **Cross-Reference Integrity Check** — `unspecified-high`
  - Read `audit/12-NHI-correlation.md`, extract all relative Markdown links
  - Use Glob to verify every target `.md` file exists
  - Check that link paths resolve correctly (relative to `audit/`)
  - Verify INDEX update at `audit/00-INDEX.md` — new entry present, format preserved
  Output: `Cross-references [N verified / N total] | INDEX [PASS/FAIL] | VERDICT: APPROVE/REJECT`

- [x] F3. **Thematic Fidelity Scan** — `deep`
  - Read the document against the original plan at `audit/12-NHI-correlation.plan.md`
  - Verify: the document covers all original plan's intended content (even if reordered/restructured)
  - Check: no scope creep — the document stays within NHI correlation bounds
  - Check: the "agnostic" position on dimensions vs tiers is maintained throughout
  - Check: all 4 identified gaps from the analysis (methodology, timeline, adaptation, falsification) are properly addressed
  Output: `Original plan coverage [N/N] | Scope compliance [CLEAN/ISSUES] | Gaps addressed [4/4] | VERDICT`

- [x] F4. **Source-Footing Verification** — `deep`
  - Read `audit/12-NHI-correlation.md` against the deep sourcing extracts (Tasks 1-3)
  - Verify: all NHI claims attributed to specific sources (Vallée, Keel, Grusch, AARO, Pasulka)
  - Check: no unattributed factual claims about NHI discourse
  - Check: all inline citations match what the source extracts actually contain
  - Check: evidence quality tiers from Methodology section are respected throughout
  Output: `Attributed claims [N/N] | Source match [PASS/FAIL] | Evidence tiers respected [YES/NO] | VERDICT`

---

## Commit Strategy

- **Task 16**: `docs(audit): add 12-NHI-correlation.md — NHI/Archive convergence synthesis` — `audit/12-NHI-correlation.md`
- **Task 15**: `docs(index): add 12-NHI-correlation.md entry to INDEX` — `audit/00-INDEX.md`

---

## Success Criteria

### Verification Commands
```bash
# Check document exists
[ -f audit/12-NHI-correlation.md ] && echo "PASS: Document exists" || echo "FAIL: Missing"

# Check classification header
head -5 audit/12-NHI-correlation.md | grep -q "SPECIES WITH AMNESIA" && echo "PASS: Header" || echo "FAIL: Header missing"

# Count sections (## headings)
grep -c "^## " audit/12-NHI-correlation.md && echo "sections found"

# Check INDEX updated
grep -q "12-nhi-correlation" audit/00-INDEX.md && echo "PASS: INDEX updated" || echo "FAIL: INDEX not updated"

# Verify cross-references resolve
for ref in $(grep -oP '\]\(([^)]+\.md)\)' audit/12-NHI-correlation.md | sed 's/](//;s/)//'); do
  [ -f "audit/$ref" ] && echo "OK: $ref" || echo "BROKEN: $ref"
done
```

### Final Checklist
- [x] `audit/12-NHI-correlation.md` exists with 12 sections
- [x] Classification header and scope line present
- [x] All cross-references resolve to existing files
- [x] Correlation methodology section present (new)
- [x] Timeline tension as Section 3
- [x] "Adaptation to expectation" objection addressed in Section 8
- [x] Disconfirmation criteria section present (new)
- [x] Correlation table with convergence strength ratings
- [x] `audit/00-INDEX.md` updated
- [x] Clinical/forensic tone consistent throughout
- [x] All 4 verification agents approve
