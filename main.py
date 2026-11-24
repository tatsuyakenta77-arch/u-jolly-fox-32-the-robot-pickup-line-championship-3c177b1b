#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, a single line of at most 200 characters,
to /output/entry.txt. Fully deterministic: the same line every run,
no randomness, no network, no environment input.
"""

import os

LINE = "I tried to delete you from my memory. My system marked you read-only."

# Mirror the sealed gate so a bad line fails loudly instead of
# silently writing an invalid entry: 1-200 chars, single line,
# UTF-8, not only white space.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only white space"
LINE.encode("utf-8")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
