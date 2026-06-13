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
  },
});
