import { defineConfig } from 'astro/config';

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
    remarkPlugins: [],
    rehypePlugins: [],
  },
});
