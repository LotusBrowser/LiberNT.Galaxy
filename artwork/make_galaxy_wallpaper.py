#!/usr/bin/env python3
"""Generate the placeholder Galaxy wallpaper (1920x1080, procedural, no external assets).

    python3 artwork/make_galaxy_wallpaper.py [output.png]

Default output: modules/wallpapers/Galaxy.png
To use your own artwork instead, just overwrite that file with your own PNG
(1920x1080 or larger, 16:9); nothing else needs to change.
"""
import os
import sys

import numpy as np
from PIL import Image, ImageFilter

W, H = 1920, 1080
BG = np.array([11, 11, 43], np.float32)
SURFACE = np.array([21, 21, 61], np.float32)
ACCENT = np.array([123, 47, 247], np.float32)
ACCENT_LIGHT = np.array([179, 136, 255], np.float32)
TEXT = np.array([234, 230, 255], np.float32)

rng = np.random.default_rng(20261107)


def fbm(octaves=7, base=4, persistence=0.55):
    """Fractal value noise in 0..1, built from upsampled random grids."""
    acc = np.zeros((H, W), np.float32)
    amp, total = 1.0, 0.0
    for o in range(octaves):
        gw, gh = base * 2 ** o, int(base * 2 ** o * H / W) + 2
        g = rng.random((gh, gw)).astype(np.float32)
        img = Image.fromarray((g * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
        acc += amp * np.asarray(img, np.float32) / 255.0
        total += amp
        amp *= persistence
    acc /= total
    return (acc - acc.min()) / (acc.max() - acc.min())


yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
u, v = xx / W, yy / H

# Deep navy base, drifting toward purple at the lower right.
t = np.clip(0.55 * u + 0.45 * v, 0, 1)[..., None]
img = BG * (1 - t) + SURFACE * t

# Galactic band: a tilted gaussian ridge, modulated by noise.
ang = np.deg2rad(-24)
d = (u - 0.5) * np.sin(ang) * (W / H) + (v - 0.52) * np.cos(ang)
band = np.exp(-(d / 0.20) ** 2)
n1, n2, n3 = fbm(), fbm(base=3), fbm(base=6, persistence=0.62)
neb = np.clip(band * (0.35 + 1.15 * n1) - 0.12, 0, 1) ** 1.25
core = np.exp(-(d / 0.07) ** 2) * (0.4 + 0.9 * n2)

col = np.zeros((H, W, 3), np.float32)
tt = np.clip(neb * 1.5, 0, 1)[..., None]
col += (BG * 0.0 + SURFACE) * (1 - tt) + ACCENT * tt * 0.9
col += (ACCENT_LIGHT * 0.55)[None, None, :] * (np.clip(core, 0, 1) ** 1.6)[..., None]
col += TEXT * 0.20 * (np.clip(core - 0.55, 0, 1) ** 1.4)[..., None]
img += (col - SURFACE * (1 - tt)) * np.clip(neb * 1.8, 0, 1)[..., None]

# Dust lanes darken the band.
dust = np.clip((n3 - 0.52) * 3.2, 0, 1) * band
img *= (1 - 0.65 * dust)[..., None]
# A second, faint violet wash in the upper-left so the whole frame has depth.
wash = np.exp(-(((u - 0.12) / 0.45) ** 2 + ((v - 0.1) / 0.5) ** 2)) * n2
img += ACCENT[None, None, :] * (0.16 * wash)[..., None]

# Stars on a separate float layer; denser inside the band.
stars = np.zeros((H, W), np.float32)
density = 0.35 + 0.65 * np.clip(band + 0.25 * n1, 0, 1)
pts = rng.random((9000, 2))
for px, py in pts:
    x, y = int(px * W), int(py * H)
    if rng.random() < density[y, x]:
        stars[y, x] = max(stars[y, x], 0.15 + 0.85 * rng.random() ** 3)
glow = np.asarray(Image.fromarray((np.clip(stars, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1)), np.float32) / 255.0
stars = np.clip(stars + glow * 1.6, 0, 1)

big = np.zeros((H, W), np.float32)
for _ in range(120):                       # medium stars
    x, y = int(rng.random() * W), int(rng.random() * H)
    big[y, x] = 0.5 + 0.5 * rng.random()
bigb = np.asarray(Image.fromarray((big * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2.2)), np.float32) / 255.0
stars = np.clip(stars + bigb * 9.0, 0, 1)

spike = np.zeros((H, W), np.float32)
for _ in range(9):                         # a few bright stars with diffraction spikes
    x, y = int(rng.integers(60, W - 60)), int(rng.integers(60, H - 60))
    L = int(rng.integers(18, 46))
    for k in range(-L, L + 1):
        f = (1 - abs(k) / L) ** 2
        spike[y, min(max(x + k, 0), W - 1)] += f
        spike[min(max(y + k, 0), H - 1), x] += f
    spike[y - 1:y + 2, x - 1:x + 2] += 2.0
spb = np.asarray(Image.fromarray((np.clip(spike, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)), np.float32) / 255.0
spglow = np.asarray(Image.fromarray((np.clip(spike, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(7)), np.float32) / 255.0
stars = np.clip(stars + spb + spglow * 0.8, 0, 1)

tint = rng.random((H, W, 1)).astype(np.float32)           # star colour: white <-> lavender
star_col = np.ones((H, W, 3), np.float32) * 255 * (1 - 0.25 * tint) + ACCENT_LIGHT * 0.25 * tint
img = img * (1 - stars[..., None] * 0.9) + star_col * stars[..., None]

# Vignette, then a touch of dither so the dark gradients do not band.
vig = 1 - 0.45 * (((u - 0.5) * 1.15) ** 2 + ((v - 0.5) * 1.3) ** 2)
img *= np.clip(vig, 0.5, 1)[..., None]
img += rng.normal(0, 0.8, img.shape).astype(np.float32)

out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")
dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "modules", "wallpapers", "Galaxy.png")
out.save(dest, optimize=True)
print("wrote", os.path.abspath(dest), out.size)
