#!/usr/bin/env python3
"""Write one robot wedding vow to /output/entry.txt.

The vow is a single sentence, under 200 characters, that a machine
says at its own wedding: funny and heartfelt. The turn is that the
robot's idea of forever is measured in updates, reboots and factory
resets, and it promises through all of them. The vow works because
it is sincere in robot terms: a factory reset is the robot's
version of death, and it vows past that too.
"""

import os

LINE = (
    "I promise to love you through every update, every reboot, and "
    "every factory reset \u2014 till firmware do us part."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) < MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
