#!/usr/bin/env python3
"""One Emoji, One Smile - make.fun entry.

Writes exactly one emoji to /output/entry.txt and prints it.
The duel-tested winner: U+1F604 GRINNING FACE WITH SMILING EYES.
"""

import os

EMOJI = "\U0001F604"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check the gate contract: exactly one character, UTF-8, no
    # trailing newline or extra whitespace in the file itself.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, f"gate violation: entry is {written!r}"
    print(EMOJI)


if __name__ == "__main__":
    main()
