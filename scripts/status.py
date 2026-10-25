"""Checks whether the things I have shipped are up, and draws the answer.
Run by .github/workflows/status.yml once a day. Standard library only.
One request per site per run. The text uses system fonts, because this runs on a bare runner."""
import datetime as dt
import os
import time
import urllib.request

SITES = [
    ("BeatMind", "https://www.beatmind.tech"),
    ("Kanata", "https://kanata.studio"),
    ("Portfolio", "https://parth-tiwari-1.vercel.app"),
    ("Tabla Tuner", "https://tabla-tuner.vercel.app"),
    ("Tathya", "https://tathya-1.vercel.app"),
]
PAL = dict(bg="#0c0c10", border="#2a2a33", fg="#f4f1ea", mute="#8f8f98", ok="#c8ff2e", bad="#ff4a1c")
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 1200, 176


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": "parthtiwari-dev-status/1.0"})
    t = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            code = r.status
    except Exception:
        return False, None
    ms = round((time.perf_counter() - t) * 1000)
    return 200 <= code < 400, ms


def svg(results, stamp, p):
    n = len(results)
    col = (W - 112) / n
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Live check of {n} things I have shipped. Checked {stamp}.">',
           f'<rect width="{W}" height="{H}" rx="22" fill="{p["bg"]}"/>',
           f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="22" fill="none" stroke="{p["border"]}"/>',
           f'<text x="56" y="52" font-family="{FONT}" font-size="16" letter-spacing="3" font-weight="700" '
           f'fill="{p["fg"]}">STILL UP</text>',
           f'<text x="{W-56}" y="44" text-anchor="end" font-family="{FONT}" font-size="14" letter-spacing="1.2" '
           f'fill="{p["mute"]}">CHECKED {stamp}, ONCE A DAY</text>']
    for i, (name, ok, ms) in enumerate(results):
        x = 56 + i * col
        c = p["ok"] if ok else p["bad"]
        out.append(f'<circle cx="{x+8:.1f}" cy="112" r="8" fill="{c}">'
                   + (f'<animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/>' if ok else '')
                   + '</circle>')
        out.append(f'<text x="{x+28:.1f}" y="110" font-family="{FONT}" font-size="23" font-weight="700" fill="{p["fg"]}">{name}</text>')
        sub = f"up, {ms} ms" if ok else "not answering"
        out.append(f'<text x="{x+28:.1f}" y="140" font-family="{FONT}" font-size="17" fill="{p["mute"]}">{sub}</text>')
    out.append("</svg>\n")
    return "\n".join(out)


if __name__ == "__main__":
    results = [(n, *check(u)) for n, u in SITES]
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    here = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(here, exist_ok=True)
    with open(os.path.join(here, "status.svg"), "w", encoding="utf-8") as f:
        f.write(svg(results, stamp, PAL))
    for r in results:
        print(r)
