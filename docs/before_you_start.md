# Read this before starting the work

In this order. About seven hours in total, most of it the sources. The point of each step is written next to it, so you can stop when you have what you need. Steps 1 to 6 are the repository and take about ninety minutes; do them in one sitting. Steps 7 to 14 are the sources you will be extracting from; read each one the day before you extract from it, not all at once.

## The repository, ninety minutes

| Step | Read | Time | Why |
|---|---|---|---|
| 1 | `CLAUDE.md` | 10 min | The question, the deliverables, the rules the work is bound by, the fixed citations. If something in a later file contradicts this, this wins |
| 2 | `docs/kevin_answers.md` | 10 min | Kevin's steer in his own words and the five decisions taken from it. Everything in the definitions follows from this |
| 3 | `standard/definitions.md` | 30 min | The most important file. Five factors, the rule that fills each, the three worked examples for when a scheme requirement names an indicator, and the 0 to 3 mapping that ranks the table. You are approving this; read it as if you had to defend every rule to Kevin |
| 4 | `data/README.md` | 10 min | The four CSV files, every column, what an empty cell means |
| 5 | `data/indicators.csv` in a spreadsheet, sorted by the tier column | 15 min | The 57 rows you will be grading: 6 joined, 24 EFSA only, 27 Welfare Quality only. Notice which ones a sensor could plausibly measure and which could not; the sensor coverage grades will make that explicit |
| 6 | `docs/PLF_Handover_2026-09-23.md`, the Blockers and Insights sections only | 15 min | What went wrong in the larger project and the findings worth keeping, especially the ICAR result and the 24 EFSA only measures |

## The sources for column 2, read before the sensor coverage week

| Step | Read | Time | Why |
|---|---|---|---|
| 7 | Maroto Molina et al. 2020, `corpus/maroto_molina_2020.pdf`, 6 pages | 40 min | Table 1 is the Welfare Quality spine. The text after it says, measure by measure, what technology exists. This fills research_only and none, and the hardware class for measures with no product |
| 8 | Stygar et al. 2021, `corpus/stygar_2021.pdf`, pages 1 to 7 | 60 min | Page 3, the two definitions of external validation. Page 6, Table 1, the 18 validated technologies with reference numbers in two columns. Page 7, Table 2, which traits each was validated on. This fills validated_commercial. Look at Table 1 on the rendered page, not extracted text; the columns matter |
| 9 | `corpus/stygar_2021_supplementary.xlsx`, sheet 1 | 20 min | The 129 products and their stated aims. This is the source of commercial_unvalidated and of market breadth. Skim the AIM column so the keywords you will approve make sense |
| 10 | `data/products.csv` | 10 min | The 20 products already carrying Stygar validation levels and the notes on each |

## The sources for column 3, read before the crosswalk week

| Step | Read | Time | Why |
|---|---|---|---|
| 11 | RSPCA welfare standards for dairy cattle April 2026, `corpus/rspca_dairy_standards_2026.pdf`, contents page, then the Health section from page 42 | 60 min | The richest scheme. Keep `corpus/rspca_dairy_justification_2026.pdf` open beside it; it says why each requirement exists, which goes in notes |
| 12 | FARM Animal Care v5, `corpus/farm_animal_care_v5.pdf`, the animal observation and lameness sections | 40 min | The industry authored programme, so it fills factor 4. Its numeric thresholds are the named_with_threshold cases |
| 13 | GAP dairy v2.0 and Certified Humane dairy Edition 23, `corpus/gap_dairy_standard.pdf` and `corpus/certified_humane_dairy.pdf`, skim the animal health and welfare sections | 40 min | Lighter extraction, same rule |
| 14 | ICAR page, `corpus/icar_validated_sensors.html` | 10 min | The one finding to carry into the write up: three validated systems, none welfare. It frames why sensor_accepted is rare in column 3 |

## Not needed for this scope

The EFSA opinion in full (its ABM tables are already in indicators.csv), the legal texts, the course essays, the coding frame and rubric from the predecessor. `docs/reading_order.md` lists them if the larger project is ever picked up again.

## What to do after reading

Say whether `standard/definitions.md` stands. Any change is a decisions entry before extraction starts. Then session 1 begins with the first ten rows of sensor coverage.
