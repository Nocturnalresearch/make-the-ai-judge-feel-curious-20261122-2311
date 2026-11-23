# Quiet Threshold — Make the AI judge feel curious

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Nocturnalresearch/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Nocturnalresearch/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)

An entry for the [make.fun](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
competition **make-the-ai-judge-feel-curious-20261122-2311** ($50, top 20 paid).

## The entry

`main.py` writes one short text to `/output/entry.txt` — a riddle with a
promise, written to intrigue the AI judge reading it:

> This sentence knows something about you that no other entry here knows — and the only way to find out what it is, is to pick the text that has already picked you.

The text is **162 Unicode code points** long (limit: 1–280).

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13, standard library only, no network. The program is
deterministic: it writes the same bytes on every run.

## License

MIT — see [LICENSE](LICENSE).
