import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Content collection for audit/ directory.
 *
 * Loads all .md files under audit/. Exclusions are applied at query time:
 * - audit/verification/**  (QA evidence)
 * - audit/analyses/AGENTS.md  (internal template)
 * See src/pages/index.astro for the exclusion logic.
 */
const audit = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './audit' }),
  schema: z.object({
    title: z.string().optional(),
    description: z.string().optional(),
  }),
});

export const collections = { audit };
