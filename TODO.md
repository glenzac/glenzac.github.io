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

- [ ] **Add copy-to-clipboard button on code blocks** — A small inline script in `PostLayout.astro`, no dependencies needed.

- [ ] **Add table of contents for long posts** — Astro's `getHeadings()` is built-in. Add an opt-in TOC component to `PostLayout.astro` for technical posts with many sections.

- [ ] **Add a back-to-top button** — Useful on long posts. Simple CSS + a small script, no dependencies.

- [ ] **Add a dedicated `/about` page** — No about page exists; the removed sidebar widget was the only "about" content.

- [ ] **Normalize category URL casing** — Category links use `.toLowerCase()` but the nav hardcodes lowercase paths. If category frontmatter has inconsistent casing, pages could 404.
