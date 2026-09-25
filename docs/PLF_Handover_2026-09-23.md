# PLF welfare audit project: attempts, blockers, insights and next steps

Manisha Sarkar, 23 September 2026. Written at Kevin Xia's request after the call of 22 September, so that the work done so far is not lost. Repository: github.com/NewAi25/plf-audit.


## What was attempted

The project set out to answer one question for dairy cattle: can a welfare claim made by a sensor system be verified by someone outside the vendor, and what would the system have to log and expose to make that possible? It combined items #9 and #13 from the Top 30 list with a fourth column, an auditability standard scored against real products. Six deliverables were planned for five weeks: a claims register of 20 products, a crosswalk of indicators against sensors against certification schemes, a seven dimension standard with a rubric, a scorecard, a reference logger proving the logging requirements are cheap, and a write up with a two page certifier annex.

The design was four columns. Column 1, validated welfare indicators, from the EFSA 2023 dairy cow opinion and the Welfare Quality dairy protocol. Column 2, what commercial sensors measure and how well that is validated, from Stygar et al. 2021. Column 3, what certification schemes require and how they audit it. Column 4, what a system must log and prove. Columns 1 and 2 already existed in the literature. Columns 3 and 4 were the new work.


## What got built, 15 to 22 September

| Piece | State | Where in the repository |
|---|---|---|
| Corpus | 31 of 32 sources, 29 of them hash verified against the URL they came from and two whose source sites no longer answer scripted requests, so only the local hash is checked. The one gap is a paywalled paper, van Erp-van der Kooij and Rutter 2020. | corpus/README.md, corpus/manifest.csv |
| Column 1, indicators | 57 rows: EFSA's 30 animal based measures and Welfare Quality's 31 measures, joined only where EFSA itself cites Welfare Quality (6 joins), with the technology Maroto Molina et al. 2020 identify where they discuss the measure (36 rows) and a not discussed flag on the other 21. | data/indicators.csv |
| Column 2, products | 17 dairy sensor products from Stygar's appendix across collars, ear tags, boluses, cameras and milking systems plus leg tags, a load cell plate and an in line milk analyser, the 3 ICAR validated systems, AI4Animals as comparator, each with Stygar's validation level: 7 independently validated, 1 self validated, 9 none. | data/products.csv |
| Column 3, crosswalk | Schema designed with the audit method categories, the industry flag and the three queries item #13 asks for, computed by script. No rows extracted yet. All four standards are in the corpus. | data/crosswalk.csv, scripts/stats.py |
| Column 4 and the rest | Coding frame, rubric, pass threshold and scope note written and fixed. Claims register, standard text, scorecard, logger and write up not started. | standard/ |
| Verification | A separate checking agent reads every factual claim against the source pages before anything is pushed, and a git hook enforces it. Every judgement call is dated in decisions.md; every welfare science question is parked in kevin_questions.md rather than decided in the data. | notes/, .claude/agents/ |


## Blockers

- Scope. Six deliverables in five weeks at 15 to 20 hours a week was too much for one person, and the call on 22 September confirmed it. Week 1 delivered the foundation but not the market scan or the column 4 draft.
- Domain expertise. I am an engineer, not a welfare scientist. The design handled this by taking every indicator from a published protocol and parking every mapping judgement for review, but that made the original plan depend on validation I could not give myself and a mentor could not give in one to three hours. The smaller scope in the companion document is chosen so that it does not have that dependency.
- Accuracy of AI assisted extraction. The repository was built with Claude Code. The first verification pass found nine wrong or unsupported statements (five wrong, four unsupported), among them a wrong first author (the EU PLF blueprint is Guarino, Norton, Berckmans, Vranken and Berckmans 2017, not Berckmans 2017) and a missed EFSA measure. All were corrected before anything was shared, and the checking gate exists because of it. Anyone continuing this should keep the gate.
- Source access. Three publishers block scripted downloads and two stamp every download with the date; both were handled. One paper is paywalled; per Kevin's suggestion the route is the Sentient Futures request help channel.
- Table extraction. Stygar's Table 1 has two reference columns that text extraction merges. For one product the paper and its supplementary table disagree, and the data records the disagreement rather than choosing.


## Insights worth keeping

- ICAR, the nearest existing validation scheme for dairy sensors, has validated three systems, all milk yield or composition, none welfare, and it validates only the claim the applicant chooses to make. Its application checklist (technical manual, internal validation studies, peer reviewed publications, routine checking procedures) is a ready made disclosure requirement.
- 24 of EFSA's 30 dairy measures have no Welfare Quality equivalent, and they are what sensors measure best: lying time, lying bouts, step activity, walking distance. EFSA rates lying time low feasibility on farm because validated monitors are not widely available. Any indicator table has to decide how to show these, and the honest way is as a separate tier, not a ruling.
- Stygar 2021: 129 commercial dairy technologies, 18 externally validated. Lying, standing and rumination validate well; body condition and health detection worse. That is the ceiling on "measurable by AI" for dairy today.
- Maroto Molina 2020 already mapped every Welfare Quality measure to candidate technology, so an indicators against sensors table is not new. The join to what certification schemes require, and how they audit it, is where the value sits. Kevin's steer on the call: certifiers such as RSPCA are the audience that fits the theory of change.
- Elliott and Werkheiser 2023 name independent verification as a strategy but specify no mechanism. Nobody has written what a welfare PLF system must log so a claim can be checked after the fact. That gap is real and remains open if anyone wants the larger project later.


## Next steps

The scope narrows to Kevin's item #13, the three way crosswalk, as one table answering which welfare indicators are measurable by AI, acceptable to industry, and already covered by sensors or certification schemes. The companion document sets out how, for dairy in about 25 hours or for broilers in about 30 to 35, and asks Kevin for three decisions on Slack. Nothing built so far is wasted: the crosswalk was always deliverable 2, and its schema, corpus and checks are in place. The larger standard stays documented in the repository for whoever wants it.

For anyone picking the repository up cold: docs/reading_order.md, Part 1, about three hours, then notes/decisions.md. The README section "How to verify any number" shows how to walk any value back to its source page.
