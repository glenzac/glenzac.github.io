import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import MarkdownIt from 'markdown-it';
import sanitizeHtml from 'sanitize-html';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';
import { postSlug } from '../utils/postSlug';

const parser = new MarkdownIt({ html: true });

// Map `@assets/...` markdown image references to their final built URLs.
const assetModules = import.meta.glob(
	'../assets/**/*.{png,jpg,jpeg,gif,webp,svg,avif}',
	{ eager: true }
);

function renderPostHtml(post, site) {
	// MDX posts use imports/components that markdown-it can't render;
	// fall back to the summary for those.
	if (post.filePath?.endsWith('.mdx')) {
		return post.data.summary || post.data.description || '';
	}

	let html = parser.render(post.body ?? '');

	// Resolve @assets/ references (img src and links to images) to built asset URLs.
	html = html.replace(/(src|href)="@assets\/([^"]+)"/g, (match, attr, path) => {
		const mod = assetModules[`../assets/${path}`];
		return mod ? `${attr}="${new URL(mod.default.src, site).href}"` : match;
	});

	// Make root-relative URLs absolute so feed readers resolve them.
	html = html
		.replace(/src="\/(?!\/)/g, `src="${site}`)
		.replace(/href="\/(?!\/)/g, `href="${site}`);

	return sanitizeHtml(html, {
		allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
		allowedAttributes: {
			...sanitizeHtml.defaults.allowedAttributes,
			img: ['src', 'alt', 'title'],
		},
	});
}

export async function GET(context) {
	const site = context.site.href;
	const posts = await getCollection('posts', ({ data }) => !data.draft);
	posts.sort((a, b) => new Date(b.data.date).valueOf() - new Date(a.data.date).valueOf());
	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: context.site,
		items: posts.map((post) => ({
			title: post.data.title,
			pubDate: new Date(post.data.date),
			description: post.data.summary || post.data.description || '',
			link: `/posts/${postSlug(post.id)}/`,
			categories: [...(post.data.categories ?? []), ...(post.data.tags ?? [])],
			content: renderPostHtml(post, site),
		})),
	});
}
