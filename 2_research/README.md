# How the research was done and how to check it

This folder holds the research behind the dairy cow crosswalk: the written rules, the tables, and the logs of every decision and every check. The answer itself is one Excel file, [../4_output/welfare_crosswalk_dairy.xlsx](../4_output/welfare_crosswalk_dairy.xlsx), and a script builds it from the tables in this folder. Nobody types into it by hand.

A crosswalk is a table that lines things up side by side. Here it lines up three things for each welfare indicator, which is a measure of how an animal is faring, such as lameness or body condition. The three things are: whether a commercial sensor measures the indicator, whether certification schemes require it, and how they check it. The question comes from item 13 of Kevin Xia's Top 30 list ([his text](../1_sources/kevin_item_13.md)).

This page explains how the tables were filled and how anyone can check them without writing code. It describes the state as of 3 October 2026.

## 1. What is in this folder

| File | What it holds |
|---|---|
| README.md | This page. |
| [rules.md](rules.md) | The written rules. For every column it gives the values allowed and the rule that decides which value a row gets. Its version is at the top and its change log at the end. The older column guide, tables_explained.md, was merged into it on 2 October and removed. |
| [indicators.csv](indicators.csv) | The 58 welfare indicators, one row each, with where each source lists it. A CSV file is a plain spreadsheet; Excel opens it. |
| [products.csv](products.csv) | 20 sensor products described in more detail, including whether a published study tested each one. |
| [sensor_coverage.csv](sensor_coverage.csv) | For each indicator checked so far: whether a product measures it, what device it needs, how many vendors name it, and the pages that show this. |
| [crosswalk.csv](crosswalk.csv) | What the four certification schemes require for each indicator, and how they check it. So far it holds only the column headings. |
| [decision_log.md](decision_log.md) | Every judgement the rules did not cover, dated and written down before it was applied. Entries are not edited once pushed, so older entries use the file and column names of their day. |
| [audit_log.md](audit_log.md) | One row for each audited version that was published, recording the AI audit that allowed it (section 5). |
| [open_questions.md](open_questions.md) | Cells the rules do not settle, one line each, with the factor, the possible readings and the pages behind them. A line that has been resolved stays, with its resolution. |
| [literature_check_2026-09-29.md](literature_check_2026-09-29.md) | A check, made on 29 September, of whether newer reviews have updated the two sensor sources. |

## 2. The method in four steps

### Step 1. Choosing the 58 indicators

The indicators come from two documents. The first is the 2023 scientific opinion of the European Food Safety Authority (EFSA) on the welfare of dairy cows, EFSA Journal 21(5):7993 (efsa_2023_dairy_cows.pdf (link only, see [1_sources/README.md](../1_sources/README.md))). The second is the Welfare Quality assessment protocol for dairy cows, version 3.2 of February 2024, which sets out how an assessor scores a farm. It is in 1_sources/welfare_quality_dairy.pdf on the author's disk; its licence does not allow it to be committed, so download it from the link in [manifest.csv](../1_sources/manifest.csv).

The rule is [rules.md](rules.md), section 4.1. From EFSA, the rows are every animal based measure (a measure taken on the animal itself, not on its housing) in the nine tables where EFSA assesses measures for its five welfare consequences: Tables 16, 17, 18, 27, 31, 32, 33, 42 and 46. Each of these tables gives the feasibility, sensitivity and specificity of each measure. From Welfare Quality, the rows are every measure in the protocol overview on PDF page 22 (printed page 21). Most of these are animal based. Six are about resources, such as housing or water points, and three are about management, as the Scope line of each measure in the protocol says.

Three adjustments are written into the rule. The two Welfare Quality lameness measures, for loose housed and for tied cows, share one row, I001. The one Welfare Quality measure of integument alterations (hairless patches and lesions or swellings on the skin, PDF page 30) is split into I004 and I005, to follow EFSA's separate hock and knee measures. Thermal comfort, for which the protocol says no measure has yet been developed, gets its own row, I039. That gives 32 EFSA rows and 32 Welfare Quality rows. Six of them are the same measure in both, so there are 58 rows: 26 listed by EFSA only, 26 by Welfare Quality only, and 6 by both. The column listed_by in indicators.csv shows which, so a reader who trusts only Welfare Quality can set the EFSA only rows aside.

Some EFSA tables were left out on purpose, and the decision_log entries of 2 October 2026 say why. Tables 15 and 26 list measures found in the literature on lameness and mastitis; EFSA then names the measures it actually assesses in Tables 16 and 27. Tables 51 to 59 belong to EFSA's separate farm level, risk based scheme. Appendix K Table K.1 lists the measures shown to experts during a consultation, which is a working step, not an assessed set.

Two changes were made on 2 October. EFSA Table 27 continues onto PDF page 44 with two more measures, so they became rows I058 and I059. Row I042, coughing, was removed, because coughing is not a measure in version 3.2 of the protocol; the version note on PDF page 1 records that the coughing measurement was dropped in version 3.0. The other rows kept their numbers, so the identifiers run from I001 to I059 with no I042.

Kevin's item 13 ([kevin_item_13.md](../1_sources/kevin_item_13.md)) names three kinds of source for validated welfare indicators: Welfare Quality, AWIN and the species literature. AWIN is not used for this dairy unit.

For the species literature, this project uses the EFSA opinion alone, not a wider reading of studies on dairy cows. That choice was carried over from the project before this one, and no document here records a reason for it. Each EFSA measure carries EFSA's own ratings of feasibility, sensitivity and specificity, and some are low; the notes column of indicators.csv quotes them where they matter, as on I012, lying time, which EFSA rates low on feasibility on farm.

### Step 2. Reading the sensor evidence

This is column 2 of the crosswalk, in [sensor_coverage.csv](sensor_coverage.csv). It reads from two sources.

The first is Stygar et al. 2021, Frontiers in Veterinary Science 8:634338 ([stygar_2021.pdf](../1_sources/stygar_2021.pdf)). Their abstract, on PDF page 1, says a market search found 129 technologies on sale that could be used to assess the welfare of dairy cows, and that only 18 of them had been externally validated (14%). Externally validated means tested in a published study on animals and herds other than those the product was built on. Stygar then split those studies in two (footnotes to Table 1, page 6). An independent validation is one whose authors were not involved in developing the technology. A self validation is one where at least one author developed it or represents the company that sells it. Three parts of Stygar are used. Table 1 on page 6 lists each validated product with the reference numbers of its studies, in an independent column or a self column. Table 2 on page 7 lists the trait each product was validated on, such as lying time or body condition, and whether it met the authors' high performance threshold or fell below it. The supplementary spreadsheet ([stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx)) lists the 129 products, each with the vendor's own one line description of what it does (the AIM column), and the validation studies.

The second source is Maroto Molina et al. 2020, Journal of Dairy Research 87(S1) (maroto_molina_2020.pdf (link only, see [1_sources/README.md](../1_sources/README.md))). They go through the Welfare Quality protocol measure by measure and say which technologies could assess each one. This source is used where no product covers an indicator, to tell whether researchers have proposed a way to measure it. They give no rating of their own, so the column maroto_molina_rating (yes, partial, no or not_covered) is this project's coding of their text, under rule 4.3 in rules.md. Since 3 October that rule is read literally: yes only where the passage says the technology is commercially available or in use on commercial farms. Across the 58 rows the rating is yes on 2 (I023 and I039), partial on 29, no on 2 and not_covered on 25.

Each indicator gets one of five labels for sensor evidence (rules.md, rule 4.2):

| Label | Meaning |
|---|---|
| validated_commercial | A product in Stygar's list measures it, and Stygar record at least one external validation study of that product on that trait. |
| commercial_unvalidated | A product's description names it, and no external study is recorded. |
| research_only | No product, but Maroto Molina name research level technology or a substitute measure. |
| none | No product, and Maroto Molina say sensors cannot provide it or do not discuss it. |
| unsure | The sources do not settle it. The possible readings go in the row and in open_questions.md. |

A validation only counts when Stygar's trait and the indicator are the same measure. In the words of rules.md, a product validated on one trait does not earn a grade on another.

Two more columns come from the same sources. device_needed is the cheapest kind of equipment that measures the indicator and is on sale: nothing extra because the value is already in milk or farm records (routine_data), one device per farm or barn such as a camera (farm_fixed), one device per animal such as a collar (animal_mounted), a sample or a scoring by a person (sample_or_procedure), or no technology named (none). vendors_naming_it counts how many of the 129 product descriptions contain the search words written in the row. It counts claims, not proof.

So far 40 of the 58 rows are done, I001 to I040. Of these, 7 are validated_commercial, 1 is commercial_unvalidated, 15 are research_only, 12 are none and 5 are unsure. For device_needed the 40 rows split into 7 routine_data, 17 farm_fixed, 8 animal_mounted, 1 sample_or_procedure and 7 none. The other 18 rows, I041 and I043 to I059, are not yet checked.

Why only these two sources? The decision_log entry of 29 September answers this. It was a design choice made when the rules were written, not an instruction from Kevin. Stygar apply a stated standard for validation, every grade can be checked against a page, and the project had a budget of about 25 hours. The cost is that the table shows the market and the research as they stood around 2020. A later product or a later study is invisible, and a grade of none means none in these two papers.

The [literature check of 29 September](literature_check_2026-09-29.md) then asked whether anyone had repeated either paper since. It found no review that repeats Stygar's method, and none that repeats Maroto Molina's measure by measure mapping. It found partial updates, read so far only as abstracts: Lee, Brause, Foy and Cantor 2025 on wearable sensors for behaviour, Hudson and colleagues 2026 on automated lameness detection, Islam and colleagues 2026 on cameras, Fuentes and colleagues 2026 on social behaviour, and Leliveld and Provolo 2020 as a second source for the research_only and none grades. On 30 September Manisha approved an update pass and deferred it (decision_log, 30 September). The order is: finish column 2 on the two sources, then do column 3, then the update pass, before the write up. The Stygar grade stays as the 2021 baseline. The update pass adds a separate column, evidence since 2021, with its own sources, and checks every research_only and none row against Leliveld and Provolo. It is estimated at nine to eleven hours and has not started.

### Step 3. Reading the certification schemes

This is column 3, in [crosswalk.csv](crosswalk.csv). It has not started.

Four schemes will be read (rules.md, rule 4.7): RSPCA Assured dairy cattle, April 2026; FARM Animal Care version 5, the US industry programme written by the National Milk Producers Federation; Global Animal Partnership dairy version 2.0; and Certified Humane dairy, Edition 23. Their documents are in 1_sources on the author's disk but are not committed, for licence reasons; the links are in [manifest.csv](../1_sources/manifest.csv).

Each indicator will get one row per scheme. The row quotes the requirement word for word with its section and page, copies any number it sets, and records how the scheme checks it: an inspector looks at the animals (visual_inspection), an inspector checks farm records (records_review), the scheme accepts sensor data (sensor_accepted), the scheme does not say (unspecified), or its text does not settle it (unsure, with a line in open_questions.md). A requirement counts only if it names the measure or a direct synonym. A rule about housing that would affect the measure, such as a minimum cubicle size, is recorded as related but does not count as requiring the indicator. rules.md gives three worked examples, two of them quoted from the RSPCA and FARM texts. For FARM alone a fourth column, farm_naming, records whether the US industry programme names the measure, with or without a number to meet.

### Step 4. The score and Kevin's two lists

In his Slack reply ([kevin_slack_2026-09-25.md](../1_sources/kevin_slack_2026-09-25.md)) Kevin called industry acceptability, and coverage by existing sensors and by existing certification schemes, soft factors that make adoption easier, not hard requirements. So no indicator is dropped. Instead each indicator gets five factors, each turned into 0 to 3 points, and the points are added to a score from 0 to 15 (rules.md, section 5; [3_code/build_output.py](../3_code/build_output.py) applies it).

| Factor | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| Sensor evidence | validated_commercial | commercial_unvalidated | research_only | none or unsure |
| Device needed | routine_data | farm_fixed | animal_mounted | anything else |
| Vendors naming it | 10 or more | 3 to 9 | 1 or 2 | none |
| Named by FARM | named with a number | named | only a related rule | not named or unsure |
| Schemes requiring it | all four | two or three | one | none |

The score is a sort order, not a welfare judgement and not a recommendation. Every factor stays visible in the Excel file, so a reader can sort by any one of them instead. Indicators with the same score are listed in order of their identifier. A factor not yet researched counts 0, so today's ranking is provisional, and the Excel file says so in the heading of the rank column.

The five factors are scored independently. So one row can earn sensor points from a tested product that is an added device, and device points because the value is already in records. I021 and I025 work this way: the sensor points come from AfiLab, an inline milk analyser, and the device points from routine milk recording. Tested products and products whose description names it are separate columns too, so a product can be tested without its description naming the measure, and the reverse. On I012, Track a))) Cow and RumiWatch were tested for lying, but their descriptions do not contain the search words.

Kevin's first list is, in his words, indicators "already instrumented but not required". An indicator is on it when its sensor evidence is validated_commercial or commercial_unvalidated and none of the four schemes requires it. It is reported only once all four schemes have been read for that indicator, because before then a count of zero schemes means not yet read. Today 8 indicators are graded Tested or Claimed (sensor evidence validated_commercial or commercial_unvalidated) and are waiting for the scheme check, so the list reads not yet known for them. The 5 indicators whose sensor evidence is unsure read Unclear, because they could join the list once their question is settled.

Kevin's second list is indicators required by schemes but checked by hand. An indicator is on it when at least one scheme requires it and checks it by inspection or by records, not by accepting sensor data. The sensor evidence is shown beside it. Where a scheme requires the indicator but its text does not settle how it is checked (how_checked unsure), the list reads Unclear, unless another scheme that requires it checks it by hand. Today no scheme has been read, so this list reads not yet known.

Both tests are set out in rules.md, section 6, and [build_output.py](../3_code/build_output.py) applies them as written there: it holds back list 1 until all four schemes are read for an indicator, and it uses the wider list 2 test. The decision_log entry of 2 October on the two item 13 views says the script still applied the old filter; the entry of 3 October on build_output.py records that it now applies both tests.

## 3. What "checked" means

A value in the tables is checked in one of three ways: read the page, apply the rule, or count again. A fourth kind of cell, not known yet, has nothing to check; it says openly what is missing.

**Read from a page.** The row names the document, the page and the table, and often the study number. To check it, open that page and read it. The where_to_check column of sensor_coverage.csv, shown as "Where to check" in the Excel file, gives these references.

**Decided by a written rule.** The row's label follows from what the page says under a rule in [rules.md](rules.md). To check it, read the rule, then confirm that the row follows it. Where the rules did not cover a case, the decision is a dated entry in [decision_log.md](decision_log.md), written before it was applied.

**Counted.** vendors_naming_it and every total on this page are counts. To check one, count again: open the Stygar spreadsheet in Excel, search column E (AIM) for each search word of the row with Find (Ctrl+F), and count the products that match at least one word. Or run the script that does the same count, [3_code/count_vendors.py](../3_code/count_vendors.py).

**Not known yet.** These are marked openly: unsure (the rules do not settle it, with a line in [open_questions.md](open_questions.md)), none (the sources were checked and name nothing), or not yet checked (nobody has looked yet). A cell is never left blank where a source was checked and nothing was found.

## 4. One worked example: I023, body condition

This follows one row from the source pages to the Excel file. Body condition is how much fat a cow carries, judged from her shape.

**The indicator.** EFSA Table 46, PDF page 75, lists body condition scoring as a measure for subclinical ketosis, a metabolic disorder. EFSA defines it as assessing body fat by "evaluating overall body shape and fat cover with a scoring from 1 to 5", citing Welfare Quality 2009. The Welfare Quality protocol lists body condition score in its overview on PDF page 22 (printed 21), under the criterion absence of prolonged hunger. Its method, on PDF pages 22 and 23 (printed 21 and 22), says the animals are only observed, never touched. Each cow scores 0 for regular condition, 1 for very lean or 2 for very fat, the last two only when the signs show in at least three body regions, and the Scope line calls it an animal based measure. Because both sources list it, the row is joined, one of the 6. The row's notes record that the two scales differ.

**The sensor evidence.** Stygar Table 2, PDF page 7, has a row for the trait body condition scoring, validated on a commercial farm, with one product: DeLaval Body condition scoring, reference 48. The text on the same page says that all tools for physical condition and health were classed as lower performance, below the authors' high performance threshold. It adds that the technology was reliable for cows of average body condition but did not score thinner or fatter cows accurately. Stygar Table 1, PDF page 6, has the row Body Condition Scoring, DeLaval International AB, Tumba, Sweden, sensor Camera, with reference 48 in the column headed Independent validation. The reference list on PDF page 14 gives reference 48 as Mullins and colleagues 2019, "Validation of a commercial automated body condition scoring system on a commercial dairy farm", Animals 9:287.

**The spreadsheet.** In stygar_2021_supplementary.xlsx, sheet Appendix table 1, row 31 is DeLaval BCS, provider DeLaval, sensor type Camera (3D), aim "Automatic body condition scoring", country Sweden, validation studies yes. On sheet Appendix table 2, row 37 is the Mullins study, with the same DOI, 10.3390/ani9060287, on a commercial herd in the USA, coded external independent validation.

**The rule that gives the label.** validated_commercial needs a product in Stygar's list, a trait in Table 2 that is the same measure as the indicator, and a study number against that product in Table 1. All three hold: the trait is body condition scoring, the product is DeLaval BCS, and the study is 48. So sensor_evidence is validated_commercial, the product is P009 in products.csv, and study_numbers is 48. Maroto Molina, on page 2, say the Welfare Quality scoring is less precise than what "commercially available technologies" can provide, and name the DeLaval BCS camera, which uses 3D imaging to give a score on a 5 point scale in steps of 0.1. Under the rule for their rating, naming commercially available technology gives yes.

**The device class.** Three product descriptions name body condition. Two are 3D cameras, DeLaval BCS and LIC Protrack BCS, which are one device per farm or barn. The third, Bayer Cowdition, is a mobile app, and the spreadsheet does not say who or what does its scoring. The row records this, and device_needed is farm_fixed.

**The search words and the count.** The search words are "body condition" and "bcs". In column E of the spreadsheet they match three products: Bayer Cowdition, DeLaval BCS and LIC Protrack BCS. So vendors_naming_it is 3, and `python 3_code/count_vendors.py I023` prints the same three.

**The cell in the Excel file.** On the Answer sheet, the row with ID I023 reads: can a sensor measure it, "Tested: a product in the Stygar list was tested for this in a published study", followed by a pointer to the column What was tested, and how well; tested products, DeLaval BCS; what was tested, and how well, "Body condition scoring, Table 2 page 7, commercial farm, lower performance column"; products whose description names it, 3; device needed, one device per farm or barn. FARM and the schemes read not yet checked. The score is 7, made of 3 + 2 + 2 + 0 + 0: 3 for the validated product, 2 for one device per farm, 2 for three vendors, and 0 for the two scheme factors not yet read. Kevin's two lists read not yet known. On the Sensors x products sheet, row I023 marks DeLaval BCS as validated, and Cowdition and Protrack BCS as named.

## 5. How the work is checked

There are three layers.

**Written rules, so that no cell rests on judgement.** Every label follows a rule in [rules.md](rules.md). The first version was fixed before the rows were filled, and every change since is dated in its change log. When a row does not fit a rule, it is not guessed. It is marked unsure, or the rule is tightened with a dated entry in [decision_log.md](decision_log.md) and a new version of rules.md.

**An AI auditor, separate from the writer.** Before anything is published, an AI agent, the research auditor ([.claude/agents/research-auditor.md](../.claude/agents/research-auditor.md)), reopens every cited page and checks every claim and every row against the source and the rules. It is Claude, a language model, running in its own session from a fixed checklist, so it has no memory of writing the rows. It is not a person and not an outside reviewer. It does not edit anything; it reports each claim as confirmed, wrong, unsupported, imprecise or overstated, and returns PASS or FAIL. Only a PASS allows publication, and the result is recorded in [audit_log.md](audit_log.md). That log lists every version that passed, with what was checked and found. The reorganisation of 2 and 3 October went through several rounds of audit, as decision_log.md describes, and is published only with a PASS row in audit_log.md.

**A human spot check, planned.** The working routine in [CLAUDE.md](../CLAUDE.md) says that after each batch is published, Manisha Sarkar, the author, reads ten rows against the source pages before the next batch starts. No spot check is yet recorded in decision_log.md or audit_log.md, so none should be counted as done. No review of the tables by a welfare scientist is recorded here either.

Under these sit four mechanical checks, small programs in [3_code](../3_code) that anyone can run. They check that the files are consistent; they cannot tell whether a value is true, which is the job of the auditor and of the reader with the page open.

1. [check_tables.py](../3_code/check_tables.py) checks that the four tables have the right columns, use only the allowed labels, have no duplicate or unknown identifiers, and follow the rules that a machine can test. For example, a validated row must name its products and study numbers, and every unsure cell must have a line in open_questions.md.
2. [count_vendors.py](../3_code/count_vendors.py) counts again, from the Stygar spreadsheet, how many vendors name each indicator, and compares the count with the table. It changes nothing unless asked to.
3. [check_sources.py](../3_code/check_sources.py) proves the documents are the ones the research read. Each document in [manifest.csv](../1_sources/manifest.csv) has a fingerprint, a long code computed from the file's exact contents that changes completely if one character changes. With `--local` it recomputes the fingerprints on your copy; without it, it also fetches each link and compares.
4. [build_output.py](../3_code/build_output.py) with `--check` confirms that the Excel file still matches the tables.

The push gate, [3_code/hooks/pre-push](../3_code/hooks/pre-push), runs automatically before every push, which is the step that publishes saved work to the online copy on GitHub. It refuses the push if the version being pushed is not the one checked out, if there are unsaved changes, if check_tables.py, check_sources.py --local or build_output.py --check fails, or if the audit log has no PASS row for the exact version being published (or for the version just before it, when the only change since is the audit row itself). check_tables.py runs the vendor recount itself, so all four checks run. The gate is turned on once per copy of the repository with `git config core.hooksPath 3_code/hooks`.

To run a check yourself, install Python, open a terminal in the repository folder and type, for example, `python 3_code/check_tables.py`. On Windows, set `PYTHONIOENCODING=utf-8` first so the output prints correctly.

## 6. Known limits and what is not done

Public documents only. The project never contacts a vendor and never uses anything behind a login, so what a product does is what the published sources say it does.

The sensor evidence is a 2021 baseline. It rests on the products and studies Stygar and colleagues found for their 2021 paper, and on Maroto Molina's 2020 reading. Newer products and studies are not in the table until the update pass described in Step 2.

A validated product is not the same as an accurate one. Stygar classed every tool for physical condition and health as below their high performance threshold, and for body condition they report it was reliable only for cows of average condition.

[open_questions.md](open_questions.md) has 6 lines. Five are open, all about sensor evidence (I006, I009, I013, I020 and I039). The sixth, on the Maroto Molina rating of I057 and I058, was closed on 3 October 2026 by reading rule 4.3 literally, which gives partial. An unsure row scores 0 on sensor evidence until a rule settles it.

Column 3, the certification schemes, has not started, so FARM naming and scheme coverage are not yet known for any indicator, and neither of Kevin's two lists can yet be given.

Eighteen sensor rows, I041 and I043 to I059, are not yet checked.

The decision_log entry of 30 September also queues a full read of rows I001 to I030 against the wording of rule version 0.1.4, which has not yet been done.
