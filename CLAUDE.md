# Welfare indicators x deployed sensors x certification requirements

## The question
Which welfare indicators are (a) measurable by AI, (b) acceptable to industry for adoption, and (c) potentially already covered by existing sensors or widely used certification schemes? Item #13 on Kevin Xia's Top 30 list: a three way crosswalk for one species, validated welfare indicators against what commercial PLF sensors actually measure against what certification schemes require and audit. The valuable cells are indicators already instrumented but required by no scheme, and indicators required but audited only by inspection. Dairy first, then a poultry unit. Sentient Futures incubator, mentor Kevin Xia.

This is the narrowed successor of `C:\Epoch Ai project\plf\plf-audit` (github.com/NewAi25/plf-audit), which is frozen. Column 1 (57 indicators), most of column 2 (20 products, 17 of them with Stygar validation levels and 3 from the ICAR list), the hash verified corpus and the verification gate were built there and copied here. docs/PLF_Handover_2026-09-23.md says what was attempted and why it narrowed. docs/kevin_answers.md holds Kevin's steer of 25 September 2026: the three criteria are soft factors that make adoption easier, not filters, so the deliverable is a ranked table with every factor visible.

## Deliverables
1. data/crosswalk.csv complete for the four dairy schemes, one row per indicator per scheme, requirement text quoted with section and page.
2. data/sensor_coverage.csv, one row per indicator: sensor coverage grade, hardware class, market breadth, with the product ids and Stygar reference numbers behind each.
3. results/adoption_table.csv, every indicator ranked by ease of adoption with each factor visible, plus the two item #13 views: results/instrumented_not_required.csv and results/required_manual_only.csv. Written by scripts/stats.py, never by hand.
4. writeup/note.md, about 1,500 words, and writeup/list_entry.md, one page in the format of Kevin's list entry.
5. A poultry unit after dairy, same schema, broilers or laying hens depending on which has usable sensor and indicator sources.

## Hard rules
- Public documents only. Never contact a vendor, never fetch anything behind a login.
- Never make a welfare science judgement. Every mapping follows a written rule in standard/definitions.md. Anything the rules do not cover is coded unsure with the candidate reading in notes and a line in notes/unsure.md. It is never resolved by asking Kevin and never guessed; it is resolved by tightening a rule with a decisions entry, or left as unsure in the published table.
- Every decision not covered by a rule gets a dated entry in notes/decisions.md before it is applied.
- CSV headers and column order never change without a decisions entry. Run scripts/validate_csv.py after every edit to data/.
- Every value is one of three kinds and the kind is visible: sourced (file, page or reference number in the row), decided (dated decisions entry), or unknown (unsure, none, not_covered, missing). Never blank where a source was checked and nothing was found; say so in notes.
- Every corpus file has a row in corpus/manifest.csv before it is used. A new source is fetched, hashed and recorded the same day. scripts/check_corpus.py --local must pass before every commit.
- Every row in crosswalk.csv quotes the requirement text and gives section and page. Every row in sensor_coverage.csv names the product ids and Stygar reference numbers behind its grade and the keywords behind its market breadth.
- Nothing is pushed without a logged AUDIT PASS from the research-auditor agent, recorded in notes/audit_log.md. The pre push hook in .githooks/pre-push enforces it. Manisha spot checks ten rows of every batch against the rendered PDF pages before it is pushed, and the batch is not pushed until she says so.
- Prose with no dashes as punctuation, varied sentence length, first person where the author speaks. No bullet lists in writeup/.
- Fixed citations: Twelve Threats is Tuyttens, Molento and Benaissa 2022. The transparency framework is Elliott and Werkheiser 2023. The EU PLF blueprint is Guarino, Norton, Berckmans, Vranken and Berckmans 2017, Animal Frontiers 7(1), never shortened to Berckmans 2017. The measure to technology mapping is Maroto Molina et al. 2020, Journal of Dairy Research 87(S1). Stygar et al. 2021, Frontiers in Veterinary Science 8:634338, report 129 technologies and 18 externally validated. ICAR has validated three sensor systems as of September 2026, none measuring a welfare indicator. The Welfare Quality dairy protocol in the corpus is version 3.2, February 2024.

## Kevin
Mentor time is one to three hours in total. The three scope questions are answered in docs/kevin_answers.md; nothing further is asked of him. The Friday update is one line and a link on Slack, no question. Help requests, including the paywalled paper and a one hour welfare science look at the final table, go to the Sentient Futures request help channel.

## Working style
- Start every session by reading notes/decisions.md and notes/status.md and stating what done looks like for the session.
- Work in batches of ten rows. Show them with the evidence behind each. Wait for the spot check. Continue.
- Commit at the end of every session with a message naming the batch. Update notes/status.md.
- GitHub: private repository NewAi25/welfare-crosswalk. Run `gh auth switch --user NewAi25` before any push and `gh auth switch --user manisha-oz` after.
