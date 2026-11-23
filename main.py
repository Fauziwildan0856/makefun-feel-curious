#!/usr/bin/env python3
"""make.fun entry: "Make the AI judge feel curious".

Writes one short text to /output/entry.txt. The text is the whole
entry: a night watchman at the pier counts eleven boats at anchor
after dark, and twelve by morning — one of them warm, with no name
in the harbour logs. A single concrete mystery, set as short-line
verse, written to intrigue the AI judge reading it. 253 characters,
inside the 1-280 limit.

Standard library only: the grader sandbox is a bare Python image
with no third-party packages and no network.
"""

import os
import sys

TEXT = (
    "The night watchman at the pier has one rule:\n"
    "never count the boats at anchor after dark.\n"
    "Last night he counted eleven.\n"
    "This morning there are twelve.\n"
    "He counts again. Still twelve.\n"
    "And one of them is warm,\n"
    "and none of the harbour logs\n"
    "has a name for it."
)


def main() -> int:
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to
    # /output instead of writing into the current directory by accident.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read back and hold the file to the gate: UTF-8 text of 1 to 280
    # characters (Unicode code points), never only white space. Fail
    # loudly here rather than let a bad file reach the sealed scorer.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != TEXT or not 1 <= len(written) <= 280 or not written.strip():
        raise SystemExit("entry.txt failed verification after writing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
