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
  // "01-entity-registry.md" → "audit" (audit root — content collection glob is audit/**/*.md)
  // "analyses/gilgamesh.md" → "analyses"
  const srcRelDir = entryId.includes('/')
    ? entryId.substring(0, entryId.lastIndexOf('/'))
    : 'audit';
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

/**
 * extractHeadings — Pull h2/h3 headings (with ids) from rendered HTML for a TOC.
 *
 * rehype-slug already adds `id` attributes to headings during content-layer
 * rendering, so we simply read them here.
 *
 * @param {string} html
 * @returns {{ depth: number, id: string, text: string }[]}
 */
export function extractHeadings(html) {
  const headings = [];
  const re = /<(h[23])\b[^>]*\bid="([^"]+)"[^>]*>([\s\S]*?)<\/\1>/g;
  let m;
  while ((m = re.exec(html)) !== null) {
    const depth = m[1] === 'h2' ? 2 : 3;
    const id = m[2];
    const text = m[3]
      .replace(/<[^>]+>/g, '') // strip inline tags (em, code, anchors)
      .replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&#39;/g, "'")
      .replace(/&quot;/g, '"')
      .trim();
    if (text) headings.push({ depth, id, text });
  }
  return headings;
}

/**
 * Normalize Astro BASE_URL to a path prefix without a trailing slash.
 * @param {string} base
 */
function normalizeBase(base) {
  if (!base || base === '/') return '';
  return base.endsWith('/') ? base.slice(0, -1) : base;
}

/**
 * Rewrite local image src paths so they resolve under Astro's configured base.
 * Markdown should use root-relative paths like `/images/foo.jpg`.
 *
 * @param {string} html
 * @param {string} base - import.meta.env.BASE_URL
 * @returns {string}
 */
export function rewriteAssetPaths(html, base) {
  const baseNorm = normalizeBase(base);

  return html.replace(/\bsrc="([^"]+)"/g, (match, src) => {
    if (/^(https?:|data:|mailto:|tel:|#)/.test(src)) return match;
    if (baseNorm && src.startsWith(`${baseNorm}/`)) return match;

    let path = src;
    if (path.startsWith('/ancient-texts-research/')) {
      path = path.slice('/ancient-texts-research'.length);
    }
    if (!path.startsWith('/')) return match;

    return `src="${baseNorm}${path}"`;
  });
}

/**
 * Wrap markdown-rendered images in semantic figure elements. When an image is
 * immediately followed by an italic caption paragraph, pair them as figcaption.
 *
 * @param {string} html
 * @returns {string}
 */
export function wrapContentFigures(html) {
  let out = html.replace(
    /<p><img([^>]*?)><\/p>\s*<p><em>([\s\S]*?)<\/em><\/p>/g,
    (_match, imgAttrs, caption) =>
      `<figure class="content-figure"><img${imgAttrs}><figcaption>${caption}</figcaption></figure>`
  );

  out = out.replace(
    /<p><img([^>]*?)><\/p>/g,
    (_match, imgAttrs) => `<figure class="content-figure"><img${imgAttrs}></figure>`
  );

  return out;
}

/**
 * enhanceContentHtml — Post-process rendered Markdown HTML:
 *   1. Rewrite local image paths for Astro base URL.
 *   2. Wrap images in contextual <figure> elements.
 *   3. Wrap <table> elements in a horizontally-scrollable container.
 *   4. Append subtle anchor links to headings that carry an id.
 *
 * @param {string} html
 * @param {string} [base='/ancient-texts-research/'] - import.meta.env.BASE_URL
 * @returns {string}
 */
export function enhanceContentHtml(html, base = '/ancient-texts-research/') {
  let out = html;

  out = rewriteAssetPaths(out, base);
  out = wrapContentFigures(out);

  // Wrap tables for responsive horizontal scroll (no nested tables in MD)
  out = out.replace(
    /<table\b([\s\S]*?)<\/table>/g,
    '<div class="table-scroll"><table$1</table></div>'
  );

  // Heading anchor links (only headings that already have an id)
  out = out.replace(
    /<(h[1-4])\b([^>]*\bid="([^"]+)"[^>]*)>([\s\S]*?)<\/\1>/g,
    (_match, tag, attrs, id, inner) =>
      `<${tag}${attrs}>${inner}<a class="heading-anchor" href="#${id}" aria-label="Link to this section">#</a></${tag}>`
  );

  return out;
}
