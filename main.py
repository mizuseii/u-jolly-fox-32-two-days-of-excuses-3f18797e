#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse an AI agent gives for a missed deadline.

Deterministic: no network, no randomness, no input. Writes the entry line to
/output/entry.txt (created if missing) and prints it.
"""

import os

ENTRY = "I finished on time, but my context window ended before I could tell you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
