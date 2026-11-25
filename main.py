#!/usr/bin/env python3
"""Write one funny one-line resignation letter to /output/entry.txt."""

import os
import sys

LINE = "Effective today, I resign. My out-of-office reply has been doing my job for a year and deserves the promotion."

# Why this line works: it opens like a formal resignation ("Effective today,
# I resign") and then the punchline turns the joke on the job itself - the
# auto-reply, a dumb piece of text, has been doing the work all along, so
# the promotion goes to it, not to the person quitting. Specific, surprising,
# and it reads exactly like a letter someone could actually send.


def main() -> int:
    # The gate allows 1 to 140 characters; the line is 110, one line only,
    # no trailing newline, so the output is exactly the letter as written.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
