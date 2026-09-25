# Decisions

Every judgement not covered by standard/definitions.md is entered here, dated, before it is applied. The predecessor repository's decisions are in docs/decisions_from_plf_audit.md and are not repeated.

## 2026-09-25: repository created from plf-audit

Created as the narrowed successor of plf-audit after the mentor call of 22 September and Kevin's Slack reply of 25 September (docs/kevin_answers.md). Copied unchanged: data/products.csv, the corpus with its manifest and README, scripts/check_corpus.py, the research-auditor agent and the pre push hook. Copied with a change: data/indicators.csv gains the tier column, the audit skill description names this repository, and reading_order.md carries a two line inherited header. Copied as read only history into docs/: the predecessor's decisions.md, kevin_questions.md and reading_order.md. Not copied: claims, scorecard and reliability schemas, the coding frame, rubric, scope note, logger and writeup skeletons, which belong to the larger project and stay in the frozen repository.

Five decisions from Kevin's reply. Dairy first, then a poultry unit, broilers or laying hens depending on sources; the poultry unit is a commitment. The three criteria are adoption factors, not filters, so the deliverable is a ranked table with every factor visible and no row excluded. Industry acceptability is read as ease of implementation at low or no cost, made visible through two sourced factors added to FARM naming: hardware class and market breadth. Certification coverage is a count with audit method, not a gate. Nothing further is asked of Kevin.

Schema changes from the predecessor: indicators.csv gains a final column tier (joined, efsa_only, wq_only), filled by scripts/stats.py from the existing columns. sensor_coverage.csv and crosswalk.csv are new; crosswalk.csv drops the predecessor's computed query columns, which now live in results/, and adds section_ref, page and industry_naming. The 0 to 3 mapping and the sum in definitions.md are the ranking heuristic and the only place a later decision can change the order.

Open: the poultry unit's sources. Candidates verified on Crossref on 23 September, content not yet checked: EFSA 2023 Welfare of broilers on farm, EFSA Journal 21(2):7788; Rowe, Dawkins and Gebhardt-Henrich 2019, Animals 9(9):614; Brassó, Komlósi and Várszegi 2025, Animals 15(4):493. Whether either review codes commercial availability and validation the way Stygar does decides whether the poultry unit's sensor coverage rests on validation or on claims.
