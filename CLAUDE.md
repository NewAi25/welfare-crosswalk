# Instructions for Claude sessions in this repository

## The question

Item 13 on Kevin Xia's Top 30 list, for dairy cows ([his text](1_sources/kevin_item_13.md)): a three way crosswalk of validated welfare indicators, against what commercial sensors measure, against what certification schemes require and audit. He names two valuable cells: indicators already measured by sensors but required by no scheme, and indicators required by schemes but checked by hand.

Kevin's steer. The three part question, indicators that are (a) measurable by AI, (b) acceptable to industry and (c) covered by existing sensors or certification schemes, comes from Kevin's proposal on the call of 22 September 2026 ([automated notes](1_sources/kevin_call_2026-09-22.md), written by a meeting tool, not Kevin's words), as written up in Manisha's smaller scope analysis, which Kevin quotes in his Slack reply of 25 September ([his reply](1_sources/kevin_slack_2026-09-25.md)). Item 13 itself has no (a), (b), (c) list. In that reply Kevin calls industry acceptability, "covered by existing sensors" and "covered by existing certification schemes" soft factors that make adoption easier, and says that for industry acceptability the real question is how easily a measure can be implemented, ideally at low or no cost. So the deliverable is a ranked table with every factor visible. Nothing is filtered out.

This repository follows the frozen predecessor github.com/NewAi25/plf-audit, which is public. Sentient Futures incubator, mentor Kevin Xia, author Manisha Sarkar.

## The four folders

1. [1_sources](1_sources): the source documents, [manifest.csv](1_sources/manifest.csv) with a link and a fingerprint (SHA256 hash) for each, and the kevin_*.md files that hold what was received from Kevin: his item 13 text, his Slack reply (which quotes three of Manisha's questions) and the automated notes of the call. Only the four open licence files are committed (stygar_2021.pdf, stygar_2021_supplementary.xlsx, maroto_molina_2020.pdf, efsa_2023_dairy_cows.pdf). The others stay on disk and are never committed; .gitignore keeps them out.
2. [2_research](2_research): [rules.md](2_research/rules.md) (how every column is filled and scored), the four tables (indicators.csv, products.csv, sensor_coverage.csv, crosswalk.csv), [decision_log.md](2_research/decision_log.md), [audit_log.md](2_research/audit_log.md) and [open_questions.md](2_research/open_questions.md).
3. [3_code](3_code): check_tables.py, count_vendors.py, check_sources.py, build_output.py and the push gate hooks/pre-push. Each script explains itself at the top; read that before running it.
4. [4_output](4_output): the Excel answer.

## Deliverables

1. [4_output/welfare_crosswalk_dairy.xlsx](4_output/welfare_crosswalk_dairy.xlsx). It is built only by `python 3_code/build_output.py`, never edited by hand.
2. The four tables in 2_research, complete for dairy. crosswalk.csv has one row per indicator per scheme for the four schemes (RSPCA Assured, FARM v5, Global Animal Partnership, Certified Humane), with the requirement quoted and its section and page.
3. A write up of about 1,500 words and a one page entry in the format of Kevin's list, both in 4_output when written.
4. A poultry unit after dairy, same tables and rules: broilers, or laying hens if that is where the sources are.

## Hard rules

1. Public documents only. Never contact a vendor. Never fetch anything behind a login.
2. Never make a welfare science judgement. Every value follows a written rule in rules.md. A cell the rules do not settle is coded unsure, with the candidate readings in the row and a line in open_questions.md. It is resolved only by tightening a rule with a dated decision_log.md entry, or it stays unsure in the published table. It is never resolved by asking Kevin and never guessed.
3. Every decision not covered by a rule gets a dated entry in decision_log.md before it is applied. A change to rules.md also gets a new version and a row in its change log, and a rewording must keep the meaning unless the decision_log entry says the meaning changes.
4. Column names and column order never change without a decision_log.md entry. Run `python 3_code/check_tables.py` after every edit to a table.
5. Every value is one of three kinds, and the kind is visible: sourced (document and page, or study number, in the row), decided (a dated decision_log.md entry) or unknown (unsure, none, not_covered). Never leave a cell blank where a source was checked and nothing was found; say so in the row.
6. Every source a table cell, rule or count rests on has a row in manifest.csv before it is used; papers read only as abstracts in a literature check, and candidates named in decision_log.md, are cited by DOI until a cell rests on them. A new source is fetched, fingerprinted and recorded the same day (`python 3_code/check_sources.py --record --only <file>`). `python 3_code/check_sources.py --local` must pass before every commit.
7. Every crosswalk.csv row quotes the requirement exactly and gives section and page. Every sensor_coverage.csv row names its products, its study_numbers and the search_words behind vendors_naming_it.
8. The kevin_*.md files hold only what was received, apart from survey and calendar links removed from the call notes, which their header states: Kevin's item 13 text, his Slack reply verbatim, and the call notes as the meeting tool wrote them, each under a header naming the source and date. Nothing is added to them. Notes about them go in decision_log.md. When describing them, say which words are Kevin's: the call notes are a tool's summary, and the Slack reply quotes Manisha's questions.
9. Nothing is pushed without a logged AUDIT PASS from the research-auditor agent in audit_log.md. The push gate (3_code/hooks/pre-push, turned on with `git config core.hooksPath 3_code/hooks`) refuses a push without it, and also refuses one where the tables fail their checks, a fingerprint does not match, or the Excel file does not match the tables.
10. Writing for readers who do not code: funders, welfare people, Kevin. Short sentences, plain words, every technical term explained the first time, varied sentence length, no dashes as punctuation, no bullet lists in the write up. Every number comes from a table or a script output. When you describe a source, open it first. If unsure, say less.
11. Stage files by name. Never commit the source files that are not open licence, the video files or docs/.

## The batch routine

Work in batches of ten rows.

1. Start the session by reading decision_log.md, open_questions.md and the README section "Answers so far", and say what done looks like for the session.
2. Fill ten rows, each with the evidence behind it, following rules.md.
3. Run the checks with `PYTHONIOENCODING=utf-8`: `python 3_code/check_tables.py`, `python 3_code/count_vendors.py` (it only compares; `--write <ids>` saves a fresh count) and `python 3_code/check_sources.py --local`.
4. Rebuild the Excel file with `python 3_code/build_output.py`, then confirm with `python 3_code/build_output.py --check`.
5. Update the README section "Answers so far" from the Read me sheet and the tables.
6. Commit the batch, naming it in the message. Run the audit skill (/audit), which launches the research-auditor agent on everything that differs from origin/master. Fix every finding, commit, and audit again until it returns AUDIT: PASS.
7. On PASS, add the row to audit_log.md, commit it as `Audit: PASS for <short hash>`, and push.
8. Manisha spot checks ten rows of the pushed batch against the source pages before the next batch starts. Each spot check is logged in decision_log.md with its date and the rows read; a spot check that is not logged is never described as done. Anything she finds is corrected with a decision_log.md entry and audited again.

## GitHub

Public repository NewAi25/welfare-crosswalk. Run `gh auth switch --user NewAi25` before a push and `gh auth switch --user manisha-oz` after it.

## Kevin

Mentor time is one to three hours in total. The scope questions are answered in his Slack reply of 25 September; nothing further is asked of him. The Friday update is one line and a link on Slack, with no question. Help requests, such as a paywalled paper or a welfare science look at the final table, go to the Sentient Futures request help channel.

## Fixed citations

Use these exactly. Any other form is wrong.

1. Stygar et al. 2021, Frontiers in Veterinary Science 8:634338. They found 129 sensor technologies on the market for dairy cow welfare assessment, of which 18 had been externally validated.
2. Maroto Molina et al. 2020, Journal of Dairy Research 87(S1): the mapping of Welfare Quality measures to sensor technologies.
3. The Welfare Quality dairy protocol in 1_sources is version 3.2, February 2024.
4. EFSA 2023, the scientific opinion on the welfare of dairy cows, EFSA Journal 21(5):7993.
5. ICAR (the International Committee for Animal Recording). Its list of validated sensor systems, saved on 16 September 2026, names three: the Ekomilk Horizon Unlimited milk analyser (somatic cell count and milk composition), the Brolis BLH01 in line sensor (milk fat and protein) and the Panazoo MMI sensor (milk yield). Somatic cell count is an indicator in this table (I057 from Welfare Quality, I058 from EFSA), and EFSA reads subclinical ketosis (I021) and subacute ruminal acidosis (I025) from milk fat and the fat to protein ratio. So never write that none of the three measures a welfare indicator; an earlier version of this file said so and was wrong. The Ekomilk report found its somatic cell count met ICAR's accuracy limit only between 0 and 500,000 cells per ml, not over the full range.
