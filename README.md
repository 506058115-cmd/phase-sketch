# phase-sketch

Draw a Lissajous curve as plain ASCII art. Choose two integer frequencies and a phase shift to explore how the curve changes; the same arguments always produce the same drawing.

## Use

Requires Python 3.8+; no packages to install.

```sh
python phase_sketch.py
python phase_sketch.py --a 5 --b 4 --phase 35 --width 80 --height 28
```

Frequencies must be 1–12, phase 0–360 degrees, width 20–120, and height 10–50. The canvas uses a single printable ASCII glyph, selected with `--glyph`. The renderer connects sampled curve points so the line stays continuous at small sizes.

## License

MIT
