#!/usr/bin/env python3
"""Draw a bounded Lissajous curve in a plain-text terminal grid."""

import argparse
import math


def line(grid, x0, y0, x1, y1, glyph):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    error = dx - dy
    while True:
        grid[y0][x0] = glyph
        if x0 == x1 and y0 == y1:
            return
        doubled = 2 * error
        if doubled > -dy:
            error -= dy
            x0 += sx
        if doubled < dx:
            error += dx
            y0 += sy


def draw(width, height, a, b, phase, glyph):
    grid = [[" "] * width for _ in range(height)]
    steps = 8 * max(width, height) * max(a, b)
    previous = None
    for index in range(steps + 1):
        angle = 2 * math.pi * index / steps
        x = round((math.sin(a * angle + phase) + 1) * (width - 1) / 2)
        y = round((1 - math.sin(b * angle)) * (height - 1) / 2)
        if previous is not None:
            line(grid, *previous, x, y, glyph)
        previous = x, y
    return "\n".join("".join(row).rstrip() for row in grid)


def main():
    parser = argparse.ArgumentParser(description="Draw a Lissajous curve as ASCII art.")
    parser.add_argument("--a", type=int, default=3, help="horizontal frequency (1–12)")
    parser.add_argument("--b", type=int, default=2, help="vertical frequency (1–12)")
    parser.add_argument("--phase", type=float, default=90, help="horizontal phase in degrees (0–360)")
    parser.add_argument("--width", type=int, default=72, help="canvas width (20–120)")
    parser.add_argument("--height", type=int, default=24, help="canvas height (10–50)")
    parser.add_argument("--glyph", default="*", help="one printable non-space ASCII character")
    args = parser.parse_args()
    if not 1 <= args.a <= 12 or not 1 <= args.b <= 12:
        parser.error("--a and --b must be between 1 and 12")
    if not 0 <= args.phase <= 360:
        parser.error("--phase must be between 0 and 360 degrees")
    if not 20 <= args.width <= 120 or not 10 <= args.height <= 50:
        parser.error("--width must be 20–120 and --height 10–50")
    if len(args.glyph) != 1 or ord(args.glyph) > 127 or not args.glyph.isprintable() or args.glyph.isspace():
        parser.error("--glyph must be one printable non-space ASCII character")

    print(f"Lissajous {args.a}:{args.b} | phase {args.phase:g}°")
    print(draw(args.width, args.height, args.a, args.b, math.radians(args.phase), args.glyph))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
