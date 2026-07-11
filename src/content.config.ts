import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
	loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) => z.object({
		title: z.string(),
		date: z.coerce.date(),
		updated: z.coerce.date().optional(),
		author: z.string().optional().default('glenzac'),
		categories: z.array(z.string()).optional().default([]),
		tags: z.array(z.string()).optional().default([]),
		cover: z.object({
			image: image(),
			alt: z.string().optional(),
		}).optional(),
		draft: z.union([z.boolean(), z.string()]).optional().transform(val => {
			if (typeof val === 'string') return val === 'true';
			return val ?? false;
		}),
		summary: z.string().optional(),
		description: z.string().optional(),
	}),
});

const pages = defineCollection({
	loader: glob({ base: './src/content/pages', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		date: z.coerce.date().optional(),
		author: z.string().optional().default('glenzac'),
		draft: z.union([z.boolean(), z.string()]).optional().transform(val => {
			if (typeof val === 'string') return val === 'true';
			return val ?? false;
		}),
	}),
});

export const collections = { posts, pages };
