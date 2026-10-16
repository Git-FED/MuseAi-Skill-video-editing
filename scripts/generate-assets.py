#!/usr/bin/env python3
"""Generate raster favicon variants from the canonical FED-OS mark.

The social preview is a finished artwork in site/assets/images and is not
regenerated here. Requires Pillow.
Usage: python3 scripts/generate-assets.py
"""
from __future__ import annotations

import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG_DIR = os.path.join(ROOT, "site", "assets", "images")
BG = (7, 7, 10, 255)
CYAN = (0, 240, 255)
VIOLET = (112, 0, 255)
HEX = [(32, 7), (53, 19), (53, 45), (32, 57), (11, 45), (11, 19)]
F_SHAPE = [(24, 23), (42, 23), (42, 28), (29, 28), (29, 32),
           (39, 32), (39, 37), (29, 37), (29, 45), (24, 45)]


def gradient(size: tuple[int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size)
    pixels = image.load()
    denominator = max(1, width + height - 2)
    for y in range(height):
        for x in range(width):
            t = (x + y) / denominator
            pixels[x, y] = tuple(
                round(CYAN[i] + (VIOLET[i] - CYAN[i]) * t) for i in range(3)
            )
    return image


def scale_points(points: list[tuple[int, int]], size: int) -> list[tuple[int, int]]:
    scale = size / 64
    return [(round(x * scale), round(y * scale)) for x, y in points]


def draw_mark(size: int = 256) -> Image.Image:
    mark = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(mark).rounded_rectangle(
        [0, 0, size - 1, size - 1], radius=round(size * 14 / 64), fill=BG
    )
    color = gradient((size, size)).convert("RGBA")
    hex_points = scale_points(HEX, size)
    hex_mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(hex_mask).line(
        hex_points + [hex_points[0]], fill=255,
        width=max(1, round(size * 3.5 / 64)), joint="curve"
    )
    f_mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(f_mask).polygon(scale_points(F_SHAPE, size), fill=255)
    mark.paste(color, (0, 0), hex_mask)
    mark.paste(color, (0, 0), f_mask)
    return mark


def main() -> None:
    os.makedirs(IMG_DIR, exist_ok=True)
    mark = draw_mark()
    png_path = os.path.join(IMG_DIR, "favicon.png")
    ico_path = os.path.join(IMG_DIR, "favicon.ico")
    mark.save(png_path, "PNG", optimize=True)
    mark.save(ico_path, "ICO", sizes=[(16, 16), (32, 32), (48, 48),
                                      (64, 64), (128, 128), (256, 256)])
    print("wrote", png_path)
    print("wrote", ico_path)


if __name__ == "__main__":
    main()
