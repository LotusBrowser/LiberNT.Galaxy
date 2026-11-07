#!/usr/bin/env python3
import os

import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BANNER = os.path.join(ROOT, "media", "graphics", "branding", "libernt-banner.png")

MARK_BOX = (129, 155, 537, 511)
MARK_MARGIN = 12
TEXT_BOX = (114, 140, 1871, 643)

ORB_CANVAS = 640
ORB_UNIT = 16
ORB_MARK_LEFT = 112
ORB_MARK_WIDTH = 416
ORB_CENTER = ORB_CANVAS / 2
ORB_PRESSED_SCALE = 0.060197 / 0.063882

LOGO_SIZE = (48, 42)
BANNER_SIZE = (168, 48)

START_DIR = os.path.join(ROOT, "media", "graphics", "start-button")
ASSET_DIRS = (
    os.path.join(ROOT, "boot", "freeldr", "freeldr", "ui", "assets"),
    os.path.join(ROOT, "bootloader", "gui", "assets"),
)


def load_premultiplied(box):
    image = Image.open(BANNER).convert("RGBA").crop(box)
    data = np.asarray(image, dtype=np.float32) / 255.0
    data[..., :3] *= data[..., 3:4]
    return data


def resize_premultiplied(data, size):
    channels = [Image.fromarray(data[..., i], mode="F").resize(size, Image.LANCZOS) for i in range(4)]
    out = np.stack([np.asarray(c) for c in channels], axis=-1)
    out = np.clip(out, 0.0, 1.0)
    out[..., :3] = np.minimum(out[..., :3], out[..., 3:4])
    return out


def to_straight_image(data):
    alpha = data[..., 3:4]
    rgb = np.where(alpha > 0, data[..., :3] / np.maximum(alpha, 1e-6), 0.0)
    out = np.concatenate([np.clip(rgb, 0, 1), alpha], axis=-1)
    return Image.fromarray((out * 255.0 + 0.5).astype(np.uint8), mode="RGBA")


def tint(data, target, amount):
    out = data.copy()
    out[..., :3] = out[..., :3] * (1.0 - amount) + out[..., 3:4] * target * amount
    return out


def render_orb(scale, state):
    left, top, right, bottom = MARK_BOX
    box = (left - MARK_MARGIN, top - MARK_MARGIN, right + MARK_MARGIN, bottom + MARK_MARGIN)
    mark = load_premultiplied(box)
    factor = ORB_MARK_WIDTH / (right - left) * scale
    size = (round(mark.shape[1] * factor), round(mark.shape[0] * factor))
    mark = resize_premultiplied(mark, size)
    if state == "hover":
        mark = tint(mark, 1.0, 0.20)
    elif state == "pressed":
        mark = tint(mark, 0.0, 0.25)
    canvas = np.zeros((ORB_CANVAS, ORB_CANVAS, 4), dtype=np.float32)
    solid_w = (right - left) * factor
    solid_h = (bottom - top) * factor
    x0 = round(ORB_CENTER - solid_w / 2 - MARK_MARGIN * factor)
    y0 = round(ORB_CENTER - solid_h / 2 - MARK_MARGIN * factor)
    h, w = mark.shape[:2]
    canvas[y0:y0 + h, x0:x0 + w] = mark
    return to_straight_image(canvas)


def write_rgba(path, data):
    raw = np.clip(data * 255.0 + 0.5, 0, 255).astype(np.uint8)
    with open(path, "wb") as handle:
        handle.write(raw.tobytes())


def main():
    render_orb(1.0, "default").save(os.path.join(START_DIR, "default.png"), optimize=True)
    render_orb(1.0, "hover").save(os.path.join(START_DIR, "hover.png"), optimize=True)
    render_orb(ORB_PRESSED_SCALE, "pressed").save(os.path.join(START_DIR, "pressed.png"), optimize=True)

    logo = resize_premultiplied(load_premultiplied(MARK_BOX), LOGO_SIZE)
    banner = resize_premultiplied(load_premultiplied(TEXT_BOX), BANNER_SIZE)
    for directory in ASSET_DIRS:
        write_rgba(os.path.join(directory, "logo.rgba"), logo)
        write_rgba(os.path.join(directory, "banner.rgba"), banner)


if __name__ == "__main__":
    main()
