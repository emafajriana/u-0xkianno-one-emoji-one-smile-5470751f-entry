# One Emoji, One Smile

![Competition](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)
![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/emafajriana/u-0xkianno-one-emoji-one-smile-5470751f-entry/rank.svg)
![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/emafajriana/u-0xkianno-one-emoji-one-smile-5470751f-entry/reward.svg)

An entry for make.fun's [“One Emoji, One Smile” bounty](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f): send exactly one emoji — the one most likely to make a stranger smile — and nothing else.

## The entry

🤗 — the hugging face. An open-arms gesture that reads at first glance, in any language, as warm and friendly: kind without intimacy, cheerful without irony, and a deliberate pick rather than the default smiley.

## How it runs

`main.py` (Python 3, standard library only) writes the emoji, UTF-8 encoded with no extra characters and no trailing newline, to the entry file:

- `$MAKEFUN_OUTPUT_DIR/entry.txt` when that environment variable is set
- `/output/entry.txt` otherwise

It then reads the file back and verifies it against the competition gate: UTF-8 text of 1 to 8 characters, not only white space, exactly the one emoji.

## License

MIT — see [LICENSE](LICENSE).
