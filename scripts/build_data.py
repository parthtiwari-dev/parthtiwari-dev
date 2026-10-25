"""The posters that are drawn from data: the contribution sequencer, the night-shift clock, the
errata ledger and the four stat cards.
  python scripts/build_data.py --fonts <dir> --beatmind <repo> --arrivo <repo> [--contrib contrib.json]
Without --contrib it asks GitHub for the last twelve months through the gh CLI."""
import argparse
import datetime as dt
import json
import math
import os
import subprocess

from art_lib import (COBALT, INK, LIME, ORANGE, PAPER, PINK, W, Fonts, animate, fade_out, fit, header,
                     n, poster, step, text)

PAGE = W - 96


# ---------------------------------------------------------------- 07 the year as a beat
def contributions(path):
    if path:
        data = json.load(open(path))
    else:
        q = ('{ user(login:"parthtiwari-dev"){ contributionsCollection { contributionCalendar { totalContributions '
             'weeks { contributionDays { date contributionCount weekday } } } } } }')
        data = json.loads(subprocess.run(["gh", "api", "graphql", "-f", f"query={q}"], capture_output=True,
                                         text=True, check=True).stdout)
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def sequencer(F, cal):
    H, T = 480, 11
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    total = cal["totalContributions"]
    active = sum(1 for d in days if d["contributionCount"])
    peak = max(d["contributionCount"] for d in days)
    x0, y0, pitch, cell, rp = 100, 236, (W - 48 - 78) / len(weeks), 16, 24
    ramp = ["#2f4a12", "#62a117", "#9be31c", LIME]
    b = [header(F, "07", "MY YEAR", "GITHUB  ·  LAST 12 MONTHS", PAPER)]
    b.append(text(F.disp, "MY YEAR,", 64, 44, 146, PAPER, 0))
    b.append(text(F.serif, "as a beat.", 70, 44 + F.disp.width("MY YEAR,", 64, 0) + 26, 146, LIME))
    b.append(text(F.mono, f"{total} CONTRIBUTIONS  ·  {active} ACTIVE DAYS  ·  EVERY BOX IS A DAY, EVERY LIT BOX IS A BEAT",
                  16, 48, 186, PAPER, 1.3, extra='opacity=".78"'))
    for r, lab in ((1, "MON"), (3, "WED"), (5, "FRI")):
        b.append(text(F.mono, lab, 14, 48, y0 + r * rp + 13, PAPER, 1.0, extra='opacity=".6"'))
    seen, last_label = None, -9
    cells = []
    for i, w in enumerate(weeks):
        first = w["contributionDays"][0]["date"]
        month = dt.date.fromisoformat(first).strftime("%b").upper()
        if month != seen and i < len(weeks) - 2 and i - last_label >= 3:
            last_label = i
            b.append(text(F.mono, month, 14, x0 + i * pitch, y0 - 14, PAPER, 1.0, extra='opacity=".7"'))
            seen = month
        for d in w["contributionDays"]:
            c = d["contributionCount"]
            x, y = x0 + i * pitch, y0 + d["weekday"] * rp
            if not c:
                cells.append(f'<rect x="{n(x)}" y="{n(y)}" width="{cell}" height="{cell}" rx="4" fill="#1c1c26"/>')
                continue
            lvl = min(3, int(c / peak * 4)) if peak else 0
            col = ramp[lvl]
            hit = 0.6 + (i / len(weeks)) * 8.6
            k = f"0;{hit/T:.4f};{(hit+.08)/T:.4f};{(hit+.7)/T:.4f};1"
            cells.append(f'<rect x="{n(x)}" y="{n(y)}" width="{cell}" height="{cell}" rx="4" fill="{col}">'
                         f'<animate attributeName="fill" values="{col};{col};#ffffff;{col};{col}" keyTimes="{k}" dur="{T}s" repeatCount="indefinite"/></rect>')
    b.append("".join(cells))
    gx = f'<linearGradient id="trail" x1="0" x2="1"><stop offset="0" stop-color="{LIME}" stop-opacity="0"/><stop offset="1" stop-color="{LIME}" stop-opacity=".28"/></linearGradient>'
    end = x0 + len(weeks) * pitch
    b.append(f'<rect y="{y0-8}" width="90" height="{7*rp+10}" fill="url(#trail)">'
             f'<animate attributeName="x" values="{n(x0-90)};{n(x0-90)};{n(end-90)};{n(end-90)}" keyTimes="0;{0.6/T:.4f};{9.2/T:.4f};1" dur="{T}s" repeatCount="indefinite"/></rect>'
             f'<rect y="{y0-8}" width="2.5" height="{7*rp+10}" fill="{LIME}">'
             f'<animate attributeName="x" values="{n(x0-2)};{n(x0-2)};{n(end)};{n(end)}" keyTimes="0;{0.6/T:.4f};{9.2/T:.4f};1" dur="{T}s" repeatCount="indefinite"/></rect>')
    ly = H - 56
    b.append(text(F.serif, "Most nights it was the same two or three things.", 30, 48, ly + 8, PAPER, extra='opacity=".85"'))
    lx = W - 48 - 5 * 24 - 130
    b.append(text(F.mono, "LESS", 14, lx, ly + 6, PAPER, 1.0, extra='opacity=".7"'))
    for i, c in enumerate(["#1c1c26"] + ramp):
        b.append(f'<rect x="{lx+50+i*24}" y="{ly-10}" width="16" height="16" rx="4" fill="{c}"/>')
    b.append(text(F.mono, "MORE", 14, lx + 50 + 5 * 24 + 6, ly + 6, PAPER, 1.0, extra='opacity=".7"'))
    return poster(H, INK, "\n".join(b), f"My year as a beat. {total} GitHub contributions over twelve months drawn as a step sequencer; "
                  f"a playhead sweeps across and lights each active day.", gx)


# ---------------------------------------------------------------- 08 night shift
def hours(repo):
    out = subprocess.run(["git", "-C", repo, "log", "--all", "--format=%ai"], capture_output=True, text=True,
                         check=True).stdout.split("\n")
    return [int(x[11:13]) for x in out if x.strip()]


def nightclock(F, hrs):
    H, T = 580, 9
    cx, cy, rin, rmax = 330, 322, 66, 205
    counts = [hrs.count(h) for h in range(24)]
    peak = max(counts)
    night = sum(counts[:6])
    pct = round(100 * night / len(hrs))
    b = [header(F, "08", "NIGHT SHIFT", "BEATMIND + ARRIVO  ·  EVERY COMMIT", PAPER)]
    il = [f'<circle cx="{cx}" cy="{cy}" r="{rin-10}" fill="none" stroke="{PAPER}" stroke-opacity=".3"/>',
          f'<circle cx="{cx}" cy="{cy}" r="{rmax+16}" fill="none" stroke="{PAPER}" stroke-opacity=".18"/>']
    for h, c in enumerate(counts):
        ln = 8 + (rmax - rin - 8) * c / peak
        col = LIME if h < 6 else PAPER
        dl = 0.4 + h * 0.13
        il.append(f'<g transform="rotate({h*15} {cx} {cy})"><rect x="{cx-9}" y="{n(cy-rin-ln)}" width="18" height="{n(ln)}" rx="5" fill="{col}">'
                  f'{step("y", n(cy-rin), n(cy-rin-ln), dl, 0.6, T)}{step("height", "0", n(ln), dl, 0.6, T)}</rect></g>')
    for h in (0, 6, 12, 18):
        a = math.radians(h * 15)
        il.append(text(F.mono, f"{h:02d}", 16, cx + (rmax + 36) * math.sin(a), cy - (rmax + 36) * math.cos(a) + 5, PAPER, 1.2, "middle"))
    il.append(f'<g><path d="M{cx} {cy}V{cy-rmax-16}" stroke="{PAPER}" stroke-opacity=".7" stroke-width="2"/>'
              f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="12s" repeatCount="indefinite"/></g>')
    il.append(text(F.mono, "24H", 17, cx, cy + 6, PAPER, 2, "middle"))
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    sz, trk = fit(F.disp, f"{pct}%", 170, 500, -0.02)
    b.append(text(F.disp, f"{pct}%", sz, 640, 330, LIME, trk))
    lines = F.mono.wrap(f"OF MY COMMITS ON BEATMIND AND ARRIVO LAND BETWEEN MIDNIGHT AND 6 AM.", 20, 500, 1.2)
    for i, ln in enumerate(lines):
        b.append(text(F.mono, ln, 20, 646, 384 + i * 32, PAPER, 1.2))
    b.append(text(F.serif, "Not a flex. Just when the work gets done.", 36, 646, 384 + len(lines) * 32 + 56, PAPER, extra='opacity=".85"'))
    b.append(text(F.mono, f"{len(hrs)} COMMITS  ·  {night} BETWEEN 00:00 AND 05:59", 16, 646, H - 48, PAPER, 1.2, extra='opacity=".75"'))
    size, tr = fit(F.disp, "NIGHT SHIFT.", 70, 500, -0.02)
    b.append(text(F.disp, "NIGHT SHIFT.", size, 646, 164, PAPER, tr))
    return poster(H, COBALT, "\n".join(b), f"Night shift. A 24-hour clock of when I commit. {pct}% of commits on BeatMind and Arrivo land between midnight and 6 am.")


# ---------------------------------------------------------------- 09 errata
ROWS = [
    ("BEATMIND  ·  GPU", "The GPU was doing the work.",
     "It had silently fallen back to the CPU. One missing library, libcublasLt.so.13.",
     "Fixed it. About a minute became 23 seconds (two different tracks, so “about”)."),
    ("BEATMIND  ·  RIGHTS", "A tick box saying “I own this” is enough.",
     "A checkbox is not a rights check.",
     "Deleted it. Export now needs a fingerprint match."),
    ("BEATMIND  ·  BILLING  ·  2026-09-20", "Refunds on a downgrade were fair.",
     "They refunded cash for credits already spent.",
     "Found it fact-checking one sentence for a client. Fixed the same day."),
    ("VIVID  ·  SPEED", "A turbo model, 5.9× cheaper, was a win.",
     "Faces got worse and people were duplicated.",
     "Did not ship it."),
    ("UPI FRAUD ENGINE  ·  JAN 2026", "0.9106 ROC-AUC. Ready to go.",
     "A column that only existed in my synthetic data matched the label 100%.",
     "Removed it and retrained. 0.8953 is the honest number."),
    ("QUERYPILOT", "A hallucination rate of 100%.",
     "My detector was reading dictionary keys, not table names. The real rate was 0%.",
     "Fixed the detector."),
]


def errata(F):
    colA, wA, colB, wB = 48, 480, 600, 552
    rows, y = [], 296
    for where, bel, meas, so in ROWS:
        la = F.serif.wrap(bel, 32, wA)
        lm = F.body.wrap(meas, 18, wB)
        ls = F.body.wrap(so, 18, wB - 34)
        h = max(len(la) * 36, len(lm) * 26 + 12 + len(ls) * 26) + 52
        rows.append((where, la, lm, ls, y, h))
        y += h
    H = y + 40
    T = 3 + len(ROWS) * 1.9 + 2.5
    b = [header(F, "09", "ERRATA", "BELIEVED, THEN MEASURED", PAPER)]
    size, tr = fit(F.disp, "WHAT I GOT WRONG.", 76, PAGE, -0.02)
    b.append(text(F.disp, "WHAT I GOT WRONG.", size, 44, 156, PAPER, tr))
    b.append(text(F.serif, "The record is the part of my work I trust most.", 36, 48, 222, LIME))
    b.append(text(F.mono, "I BELIEVED", 15, colA, 274, PAPER, 2.2, extra='opacity=".6"'))
    b.append(text(F.mono, "THEN I MEASURED", 15, colB, 274, PAPER, 2.2, extra='opacity=".6"'))
    il = []
    for i, (where, la, lm, ls, ry, rh) in enumerate(rows):
        t0 = 1.0 + i * 1.9
        il.append(f'<path d="M48 {ry}H{W-48}" stroke="{PAPER}" stroke-opacity=".18"/>')
        il.append(text(F.mono, where, 14.5, colA, ry + 28, PAPER, 1.3, extra='opacity=".65"'))
        g = [text(F.serif, ln, 32, colA, ry + 62 + j * 36, PAPER, extra='opacity=".62"') for j, ln in enumerate(la)]
        il.append(f'<g>{"".join(g)}{step("opacity", "0", "1", t0, 0.4, T)}</g>')
        for j, ln in enumerate(la):
            wl = F.serif.width(ln, 32)
            il.append(f'<rect x="{colA-4}" y="{ry+62+j*36-11}" width="{n(wl+8)}" height="3.5" fill="{ORANGE}">'
                      f'{step("width", "0", n(wl+8), t0+0.5+j*0.12, 0.45, T)}</rect>')
        m = [text(F.body, ln, 18, colB, ry + 34 + j * 26, PAPER) for j, ln in enumerate(lm)]
        sy = ry + 34 + len(lm) * 26 + 12
        s_ = [text(F.body, ("→ " if j == 0 else "   ") + ln, 18, colB, sy + j * 26, LIME) for j, ln in enumerate(ls)]
        il.append(f'<g>{"".join(m)}{step("opacity", "0", "1", t0 + 1.0, 0.4, T)}</g>')
        il.append(f'<g>{"".join(s_)}{step("opacity", "0", "1", t0 + 1.4, 0.4, T)}</g>')
    b.append(f'<g>{"".join(il)}{fade_out(T, 0.6)}</g>')
    alt = "What I got wrong. " + " ".join(f"{w}: believed {b_}; measured {m}; so {s}" for w, b_, m, s in ROWS)
    return poster(H, INK, "\n".join(b), alt.replace('"', "'"))


# ---------------------------------------------------------------- stat cards (full width, readable)
CH = 372


def card(F, name, big, sub, bg, fg, art, alt):
    b = [text(F.mono, name, 17, 48, 62, fg, 2.2)]
    size, tr = fit(F.disp, big, 175, 480, -0.02)
    b.append(text(F.disp, big, size, 44, 200, fg, tr))
    for i, ln in enumerate(F.mono.wrap(sub, 18, 470, 0.6)):
        b.append(text(F.mono, ln, 18, 48, 252 + i * 28, fg, 0.6, extra='opacity=".88"'))
    b.append(art)
    return poster(CH, bg, "\n".join(b), alt)


def key(F, items, x, y, fg, gap=38):
    out = []
    for i, (shape, label) in enumerate(items):
        yy = y + i * gap
        out.append(shape(x, yy) + text(F.mono, label, 16, x + 30, yy + 6, fg, 0.8))
    return "".join(out)


def card_querypilot(F):
    T, g = 8, []
    for i in range(70):  # 63 right first time, 4 rescued by the correction loop, 3 still wrong
        col, row = i % 10, i // 10
        x, y = 620 + col * 36, 56 + row * 36
        if i < 63:
            g.append(f'<rect x="{x}" y="{y}" width="29" height="29" rx="8" fill="{COBALT}">{step("opacity", "0", "1", 0.3 + i * 0.03, 0.2, T)}</rect>')
        elif i < 67:
            g.append(f'<rect x="{x}" y="{y}" width="29" height="29" rx="8" fill="{ORANGE}">{step("opacity", "0", "1", 3.4 + (i - 63) * 0.5, 0.25, T)}</rect>')
        else:
            g.append(f'<rect x="{x+1}" y="{y+1}" width="27" height="27" rx="7" fill="none" stroke="{INK}" stroke-width="2.5" stroke-opacity=".55"/>')
    k = key(F, [(lambda x, y: f'<rect x="{x}" y="{y-8}" width="18" height="18" rx="5" fill="{COBALT}"/>', "63  FIRST TRY"),
                (lambda x, y: f'<rect x="{x}" y="{y-8}" width="18" height="18" rx="5" fill="{ORANGE}"/>', "4  SELF-FIXED"),
                (lambda x, y: f'<rect x="{x+1}" y="{y-7}" width="16" height="16" rx="4" fill="none" stroke="{INK}" stroke-width="2.5" stroke-opacity=".55"/>', "3  WRONG")],
            1002, 120, INK)
    return card(F, "QUERYPILOT  /  TEXT TO SQL", "95.7%", "Of 70 test questions, answered right. It checks its own SQL and corrects it.", PAPER, INK,
                f'<g>{"".join(g)}{fade_out(T)}</g>{k}', "QueryPilot. 95.7% of 70 test questions answered correctly after self-correction.")


def card_upi(F):
    T, g = 8, []
    for i in range(100):
        col, row = i % 10, i // 10
        x, y = 620 + col * 31, 52 + row * 30
        if i < 92:
            g.append(f'<circle cx="{x+12}" cy="{y+12}" r="12" fill="{INK}">{step("opacity", "0", "1", 0.2 + i * 0.025, 0.2, T)}</circle>')
        else:
            g.append(f'<circle cx="{x+12}" cy="{y+12}" r="10.5" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    k = key(F, [(lambda x, y: f'<circle cx="{x+9}" cy="{y+1}" r="9" fill="{INK}"/>', "92  REAL FRAUD"),
                (lambda x, y: f'<circle cx="{x+9}" cy="{y+1}" r="8" fill="none" stroke="{INK}" stroke-width="2.5"/>', "8  FALSE ALARM")],
            956, 150, INK)
    return card(F, "UPI FRAUD ENGINE  /  REAL TIME", "92.06%", "Of alerts were real fraud, inside a 0.5% daily alert budget. p95 312 ms. 55+ leakage tests.", LIME, INK,
                f'<g>{"".join(g)}{fade_out(T)}</g>{k}', "UPI Fraud Engine. 92.06% of alerts were real fraud inside a 0.5% daily alert budget.")


def card_rag(F):
    T, g = 8, []
    for i in range(10):
        y = 50 + i * 30
        wd = 250 + (i * 53) % 130
        if i < 8:
            g.append(f'<rect x="620" y="{y}" width="{wd}" height="22" rx="11" fill="{INK}">{step("width", "0", wd, 0.3 + i * 0.3, 0.5, T)}</rect>')
        else:
            g.append(f'<rect x="621" y="{y+1}" width="{wd-2}" height="20" rx="10" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 6">{step("opacity", "0", "1", 0.3 + i * 0.3, 0.4, T)}</rect>')
    k = key(F, [(lambda x, y: f'<rect x="{x}" y="{y-6}" width="22" height="12" rx="6" fill="{INK}"/>', "8  GROUNDED"),
                (lambda x, y: f'<rect x="{x}" y="{y-6}" width="22" height="12" rx="6" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="4 3"/>', "2  NOT")],
            1022, 120, INK)
    stamp = (f'<g transform="rotate(-4 280 340)"><rect x="48" y="318" width="340" height="40" rx="10" fill="{INK}"/>'
             + text(F.mono, "REFUSES WHEN IT CAN'T CITE", 16, 66, 344, PAPER, 1.2) + '</g>')
    return card(F, "DRUG RAG  /  FDA + NICE", "0.80", "RAGAS faithfulness. Cited answers from the documents only. Not medical advice.", PINK, INK,
                f'<g>{"".join(g)}{fade_out(T)}</g>{k}{stamp}', "Evidence-Bound Drug RAG. RAGAS faithfulness 0.80, refuses when the documents are silent.")


def card_tathya(F):
    T, g = 8, []
    for i, lab in enumerate(["GOVERNMENT", "MEDIA", "CITIZENS"]):
        y = 96 + i * 92
        g.append(text(F.mono, lab, 17, 640, y - 16, PAPER, 2.0, extra='opacity=".9"'))
        g.append(f'<path d="M640 {y}C790 {y} 800 214 900 214" pathLength="1" fill="none" stroke="{LIME}" stroke-width="5" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="0">'
                 f'{step("stroke-dashoffset", "1", "0", 0.4 + i * 0.5, 0.9, T)}</path>')
    g.append(f'<g><rect x="900" y="146" width="130" height="136" rx="14" fill="{PAPER}"/>'
             f'<path d="M926 182h78M926 208h78M926 234h50" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
             f'{step("opacity", "0", "1", 2.0, 0.4, T)}</g>')
    g.append(text(F.mono, "CASE FILE", 16, 965, 320, PAPER, 2.0, "middle"))
    return card(F, "TATHYA  /  A PUBLIC RECORD", "YOU DECIDE", "India's Union Government, from public sources: what government, media and citizens each said. Live, still being finished.", COBALT, PAPER,
                f'<g>{"".join(g)}{fade_out(T)}</g>', "Tathya. Sources from government, media and citizens cluster into one sourced case file. You decide.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True)
    ap.add_argument("--beatmind", required=True)
    ap.add_argument("--arrivo", required=True)
    ap.add_argument("--contrib")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "assets"))
    a = ap.parse_args()
    F = Fonts(a.fonts)
    hrs = hours(a.beatmind) + hours(a.arrivo)
    outs = {"p07-year": sequencer(F, contributions(a.contrib)), "p08-night": nightclock(F, hrs), "p09-errata": errata(F),
            "c1-querypilot": card_querypilot(F), "c2-upi": card_upi(F), "c3-rag": card_rag(F), "c4-tathya": card_tathya(F)}
    for name, svg in outs.items():
        with open(os.path.join(a.out, f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", name)
    night = sum(1 for h in hrs if h < 6)
    print("commits", len(hrs), "night", night, f"{round(100*night/len(hrs))}%")
