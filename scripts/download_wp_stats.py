#!/usr/bin/env python3
"""Download the full stats history for glenzac.wordpress.com into
data/wordpress-stats/ as raw JSON (one file per endpoint/period).

Auth: reads the OAuth bearer token from .secrets/token.json (gitignored).
"""
import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "data" / "wordpress-stats"
SITE = "97134063"
BASE = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE}"
TOKEN = json.loads((REPO / ".secrets" / "token.json").read_text())["access_token"]

FIRST_YEAR = 2015
THIS_YEAR = date.today().year


def get(path: str, **params) -> dict:
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def save(name: str, data: dict) -> None:
    p = OUT / f"{name}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(f"  {p.relative_to(REPO)}")


def main() -> None:
    print("summary + insights:")
    save("summary", get("/stats"))
    save("insights", get("/stats/insights"))

    print("visits by month (full history):")
    save("visits-monthly", get(
        "/stats/visits", unit="month",
        quantity=(THIS_YEAR - FIRST_YEAR + 1) * 12, date=date.today().isoformat(),
    ))

    print("visits by day, per year:")
    for y in range(FIRST_YEAR, THIS_YEAR + 1):
        save(f"visits-daily/{y}", get(
            "/stats/visits", unit="day", quantity=366, date=f"{y}-12-31",
        ))
        time.sleep(0.3)

    print("per-year breakdowns:")
    for kind, path in [
        ("top-posts", "/stats/top-posts"),
        ("referrers", "/stats/referrers"),
        ("countries", "/stats/country-views"),
        ("search-terms", "/stats/search-terms"),
        ("clicks", "/stats/clicks"),
    ]:
        for y in range(FIRST_YEAR, THIS_YEAR + 1):
            save(f"{kind}/{y}", get(
                path, period="year", date=f"{y}-12-31", max=500,
            ))
            time.sleep(0.3)

    print("done")


if __name__ == "__main__":
    main()
