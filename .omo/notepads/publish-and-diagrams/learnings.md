## 2026-06-13 Wave 1 Initial Setup
- Astro 4.16.19 installed successfully
- Content collections use `glob` loader from `astro/loaders` (Astro 4.x content layer) pointing at `audit/` directory
- Exclusions handled at query time (not in loader pattern) because `glob` only accepts string patterns
- BaseLayout: dark theme (#0d1117 bg), Mermaid CDN v10, system font stack
- Sidebar: 14 Syntheses + 14 Analyses, mobile collapse via hamburger
- PLAN.md updated: Phases 1-4 COMPLETED, 5 IN PROGRESS, 6 DEFERRED, 7 CURRENT, 8-9 added
- Parallel execution of Tasks 1, 2, 3, 5 was successful — all completed in ~5 min
- Task 2 and Task 3 had overlapping scope (both created layout/sidebar) but converged cleanly
