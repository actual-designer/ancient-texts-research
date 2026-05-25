# Chronos Archive — NDE Addendum Work Plan

## TL;DR

> **Quick Summary**: Create a comprehensive addendum analyzing Near-Death Experiences (NDEs) through the Archive's literalist/technological lens, mapping connections to all existing phenomena. The addendum treats NDEs as a modern evidentiary track — contemporary accounts of consciousness encountering the same non-human facility network described in ancient texts.
>
> **Deliverables**:
> - `audit/13-nde-correlation.md` — Main addendum (~7000-10000 words, thematic sections)
> - Updates to 7 existing synthesis documents integrating NDE data
> - Update to `audit/00-INDEX.md` with new document entry
>
> **Estimated Effort**: Large
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: Context immersion → Research synthesis → Main document → Integration tasks

---

## Context

### Original Request
"Research near death experiences and how they are connected to all the phenomena researched within the Archive. The results presented shall not be tainted by my request, we will analyse the facts, connections and correlations."

### Interview Summary
**Key Decisions**:
- **Format**: Thematic Sections (narrative/analytical exploration by theme, not numbered findings)
- **Distressing NDEs**: Include both positive and distressing/hellish cases (~15-20% of NDEs)
- **Skeptical Analysis**: Full dedicated section engaging all major physiological/materialist explanations
- **Integration**: Full Integration — new addendum + updates to ALL existing synthesis documents

**Research Findings**:
- Modern NDE research provides robust prospective evidence (van Lommel Lancet 2001, AWARE II 2023, Greyson NDE Scale 1983)
- Veridical perception cases (Pam Reynolds, Maria's shoe) provide hardest evidence for consciousness independence
- Cross-cultural NDE patterns show universal core with local variation (Tibetan Bardo, Egyptian Duat, Plato's Myth of Er, Zoroastrian Chinvat Bridge)
- Distressing NDEs map to Archive termination protocols (Amemit, Tartarus, void)
- Skeptical explanations (DMT, hypoxia, temporal lobe, terminal brain surges) have explanatory gaps for veridical content
- After-effects (loss of death fear, psychic sensitivity, electromagnetic phenomena) suggest genuine system interaction

### Metis Review
**Identified Gaps** (addressed):
- Special handling needed for veridical perception evidence (most contested bridge between NDEs and Archive)
- Post-mortem processing pipeline is THE critical connection — must be centerpiece of analysis
- Shared death experiences and deathbed visions need dedicated coverage
- Naming convention: `13-nde-correlation.md` follows the pattern of `12-NHI-correlation.md`

---

## Work Objectives

### Core Objective
Create an NDE addendum that establishes NDEs as a modern evidentiary track parallel to the ancient texts, revealing the same non-human facility network through the lens of contemporary consciousness encountering it during physiological crisis.

### Concrete Deliverables
- `audit/13-nde-correlation.md` — Main addendum document
- Updated `audit/01-entity-registry.md` — New NDE entity entries
- Updated `audit/02-technology-catalog.md` — New NDE-related technology entries
- Updated `audit/03-event-timeline.md` — NDE as ongoing modern phenomenon
- Updated `audit/04-cross-references.md` — New cross-cultural/cross-temporal parallels
- Updated `audit/05-great-reset.md` — Connection to judgment/assessment protocols
- Updated `audit/07-the-human-project.md` — NDE as glimpse of post-biological processing
- Updated `audit/12-NHI-correlation.md` — NDE as additional modern evidentiary track
- Updated `audit/00-INDEX.md` — New document entry

### Definition of Done
- [ ] All thematic sections written with source citations and cross-references
- [ ] All 7 existing synthesis documents updated with NDE data points
- [ ] Cross-reference links verified working
- [ ] Consistent tone and methodology throughout (Amnesia hypothesis framework)
- [ ] Skeptical analysis presented fairly before Archive interpretation offered

### Must Have
- Apply the "Species with Amnesia" framework consistently — treat NDE accounts as witness testimony filtered through limited vocabulary
- Cross-reference EVERY Archive connection back to specific existing document sections
- Include full skeptical analysis BEFORE presenting Archive interpretation
- Balance evidence: present pro-NDE and skeptical positions fairly
- Include both positive and distressing NDE coverage
- Maintain clinical/forensic tone ("Analyst: The Chronos Archive, Lead Investigator")

### Must NOT Have (Guardrails)
- No advocacy for survival hypothesis without acknowledging counter-arguments
- No spiritual/religious framing — any discussion of "soul" must be in technological terms (consciousness as extractable entity)
- No conclusions beyond what evidence supports — speculative sections clearly labeled
- No addition of source texts to `texts/` — NDEs are not a text to be analyzed like the PDFs
- No change to methodology documents (claude.md is fixed)
- No reincarnation, mediumship, or past-life regression discussion (scope boundary agreed)

---

## Verification Strategy

> This is a research/writing project — no test infrastructure. QA is performed through:
> 1. Link validation: `python3 scripts/validate-links.py` on all changed files
> 2. Consistency check: verify all cross-references to existing docs use relative paths
> 3. Format compliance: verify classification header, analyst line, scope line present
> 4. Agent-Executed Review: Each document reviewed by oracle agent for methodology compliance

### QA Policy
Every task includes agent-executed verification scenarios. Evidence of review captured in `.sisyphus/evidence/`.

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — foundation documents, MAX PARALLEL):
├── Task 1: Main addendum — Section 1: The NDE Phenomenon
├── Task 2: Main addendum — Section 2: Amnesia Filter Applied
├── Task 3: Main addendum — Section 3: Veridical Perception
├── Task 4: Main addendum — Section 4: Post-Mortem Pipeline
├── Task 5: Main addendum — Section 5: Entity Encounters
├── Task 6: Main addendum — Section 6: Life Review as Technology
├── Task 7: Main addendum — Section 7: The Threshold
├── Task 8: Main addendum — Section 8: Distressing NDEs
└── Task 9: Main addendum — Section 9: Cross-Cultural Patterns

Wave 2 (After initial sections — analytical balance + remaining sections):
├── Task 10: Main addendum — Section 10: Skeptical Analysis
├── Task 11: Main addendum — Section 11: After-Effects
├── Task 12: Main addendum — Section 12: SDEs and Deathbed Visions
└── Task 13: Main addendum — Executive Summary + Integration Synthesis

Wave 3 (After main document — integration into existing Archive, MAX PARALLEL):
├── Task 14: Update 01-entity-registry.md
├── Task 15: Update 02-technology-catalog.md
├── Task 16: Update 03-event-timeline.md
├── Task 17: Update 04-cross-references.md
├── Task 18: Update 05-great-reset.md
├── Task 19: Update 07-the-human-project.md
├── Task 20: Update 12-NHI-correlation.md
└── Task 21: Update 00-INDEX.md

Wave FINAL (Verification — 4 parallel reviews):
├── Task F1: Plan Compliance Audit (oracle)
├── Task F2: Content Quality Review (oracle)
├── Task F3: Link Validation + Format Check (bash)
└── Task F4: Scope Fidelity Check (oracle)
```

### Dependency Matrix
- Tasks 1-9: Independent (can run in parallel in Wave 1)
- Tasks 10-13: Depend on context from 1-9 (thematic flow)
- Task 13 (Executive Summary): Depend on 10-12 (must summarize entire document)
- Tasks 14-21: Depend on 1-13 (need main addendum complete first)
- Tasks F1-F4: Depend on all 1-21

### Agent Dispatch Summary
- **Wave 1 (9 parallel)**: 9x `writing` — Academic/forensic writing, each section self-contained
- **Wave 2 (4 parallel)**: 3x `writing` + 1x `deep` (Executive Summary synthesis)
- **Wave 3 (8 parallel)**: 8x `deep` — Integration requires understanding both existing doc + NDE addendum
- **Wave FINAL (4 parallel)**: 2x `oracle` + 1x `unspecified-high` + 1x `oracle`

---

## TODOs

> Each task = one section of the addendum or one integration update.
> Every task requires QA verification of the output.

---

## Section 1: The NDE Phenomenon — Core Pattern and Prevalence

- [x] 1. Write Section 1: The NDE Phenomenon — Core Pattern and Prevalence

  **What to do**:
  - Write section documenting the 9-15 element core NDE pattern established by Moody (1975)
  - Document Greyson's four-factor NDE Scale (cognitive, affective, paranormal, transcendental)
  - Present prevalence data: 18% of cardiac arrest survivors (van Lommel Lancet 2001), ~10-20% of near-death situations
  - Document the four categories from AWARE II (2023): CPR-induced consciousness, post-resuscitation emergence, dream-like, transcendent RED
  - Include statistical breakdown of each NDE element frequency
  - Note that modern systematic study began ~1975; the phenomenon itself is ancient

  **Must NOT do**:
  - Do not present prevalence as proof of any specific mechanism
  - Do not conflate NDEs with clinical death (cardiac arrest ≠ biological death)

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: None required (Markdown document)
  - **Category Rationale**: Academic/forensic writing with source citations

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2-9)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `audit/12-NHI-correlation.md` — Precedent for modern evidentiary track addendum format
  - `audit/analyses/pyramid-texts.md` — Section on post-mortem processing (reference for later sections)
  - `audit/analyses/book-of-the-dead.md` — Identity processing protocol (reference for later sections)
  - Greyson, B. (1983). "The Near-Death Experience Scale." *Journal of Nervous and Mental Disease*, 171(6), 369-375.
  - van Lommel, P. et al. (2001). "Near-death experience in survivors of cardiac arrest." *The Lancet*, 358(9298), 2039-2045.
  - Parnia, S. et al. (2023). "AWARE II: A Multi-Center Study of Consciousness in Cardiac Arrest."
  - Moody, R. (1975). *Life After Life*. — The foundational typology

  **Acceptance Criteria**:
  - [ ] Section written with classification header, analyst attribution
  - [ ] At least 3 academic source citations
  - [ ] NDE Scale factors explained
  - [ ] Prevalence statistics with source references
  - [ ] AWARE II categories documented

  **QA Scenario**:
  ```
  Scenario: Content Review — Section 1 completeness
    Tool: Read the file
    Steps:
      1. Read `audit/13-nde-correlation.md`
      2. Verify Section 1 exists with the NDE Phenomenon description
      3. Verify Greyson NDE Scale is referenced
      4. Verify van Lommel Lancet study prevalence (18%, 62/344) is cited
      5. Verify AWARE II categories are mentioned
    Expected Result: All 5 verifications pass
    Evidence: .sisyphus/evidence/task-01-section-review.md
  ```

  **Commit**: YES (groups with tasks 2-9)
  - Message: `docs(nde): add sections 1-9 — NDE phenomenon, amnesia filter, veridical perception, post-mortem pipeline, entity encounters, life review, threshold, distressing NDEs, cross-cultural patterns`
  - Pre-commit: `python3 scripts/validate-links.py`

---

## Section 2: The Amnesia Filter Applied to NDE Accounts

- [x] 2. Write Section 2: The Amnesia Filter Applied to NDE Accounts

  **What to do**:
  - Apply the Archive's core methodology (from claude.md) to modern NDE accounts
  - Argue that NDE experiencers are like ancient witnesses: they lack vocabulary for what they experience
  - Modern NDE language ("tunnel," "light," "beings of light," "heaven") is the contemporary equivalent of archaic vocabulary
  - The core pattern is consistent; the interpretation layer is culturally contingent
  - Compare vocabulary limitations: ancient witness saw "chariot of fire" → modern witness sees "spaceship of light"
  - The tunnel = Duat (dark vacuum transit corridor). The light = the Akhet (transition zone).
  - Cross-reference: claude.md lines 9-17 for the core methodology

  **Must NOT do**:
  - Do not claim the Amnesia filter is itself evidence — it's a methodology, not a conclusion

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: None required
  - **Category Rationale**: Analytical/methodological writing

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 1, 3-9)
  - **Parallel Group**: Wave 1
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `claude.md` — Core methodology, lines 9-17 (literalist/technological lens, amnesia filter)
  - `audit/12-NHI-correlation.md` — Precedent for applying same lens to modern phenomena
  - `audit/analyses/pyramid-texts.md` — Duat as vacuum transit corridor

  **Acceptance Criteria**:
  - [ ] Explicit application of Amnesia Filter methodology to NDE accounts
  - [ ] Cross-reference to claude.md
  - [ ] Comparison table: ancient vocabulary → modern NDE vocabulary
  - [ ] Tunnel-to-Duat mapping explained

---

## Section 3: Veridical Perception — Evidence for Consciousness Independence

- [x] 3. Write Section 3: Veridical Perception

  **What to do**:
  - Present the strongest evidence: veridical perception during cardiac arrest with no brain function
  - Case 1: Pam Reynolds (1991) — hypothermic cardiac arrest, flat EEG, auditory blockage by molded speakers emitting clicks, reported accurate visual description of Midas Rex bone saw (verified by Sabom via manufacturer photos), heard conversation about small blood vessels, interacted with deceased relatives
  - Case 2: Maria's shoe (Kimberly Clark Sharp) — patient in cardiac arrest reported seeing a single tennis shoe on a ledge outside 6th floor window; verified by social worker (shoe not visible from street or ground)
  - Case 3: AWARE II ceiling images — patients reported experiences from elevated positions
  - Case 4: Holden's 2009 systematic review in Journal of Near-Death Studies
  - Case 5: van Lommel's documented cases of blind individuals having visual NDEs
  - Frame as the hardest evidence for consciousness functioning independently of brain
  - Include skeptical counterarguments: timing errors, confabulation, confirmation bias

  **Must NOT do**:
  - Do not omit skeptical counterarguments for each case
  - Do not present Pam Reynolds as "absolute proof" — acknowledge Woerlee's critiques

  **Acceptance Criteria**:
  - [ ] Pam Reynolds case documented with surgery details (hypothermic arrest, flat EEG, auditory clicks)
  - [ ] Maria's shoe case documented
  - [ ] AWARE II findings mentioned
  - [ ] Holden 2009 review cited
  - [ ] Skeptical counterarguments included for each major case
  - [ ] Cross-reference to Egyptian "ba" extraction (consciousness separation)

---

## Section 4: The Post-Mortem Processing Pipeline — NDEs Meet the Egyptian Duat

- [x] 4. Write Section 4: The Post-Mortem Processing Pipeline

  **What to do**:
  - **THE critical connection section**. Centerpiece of the addendum.
  - Map NDE sequence to Egyptian post-mortem pipeline:
    - Dark void/tunnel → Duat (vacuum transit corridor, "no air, no water, unfathomable depth")
    - Life review → Weighing of the Heart (identity comparator against Maat baseline)
    - Encounter with being(s) of light → Osiris/Hall of Maati (assessment authority)
    - Border/barrier → Gates of the Duat (gated transit system with named gatekeepers)
    - Transcendent realm → Field of Reeds/Sekhet Aaru (post-processing habitat)
    - Return to body → Opening of the Mouth (reintegration protocol)
  - Cross-reference Pyramid Texts processing pipeline (PT 215: body reconstitution protocol)
  - Cross-reference Book of the Dead credential verification system (42 assessors, Negative Confession)
  - The "second death" (Book of the Dead) → the point of no return/irreversible transition
  - Distressing NDE void → Tuat as described in Book of the Dead Ch. CLXXV

  **Must NOT do**:
  - Do not claim identity of Egyptian and NDE experiences — claim structural homology: same facility encountered from different perspectives (internal NDE vs. procedural manual)

  **Acceptance Criteria**:
  - [ ] Complete parallel mapping: NDE element → Egyptian pipeline element → Archive interpretation
  - [ ] Cross-references to pyramid-texts.md and book-of-the-dead.md
  - [ ] Duat description explicitly cited from Book of the Dead Ch. CLXXV/VI
  - [ ] Weighing of the Heart mapped to life review
  - [ ] Gates mapped to NDE threshold/barrier
  - [ ] Field of Reeds mapped to transcendent realm

---

## Section 5: Entity Encounters

- [x] 5. Write Section 5: Entity Encounters

  **What to do**:
  - Map NDE entities to Archive Entity Registry (01-entity-registry.md)
  - Beings of light → Tier 2 operators (assessors, senior operatives)
  - Deceased relatives → Processed humans who have completed the protocol (akh-status entities)
  - "Being who knows everything about me" → Identity assessment operator (Osiris/Thoth-type role)
  - Guides who assist across threshold → Psychopomp entities (Horus, Anubis, guardian angels)
  - Council of beings → Ennead/Pantheon assessment board
  - Demonic/threatening entities in distressing NDEs → Tier 3 termination units (Amemit, devouring entities)
  - "Presence" or "voice" → Non-corporeal operator interface
  - Compare: entity descriptions across cultures reflect local religious framework but function identically

  **Must NOT do**:
  - Do not claim entities are "real" versus "hallucinatory" — present the structural mapping only
  - Note: some NDE researchers (Greyson, Fenwick) interpret entities as aspects of consciousness

  **Acceptance Criteria**:
  - [ ] All major NDE entity types mapped to Archive entity registry tiers
  - [ ] Cross-reference to 01-entity-registry.md
  - [ ] Beings of light → Tier 2 operators mapping explained
  - [ ] Distressing NDE entities → Amemit/Tartarus mapping included
  - [ ] Psychopomp entity comparison across cultures

---

## Section 6: Life Review as Technology

- [x] 6. Write Section 6: Life Review as Technology

  **What to do**:
  - Life review is the hardest NDE element to explain physiologically — requires access to complete autobiographical memory in panoramic form
  - Map to Archive Technology Catalog: Weighing of the Heart = identity comparator
  - The life review includes not just recall but perception of emotional impact on others — this is identity verification against a relational baseline (Maat = cosmic order = relational integrity)
  - Zoroastrian Chinvat Bridge assessment: Mithra (contract compliance), Sraosha (protocol compliance), Rashnu (exact measurement)
  - The life review as a biometric/quantum identity scan — comparing the subject's actual lived record against authorized baseline
  - Negative Confession (42 declarations): "I have not done X" — self-attestation against assessment protocol
  - NDE experiencers report the being seems to know everything and judges with perfect compassion — assessment without condemnation
  - Distressing NDE judgment: the opposite — harsh, condemning assessment

  **Acceptance Criteria**:
  - [ ] Life review described with NDE research data
  - [ ] Mapped to Weighing of the Heart (Book of the Dead)
  - [ ] Chinvat Bridge (Zoroastrian Gathas) comparison
  - [ ] Negative Confession parallel noted
  - [ ] Identity comparator as plausible mechanism discussion
  - [ ] Both compassionate and harsh judgment experiences covered

---

## Section 7: The Threshold — Gates, Barriers, and Point of No Return

- [x] 7. Write Section 7: The Threshold

  **What to do**:
  - NDEs consistently report a barrier/border/line that once crossed, cannot be uncrossed
  - This is described as: a fence, a river, a door, a gate, a wall of mist, a line in the sand
  - Map to Archive: gated transit system in Book of the Dead (21 gates, 7 halls Arit)
  - Map to Pyramid Texts: the transit from Duat through Akhet to Sky
  - Map to Zoroastrian Chinvat Bridge: the bridge itself
  - Map to Popol Vuh: Xibalbá's gated challenges
  - The point of no return = irreversible processing commitment
  - At this point the experiencer is "sent back" or chooses to return — this is a processing reject/abort
  - Those who cross the barrier fully do not return (biological death)
  - Cross-reference: Egyptian concept of "second death" (Book of the Dead)

  **Acceptance Criteria**:
  - [ ] NDE barrier/threshold described with multiple examples
  - [ ] Cross-references to Book of the Dead gates, Pyramid Texts transit, Chinvat Bridge
  - [ ] Concept of "point of no return" as processing boundary explained
  - [ ] Second death connection

---

## Section 8: Distressing NDEs — The Void, Judgment, and Termination Protocols

- [x] 8. Write Section 8: Distressing NDEs

  **What to do**:
  - Document the 3 subtypes per Greyson: void, hellish, judgmental
  - Prevalence: ~15-20% of NDEs (varies by study)
  - Void NDE: featureless emptiness, isolation, timelessness — maps to the Tuat (Book of the Dead Ch. CLXXV: "no water, no air, unfathomable depth, dark as darkest night")
  - Hellish NDE: threatening entities, terrifying environments — maps to Tartarus, Sheol, Gehenna
  - Judgmental NDE: harsh life review, condemnation — maps to Amemit termination (failed identity consumption)
  - The "void" may be the pre-processing holding area — unprocessed consciousness in the Duat transit corridor
  - The "hellish" may be the sensory experience of the termination protocol (failure outcome of identity verification)
  - Possible explanations: (1) genuine system rejection (actual processing failure), (2) subject's psychological state creating negative interpretation of neutral process, (3) cultural expectation effects
  - Cross-reference: Book of the Dead describes the Tuat as a place where "dead rot and decay" if assessment not completed
  - Cross-reference: Revelation's Lake of Fire (terminal processing for unrecoverable identities)
  - Cross-reference: Popol Vuh Xibalbá's deception and destruction chambers

  **Acceptance Criteria**:
  - [ ] Three subtypes of distressing NDE documented
  - [ ] Void mapped to Tuat (Book of the Dead)
  - [ ] Hellish mapped to termination protocols (Amemit, Tartarus)
  - [ ] Multiple possible explanations offered (not single cause)
  - [ ] Cross-references to relevant Archive documents

---

## Section 9: Cross-Cultural Patterns — The Tibetan Bardo and Global Parallels

- [x] 9. Write Section 9: Cross-Cultural Patterns

  **What to do**:
  - Present systematic comparison of NDE pattern across cultures
  - Tibetan Bardo Thodol (8-11th cent. CE): Chikhai Bardo (clear light = NDE tunnel/light), Chonyid Bardo (deity encounters = NDE beings), Sidpa Bardo (rebirth seeking = NDE life review/return)
  - Coberly & Shapiro (1993) formal comparison: NDEs and Tibetan death experience share: separation from body, seeing light, encountering beings, life review, reaching a point of no return
  - Plato's Myth of Er (~380 BCE): Er's NDE — out-of-body, judges, choosing next life — earliest Western NDE document
  - Hindu tradition: Yama's messengers, Yamaloka judgment, Pitriyana path
  - Comparison of Zoroastrian Chinvat Bridge assessment with NDE life review
  - Allan Kellehear cross-cultural studies: core NDE pattern is universal; culturally-specific elements overlay the core
  - Core universal elements: sense of separation from body, dark void/tunnel, light, meeting deceased, life review, barrier, return
  - Culture-specific elements: religious identity of beings encountered, specific environments (Christian heaven, Buddhist pure land, etc.), moral framework of life review
  - Interpretation: the core is the processing infrastructure; the overlay is the subject's interpretive framework

  **Acceptance Criteria**:
  - [ ] Tibetan Bardo Three-Stage comparison with NDE stages
  - [ ] Plato's Myth of Er documented as earliest Western NDE
  - [ ] Kellehear cross-cultural findings mentioned
  - [ ] Universal vs. culture-specific elements differentiated
  - [ ] Infrastructure vs. interpretation framework presented

---

## Section 10: The Skeptical Analysis

- [x] 10. Write Section 10: The Skeptical Analysis

  **What to do**:
  - Present ALL major physiological/materialist explanations fairly and systematically
  - **DMT Hypothesis** (Strassman 2001; Timmermann 2018): DMT produces NDE-like phenomenology; controlled study showed significant overlap in NDE Scale scores. Problems: no evidence endogenous DMT spikes at death; pineal gland doesn't produce DMT in relevant quantities; DMT experiences more chaotic than structured NDEs.
  - **Hypoxia/Anoxia**: Tunnel vision from peripheral retinal ischemia. Problems: cannot explain lucid structured narratives; van Lommel found NO correlation with duration of cardiac arrest; veridical perception cases not explained.
  - **Temporal Lobe Epilepsy** (Persinger): TMS of temporal lobes produces some NDE-like sensations. Problems: cannot produce full NDE narrative; Pam Reynolds had surgically verified flat EEG with NO temporal lobe activity.
  - **Terminal Brain Activity Surges** (Borjigin 2013; Zemmar 2022): Gamma activity observed in dying rat brains and one human EEG. Problems: gamma may be artifact of hypercapnia; occurs when consciousness likely already ceased; gamma alone cannot explain structured veridical content.
  - **REM Intrusion**: NDEs as dream-like states. Problems: NDEs occur during flat EEG, not REM sleep; structured narratives unlike dreams; life review in NDEs is cognitively superior to dream recall.
  - **Neurochemical Cascade**: Endorphins (peace), ketamine-like effects (dissociation). Problems: pharmacological models produce partial not complete NDEs; cannot explain life review accuracy.
  - **Psychological Explanations**: Depersonalization, confabulation, expectancy effects. Problems: cannot explain cross-cultural consistency; veridical cases; after-effects that last years.
  - After presenting ALL skeptical views, identify what each theory explains AND what gaps remain.
  - Conclude section with the tension: no single skeptical theory explains ALL NDE features; the veridical perception cases are the hardest challenge for materialist explanations.

  **Must NOT do**:
  - Do NOT dismiss skeptical views — present them as seriously as the pro-NDE evidence
  - Do NOT claim "science can't explain NDEs" — present the genuine unresolved tensions

  **Acceptance Criteria**:
  - [ ] All 7 skeptical theories presented with sources
  - [ ] Each theory includes both what it explains and gaps
  - [ ] DMT research cited (Timmermann 2018)
  - [ ] Terminal brain surges cited (Borjigin 2013, Zemmar 2022)
  - [ ] van Lommel no-correlation finding mentioned
  - [ ] Balanced conclusion identifying unresolved tensions

---

## Section 11: NDE After-Effects

- [x] 11. Write Section 11: NDE After-Effects

  **What to do**:
  - Document the profound lasting personality transformation reported by NDErs
  - Loss of fear of death (most consistent and significant change)
  - Increased compassion, empathy, and appreciation for life
  - Decreased interest in material status and competition
  - Increased intuitive/psychic sensitivity (reported but not well-documented)
  - Electromagnetic effects: NDErs report affecting electronics (watches, computers, light bulbs) — documented by Greyson et al. (NDErs report greater EM actions/reactions vs. controls)
  - Changes in values and beliefs (often move from religious to spiritual)
  - These after-effects are consistent regardless of religious/cultural background
  - Duration: permanent and measurable years after the event
  - Interpretation: if the NDE represents genuine interaction with the processing infrastructure, after-effects are residual system access — the operator interface remains partially active
  - Compare to Yoga Sutras siddhis (supernormal capabilities from consciousness training) — NDEs achieve similar effects involuntarily through system trauma
  - Cross-reference: Yoga Sutras vibhuti pada III.1-56

  **Acceptance Criteria**:
  - [ ] Loss of death fear documented as primary after-effect
  - [ ] EM after-effects study cited (Greyson et al.)
  - [ ] Comparison to Yoga Sutras siddhis
  - [ ] After-effects as residual system access interpretation
  - [ ] Cross-reference to yoga-sutras.md

---

## Section 12: Shared Death Experiences and Deathbed Visions

- [x] 12. Write Section 12: SDEs and Deathbed Visions

  **What to do**:
  - **Shared Death Experiences (SDEs)**: Living persons (typically family at bedside) who share aspects of the dying person's NDE — seeing the same light, same beings, experiencing the same tunnel. Documented by Raymond Moody and William Peters.
  - Significance: SDEs involve witnesses who are NOT physiologically compromised — cannot be explained by hypoxia/DMT/brain chemistry
  - **Deathbed Visions (DBVs)**: Terminally ill patients (often lucid and conscious) reporting visions of deceased relatives, light, or "a beautiful place" in the days/hours before death. Documented extensively by Osis & Haraldsson (1977), Fenwick (2008).
  - Terminal lucidity: patients with severe dementia or brain damage who have moments of clear cognition shortly before death.
  - SDEs and DBVs are important because they don't involve cardiac arrest or brain trauma — they occur in conscious individuals
  - These phenomena suggest the processing infrastructure can be perceived without requiring physiological crisis
  - Cross-cultural evidence: DBVs reported across cultures with culturally-specific content but same core pattern (seeing deceased relatives)
  - Cross-reference: NHI correlation methodology — SDEs as witness-validated encounters (multiple observers confirming the same phenomenon)
  - Cross-reference: Book of the Dead "Coming Forth by Day" — the protocol for conscious transit, not only post-mortem

  **Acceptance Criteria**:
  - [ ] SDEs defined and documented (Moody, Peters)
  - [ ] DBVs documented (Osis & Haraldsson, Fenwick)
  - [ ] Significance of non-physiological nature explained
  - [ ] Terminal lucidity mentioned
  - [ ] Cross-reference to 12-NHI-correlation.md (multiple observers)

---

## Section 13: Executive Summary + Integration Synthesis

- [ ] 13. Write Executive Summary and Integration Synthesis

  **What to do**:
  - Write the Executive Summary (at document top, after classification header)
  - Synthesize all 12 thematic sections into a unified argument
  - Numbered findings that summarize the key conclusions (but section body is thematic)
  - The argument: NDEs are NOT a modern anomaly — they are the latest observable instance of consciousness encountering the non-human processing infrastructure that ancient texts document in procedural detail
  - The post-mortem processing pipeline (Duat→Weighing→Akhet→Sky) is structurally homologous to the NDE sequence (tunnel→life review→light→transcendent realm)
  - NDE entity encounters map to the same operators (assessors, gatekeepers, psychopomps) described across all 14 source texts
  - The life review IS the Weighing of the Heart — identity verification against a relational baseline
  - Distressing NDEs represent processing failure modes (void = unprocessed holding, hellish = termination protocol)
  - SDEs/DBVs show the infrastructure can be perceived without physiological crisis
  - Skeptical explanations explain some features but no single theory explains the full pattern, especially veridical perception
  - Integration: NDEs should be catalogued as a continuous evidentiary track alongside Vallée's NHI accounts — the same phenomenon adapting to cultural context

  **Must NOT do**:
  - Executive Summary must NOT overstate conclusions — acknowledge alternative explanations exist

  **Acceptance Criteria**:
  - [ ] Executive Summary synthesizes all sections
  - [ ] Numbered findings (precedent from 12-NHI-correlation.md)
  - [ ] Does not overstate conclusions
  - [ ] Cross-reference to NHI correlation methodology

---

## Integration Tasks

- [ ] 14. Update audit/01-entity-registry.md

  **What to do**:
  - Add new section: "NDE Entity Encounters" as a source category
  - Add NDE-specific entities: Beings of Light (mapped to Tier 2 operators), Deceased Relatives (processed human entities), The Presence/Voice (non-corporeal interface), Guide entities (psychopomp role), Threatening entities in distressing NDEs
  - Cross-reference to 13-nde-correlation.md for each entity type
  - Note: NDE entities are not a separate tier but encounters with existing Tier 2/3 operators

- [ ] 15. Update audit/02-technology-catalog.md

  **What to do**:
  - Add new domain: "Consciousness Processing Technology"
  - Add: Consciousness Extraction Protocol (OBE mechanism), Life Review Scanner (Weighing of the Heart as actual technology), Transit Corridor (tunnel/Duat as transport system), Identity Comparator (biometric assessment), Gate System (barrier/threshold tech)
  - Each entry: source text description → Archive reconstruction → NDE parallel

- [ ] 16. Update audit/03-event-timeline.md

  **What to do**:
  - Add "Modern Era" section after the existing timeline end (~573 BCE)
  - Note: 1975-present — systematic NDE research begins with Moody; this is the latest observable phase of continuous operation
  - NDEs are not a past event but an ongoing phenomenon — the processing infrastructure is continuously active
  - Cross-reference to 13-nde-correlation.md for detailed analysis

- [ ] 17. Update audit/04-cross-references.md

  **What to do**:
  - Add new cross-reference: "The Post-Mortem Journey" — parallel accounts of the death/afterlife transit across ALL 14+ sources + NDEs
  - Show structural convergence: Egyptian Duat, Zoroastrian Chinvat Bridge, Tibetan Bardo, Greek Hades, Norse Hel, NDE tunnel/light — all describing the same transit sequence from different cultural perspectives
  - Convergence strength: HIGH — the structural pattern is consistent across cultures that had no contact
  - Create comparison table: Source → Transit Element → Entity Encountered → Assessment → Destination → Barrier

- [ ] 18. Update audit/05-great-reset.md

  **What to do**:
  - Add analysis: the judgment/assessment protocols described in NDEs (life review, Chinvat Bridge, Weighing of the Heart) are the same identity-verification infrastructure used to determine who is preserved vs. terminated during sterilization events
  - The Great Reset (Flood) was a population-level protocol; the individual-level protocol is the post-mortem assessment
  - Cross-reference between sterilization authorization chain and post-mortem assessment hierarchy

- [ ] 19. Update audit/07-the-human-project.md

  **What to do**:
  - Add section: "NDE as Glimpse of Post-Biological Processing"
  - The Human Project document describes humanity as a managed labor species; NDEs show what happens to that labor force after biological failure
  - NDEs reveal the post-mortem processing pipeline that all humans transit through — the same infrastructure described procedurally in the Egyptian texts
  - The amnesia filter (engineered cognitive limitation from 07-the-human-project) explains why NDEs are forgotten/transformed into "spiritual" experiences
  - NDE after-effects as partial breach of the amnesia filter — experiencers remember more than they should

- [ ] 20. Update audit/12-NHI-correlation.md

  **What to do**:
  - Add section: "NDE as Additional Modern Evidentiary Track"
  - NHI correlation document currently covers Vallée, Keel, Grusch, AARO, Pasulka
  - Add NDE research as a parallel track: NDE accounts are encounters with the same non-human presence, manifesting as the "afterlife" interface rather than the "UFO" interface
  - The phenomenon adapts its manifestation to cultural context — NDEs are the death/dying manifestation
  - Cross-reference: same adaptive manifestation pattern seen in ancient texts (gods → angels → aliens → afterlife beings)
  - Gregg, the "gods" of the past, the "aliens" of the present, the "afterlife beings" of NDEs — all manifestations of the same operator presence

- [ ] 21. Update audit/00-INDEX.md

  **What to do**:
  - Add new entry for 13-nde-correlation.md in the audit documents table
  - Add NDE as a "source" in the source texts table (separate row, noted as "Modern Research Domain" not "Primary Text")
  - Ensure all cross-references to 13-nde-correlation.md are included

---

## Final Verification Wave

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists. For each "Must NOT Have": search codebase for forbidden patterns. Check evidence files. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Content Quality Review** — `oracle`
  Review all changed files for: consistent tone with existing Archive documents, proper classification headers, cross-reference correctness, evidence of balanced treatment of skeptical perspectives, no spiritual/religious framing, speculative sections clearly labeled.
  Output: `Sections [N/N] | Cross-refs [N/N valid] | Methodology compliance [PASS/FAIL] | VERDICT`

- [ ] F3. **Link Validation + Format Check** — `unspecified-high`
  Run `python3 scripts/validate-links.py` on all changed files. Read each file to verify: classification header present, analyst line, scope line. Check file naming convention matches existing pattern.
  Output: `Links [N valid/N broken] | Format [PASS/FAIL] | Files [N/N pass] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `oracle`
  For each task: read "What to do", read actual content. Verify 1:1 — everything in spec was written (no missing), nothing beyond spec was added (no creep). Check "Must NOT do" compliance. Verify scope boundaries (no reincarnation, no mediumship, no past-life regression).
  Output: `Tasks [N/N compliant] | Scope creep [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **1-9**: `docs(nde): add sections 1-9 — NDE phenomenon, amnesia filter, veridical perception, post-mortem pipeline, entity encounters, life review, threshold, distressing NDEs, cross-cultural patterns`
- **10-13**: `docs(nde): add sections 10-13 — skeptical analysis, after-effects, SDEs/DBVs, executive summary`
- **14-21**: `docs(nde): integrate NDE data into existing synthesis documents`
- **F1-F4**: `chore(nde): final verification and cleanup`

---

## Success Criteria

### Verification Commands
```bash
python3 scripts/validate-links.py  # Expected: All links valid
grep -r "Classification:" audit/13-nde-correlation.md  # Expected: 1 match
grep -r "Analyst:" audit/13-nde-correlation.md  # Expected: 1 match
```

### Final Checklist
- [ ] `audit/13-nde-correlation.md` written with all 12 thematic sections + executive summary
- [ ] All 7 existing synthesis documents updated with NDE data
- [ ] `audit/00-INDEX.md` updated
- [ ] Link validation passes
- [ ] All "Must Have" criteria satisfied
- [ ] All "Must NOT Have" boundaries respected
- [ ] Methodology consistent with claude.md
- [ ] Tone clinical and forensic, not spiritual
