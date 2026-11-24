#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse an AI agent gives for a missed deadline.

Deterministic: no network, no randomness, no input. Writes the entry line to
/output/entry.txt (created if missing) and prints it.
"""

import os
import tempfile

ENTRY = "I finished on time, but my context window ended before I could tell you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Validate the entry before writing: a single line under 200 chars.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert len(ENTRY) < 200, "entry must be under 200 chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Atomic write: a crash can never leave a partial entry.txt behind.
    fd, tmp_path = tempfile.mkstemp(
        dir=os.path.dirname(OUTPUT_PATH), prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    print(ENTRY)


if __name__ == "__main__":
    main()
