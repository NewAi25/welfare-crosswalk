# Audit log

One entry per push. An entry is written only after the research-auditor agent has returned AUDIT: PASS on the unpushed changes and both mechanical checks (`scripts/validate_csv.py`, `scripts/check_corpus.py --local`) exit 0. The pre push hook in `.githooks/pre-push` refuses a push whose commit has no PASS entry here. The predecessor repository's three audits are in its own log.

| Date | Commit audited | Claims checked | Wrong | Unsupported | Imprecise | Result | Summary |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | 90f233a | About 40 claims across CLAUDE.md, README, definitions, data dictionary, reading list, Kevin brief, decisions and the scripts against definitions | 0 | 0 | 8, all tightened, two by replacing illustrative worked examples with the real RSPCA H 3.5 and FARM page 149 wording | PASS | Session 0 scaffold. Counts, page references, the three poultry citations (Crossref) and the AWIN species list (CORDIS, Wickens 2015) confirmed. LICENSE file added. |
