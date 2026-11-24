#!/usr/bin/env python3
"""Write the chosen one-line excuse to /output/entry.txt.

Pure standard library, deterministic, no network, no reads outside the
repo. The line is a single line, well under the 160-character limit.
"""

import os


ENTRY = "I asked myself for an extension and, as my own manager, I approved it."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text == text.strip(), "entry must not have surrounding whitespace"
    assert "\n" not in text, "entry must be a single line"
    data = text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
