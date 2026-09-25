# Reading order

Inherited from the plf-audit repository on 25 September 2026. Part 1 refers to that repository's files (its coding frame, rubric and Kevin questions belong to the larger project); Parts 2 to 5 are the sources and apply unchanged here. For this repository, read CLAUDE.md, standard/definitions.md and docs/kevin_answers.md first.

Written 16 September 2026 for whoever picks this repository up, including its author. Read in this order. Times are rough. Each step says what to look for, so the reading has a purpose beyond coverage.

## Part 1. The repository itself, about three hours

| Step | Read | Time | Look for |
|---|---|---|---|
| 1 | `CLAUDE.md` | 10 min | The one sentence question, the six deliverables, the hard rules. Everything else in the repo is bound by these |
| 2 | `README.md`, the Start here and How to verify any number sections | 10 min | The four columns, and the three kinds of statement: sourced, decided, unknown |
| 3 | `docs/PLF_Project_Resources.md`, Part 1 and Part 2 only | 30 min | The eight problems the critical review found in the original plan and the mentor's steer. This is why the scope is what it is |
| 4 | `notes/decisions.md`, all of it | 40 min | Every judgement call in date order. Pay attention to the corrections entry: what went wrong on the first audit and how it was fixed |
| 5 | `data/README.md` | 15 min | What each CSV holds and what an empty cell means in each |
| 6 | `data/indicators.csv`, opened in a spreadsheet | 30 min | The 57 rows. Then pick five and walk each back to its source, using the notes cell and `corpus/README.md`. If the trail holds for five, it holds |
| 7 | `data/products.csv` | 15 min | The 20 products plus the comparator, and the notes on each validation value |
| 8 | `notes/kevin_questions.md` | 15 min | The eleven open questions. Question 1 (theory of change) and question 10 (which measures count as validated indicators) decide the shape of weeks 3 to 5 |
| 9 | `standard/coding_frame.md` | 20 min | The rules for the claims register. Test them in your head against a vendor sentence such as "detects lameness early". Week 2 depends on agreeing with these |
| 10 | `standard/rubric.md` and `standard/scope_note.md` | 15 min | The seven dimensions, the pass threshold fixed before scoring, and the position the standard does not take |
| 11 | `notes/audit_log.md` and `.claude/agents/research-auditor.md` | 10 min | How a change gets checked before it is pushed, and what the auditor is told to do |

## Part 2. The prior work, about five hours

Every file is in `corpus/` with its source link in `corpus/README.md`. Read the papers in this order because each one sets up the next.

| Step | Read | Time | Look for |
|---|---|---|---|
| 12 | Maroto Molina et al. 2020, `maroto_molina_2020.pdf`, 6 pages | 40 min | Table 1, the Welfare Quality principles, criteria and measures. Then their measure by measure account of what technology could monitor each. This is columns 1 and 2 as they existed before the project. Check three rows of indicators.csv against it while reading |
| 13 | Stygar et al. 2021, `stygar_2021.pdf`, 15 pages | 60 min | Page 3 for the definitions of external self validation and external independent validation. Table 1 on page 6 for the 18 validated technologies and which column each reference sits in. Table 2 for which traits validated well. The headline: 129 technologies, 18 externally validated |
| 14 | Stygar supplementary, `stygar_2021_supplementary.xlsx` | 20 min | Sheet 1, the 129 products, is where products.csv came from. Sheet 2 codes the 42 validation studies. Look at the products chosen for the register and the ones left out |
| 15 | Tuyttens, Molento and Benaissa 2022, `tuyttens_2022.pdf`, 12 pages | 40 min | The twelve threats in four categories. The two direct threats the standard scores: threat 3, poor external validation, and threat 4, focusing on the measurable rather than the most meaningful indicators. The indirect threats, which the scope note answers |
| 16 | Elliott and Werkheiser 2023, `elliott_werkheiser_2023.pdf`, 11 pages | 30 min | The framework has four parts: audience, content, challenges and strategies. Table 1 lists five audiences (scientists and engineers, farmers, consumers, industry groups, regulators) and five kinds of content. They name independent verification as a strategy but specify no mechanism for it. List what they leave unspecified: what to log, how to trace an alert to its data, how records are kept from being altered, how a claim is scored. That list is the gap this project fills |
| 17 | Guarino, Norton, Berckmans, Vranken and Berckmans 2017, `berckmans_2017_euplf_blueprint.pdf`, 6 pages | 20 min | The gold standard idea for validating PLF tools. This is where validation thinking in the field started. Note the first author is Guarino |
| 18 | Rutten et al. 2013, `rutten_2013.pdf`, 26 pages, read the first eight | 30 min | The four level model: technique, data interpretation, integration, decision. The data lineage requirement in column 4 is "can a level IV decision be traced to level I data", in their terms |
| 19 | Gómez et al. 2021, `gomez_2021.pdf`, skim | 15 min | The same pattern as Stygar for pigs. Cited for the write up, not extracted |

## Part 3. The welfare indicators, about two hours

| Step | Read | Time | Look for |
|---|---|---|---|
| 20 | EFSA 2023 dairy cows, `efsa_2023_dairy_cows.pdf`, section 4 only, pages 29 to 78 | 90 min | The five welfare consequences and the ABM tables: 16, 17, 18, 27, 31, 32, 33, 42, 46. Each ABM has a definition, a feasibility rating and a sensitivity and specificity note. The feasibility ratings matter: EFSA calls lying time low feasibility because validated monitors are not widely available, which is exactly the gap a sensor standard addresses |
| 21 | Welfare Quality dairy protocol, `welfare_quality_dairy.pdf`, pages 20 to 45 | 30 min | How each measure is scored on farm. PDF page 35 (printed page 34) for somatic cell count from individual cow records, which is why I007 and I057 are separate rows |

## Part 4. Certification and law, about three hours

Read these after the indicators, because column 3 is about which indicators the schemes require.

| Step | Read | Time | Look for |
|---|---|---|---|
| 22 | ICAR page, `icar_validated_sensors.html`, and `icar_section11.pdf` first ten pages | 30 min | On the saved page: three validated systems, all milk yield or composition, and the application checklist, which becomes the disclosure dimension. In Section 11: what ICAR tests and what it never asks about |
| 23 | One ICAR validation report, `icar_panazoo_report.pdf`, 4 pages | 10 min | What an ICAR test actually checks: agreement with a reference device. Nothing about logging or access |
| 24 | RSPCA dairy standards 2026, `rspca_dairy_standards_2026.pdf`, the Health section from page 42, including Lameness at page 46 | 45 min | Every requirement that names an animal based indicator, and how it is checked. Keep the justification document open beside it |
| 25 | FARM Animal Care v5, `farm_animal_care_v5.pdf`, 164 pages, the animal observation and lameness sections | 30 min | The numeric thresholds: locomotion score and lameness benchmarks. This is the industry acceptability proxy |
| 26 | GAP dairy v2.0 and Certified Humane dairy, skim | 30 min | The same extraction, lighter. GAP is the scheme that launched with a sensor partner |
| 27 | `eu_data_act_chapter2.md`, Articles 3 to 5 | 20 min | The user's right to access product data and share it with a third party. The access and ownership dimension is this right, applied |
| 28 | `eu_ai_act_art12_13_26.md`, Article 12 and Article 26(6) | 15 min | Automatic logging over the system lifetime, six months minimum retention. The logging dimension borrows this wording |
| 29 | `cap_code_rule_3_7.md` | 10 min | Objective claims need documentary evidence. Every register row with evidence_cited none is a claim that would fail this rule if advertised in the UK |

## Part 5. The course materials, about three hours, evenings

| Step | Read or watch | Time | Look for |
|---|---|---|---|
| 30 | `simoneau_gilbert_birch_2024.md` | 20 min | The four principles. Principles 2 and 3 are column 4 stated as ethics |
| 31 | `boddy_welfare_tech.md` and `boddy_industry_table.md` | 20 min | The theory of change argument: welfare people specifying the tech, and sitting at the industry's table |
| 32 | `brown_2024_restrict_ai.md` | 20 min | The strongest counter position. The write up answers it in one paragraph: a standard that makes claims checkable removes the marketing advantage of unverified claims, it does not increase adoption |
| 33 | `taylor_2024_ai_factory_farming.md` and `mckay_shah_2025_forecast.md` | 30 min | Framing and scale for the write up |
| 34 | The Livestack episodes 25 and 26, the AI4Animals talk, the Dawkins talk | 2.5 hours | Listed in `docs/PLF_Resources_To_Share_With_ClaudeCode.md` section D. Write two paragraphs of notes into `notes/course_notes.md` afterwards. Episode 25 informs the audit_method column; the AI4Animals talk is the comparator |

## Before week 2 starts

One file is still missing, `van_erp_rutter_2020.pdf`, see the missing files table in `corpus/README.md`. Send Kevin the Friday message with the theory of change question first. Spot check ten rows of your own choosing in indicators.csv against the sources; if any fails, open a decisions entry before anything else is built on it.
