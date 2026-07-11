import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';
import { postSlug } from '../utils/postSlug';

export async function GET(context) {
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
		})),
	});
}
