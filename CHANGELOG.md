# Changelog

All notable changes to The Chronos Archive are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.11.1] — 2026-06-19

### Fixed

- **Lifecycle State Diagram syntax error** (`audit/07-the-human-project.md`) — The Human Project state diagram failed to render with Mermaid v11's "Syntax error in text" overlay. Root cause: HTML entities (`R&amp;D`) in the diagram source and inline `note` lines with embedded colons and `<br/>` tags that the v11 parser rejects. Fixed by renaming the state id to `RD`, converting notes to block `note … end note` format, and simplifying state labels.
- **Mermaid HTML entity normalization** (`src/components/Mermaid.astro`) — Added `normalizeMermaidSource()` to decode HTML entities (e.g. `&amp;` → `&`) from Shiki code-block `textContent` before passing source to `mermaid.run()`, preventing similar parse failures in other diagrams.

---

## [0.11.0] — 2026-06-19

A structural UI/UX redesign ("declassified forensic dossier") plus a complete rebuild of the Mermaid pipeline.

### Added

- **Bundled, theme-aware Mermaid** (`src/components/Mermaid.astro`) — Mermaid is now an npm dependency (`mermaid@^11`) bundled by Astro and **lazy-loaded via dynamic `import()`** (diagram-free pages stay light; it is code-split into its own chunk). The runtime resiliently selects diagram blocks (`pre[data-language="mermaid"]` with Prism/legacy fallbacks), renders with `startOnLoad: false` + `mermaid.run()`, and **re-renders on theme toggle** via a `MutationObserver` on `data-theme` so diagrams recolor live. Diagrams sit in a horizontally-scrollable `.mermaid-figure`.
- **Global content stylesheet** (`src/styles/global.css`) — Base reset + content typography moved here so it reliably styles Markdown injected via `set:html` (previously these rules were component-scoped and never reached the content). Includes manuscript blockquotes, themed code blocks, sticky-header/scroll-shadow tables, heading-anchor styles, a `.callout` utility, and the Mermaid container.
- **Top bar** (`src/components/TopBar.astro`) — Mobile slim header with hamburger, wordmark, and theme toggle, so theme switching is reachable without opening the drawer.
- **Table of contents** (`src/components/TableOfContents.astro`) — Right-rail TOC built from h2/h3 headings, sticky at ≥1200px, with IntersectionObserver scrollspy. Heading anchor links injected during post-processing.
- **Skip-to-content link** and a single `<main>` landmark.
- **Shiki dual-theme code blocks** — `astro.config.mjs` now emits `github-light`/`github-dark` as CSS variables (`defaultColor: false`); code blocks follow the site theme instead of always rendering dark.

### Changed

- **`theme.css`** — Refined dark/light palettes (improved contrast), added `color-scheme`, focus `--ring`, layout tokens (`--topbar-height`, `--toc-width`, `--content-max-width`), a global `:focus-visible` ring, and a `prefers-reduced-motion` block. Render-blocking Google Fonts `@import` replaced with non-blocking `<link rel="preconnect/stylesheet">` (with `display=swap`) in the layout head.
- **`BaseLayout.astro`** — Reworked into a 3-zone responsive shell: sidebar + centered reading column (≈72ch) + optional sticky TOC rail. Single `<meta name="theme-color">` now follows the manual toggle. Removed the Mermaid CDN `<script>` and inline init.
- **`Sidebar.astro`** — Cleaner grouping with a new **Field Notes** group; nav now lists every built page (added `14 — Celestial Events`, `Control Baseline`, `Broadsheet Methodology`). Refined active state and mobile drawer.
- **`ThemeToggle.astro`** — Binds all toggle instances, syncs the `theme-color` meta, sets `aria-pressed`, and respects reduced motion.
- **`index.astro`** — Hero gains CTAs ("Enter the Archive" / "Read the Hypothesis"); Key Syntheses table wrapped for responsive scroll.
- **Content post-processor** (`src/utils/rewrite-html-links.mjs`) — Added `extractHeadings()` (TOC source) and `enhanceContentHtml()` (wrap tables, append heading anchors).

### Fixed

- **Mermaid diagrams now render reliably** — The previous CDN + `DOMContentLoaded` approach was replaced entirely; flowcharts, state diagrams, and the gantt all render and recolor with the theme. *(Note: the deep-time gantt in `03-event-timeline` renders but is visually compressed because its axis spans ~12,000 years with year-granularity dates — a data characteristic, not a pipeline issue.)*
- **Nested `<main>`** removed from `404.astro` (it now sits inside BaseLayout's single `<main>`).
- **Markdown content was previously unstyled** for most block elements (component-scoped rules didn't apply to `set:html` output); content typography now applies correctly.

---

## [0.10.1] — 2026-06-19

### Fixed

- **Mermaid diagram rendering** — Replaced the fragile `defer` + `onload` initialization pattern with a consolidated `DOMContentLoaded` handler. The transform (Shiki `<pre>` → raw `<pre class="mermaid">`) and `mermaid.initialize()` now both run inside a single `DOMContentLoaded` listener, guaranteeing that all deferred scripts (including the Mermaid CDN) have fully executed before the DOM is scanned for `.mermaid` elements. This eliminates the timing gap where the synchronous transform script at end of body would run before the deferred Mermaid library had loaded.

---

## [0.10.0] — 2026-06-19

### Added

- **Design token system** (`src/styles/theme.css`) — Centralized CSS custom properties for light/dark theming. Two palettes: "Archive Vault" dark theme (warm deep blacks, amber gold `#c9a64e` accent) and "Reading Room" light theme (warm ivory `#faf7f0`, saddle brown `#8b4513` accent). Fluid typography scale, spacing, shadow, scrollbar, and transition tokens. Google Fonts import: Cormorant Garamond (headings), Source Serif 4 (body), Inter (UI), JetBrains Mono (code).
- **Theme toggle** (`src/components/ThemeToggle.astro`) — Moon/sun SVG button in the sidebar header. Persists choice to `localStorage` as `chronos-theme`. Toggles `data-theme="light"` on `<html>`. Smooth 300ms crossfade via `theme-transitioning` class.
- **Reading progress bar** (`src/components/ReadingProgress.astro`) — Fixed 3px accent-colored bar at viewport top with glow shadow. Passive `requestAnimationFrame`-throttled scroll tracking.

### Changed

- **`BaseLayout.astro`** — Replaced all hardcoded GitHub-dark colors with theme.css design tokens. Added inline anti-flash `<script>` that reads `localStorage` before first paint. Added radial vignette pseudo-element on body, `::selection` colors in accent, smooth scroll. Typography now uses serif families: Cormorant Garamond for h1–h6, Source Serif 4 for body, JetBrains Mono for code. Tables, blockquotes, scrollbars all use theme tokens. Z-index layering for vignette vs content.
- **`Sidebar.astro`** — Header now uses serif font (Cormorant Garamond, 700 weight, accent color) with ThemeToggle in flexbox row. Section headings gain 30px accent-colored decorative rules. Nav links use Inter font with improved active state (accent-muted background + left border). Footer line with © added at bottom. Mobile overlay uses `backdrop-filter: blur(4px)`. All colors migrated to CSS custom properties.
- **`index.astro`** — Complete landing page redesign. Hero section: small-caps classification label, italic Cormorant Garamond tagline at fluid display size, subtitle, accent divider rule. Statistics bar: live document/synthesis/analysis/tradition counts in serif numerals. "First Doorways" section: 6-card grid with quote hooks, hover lift animation, and arrow indicators. Archive footer: thematic tagline, GitHub + index links, open-source credit. Responsive: left-aligned hero on mobile, single-column card grid, wrapped stats.
- **`404.astro`** — Giant "404" watermark at 6% opacity in Cormorant Garamond behind content. Tier diagram styled with accent-muted border. Return links converted to card grid with hover lift matching doorway card pattern. All colors use theme tokens.
- **`favicon.svg`** — Accent color updated from blue (`#58a6ff`) to amber gold (`#c9a64e`), background from `#0d1117` to `#0d0e12`.

---

## [0.10.1] — 2026-06-19

### Fixed

- **Mobile sidebar** (`src/components/Sidebar.astro`) — Replaced CSS-only checkbox hack with JavaScript-driven open/close. New implementation adds backdrop overlay with blur, close button, Escape key handling, body scroll lock, and auto-scroll active link into view. Sidebar width capped at `85vw` on small viewports.
- **Mermaid diagrams** (`src/layouts/BaseLayout.astro`) — Mermaid now initializes with `default` or `dark` theme based on `data-theme` attribute. Shiki-highlighted `<pre data-language="mermaid">` blocks are transformed to raw `<pre class="mermaid">` before Mermaid's deferred render.
- **Code block scroll shadows** (`src/layouts/BaseLayout.astro`) — Added gradient-based scroll shadows on overflowing `<pre>` blocks to indicate hidden content.
- **Anti-flash script** (`src/layouts/BaseLayout.astro`) — Now respects `prefers-color-scheme` media query when no explicit `localStorage` preference is set.
- **Hero text alignment** (`src/pages/index.astro`) — Removed redundant `text-align: left` override on mobile that broke centered hero layout.

### Changed

- **Accent colour palette** — Dark theme accent shifted from `#c9a64e` to `#d4aa4e` (warmer gold); light theme accent from `#8b4513` to `#a0522d` (sienna). Corresponding hover, muted, glow, and selection values updated across `src/styles/theme.css` and `public/favicon.svg`.
- **`src/layouts/BaseLayout.astro`** — Added `BackToTop` component import and placement, dual `<meta name="theme-color">` tags for dark/light modes, improved anti-flash script with `prefers-color-scheme` detection, Mermaid theme-follows-data-theme initialization, Mermaid block transform for Shiki output, and scroll-shadow CSS on overflowing code blocks.

### Added

- **`src/components/BackToTop.astro`** — New floating button that appears on scroll past one viewport height. Smoothly scrolls to top on click.

---

## [0.9.0] — 2026-06-18

### Added

- **Broadsheet Celestial Events synthesis** (`audit/14-broadsheet-celestial-events.md`) — Gap-evidence analysis for the "Silent Period" (573 BCE – 1975 CE), examining seven historical celestial phenomenon events recorded in European broadsheets and one mass-witness phenomenon (1535–1917 CE). 10 numbered findings covering: signal/noise methodology adapted from NHI correlation framework, control baseline (Stockholm Vädersolstavlan 1535), high-signal events (Nuremberg 1561, Basel 1566, Stralsund 1665), complex signal (Fátima 1917), source credibility context (Hans Glaser's broadsheet pattern), and gap-evidence integration with the unified hypothesis. ~828 lines, 8 sections.
- **Control baseline document** (`audit/control-baseline-vadersolstavlan.md`) — Full forensic analysis of the 1535 Stockholm sun dog painting as the control baseline for pre-modern atmospheric-optics depiction. Establishes the upper bound of "mundane" accuracy achievable by 16th-century observers against which anomalous claims are measured.
- **Research notes** (`audit/research-notes-broadsheet-methodology.md`) — Scholarly frameworks for historical celestial broadsheet analysis: Vallée's "stock myth" / propaganda hypothesis, Aubeck's *Wonders in the Sky* dataset, Magin's source-critical methodology, and modern halo-simulation cross-validation.
- **ERA 6.5: BROADSHEET ERA** in `audit/03-event-timeline.md` — New timeline era inserting intermittent witness accounts (1535–1917 CE) between the Reduced Contact / Silent Period and the Contemporary Processing Infrastructure era. Includes 6 events with signal-strength classification and cross-references. ASCII timeline and Gantt chart updated.
- **CROSS-REFERENCE 25: Celestial Battle Accounts** in `audit/04-cross-references.md` — Five-column comparison (Revelation, Mahābhārata, Ezekiel, Popol Vuh, Broadsheet Reports) demonstrating structural homology between ancient "divine warfare" accounts and 16th-century broadsheet "objects fighting in the sky" reports. Convergence strength: HIGH.
- **Section 1.14: Broadsheet of Celestial Events** in `audit/10-correlation-map.md` — Per-text perspective inventory entry with key correlations (celestial battle analogs, signal/noise methodology, ambient vs. directed contact distinction).
- **Thematic Cluster 2.9: Silent Period & Gap Evidence** in `audit/10-correlation-map.md` — New correlation cluster linking broadsheet evidence with NHI correlation, NDE correlation, timeline gap entries, and ancient celestial battle parallels. Mermaid diagram updated to 9 clusters.
- **Linking blueprint updates** in `audit/10-correlation-map.md` — Phase 2 hyperlink retrofit extended: 11 new link targets across synthesis documents connecting broadsheet analysis to timeline, cross-references, NHI correlation, NDE correlation, and unified hypothesis.

### Updated

- `README.md` — `14-broadsheet-celestial-events.md` added to Cross-Cutting Syntheses list and First Doorways table ("The Silent Period" entry).
- `audit/00-INDEX.md` — `14-broadsheet-celestial-events.md` entry added to cross-cutting synthesis table.
- `audit/11-unified-hypothesis.md` — Added broadsheet reference in Chapter VII (autonomous test phase) acknowledging ambient observations during the Silent Period.
- `audit/12-NHI-correlation.md` — Added broadsheet reference in the two-readings framework, establishing the broadsheet record as the first witness-account evidence from within the gap period itself.
- `.omo/boulder.json` — Boulder state updated for broadsheet workstream completion.

---

## [0.8.2] — 2026-06-15

### Fixed

- **`src/remark-link-rewrite.mjs`** — Normalise `file.path` from Astro content layer: content collection entries pass the path as a `file://` URL, causing `path.dirname` to produce an invalid root directory. Added `fileURLToPath` conversion to handle both plain filesystem paths and URL-encoded paths.

### Updated

- **`PLAN.md`** — Phase 5 (Visual Assets) and Phase 7 (Publishing Pipeline) marked COMPLETED. All 6 Mermaid diagrams deployed and verified; static site live at `actual-designer.github.io/ancient-texts-research/`.

---

## [0.8.1] — 2026-05-25

### Added

- **Unified Hypothesis NHI/NDE integration** (`audit/11-unified-hypothesis.md`) — 6 targeted insertions integrating modern evidentiary tracks from the NHI and NDE correlation addenda into the capstone synthesis document:
  - Ch. I: NHI discourse independently converges on same operator properties (stratified hierarchy, biological intervention, terrestrial infrastructure).
  - Ch. V: NHI two-readings framework extends the withdrawal scenarios — post-mortem pipeline as continuous interface vs. renewed contact via contamination cycle.
  - Ch. VI: NDE post-mortem pipeline homology confirms the Egyptian Duat sequence through modern cardiac arrest data (tunnel/Duat, life review/Weighing, Being of Light/Osiris).
  - Ch. VII: NDE and NHI records represent leakage from the otherwise-filtered operational environment — the interface never fully closed.
  - Ch. VIII: Single sentence extended with coda clause acknowledging modern convergent evidentiary tracks.
  - Predictions: Two new falsifiable entries — NDE verifiability (AWARE II template) and NHI discourse convergence (40+ structural parallels).

## [0.8.0] — 2026-05-25

### Added

- **NDE Correlation addendum** (`audit/13-nde-correlation.md`) — Comprehensive analysis of Near-Death Experiences through the Archive's literalist/technological lens, treating NDEs as a modern evidentiary track revealing the same non-human facility network described in ancient texts. 13 sections, ~7,500 words covering:
  - NDE core phenomenology and prevalence (Moody, Greyson, AWARE II).
  - Amnesia filter applied to modern NDE accounts.
  - Veridical perception evidence (Pam Reynolds, Maria's shoe, AWARE II ceiling targets).
  - Post-mortem processing pipeline structural homology with Egyptian Duat.
  - Entity encounters (beings of light, guides, deceased relatives, malevolent entities).
  - Life review as identity-comparator technology.
  - Distressing NDEs as individual-level termination protocols.
  - Cross-cultural patterns (Egyptian, Tibetan, Greek, Zoroastrian, modern).
  - Full skeptical analysis engaging DMT, hypoxia, temporal lobe, and terminal brain surge hypotheses.
  - After-effects as evidence of functional reprogramming.
  - Shared Death Experiences and Deathbed Visions demonstrating continuous infrastructure access.
  - Executive summary with integration synthesis across all 12 prior Archive documents.
- **NDE-DERIVED ENTITY CATEGORIES** section in `audit/01-entity-registry.md` — 5 new entity types with functional classification and cross-references.
- **NDE-RELATED TECHNOLOGIES** section in `audit/02-technology-catalog.md` — 3 new technology entries (life review comparator, consciousness transport corridor, adaptive assessment interface).
- **ERA 6: Contemporary Processing Infrastructure** in `audit/03-event-timeline.md` — NDEs, AWARE II, and SDE/DBV as continuous modern phenomenon.
- **CROSS-REFERENCE 24: The Near-Death Experience Sequence** in `audit/04-cross-references.md` — FIVE independent traditions (Egyptian, Tibetan, Greek, Zoroastrian, modern medical) mapping the same processing pipeline.
- **Section 7: Individual-Level Termination** in `audit/05-great-reset.md` — NDE judgment encounters as individual-scale equivalent of population-level sterilization.
- **Section 7: Individual Termination and Post-Biological Processing** in `audit/07-the-human-project.md` — Completes the human management arc with NDE as missing phase.
- **Section 12.3: NDE and NHI Contact Overlap** in `audit/12-NHI-correlation.md` — Parallel modern evidentiary track convergence.
- **INDEX entry** for `13-nde-correlation.md` in `audit/00-INDEX.md`.

### Updated

- Link validation: all NDE-related cross-references cleaned and verified (script: `scripts/validate-links.py`).
- `.sisyphus/plans/nde-addendum.md` — Completion of 21-task execution plan.
- `.sisyphus/notepads/nde-addendum/learnings.md` — Writing patterns and conventions for NDE analysis.
- `.sisyphus/run-continuation/` — Session continuation state for NDE completion.
- **`README.md`** — Added NDE addendum to Narrative Arc (chapter 8), Cross-Cutting Syntheses list (13th entry), First Doorways table, and How to Explore trails.

---

## [0.7.4] — 2026-05-20

### Added

- **Deep fact-check — Full audit of all 14 source texts completed:**
  - Numerical claims verified against source material across all documents.
  - Cross-references validated for existence, accuracy, and bidirectional consistency.
  - External source claims traced to originals (including Zoroastrian Gathas, Hesiod's Theogony, Yoga Sutras) with detailed audit reports.
  - Quote accuracy verified against extracted text with remediation tracking for discrepancies.
  - Certification document (`audit/verification/certification.md`) and master audit summary (`audit/verification/00-audit-master.md`) generated — zero errors certified.
  - Per-document audit reports and evidence files produced in `audit/verification/reports/` and `audit/verification/evidence/`.
  - Verification toolkit (`scripts/verify/`) with automated Python scripts for numerical, cross-ref, external-source, and quote verification, plus `run_all.py` orchestration.
- **Extracted text corpus** (`texts/extracted/`) — Plain-text extraction of all 14 source PDFs for programmatic analysis, cross-reference search, and automated verification.
- `.sisyphus/run-continuation/ses_1c3a4279dffezXLE1SpgIS07ai.json` — Session continuation state for deep fact-check completion.

### Updated

- `.sisyphus/plans/deep-fact-check.md` — All remaining plan tasks (33, F1–F4) marked completed and approved by review agents.
- `.obsidian/workspace.json` — Added verification review documents to workspace tabs (cross-ref, NHI, numerical, quote review summaries); active file set to certification summary.

---

## [0.7.3] — 2026-05-18

### Added

- **`README.md` — Complete narrative gateway rewrite:**
  - New "The Amnesia Problem" section with smartphone-to-3000-BCE analogy, reframing every "miracle" as a vocabulary-limited technical description.
  - "Evidence of Convergence" cross-region isolation table (Mesopotamia, Levant, India, Egypt, Mesoamerica, Scandinavia, Greece, Persia) demonstrating independent tradition convergence.
  - "Case Studies" section with two full analyses: Atrahasis Flood (sterilization protocol with technical breakdown) and Ezekiel's Merkabah (aerospace vehicle with component identification and ASCII schematic).
  - "The Narrative Arc" — end-to-end story summary from operator arrival to present autonomous test phase.
  - "How to Navigate" guide with "First Doorways" table recommending entry points for new readers.
  - Archipelago ASCII diagram and complete synthesis document listing with descriptions.
- `.sisyphus/plans/readme-rewrite.md` — Execution plan for the README rewrite.
- `.sisyphus/evidence/readme-rewrite-*.txt` — 6 verification evidence files documenting link validation, content checks, and QA passes.

### Updated

- `audit/00-INDEX.md` — Reordered synthesis docs to proper numerical sequence (08-09-10 before 11-12); added missing entries for `08-translation-key.md` and `09-location-registry.md` which were absent since inception; updated source text counts from 13 to 14 throughout.
- `audit/08-translation-key.md` — Scope header updated from "13 source texts" to "14" with Bhagavad Gītā added to listing.
- `audit/10-correlation-map.md` — Updated "13 per-text analyses" to "14" to reflect current document count.
- `.sisyphus/boulder.json` — NHI correlation workstream marked completed; readme-rewrite plan registered and completed.
- `.obsidian/workspace.json` — Added 11-unified-hypothesis tab alongside 12-NHI-correlation; active tab updated.

---

## [0.7.2] — 2026-05-18

### Added

- `AGENTS.md` — Added header metadata (Generation timestamp, commit hash, branch) following the repo's conventions.
- `audit/analyses/AGENTS.md` — New directory-level guide documenting the per-text deep-dive template structure, numbering conventions, incident format, cross-reference style, source attribution rules, and anti-patterns for analysts writing new analyses.

### Updated

- **`AGENTS.md`** — Major restructure of repository tree with full detail:
  - Expanded synthesis document listing from 7 to 12 (now includes 08-nephilim-reassessment through 12-nhi-correlation).
  - Updated per-text analysis count from 7 to 14.
  - Added `scripts/` directory with `validate-links.py`.
  - Refined descriptions for all documents with consistent formatting.
- `.obsidian/workspace.json` — Active document switched from `12-NHI-correlation.plan.md` to the finalized `12-NHI-correlation.md`; OpenCode view tab reordering; removed `github-sync` from hidden items.
- `.sisyphus/run-continuation/` — New session continuation state for the current workstream.

---

## [0.7.0] — 2026-05-18

### Added

- **NHI correlation synthesis document:**
  - `audit/12-NHI-correlation.md` — Cross-cutting synthesis correlating modern UFO/NHI disclosure discourse (Vallée, Keel, Grusch, AARO/Pasulka) with the Archive's unified hypothesis. 14 numbered findings covering: historical continuity of encounter traditions, structural failure of the Extraterrestrial Hypothesis, operator ontology (interdimensional/physical hybrid), the amnesia control architecture as the "psychic veil," Watcher-equivalent surveillance posture, the three-tier operational hierarchy matching ancient entity registries, timeline-gap analysis addressing the 2,500-year apparent lull, the multigenerational human-NHI lineage program, and falsification criteria. Includes correlation methodology section addressing pattern-seeking bias, treatment of Vallée's "adaptation to expectation" objection, and appendix-level source extracts from all four modern evidentiary tracks.
- **Deep source research evidence:**
  - `.sisyphus/evidence/deep-source-vallee.md` — Key passages from *Passport to Magonia* and *Messengers of Deception*
  - `.sisyphus/evidence/deep-source-keel-grusch.md` — Extracts from *Operation Trojan Horse* and Grusch congressional testimony
  - `.sisyphus/evidence/deep-source-aaro-pasulka.md` — AARO report analysis and Pasulka's *American Cosmic* findings
- `.sisyphus/evidence/fragments/` — 14 task output fragments documenting the section-by-section drafting process

### Updated

- `audit/00-INDEX.md` — Added `12-NHI-correlation.md` entry to cross-cutting synthesis table with description
- `.sisyphus/` — Active plan, boulder state, notepads, and run-continuation updated for NHI correlation workstream
- `.obsidian/workspace.json` — Editor layout updated to reference NHI correlation documents

### Removed

- `audit/12-NHI-correlation.plan.md` — Deleted planning document for NHI correlation workstream (plan completed and superseded by deliverable)

---

## [0.6.1] — 2026-05-17

### Updated

- **README.md** — Added `11-unified-hypothesis.md` to "Cross-Cutting Syntheses" listing and "First Doorways" table; moved `08-translation-key.md` from "Evidence Locker" into syntheses section where it belongs.
- **Style pass — em dash reduction** across 10 documents to comply with audit style conventions:
  - `audit/01-entity-registry.md`, `audit/03-event-timeline.md`, `audit/04-cross-references.md`, `audit/09-location-registry.md`, `audit/10-correlation-map.md`, `audit/11-unified-hypothesis.md`
  - `audit/analyses/poetic-edda.md`, `audit/analyses/theogony-works-and-days.md`, `audit/analyses/yoga-sutras.md`, `audit/analyses/zoroastrian-gathas.md`
- `audit/11-unified-hypothesis.md` — Comprehensive hyperlink retrofit adding cross-references to all source analyses and synthesis documents.

### Added

- `.sisyphus/` — Sisyphus tool working state (plans, evidence logs, run-continuation state, boulder config).
- `.obsidian/` — Obsidian workspace and editor configuration (themes, plugins, workspace layout).
- `.sisyphus/evidence/` — Em dash audit verification files documenting pre/post counts across all modified documents.

### Fixed

- `audit/10-correlation-map.md` — Table column alignment formatting in remaining unaligned tables.

---

## [0.6.0] — 2026-05-17

### Added

- **Capstone synthesis document:**
  - `audit/11-unified-hypothesis.md` — Singular hypothesis unifying all fourteen foundational texts and all prior synthesis documents. Eight chapters covering: operator origin and ontology (agnostic on extraterrestrial vs. precursor vs. multidimensional), the human project from labor solution to candidate civilization, the structural contamination cycles, the Flood as failed sterilization protocol, the withdrawal as planned handoff accelerated by institutional entropy, the post-mortem integration pipeline as a promotion track, the current autonomous test phase under active amnesia architecture, and the Revelation briefing as a standing operational plan. Includes single-sentence hypothesis statement, full unified statement, 5 testable predictions, 5 falsification conditions, 5 acknowledged open questions, and complete arc ASCII timeline from pre-operational void to present.

### Updated

- `audit/00-INDEX.md` — 11-unified-hypothesis.md entry added to cross-cutting synthesis table.

---

## [0.5.2] — 2026-05-16

### Fixed

- `audit/10-correlation-map.md` — Table column alignment formatting in all 8 thematic correlation tables (cosmetic/readability).

---

## [0.5.1] — 2026-05-16

### Updated

- **README.md** — Complete rewrite: added epigraph quote, restructured Project Architecture into Evidence Locker and Cross-Cutting Syntheses subsections with hyperlinks, added "First Doorways" quick-start table with entrance hooks for all synthesis documents.
- **Phase 2 hyperlink retrofit — completion pass** across 10 documents:
  - `audit/00-INDEX.md` — Source table text names converted to Markdown links.
  - `audit/05-great-reset.md` — Scope line bare references linked.
  - `audit/06-weapons-doctrine.md` — Full hyperlink retrofit of all source references in escalation-phase and aftermath tables.
  - `audit/07-the-human-project.md` — Full hyperlink retrofit: surveillance, liaison, escalation, cycle-comparison, and invariants sections.
  - `audit/09-location-registry.md` — All source and cross-reference columns in all location tables retrofitted with Markdown links (~324 line changes).
  - `audit/10-correlation-map.md` — Full hyperlink retrofit: section headers, relevant-synthesis-doc lists, and all thematic correlation table rows.
  - `audit/analyses/book-of-the-dead.md` — Xibalbá cross-reference extended with explicit source link.
  - `audit/analyses/enoch-watchers.md` — Viśvarūpa and Pyramid Texts sky portals cross-references added.
  - `audit/analyses/ezekiel-merkabah.md` — Enoch wheels and location-registry cross-references added.
  - `audit/analyses/gilgamesh.md` — Technology catalog and human-project cross-references added.
  - `audit/analyses/revelation.md` — Book of the Dead cross-reference added.

---

## [0.5.0] — 2026-05-16

### Added

- **Per-text analysis:**
  - **Yoga Sutras** (`audit/analyses/yoga-sutras.md`) — 6-incident forensic analysis covering: citta-vṛtti-nirodha (consciousness lockdown protocol), Īśvara as reference-grade entity with AUM resonance call-sign, five kleśas as cognitive lock-in architecture, Aṣṭāṅga yoga as 8-stage operator conditioning curriculum, siddhi catalog (40+ supernormal capabilities), Kaivalya as full system decoupling.
- **Source files (2):**
  - `texts/yoga-sutras-patanjali.pdf` — Madhvācārya/Beloved 2007 translation (239 pp).
  - `texts/yoga-sutras-patanjali.txt` — plain-text extraction for search indexing.
- **Planning document:**
  - `audit/10-correlation-map.md` — Phase 1 deliverable: per-text perspective inventory, 8 thematic correlation clusters, complete linking blueprint for Phase 2 hyperlink retrofit.

### Updated

- **Phase 2 hyperlink retrofit — all 20 content documents** received cross-reference links:
  - **9 previously unlinked per-text analyses** (atrahasis, book-of-the-dead, enoch-watchers, ezekiel-merkabah, gilgamesh, poetic-edda, revelation, rig-veda, theogony-works-and-days, zoroastrian-gathas) — ~218 inline links added connecting parallel incidents across sources.
  - **4 already-linked analyses** (pyramid-texts, rig-veda, mahabharata, popol-vuh) — ~19 gap-fill links added.
  - **4 synthesis documents** (05-great-reset, 06-weapons-doctrine, 07-the-human-project, 09-location-registry) — ~16 inline source citation links added.
  - `audit/00-INDEX.md` — 10-correlation-map.md entry added to synthesis table.
  - `audit/01-entity-registry.md` — Yoga Sutras theater added: Īśvara (Tier 2 reference entity), Patañjali (Tier 3 human compiler), system architecture (puruṣa, citta), managed principles (kleśas, Kaivalya). Scope updated to 14 foundational texts.
  - `audit/02-technology-catalog.md` — New section 13 (Consciousness Training and Operator Conditioning): 6 entries covering the full Yoga Sutras protocol stack. Scope updated to 14 texts.
  - `audit/04-cross-references.md` — 4 new cross-reference rows: consciousness training/operator conditioning, consciousness lockdown state, multi-stage operator qualification, omega-point consciousness state. Scope updated to 14 texts.

---

## [0.4.0] — 2026-05-16

### Added

- **Per-text analyses (5 new):**
  - **Book of the Dead** (`audit/analyses/book-of-the-dead.md`) — Egyptian post-mortem processing pipeline: Tuat transit, Hall of Maati, Negative Confession before 42 Assessors, the Weighing of the Heart (biometric identity comparator), Osiris throne ratification, and the Field of Reeds as post-biological settlement.
  - **Poetic Edda** (`audit/analyses/poetic-edda.md`) — Norse creation (Ginnungagap, Ymir → planetary infrastructure), Ask/Embla triple-operator fabrication, Aesir-Vanir factional war and merger, Yggdrasil nexus, Odin's rune upgrade protocol, Baldr's termination and Ragnarök cascade.
  - **Revelation** (`audit/analyses/revelation.md`) — Projected terminal intervention sequence: throne room command center, seven-sealed scroll authorization transfer, multi-phase calibrated strikes (Four Horsemen, Trumpets at 33% yield, Vials at full yield), War in Heaven, Two Beasts, Armageddon, Millennium, New Jerusalem replacement habitat.
  - **Theogony & Works and Days** (`audit/analyses/theogony-works-and-days.md`) — Greek creation sequence (Chaos → Gaia → Ouranos), generational command coups (Ouranos→Kronos→Zeus), Titanomachy factional war, Prometheus knowledge theft, Pandora as counter-deployment, and sequential Five Ages human prototypes.
  - **Zoroastrian Gathas** (`audit/analyses/zoroastrian-gathas.md`) — Ahura Mazda as supreme command, dual-operator system (Spenta/Angra Mainyu), seven Amesha Spenta functional terminals, Zarathushtra as first-person corruption whistleblower, Chinvat Bridge entity-assessment gateway, Frashokereti terminal renewal sequence.
- **Synthesis documents (2 new):**
  - `audit/08-translation-key.md` — Terminology mapping from source-text vocabulary to modern technology equivalents across all traditions (Norse, Greek, Egyptian, Zoroastrian, Hebrew, Vedic, Mesoamerican).
  - `audit/09-location-registry.md` — Geographical and extradimensional registry of all named locations across the archive (Mount Meru, Olympus, Asgard, Tuat, Xibalbá, New Jerusalem, etc.).
- **Source PDFs (3):**
  - `texts/Hesiod-Theogony-Works-and-Days.pdf`
  - `texts/The-Poetic-Edda.pdf`
  - `texts/The-Yasna.pdf`
- **Script:** `scripts/validate-links.py` — cross-reference link validation utility.
- **Plan document:** `PLAN.md` — project roadmap and source backlog.

### Updated

- **All 8 cross-cutting synthesis documents** — extended to integrate findings from all 5 new source analyses:
  - `audit/00-INDEX.md` — 5 new analyses, 2 new synthesis docs, 3 new sources added to source table.
  - `audit/01-entity-registry.md` — entities from Greek pantheon (Zeus, Kronos, Ouranos, Prometheus, Pandora, etc.), Norse pantheon (Odin, Thor, Loki, etc.), Egyptian Osiris/42 Assessors, Zoroastrian Amesha Spenta terminals, and Revelation's Dragon/Beasts/Lamb added with hierarchy mapping.
  - `audit/02-technology-catalog.md` — Norse (Ginnungagap, Yggdrasil, runes), Greek (adamantine sickle, Pandora's jar, Olympic council), Egyptian (Balance of Maat, Tuat, Field of Reeds), Zoroastrian (Chinvat Bridge, Frashokereti), and Revelation (sealed scroll, New Jerusalem, lake of fire) entries added.
  - `audit/03-event-timeline.md` — 5 new eras added: Norse (Ymir→Ragnarök→rebirth), Greek (Chaos→Iron Age), Zoroastrian (dual-operator ontology→Frashokereti), Egyptian continuous post-mortem processing, and Revelation projected terminal sequence.
  - `audit/04-cross-references.md` — 12 new cross-references (CR-12 through CR-23): Throne Room/Command Center, Gated Transit Pipeline, Biometric Tagging, Processor Entity Death/Reassembly, Post-Mortem Reanimation, Post-Biological Settlement, War in Heaven, Primeval Entity → Infrastructure, Iterative Prototypes, Intra-Pantheon Factional War, Knowledge Restriction, Terminal Collapse + Renewal.
  - `audit/05-great-reset.md` — scope expanded to include Revelation's projected terminal sterilization.
  - `audit/06-weapons-doctrine.md` — scope expanded to include Revelation's multi-phase kinetic and environmental weapon systems.
  - `audit/07-the-human-project.md` — scope expanded from 7 to 10 foundational texts; Norse, Greek, and Zoroastrian creation arcs integrated.

---

## [0.3.0] — 2026-05-12

### Added

- **Per-text analysis:**
  - **Rig Veda** (`audit/analyses/rig-veda.md`) — 10-incident forensic analysis covering: Nasadiya Sukta (facility activation), Hiranyagarbha (operator gestation chamber), Purusa Sukta (primary intelligence decomposition), Indra's Vajra (directed-energy weapon), Asvins biomedical corps (regeneration, prosthetics, ocular restoration), Vishnu's three strides (orbital demarcation), Soma (bio-enhancement compound), Yama (post-mortem transport and processing), Varuna (surveillance network), and Agni (communications relay).

### Updated

- **Cross-cutting synthesis documents** — all extended to integrate Rig Veda findings:
  - `audit/01-entity-registry.md` — 14 Vedic entities mapped to 3-tier hierarchy (Tier 1: Hiranyagarbha/Purusa; Tier 2: Indra, Agni, Varuna, Asvins, Yama, Tvastar, Vishnu, Adityas; Tier 3: Maruts, Vayu, Surya, Soma).
  - `audit/02-technology-catalog.md` — Vedic entries added across all sections: aerospace (vimanas), weapons (Vajra), facilities (Hiranyagarbha, orbital habitats), communication (Agni relay), medical (Asvins protocols, Soma), surveillance (Varuna network), and knowledge systems.
  - `audit/03-event-timeline.md` — new ERA 0: VEDIC CREATION CYCLE inserted before Era 1, with 7 events predating all other sources (facility activation, entity generation, system decomposition, Vrtra engagement, Asvins protocols, Soma program, Yama processing).
  - `audit/04-cross-references.md` — new CR-11 (Creation from Void / Cosmic Egg) added, plus Vedic evidence appended to 7 existing cross-references.
  - `audit/00-INDEX.md` — Rig Veda added as source #8 with analysis entry.

---

## [0.2.0] — 2026-05-11

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0] — 2026-05-11

### Added

- **Per-text analyses (3 new):**
  - **Mahābhārata** (`audit/analyses/mahabharata.md`) — vimānas, astras, genetic commissioning of Kurukshetra heroes, combined-arms warfare, immortality and quarantine motifs.
  - **Popol Vuh** (`audit/analyses/popol-vuh.md`) — iterative creation R&D with four prototypes, deliberate flood of the Wood People, engineered amnesia / cognitive limitation, Xibalbá as a subterranean facility.
  - **Ancient Egyptian Pyramid Texts** (`audit/analyses/pyramid-texts.md`) — post-mortem processing pipeline (Duat → Akhet → Sky), body reconstitution protocol, gated transit via ferryman and doorkeeper, the Cannibal Hymn as capability absorption, celestial geography.
- **Synthesis documents (2 new):**
  - `audit/06-weapons-doctrine.md` — weapons authorization hierarchy and escalation pathology across all source traditions.
  - `audit/07-the-human-project.md` — complete longitudinal narrative of human creation, management, reset, and the Pyramid Texts' "return path" integration protocol.

### Updated

- **Cross-cutting synthesis documents** (Entity Registry, Technology Catalog, Event Timeline, Cross-References, Great Reset, master Index) — all extended to integrate findings from all seven source texts.

---

## [0.1.0] — 2026-05-11

### Added

- **Project methodology** (`claude.md`) — core directives: literalism over metaphor, reverse-engineering framework (glory → plasma, angels → entities, etc.), amnesia filter, and the four-part analysis structure (Source Material → Mainstream Interpretation → Literal Reconstruction → Plausible Mechanism).
- **Per-text analyses (4):**
  - **Epic of Atrahasis** (`audit/analyses/atrahasis.md`) — Igigi labor revolt, creation of humanity as workforce, the Flood as population control.
  - **Book of Enoch (1 Enoch)** (`audit/analyses/enoch-watchers.md`) — Watchers' descent, technology transfer to humanity, Nephilim hybrids, heavenly journeys through crystal structures.
  - **Epic of Gilgamesh** (`audit/analyses/gilgamesh.md`) — Enkidu as biological fabrication, Cedar Forest expedition, Bull of Heaven, Utnapishtim's first-hand Flood account, plant of immortality as anti-aging research.
  - **Book of Ezekiel** (`audit/analyses/ezekiel-merkabah.md`) — Merkabah craft description, transport events, Valley of Dry Bones reanimation protocol, Temple blueprints as a specification document.
- **Synthesis documents (5):**
  - `audit/01-entity-registry.md` — non-human actors and hierarchy across all sources.
  - `audit/02-technology-catalog.md` — miracles mapped to plausible technology (genetic engineering, aerospace, directed energy, etc.).
  - `audit/03-event-timeline.md` — unified chronology across all sources.
  - `audit/04-cross-references.md` — parallel accounts (Flood, etc.) across independent traditions.
  - `audit/05-great-reset.md` — Flood as deliberate sterilization protocol, Ark as genetic vault.
- **Master index** (`audit/00-INDEX.md`) — source table and audit document index.
- **Source PDFs (6):**
  - `texts/EpicofAtrahasis.pdf`
  - `texts/The Complete Book of Enoch, Standard English Version - Jay Winter.pdf`
  - `texts/THE EPIC OF GILGAMESH.pdf`
  - `texts/eze.pdf` (Book of Ezekiel)
  - `texts/Mahabharata.pdf` (Romesh C. Dutt condensed verse)
  - `texts/Menon_Ramesh-The-Complete-Mahabharata_-Volume-1-12.pdf` (full Menon translation)

---

[0.2.0]: https://github.com/AndreVairCrux/ancient-texts-research/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/AndreVairCrux/ancient-texts-research/releases/tag/v0.1.0
