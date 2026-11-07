#!/usr/bin/env python3
"""Regenerate the Galaxy theme bitmaps and INI files from the Win8 theme.

Usage (from the repository root):
    python3 media/themes/Galaxy/tools/recolor_from_win8.py

Reads  media/themes/Win8/win8.msstyles/{bitmaps,textfiles}
Writes media/themes/Galaxy/galaxy.msstyles/{bitmaps,textfiles}

BMP files are edited in place byte-for-byte (headers untouched), so palettised,
24-bit, 32-bit and BITFIELDS bitmaps all keep their exact original format.
"""
import os
import re
import struct
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from galaxy_palette import map_rgb  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "media", "themes", "Win8", "win8.msstyles")
DST = os.path.join(ROOT, "media", "themes", "Galaxy", "galaxy.msstyles")

_cache = {}


def mapc(rgb, green):
    key = (rgb, green)
    if key not in _cache:
        _cache[key] = map_rgb(*rgb, shift_green=green)
    return _cache[key]


def recolor_bmp(data, green):
    d = bytearray(data)
    off = struct.unpack_from("<I", d, 10)[0]
    hs = struct.unpack_from("<I", d, 14)[0]
    w, h = struct.unpack_from("<ii", d, 18)
    bpp = struct.unpack_from("<H", d, 28)[0]
    comp = struct.unpack_from("<I", d, 30)[0]
    clr_used = struct.unpack_from("<I", d, 46)[0]
    h = abs(h)
    stats = {"bpp": bpp, "premult_pixels": 0, "partial_alpha": 0}

    if bpp <= 8:
        n = clr_used or (1 << bpp)
        p = 14 + hs
        for i in range(n):
            b, g, r = d[p + 4 * i], d[p + 4 * i + 1], d[p + 4 * i + 2]
            nr, ng, nb = mapc((r, g, b), green)
            d[p + 4 * i], d[p + 4 * i + 1], d[p + 4 * i + 2] = nb, ng, nr
        return bytes(d), stats

    if comp == 3:
        masks = struct.unpack_from("<4I", d, 54)
        if masks[:3] != (0x00FF0000, 0x0000FF00, 0x000000FF):
            raise ValueError("unexpected BITFIELDS masks %r" % (masks,))
    elif comp != 0:
        raise ValueError("unsupported compression %d" % comp)

    bytespp = bpp // 8
    stride = ((w * bpp + 31) // 32) * 4
    buf = np.frombuffer(bytes(d), dtype=np.uint8)
    rows = np.stack([buf[off + y * stride: off + y * stride + w * bytespp] for y in range(h)])
    px = rows.reshape(h, w, bytespp).copy()          # B G R (A)
    flat = px.reshape(-1, bytespp)
    alpha = flat[:, 3] if bytespp == 4 else None

    bgr = flat[:, :3]
    uniq, inv = np.unique(bgr, axis=0, return_inverse=True)
    inv = inv.reshape(-1)
    out = np.empty_like(uniq)
    for i, (b, g, r) in enumerate(uniq):
        # Premultiplied alpha cannot be told apart per unique colour, so alpha
        # pixels are handled separately below.
        nr, ng, nb = mapc((int(r), int(g), int(b)), green)
        out[i] = (nb, ng, nr)
    new_bgr = out[inv]

    if alpha is not None:
        part = (alpha > 0) & (alpha < 255)
        stats["partial_alpha"] = int(part.sum())
        stats["premult_pixels"] = int((part & (bgr.max(axis=1) <= alpha)).sum())
        # Premultiplied only if every partially transparent pixel has colour <= alpha;
        # such files are un-premultiplied, mapped, then premultiplied again.
        # Straight-alpha files are mapped directly (new_bgr already holds that).
        if part.any() and stats["premult_pixels"] == stats["partial_alpha"]:
            a = alpha[part].astype(np.float64) / 255.0
            un = np.clip(bgr[part].astype(np.float64) / a[:, None], 0, 255)
            mapped = np.empty_like(un)
            for k in range(un.shape[0]):
                b, g, r = (int(round(x)) for x in un[k])
                nr, ng, nb = mapc((r, g, b), green)
                mapped[k] = (nb, ng, nr)
            new_bgr[part] = np.clip(np.round(mapped * a[:, None]), 0, 255).astype(np.uint8)
        # fully transparent pixels: leave the colour exactly as it was
        new_bgr[alpha == 0] = bgr[alpha == 0]

    flat[:, :3] = new_bgr
    px = flat.reshape(h, w, bytespp)
    for y in range(h):
        d[off + y * stride: off + y * stride + w * bytespp] = px[y].tobytes()
    return bytes(d), stats


TRIPLE = re.compile(rb"^(\s*)([A-Za-z0-9_]+)(\s*=\s*)(\d{1,3}) (\d{1,3}) (\d{1,3})(\s*)$")
KEEP_KEYS = (b"transparentcolor",)      # transparency keys must stay exactly as they are


def recolor_ini(data):
    out, section, changed = [], b"", 0
    for line in data.split(b"\n"):
        s = line.strip()
        if s.startswith(b"[") and s.endswith(b"]"):
            section = s.lower()
        m = TRIPLE.match(line.rstrip(b"\r"))
        if m:
            pre, key, eq, r, g, b, post = m.groups()
            k = key.lower()
            is_color = section == b"[sysmetrics]" or k.endswith(b"color") or k.endswith(b"colorhint") or k == b"color"
            if is_color and not any(k.endswith(x) for x in KEEP_KEYS) and (r, g, b) != (b"255", b"0", b"255"):
                rgb = (int(r), int(g), int(b))
                if k == b"accentcolorhint":
                    new = (123, 47, 247)
                else:
                    new = mapc(rgb, True)
                if new != rgb:
                    changed += 1
                cr = b"\r" if line.endswith(b"\r") else b""
                line = pre + key + eq + ("%d %d %d" % new).encode() + post.rstrip(b"\r") + cr
        out.append(line)
    return b"\n".join(out), changed


def main():
    os.makedirs(os.path.join(DST, "bitmaps"), exist_ok=True)
    os.makedirs(os.path.join(DST, "textfiles"), exist_ok=True)
    totals = {"bitmaps": 0, "partial": 0, "premult": 0}
    for name in sorted(os.listdir(os.path.join(SRC, "bitmaps"))):
        if not name.lower().endswith(".bmp"):
            continue
        with open(os.path.join(SRC, "bitmaps", name), "rb") as f:
            data = f.read()
        new, st = recolor_bmp(data, green="PROGRESS" in name.upper())
        assert len(new) == len(data)
        with open(os.path.join(DST, "bitmaps", name), "wb") as f:
            f.write(new)
        totals["bitmaps"] += 1
        totals["partial"] += st["partial_alpha"]
        totals["premult"] += st["premult_pixels"]
    for name in sorted(os.listdir(os.path.join(SRC, "textfiles"))):
        with open(os.path.join(SRC, "textfiles", name), "rb") as f:
            data = f.read()
        new, n = recolor_ini(data)
        with open(os.path.join(DST, "textfiles", name), "wb") as f:
            f.write(new)
        print("%-24s %4d colour values remapped" % (name, n))
    print("bitmaps: %(bitmaps)d  partial-alpha px: %(partial)d (premultiplied: %(premult)d)" % totals)


if __name__ == "__main__":
    main()
