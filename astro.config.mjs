import { defineConfig } from 'astro/config';
import remarkLinkRewrite from './src/remark-link-rewrite.mjs';

// https://astro.build/config
export default defineConfig({
  site: 'https://actual-designer.github.io',
  base: '/ancient-texts-research',
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  experimental: {
    contentLayer: true,
  },
  integrations: [],
  srcDir: './src',
  outDir: './dist',
  markdown: {
    remarkPlugins: [remarkLinkRewrite],
    rehypePlugins: ['rehype-slug'],
    shikiConfig: {
      // Dual themes: emit both palettes as CSS variables so code blocks
      // follow the site's light/dark theme (see src/styles/global.css).
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      defaultColor: false,
      wrap: false,
    },
  },
});
