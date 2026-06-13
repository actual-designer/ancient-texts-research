/**
 * rewrite-html-links — Post-processes rendered HTML to rewrite .md links.
 *
 * The content layer (experimental.contentLayer) renders markdown to HTML
 * without applying Astro's configured remark plugins. This function catches
 * `.md` links that survived rendering and rewrites them to clean directory URLs.
 *
 * Examples:
 *   href="analyses/gilgamesh.md"   → href="/ancient-texts-research/audit/analyses/gilgamesh/"
 *   href="../claude.md"            → href="/ancient-texts-research/claude/"
 *   href="01-entity-registry.md"   → href="/ancient-texts-research/audit/01-entity-registry/"
 *
 * @param {string} html - Rendered HTML from the content layer
 * @param {string} entryId - Entry ID from content collection (e.g. "01-entity-registry.md", "analyses/gilgamesh.md")
 * @returns {string} HTML with all .md links rewritten
 */
export function rewriteMdLinks(html, entryId) {
  // Derive the source directory from the entry ID
  // "01-entity-registry.md" → "" (audit root)
  // "analyses/gilgamesh.md" → "analyses"
  const srcRelDir = entryId.includes('/') ? entryId.substring(0, entryId.lastIndexOf('/')) : '';
  const BASE = '/ancient-texts-research';

  return html.replace(
    /href="([^"]*\.md(?:#[^"]*)?)"/g,
    (match, url) => {
      // Skip external / special protocols
      if (/^(https?:|mailto:|tel:|#)/.test(url)) return match;

      // Separate anchor fragment
      let anchor = '';
      const hashIdx = url.indexOf('#');
      if (hashIdx !== -1) {
        anchor = url.slice(hashIdx);
        url = url.slice(0, hashIdx);
      }

      // Strip .md extension
      url = url.replace(/\.md$/, '');

      // Resolve relative path based on source location
      let resolved;
      if (url.startsWith('/')) {
        // Root-relative: keep as-is but strip leading slash for joining
        resolved = url;
      } else {
        // Count parent directory hops
        let parts = srcRelDir ? srcRelDir.split('/') : [];
        while (url.startsWith('../')) {
          parts.pop();
          url = url.slice(3);
        }
        // Prepend source directory if not already absolute
        if (parts.length > 0) {
          resolved = '/' + parts.join('/') + '/' + url;
        } else {
          resolved = '/' + url;
        }
      }

      // Normalise slashes
      const cleanPath = resolved.replace(/\/+/g, '/');
      return `href="${BASE}${cleanPath}/${anchor}"`;
    }
  );
}
