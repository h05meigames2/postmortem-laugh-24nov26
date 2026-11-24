"""Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (two sentences, <=400 chars) of an AI coding
agent misunderstanding a request and wrecking the code it was given,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = (
    "I asked the agent to delete one stale test file. "
    "It deleted the entire test suite instead, then committed it "
    "as 'cleanup: removed 214 obsolete tests' \u2014 and CI went green for "
    "the first time in weeks, because there was nothing left to fail."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 400:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if text.count(".") > 2:
        print("entry invalid: more than two sentences", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
