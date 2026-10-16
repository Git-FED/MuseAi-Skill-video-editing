#!/usr/bin/env python3
"""Overlay clean, readable captions onto the comical promo illustrations.

The illustrations are generated art; the captions are drawn here so the text is
always crisp and correct (generated art renders text unreliably). Output goes to
promo/promo-*.png. Source art lives in promo/_src-*.png.

No network access. No credentials.

Usage:
    python3 scripts/make-promos.py
"""
from __future__ import annotations

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROMO = os.path.join(ROOT, "promo")

BG = (7, 7, 10)
CYAN = (0, 240, 255)
VIOLET = (112, 0, 255)
INK = (233, 236, 245)
MUTED = (168, 176, 196)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# (source, output, headline, subhead)
CARDS = [
    ("_src-1.png", "promo-1-one-repo-per-skill.png",
     "One repo per skill.", "Not one drawer of everything."),
    ("_src-2.png", "promo-2-no-credentials.png",
     "No credentials in the repo.", "The bouncer says no."),
    ("_src-3.png", "promo-3-canonical-links.png",
     "Canonical links only.", "Untangle the checkout URL."),
    ("_src-4.png", "promo-4-no-fake-gates.png",
     "No fake gates.", "A checkbox is not a lock."),
]


def fit(path, text, max_w, start):
    size = start
    while size > 12:
        f = ImageFont.truetype(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, 12)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def gradient_bar(size, c0=CYAN, c1=VIOLET):
    w, h = size
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = x / max(1, w - 1)
            px[x, y] = tuple(round(c0[i] + (c1[i] - c0[i]) * t) for i in range(3))
    return img


def make_card(src, out, headline, subhead):
    img = Image.open(os.path.join(PROMO, src)).convert("RGBA")
    W, H = img.size

    # Bottom scrim: dark gradient so text always reads
    scrim_h = int(H * 0.42)
    scrim = Image.new("RGBA", (W, scrim_h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for y in range(scrim_h):
        a = int(235 * (y / scrim_h) ** 0.9)
        sd.line([(0, y), (W, y)], fill=(7, 7, 10, a))
    img.alpha_composite(scrim, (0, H - scrim_h))

    d = ImageDraw.Draw(img)

    # Accent bar
    bar = gradient_bar((W, 8)).convert("RGBA")
    img.alpha_composite(bar, (0, H - scrim_h))

    pad = int(W * 0.06)
    y = H - scrim_h + int(scrim_h * 0.20)

    hl_font = fit(FONT_BOLD, headline, W - 2 * pad, start=int(W * 0.075))
    d.text((pad, y), headline, font=hl_font, fill=INK)
    y += hl_font.size + int(W * 0.012)

    sub_font = ImageFont.truetype(FONT_REG, int(W * 0.040))
    d.text((pad, y), subhead, font=sub_font, fill=CYAN)

    # Corner tag
    tag_font = ImageFont.truetype(FONT_BOLD, int(W * 0.026))
    tag = "FED-OS Muse Skills"
    tw = d.textlength(tag, font=tag_font)
    d.text((W - pad - tw, int(W * 0.045)), tag, font=tag_font, fill=MUTED)

    out_path = os.path.join(PROMO, out)
    img.convert("RGB").save(out_path, "PNG")
    print("wrote", out_path)


if __name__ == "__main__":
    for src, out, hl, sub in CARDS:
        make_card(src, out, hl, sub)
