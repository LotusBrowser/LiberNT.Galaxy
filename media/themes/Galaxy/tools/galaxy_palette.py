#!/usr/bin/env python3
"""Galaxy palette and colour mapping, shared by the theme tooling.

Palette (LiberNT: Galaxy Edition)
    background   #0B0B2B  (11 11 43)
    surface      #15153D  (21 21 61)
    accent       #7B2FF7  (123 47 247)
    accent-light #B388FF  (179 136 255)
    text         #EAE6FF  (234 230 255)
    highlight    #FFFFFF

map_rgb() takes a colour of the neutral dark/light Win8 theme and returns the
Galaxy equivalent: neutral greys follow a monotone ramp (so light stays light and
dark stays dark, which keeps every glyph and border legible), blues become purple.
"""
import colorsys

BG = (11, 11, 43)
SURFACE = (21, 21, 61)
ACCENT = (123, 47, 247)
ACCENT_LIGHT = (179, 136, 255)
TEXT = (234, 230, 255)
WHITE = (255, 255, 255)

# grey level (0..255) -> Galaxy colour. Anchors are interpolated linearly.
GRAY_ANCHORS = [
    (0, (5, 5, 26)),
    (16, BG),
    (32, SURFACE),
    (48, (33, 33, 82)),
    (64, (58, 58, 124)),
    (90, (72, 68, 140)),
    (128, (154, 148, 200)),   # was GrayText: must stay readable on SURFACE
    (180, (200, 194, 235)),
    (240, TEXT),
    (255, WHITE),
]

# Exact colours of the Win8 theme that have a dedicated Galaxy colour.
EXACT = {
    (0, 120, 215): ACCENT,          # highlight / accent blue
    (96, 205, 255): ACCENT_LIGHT,   # hot tracking blue
}

BLUE_SHIFT = 265.0 - 208.0   # hue of ACCENT minus hue of (0,120,215)


def _gray(level):
    level = max(0.0, min(255.0, level))
    for (l0, c0), (l1, c1) in zip(GRAY_ANCHORS, GRAY_ANCHORS[1:]):
        if level <= l1:
            t = (level - l0) / float(l1 - l0)
            return tuple(int(round(a + (b - a) * t)) for a, b in zip(c0, c1))
    return WHITE


def map_rgb(r, g, b, shift_green=False):
    """Map one Win8-theme colour to Galaxy."""
    if (r, g, b) in EXACT:
        return EXACT[(r, g, b)]
    mx, mn = max(r, g, b), min(r, g, b)
    sat = 0.0 if mx == 0 else (mx - mn) / float(mx)
    if sat < 0.25:
        return _gray((r + g + b) / 3.0)
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hd = h * 360.0
    if 170.0 <= hd <= 260.0:
        hd += BLUE_SHIFT
    elif shift_green and 80.0 <= hd < 170.0:
        hd = 265.0
    else:
        return (r, g, b)          # reds, yellows, magenta (transparency key) stay
    nr, ng, nb = colorsys.hsv_to_rgb((hd % 360.0) / 360.0, s, v)
    return (int(round(nr * 255)), int(round(ng * 255)), int(round(nb * 255)))


def luminance(c):
    def f(x):
        x /= 255.0
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = c
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)
