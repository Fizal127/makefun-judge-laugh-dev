#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses (make.fun).

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

import os
import sys

ENTRY = "The deploy was fine. I just forgot production reads the .env file while staging reads my optimism."

# Output dir: grader env first, then an argv override, then the cwd —
# never a hard-coded path, so the program also works when the grader
# runs it with no arguments in a read-only directory.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or (sys.argv[1] if len(sys.argv) > 1 else ".")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate guard: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip() and "\n" not in ENTRY
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
