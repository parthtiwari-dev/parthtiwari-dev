"""Shared toolkit for the poster art. Text becomes SVG outlines (shaped with HarfBuzz, so kerning is
right), because README images cannot load web fonts. Fonts are not stored in the repo, all are OFL:
  Unbounded, Instrument Serif Italic, JetBrains Mono, Inter, Noto Sans JP  (github.com/google/fonts)
Needs: pip install fonttools uharfbuzz"""
import io
import os
import random

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

INK, PAPER = "#0c0c10", "#f4f1ea"
COBALT, LIME, PINK, ORANGE = "#2b3dff", "#c8ff2e", "#ff5fa8", "#ff4a1c"
W = 1200


def n(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Face:
    def __init__(self, path, axes=None, only=None):
        import hashlib
        key = os.path.join(os.path.dirname(path), "cache-" + hashlib.md5(
            f"{os.path.basename(path)}{sorted((axes or {}).items())}{only}".encode()).hexdigest()[:10] + ".ttf")
        if os.path.exists(key):
            f = TTFont(key)
        else:
            f = TTFont(path)
            if only:  # keep just these characters, so a huge CJK font loads fast
                from fontTools import subset
                sub = subset.Subsetter()
                sub.populate(text=only)
                sub.subset(f)
            if axes:
                f = instancer.instantiateVariableFont(f, axes)
            f.save(key)
            f = TTFont(key)
        buf = io.BytesIO()
        f.save(buf)
        self.hbfont = hb.Font(hb.Face(hb.Blob(buf.getvalue())))
        self.gs, self.order, self.upm = f.getGlyphSet(), f.getGlyphOrder(), f["head"].unitsPerEm
        self.cmap = f.getBestCmap()

    def shape(self, text):
        b = hb.Buffer()
        b.add_str(text)
        b.guess_segment_properties()
        hb.shape(self.hbfont, b, {"kern": True, "liga": False})
        return b.glyph_infos, b.glyph_positions

    def glyphs(self, text, size, x=0.0, y=0.0, tracking=0.0):
        """[(path d, x of glyph, advance)] for each glyph, baseline at y."""
        s, out, cx = size / self.upm, [], x
        infos, pos = self.shape(text)
        for info, p in zip(infos, pos):
            pen = SVGPathPen(self.gs, ntos=n)
            self.gs[self.order[info.codepoint]].draw(
                TransformPen(pen, (s, 0, 0, -s, cx + p.x_offset * s, y - p.y_offset * s)))
            adv = p.x_advance * s + tracking
            out.append((pen.getCommands(), cx, adv))
            cx += adv
        return out

    def width(self, text, size, tracking=0.0):
        infos, pos = self.shape(text)
        return sum(p.x_advance for p in pos) * size / self.upm + tracking * len(text)

    def wrap(self, text, size, maxw, tracking=0.0):
        lines, cur = [], ""
        for word in text.split():
            t = f"{cur} {word}".strip()
            if cur and self.width(t, size, tracking) > maxw:
                lines.append(cur)
                cur = word
            else:
                cur = t
        return lines + [cur]


class Fonts:
    def __init__(self, d):
        j = lambda f: os.path.join(d, f)
        self.disp = Face(j("Unbounded.ttf"), {"wght": 800})  # 900 has broken glyphs (B, R, E)
        self.disp8 = Face(j("Unbounded.ttf"), {"wght": 800})
        self.serif = Face(j("InstrumentSerif-Italic.ttf"))
        self.mono = Face(j("JetBrainsMono.ttf"), {"wght": 700})
        self.monoL = Face(j("JetBrainsMono.ttf"), {"wght": 500})
        self.body = Face(j("Inter-var.ttf"), {"wght": 600, "opsz": 18})
        self.jp = Face(j("NotoSansJP.ttf"), {"wght": 900}, only="彼方")


def text(face, s, size, x, y, fill, tracking=0.0, anchor="start", extra=""):
    """One <path> with the whole line. anchor: start | middle | end."""
    w = face.width(s, size, tracking) - tracking
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    d = "".join(g[0] for g in face.glyphs(s, size, x0, y, tracking))
    return f'<path d="{d}" fill="{fill}" {extra}/>'


def animate(attr, values, keys, total, extra=""):
    return (f'<animate attributeName="{attr}" values="{values}" keyTimes="{keys}" dur="{n(total)}s" '
            f'begin="0s" repeatCount="indefinite" {extra}/>')


def step(attr, v0, v1, delay, dur, total, loop=True, ease="0.2 0.8 0.2 1"):
    """Hold v0, ease to v1 between delay and delay+dur, hold v1. The element's own attribute is the
    END state, so a viewer that does not run SVG animation still sees the finished poster.
    loop=False plays once and stays."""
    k = [0, delay / total, min((delay + dur) / total, 0.9999), 1]
    keys = ";".join(str(x) if x in (0, 1) else f"{x:.4f}" for x in k)
    rep = 'repeatCount="indefinite"' if loop else 'fill="freeze"'
    return (f'<animate attributeName="{attr}" values="{v0};{v0};{v1};{v1}" keyTimes="{keys}" '
            f'dur="{n(total)}s" begin="0s" {rep} calcMode="spline" keySplines="0 0 1 1;{ease};0 0 1 1"/>')


def step_move(delay, dur, total, frm, to, loop=True, ease="0.2 0.8 0.2 1"):
    """translate animation, same hold-then-move pattern."""
    k = [0, delay / total, min((delay + dur) / total, 0.9999), 1]
    keys = ";".join(str(x) if x in (0, 1) else f"{x:.4f}" for x in k)
    rep = 'repeatCount="indefinite"' if loop else 'fill="freeze"'
    return (f'<animateTransform attributeName="transform" type="translate" values="{frm};{frm};{to};{to}" '
            f'keyTimes="{keys}" dur="{n(total)}s" begin="0s" {rep} calcMode="spline" '
            f'keySplines="0 0 1 1;{ease};0 0 1 1"/>')


def fade_out(total, lead=0.5):
    """Wrap-up fade so a looping poster restarts clean."""
    return animate("opacity", "1;1;0", f"0;{(total-lead)/total:.4f};1", total)


def poster(h, bg, body, label, defs="", w=W):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}">\n<defs><clipPath id="pf"><rect width="{w}" height="{h}" rx="22"/>'
            f'</clipPath>{defs}</defs>\n<g clip-path="url(#pf)">\n<rect width="{w}" height="{h}" fill="{bg}"/>\n'
            f'{body}\n</g>\n</svg>\n')


def header(F, no, left, right, fg):
    """The strip every poster shares: number and name on the left, address on the right."""
    return (text(F.mono, f"{no}  /  {left}", 18, 48, 60, fg, 2.2) + text(F.mono, right, 18, W - 48, 60, fg, 2.2, "end"))


def fit(face, s, size_max, maxw, tracking_em=0.0):
    """Largest size (up to size_max) at which the line fits maxw. Returns (size, tracking px)."""
    w100 = face.width(s, 100, tracking_em * 100) - tracking_em * 100
    size = min(size_max, maxw / w100 * 100)
    return size, tracking_em * size


def bars(rng, count, x0, pitch, bw, cy, maxh, minh, color, dur=(0.8, 2.2), stroke=""):
    """A row of audio-meter bars, each pulsing with its own rhythm."""
    out = []
    for i in range(count):
        cx = x0 + i * pitch
        env = 0.45 + 0.55 * abs(((i * 0.37) % 2) - 1)
        a, b = rng.uniform(minh, maxh * env), rng.uniform(minh, maxh * env)
        c = rng.uniform(minh, maxh * env)
        d, ph = rng.uniform(*dur), rng.uniform(0, 2)
        out.append(
            f'<g transform="translate({n(cx)} {n(cy)})"><rect x="{n(-bw/2)}" y="-50" width="{n(bw)}" height="100" '
            f'rx="{n(bw/2)}" fill="{color}" {stroke} transform="scale(1 {a/100:.3f})">'
            f'<animateTransform attributeName="transform" type="scale" values="1 {a/100:.3f};1 {b/100:.3f};'
            f'1 {c/100:.3f};1 {a/100:.3f}" dur="{d:.2f}s" begin="-{ph:.2f}s" repeatCount="indefinite"/></rect></g>')
    return "".join(out)


def rng(seed):
    return random.Random(seed)
