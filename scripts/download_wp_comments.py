#!/usr/bin/env python3
"""Archive approved WordPress.com comments for the Astro site.

Writes src/data/comments.json keyed by post slug. Sensitive fields
(author email, IP address) are stripped — this file is committed to a
public repo. Pingbacks/trackbacks are excluded.
"""
import json
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = "97134063"
BASE = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE}"
TOKEN = json.loads((REPO / ".secrets" / "token.json").read_text())["access_token"]


def get(path: str, **params) -> dict:
    url = f"{BASE}{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def main() -> None:
    # post ID -> slug
    slug_by_id = {}
    for page in range(1, 4):
        d = get("/posts/", number=100, page=page, fields="ID,slug", status="publish")
        for p in d["posts"]:
            slug_by_id[str(p["ID"])] = p["slug"]
        if len(d["posts"]) < 100:
            break

    comments, offset = [], 0
    while True:
        d = get("/comments/", number=100, offset=offset, status="approved")
        batch = d["comments"]
        comments += batch
        offset += len(batch)
        if len(batch) < 100:
            break

    by_slug = {}
    skipped = 0
    for c in comments:
        if c.get("type") not in (None, "comment"):
            skipped += 1
            continue
        slug = slug_by_id.get(str(c["post"]["ID"]))
        if not slug:
            skipped += 1
            continue
        parent = c.get("parent")
        by_slug.setdefault(slug, []).append({
            "id": c["ID"],
            "parent": parent["ID"] if isinstance(parent, dict) else None,
            "author": c["author"]["name"],
            "url": c["author"].get("URL") or None,
            "date": c["date"],
            "content": c["content"],
        })
    for slug in by_slug:
        by_slug[slug].sort(key=lambda x: x["date"])

    out = REPO / "src" / "data" / "comments.json"
    out.write_text(json.dumps(by_slug, indent=1, ensure_ascii=False))
    n = sum(len(v) for v in by_slug.values())
    print(f"{n} comments on {len(by_slug)} posts -> {out.relative_to(REPO)} (skipped {skipped})")


if __name__ == "__main__":
    main()
