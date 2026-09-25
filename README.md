# Welfare indicators x deployed sensors x certification requirements

Which welfare indicators are (a) measurable by AI, (b) acceptable to industry for adoption, and (c) potentially already covered by existing sensors or widely used certification schemes? One species per unit. Dairy cattle first.

## Start here

| Step | File | What it tells you |
|---|---|---|
| 1 | [`CLAUDE.md`](CLAUDE.md) | The question, the deliverables, the hard rules, the fixed citations |
| 2 | [`standard/definitions.md`](standard/definitions.md) | Every column of the table, the rule that fills it, and the heuristic that ranks it. Fixed before extraction |
| 3 | [`docs/kevin_answers.md`](docs/kevin_answers.md) | The mentor's steer that made the criteria soft factors rather than filters |
| 4 | [`docs/PLF_Handover_2026-09-23.md`](docs/PLF_Handover_2026-09-23.md) | What the larger predecessor project attempted, what blocked it, and what was kept |
| 5 | [`notes/decisions.md`](notes/decisions.md) | Every judgement call in date order |
| 6 | [`docs/before_you_start.md`](docs/before_you_start.md) | What to read before the work starts, in order, with why |

## Deliverables

| # | Deliverable | Files |
|---|---|---|
| 1 | Column 3: what four certification schemes require and how they audit it | `data/crosswalk.csv` |
| 2 | Column 2: sensor coverage, hardware class and market breadth for every indicator | `data/sensor_coverage.csv` |
| 3 | The adoption table and the two item #13 views | `results/` |
| 4 | Write up and one page list entry | `writeup/` |
| 5 | A poultry unit, same schema | after dairy |

## How to verify any number

Every value in `data/` traces to a public source. A crosswalk row quotes the requirement with section and page; open the scheme PDF named in [`corpus/README.md`](corpus/README.md) and find it. A sensor coverage row names the product ids and the Stygar reference numbers; open `corpus/stygar_2021.pdf` Table 1 on page 6 and the supplementary spreadsheet. `corpus/manifest.csv` holds the SHA256 of every source so you can confirm you have the same file, and `python scripts/check_corpus.py` re-fetches every URL. Nothing is pushed until a separate auditing agent has checked every claim in the change and returned PASS; the log, failures included, is [`notes/audit_log.md`](notes/audit_log.md). Every value is sourced, decided (a dated entry in `notes/decisions.md`) or unknown (`unsure`, `none`, `not_covered`), never guessed.

The adoption score is a heuristic sort order from a stated 0 to 3 mapping of five factors. It is not a welfare judgement and every factor stays visible so the table can be re sorted by any one of them.

## Running it

```
python scripts/validate_csv.py
python scripts/market_breadth.py
python scripts/stats.py
```

## Licence and credits

Data and text CC BY 4.0, code MIT. Author Manisha Sarkar. Mentor Kevin Xia. Sentient Futures incubator, fall 2026. Predecessor: github.com/NewAi25/plf-audit.
