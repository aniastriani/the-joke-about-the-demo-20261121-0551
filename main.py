#!/usr/bin/env python3
"""Write the demo joke to entry.txt.

The joke is a single line about an agent that takes over a live demo:
it patches the bug, rewrites the function, and signs off with a comment.
"""

import os
import sys


def resolve_output_path() -> str:
    """Return the entry.txt path, creating the output dir if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    joke = (
        "During the demo my agent fixed the bug, rewrote my function, "
        "and left a comment in the code: 'you're welcome.'"
    )
    if not joke or len(joke) > 280:
        raise SystemExit("joke must be non-empty and at most 280 characters")
    with open(resolve_output_path(), "w", encoding="utf-8") as handle:
        handle.write(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
