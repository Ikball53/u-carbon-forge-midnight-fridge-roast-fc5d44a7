"""Midnight Fridge Roast — one-line entry.

Writes a single original roast line to /output/entry.txt.
No trailing newline, UTF-8, exactly one line, 1-200 characters.
"""

from pathlib import Path

ENTRY_LINE = "My smart fridge locks after midnight, so my leftovers now have better boundaries than I do."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY_LINE
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
