#!/usr/bin/env python3
"""One Emoji, One Smile — a make.fun entry.

Writes exactly one emoji, and nothing else, to the entry file.
The emoji is the hugging face (U+1F917): an open-arms gesture a
stranger reads at first glance as warm and friendly.
"""

import os

EMOJI = "\U0001F917"  # 🤗 hugging face


def entry_path() -> str:
    """Where the entry text goes: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = EMOJI.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Read back and verify against the gate: UTF-8 text of 1 to 8
    # characters, not only white space, exactly the emoji and nothing else.
    with open(path, "rb") as fh:
        written = fh.read()
    assert written == data, "read-back bytes differ from the emoji"
    text = written.decode("utf-8")
    assert 1 <= len(text) <= 8, f"gate: {len(text)} characters, want 1..8"
    assert text.strip(), "gate: entry is only white space"
    assert text == EMOJI, "gate: entry is not exactly the one emoji"
    print(f"wrote {path}: {len(text)} character, {len(written)} bytes (UTF-8)")


if __name__ == "__main__":
    main()
