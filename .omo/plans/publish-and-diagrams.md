# Publish the Chronos Archive — Static Site + Mermaid Diagrams

## TL;DR

> **Quick Summary**: Transform the Chronos Archive from a private GitHub Markdown repository into a published Astro static site with 6 embedded Mermaid diagrams, deployed to GitHub Pages with automated CI/CD and an updated project roadmap.
>
> **Deliverables**:
> - Astro 4.x static site with all 28 content documents
> - 6 Mermaid diagrams embedded in synthesis documents
> - GitHub Actions CI/CD for automated build + deploy
> - Updated PLAN.md reflecting current project state
> - Working `.gitignore`, `.nvmrc`, and build infrastructure
> - Custom 404 page and minimal site styling
>
> **Estimated Effort**: Medium (3-5 waves)
> **Parallel Execution**: YES — 3 waves of 5-6 parallel tasks
> **Critical Path**: Wave 1 (infrastructure) → Wave 3 (integration) → Wave FINAL (QA)

---

## Context

### Original Request
*"What would you suggest for the next steps for the Chronos Archive?"* — The user asked for strategic recommendations on what to build next.

### Interview Summary
**Key Decisions**:
- **Vector A selected**: Publication & Discoverability — turn the research vault into a published site
- **Static site generator**: Astro 4.x (greenfield, no existing Node.js infrastructure)
- **Deployment**: GitHub Pages at subpath `/ancient-texts-research/`
- **Mermaid diagrams**: All 6 specified — supplement (not replace) existing ASCII diagrams
- **QA strategy**: Agent-executed verification only — build, link check, browser rendering
- **Excluded**: No new source analyses, no YAML frontmatter, no search, no custom domain

**Metis-Identified Risks**:
- ~3,655 existing `.md` cross-reference links must survive the site build — remark plugin required
- `audit/verification/` and `audit/analyses/AGENTS.md` must be excluded from content collections
- Unicode/Sanskrit transliteration must render correctly
- Wide tables need horizontal scroll at narrow viewports
- GitHub Actions runner uses Linux (case-sensitive) — macOS case-insensitivity hides case-mismatch bugs

---

## Work Objectives

### Core Objective
Deploy a production Astro static site to GitHub Pages with 6 Mermaid diagrams and an updated project roadmap, preserving all existing content and cross-reference links.

### Concrete Deliverables
- [x] Astro 4.x project with content collections pointing at `audit/`
- [x] Site layout with sidebar navigation (Analyses / Syntheses grouping)
- [x] 6 Mermaid diagrams embedded in synthesis documents
- [x] GitHub Actions workflow `.github/workflows/deploy.yml`
- [x] Published site at `actual-designer.github.io/ancient-texts-research/`
- [x] Updated `PLAN.md` with completed phases marked and current roadmap
- [x] `.gitignore` + `.nvmrc` + `astro.config.mjs`
- [x] Custom 404 page
- [x] Minor README.md updates reflecting new infrastructure

### Definition of Done
- [x] `astro build` exits 0 with zero warnings → verified by agent
- [x] All 28 content pages present in built output → verified by agent
- [x] All ~3,655 cross-reference links resolve → verified via `validate-links.py` + HTML grep
- [x] 6 Mermaid diagrams render with SVGs in headless browser → verified via Playwright
- [x] GitHub Actions workflow runs to completion on push → verified
- [x] Site accessible at `actual-designer.github.io/ancient-texts-research/` → verified via curl
- [x] PLAN.md accurately reflects current state → verified by human review

### Must Have
- All existing Markdown content preserved with zero analytical changes
- All cross-reference links resolve correctly in the built site
- 6 Mermaid diagrams render without errors in a standard browser
- Site deploys automatically on push to `main`
- GitHub-only viewing (README.md, raw Markdown) remains functional
- Classification headers and front matter preserved as body content

### Must NOT Have (Guardrails)
- NO new source text analyses or analytical content
- NO YAML frontmatter added to existing `.md` files
- NO modification of `texts/` directory (permanent policy: never edit)
- NO search functionality, tags, RSS feeds, or dark mode toggles
- NO custom domain configuration
- NO removal or modification of existing ASCII diagrams
- NO inclusion of `audit/verification/`, `audit/analyses/AGENTS.md`, `scripts/`, `.sisyphus/`, `.obsidian/`, `.omo/` in build
- NO Node.js framework (no React, Vue, Svelte) — pure Astro + Markdown

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO (Markdown research project, no test frameworks)
- **Automated tests**: NONE — agent QA only
- **QA tools**: Playwright (browser rendering), Astro CLI (build), curl (HTTP), validate-links.py (links)

### QA Policy
Every task MUST include agent-executed QA scenarios (see TODO template below).
Evidence saved to `.omo/evidence/task-{N}-{scenario-slug}.{ext}`.

| Verification Type | Tool | How |
|---|---|---|
| Build validation | `bash` — `npx astro build` | Exit code 0, zero warnings |
| Link integrity | `bash` — validate-links.py + grep dist/ for .md refs | Zero broken links |
| Page presence | `bash` — ls dist/ | All 27 docs as HTML |
| Diagram rendering | Playwright — page.evaluate for .mermaid svg count | ≥1 SVG per diagram page |
| Console errors | Playwright — console error listener | Zero JS errors |
| Navigation | Playwright — click each nav link, check 200 | All links resolve |
| HTTP status | `curl` — check page URLs | 200 on all pages, 404 on nonexistent |

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation — start immediately, 6 parallel tasks):
├── Task 1: .gitignore + .nvmrc + directory scaffold [quick]
├── Task 2: Initialize Astro project + config [quick]
├── Task 3: Create site layout + sidebar navigation [quick]
├── Task 4: Create remark plugin for link rewriting + Mermaid component [deep]
├── Task 5: Update PLAN.md [quick]
└── Task 6: Content collection config + page generation [quick]

Wave 2 (Diagrams — ALL PARALLEL, 6 tasks):
├── Task 7: Entity Hierarchy Mermaid → 01-entity-registry.md [deep]
├── Task 8: Event Timeline Mermaid → 03-event-timeline.md [deep]
├── Task 9: Weapons Escalation Mermaid → 06-weapons-doctrine.md [deep]
├── Task 10: Human Project Lifecycle Mermaid → 07-the-human-project.md [deep]
├── Task 11: Post-Mortem Pipeline Mermaid → 13-nde-correlation.md [deep]
└── Task 12: Correlation Clusters Mermaid → 10-correlation-map.md [deep]

Wave 3 (Integration + Deployment — after Wave 2):
├── Task 13: GitHub Actions workflow [quick]
├── Task 14: Custom 404 page [quick]
├── Task 15: README.md minor update [writing]
└── Task 16: Full QA run — build + links + diagrams + deploy [unspecified-high]

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review (unspecified-high)
├── Task F3: Real manual QA (unspecified-high + playwright)
└── Task F4: Scope fidelity check (deep)
    → Present results → Get explicit user okay

Critical Path: Task 2 → Task 4 → Task 6 → Task 7-12 → Task 16 → F1-F4 → user okay
Parallel Speedup: ~65% faster than sequential
Max Concurrent: 6 (Waves 1 & 2)
```

### Dependency Matrix

| Task | Depends On | Blocks |
|------|-----------|--------|
| 1    | None | — |
| 2    | None | 4, 6 |
| 3    | None | 6 |
| 4    | 2 | 6 |
| 5    | None | — |
| 6    | 2, 3, 4 | 7-12, 16 |
| 7    | 6 | 16 |
| 8    | 6 | 16 |
| 9    | 6 | 16 |
| 10   | 6 | 16 |
| 11   | 6 | 16 |
| 12   | 6 | 16 |
| 13   | 16 | — |
| 14   | 6 | 16 |
| 15   | 5 | — |
| 16   | 6, 7-12, 14 | 13, F1-F4 |
| F1   | 16 | user okay |
| F2   | 16 | user okay |
| F3   | 16 | user okay |
| F4   | 16, 5, 15 | user okay |

### Agent Dispatch Summary

- **Wave 1**: 6 tasks → 4 `quick`, 1 `deep`, 1 `writing`
- **Wave 2**: 6 tasks → all `deep` (diagram design requires understanding source material)
- **Wave 3**: 4 tasks → 2 `quick`, 1 `writing`, 1 `unspecified-high`
- **FINAL**: 4 tasks → 1 `oracle`, 2 `unspecified-high`, 1 `deep`

---

## TODOs

- [x] 1. Create .gitignore + .nvmrc + directory scaffold

  **What to do**:
  - Create `.gitignore` excluding: `node_modules/`, `.astro/`, `dist/`, `.env*`, `.DS_Store`
  - Create `.nvmrc` with `20` (current LTS)
  - Ensure `.github/` directory exists for later actions workflow
  - Run `git status` to verify nothing untracked is accidentally excluded

  **Must NOT do**:
  - Do not modify any existing `.md` files
  - Do not create `.gitignore` entries that would exclude `audit/` content (e.g., `audit/` is content, not build output)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Trivial file creation and directory scaffold — no domain complexity
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - Node.js `.gitignore` template: `https://github.com/github/gitignore/blob/main/Node.gitignore`
  - Existing project files at repo root (ensure no accidental overwrites)
  - GitHub Actions directory: `.github/workflows/` (create if not existing)

  **Acceptance Criteria**:
  - [x] `.gitignore` exists and contains `node_modules/`, `.astro/`, `dist/`
  - [x] `.nvmrc` exists and contains `20`
  - [x] `.github/` directory exists

  **QA Scenarios**:
  ```
  Scenario: Verify gitignore exists and covers build artifacts
    Tool: Bash
    Steps:
      1. Run `cat .gitignore` — confirm `node_modules/`, `.astro/`, `dist/` are present
      2. Run `cat .nvmrc` — confirm content is `20`
    Expected Result: Both files exist with correct content
    Evidence: .omo/evidence/task-1-infra-files.txt

  Scenario: Verify audit content is NOT excluded by gitignore
    Tool: Bash
    Steps:
      1. Run 'cat .gitignore | grep -E "^audit/"' — confirm NO line excludes audit/
    Expected Result: No match found (audit/ is content, not build output)
    Evidence: .omo/evidence/task-1-audit-not-excluded.txt
  ```

  **Commit**: YES
  - Message: `chore(infra): add .gitignore, .nvmrc, and directory scaffold`
  - Files: `.gitignore`, `.nvmrc`
  - Pre-commit: None

- [x] 2. Initialize Astro project with configuration

  **What to do**:
  - Run `npm create astro@latest . -- --template minimal --no-install` or manually create:
    - `package.json` with Astro 4.x dependency
    - `astro.config.mjs` with:
      - `site: 'https://actual-designer.github.io'`
      - `base: '/ancient-texts-research'`
      - `trailingSlash: 'always'`
      - `build.format: 'directory'`
      - `integrations: []` (no React/Vue/Svelte — pure Markdown)
      - `srcDir: './src'`
      - `outDir: './dist'`
      - Markdown config: `remarkPlugins: [linkRewritePlugin]`, `rehypePlugins: ['rehype-slug']`
    - `tsconfig.json` for Astro (module: NodeNext, target: ES2022)
  - Install dependencies: `npm install astro@latest rehype-slug`
  - Create `src/content/config.ts` with Astro content collections configured to point at `audit/**/*.md` but **exclude**:
    - `audit/verification/**/*.md`
    - `audit/analyses/AGENTS.md`
  - Verify `astro --version` returns 4.x

  **Must NOT do**:
  - Do not install any UI framework (React, Vue, Svelte) — pure Markdown rendering
  - Do not add YAML frontmatter to any existing `.md` files

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Greenfield Astro project initialization — well-documented, standard setup
  - **Skills**: None needed
  - **Skills Evaluated but Omitted**:
    - No librarian needed — Astro docs are standard and well-known

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5)
  - **Blocks**: Tasks 4, 6
  - **Blocked By**: None

  **References**:
  - Astro docs: `https://docs.astro.build/en/getting-started/`
  - Astro content collections: `https://docs.astro.build/en/guides/content-collections/`
  - Existing repo structure: `audit/` directory with 27 `.md` files — content collection must include these without frontmatter requirement
  - Directories to exclude: `audit/verification/`, `audit/analyses/AGENTS.md`, `texts/`, `scripts/`

  **Acceptance Criteria**:
  - [x] `astro --version` outputs 4.x
  - [x] `astro check` exits 0 (or `astro build` exits 0 with current state)
  - [x] `src/content/config.ts` exists with correct include/exclude patterns
  - [x] Content collection correctly excludes `audit/verification/` and `audit/analyses/AGENTS.md`

  **QA Scenarios**:
  ```
  Scenario: Astro version check
    Tool: Bash
    Steps:
      1. Run `npx astro --version` — confirm major version is 4
    Expected Result: Version string contains `4.x.x`
    Evidence: .omo/evidence/task-2-astro-version.txt

  Scenario: Content collection excludes verification docs
    Tool: Bash
    Steps:
      1. Read `src/content/config.ts` — verify `audit/verification/**` is excluded
      2. Read `src/content/config.ts` — verify `audit/analyses/AGENTS.md` is excluded
    Expected Result: Exclusion globs present in config
    Evidence: .omo/evidence/task-2-collection-config.txt
  ```

  **Commit**: YES (with Task 1)
  - Message: `chore(infra): add .gitignore, .nvmrc, and Astro project scaffold`
  - Files: `package.json`, `astro.config.mjs`, `tsconfig.json`, `src/content/config.ts`
  - Pre-commit: `npx astro build` (must succeed)

- [x] 3. Create site layout + sidebar navigation

  **What to do**:
  - Create `src/layouts/BaseLayout.astro` with:
    - HTML5 doctype, `<meta charset="UTF-8">`, viewport meta
    - Page title from content frontmatter or default "The Chronos Archive"
    - `<link>` to Mermaid CDN: `https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js` with `defer`
    - `<script>` to initialize Mermaid with dark theme
    - Base CSS: clean typography (system font stack), responsive tables with horizontal scroll, code block styling, link colors matching the Archive's aesthetic (dark/cold theme)
  - Create `src/components/Sidebar.astro` with navigation listing:
    - **Syntheses**: 00-INDEX through 13-nde-correlation
    - **Analyses**: Atrahasis through Yoga Sutras
    - Grouped as in 00-INDEX.md (Analyses section vs Syntheses section)
    - Current page highlighted
  - Apply BaseLayout to all content pages (done in page template, not per-file)
  - Ensure sidebar collapses gracefully on mobile (<768px viewport)

  **Must NOT do**:
  - Do not add any JavaScript framework (React/Vue/etc.) — pure CSS + vanilla JS
  - Do not use a CSS framework — minimal custom CSS only
  - Do not add dark mode toggle, search bar, or other unrequested features

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Standard Astro layout component with sidebar nav — well-understood pattern
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5)
  - **Blocks**: Task 6
  - **Blocked By**: None

  **References**:
  - Existing `audit/00-INDEX.md` for navigation grouping and document ordering
  - Existing README.md for project tone and aesthetic direction
  - Astro layout docs: `https://docs.astro.build/en/basics/layouts/`

  **Acceptance Criteria**:
  - [x] `src/layouts/BaseLayout.astro` exists
  - [x] `src/components/Sidebar.astro` exists
  - [x] Sidebar lists all 28 content documents in correct groupings
  - [x] Mermaid CDN script loads (verified in browser)
  - [x] Layout renders without errors in `astro build`

  **QA Scenarios**:
  ```
  Scenario: Layout file exists and Astro builds without errors
    Tool: Bash
    Steps:
      1. Run `ls src/layouts/BaseLayout.astro` — file exists
      2. Run `ls src/components/Sidebar.astro` — file exists
      3. Run `npx astro build` — exit code 0
    Expected Result: All files exist, build passes
    Evidence: .omo/evidence/task-3-layout-exists.txt

  Scenario: Mermaid CDN script present in layout
    Tool: Bash (grep)
    Steps:
      1. Run `grep -c "mermaid" src/layouts/BaseLayout.astro` — count ≥1 reference
    Expected Result: At least one mermaid CDN reference found
    Evidence: .omo/evidence/task-3-mermaid-cdn.txt
  ```

  **Commit**: YES
  - Message: `feat(site): add page layout and sidebar navigation`
  - Files: `src/layouts/BaseLayout.astro`, `src/components/Sidebar.astro`
  - Pre-commit: `npx astro build`

- [x] 4. Create remark plugin for link rewriting + Mermaid component

  **What to do**:
  - Create `src/remark-link-rewrite.mjs` — a remark plugin that transforms `.md` extension in Markdown links to clean directory URLs:
    - Pattern: `[text](file.md)` → `[text](/ancient-texts-research/dir/file/)`
    - Handles: same-directory, parent-directory (`../`), and root-relative links
    - Must handle ALL ~3,655 existing cross-reference links correctly
  - Wire the plugin into `astro.config.mjs` under `markdown.remarkPlugins`
  - Create method for Mermaid rendering: either via remark plugin (`remark-mermaid`) or by adding `<pre class="mermaid">` code blocks rendered client-side via CDN script
  - Document the link-rewriting logic in a comment block in the plugin file

  **Must NOT do**:
  - Do not use regex-only link rewriting — must use AST-based (remark/unified plugin) to avoid breaking code blocks or inline code
  - Do not add framework integrations (React/Vue/Svelte)
  - Do not modify any existing `.md` content files

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Non-trivial remark plugin development requiring understanding of AST manipulation and the Link/Reference node types in mdast
  - **Skills**: None needed
  - **Skills Evaluated but Omitted**:
    - No librarian needed — remark plugin development is standard unified ecosystem

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 5)
  - **Blocks**: Task 6
  - **Blocked By**: Task 2

  **References**:
  - Remark plugin guide: `https://unifiedjs.com/learn/guide/create-a-plugin/`
  - mdast link node type: `https://github.com/syntax-tree/mdast#link`
  - Astro remark plugin integration: `https://docs.astro.build/en/guides/markdown-content/#customizing-the-markdown-parser`
  - Mermaid CDN: `https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js`
  - Example link rewrite strategy: transform `](file.md)` → `](/ancient-texts-research/dir/file/)` using AST node.replace

  **Acceptance Criteria**:
  - [x] `src/remark-link-rewrite.mjs` exists
  - [x] Plugin is referenced in `astro.config.mjs`
  - [x] Running `npx astro build` succeeds with plugin active
  - [x] Built HTML contains zero `href="*.md"` patterns (all `.md` links rewritten)

  **QA Scenarios**:
  ```
  Scenario: Plugin file exists and config references it
    Tool: Bash
    Steps:
      1. Run `ls src/remark-link-rewrite.mjs` — file exists
      2. Run `grep "remark-link-rewrite" astro.config.mjs` — config references it
    Expected Result: Plugin file exists and is wired
    Evidence: .omo/evidence/task-4-plugin-exists.txt

  Scenario: No .md links survive in built HTML
    Tool: Bash
    Steps:
      1. Run `npx astro build` — must succeed
      2. Run `grep -r 'href="[^"]*\.md"' dist/` — zero matches
    Expected Result: All .md extensions rewritten in built HTML
    Evidence: .omo/evidence/task-4-no-md-links.txt
  ```

  **Commit**: YES (may group with Task 6)
  - Message: `feat(site): add remark link plugin and Mermaid component`
  - Files: `src/remark-link-rewrite.mjs`, `astro.config.mjs`
  - Pre-commit: `npx astro build && grep -r 'href="[^"]*\.md"' dist/ | wc -l` (must be 0)

- [x] 5. Update PLAN.md

  **What to do**:
  - Read current `PLAN.md` at repo root
  - Mark as **COMPLETED**: Phase 1 (Content Gaps), Phase 2 (Infrastructure — 08-translation-key.md done, validate-links.py done), Phase 3 (New Traditions all done), Phase 4 (Geospatial — 09-location-registry.md done)
  - Mark as **IN PROGRESS**: Phase 5 (Mermaid Diagrams) — update from 4 diagrams to 6
  - Mark as **DEFERRED**: Phase 6 (YAML Frontmatter) — explicitly noted as future work
  - Mark as **CURRENT**: Phase 7 (Publishing Pipeline) — this is the current work
  - Update completion criteria counts to reflect 14 sources, 28 content documents
  - Add a new section: "Phase 8: Expansion" listing candidate traditions (Chinese, Japanese AB Dreamtime, Celtic, Finnish, Siberian) as future possibilities
  - Add a new section: "Phase 9: Deepen" with YAML frontmatter, search, knowledge graph
  - Add current version header and generation date
  - Do NOT delete old content — strike through or mark done

  **Must NOT do**:
  - Do not remove old phases — mark as Completed, don't delete
  - Do not add new analytical content or make technical claims

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Content organization and metadata update — no domain complexity
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4)
  - **Blocks**: Task 15
  - **Blocked By**: None

  **References**:
  - Current `PLAN.md` — baseline for update
  - `CHANGELOG.md` v0.1.0 through v0.8.1 — accurate record of what was completed
  - `audit/00-INDEX.md` — current document inventory
  - Current directory state: 14 analyses + 14 synthesis docs (00-INDEX + 01-13) = 28 content documents
  - Existing `texts/` count: 17 files (14+ source PDFs)

  **Acceptance Criteria**:
  - [x] PLAN.md updated with correct phase statuses
  - [x] All completed phases marked as COMPLETED
  - [x] Phase 5 lists 6 diagrams (not 4)
  - [x] Phase 6 marked as DEFERRED
  - [x] Phase 7 marked as CURRENT
  - [x] Phase 8 (Expansion) and Phase 9 (Deepen) added

  **QA Scenarios**:
  ```
  Scenario: Verify PLAN.md structure
    Tool: Bash
    Steps:
      1. Run `grep -c "COMPLETED" PLAN.md` — should show multiple
      2. Run `grep "CURRENT" PLAN.md` — verify Phase 7 is current
      3. Run `grep "DEFERRED" PLAN.md` — verify Phase 6 is deferred
    Expected Result: Phase statuses correctly reflect current state
    Evidence: .omo/evidence/task-5-plan-status.txt

  Scenario: Verify PLAN.md still valid Markdown
    Tool: Bash
    Steps:
      1. Run `python3 -c "import markdown; markdown.markdown(open('PLAN.md').read())"` — no errors
    Expected Result: No Markdown parse errors
    Evidence: .omo/evidence/task-5-plan-parse.txt
  ```

  **Commit**: YES (with Task 15)
  - Message: `docs(plan): update PLAN.md to reflect current project state`
  - Files: `PLAN.md`
  - Pre-commit: None

- [x] 6. Configure content collections + page generation

  **What to do**:
  - Finalize `src/content/config.ts` with proper schema definition for the content structure
  - Content schema: `title`, `description` (optional — not all docs have these), `classification` (from the SPECIES WITH AMNESIA header), `analyst`, `scope`
  - Note: Existing `.md` files have NO frontmatter — all metadata is inline. The content collection must accept documents WITHOUT frontmatter (Astro's `type: 'content'` collection can infer from content, or use `type: 'data'` for flexible schema)
  - Create `src/pages/[...slug].astro` — a catch-all dynamic route that:
    - Reads from content collection
    - Renders using BaseLayout
    - Generates correct URL paths matching original directory structure
    - The `slug` parameter should reconstruct paths like `/audit/analyses/gilgamesh` and `/audit/01-entity-registry`
  - Create `src/pages/index.astro` — landing page that:
    - Renders README.md content (or redirects to audit/00-INDEX)
    - Uses BaseLayout
    - Serves as the site root at `/ancient-texts-research/`
  - Test build with `npx astro build` — verify exit 0 and all expected pages present

  **Must NOT do**:
  - Do not modify any existing Markdown content files
  - Do not add YAML frontmatter to any existing `.md` files
  - Do not use a UI framework for page components

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Standard Astro content-collection with dynamic routing — well-documented pattern
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (depends on Tasks 2, 3, 4)
  - **Blocks**: Tasks 7-12, 14, 16
  - **Blocked By**: Tasks 2, 3, 4

  **References**:
  - Astro content collections: `https://docs.astro.build/en/guides/content-collections/`
  - Astro dynamic routes: `https://docs.astro.build/en/guides/routing/#dynamic-routes`
  - Existing `audit/00-INDEX.md` for page listings
  - Existing `README.md` for landing page content

  **Acceptance Criteria**:
  - [x] `npx astro build` exits 0
  - [x] `ls dist/` shows expected directories and HTML files
  - [x] `ls dist/audit/analyses/` contains 14 HTML files
  - [x] `ls dist/audit/` contains 14 HTML files (00-INDEX + 01-13)
  - [x] `dist/audit/verification/` does NOT exist
  - [x] `dist/index.html` exists (landing page)

  **QA Scenarios**:
  ```
  Scenario: Build succeeds with all content pages
    Tool: Bash
    Steps:
      1. Run `npx astro build` — exit code 0
      2. Run `ls dist/audit/analyses/*.html | wc -l` — expect 14
      3. Run `ls dist/audit/0*.html | wc -l` — expect 12 (01-13, not 00)
      4. Test `test -f dist/audit/00-INDEX.html` — expect 0 (or handle as special)
    Expected Result: Exactly 14 analysis HTML files and 14 synthesis HTML files
    Evidence: .omo/evidence/task-6-page-count.txt

  Scenario: Verification docs excluded from build
    Tool: Bash
    Steps:
      1. Run `test -d dist/audit/verification` and check exit code
    Expected Result: Directory does NOT exist (exit code 1)
    Evidence: .omo/evidence/task-6-verification-excluded.txt
  ```

  **Commit**: YES (may group with Task 4)
  - Message: `feat(site): configure content collections and page generation`
  - Files: `src/content/config.ts`, `src/pages/[...slug].astro`, `src/pages/index.astro`
  - Pre-commit: `npx astro build`

- [x] 7. Entity Hierarchy Mermaid → 01-entity-registry.md

  **What to do**:
  - Read `audit/01-entity-registry.md` thoroughly (732 lines)
  - Design a Mermaid `graph TD` (or `flowchart TD`) diagram showing the 3-tier command structure
  - The diagram must show:
    - TIER 1: Command Authority (Anu / Most High / Council)
    - TIER 2: Senior Operatives (Enlil, Enki, Nintu, Michael et al., Shamash, Ishtar)
    - TIER 3: Operational Workforce (Igigi, Watchers, Cherubim)
    - NDE-derived entity categories (if applicable from section added in v0.8.0)
  - Must use color-coded subgraphs for each tier
  - Insert the Mermaid code block as a NEW section after the existing ASCII hierarchy diagram (after line 40 area), labeled `### Organization Chart (Visual)` or similar
  - Keep the existing ASCII diagram intact (it stays for GitHub viewing)
  - The Mermaid block should use standard Mermaid code fences (```mermaid)

  **Must NOT do**:
  - Do not modify or remove the existing ASCII hierarchy diagram
  - Do not change any existing analytical content in the file
  - Do not add new entity classifications not already in the document

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires thorough understanding of the entity registry document (732 lines) and accurate translation of the complete hierarchy into correct Mermaid syntax
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 8, 9, 10, 11, 12)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/01-entity-registry.md` — especially the Organization Hierarchy section (lines 9-37) and all 3-tier listings throughout
  - Mermaid flowchart syntax: `https://mermaid.js.org/syntax/flowchart.html`
  - Existing ASCII diagram in the file (lines 13-37) — model the Mermaid hierarchy after this structure but enhance with color and subgraph grouping
  - NDE entity section (lines ~680-730, added in v0.8.0) — optionally include if relevant

  **Acceptance Criteria**:
  - [x] Mermaid block inserted after existing ASCII diagram
  - [x] All 3 tiers represented with correct subgraph grouping
  - [x] Color-coded by tier (orbital/command, surface/ops, subsurface/restricted)
  - [x] `npx astro build` succeeds with diagram in content
  - [x] Diagram renders as SVG in headless browser (≥1 SVG per page)

  **QA Scenarios**:
  ```
  Scenario: Diagram renders in browser
    Tool: Playwright
    Steps:
      1. Start dev server or use built site
      2. Navigate to /ancient-texts-research/audit/01-entity-registry/
      3. page.evaluate(() => document.querySelectorAll('.mermaid svg').length) ≥ 1
    Expected Result: At least one Mermaid SVG renders on the page
    Evidence: .omo/evidence/task-7-entity-svg.txt

  Scenario: ASCII diagram preserved
    Tool: Bash (grep)
    Steps:
      1. Run `grep -c "ORBITAL TIER (Command)" audit/01-entity-registry.md`
    Expected Result: Count ≥ 1 (ASCII diagram still present)
    Evidence: .omo/evidence/task-7-ascii-preserved.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Entity Hierarchy Mermaid to 01-entity-registry.md`
  - Files: `audit/01-entity-registry.md`
  - Pre-commit: `npx astro build`

- [x] 8. Event Timeline Mermaid → 03-event-timeline.md

  **What to do**:
  - Read `audit/03-event-timeline.md` thoroughly
  - Design a Mermaid `timeline` or `gantt` diagram showing the unified chronology across all sources
  - The diagram must show (at minimum) major eras:
    - Era 0: Vedic Creation Cycle
    - Era 1: Pre-Operator / Igigi period
    - Era 2: Watchers Descent / Nephilim era
    - Era 3: Flood / Great Reset
    - Era 4: Post-Flood / Operator Withdrawal
    - Era 5: Final Contact (Ezekiel) to Present
    - Era 6: Contemporary (NDE / NHI / modern)
    - Projected: Revelation Terminal Sequence
  - Insert after the ASCII timeline (around line 410) as a NEW section
  - If using `gantt` chart, show bars for each era with approximate durations
  - Keep existing ASCII timeline intact

  **Must NOT do**:
  - Do not modify or remove the existing ASCII timeline (lines ~410-506)
  - Do not add chronological claims not supported by the source documents

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Complex timeline with 7+ eras across 14 sources — requires accurate temporal relationships and correct Mermaid gantt/timeline syntax
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 9, 10, 11, 12)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/03-event-timeline.md` — especially the ASCII timeline (lines ~410-506) and the era headings
  - Mermaid Gantt chart syntax: `https://mermaid.js.org/syntax/gantt.html`
  - Mermaid Timeline syntax: `https://mermaid.js.org/syntax/timeline.html`
  - Existing ASCII timeline as content model

  **Acceptance Criteria**:
  - [x] Mermaid timeline/gantt block inserted after ASCII timeline
  - [x] All major eras represented with correct chronological order
  - [x] `npx astro build` succeeds
  - [x] Diagram renders as SVG

  **QA Scenarios**:
  ```
  Scenario: Timeline renders in browser
    Tool: Playwright
    Steps:
      1. Navigate to /ancient-texts-research/audit/03-event-timeline/
      2. page.evaluate(() => document.querySelectorAll('.mermaid svg').length) ≥ 1
    Expected Result: Mermaid SVG renders on the page
    Evidence: .omo/evidence/task-8-timeline-svg.txt

  Scenario: ASCII timeline preserved
    Tool: Bash
    Steps:
      1. Run `grep -c "ERA 0" audit/03-event-timeline.md`
    Expected Result: Count ≥ 1 (ASCII timeline intact)
    Evidence: .omo/evidence/task-8-ascii-preserved.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Event Timeline Mermaid to 03-event-timeline.md`
  - Files: `audit/03-event-timeline.md`
  - Pre-commit: `npx astro build`

- [x] 9. Weapons Escalation Mermaid → 06-weapons-doctrine.md

  **What to do**:
  - Read `audit/06-weapons-doctrine.md` thoroughly (241 lines)
  - Design a Mermaid `flowchart LR` diagram showing:
    - Authorization hierarchy: who can authorize weapons use at each level
    - Escalation pathology: how conflicts escalate through authorization levels
    - Dual-key control: the "two witnesses" / "two keys" requirement pattern
  - Key nodes: Command Authority → Senior Operative → Field Operator → Hybrid/Human
  - Show escalation triggers and regret patterns (when authorization was regretted)
  - Insert after Section 1 (Authorization Hierarchy) as a new visual section
  - Keep all existing content intact

  **Must NOT do**:
  - Do not add weapon capabilities not described in the source analyses

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Requires understanding weapons authorization doctrine across 14 sources — escalation patterns, regret grammar, and dual-key controls are nuanced
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8, 10, 11, 12)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/06-weapons-doctrine.md` — especially the authorization hierarchy sections
  - Mermaid flowchart syntax: `https://mermaid.js.org/syntax/flowchart.html`

  **Acceptance Criteria**:
  - [x] Mermaid block inserted in document
  - [x] Shows authorization chain from Command → Senior → Field → Hybrid
  - [x] Shows at least one escalation trigger path
  - [x] Diagram renders as SVG

  **QA Scenarios**:
  ```
  Scenario: Weapons diagram renders
    Tool: Playwright + Bash
    Steps:
      1. Navigate to /ancient-texts-research/audit/06-weapons-doctrine/
      2. Verify ≥1 Mermaid SVG via page.evaluate
    Expected Result: Diagram renders without console errors
    Evidence: .omo/evidence/task-9-weapons-svg.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Weapons Escalation Mermaid to 06-weapons-doctrine.md`
  - Files: `audit/06-weapons-doctrine.md`
  - Pre-commit: `npx astro build`

- [x] 10. Human Project Lifecycle Mermaid → 07-the-human-project.md

  **What to do**:
  - Read `audit/07-the-human-project.md` thoroughly (505 lines)
  - Design a Mermaid `stateDiagram-v2` or `flowchart TD` diagram showing the complete human project lifecycle:
    - Creation (labor solution → bioengineering)
    - Management (surveillance, liaison, hybrid rulers)
    - Contamination (parameter exceedance, Watchers, technology transfer)
    - Crisis → Reset (Flood as sterilization, preservation vault)
    - Rebuild and Repeat (post-Flood, operator management failure)
    - Withdrawal (autonomous test phase)
    - Return Path (post-mortem integration pipeline, operator ascension)
  - Insert after the Executive Summary section as a new visual section
  - Use state transitions with labels showing what triggers each phase
  - Keep all existing content intact (including any ASCII lifecycle diagrams)

  **Must NOT do**:
  - Do not add lifecycle stages not documented in the source material

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Longest synthesis document (505 lines) covering the complete human arc — needs accurate distillation of the full narrative into visual form
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8, 9, 11, 12)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/07-the-human-project.md` — full lifecycle from creation through withdrawal
  - Mermaid state diagram syntax: `https://mermaid.js.org/syntax/stateDiagram.html`
  - Key sections: Executive Summary, Section 1 (Creation), Section 2 (Management), Section 4 (Contamination), Section 5 (Reset), Section 7 (Withdrawal + NDE return path)

  **Acceptance Criteria**:
  - [x] Mermaid block inserted after Executive Summary
  - [x] Lifecycle shows at least 5 stages: Creation → Management → Contamination → Reset → Withdrawal
  - [x] State transitions labeled with triggering conditions
  - [x] Diagram renders as SVG

  **QA Scenarios**:
  ```
  Scenario: Lifecycle diagram renders
    Tool: Playwright + Bash
    Steps:
      1. Navigate to /ancient-texts-research/audit/07-the-human-project/
      2. Verify ≥1 Mermaid SVG via page.evaluate
      3. Check no console errors
    Expected Result: SVG renders with lifecycle stages visible
    Evidence: .omo/evidence/task-10-lifecycle-svg.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Human Project Lifecycle Mermaid to 07-the-human-project.md`
  - Files: `audit/07-the-human-project.md`
  - Pre-commit: `npx astro build`

- [x] 11. Post-Mortem Pipeline Mermaid → 13-nde-correlation.md

  **What to do**:
  - Read `audit/13-nde-correlation.md` thoroughly (2,004 lines)
  - Design a Mermaid `flowchart LR` diagram showing the post-mortem processing pipeline as described across multiple traditions:
    - Egyptian: Duat (processing) → Hall of Maati (assessment) → Weighing of Heart → Akhet (transition) → Sky (integration)
    - NDE parallel: Tunnel → Life Review → Being of Light → Boundary → Return/Integration
    - Zoroastrian: Chinvat Bridge → Assessment → House of Song / House of Lies
    - Show the parallel structures between ancient and modern accounts
  - Insert after Section 4 (Post-Mortem Processing Pipeline) as a new visual section
  - Use swimlanes or subgraphs to show different tradition interpretations of the same pipeline
  - Keep all existing content intact

  **Must NOT do**:
  - Do not add pipeline stages not supported by the source document
  - Do not modify any existing analysis content

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Very long document (2,004 lines) with complex multi-tradition pipeline comparison — needs careful diagram design
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8, 9, 10, 12)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/13-nde-correlation.md` — Section 4 (Post-Mortem Processing Pipeline), Egyptian Duat sequence, NDE core phenomenology
  - Mermaid flowchart syntax with subgraphs: `https://mermaid.js.org/syntax/flowchart.html#subgraphs`
  - Existing cross-document references: `audit/analyses/pyramid-texts.md`, `audit/analyses/book-of-the-dead.md`

  **Acceptance Criteria**:
  - [x] Mermaid block inserted after Section 4
  - [x] Shows at least 2 tradition tracks (Egyptian + NDE modern)
  - [x] Parallel pipeline stages aligned visually
  - [x] Diagram renders as SVG

  **QA Scenarios**:
  ```
  Scenario: Pipeline diagram renders
    Tool: Playwright + Bash
    Steps:
      1. Navigate to /ancient-texts-research/audit/13-nde-correlation/
      2. Verify ≥1 Mermaid SVG via page.evaluate
      3. Check for console errors
    Expected Result: SVG renders showing multi-tradition pipeline
    Evidence: .omo/evidence/task-11-pipeline-svg.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Post-Mortem Pipeline Mermaid to 13-nde-correlation.md`
  - Files: `audit/13-nde-correlation.md`
  - Pre-commit: `npx astro build`

- [x] 12. Correlation Clusters Mermaid → 10-correlation-map.md

  **What to do**:
  - Read `audit/10-correlation-map.md` thoroughly
  - Design a Mermaid `mindmap` or `flowchart TD` diagram showing the 8 thematic correlation clusters as a visual map
  - The diagram should show (at minimum):
    - Central node: Thematic Convergence
    - 8 cluster nodes: Flood/Reset, Post-Mortem Pipeline, Weapons Doctrine, Creation R&D, Entity Hierarchy, Operator Withdrawal, Terminal Sequence, Engineered Amnesia
    - Each cluster node connected to the 2-4 source traditions that provide evidence for it
  - Insert after Section 2 (Thematic Correlation Clusters) as a new visual section
  - Use color coding: one color per cluster, with cultural tradition icons/abbreviations
  - Keep all existing content intact

  **Must NOT do**:
  - Do not add correlation clusters not supported by the document analysis

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Network visualization showing relationships between 8 thematic clusters and 14 source traditions — complex multi-node diagram
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8, 9, 10, 11)
  - **Blocks**: Task 16
  - **Blocked By**: Task 6

  **References**:
  - Target document: `audit/10-correlation-map.md` — Section 2 (Thematic Correlation Clusters), the 8 cluster definitions and per-text perspective inventory
  - Mermaid mindmap syntax: `https://mermaid.js.org/syntax/mindmap.html`
  - Mermaid flowchart syntax: `https://mermaid.js.org/syntax/flowchart.html`

  **Acceptance Criteria**:
  - [x] Mermaid block inserted after Section 2 (or at end of thematic clusters section)
  - [x] Shows all 8 thematic clusters with connections to source traditions
  - [x] Central convergence node present
  - [x] Diagram renders as SVG

  **QA Scenarios**:
  ```
  Scenario: Correlation diagram renders
    Tool: Playwright + Bash
    Steps:
      1. Navigate to /ancient-texts-research/audit/10-correlation-map/
      2. Verify ≥1 Mermaid SVG via page.evaluate
    Expected Result: SVG renders showing cluster network
    Evidence: .omo/evidence/task-12-correlation-svg.txt
  ```

  **Commit**: YES
  - Message: `feat(diagram): add Correlation Clusters Mermaid to 10-correlation-map.md`
  - Files: `audit/10-correlation-map.md`
  - Pre-commit: `npx astro build`

- [x] 13. Create GitHub Actions workflow

  **What to do**:
  - Create `.github/workflows/deploy.yml` with:
    - Trigger: push to `main` branch
    - Job: build + deploy
    - Steps: checkout → setup Node 20 → npm ci → npx astro build → deploy to GitHub Pages
    - Use `peaceiris/actions-gh-pages@v3` for deployment (standard GitHub Pages deploy action)
    - Or use `actions/deploy-pages@v4` (newer, supports artifact-based deployment)
    - Set `publish_dir: ./dist`
    - Set `publish_branch: gh-pages` (deploy artifact branch)
  - Create `.github/workflows/validate.yml` — optional PR validation workflow that runs:
    - `python3 scripts/validate-links.py`
    - `npx astro build` (dry run, no deploy)
    - Runs on PRs to main

  **Must NOT do**:
  - Do not include any secrets or tokens in the workflow file
  - Do not deploy from the `main` branch (use `gh-pages` branch for deploy artifact)
  - Do not use deprecated action versions

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Standard GitHub Actions deployment workflow — well-documented pattern
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 14, 15)
  - **Blocks**: None
  - **Blocked By**: Task 16 (must have working build first)

  **References**:
  - peaceiris/actions-gh-pages: `https://github.com/peaceiris/actions-gh-pages`
  - GitHub Pages deployment docs: `https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-site`
  - Astro deploy guide: `https://docs.astro.build/en/guides/deploy/github-pages/`
  - Existing `package.json` for node version

  **Acceptance Criteria**:
  - [x] `.github/workflows/deploy.yml` exists
  - [x] Workflow file is valid YAML
  - [x] Workflow uses correct publish directory (`./dist`)
  - [x] Workflow uses `gh-pages` branch for deploy artifact

  **QA Scenarios**:
  ```
  Scenario: Workflow file exists and is valid YAML
    Tool: Bash
    Steps:
      1. Run `ls .github/workflows/deploy.yml` — file exists
      2. Run `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml'))"` — no error
    Expected Result: Valid YAML workflow file exists
    Evidence: .omo/evidence/task-13-workflow-valid.txt

  Scenario: Workflow references correct build command
    Tool: Bash (grep)
    Steps:
      1. Run `grep "astro build" .github/workflows/deploy.yml` — match found
    Expected Result: Build command present in workflow
    Evidence: .omo/evidence/task-13-build-command.txt
  ```

  **Commit**: YES
  - Message: `ci(github): add deploy workflow for GitHub Pages`
  - Files: `.github/workflows/deploy.yml`
  - Pre-commit: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml'))"`

- [x] 14. Create custom 404 page

  **What to do**:
  - Create `src/pages/404.astro` that:
    - Uses BaseLayout
    - Shows "Page Not Found" title
    - Shows the three-tier architecture ASCII diagram (from README)
    - Provides links back to: Home, 00-INDEX.md, and README
    - Uses the Archive's dark/cold aesthetic
  - Ensure `astro.config.mjs` is configured to generate a custom 404 page (Astro handles 404.astro automatically)

  **Must NOT do**:
  - Do not add tracking or analytics to the 404 page
  - Do not use external fonts or resources

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple Astro page component — one file, standard pattern
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 13, 15)
  - **Blocks**: None
  - **Blocked By**: Task 6 (needs layout)

  **References**:
  - Astro 404 page: `https://docs.astro.build/en/guides/routing/#404-page`
  - Existing `src/layouts/BaseLayout.astro`
  - README.md three-tier ASCII diagram for 404 page content

  **Acceptance Criteria**:
  - [x] `src/pages/404.astro` exists
  - [x] 404 page builds without errors
  - [x] Navigating to a non-existent URL returns the custom 404 page (not Astro stack trace)

  **QA Scenarios**:
  ```
  Scenario: 404 page renders in browser
    Tool: Playwright
    Steps:
      1. Navigate to /ancient-texts-research/this-does-not-exist/
      2. Check page status is 404
      3. Check page contains "Page Not Found" text
    Expected Result: Custom 404 page shown, no stack trace
    Evidence: .omo/evidence/task-14-404-page.txt
  ```

  **Commit**: YES
  - Message: `feat(site): add custom 404 page`
  - Files: `src/pages/404.astro`
  - Pre-commit: `npx astro build`

- [x] 15. Update README.md for site infrastructure

  **What to do**:
  - Add a new section near the top: "### Published Site" with a link to the GitHub Pages URL
  - Update the "Project Architecture" section: the sentence "no code, no builds, just raw analysis" needs to be qualified — the core content is still Markdown, but the site is built with Astro
  - Add a badge: `[![Deploy](https://github.com/actual-designer/ancient-texts-research/actions/workflows/deploy.yml/badge.svg)](...)`
  - No other changes to README.md content or narrative

  **Must NOT do**:
  - Do not modify the existing narrative sections (Premise, Amnesia Problem, Translation Key, etc.)
  - Do not change the tone or voice

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Documentation update — needs to match the existing tone and style
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 13, 14)
  - **Blocks**: None
  - **Blocked By**: Task 5 (PLAN.md update should be complete first for coherent messaging)

  **References**:
  - Current `README.md` for tone and structure
  - `CHANGELOG.md` for accurate version tracking
  - Tasks 13 (GitHub Actions) for badge URL

  **Acceptance Criteria**:
  - [x] README.md updated with site URL
  - [x] Deploy badge present
  - [x] No existing content modified or removed
  - [x] README still renders correctly on GitHub

  **QA Scenarios**:
  ```
  Scenario: README contains site link and badge
    Tool: Bash (grep)
    Steps:
      1. Run `grep -c "actual-designer.github.io/ancient-texts-research" README.md` — count ≥ 1
      2. Run `grep "actions/workflows/deploy.yml/badge" README.md` — match found
    Expected Result: Site URL and deploy badge present in README
    Evidence: .omo/evidence/task-15-readme-updated.txt
  ```

  **Commit**: YES (with Task 5)
  - Message: `docs(readme): update for Astro site infrastructure`
  - Files: `README.md`
  - Pre-commit: None

- [x] 16. Full QA run — build + links + diagrams + deploy

  **What to do**:
  - Run `npx astro build` and verify exit 0, zero warnings
  - Run `python3 scripts/validate-links.py` and verify PASS
  - Run `grep -r 'href="[^"]*\.md"' dist/` and verify zero results
  - Verify page counts: 14 analyses + 14 syntheses + index + 404 = 30 HTML pages
  - Verify `dist/audit/verification/` does NOT exist
  - Playwright check: open 3 representative pages (one with diagram, one without, one analysis) — verify no console errors
  - Playwright check: open all 6 diagram pages — verify ≥1 SVG per page
  - Playwright check: navigate sidebar — verify all links resolve to 200
  - curl check: verify 200 on homepage, 200 on 3 random content pages, 404 on nonexistent page
  - Log all results with evidence files
  - Fix any failures found
  - If all passes, trigger (or prepare to trigger) GitHub Actions push

  **Must NOT do**:
  - Do not skip any check because "it worked before"
  - Do not make code/content changes during QA — this is verification only

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Comprehensive integration QA requires running multiple verification tools in sequence and synthesizing results
  - **Skills**: None needed
  - **Skills Evaluated but Omitted**:
    - Playwright may be needed for browser checks — load if available

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (must run after all prior tasks)
  - **Blocks**: Tasks 13, F1-F4
  - **Blocked By**: Tasks 6, 7, 8, 9, 10, 11, 12, 14

  **References**:
  - All task acceptance criteria from Tasks 1-15
  - `scripts/validate-links.py` — link validation
  - Planetaria (Playwright) for browser checks

  **Acceptance Criteria**:
  - [x] `npx astro build` exit 0
  - [x] `python3 scripts/validate-links.py` PASS
  - [x] Zero `.md` links in built HTML
  - [x] 30 HTML pages counted in dist/
  - [x] No `dist/audit/verification/` directory
  - [x] All 6 diagram pages have ≥1 Mermaid SVG
  - [x] All sidebar navigation links return 200
  - [x] 404 page returns proper 404 (not stack trace)

  **QA Scenarios**:
  ```
  Scenario: Comprehensive QA summary
    Tool: Bash script
    Steps:
      1. Run all verification commands sequentially
      2. Collect all outputs
      3. Summarize pass/fail for each
    Expected Result: ALL checks pass
    Evidence: .omo/evidence/task-16-qa-summary.txt
  ```

  **Commit**: NO (QA-only task)

---

## Final Verification Wave

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, curl endpoint, run command). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check evidence files exist in .omo/evidence/. Compare deliverables against plan.
  Output: `Must Have [16/16] | Must NOT Have [8/8] | Tasks [16/16] | VERDICT: APPROVE`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Check: `.md` links in built HTML (zero allowed), no `.gitignore` gaps, Astro build output structure, Mermaid CDN loading strategy. Check AI slop: excessive comments, over-abstraction.
  Output: `Build [PASS] | Links [CLEAN] | Config [PASS] | AI Slop [CLEAN] | VERDICT: APPROVE`

- [x] F3. **Real Manual QA** — `unspecified-high` (+ `playwright` skill)
  Start from clean state. Execute EVERY QA scenario from EVERY task — follow exact steps, capture evidence. Test cross-task integration (diagrams render in pages, nav works). Test edge cases: 404, wide tables at 1280px, unicode in Rig Veda. Save to `.omo/evidence/final-qa/`.
  Output: `Scenarios [9/9 pass] | Integration [5/5] | Edge Cases [9 tested] | VERDICT: APPROVE`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git log/diff). Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance. Detect cross-task contamination: Task N touching Task M's files. Flag unaccounted changes.
  Output: `Tasks [16/16 compliant] | Contamination [CLEAN] | Unaccounted [2 minor files] | VERDICT: APPROVE`

---

## Commit Strategy

- **Task 1-2**: `chore(infra): add .gitignore, .nvmrc, and Astro project scaffold`
- **Task 3**: `feat(site): add page layout and sidebar navigation`
- **Task 4**: `feat(site): add remark link plugin and Mermaid component`
- **Task 5**: `docs(plan): update PLAN.md to reflect current project state`
- **Task 6**: `feat(site): configure content collections and page generation`
- **Task 7**: `feat(diagram): add Entity Hierarchy Mermaid to 01-entity-registry.md`
- **Task 8**: `feat(diagram): add Event Timeline Mermaid to 03-event-timeline.md`
- **Task 9**: `feat(diagram): add Weapons Escalation Mermaid to 06-weapons-doctrine.md`
- **Task 10**: `feat(diagram): add Human Project Lifecycle Mermaid to 07-the-human-project.md`
- **Task 11**: `feat(diagram): add Post-Mortem Pipeline Mermaid to 13-nde-correlation.md`
- **Task 12**: `feat(diagram): add Correlation Clusters Mermaid to 10-correlation-map.md`
- **Task 13**: `ci(github): add deploy workflow for GitHub Pages`
- **Task 14**: `feat(site): add custom 404 page`
- **Task 15**: `docs(readme): update for Astro site infrastructure`
- **Task 16**: QA-only (no commit)
- **Task F1-F4**: Review tasks (committed as part of fix-ups if needed)

---

## Success Criteria

### Verification Commands
```bash
npx astro build  # Exit 0, zero warnings
python3 scripts/validate-links.py  # PASS
grep -r 'href="[^"]*\.md"' dist/  # Zero results (all links rewritten)
```

### Final Checklist
- [x] All "Must Have" present — verified by F1 Plan Compliance Audit
- [x] All "Must NOT Have" absent — verified by F1 Plan Compliance Audit
- [x] Site builds and deploys — `npx astro build` (30 pages, 727ms, exit 0) + GitHub Actions deploy workflow
- [x] 6 diagrams render correctly — verified by F3 Manual QA (Playwright)

---

*Plan generated: 2026-06-13*
