// @ts-check
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';
import pagefind from 'astro-pagefind';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
	site: 'https://glenzac.github.io',
	integrations: [mdx(), sitemap(), pagefind()],
	vite: {
		plugins: [tailwindcss()],
	},
	markdown: {
		shikiConfig: {
			theme: 'github-dark',
			wrap: true,
		},
	},
	build: {
		format: 'directory',
	},
	image: {
		service: {
			entrypoint: 'astro/assets/services/sharp',
			config: {
				limitInputPixels: false,
			},
		},
	},
});
