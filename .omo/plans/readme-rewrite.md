# README Gateway Rewrite — Chronos Archive

## TL;DR

> **Quick Summary**: Rewrite the existing README.md (70 lines, reference-index style) into a narrative gateway that draws readers into the Chronos Archive's amnesia hypothesis. 8 specific improvements identified in an interview session, from a dedicated "Amnesia Problem" section to a full "Narrative Arc" roadmap and convergence evidence table.
>
> **Deliverables**:
> - Rewritten `README.md` — narrative gateway document with 8 improvements integrated
> - Updated `audit/00-INDEX.md` — synthesis table includes doc 08, summaries aligned to new README tone
> - Updated any other gateway documents that reference the project description (if found during alignment pass)
> - Link validation passes on all changed files
>
> **Estimated Effort**: Short (3-4 focused tasks, single writer track)
> **Parallel Execution**: NO — sequential content track (single document rewrite + alignment + validation)
> **Critical Path**: Research → README rewrite → INDEX alignment → Gateway scan → Validate

---

## Context

### Original Request

The README needs to serve as a "gateway and initial entry to the Chronos Archive. A reader's delight where we establish our premise and our mission, and start building the narrative of what we are discovering and have discovered."

### Interview Summary

**Key Discussions**:
- Identified 8 gaps in current README: Amnesia Problem (buried), Narrative Arc (absent), Convergence Evidence (underplayed), NHI Bridge (missing), Three-Tier Hierarchy (invisible), Reading Paths (absent), Stakes (understated), Call to Action (missing)
- **Scope**: Full alignment pass — README + `audit/00-INDEX.md` + any other gateway docs referencing the project description
- **Content**: Craft new original summaries for the 8-chapter Narrative Arc (not quoted from doc 11)
- **Tone**: "Gateway gets a touch of scope" — slightly more cinematic/atmospheric in Premise, Amnesia, and Narrative Arc sections; clinical/researcher voice in Architecture and reference sections
- **Priority**: All 8 improvements, in one cohesive rewrite

**Metis Findings**:
- The Unified Hypothesis (doc 11) has **8 chapters** (I-VIII), not 7 as initially referenced — chapter count default applied
- `audit/00-INDEX.md` is missing document `08-translation-key.md` from its Cross-Cutting Synthesis table — this will be fixed in the alignment pass
- 267 pre-existing broken links exist in docs 10, 11, and AGENTS.md — these are non-gateway documents and out of scope
- The README currently has zero broken links — new links must match the working relative path pattern (e.g., `audit/01-entity-registry.md`)

---

## Work Objectives

### Core Objective
Transform README.md from a reference index into a narrative gateway that hooks readers, establishes the amnesia lens viscerally, maps the journey ahead, and invites exploration of the full archive.

### Concrete Deliverables
- `README.md` — complete rewrite with all 8 improvements
- `audit/00-INDEX.md` — updated synthesis document table (includes doc 08), updated language alignment
- Any additional gateway docs found during alignment pass — updated for tone/description consistency
- `python3 scripts/validate-links.py` passes on all modified files

### Definition of Done
- [x] `README.md` contains all 8 improvements coherently integrated
- [x] All existing strengths preserved (opening hook, Translation Key, First Doorways table, closing line)
- [x] `audit/00-INDEX.md` synthesis table includes `08-translation-key.md`
- [x] `python3 scripts/validate-links.py` output shows zero new broken links from README changes
- [x] Human review confirms tone consistency (cinematic gateway vs clinical references)
- [x] All links in README follow the existing working pattern `audit/{doc-name}.md`

### Must Have
- New "The Amnesia Problem" section — visceral hook with a worked example of vocabulary gap
- New "Evidence of Convergence" section — geographic/cultural span table showing independent traditions
- New "The Narrative Arc" section — 8-chapter roadmap based on Unified Hypothesis (doc 11)
- New "How to Explore the Archive" section — reading paths for different reader types
- Expanded "The Premise" — stakes presence (managed species, recurring cycles)
- Expanded "The Goal" — open question about whether the cycle is over
- Added modern NHI bridge — brief paragraph/pull-quote linking to doc 12
- Added three-tier hierarchy visual in architecture section
- Added Call to Action after closing line
- `08-translation-key.md` added to 00-INDEX Cross-Cutting Synthesis table
- 00-INDEX language/descriptions updated to align with new README tone

### Must NOT Have (Guardrails)
- No quoting of Unified Hypothesis (doc 11) chapter text directly — craft new summaries
- No fixing pre-existing broken links in non-gateway documents (docs 10, 11, AGENTS.md) — out of scope
- No changes to per-text analysis files (`audit/analyses/*.md`) — not gateway documents
- No changes to source PDFs (`texts/`) — never edited
- No code or configuration changes
- No new files created — all changes are edits to existing files
- No removal of existing strong content (opening hook, Translation Key, First Doorways, closing line)

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: YES (Python link validator)
- **Automated tests**: Tests-after (link validation only)
- **Framework**: `python3 scripts/validate-links.py`
- **Human review**: Final manual quality check of tone, flow, and readability

### QA Policy
Every task includes agent-executed verification. For content changes, verification is:
1. **Read the file** — confirm content is correct, no broken markdown
2. **Run link validator** — `python3 scripts/validate-links.py` — confirm any NEW breakage is explained (links to new sections within README itself, not external)
3. **LSP diagnostics** (for Markdown) — check for broken links, syntax errors

---

## Execution Strategy

### Execution Waves

```
Wave 1 (Sequential — research + content creation):
├── Task 1: Read source syntheses for narrative material [quick]
├── Task 2: Rewrite README.md with all 8 improvements [writing]
└── Task 3: Align 00-INDEX.md + gateway doc scan [writing]

Wave FINAL:
├── Task 4: Link validation + final review [unspecified-high]
```

**Critical Path**: T1 → T2 → T3 → T4
**Max Concurrent**: 1 (sequential content track — single document)

---

## TODOs

- [x] 1. **Source research pass — extract narrative material from synthesis documents**

  **What to do**:
  - Read the following synthesis documents to extract key findings, pull-quotes, and structural elements for the README rewrite:
    - `audit/01-entity-registry.md` — three-tier hierarchy, entity roles, rogue Watcher unit, managed species
    - `audit/02-technology-catalog.md` — bioengineering protocols, Soma, Vimanas, astras (for Translation Key reinforcement)
    - `audit/05-great-reset.md` — Flood as sterilization protocol, authorization chain, Ark as genetic vault (for Amnesia Problem + Stakes)
    - `audit/06-weapons-doctrine.md` — dual-key authorization, escalation pathology, weapons custody (for Stakes + Convergence)
    - `audit/07-the-human-project.md` — Igigi labor revolt, human creation, contamination cycles, operator withdrawal (for Narrative Arc backbone)
    - `audit/08-translation-key.md` — full archaic-to-technical glossary (for Translation Key reinforcement)
    - `audit/09-location-registry.md` — three-tier vertical zones, axis mundi convergence (for Hierarchy visual)
    - `audit/11-unified-hypothesis.md` — 8-chapter structure, executive summary findings, falsifiability criteria (for Narrative Arc)
    - `audit/12-NHI-correlation.md` — NHI continuity with ancient patterns, Vallée/Keel/Grusch references (for NHI bridge)
  - Extract 3-5 key pull-quotes per document suitable for README hooks
  - Map the 8-chapter structure from doc 11 for the Narrative Arc section
  - Compile the "Convergence Table" data: which traditions describe which structural elements (three-tier hierarchy, bioengineering, flood/reset, post-mortem processing, weapons doctrine)
  - Note: this task is RESEARCH ONLY — no files are modified. Output is a research memo in the agent's response for the next task.

  **Must NOT do**:
  - Do not modify any files in this task
  - Do not pre-write README content — leave that for Task 2
  - Do not spend time on non-gateway documents (per-text analyses in `audit/analyses/`)

  **Recommended Agent Profile**:
  - **Category**: `writing` — this is research synthesis and content extraction
    - Reason: Document analysis and content extraction for narrative writing
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**: All — this is pure reading/extraction, no specialized skills needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (standalone research)
  - **Blocks**: Task 2
  - **Blocked By**: None

  **References**:
  - `audit/01-entity-registry.md` — Entity hierarchy (three tiers, managed species, Watchers)
  - `audit/02-technology-catalog.md` — Bioprinting, directed-energy, consciousness upload technology entries
  - `audit/05-great-reset.md` — Flood authorization chain (Anu/Enlil/Ea), Ark as seed vault analysis
  - `audit/06-weapons-doctrine.md` — Dual-key custody, tiered authorization, escalation arc
  - `audit/07-the-human-project.md` — Complete arc from labor revolt → bioengineering → contamination → reset → withdrawal
  - `audit/08-translation-key.md` — Full archaic→technical glossary
  - `audit/09-location-registry.md` — Three-tier vertical structure, axis mundi locations
  - `audit/11-unified-hypothesis.md` — 8-chapter structure, executive summary, falsifiability
  - `audit/12-NHI-correlation.md` — NHI continuity argument, Vallée/Keel/Grusch references

  **WHY Each Reference Matters**:
  - The executor has ZERO context from the planning interview. These documents contain the specific findings, pull-quotes, and structural data needed to write informed README content. Each must be read for narrative material.

  **Acceptance Criteria**:
  - [x] All 9 synthesis documents read and extracted
  - [x] Key pull-quotes identified per document
  - [x] 8-chapter narrative arc mapped from doc 11
  - [x] Convergence data compiled: which traditions share which structural elements
  - [x] Research memo output provided for Task 2

  **QA Scenarios**:
  ```
  Scenario: Research output completeness
    Tool: Bash — output listing of key findings
    Steps:
      1. Verify the agent's response contains extraction notes for each of the 9 documents
      2. Confirm the 8-chapter arc from doc 11 is mapped
      3. Confirm convergence table data is compiled
    Expected Result: All 9 documents extracted, arc mapped, convergence data compiled
    Evidence: .sisyphus/evidence/readme-rewrite-task1-research.txt
  ```

  **Commit**: NO (research task — no files changed)

---

- [x] 2. **Rewrite README.md with all 8 improvements**

  **What to do**:
  Rewrite `README.md` to incorporate all 8 identified improvements while preserving everything that works. The target structure:

  ```
  1. Title + Classification header              [PRESERVE — line 1-4]
  2. The Premise                                 [EXPAND — add stakes, managed species frame]
  3. The Amnesia Problem                         [NEW — visceral hook with vocabulary-gap example]
  4. Evidence of Convergence                     [NEW — geographic table of independent traditions]
  5. Translation Key                             [PRESERVE — lines 18-23, expand with 2-3 more entries from doc 08]
  6. The Narrative Arc: 8 Chapters               [NEW — chapter-by-chapter roadmap with links]
  7. How to Explore the Archive                  [NEW — reading paths for different reader types]
  8. Project Architecture                        [EXPAND — add three-tier hierarchy visual]
  9. First Doorways                              [PRESERVE — lines 54-63, update if needed]
  10. The Goal                                   [EXPAND — stakes, open question]
  11. Closing + Call to Action                   [EXPAND — add "Dive in" / "Join the investigation"]
  ```

  **Content guidelines for each section**:

  **Section 2 — The Premise (EXPAND)**:
  - Keep the existing opening 3 paragraphs (they're strong)
  - Add 1-2 paragraphs expanding the stakes: "If the texts are right, we are a managed species. The question isn't whether these events happened — it's whether the cycle is over or just between intervals."
  - Reference the convergence: mention that this pattern appears across Mesopotamian, Indian, Mesoamerican, Egyptian, Norse, Greek, and Zoroastrian traditions.

  **Section 3 — The Amnesia Problem (NEW)**:
  - This is the visceral hook. Lead with the question: "What would you see if you lacked the vocabulary to describe it?"
  - Worked example: "Show a smartphone to a witness from 3000 BCE. They see a glowing rectangle that captures images, speaks, and reveals distant places. They call it a 'spirit mirror' or 'oracle stone.' They're not wrong — they're accurate. They just lack the words 'OLED display,' 'camera sensor,' and 'cellular network.'"
  - Bridge to the Archive: "Now apply that same vocabulary gap to every 'miracle,' 'vision,' and 'divine encounter' in the historical record. The description is not the delusion. The vocabulary is the limitation."
  - Keep clinical/cool in tone, not ranting. The power is in the logic, not the rhetoric.

  **Section 4 — Evidence of Convergence (NEW)**:
  - Create a table showing the geographic and cultural span of traditions:
    | Region | Tradition | Key Sources | Isolation Status |
    |--------|-----------|-------------|------------------|
    | Mesopotamia | Sumerian/Akkadian | Atrahasis, Gilgamesh | — |
    | Levant | Hebrew/Enochic | Enoch, Ezekiel | Partial overlap with Mesopotamia |
    | India | Vedic/Epic | Rig Veda, Mahābhārata | Independent from West |
    | Egypt | Nilotic | Pyramid Texts, Book of Dead | Independent |
    | Mesoamerica | Maya/Quiché | Popol Vuh | Independent from ALL above |
    | Scandinavia | Norse | Poetic Edda | Independent from Mesoamerica, India |
    | Greece | Hellenic | Theogony, Works and Days | Independent from Mesoamerica |
    | Persia | Zoroastrian | Gathas | Independent from Mesoamerica, Scandinavia |
  - Below the table: "If these were independent mythologies, how do they describe the same three-tier hierarchy, the same bioengineering origin for humanity, the same catastrophic flood as a deliberate sterilization, the same weapons custody protocols? Either they all tapped into a shared delusion — or they all witnessed the same operational reality through different cultural lenses."

  **Section 5 — Translation Key (EXPAND)**:
  - Preserve the existing entries (glory→plasma, angels→entities, heaven→orbital, miracles→physics)
  - Add 2-3 more entries drawn from `audit/08-translation-key.md`:
    - `Merkabah / Chariot of Fire` → VTOL aerospace vehicle with omnidirectional propulsion
    - `Soma / Ambrosia / Amrita` → Controlled cognitive-enhancement compound (source: doc 08)
    - `Weighing of the Heart` → Identity verification / biometric assessment (source: doc 08)
  - Format preserves the arrow notation for scannability

  **Section 6 — The Narrative Arc (NEW)**:
  - Frame as "The Sequence of Events" or "The Forgotten History in 8 Chapters"
  - Each chapter gets: chapter title, 1-2 sentence original summary, link to relevant document
  - Based on the 8 chapters from `audit/11-unified-hypothesis.md`:
    
    1. **The Operators** — A stratified non-human organization deployed on Earth before humanity, with orbital command nodes, surface operations, and subsurface facilities. They had departments, chains of command, and a labor force that eventually revolted. → [`01-entity-registry.md`](audit/01-entity-registry.md)
    
    2. **The Human Project** — Humanity was bioengineered as a replacement labor species. The project evolved: iterative R&D across cultures, precision genetic commissions, hybrid rulers, and a post-mortem integration pipeline that suggests the scope expanded far beyond the original mandate. → [`07-the-human-project.md`](audit/07-the-human-project.md)
    
    3. **The Contamination Cycles** — Every era follows the same pattern: humanity exceeds parameters → contamination escalates → a reset is authorized. The failure is structural, not accidental — built into the management model. → [`04-cross-references.md`](audit/04-cross-references.md)
    
    4. **The Great Reset** — The Flood was not divine punishment or natural disaster. It was a deliberate multi-vector sterilization protocol, authorized at the highest level, preceded by a covert genetic preservation operation by a dissenting scientist. → [`05-great-reset.md`](audit/05-great-reset.md)
    
    5. **The Withdrawal** — After the reset, the operators progressively withdrew from direct management. By Ezekiel's era (593 BCE, the last precisely dated contact), the command structure was issuing termination-of-engagement protocols. → [`03-event-timeline.md`](audit/03-event-timeline.md)
    
    6. **The Integration Protocol** — The texts describe a post-mortem processing pipeline (Egyptian Duat → Akhet → Sky) that suggests human consciousness was designed for integration into a larger infrastructure. The "afterlife" is a technological system. → [`analyses/pyramid-texts.md`](audit/analyses/pyramid-texts.md)
    
    7. **The Current State** — We are in the autonomous test phase: a managed species operating without active oversight, with engineered amnesia, repeating the same patterns that triggered previous resets. The question is whether the cycle is truly broken — or merely between intervals. → [`11-unified-hypothesis.md`](audit/11-unified-hypothesis.md)
    
    8. **The Return Path** — The projected terminal sequence (Revelation) describes a final sterilization, biometric registration of survivors, and a replacement habitat. Whether this is prophecy, contingency plan, or scheduled maintenance is the Archive's central open question. → [`analyses/revelation.md`](audit/analyses/revelation.md)
  
  - Each chapter should be 2-4 sentences, punchy, with a clear link to dig deeper

  **Section 7 — How to Explore the Archive (NEW)**:
  - Reading paths for different reader types:
    - **"I have 5 minutes"**: README → Translation Key → pick one First Doorway entry
    - **"I want the big picture"**: Unified Hypothesis → The Human Project → Event Timeline
    - **"I want the scariest finding"**: Weapons Doctrine → Great Reset
    - **"I want to verify the methodology"**: Pick a text you know → Read its forensic analysis → Check cross-references
    - **"I'm writing sci-fi and need inspiration"**: Technology Catalog → Entity Registry → Location Registry
    - **"Connect this to modern UFO/UAP"**: NHI Correlation → Unified Hypothesis → Weapons Doctrine

  **Section 8 — Project Architecture (EXPAND)**:
  - Preserve existing structure (Evidence Locker + Cross-Cutting Syntheses)
  - Add a three-tier hierarchy visual in the architecture section. Use ASCII art:

    ```
    ORBITAL TIER (Command)
      └── Heaven of Anu / Seventh Heaven / Throne Room
          └── Council / Assembly of the Gods
    
    SURFACE TIER (Operations)
      ├── Enlil — Ground Command / Storm Operations
      ├── Enki — Subsurface R&D / Bioengineering
      ├── Nintu — Genetic Fabrication
      ├── Weapons custody — Authorized deployment
      └── Human settlements — Managed zones
    
    SUBSURFACE TIER (Restricted)
      ├── Apsu / Abzu — Enki's domain
      ├── Xibalbá — Trial facility
      ├── Duat — Post-mortem processing
      ├── Tartarus / Prison of Stars — Detention
      └── The Abyss — Terminal containment
    ```

  **Section 10 — The Goal (EXPAND)**:
  - Keep existing sentence as lead
  - Add: "The question isn't whether these events happened. The question is whether the cycle is over — or just between intervals."
  - Add: "We are not evolving. We are remembering. And the Archive's findings suggest the amnesia may not be permanent."

  **Section 11 — Closing + Call to Action (EXPAND)**:
  - Preserve "Stop praying. Start calculating." exactly
  - Add below, in a new line or two:
    > **Dive in**: [`audit/00-INDEX.md`](audit/00-INDEX.md) — the master map.
    > **Pick a thread** from the First Doorways table above.
    > **Join the investigation**: The Archive is open-source. Read. Question. Verify. Reconstruct.

  **Tone guide**:
  - Sections 2, 3, 6, 10, 11: "Gateway gets a touch of scope" — slightly more atmospheric, cinematic, gripping prose. Use rhetorical questions, evocative imagery, implication-laden statements.
  - Sections 4, 5, 7, 8, 9: Clinical, researcher voice. Plain descriptions, factual presentation, tables for data.
  - The shift should feel natural — the reader is being drawn in (cinematic) and then handed tools (clinical).

  **Must NOT do**:
  - Do NOT delete the existing opening hook "Humanity isn't evolving; it's remembering" — preserve as lead line
  - Do NOT delete the Translation Key arrow-notation format
  - Do NOT delete the First Doorways table
  - Do NOT delete the closing line "Stop praying. Start calculating."
  - Do NOT quote directly from doc 11's chapter text — write original summaries
  - Do NOT add emojis unless present in original
  - Do NOT use HTML or raw LaTeX — stick to Markdown

  **Recommended Agent Profile**:
  - **Category**: `writing` — content rewrite, narrative document creation
    - Reason: This is a prose-heavy content rewrite requiring narrative construction, tone management, and structured documentation
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**: All — pure Markdown content writing, no specialized skills needed

  **Parallelization**:
  - **Can Run In Parallel**: NO (depends on Task 1 research output)
  - **Parallel Group**: Sequential (Wave 1)
  - **Blocks**: Task 3
  - **Blocked By**: Task 1

  **References**:
  - `README.md` (current) — the file being rewritten; preserve its strengths
  - `audit/01-entity-registry.md` — Three-tier hierarchy, entity names/roles for the visual and convergence table
  - `audit/02-technology-catalog.md` — Technology entries for Translation Key expansion
  - `audit/05-great-reset.md` — Flood as sterilization, Ark as vault for Amnesia Problem
  - `audit/06-weapons-doctrine.md` — Dual-key authorization for stakes/convergence
  - `audit/07-the-human-project.md` — Full arc from labor to withdrawal for Narrative Arc
  - `audit/08-translation-key.md` — Full glossary for Translation Key expansion entries
  - `audit/09-location-registry.md` — Three-tier zones, axis mundi for hierarchy visual
  - `audit/11-unified-hypothesis.md` — 8-chapter structure, executive summary for Narrative Arc
  - `audit/12-NHI-correlation.md` — NHI bridge content for Premise/Goal
  - `audit/00-INDEX.md` — Current INDEX structure for alignment reference
  - Task 1 research memo — the extracted findings, pull-quotes, and compiled data

  **Acceptance Criteria**:
  - [x] README.md rewritten with all 8 improvements integrated
  - [x] All existing strengths preserved (opening hook, Translation Key, First Doorways, closing line)
  - [x] The Amnesia Problem section contains a worked vocabulary-gap example
  - [x] Evidence of Convergence section has a geographic table of independent traditions
  - [x] The Narrative Arc has 8 chapters with original summaries and document links
  - [x] How to Explore section has 6 reading paths
  - [x] Architecture section includes three-tier hierarchy visual
  - [x] Translation Key expanded with 2-3 new entries from doc 08
  - [x] The Goal section expanded with stakes/open question
  - [x] Call to Action added after closing line
  - [x] NHI bridge present (paragraph or pull-quote)
  - [x] Tone matches: cinematic in gateway sections, clinical in reference sections
  - [x] All links follow `audit/{doc-name}.md` pattern (no `../` prefix)

  **QA Scenarios**:
  ```
  Scenario: Content completeness — all 8 improvements present
    Tool: Bash — grep content markers
    Steps:
      1. grep "Amnesia Problem" README.md — confirm section exists
      2. grep "Evidence of Convergence" README.md — confirm section exists
      3. grep "The Narrative Arc" README.md — confirm section exists
      4. grep "How to Explore" README.md — confirm section exists
      5. grep "ORBITAL TIER" README.md — confirm hierarchy visual present
      6. grep "Stop praying" README.md — confirm closing line preserved
      7. grep "Dive in" README.md — confirm call to action present
      8. grep "NHI" README.md — confirm NHI bridge present
    Expected Result: All 8 patterns found
    Evidence: .sisyphus/evidence/readme-rewrite-task2-content-check.txt

  Scenario: Link pattern validation — no broken ../ links
    Tool: Bash — grep for relative links
    Steps:
      1. grep -c "\.\./" README.md — should be 0 (all links use audit/ prefix)
    Expected Result: 0 instances of ../ in links
    Evidence: .sisyphus/evidence/readme-rewrite-task2-links.txt

  Scenario: Original content preserved
    Tool: Bash — grep for preserved phrases
    Steps:
      1. grep "Humanity isn't evolving" README.md — preserved
      2. grep "Glory/Radiance" README.md — preserved in Translation Key
      3. grep "First Doorways" README.md — preserved
      4. grep "Start calculating" README.md — preserved at end
    Expected Result: All 4 preserved
    Evidence: .sisyphus/evidence/readme-rewrite-task2-preserved.txt
  ```

  **Evidence to Capture**:
  - [x] `.sisyphus/evidence/readme-rewrite-task2-content-check.txt`
  - [x] `.sisyphus/evidence/readme-rewrite-task2-links.txt`
  - [x] `.sisyphus/evidence/readme-rewrite-task2-preserved.txt`

  **Commit**: YES — single commit for README rewrite
  - Message: `docs(readme): rewrite as narrative gateway with 8 improvements`
  - Files: `README.md`
  - Pre-commit: None

---

- [x] 3. **Align 00-INDEX.md and scan other gateway documents**

  **What to do**:
  A. **Update `audit/00-INDEX.md`**:
    - Add missing `08-translation-key.md` entry to the Cross-Cutting Synthesis table (section marked by `### Cross-Cutting Synthesis`, lines 51-66)
    - Place it in correct numerical order: after `07-the-human-project.md` (line 61) and before `11-unified-hypothesis.md` (line 62)
    - Entry format (matching existing style):
      ```
      | [08-translation-key.md](08-translation-key.md) | Terminology glossary: archaic vocabulary to technical equivalents across all sources |
      ```
    - Update the "Scope" line at the top of the document (line 4: `**Scope:** All fourteen foundational texts`) to reflect the current count if needed
    - Review the Source Texts table (lines 11-28) — ensure the count and entries match the actual `audit/analyses/` directory (14 source analyses)
    - Review the Per-Text Deep Dives table (lines 34-50) — ensure all 14 analyses are listed and descriptions are consistent with new README tone
    - Ensure the Guiding Principles section (lines 78+) aligns with language from the new README's Amnesia Problem section where they overlap
    - No major structural changes — 00-INDEX should remain a reference index, not become narrative

  B. **Scan other gateway documents**:
    - Read `audit/10-correlation-map.md` and `audit/11-unified-hypothesis.md` — these are synthesis docs that reference the Archive's scope in their headers
    - Check if their description/scope lines reference "14 foundational texts" and update if the count has changed
    - Also read `audit/analyses/AGENTS.md` — it's in the analyses folder but may reference project description
    - NOTE: Only update description/scope lines — do not rewrite these documents. The 8-chapter arc and other new README content stays in README.

  **Must NOT do**:
  - Do NOT restructure 00-INDEX significantly — it's a reference index, not narrative
  - Do NOT fix pre-existing broken links in docs 10, 11, or AGENTS.md — out of scope
  - Do NOT rewrite per-text analysis files
  - Do NOT change source PDFs
  - Do NOT modify the README in this task

  **Recommended Agent Profile**:
  - **Category**: `writing` — document alignment, table editing, descriptive text updates
    - Reason: Editing existing Markdown documents for consistency and completeness
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: NO (depends on Task 2 completing so we know the README's final form)
  - **Parallel Group**: Sequential (Wave 2)
  - **Blocks**: Task 4
  - **Blocked By**: Task 2

  **References**:
  - `audit/00-INDEX.md` — the file being updated
  - `audit/08-translation-key.md` — verify the file exists and has correct path
  - `audit/10-correlation-map.md` — check for out-of-date scope/description references
  - `audit/11-unified-hypothesis.md` — check for out-of-date scope/description references
  - `audit/analyses/AGENTS.md` — check for out-of-date references
  - Updated `README.md` (from Task 2) — reference for tone/language alignment

  **Acceptance Criteria**:
  - [x] `08-translation-key.md` added to 00-INDEX Cross-Cutting Synthesis table in correct position
  - [x] 00-INDEX Source Texts table accurate (14 entries)
  - [x] 00-INDEX Per-Text Deep Dives table complete (14 entries)
  - [x] 00-INDEX Guiding Principles aligned with README's Amnesia Problem language
  - [x] Any other gateway docs with stale scope references updated
  - [x] No changes to non-gateway documents
  - [x] All links in 00-INDEX follow the same relative pattern (no `../`)

  **QA Scenarios**:
  ```
  Scenario: Doc 08 present in 00-INDEX synthesis table
    Tool: Bash — grep for 08-translation-key in 00-INDEX.md
    Steps:
      1. grep "08-translation-key" audit/00-INDEX.md
    Expected Result: Entry found in Cross-Cutting Synthesis section
    Evidence: .sisyphus/evidence/readme-rewrite-task3-index-08.txt

  Scenario: Gateway docs scanned
    Tool: Bash — verify no unintended changes
    Steps:
      1. git diff --name-only audit/10-correlation-map.md — expect no changes OR minimal scope line updates
      2. git diff --name-only audit/11-unified-hypothesis.md — same
      3. git diff --name-only audit/analyses/AGENTS.md — same
    Expected Result: Only intended files changed
    Evidence: .sisyphus/evidence/readme-rewrite-task3-gateway-scan.txt
  ```

  **Evidence to Capture**:
  - [x] `.sisyphus/evidence/readme-rewrite-task3-index-08.txt`
  - [x] `.sisyphus/evidence/readme-rewrite-task3-gateway-scan.txt`

  **Commit**: YES — group with Task 2 or separate
  - Message: `docs(index): add 08-translation-key to synthesis table, align gateway docs`
  - Files: `audit/00-INDEX.md`, plus any updated gateway docs
  - Pre-commit: None

---

## Final Verification Wave

- [x] F1. **Link validation + final quality review**

  **What to do**:
  **A. Validate all links**:
  - Run `python3 scripts/validate-links.py`
  - Capture the output
  - The README should have zero broken links. If any new broken links are introduced:
    - Identify the link
    - Check if it's a link to a section within the README itself (anchor links like `#the-premise`) — these are fine and the validator may flag them
    - If it's a broken external link, fix it
    - Re-run the validator until clean

  **B. Final quality check**:
  - Read the rewritten README.md end-to-end
  - Check for:
    - Tone consistency (cinematic in gateway sections, clinical in reference sections)
    - No duplicate content
    - All 8 improvements visible and coherent
    - Opening hook preserved at the very top of the document body
    - Translation Key arrows → format preserved
    - First Doorways table intact with all entries
    - Closing line "Stop praying. Start calculating." present
    - Call to action present below closing line
    - NHI bridge present
    - All links use `audit/{doc-name}.md` format (no `../` relative paths)

  **C. Create evidence summary**:
  - Save the validator output to evidence
  - Note any pre-existing broken links (in non-gateway docs) that are not the task's responsibility

  **Must NOT do**:
  - Do not fix pre-existing broken links in non-gateway documents
  - Do not make additional content changes to README — this is verification only
  - Do not change the closing line or opening hook

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` — verification and quality check
    - Reason: Multi-step validation combining script execution, file reading, and manual quality review
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: NO (depends on all prior tasks)
  - **Parallel Group**: Final
  - **Blocks**: Nothing — this is the last step
  - **Blocked By**: Task 3

  **References**:
  - `scripts/validate-links.py` — the link validator script
  - Updated `README.md` — the file being verified
  - Updated `audit/00-INDEX.md` — the file being verified
  - Any other changed gateway docs

  **Acceptance Criteria**:
  - [x] `python3 scripts/validate-links.py` shows zero NEW broken links from README/INDEX changes
  - [x] README.md reads coherently end-to-end
  - [x] All 8 improvements present and integrated
  - [x] Opening hook, Translation Key, First Doorways, closing line all preserved
  - [x] Evidence captured to `.sisyphus/evidence/`

  **QA Scenarios**:
  ```
  Scenario: Link validation clean
    Tool: Bash — run python3 scripts/validate-links.py
    Steps:
      1. python3 scripts/validate-links.py 2>&1
      2. Check for any broken link errors that reference README.md or audit/00-INDEX.md
    Expected Result: Zero broken links in README.md and audit/00-INDEX.md
    Failure Indicators: Any line saying "BROKEN" or "ERROR" for README.md or audit/00-INDEX.md links
    Evidence: .sisyphus/evidence/readme-rewrite-final-link-validation.txt

  Scenario: End-to-end reading quality
    Tool: Read — read the final README.md
    Steps:
      1. Read README.md from start to finish
      2. Verify narrative flow: Premise → Amnesia → Convergence → Translation Key → Arc → How To → Architecture → First Doorways → Goal → Closing
      3. Verify no broken markdown rendering
    Expected Result: Coherent flow, no broken formatting
    Evidence: (manual review - note in output)
  ```

  **Evidence to Capture**:
  - [x] `.sisyphus/evidence/readme-rewrite-final-link-validation.txt`
  - [x] `.sisyphus/evidence/readme-rewrite-final-reading-review.txt`

  **Commit**: NO (verification only, no file changes)

---

## Commit Strategy

- **Task 2**: `docs(readme): rewrite as narrative gateway with 8 improvements` — `README.md`
- **Task 3**: `docs(index): add 08-translation-key to synthesis table, align gateway docs` — `audit/00-INDEX.md` plus any updated gateway docs

---

## Success Criteria

### Verification Commands
```bash
python3 scripts/validate-links.py  # Expected: zero broken links in README.md and audit/00-INDEX.md
grep "The Amnesia Problem" README.md  # Expected: section exists
grep "Evidence of Convergence" README.md  # Expected: section exists
grep "The Narrative Arc" README.md  # Expected: section exists
grep "How to Explore" README.md  # Expected: section exists
grep "ORBITAL TIER" README.md  # Expected: hierarchy visual present
grep "Stop praying" README.md  # Expected: closing line preserved
grep "08-translation-key" audit/00-INDEX.md  # Expected: entry present in synthesis table
```

### Final Checklist
- [x] All "Must Have" content present in README
- [x] All "Must NOT Have" guardrails respected
- [x] Link validation passes (no NEW broken links)
- [x] Original strengths preserved (hook, translation key, first doorways, closing line)
- [x] 00-INDEX synthesis table includes doc 08
- [x] Tone matches: cinematic gateway vs clinical reference
