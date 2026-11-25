"""I Checked. It Has Not Changed: one note from a smart fridge.

The entry is a single passive-aggressive note a smart fridge leaves on
its door screen for its owner. The fridge speaks like a smug appliance
with a door log and an inventory: nine opens since midnight, all to
stare at a yogurt that expired Tuesday. The sting is the fridge
confirming, from its own sensors, that staring changed nothing. The
program writes exactly that one line, and nothing else, to
/output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Door log: 9 opens since midnight, all to stare at a yogurt that "
    "expired Tuesday. It has not changed. I checked."
)


def main():
    if LINE.strip() != LINE:
        raise ValueError("line has stray leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1 to 200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("line must not be only white space")
    if "  " in LINE:
        raise ValueError("line has a double space")
    if "\u2014" in LINE or "\u2013" in LINE:
        raise ValueError("line must not contain an em dash or en dash")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt mismatch, got %r" % written)


if __name__ == "__main__":
    main()
