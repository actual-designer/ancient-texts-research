# Chronos Archive — Development Plan

**Generated:** 2026-05-15
**Status:** Active

---

## Phase 1: Close Content Gaps

### 1.1 Analyze Book of Revelation
- Read `texts/bookofrevelation.pdf`
- Write `audit/analyses/revelation.md` (10+ incidents: throne room, seven seals, trumpets, beasts, Armageddon, lake of fire, New Jerusalem)
- Estimated incidents: 12

### 1.2 Analyze Book of the Dead
- Read `texts/The-Book-of-the-Dead.pdf`
- Write `audit/analyses/book-of-the-dead.md` (weighing of heart, ferryman, gates, field of reeds, judgment hall)
- Estimated incidents: 8

### 1.3 Update Synthesis Documents
- Update `00-INDEX.md` with both new sources
- Extend entity registry with new actors
- Extend technology catalog with new tech
- Update cross-references
- Update event timeline (Book of Revelation postdates all — could be future projection)

---

## Phase 2: Infrastructure & Quality

### 2.1 Centralized Glossary / Translation Key
- Create `audit/08-translation-key.md`
- Every archaic→technical mapping across all sources, cross-referenced
- Sortable by archaic term and by modern concept

### 2.2 Automated Quality Checks
- Script to validate cross-reference links in all Markdown files
- Script to verify all analyses include the four-part framework
- Script to flag orphan entities/tech not referenced in synthesis docs

---

## Phase 3: Expand to New Traditions

### 3.1 Norse Mythology
- Add `texts/poetic-edda.pdf` (source)
- Analyze Völuspá (creation, Ragnarök), Grímnismál (cosmology), Vafþrúðnismál
- Key intersections: Yggdrasil (world-tree/axis mundi), Ragnarök (scheduled reset), Mimir's well (knowledge repository)

### 3.2 Greek Mythology
- Add `texts/theogony.pdf` (Hesiod)
- Analyze Titanomachy (regime-change warfare), Prometheus (human creation/R&D), Pandora (engineered amnesia vector)

### 3.3 Zoroastrian
- Add Gathas / Bundahishn
- Analyze dualistic cosmology, Frashokereti (final restoration/reset)

---

## Phase 4: Geospatial / Geographic Analysis

### 4.1 Create Location Catalog
- `audit/09-location-registry.md`
- All named locations across all sources
- Cross-reference same location under different names (e.g., Dilmun ≈ Eden ≈ Yggdrasil base?)
- Map axis mundi sites (Mount Meru, Mount Zion, Olympus, etc.)

---

## Phase 5: Visual Assets

### 5.1 Mermaid Diagrams
- Entity hierarchy diagram → embed in `01-entity-registry.md`
- Event timeline → embed in `03-event-timeline.md`
- Weapons escalation chain → embed in `06-weapons-doctrine.md`
- Human project lifecycle → embed in `07-the-human-project.md`

---

## Phase 6: Knowledge Graph Data Layer

### 6.1 YAML Frontmatter
- Add structured frontmatter to every analysis document
- Fields: title, source, date, entities, technologies, locations, cross-references
- Enables programmatic querying and future web publishing

---

## Phase 7: Publishing Pipeline

### 7.1 Static Site Generator
- Evaluate MkDocs, Jekyll, or Astro for static site generation
- Configure with the Chronos Archive theme
- Deploy to GitHub Pages

---

## Work Order

Phase 1 is highest priority — closes content gaps. Phase 2 adds infrastructure. Phases 3-7 are additive enhancements. Work sequentially within each phase.

---

## Completion Criteria

- [ ] All 11 source PDFs analyzed
- [ ] All 8 cross-cutting synthesis documents updated
- [ ] Glossary document created with 50+ entries
- [ ] Validation scripts pass with zero errors
- [ ] At least 2 new traditions added
- [ ] Location registry with 20+ entries
- [ ] Mermaid diagrams in 4+ documents
- [ ] YAML frontmatter on all analyses
- [ ] Static site deploys from main branch
