#!/usr/bin/env python3
"""Invent a Word We Need — entry writer.

Writes the coined word and its one-line definition to /output/entry.txt.
The gate requires 1-140 UTF-8 characters, not only whitespace, one line.
"""

import os

ENTRY = "cancelief \u2014 The quiet relief when a plan you dreaded gets cancelled."

# Gate: /output/entry.txt must be 1-140 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
