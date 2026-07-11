/**
 * Derive the public URL slug for a post from its collection id.
 * Post files are named `<category>-<yyyy>-<mm>-<dd>-<slug>.md` inside a
 * category folder; the public URL is just `/posts/<slug>/`.
 * e.g. "tinkering/tinkering-2020-06-10-variable-frequency-pwm-generator"
 *   -> "variable-frequency-pwm-generator"
 */
export function postSlug(id: string): string {
	const base = id.split('/').pop() ?? id;
	return base.replace(/^[a-z0-9-]+?-\d{4}-\d{2}-\d{2}-/, '');
}
