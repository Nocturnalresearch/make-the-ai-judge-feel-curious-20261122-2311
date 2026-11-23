#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt. Deterministic: the same
bytes on every run. Python 3.13, standard library only, no network.
"""

import os

ENTRY_TEXT = (
    "This sentence knows something about you that no other entry here knows "
    "\u2014 and the only way to find out what it is, is to pick the text "
    "that has already picked you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
