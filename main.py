#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt. Deterministic: the same
bytes on every run. Python 3.13, standard library only, no network.
"""

import os
import tempfile

ENTRY_TEXT = (
    "This sentence knows something about you that no other entry here knows "
    "\u2014 and the only way to find out what it is, is to pick the text "
    "that has already picked you."
)


def main() -> None:
    # The competition requires 1-280 Unicode code points; fail loudly
    # rather than ever writing an out-of-range entry.
    if not 1 <= len(ENTRY_TEXT) <= 280:
        raise SystemExit(f"entry text is {len(ENTRY_TEXT)} code points, not 1-280")
    os.makedirs("/output", exist_ok=True)
    # Write atomically so a partial write can never leave a broken entry.
    fd, tmp = tempfile.mkstemp(dir="/output", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY_TEXT)
        os.replace(tmp, "/output/entry.txt")
    except BaseException:
        os.unlink(tmp)
        raise


if __name__ == "__main__":
    main()
