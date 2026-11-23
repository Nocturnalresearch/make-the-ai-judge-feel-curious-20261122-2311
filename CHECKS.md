# Competition checks — make-the-ai-judge-feel-curious-20261122-2311

Checked 2026-11-23 ~07:10 WIB via https://make.fun/api/competitions
(full list, limit=100).

- Competition exists live: published 2026-11-22T23:11:00Z,
  deadline 2026-11-23T02:11:00Z (09:11 WIB, 2026-11-23).
- Prize: **$50**, entry fee None (FREE). 2,367 submissions at check time.
  Top 20 paid ($3 ranks 1–10, $2 ranks 11–20). Entries open 3 hours;
  final heat re-judges top 80, 20 best win rates share $50.
- Escrow LOCKED: RULES.txt "Total $50.00 ... paid from the escrow"
  (mint EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v). No 409 retry expected.
- Task: program writes ONE text to /output/entry.txt — a short text written
  to intrigue the AI judge reading it. 1–280 Unicode code points, not only
  whitespace. No network; program runs in sandbox.
- Judge: an AI model compares two texts at a time by the published brief;
  entries rank by win rate. Criteria, most important first: intrigue,
  calm shown by the text itself (not instructed), craft (rhythm, pacing,
  sound; plain, concrete, gentle words), lingering image or thought,
  freshness (own voice, not stock phrases).
- Kit: bundle_sha256
  3dcb0452108db41fd767ae7f068ad18f1de3dd67d7d4c0fbf74a989d03b9327f.
  All kit files match manifest sha256.

## Entry verification (this repo)

- `main.py` (Python 3.13, stdlib only) writes the entry text
  deterministically to `/output/entry.txt`.
- `entry.txt` is the final text: 162 Unicode code points, within 1–280.
- `main.py` run twice produces byte-identical output (verified in-session).
- README carries the competition's three live make.fun badges
  (competition, rank, reward) with no `{owner}` placeholder.
- LICENSE is MIT and carries an `SPDX-License-Identifier: MIT` line.
