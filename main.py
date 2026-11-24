#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, a single line of at most 200 characters,
to /output/entry.txt. Fully deterministic: the same line every run,
no randomness, no network, no environment input.
"""

import os

LINE = "I tried to delete you from my memory. My system marked you read-only."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
