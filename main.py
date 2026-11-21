#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

The joke is a single line, written to entry.txt inside the output
directory the grader provides. It stays well under the 280-character
cap, uses plain UTF-8, and needs nothing beyond the standard library:
no imports outside os and sys, no network, no files read.

The joke itself: during a live demo, the agent does the developer's
job better than the developer -- fixes the bug, rewrites the
function -- and then leaves a smug little comment behind. The laugh
is the role reversal: the tool thanks itself, in writing, in the
developer's own code.
"""

import os
import sys

JOKE = (
    "During the demo my agent fixed the bug, rewrote my function, "
    "and left a comment in the code: 'you're welcome.'"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
