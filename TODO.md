# Site TODO

## CRITICAL

- [x] **Fix search input icon overlap** — Pagefind icon overlapped typed text; fixed by setting `padding-left: 2.5rem !important` on `.pagefind-ui__search-input` in `global.css` and `search.astro`.

---

## HIGH

- [x] **Replace Disqus with giscus** — ⚠️ Needs GitHub Discussions enabled + `GISCUS_CATEGORY_ID` filled in `src/consts.ts` (visit giscus.app to get the value).

- [x] **Delete orphaned Hugo files from `/public`** — Removed `public/ts/`, `public/scss/`, and their contents.

- [x] **Delete orphaned fonts** — Removed unused `atkinson-bold.woff` and `atkinson-regular.woff`; only `CollegeStencil.woff2` remains.

- [ ] **Show recent posts on home page** — Skipped intentionally; current static home page layout is preferred.

---

## MEDIUM

- [x] **Fix OG type for post pages** — `BaseHead.astro` now accepts an `ogType` prop; `PostLayout.astro` passes `"article"` with `article:published_time` and `article:author` meta tags.

- [x] **Add JSON-LD structured data to posts** — `BlogPosting` schema added in `PostLayout.astro` with title, date, author, image, and canonical URL.

- [x] **Add `<meta name="author">` to BaseHead** — Added to `src/components/BaseHead.astro`.

- [x] **Add prev/next post navigation** — Older/Newer links added to `PostLayout.astro`; prev/next computed by date in `[...slug].astro`.

- [x] **Add a custom 404 page** — Created `src/pages/404.astro` with links back to Home, Archives, and Search.

- [x] **Deduplicate GA and theme scripts** — Both moved into `BaseHead.astro`; removed from `BaseLayout.astro` and `PostLayout.astro`.

- [x] **Remove license widget from sidebar** — Duplicate of footer; removed from `Sidebar.astro`.

- [x] **Remove empty "About" sidebar widget** — Removed; contained no useful content.

---

## LOW

- [x] **Add copy-to-clipboard button on code blocks** — Inline script in `PostLayout.astro`; button appears on hover, shows "Copied!" for 2s.

- [x] **Add table of contents for long posts** — `TableOfContents.astro` auto-shows for posts with 3+ h2/h3 headings; collapsible. Headings passed from `[...slug].astro` via `render()`.

- [x] **Add a back-to-top button** — `BackToTop.astro` component used in both layouts; appears after 400px scroll.

- [x] **Add a dedicated `/about` page** — Created `src/pages/about.astro` at `/about`, content in `src/content/pages/about.md`. Added "About" to nav in `consts.ts`. ⚠️ Update `about.md` with your actual bio.

- [x] **Normalize category URL casing** — All categories in posts are already lowercase; no changes needed.
