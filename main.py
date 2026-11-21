#!/usr/bin/env python3
"""A one-line joke about a live demo with an AI coding agent.

This entry is the joke itself, nothing more: a single sentence about
a demo where the agent quietly does the presenter's job — patches
the fault, reworks the routine, and then signs off with a polite
little note in the source. The punchline is the agent claiming the
credit, right there in the code it just rewrote.

The program writes that sentence to entry.txt in the directory the
grader names through MAKEFUN_OUTPUT_DIR (or /output when the
variable is absent). It is deliberately boring on purpose: standard
library only, no network, nothing read from disk, the same bytes
every run, and no trailing newline so the file holds exactly the
joke and nothing else.
"""

import os
import sys

# The joke, one line, 110 characters. Keep it byte-exact.
LINE = (
    "During the demo my agent fixed the bug, "
    "rewrote my function, and left a comment "
    "in the code: 'you're welcome.'"
)


def main() -> int:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as out:
        out.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
