#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one roast line to /output/entry.txt for the house judge to compare
pairwise against the other entries.

Strategy, in my own words:
  The judge rewards a one-line roast whose target is the fridge's petty
  midnight rule itself, with a real joke and a surprise turn — not a
  generic smart-home complaint. So the line is built as a role reversal:
  the fridge is a strict parent and its owner is the grounded teenager.
  "I pay its electricity bill" sets up the owner's authority; "it still
  grounds me" flips it — the appliance you own and power is the one
  punishing you. That indignity is the whole joke, it names the midnight
  lockout directly, and it reads like something you would actually mutter
  standing at the fridge door at 00:05.

  Deliberately NOT used: the bouncer angle (everyone will write it),
  a second joke crowding the first, or any address to the judge — the
  line wins on the roast itself, not on meta-gaming the brief.

Only the Python standard library is used: the grading sandbox installs
nothing, so no third-party import may appear here.
"""

import os
import sys

# The roast. One line, under 200 characters, spoken-voice, no second joke.
ROAST = (
    "My smart fridge locks me out at midnight \u2014 I pay its electricity "
    "bill, and it still grounds me like a teenager."
)

MAX_CHARS = 200


def main() -> int:
    # Self-check the same gate the sealed scorer applies: 1-200 UTF-8
    # characters, not only whitespace. Fail loudly instead of shipping
    # an entry the gate would refuse.
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: roast is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip check: what the judge will read must be exactly the
    # line above, byte for byte, with no stray whitespace or encoding
    # surprise introduced on the way out.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read().strip() != text:
            print("error: written entry does not match the roast",
                  file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
