/**
 * remark-link-rewrite — AST-based .md link rewriter for clean directory URLs.
 *
 * Transforms Markdown link URLs ending in `.md` (including those with
 * anchor fragments) into clean directory-style absolute URLs.
 *
 * Examples:
 *   [text](file.md)            → /ancient-texts-research/dir/file/
 *   [text](../other.md)        → /ancient-texts-research/other/
 *   [text](analyses/m.md)      → /ancient-texts-research/dir/analyses/m/
 *   [text](file.md#section)    → /ancient-texts-research/dir/file/#section
 *   [text](/abs/path/file.md)  → /ancient-texts-research/abs/path/file/
 *
 * Uses mdast AST traversal (visit on 'link' nodes) so code blocks,
 * inline code, and non-link contexts are never touched.
 */

import { visit } from 'unist-util-visit';
import path from 'node:path';

const BASE = '/ancient-texts-research';

/** @type {import('unified').Plugin} */
export default function remarkLinkRewrite() {
  return (tree, file) => {
    const srcDir = path.dirname(file.path);
    const rootDir = file.cwd || process.cwd();

    visit(tree, 'link', (node) => {
      let url = node.url;

      // --- Skip non-.md links ------------------------------------------------
      // Must end with .md or have .md# (anchor on a .md file)
      if (!url.endsWith('.md') && !/\.md#/.test(url)) {
        return;
      }

      // Skip absolute external URLs, mailto:, tel:, and anchor-only links
      if (/^(https?:|mailto:|tel:|#)/.test(url)) {
        return;
      }

      // --- Separate anchor fragment ------------------------------------------
      let anchor = '';
      const hashIdx = url.indexOf('#');
      if (hashIdx !== -1) {
        anchor = url.slice(hashIdx);
        url = url.slice(0, hashIdx);
      }

      // --- Strip .md extension ------------------------------------------------
      url = url.replace(/\.md$/, '');

      // --- Resolve relative / root-relative path ------------------------------
      let relPath;
      if (url.startsWith('/')) {
        // Root-relative: strip leading slash, treat as relative to rootDir
        relPath = url.slice(1);
      } else {
        // Relative: resolve from source file directory
        const absPath = path.resolve(srcDir, url);
        relPath = path.relative(rootDir, absPath);
      }

      // Normalise path separators for URLs
      const cleanPath = relPath.split(path.sep).join('/');

      // --- Build final URL ----------------------------------------------------
      node.url = `${BASE}/${cleanPath}/${anchor}`;
    });
  };
}
