#!/usr/bin/env python3
"""Prepend a "this blog has moved" banner to top WordPress.com posts.

Reads the top-15 mapping produced from the stats archive, fetches each
post's current content (context=edit for raw markup), and prepends a
Gutenberg group block with a button to the matching post on
https://glenzac.github.io. Idempotent: skips posts already containing
the BANNER_MARKER.

Usage:
  python3 scripts/add_wp_banners.py --dry-run          # show what would change
  python3 scripts/add_wp_banners.py --only <post_id>   # single post (canary)
  python3 scripts/add_wp_banners.py                    # all top-15
"""
import argparse
import json
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = "97134063"
BASE = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE}"
NEW_SITE = "https://glenzac.github.io"
TOKEN = json.loads((REPO / ".secrets" / "token.json").read_text())["access_token"]

BANNER_MARKER = "<!-- moved-banner -->"

BANNER = (
    BANNER_MARKER
    + """
<!-- wp:group {"style":{"border":{"width":"2px","radius":"8px"},"spacing":{"padding":{"top":"16px","bottom":"16px","left":"16px","right":"16px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group" style="border-width:2px;border-radius:8px;padding-top:16px;padding-right:16px;padding-bottom:16px;padding-left:16px">
<!-- wp:paragraph -->
<p><strong>\U0001F4CD This blog has moved!</strong> You're reading an archived copy — the up-to-date version of this post now lives on my new site.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{url}">Read this post on the new site →</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->
"""
)


def api(path: str, data=None, **params) -> dict:
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers={"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", type=int, help="only this WP post ID")
    ap.add_argument("--mapping", default="top15-mapping.json",
                    help="mapping file in data/wordpress-stats/")
    args = ap.parse_args()

    mapping = json.loads((REPO / "data" / "wordpress-stats" / args.mapping).read_text())
    for views, title, slug, post_id, status in mapping:
        if status != "OK":
            print(f"SKIP (no Astro match): {title}")
            continue
        if args.only and post_id != args.only:
            continue
        post = api(f"/posts/{post_id}", context="edit")
        content = post["content"]
        if BANNER_MARKER in content:
            print(f"SKIP (already bannered): {post['title']}")
            continue
        new_url = f"{NEW_SITE}/posts/{slug}/"
        banner = BANNER.replace("{url}", new_url)
        if args.dry_run:
            print(f"WOULD UPDATE {post_id}: {post['title']} -> {new_url}")
            continue
        res = api(f"/posts/{post_id}", data={"content": banner + content})
        warn = res.get("_content_warnings")
        print(f"UPDATED {post_id}: {res['title']} -> {new_url}" + (f"  WARNINGS: {warn}" if warn else ""))


if __name__ == "__main__":
    main()
