#!/usr/bin/env python3
"""One-off: download imgur-hotlinked media into the repo and rewrite links.

Bare imgur URLs on their own line (old WordPress auto-embeds) become
![](@assets/images/<year>/<id>.<ext>) for images, or a <video> tag for mp4s
(stored under public/videos/ since Astro's image pipeline is images-only).
Frontmatter is left untouched (bare-line match is anchored at column 0,
frontmatter enclosure URLs are indented).
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "src" / "content" / "posts"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

URL_RE = re.compile(r"^(https://i\.imgur\.com/([A-Za-z0-9]+)\.(jpe?g|png|gif|mp4))(\?\S*)?\s*$")

def download(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["curl", "-sL", "-A", UA, "--fail", "-o", str(dest), url],
        capture_output=True,
    )
    if r.returncode != 0:
        dest.unlink(missing_ok=True)
        return False
    # imgur serves a placeholder page/image for removed content; sanity-check type
    head = dest.read_bytes()[:16]
    if head.startswith(b"<!DOCTYPE") or head.startswith(b"<html"):
        dest.unlink()
        return False
    return True

def main() -> None:
    failures, changed = [], []
    for md in sorted(POSTS.rglob("*.md")):
        text = md.read_text()
        if "i.imgur.com" not in text:
            continue
        year = re.search(r"-(\d{4})-\d{2}-\d{2}-", md.name)
        year = year.group(1) if year else "misc"
        out_lines, dirty = [], False
        for line in text.splitlines():
            m = URL_RE.match(line)
            if not m:
                out_lines.append(line)
                continue
            url, img_id, ext = m.group(1), m.group(2), m.group(3).lower()
            if ext == "mp4":
                dest = REPO / "public" / "videos" / f"{img_id}.mp4"
                ok = download(url, dest)
                if ok:
                    out_lines.append(
                        f'<video controls muted playsinline src="/videos/{img_id}.mp4"></video>'
                    )
                    dirty = True
                else:
                    failures.append((md.name, url))
                    out_lines.append(line)
            else:
                dest = REPO / "src" / "assets" / "images" / year / f"{img_id}.{ext}"
                ok = download(url, dest)
                if ok:
                    out_lines.append(f"![](@assets/images/{year}/{img_id}.{ext})")
                    dirty = True
                else:
                    failures.append((md.name, url))
                    out_lines.append(line)
        if dirty:
            md.write_text("\n".join(out_lines) + "\n")
            changed.append(md.relative_to(REPO))
    print(f"Rewrote {len(changed)} files:")
    for c in changed:
        print(f"  {c}")
    if failures:
        print(f"\nFAILED downloads ({len(failures)}):")
        for name, url in failures:
            print(f"  {name}: {url}")
        sys.exit(1)

if __name__ == "__main__":
    main()
