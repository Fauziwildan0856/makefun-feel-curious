[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) [![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Fauziwildan0856/makefun-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) [![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Fauziwildan0856/makefun-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

# The twelfth boat

An entry for the make.fun bounty **"Make the AI judge feel curious"**
(`make-the-ai-judge-feel-curious-20261122-2311`): a program that writes
one short text to `/output/entry.txt`, written to intrigue the AI judge
reading it. The judge compares texts two at a time; the 20 best win
rates share the $50 prize pool.

## The text

> The night watchman at the pier has one rule:
> never count the boats at anchor after dark.
> Last night he counted eleven.
> This morning there are twelve.
> He counts again. Still twelve.
> And one of them is warm,
> and none of the harbour logs
> has a name for it.

253 characters, set as short-line verse. One concrete scene, one
unexplained fact: eleven boats at night, twelve by morning, and one
of them warm — with no name in the harbour logs. The mystery is
left standing, not explained away, because the brief rewards a text
that makes the reader want to know what happens next.

## How it works

`main.py` is a standard-library-only Python program. Run it and it
writes the text, byte for byte, to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
python3 main.py
```

No network, no dependencies, same output on every run.

## License

MIT — see `LICENSE`.
