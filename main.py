#!/usr/bin/env python3
"""Entry for make.fun bounty "Draw the cutest cat" (cutest-cat-01).

Writes a single cat image to /output/entry.png.

The image is a pre-made PNG bundled in this repository (cat.png, 1024x1024,
972941 bytes). This program only copies those exact bytes to the output
path, so every run produces byte-identical output. No network, no randomness,
no model calls -- standard library only (pathlib, shutil, sys).
"""

import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "cat.png"
OUTPUT = Path("/output/entry.png")


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
