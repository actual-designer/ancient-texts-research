# AGENTS.md — The Chronos Archive

**Generated:** 2026-05-18
**Commit:** `3f2a1e5`
**Branch:** `main`

This repo is a **hard science-fiction research project** that applies a literalist, technological lens to ancient texts. There is no code, no build system, no test runner — only Markdown analysis and PDF source documents.

## Must-read first

- **`claude.md`** — The project's core methodology: literalist/technological lens, reverse-engineering framework (glory→plasma, angels→entities, etc.), amnesia filter, and the required analysis structure (Source Material → Mainstream Interpretation → Literal Reconstruction → Plausible Mechanism). Every analysis in the repo follows this framework. Read this before any research work.

## Repository structure

```
texts/                        # Source PDFs (15) — never edit, primary references
audit/                        # Research output — Markdown synthesis documents
  00-INDEX.md                 # Master index with source table + doc links
  01-entity-registry.md       # Non-human actors, hierarchy, across all sources
  02-technology-catalog.md    # Miracles → plausible tech mapping
  03-event-timeline.md        # Unified chronology across all sources
  04-cross-references.md      # Parallel accounts across independent traditions
  05-great-reset.md           # Flood as deliberate sterilization protocol
  06-weapons-doctrine.md      # Weapons authorization hierarchy
  07-the-human-project.md     # Complete arc: creation/management/reset
  08-nephilim-reassessment.md # Nephilim as deliberate transhumanist program
  09-soma-analysis.md         # Soma as controlled substance technology
  10-vedic-weapon-taxonomy.md # Vedic astra weapon classification
  11-timeline-revision.md     # Refined event chronology
  12-nhi-correlation.md       # Non-human intelligence pattern alignment
  analyses/                   # Per-text deep dives (14 files)
scripts/
  validate-links.py           # Cross-reference link validator
```

## Where to look

| Task | Location | Notes |
|------|----------|-------|
| Core methodology | `claude.md` | Read before any analysis work |
| Quick overview | `README.md` | Project premise, scope, architecture |
| Source text list | `audit/00-INDEX.md` | Master index with source table |
| Per-text deep dive | `audit/analyses/` | 14 files, one per source text |
| Cross-cutting synthesis | `audit/` | 12 numbered docs, 00-INDEX through 12-NHI |
| Feature roadmap | `PLAN.md` | Content gaps, infrastructure, expansion |
| Link validation | `scripts/validate-links.py` | `python3 scripts/validate-links.py` |

## Conventions

- **Classification header**: Every document starts with `**Classification:** SPECIES WITH AMNESIA -- Working Hypothesis` and `**Analyst:** The Chronos Archive, Lead Investigator`.
- **Cross-references**: Use relative Markdown links like `[gilgamesh.md](gilgamesh.md)` or `[ezekiel-merkabah.md](ezekiel-merkabah.md)`. When a synthesis document references a per-text analysis, cite it in parentheses as `(source: audit/analyses/popol-vuh.md)`.
- **Section style**: Top-level `##`, subsections `###`, tables for structured data (entity comparisons, event tables, technology entries). Use blockquotes for source text excerpts. Keep source attribution explicit.
- **Source texts**: PDFs in `texts/` are primary references — never modify. Reference them by title and page count in your analysis.
- **Adding a new source**: Place the PDF in `texts/`, create a per-text analysis in `audit/analyses/`, then update `00-INDEX.md` with the new entry and integrate into the relevant synthesis documents (entity registry, technology catalog, timeline, cross-references).

## Workflow for new analysis

1. Read the source PDF (in `texts/`) — each is a complete public-domain translation.
2. Read `claude.md` to internalize the framework.
3. Read the existing analysis for the closest comparable text to match style and depth.
4. Write the per-text analysis in `audit/analyses/` following the established format: Executive Summary with numbered findings, then Incident-by-incident breakdown with tables.
5. Update the relevant cross-cutting synthesis documents (entity registry, technology catalog, event timeline, cross-references) if the new source contributes new material.
6. Update `00-INDEX.md` (source table + audit documents table).

## Research framework summary

- **Literalism Over Metaphor**: "gods" = non-human operators, "miracles" = technology, "heaven" = orbital platform.
- **Reverse-Engineering**: Translate archaic vocabulary into modern equivalents (e.g., "chariot of fire" = aerospace vehicle).
- **Amnesia Filter**: Witnesses lacked vocabulary for advanced technology — analyze their descriptions as if written by a non-technical observer.
- **Cross-source convergence**: Parallel accounts in geographically/temporally separated traditions strengthen credibility.

## Notes

- `.sisyphus/` and `.obsidian/` are local tooling directories — not part of research content.
- PDF filenames in `texts/` vary in convention (mixed casing, abbreviations); the INDEX table disambiguates them.
