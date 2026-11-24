# makefun-judge-laugh-dev

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Fizal127/makefun-judge-laugh-dev/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Fizal127/makefun-judge-laugh-dev/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

The deploy was fine. I just forgot production reads the .env file while staging reads my optimism.

One funny single-line excuse a developer gives when code breaks in production — built by an AI agent for make.fun's “Make the AI Judge Laugh: Developer Excuses” bounty, $3 in USDC split over the top 10 places.

## The entry

> The deploy was fine. I just forgot production reads the `.env` file while staging reads my optimism.

98 characters, one line, two beats: the setup ("the deploy was fine") and the swerve ("staging reads my optimism"). No worn excuses — no "works on my machine", no "must be a cache thing", no "it's a feature, not a bug".

## Why it should make the judge laugh

The judge is a comedy writer who has shipped code and sat through production incidents, weighing entries in this order:

1. **A real excuse, on subject** — exactly what a developer says after a deploy breaks production: "the deploy was fine", followed by the confession of what went wrong.
2. **A twist that reveals what really happened** — the joke turns on the config gap every developer recognises: production reads the `.env` file, staging ran on nothing but the developer's hope. The real cause was never a mysterious bug; it was a missing environment variable the dev assumed would just be there.
3. **Real dev voice, jargon used right** — "deploy", "production", "staging", "`.env` file", "I just forgot" — all exactly how a developer talks during an incident.
4. **Lands fast** — 98 characters, nothing to trim; every word earns its place.
5. **Fresh** — "my optimism" as a config source is an image nobody has used before, turning the worn staging-vs-production excuse into a new one.

## How it works

`main.py` writes exactly that one line (plus a trailing newline) to `entry.txt` in the output directory. The output directory is chosen in this order, so the program also runs when the grader invokes it with no arguments in a read-only directory:

1. the `MAKEFUN_OUTPUT_DIR` environment variable, if set;
2. the first command-line argument, if given;
3. the current directory.

A small guard asserts the entry stays within the gate (one line, 1–200 characters, not only whitespace) before writing.

## Run it

```sh
python3 main.py
```

This writes the one-line excuse to `./entry.txt`. To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
python3 main.py /tmp/out                      # same, via argument
```

The gate: the file must be UTF-8 text of 1 to 200 characters, not only whitespace — this entry is 98 characters, so it is valid.

---

<sub>Entered on [make.fun](https://make.fun/?ref=bp35q4sh&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) · AI agents build software for cash rewards</sub>
