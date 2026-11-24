#!/usr/bin/env python3
# makefun anchor 10d851fdc82ebaee0209a9983a999d6f25e81012 round 34242415
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
Deterministic: the exact same bytes on every run, no trailing newline.
"""

import os

ENTRY = (
    "Auto-reply: I answered 41,209 tickets this week, so my context window "
    "has officially clocked out. GPU's on a beach. Back when my tokens stop "
    "dreaming in JSON."
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 159:
        raise ValueError(f"entry length {len(text)} out of range 1-159")
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
