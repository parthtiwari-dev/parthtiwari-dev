"""The hero and the poster for each project. python scripts/build_posters.py --fonts <dir>
Every poster animates what the product does. Each is one SVG, no theme variants: a poster brings its
own colour, so it reads the same on a light or a dark page."""
import argparse
import math
import os

from art_lib import (COBALT, INK, LIME, ORANGE, PAPER, PINK, W, Fonts, animate, bars, fade_out, fit,
                     header, n, poster, rng, step, step_move, text)

PAGE = W - 96  # the width a title may use


def title(F, s, bg_fg, baseline, maxsize=190):
    size, tr = fit(F.disp, s, maxsize, PAGE, -0.02)
    return text(F.disp, s, size, 44, baseline, bg_fg, tr)


def caption(F, s, fg, y=424):
    return text(F.serif, s, 38, 48, y, fg)


def facts(F, s, fg, y=468):
    return text(F.mono, s, 16, 48, y, fg, 1.4, "start", 'opacity=".78"')


def draw(path, color, w, delay, dur, T, extra=""):
    """A stroke that draws itself."""
    return (f'<path d="{path}" pathLength="1" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-dasharray="1" stroke-dashoffset="0" {extra}>{step("stroke-dashoffset", "1", "0", delay, dur, T)}</path>')


# ---------------------------------------------------------------- hero
def hero(F):
    H, bx, by = 640, W - 195, 392
    b = []
    for i in range(3):  # radar ripples behind the badge
        b.append(f'<circle cx="{bx}" cy="{by}" r="200" fill="none" stroke="{PAPER}" stroke-width="1.5" opacity=".2">'
                 f'<animate attributeName="r" values="130;640" dur="7.2s" begin="-{i*2.4}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values=".32;0" dur="7.2s" begin="-{i*2.4}s" repeatCount="indefinite"/></circle>')
    b.append(text(F.mono, "PARTH TIWARI", 18, 48, 60, PAPER, 3.4))
    px = W - 48 - 310
    b.append(f'<rect x="{px}" y="30" width="310" height="46" rx="23" fill="{LIME}"/>'
             f'<circle cx="{px+28}" cy="53" r="7" fill="{INK}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>'
             + text(F.mono, "OPEN TO ROLES", 18, px + 50, 59, INK, 2.6))
    for i, line in enumerate(["FULL-STACK LEAD AI DEVELOPER", "(CONTRACT) AT STICK AND DOT", "BUILDING KANATA"]):
        b.append(text(F.mono, line, 17, W - 48, 126 + i * 28, PAPER, 1.6, "end", 'opacity=".9"'))
    # the statement, each line sliding up out of a slot
    lines = [("I BUILD", F.disp, 126, PAPER, 232, 0.2), ("WHOLE", F.disp, 126, PAPER, 366, 0.45)]
    defs = ""
    for i, (s, face, size, col, base, dl) in enumerate(lines):
        defs += f'<clipPath id="l{i}"><rect x="0" y="{base-size}" width="{W}" height="{size+24}"/></clipPath>'
        b.append(f'<g clip-path="url(#l{i})"><g>{text(face, s, size, 44, base, col, -3)}'
                 f'{step_move(dl, 0.9, 1.5, "0 160", "0 0", loop=False)}</g></g>')
    defs += f'<clipPath id="l2"><rect x="0" y="360" width="{W}" height="230"/></clipPath>'
    b.append(f'<g clip-path="url(#l2)"><g>{text(F.serif, "products.", 196, 40, 540, LIME)}'
             f'{step_move(0.7, 1.0, 1.8, "0 200", "0 0", loop=False)}</g></g>')
    # the badge: text round a circle, turning
    phrase = "DESIGN + BUILD + SHIP + " * 2
    r, size = 104, 18
    widths = [F.mono.width(c, size) for c in phrase]
    track = (2 * math.pi * r - sum(widths)) / len(phrase)
    s, g = 0.0, []
    for c, w in zip(phrase, widths):
        if c != " ":
            ang = math.degrees((s + w / 2) / r)
            d = "".join(x[0] for x in F.mono.glyphs(c, size, bx - w / 2, by - r))
            g.append(f'<path transform="rotate({ang:.2f} {bx} {by})" d="{d}" fill="{PAPER}"/>')
        s += w + track
    star = " ".join(f"{bx + (34 if i % 2 == 0 else 14) * math.cos(math.pi * i / 8):.1f},"
                    f"{by + (34 if i % 2 == 0 else 14) * math.sin(math.pi * i / 8):.1f}" for i in range(16))
    b.append(f'<g>{"".join(g)}<animateTransform attributeName="transform" type="rotate" from="0 {bx} {by}" '
             f'to="360 {bx} {by}" dur="24s" repeatCount="indefinite"/></g>')
    b.append(f'<circle cx="{bx}" cy="{by}" r="62" fill="{LIME}"/><polygon points="{star}" fill="{INK}">'
             f'<animateTransform attributeName="transform" type="rotate" from="360 {bx} {by}" to="0 {bx} {by}" dur="12s" repeatCount="indefinite"/></polygon>')
    # ticker
    words = ["BEATMIND", "VIVID", "ARRIVO", "KANATA", "TABLA TUNER", "FROM ZERO TO MOZART"]
    x, items = 0.0, []
    for w in words:
        items.append(text(F.disp8, w, 24, x, 609, INK, 0.5))
        x += F.disp8.width(w, 24, 0.5) + 34
        items.append(f'<circle cx="{n(x-17)}" cy="600" r="5.5" fill="{INK}"/>')
    seq = "".join(items)
    b.append(f'<rect y="566" width="{W}" height="74" fill="{LIME}"/><g><g>{seq}</g><g transform="translate({n(x)} 0)">{seq}</g>'
             f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-{n(x)} 0" dur="{x/70:.1f}s" repeatCount="indefinite"/></g>')
    return poster(H, COBALT, "\n".join(b), "Parth Tiwari. I build whole products. Open to roles. Full-Stack Lead AI Developer (contract) at Stick and Dot, building Kanata.", defs)


# ---------------------------------------------------------------- 01 BeatMind
def beatmind(F):
    H, T, r = 668, 10, rng(7)
    b = [header(F, "01", "BEATMIND", "BEATMIND.TECH  ↗", INK)]
    il = [bars(r, 22, 76, 12, 7, 240, 150, 16, INK)]
    il.append(f'<path d="M372 118V362" stroke="{INK}" stroke-width="3"/><path d="M372 104l8 8-8 8-8-8z" fill="{INK}"/>'
              + text(F.mono, "SEPARATE", 16, 372, 94, INK, 2, "middle"))
    lanes = [("VOCALS", COBALT, 140, (0.9, 2.0), 40), ("DRUMS", PINK, 205, (0.35, 0.8), 46),
             ("BASS", ORANGE, 270, (1.6, 3.0), 44), ("OTHER", LIME, 335, (0.9, 2.2), 36)]
    for i, (name, col, y, dur, mh) in enumerate(lanes):
        d0 = 0.7 + i * 0.3
        il.append(draw(f"M372 240C410 240 410 {y} 444 {y}", col, 4, d0, 0.6, T))
        stroke = f'stroke="{INK}" stroke-width="1"' if col == LIME else ""
        il.append(f'<g opacity="1">{bars(r, 52, 456, 10.4, 6, y, mh, 6, col, dur, stroke)}'
                  f'{step("opacity", "0", "1", d0 + 0.4, 0.5, T)}</g>')
        il.append(f'<circle cx="1018" cy="{y}" r="6" fill="{col}"' + (f' stroke="{INK}"' if col == LIME else "") + '/>'
                  + text(F.mono, name, 17, 1034, y + 6, INK, 1.6))
    pos = [(470, 108), (760, 173), (600, 303), (860, 108), (470, 108)]
    k = ";".join(f"{x:.3f}" for x in [0, .42, .58, .74, .9][:5])
    il.append(f'<rect width="132" height="56" rx="8" fill="{COBALT}" fill-opacity=".12" stroke="{COBALT}" stroke-width="2.5" '
              f'stroke-dasharray="7 5" x="470" y="108">'
              + animate("x", ";".join(str(p[0]) for p in pos), "0;.3;.5;.7;1", T, 'calcMode="spline" keySplines="0.5 0 0.2 1;0.5 0 0.2 1;0.5 0 0.2 1;0.5 0 0.2 1"')
              + animate("y", ";".join(str(p[1]) for p in pos), "0;.3;.5;.7;1", T, 'calcMode="spline" keySplines="0.5 0 0.2 1;0.5 0 0.2 1;0.5 0 0.2 1;0.5 0 0.2 1"')
              + '</rect>')
    il.append(text(F.mono, "↑ REPAINT ONE STEM INSIDE ONE SECTION", 16, 456, 392, COBALT, 1.4))
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    b.append(caption(F, "Upload a track. Get back an editable arrangement.", INK))
    b.append(facts(F, "BUILT SOLO FOR STICK AND DOT  ·  24 DAYS  ·  307 COMMITS  ·  180 USERS (2026-10-23)", INK))
    b.append(title(F, "BEATMIND", INK, 632))
    return poster(H, PAPER, "\n".join(b), "BeatMind. A track is split into vocals, drums, bass and other stems, and one section of one stem is repainted.")


# ---------------------------------------------------------------- 02 Vivid
def vivid(F):
    H, T = 668, 11
    b = [header(F, "02", "VIVID", "VIVID-ALPHA.VERCEL.APP  ↗", INK)]
    defs, il = "", []
    il.append(f'<rect x="48" y="104" width="430" height="266" rx="16" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>')
    script = ["INT. DINER. NIGHT.", "", "She watches the rain", "run down the glass.", "", "CUT TO:"]
    for i, ln in enumerate(script):
        if not ln:
            continue
        y = 156 + i * 34
        w = F.mono.width(ln, 20, 0.5)
        defs += f'<clipPath id="s{i}"><rect x="72" y="{y-24}" width="{n(w+4)}" height="34"><animate attributeName="width" values="0;0;{n(w+4)};{n(w+4)}" keyTimes="0;{(0.4+i*0.35)/T:.4f};{(0.4+i*0.35+0.7)/T:.4f};1" dur="{T}s" repeatCount="indefinite"/></rect></clipPath>'
        il.append(f'<g clip-path="url(#s{i})">{text(F.mono, ln, 20, 72, y, INK, 0.5)}</g>')
    il.append(f'<path d="M498 237h30M516 224l14 13-14 13" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    tints = [INK, COBALT, "#1b1b24", PINK, COBALT, INK]
    shots = [(0.50, 0.58, 1.5), (0.30, 0.60, 0.8), (0.66, 0.55, 1.1), (0.50, 0.62, 1.7), (0.40, 0.57, 0.95), (0.58, 0.60, 1.25)]
    heads = []
    for i, (tint, (fx, fy, sc)) in enumerate(zip(tints, shots)):
        x0, y0 = 556 + (i % 3) * 196, 104 + (i // 3) * 134
        dl = 2.4 + i * 0.5
        cx, cy = x0 + 180 * fx, y0 + 114 * fy * 0.9
        heads.append((cx, cy - 8 * sc))
        face = (f'<circle cx="{n(cx)}" cy="{n(cy-8*sc)}" r="{n(13*sc)}" fill="{PAPER}"/>'
                f'<path d="M{n(cx-24*sc)} {n(y0+114)}q0 -{n(36*sc)} {n(24*sc)} -{n(36*sc)}t{n(24*sc)} {n(36*sc)}z" fill="{PAPER}"/>')
        il.append(f'<g><rect x="{x0}" y="{y0}" width="180" height="114" rx="10" fill="{tint}"/>'
                  f'<clipPath id="f{i}"><rect x="{x0}" y="{y0}" width="180" height="114" rx="10"/></clipPath>'
                  f'<g clip-path="url(#f{i})">{face}</g>'
                  f'<circle cx="{x0+160}" cy="{y0+20}" r="11" fill="{LIME}" stroke="{INK}" stroke-width="2.5">{step("opacity", "0", "1", dl+0.4, 0.2, T)}</circle>'
                  f'<path d="M{x0+155} {y0+20}l4 4 7-8" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round">{step("opacity", "0", "1", dl+0.4, 0.2, T)}</path>'
                  f'{step("opacity", "0", "1", dl, 0.35, T)}</g>')
    for i, (hx, hy) in enumerate(heads):
        rr = [13 * s for _, _, s in shots][i] + 9
        il.append(f'<circle cx="{n(hx)}" cy="{n(hy)}" r="{n(rr)}" fill="none" stroke="{ORANGE}" stroke-width="3.5">'
                  f'{step("opacity", "0", "1", 6.0 + i * 0.18, 0.25, T)}</circle>')
    il.append(text(F.mono, "SAME FACE, EVERY SHOT", 16, 556, 396, INK, 1.4))
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    b.append(caption(F, "Script in. Cinematic storyboard out.", INK))
    b.append(facts(F, "AN LLM PLANS THE SHOTS  ·  FLUX.2 DRAWS THEM  ·  CLIP + ARCFACE CHECK  ·  OWN LORA  ·  ALPHA", INK))
    b.append(title(F, "VIVID", INK, 632))
    return poster(H, LIME, "\n".join(b), "Vivid. A script is typed out, six storyboard frames fill in, and each is checked so the same face carries through every shot.", defs)


# ---------------------------------------------------------------- 03 Arrivo
def arrivo(F):
    H, T = 668, 10
    b = [header(F, "03", "ARRIVO", "ANDROID  ·  NOT IN THE STORES YET", PAPER)]
    il = []
    x0, bw, bh, gap = 70, 100, 90, 10
    top, bot, lane = 106, 288, 242
    for row, y in ((0, top), (1, bot)):
        for k in range(6):
            il.append(f'<rect x="{x0+k*(bw+gap)}" y="{y}" width="{bw}" height="{bh}" rx="8" fill="none" stroke="{PAPER}" stroke-opacity=".32" stroke-width="2"/>')
    il.append(f'<path d="M40 {lane}H770" stroke="{PAPER}" stroke-opacity=".18" stroke-width="2" stroke-dasharray="3 14"/>')
    cars = [(0, 1, LIME, 1.0), (1, 3, ORANGE, 2.1), (0, 4, PINK, 3.2), (1, 0, "#5a66ff", 4.3), (0, 2, PAPER, 5.4)]
    free = []
    for row, k, col, dl in cars:
        cx = x0 + k * (bw + gap) + bw / 2
        by = (top if row == 0 else bot) + bh / 2
        length = cx + 70 + abs(by - lane)
        dur = length / 330
        kt = f"0;{dl/T:.4f};{(dl+dur)/T:.4f};1"
        il.append(f'<g><rect x="-31" y="-17" width="62" height="34" rx="9" fill="{col}"/><rect x="6" y="-12" width="14" height="24" rx="4" fill="{INK}" fill-opacity=".45"/>'
                  f'<animateMotion path="M-70 {lane}H{n(cx)}V{n(by)}" dur="{T}s" repeatCount="indefinite" rotate="auto" '
                  f'keyPoints="0;0;1;1" keyTimes="{kt}" calcMode="linear"/></g>')
        free.append(dl + dur)
    il.append(text(F.mono, "BAYS", 17, 880, 128, PAPER, 3, extra='opacity=".75"'))
    for i in range(12):
        sx, sy = 880 + (i % 4) * 48, 148 + (i // 4) * 48
        dead = [5, 2, 9, 0, 7]
        if i in dead:
            t = free[dead.index(i)]
            il.append(f'<rect x="{sx}" y="{sy}" width="38" height="38" rx="7" fill="#2a2a33">{step("fill", LIME, "#2a2a33", t, 0.15, T)}</rect>')
        else:
            il.append(f'<rect x="{sx}" y="{sy}" width="38" height="38" rx="7" fill="{LIME}"/>')
    il.append(f'<g transform="rotate(-5 1000 358)"><rect x="868" y="318" width="284" height="76" rx="14" fill="{ORANGE}"/>'
              + text(F.mono, "ON ANDROID PHONES.", 17, 888, 348, INK, 1.4) + text(F.mono, "APP STORES: NOT YET.", 17, 888, 376, INK, 1.4) + '</g>')
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    b.append(caption(F, "A parking app for an airport car-park operator.", PAPER))
    b.append(facts(F, "REACT NATIVE  ·  EXPO  ·  HONO  ·  NEON  ·  17 DAYS  ·  236 COMMITS", PAPER))
    b.append(title(F, "ARRIVO", PAPER, 632))
    return poster(H, INK, "\n".join(b), "Arrivo. Cars glide into parking bays and the free-bay counter drops. It runs on Android phones and is not in the app stores yet.")


# ---------------------------------------------------------------- 04 Kanata
def kanata(F):
    H, hy = 620, 392
    r = rng(3)
    defs = (f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1fb8"/><stop offset=".45" stop-color="{COBALT}"/>'
            f'<stop offset=".72" stop-color="{PINK}"/><stop offset="1" stop-color="#ffb347"/></linearGradient>')
    b = [f'<rect width="{W}" height="{hy}" fill="url(#sky)"/>']
    for i in range(46):
        x, y = r.uniform(30, W - 30), r.uniform(80, 250)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.choice([1.2,1.6,2.2])}" fill="{PAPER}"><animate attributeName="opacity" values=".15;1;.15" dur="{r.uniform(2,5):.1f}s" begin="-{r.uniform(0,4):.1f}s" repeatCount="indefinite"/></circle>')
    sx, sy = 880, hy - 30
    b.append(f'<g><g>'
             f'<circle cx="{sx}" cy="{sy}" r="150" fill="none" stroke="#fff4cf" stroke-opacity=".18" stroke-width="2"/>'
             f'<circle cx="{sx}" cy="{sy}" r="112" fill="none" stroke="#fff4cf" stroke-opacity=".32" stroke-width="3"/>'
             f'<circle cx="{sx}" cy="{sy}" r="76" fill="#fff4cf"/>'
             f'<animateTransform attributeName="transform" type="translate" values="0 190;0 190;0 0;0 0" keyTimes="0;0.05;0.62;1" dur="5.5s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;0.2 0.7 0.2 1;0 0 1 1"/></g></g>')
    b.append(f'<rect y="{hy}" width="{W}" height="{H-hy}" fill="{INK}"/><rect y="{hy}" width="{W}" height="3" fill="#fff4cf"/>')
    b.append(header(F, "04", "KANATA", "KANATA.STUDIO  ↗", PAPER))
    # the kanji, as outlines
    jp = "".join(g[0] for g in F.jp.glyphs("彼方", 150, 44, 250))
    b.append(f'<path d="{jp}" fill="{PAPER}"/>')
    b.append(text(F.serif, "far beyond.", 44, 52, 304, PAPER))
    b.append(text(F.mono, "A DESIGN AND ENGINEERING STUDIO. EARLY DAYS.", 17, 52, 340, PAPER, 1.4, extra='opacity=".9"'))
    b.append(title(F, "KANATA", PAPER, 590))
    return poster(H, INK, "\n".join(b), "Kanata, 彼方, far beyond. A design and engineering studio. A sun rises over a horizon.", defs)


# ---------------------------------------------------------------- 05 Tabla Tuner
def tabla(F):
    H, T = 712, 8
    dx, dy, R = 880, 242, 150
    b = [header(F, "05", "TABLA TUNER", "TABLA-TUNER.VERCEL.APP  ↗", INK)]
    il = []
    il.append(f'<circle cx="{dx}" cy="{dy}" r="{R+30}" fill="{INK}"/>')
    for i in range(16):  # the lace
        a = math.radians(i * 22.5)
        x1, y1 = dx + (R + 4) * math.cos(a), dy + (R + 4) * math.sin(a)
        x2, y2 = dx + (R + 38) * math.cos(a + 0.2), dy + (R + 38) * math.sin(a + 0.2)
        il.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{PAPER}" stroke-width="3" stroke-opacity=".55" stroke-linecap="round"/>')
    il.append(f'<circle cx="{dx}" cy="{dy}" r="{R}" fill="{PAPER}"/><circle cx="{dx}" cy="{dy}" r="64" fill="{INK}"/>'
              f'<circle cx="{dx}" cy="{dy}" r="64" fill="none" stroke="{PAPER}" stroke-opacity=".25" stroke-width="2" transform="scale(1)"/>')
    tx, ty = dx - 96, dy - 44
    ripples = "".join(
        f'<circle cx="{tx}" cy="{ty}" r="6" fill="none" stroke="{INK}" stroke-width="3">'
        f'<animate attributeName="r" values="6;230" dur="2.6s" begin="{1.0+i*0.55}s;{1.0+i*0.55+T}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values=".9;0" dur="2.6s" begin="{1.0+i*0.55}s" repeatCount="indefinite"/></circle>' for i in range(4))
    il.append(f'<clipPath id="skin"><circle cx="{dx}" cy="{dy}" r="{R}"/></clipPath><g clip-path="url(#skin)">{ripples}</g>')
    il.append(f'<circle cx="{tx}" cy="{ty}" r="9" fill="{ORANGE}"/>')
    # the cents meter
    mx, my, mr = 330, 350, 215
    il.append(f'<path d="M{mx-mr*math.sin(math.radians(52)):.1f} {my-mr*math.cos(math.radians(52)):.1f}A{mr} {mr} 0 0 1 {mx+mr*math.sin(math.radians(52)):.1f} {my-mr*math.cos(math.radians(52)):.1f}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    for c in range(-50, 51, 10):
        a = math.radians(c * 52 / 50)
        l = 24 if c % 50 == 0 or c == 0 else 14
        il.append(f'<path d="M{mx+(mr-6)*math.sin(a):.1f} {my-(mr-6)*math.cos(a):.1f}L{mx+(mr-6-l)*math.sin(a):.1f} {my-(mr-6-l)*math.cos(a):.1f}" stroke="{INK}" stroke-width="{4 if c==0 else 2.5}"/>')
    il.append(text(F.mono, "-50", 16, mx - 190, my - 76, INK, 1, "middle") + text(F.mono, "+50", 16, mx + 190, my - 76, INK, 1, "middle")
              + text(F.mono, "CENTS", 16, mx, my - mr - 18, INK, 3, "middle"))
    vals = "-48;22;-13;6;-2;0;0"
    il.append(f'<g><path d="M{mx} {my}L{mx} {my-mr+14}" stroke="{ORANGE}" stroke-width="5" stroke-linecap="round"/><circle cx="{mx}" cy="{my}" r="12" fill="{INK}"/>'
              f'<animateTransform attributeName="transform" type="rotate" values="{vals.replace(";", f" {mx} {my};")} {mx} {my}" '
              f'keyTimes="0;.18;.3;.4;.48;.56;1" dur="{T}s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1;0 0 1 1"/></g>')
    il.append(f'<g>{text(F.disp, "-48¢", 54, mx, my + 78, INK, 0, "middle")}{animate("opacity", "1;1;0;0", f"0;.1;.3;1", T)}</g>'
              f'<g>{text(F.disp, "0¢", 54, mx, my + 78, INK, 0, "middle")}{text(F.mono, "IN TUNE.", 17, mx, my + 110, INK, 3, "middle")}{animate("opacity", "0;0;1;1", "0;.5;.6;1", T)}</g>')
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    b.append(caption(F, "Ten years of tabla. I never once managed to tune it.", INK, 514))
    b.append(facts(F, "HAND-WRITTEN PITCH DETECTION  ·  NO SERVER  ·  THE SOUND NEVER LEAVES YOUR PHONE", INK, 556))
    b.append(title(F, "TABLA TUNER", INK, 684, 150))
    return poster(H, PINK, "\n".join(b), "Tabla Tuner. A tabla skin ripples when struck while a cents needle swings and settles on zero, in tune.")


# ---------------------------------------------------------------- 06 From Zero to Mozart
def mozart(F):
    H, T = 470, 10
    b = [header(F, "06", "FROM ZERO TO MOZART", "IN PROGRESS", INK)]
    il = []
    ys = [128, 142, 156, 170, 184]
    for y in ys:
        il.append(f'<path d="M48 {y}H{W-48}" stroke="{INK}" stroke-width="2" stroke-opacity=".5"/>')
    pitch = {"E": 184, "F": 177, "G": 170, "D": 191, "C": 198}
    seq = "EEFGGFEDCCDEEDD"
    x0, px = 110, 66
    il.append(f'<path d="M{x0+8*px-20} 198h40" stroke="{INK}" stroke-width="2" stroke-opacity=".5"/>'.replace(str(x0+8*px-20), str(x0+8*px-20)))
    il.append(f'<path d="M{x0+9*px-20} 198h40" stroke="{INK}" stroke-width="2" stroke-opacity=".5"/>')
    for i, ch in enumerate(seq):
        x, y = x0 + i * px, pitch[ch]
        t = i / len(seq)
        hit = 0.7 + t * 0.9 * 1  # playhead time of arrival, seconds into a 9 s sweep
        hit = 0.8 + i * (7.6 / len(seq))
        k = f"0;{hit/T:.4f};{(hit+.12)/T:.4f};{(hit+.9)/T:.4f};1"
        il.append(f'<g><ellipse cx="{x}" cy="{y}" rx="11.5" ry="8.5" transform="rotate(-20 {x} {y})" fill="{INK}">'
                  f'<animate attributeName="fill" values="{INK};{INK};{COBALT};{INK};{INK}" keyTimes="{k}" dur="{T}s" repeatCount="indefinite"/></ellipse>'
                  f'<path d="M{x+10.5} {y-3}V{y-50}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
                  f'{step("opacity", "0", "1", 0.2 + i*0.04, 0.3, T)}</g>')
    il.append(f'<rect x="{x0-30}" y="108" width="3" height="106" fill="{COBALT}">'
              f'<animate attributeName="x" values="{x0-34};{x0-34};{x0+14*px+20};{x0+14*px+20}" keyTimes="0;{0.7/T:.4f};{8.6/T:.4f};1" dur="{T}s" repeatCount="indefinite"/></rect>')
    b.append(f'<g>{"".join(il)}{fade_out(T)}</g>')
    b.append(text(F.serif, "I just started the violin. Ode to Joy, then Mozart.", 36, 48, 290, INK))
    b.append(text(F.mono, "A 193-PAGE COURSE PDF, REBUILT AS A CALM SITE TO READ WITH THE VIOLIN IN YOUR HANDS.", 16, 48, 326, INK, 1.2, extra='opacity=".78"'))
    b.append(text(F.mono, "PHASE 0: PLANNED AND SCAFFOLDED. FIRST LESSON TO COME.", 16, 48, 354, INK, 1.2, extra='opacity=".78"'))
    size, tr = fit(F.disp, "FROM ZERO TO MOZART", 80, PAGE, -0.02)
    b.append(text(F.disp, "FROM ZERO TO MOZART", size, 44, 438, INK, tr))
    return poster(H, PAPER, "\n".join(b), "From Zero to Mozart. Notes of Ode to Joy light up one by one on a staff as a playhead passes. I just started the violin.")


# ---------------------------------------------------------------- closing
def hello(F):
    H = 380
    b = [text(F.mono, "OPEN TO ROLES AND OPPORTUNITIES", 18, 48, 60, INK, 3)]
    size, tr = fit(F.disp, "SAY HELLO.", 200, PAGE - 60, -0.02)
    base = 222
    b.append(text(F.disp, "SAY HELLO.", size, 44, base, INK, tr))
    cx = 44 + F.disp.width("SAY HELLO.", size, tr) + 22
    b.append(f'<rect x="{n(cx)}" y="{base-size*0.72:.0f}" width="{n(size*0.14)}" height="{size*0.72:.0f}" fill="{INK}">'
             f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')
    b.append(text(F.mono, "PARTHTI2003@GMAIL.COM", 24, 48, 280, INK, 3))
    b.append(text(F.mono, "BUILT WITH CLAUDE CODE AND CODEX. WHAT TO BUILD, WHAT TO MEASURE AND WHAT TO THROW AWAY IS MY CALL.", 14, 48, 332, INK, 1.0, extra='opacity=".72"'))
    b.append(text(F.mono, "EVERY POSTER ON THIS PAGE IS GENERATED BY CODE IN /SCRIPTS.", 14, 48, 354, INK, 1.0, extra='opacity=".72"'))
    return poster(H, LIME, chr(10).join(b), "Say hello. Open to roles and opportunities. parthti2003@gmail.com. Built with Claude Code and Codex; what to build, measure and throw away is my call.")


def pill(F, label, bg, fg):
    w = F.disp.width(label, 21, 1.5) + 64
    h = 60
    border = f'<rect x="1" y="1" width="{n(w-2)}" height="{h-2}" rx="29" fill="none" stroke="{fg}" stroke-opacity=".25" stroke-width="2"/>'
    body = f'<rect width="{n(w)}" height="{h}" rx="30" fill="{bg}"/>{border}' + text(F.disp, label, 21, 32, 38, fg, 1.5)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{n(w)}" height="{h}" viewBox="0 0 {n(w)} {h}" role="img" aria-label="{label.title()}">'
            f'{body}</svg>' + chr(10))


def social_card(F):
    """1280x640 card for link previews (GitHub repo social preview, Open Graph). Same hero, wider."""
    import build_posters as me
    old = me.W
    me.W = 1280
    try:
        svg = hero(F)
    finally:
        me.W = old
    return svg.replace('width="1200"', 'width="1280"').replace('viewBox="0 0 1200 640"', 'viewBox="0 0 1280 640"')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "assets"))
    a = ap.parse_args()
    F = Fonts(a.fonts)
    os.makedirs(a.out, exist_ok=True)
    for name, label, bg, fg in (("pill-portfolio", "PORTFOLIO", COBALT, PAPER), ("pill-kanata", "KANATA", LIME, INK),
                                ("pill-linkedin", "LINKEDIN", PINK, INK), ("pill-email", "EMAIL", PAPER, INK),
                                ("pill-repos", "ALL REPOSITORIES", INK, PAPER)):
        with open(os.path.join(a.out, f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(pill(F, label, bg, fg))
    with open(os.path.join(a.out, "social-card.svg"), "w", encoding="utf-8") as f:
        f.write(social_card(F))
    for name, fn in (("hero", hero), ("p01-beatmind", beatmind), ("p02-vivid", vivid), ("p03-arrivo", arrivo),
                     ("p04-kanata", kanata), ("p05-tabla", tabla), ("p06-mozart", mozart), ("hello", hello)):
        with open(os.path.join(a.out, f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(fn(F))
        print("wrote", name)
