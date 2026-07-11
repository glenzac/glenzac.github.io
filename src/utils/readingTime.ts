// Rough reading-time estimate from raw markdown (200 wpm, same rate as PostLayout).
export function readingTime(body: string): number {
	return Math.max(1, Math.ceil(body.split(/\s+/).length / 200));
}
