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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
