#!/usr/bin/env python3
"""Generate raster assets (favicon.ico, social-preview.png) for FED-OS Muse Skills.

The SVG sources (favicon.svg, logo.svg) are the canonical art. This script
re-draws the same geometry with Pillow so we can produce an .ico and a PNG
Open Graph image without an SVG rasterizer in the toolchain.

No network access. No credentials. Deterministic output.

Usage:
    python3 scripts/generate-assets.py
"""
from __future__ import annotations

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG_DIR = os.path.join(ROOT, "site", "assets", "images")

# Brand palette (matches site/assets/css/main.css)
BG = (7, 7, 10, 255)          # #07070a
CYAN = (0, 240, 255)          # #00f0ff
VIOLET = (112, 0, 255)        # #7000ff
INK = (233, 236, 245)         # #e9ecf5
MUTED = (150, 158, 178)       # #969eb2

# Hexagon + F geometry, in the 64x64 coordinate space of favicon.svg
HEX = [(32, 7), (53, 19), (53, 45), (32, 57), (11, 45), (11, 19)]
F_SHAPE = [(24, 23), (42, 23), (42, 28), (29, 28), (29, 32),
           (39, 32), (39, 37), (29, 37), (29, 45), (24, 45)]

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def gradient(size, c0=CYAN, c1=VIOLET):
    """Diagonal linear gradient from c0 (top-left) to c1 (bottom-right)."""
    w, h = size
    img = Image.new("RGB", (w, h))
    px = img.load()
    denom = (w - 1) + (h - 1) or 1
    for y in range(h):
        for x in range(w):
            t = (x + y) / denom
            px[x, y] = lerp(c0, c1, t)
    return img


def scale_points(points, s, size):
    """Map 64-space points to a size x size canvas."""
    k = size / 64.0
    return [(round(x * k), round(y * k)) for (x, y) in points]


def draw_hexagon_mark(size, radius_ratio=14 / 64, stroke_ratio=3.5 / 64):
    """Return an RGBA image of the rounded-square hexagon 'F' mark."""
    s = size
    base = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(base)
    r = round(radius_ratio * s)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=r, fill=BG)

    grad = gradient((s, s)).convert("RGBA")

    # Hexagon outline mask
    hex_mask = Image.new("L", (s, s), 0)
    hm = ImageDraw.Draw(hex_mask)
    hm.line(scale_points(HEX, s, s) + [scale_points(HEX, s, s)[0]],
            fill=255, width=max(1, round(stroke_ratio * s)), joint="curve")

    # F glyph mask
    f_mask = Image.new("L", (s, s), 0)
    fm = ImageDraw.Draw(f_mask)
    fm.polygon(scale_points(F_SHAPE, s, s), fill=255)

    base.paste(grad, (0, 0), hex_mask)
    base.paste(grad, (0, 0), f_mask)
    return base


def make_favicon():
    master = draw_hexagon_mark(256)
    png_path = os.path.join(IMG_DIR, "favicon.png")
    master.save(png_path, "PNG")
    ico_path = os.path.join(IMG_DIR, "favicon.ico")
    master.save(ico_path, "ICO",
                sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("wrote", png_path)
    print("wrote", ico_path)


def _fit_font(path, text, max_w, start=140):
    size = start
    while size > 10:
        f = ImageFont.truetype(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, 10)


def gradient_text(img, xy, text, font, c0=CYAN, c1=VIOLET):
    """Paste gradient-colored text onto img at xy (top-left)."""
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    md.text(xy, text, font=font, fill=255)
    bbox = mask.getbbox()
    if not bbox:
        return
    grad = gradient(img.size, c0, c1).convert("RGBA")
    img.paste(grad, (0, 0), mask)


def make_social_preview():
    W, H = 1200, 630
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Faint grid
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill=(255, 255, 255, 8))
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill=(255, 255, 255, 8))

    # Glow blobs
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-180, -220, 380, 320], fill=(0, 240, 255, 40))
    gd.ellipse([W - 360, H - 320, W + 220, H + 200], fill=(112, 0, 255, 46))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)

    # Mark, top-left
    mark = draw_hexagon_mark(150)
    img.paste(mark, (72, 70), mark)

    # Wordmark next to the mark
    wm = ImageFont.truetype(FONT_BOLD, 46)
    d.text((246, 108), "FED-OS", font=wm, fill=INK)
    d.text((246, 158), "Muse Skills", font=wm, fill=MUTED)

    # Headline (gradient)
    hl_font = _fit_font(FONT_BOLD, "One repo per skill.", W - 160, start=96)
    gradient_text(img, (72, 268), "One repo per skill.", hl_font)

    # Subhead
    sub = ImageFont.truetype(FONT_REG, 36)
    d.text((72, 392), "Auditable skills for AI Muse agents.",
           font=sub, fill=INK)

    # Chips
    chips = ["No build step", "No credentials", "Canonical links", "Disclosed referrals"]
    chip_font = ImageFont.truetype(FONT_BOLD, 24)
    x = 72
    y = 486
    for c in chips:
        tw = chip_font.getlength(c)
        pad = 22
        box_w = tw + pad * 2
        d.rounded_rectangle([x, y, x + box_w, y + 54], radius=27,
                            outline=(0, 240, 255, 150), width=2)
        d.text((x + pad, y + 14), c, font=chip_font, fill=INK)
        x += box_w + 16
        if x > W - 220:
            x = 72
            y += 70

    out = os.path.join(IMG_DIR, "social-preview.png")
    img.convert("RGB").save(out, "PNG")
    print("wrote", out)


if __name__ == "__main__":
    os.makedirs(IMG_DIR, exist_ok=True)
    make_favicon()
    make_social_preview()
