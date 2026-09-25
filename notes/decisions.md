# Decisions

Every judgement not covered by standard/definitions.md is entered here, dated, before it is applied. The predecessor repository's decisions are in docs/decisions_from_plf_audit.md and are not repeated.

## 2026-09-25: repository created from plf-audit

Created as the narrowed successor of plf-audit after the mentor call of 22 September and Kevin's Slack reply of 25 September (docs/kevin_answers.md). Copied unchanged: data/products.csv, the corpus with its manifest and README, scripts/check_corpus.py and the pre push hook. Copied with a change: data/indicators.csv gains the tier column, and the research-auditor agent and audit skill were rewritten for this scope on 25 September (rule checks on every data row, scope check against the predecessor's deliverables). Copied as read only history into docs/: the predecessor's decisions.md and kevin_questions.md. Its reading_order.md was copied and then removed on 25 September because it describes the larger project's files; docs/before_you_start.md is the reading list for this scope. Not copied: claims, scorecard and reliability schemas, the coding frame, rubric, scope note, logger and writeup skeletons, which belong to the larger project and stay in the frozen repository.

Five decisions from Kevin's reply. Dairy first, then a poultry unit, broilers or laying hens depending on sources; the poultry unit is a commitment. The three criteria are adoption factors, not filters, so the deliverable is a ranked table with every factor visible and no row excluded. Industry acceptability is read as ease of implementation at low or no cost, made visible through two sourced factors added to FARM naming: hardware class and market breadth. Certification coverage is a count with audit method, not a gate. Nothing further is asked of Kevin.

Schema changes from the predecessor: indicators.csv gains a final column tier (joined, efsa_only, wq_only), filled by scripts/stats.py from the existing columns. sensor_coverage.csv and crosswalk.csv are new; crosswalk.csv drops the predecessor's computed query columns, which now live in results/, and adds section_ref, page and industry_naming. The 0 to 3 mapping and the sum in definitions.md are the ranking heuristic and the only place a later decision can change the order.

Open: the poultry unit's sources. Candidates verified on Crossref on 23 September, content not yet checked: EFSA 2023 Welfare of broilers on farm, EFSA Journal 21(2):7788; Rowe, Dawkins and Gebhardt-Henrich 2019, Animals 9(9):614; Brassó, Komlósi and Várszegi 2025, Animals 15(4):493. Whether either review codes commercial availability and validation the way Stygar does decides whether the poultry unit's sensor coverage rests on validation or on claims.

## 2026-09-25: definitions v0.1 stand; session 1 begins

Manisha asked to continue without changes, so definitions v0.1 is the frame for the extraction. Two conventions added during the first batch. First, a product that is in the Stygar appendix but not in data/products.csv is cited in product_ids as appendix:Provider|Name, so the row still names its evidence; the validator checks only that the field is filled. Second, a keyword that also matches generic aims, such as activity, is kept and the note says so, because the count is reproducible and visible, and removing it would be a judgement about what vendors mean.

Two rows in the first batch are unsure, I006 and I009, and are listed in notes/unsure.md with their candidates. One observation for the write up: rumination, the trait Stygar validate most often, maps to no EFSA or Welfare Quality measure at all.
