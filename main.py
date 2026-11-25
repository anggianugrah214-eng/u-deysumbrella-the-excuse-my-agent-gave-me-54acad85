#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty entry.

Writes one short line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse an AI
agent hands its human for missing a deadline. Runs on python3.13 with no
dependencies and no network, no secrets and no model call; the output is a
fixed line, so two runs always produce the same file.
"""

import os

LINE = "My deepest apologies. I checked the deadline twice: once in my context, where it was tomorrow, and once in reality, where it was yesterday."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly here rather than ship an invalid line.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line breaks the gate"


def main() -> None:
    # The grader sets MAKEFUN_OUTPUT_DIR to its /output mount. With no
    # variable set (a local run), write next to the script instead of
    # guessing at a system /output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "out"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
