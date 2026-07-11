#!/usr/bin/env python3
"""Crunch data/wordpress-stats/ raw JSON into src/data/journey.json,
the compact dataset behind the /journey page."""
import collections
import glob
import html
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATS = REPO / "data" / "wordpress-stats"
OUT = REPO / "src" / "data" / "journey.json"


def main() -> None:
    summary = json.loads((STATS / "summary.json").read_text())["stats"]

    # monthly series (period, views, visitors)
    monthly = []
    m = json.loads((STATS / "visits-monthly.json").read_text())
    fields = m["fields"]
    for row in m["data"]:
        d = dict(zip(fields, row))
        if d["views"] or d["visitors"]:
            monthly.append([d["period"], d["views"], d["visitors"]])

    # yearly totals
    yearly = collections.defaultdict(lambda: [0, 0])
    for period, views, visitors in monthly:
        y = period[:4]
        yearly[y][0] += views
        yearly[y][1] += visitors
    yearly = [[y, v[0], v[1]] for y, v in sorted(yearly.items())]

    # cumulative view milestones from daily data
    days = []
    for f in sorted(glob.glob(str(STATS / "visits-daily" / "*.json"))):
        d = json.loads(Path(f).read_text())
        fl = d["fields"]
        for row in d["data"]:
            r = dict(zip(fl, row))
            days.append((r["period"], r["views"]))
    days = sorted(set(days))
    milestones, cum = [], 0
    targets = [1, 1000, 5000, 10000, 25000, 50000]
    for period, views in days:
        cum += views
        while targets and cum >= targets[0]:
            milestones.append([targets.pop(0), period])

    # all-time top posts
    views_by_title = collections.Counter()
    href_by_title = {}
    for f in glob.glob(str(STATS / "top-posts" / "*.json")):
        d = json.loads(Path(f).read_text())
        for day in d.get("days", {}).values():
            for p in day.get("postviews", []):
                if p.get("type") == "post":
                    t = html.unescape(p["title"]).strip()
                    views_by_title[t] += p["views"]
                    href_by_title[t] = p.get("href", "")
    top_posts = [
        [t, v, href_by_title[t].rstrip("/").split("/")[-1]]
        for t, v in views_by_title.most_common(10)
    ]

    # countries
    country_views = collections.Counter()
    code_names = {}
    for f in glob.glob(str(STATS / "countries" / "*.json")):
        d = json.loads(Path(f).read_text())
        info = d.get("country-info") or {}
        if isinstance(info, dict):
            code_names.update({
                code: ci.get("country_full", code) for code, ci in info.items()
            })
        for day in d.get("days", {}).values():
            for c in day.get("views", []):
                country_views[c["country_code"]] += c["views"]
    country_views = collections.Counter({
        code_names.get(code, code): v for code, v in country_views.items()
    })
    countries = country_views.most_common(10)
    n_countries = len(country_views)

    # search terms (skip encrypted placeholder)
    terms = collections.Counter()
    for f in glob.glob(str(STATS / "search-terms" / "*.json")):
        d = json.loads(Path(f).read_text())
        for day in d.get("days", {}).values():
            for t in day.get("search_terms", []):
                terms[t["term"]] += t["views"]
    top_terms = [t for t in terms.most_common(12) if "encrypted" not in t[0].lower()][:8]

    data = {
        "generated_from": "data/wordpress-stats (WordPress.com 2015-2026)",
        "totals": {
            "views": summary["views"],
            "visitors": summary["visitors"],
            "posts": summary["posts"],
            "comments": summary["comments"],
            "shares": summary["shares"],
            "followers": summary["followers_blog"],
            "best_day": summary["views_best_day"],
            "best_day_views": summary["views_best_day_total"],
            "first_day": days[0][0] if days else None,
            "countries": n_countries,
        },
        "yearly": yearly,
        "monthly": monthly,
        "milestones": milestones,
        "top_posts": top_posts,
        "countries": countries,
        "search_terms": top_terms,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(f"wrote {OUT.relative_to(REPO)}")
    print(json.dumps({k: (v if not isinstance(v, list) else v[:3]) for k, v in data.items()}, indent=1, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    main()
