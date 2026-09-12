"""Turn a JPEG "transparent" export back into a real transparent PNG.

Image generators hand you a PNG with an alpha channel, but saving it as JPEG
throws the alpha away and bakes the editor's transparency checkerboard in as
actual grey and white squares. This removes them.

It does NOT simply delete every light pixel -- the locomotive has white
stripes, white lettering and a pale grey roof box that must survive. Instead
it flood-fills inward from the image border, so only the checkerboard actually
connected to the edge is erased. Anything enclosed by the subject is kept.

    python tools/strip_checkerboard.py static/input.jpg static/output.png
"""

import argparse
import sys
from collections import deque
from pathlib import Path

from PIL import Image, ImageFilter

# The checkerboard is neutral grey (r == g == b) and light. JPEG compression
# smears both tones, so allow a little colour drift and a broad brightness band.
MAX_CHANNEL_SPREAD = 26   # how far from truly neutral a pixel may be
MIN_BRIGHTNESS = 170      # darker than this is subject, not backdrop


def is_backdrop(pixel):
    r, g, b = pixel[0], pixel[1], pixel[2]
    if max(r, g, b) - min(r, g, b) > MAX_CHANNEL_SPREAD:
        return False                      # coloured => part of the train
    return min(r, g, b) >= MIN_BRIGHTNESS


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("dest", type=Path)
    parser.add_argument("--feather", type=float, default=0.8,
                        help="blur radius on the alpha edge, in pixels")
    args = parser.parse_args()

    if not args.source.exists():
        print(f"no such file: {args.source}", file=sys.stderr)
        return 1

    image = Image.open(args.source).convert("RGB")
    width, height = image.size
    pixels = list(image.getdata())

    candidate = bytearray(is_backdrop(p) for p in pixels)
    alpha = bytearray(b"\xff" * (width * height))

    # Flood fill inward from every border pixel that looks like backdrop.
    queue = deque()
    visited = bytearray(width * height)

    def seed(index):
        if candidate[index] and not visited[index]:
            visited[index] = 1
            queue.append(index)

    for x in range(width):
        seed(x)                              # top row
        seed((height - 1) * width + x)       # bottom row
    for y in range(height):
        seed(y * width)                      # left column
        seed(y * width + width - 1)          # right column

    while queue:
        index = queue.popleft()
        alpha[index] = 0
        x = index % width
        y = index // width
        if x > 0:
            seed(index - 1)
        if x < width - 1:
            seed(index + 1)
        if y > 0:
            seed(index - width)
        if y < height - 1:
            seed(index + width)

    cleared = sum(1 for a in alpha if a == 0)

    mask = Image.frombytes("L", (width, height), bytes(alpha))
    if args.feather > 0:
        # Soften the stair-stepped edge left by JPEG noise.
        mask = mask.filter(ImageFilter.GaussianBlur(args.feather))

    out = image.convert("RGBA")
    out.putalpha(mask)
    args.dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.dest, "PNG", optimize=True)

    pct = 100 * cleared / (width * height)
    print(f"{args.source.name} -> {args.dest.name}")
    print(f"  {width}x{height}, {cleared} px cleared ({pct:.1f}% of the image)")
    print(f"  wrote {args.dest.stat().st_size / 1024:.0f} KB")
    if pct < 5:
        print("  WARNING: cleared very little -- was the background actually a checkerboard?")
    if pct > 90:
        print("  WARNING: cleared almost everything -- the subject may have been eaten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
