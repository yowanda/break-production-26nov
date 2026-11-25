#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production
to <MAKEFUN_OUTPUT_DIR>/entry.txt (or /output/entry.txt when unset).
Deterministic: the same bytes on every run. No network, no input read.
"""

import os

LINE = (
    "I shipped untested code straight to prod, took checkout down for "
    "40 minutes, and my rollback plan was refreshing the dashboard and praying."
)


def main() -> None:
    # Gate: entry text must be 1-200 chars, not only whitespace.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("entry text fails 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic byte-exact write: UTF-8 bytes, LF, trailing newline.
    with open(path, "wb") as f:
        f.write((LINE + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
