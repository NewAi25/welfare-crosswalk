# Rules

Version 0.9.4, 9 November 2026. First fixed as version 0.1 on 25 September 2026, before any sensor row was graded; the indicator and product tables were carried over when this repository was set up on 25 September 2026 (decision_log.md, first entry) and corrected since. Every change is dated in the [change log](#8-change-log) at the end.

## 1. In one page

This project answers item 13 on Kevin Xia's Top 30 list for dairy cows ([his text](../1_sources/kevin_item_13.md)). It sets three things side by side: validated welfare indicators, what commercial farm sensors measure, and what certification schemes require and how they check it. Since 17 October 2026, following Kevin's change request of 7 October 2026, the rows come from two sides, the welfare protocols and the parameters that sensor products say they measure, and a column 1 says whether the welfare sources treat each row as a measure of welfare. Since 5 November 2026, following Kevin's review of November 2026 ([his messages](../1_sources/kevin_slack_review_2026-11.md)), the rows are read once per welfare state and the states are ranked on a priority list, by an ordered set of keys rather than a sum. The research sits in six tables in this folder. This file is the rulebook for those tables. For every column it says what the column means, which rule fills it, and which source the value is read from.

The three part question, indicators that are (a) measurable by AI, (b) acceptable to industry and (c) covered by existing sensors or certification schemes, comes from Kevin's proposal on the call of 22 September ([automated notes](../1_sources/kevin_call_2026-09-22.md)), as written up in Manisha's smaller scope analysis, which Kevin quotes in his Slack reply of 25 September ([his words](../1_sources/kevin_slack_2026-09-25.md)). In that reply he calls industry acceptability, and coverage by existing sensors and by existing certification schemes, soft factors that make adoption easier rather than hard requirements. So each factor is a graded column and every indicator stays in the table. Rows that the welfare sources do not back leave the priority list but are shown on a sheet of their own, and every column stays visible, so a reader can sort again by any one of them (section 5).

The answer itself is the Excel file [welfare_crosswalk_dairy.xlsx](../4_output/welfare_crosswalk_dairy.xlsx). Nothing in it is typed by hand. The script [build_output.py](../3_code/build_output.py) writes it from the six tables using the rules below.

How to use this file. If a word or a code puzzles you, look it up in section 2. If you want to know what a column holds, or what an empty cell means, see section 3. If you want to know why a cell has its value, find the rule in section 4, then open the page named in that row's where_to_check column and read it. Section 5 explains the priority list and how it is ranked, section 6 defines Kevin's two lists and how they are read per welfare state, and section 7 says what happens when the rules cannot decide.

How this file changes. A rule changes only through a dated entry in [decision_log.md](decision_log.md) and a new row in the change log at the end of this file. A rewording keeps the meaning unless the decision log entry says the meaning changes. Older entries in the decision log use the file and column names of their day; its entry of 2 October 2026 on the reorganisation gives the old and new names.

## 2. Words used here

### Sources and the bodies behind them

| Word | Meaning |
|---|---|
| EFSA | The European Food Safety Authority. Its 2023 scientific opinion on the welfare of dairy cows (EFSA Journal 21(5):7993) is one of the two sources of indicators. |
| Welfare consequence | EFSA's name for a kind of welfare problem, such as Locomotory disorders or Mastitis. The EFSA indicators here belong to five of them. EFSA assessed these five because the European Commission's mandate asked for them: "Assessment 2 addresses five welfare consequences as requested in the mandate" (abstract, PDF page 1). It does not rank them by severity, prevalence or duration (section 5). |
| ABM | Animal based measure: a measure taken on the animal itself, such as how it walks, rather than on its housing or on how the farm is run. EFSA's "ABM assessment tables" list these measures and rate each one. |
| Sensitivity | One of the three things EFSA rates for each measure. In plain words: does the measure catch the animals that have the welfare problem? EFSA rates individual cow somatic cell count (I058) low on sensitivity "because acute cases of mastitis that occur between sampling time points may be missed" (Table 27, PDF page 44). |
| Specificity | The second thing EFSA rates. In plain words: does the measure avoid flagging animals that do not have the problem? For claw lesions (I003) EFSA writes that "not all lesions result in clinical lameness which reduces specificity" (Table 17, PDF page 33). |
| Feasibility | The third thing EFSA rates. In plain words: how practical is it to take the measure on a farm? EFSA rates gait assessment (I001) high on feasibility, calling it "a practical way to assess lameness during on-farm inspection" (Table 16, PDF page 32). |
| Welfare Quality | The Welfare Quality assessment protocol for dairy cattle, version 3.2, February 2024: the second source of indicators. It is built in layers. Four principles (Good feeding, Good housing, Good health, Appropriate behaviour) are split into criteria, and each criterion is assessed by one or more measures. |
| Resource based, management based | Welfare Quality's labels for a measure of the housing or equipment (resource based) or of a farm practice (management based), as opposed to a measure taken on the animal. |
| Stygar 2021 | Stygar et al. 2021, Frontiers in Veterinary Science 8:634338, a review of sensor technologies for dairy cow welfare. They found 129 technologies on the market, of which 18 had been externally validated. |
| Stygar list, appendix | The spreadsheet that comes with Stygar 2021 ([stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), sheet "Appendix table 1"). It lists the 129 products with their name, provider, web link, sensor type, AIM, country and a column on validation studies. "The appendix" and "the Stygar list" mean the same thing. |
| AIM | The column of the Stygar list that holds a one line description of what each product does, as stated for that product. It is the only column searched when counting vendors. |
| Stygar Table 1, Table 2 | Table 1 (page 6) summarises the externally validated technologies and puts each study under independent validation or self validation. Table 2 (page 7) gives the results of the validation trials by measured trait, says whether each trial took place on a research farm or a commercial farm, and places each technology in a high performance or a lower performance column. |
| Study number | The number Stygar give a study in their reference list, for example 48. The tables call it a study number; older notes call it a reference number or ref. |
| Validated | In this repository the word has one narrow meaning: Stygar code at least one external validation study for that product on that trait. It never means more than that here. The one exception is the icar_validated column of products.csv, which means the product is on ICAR's list. |
| Linstädt 2024 | Linstädt, Thöne-Reineke and Merle 2024, Frontiers in Veterinary Science 11:1429097, a systematic review of animal based welfare indicators for dairy cows, covering studies from 2011 to 2021. It summarises studies one by one and gives no grade per indicator. It is one of the three sources of column 1 for the sensor side rows (rule 4.14). |
| Maroto Molina 2020 | Maroto Molina et al. 2020, Journal of Dairy Research 87(S1). They go through the Welfare Quality measures and say which sensor technologies could provide each one. They give no rating of their own, so the rating column here is this project's coding of their text. |
| Substitute measure | Something Maroto Molina propose measuring in place of the protocol's own measure, for example water intake in place of the water point measures. |
| PLF | Precision livestock farming: sensors, cameras and data analysis used on farms. |
| Sensor side | The rows that come from what sensor products say they measure, not from a welfare protocol: one row per kind of parameter that a product in the Stygar list names and that no protocol row covers (rule 4.12). They are coded listed_by plf_only. The protocol side is the 58 rows from EFSA and Welfare Quality. |
| Welfare state | The state or problem a row measures, read from EFSA's table headings or the Welfare Quality criterion (rule 4.13). Several rows can test one state, such as the three EFSA tests for subclinical ketosis. |
| FARM v5 | FARM Animal Care Version 5, the US dairy industry's own animal care programme, written by the National Milk Producers Federation. It is one of the four schemes. Until 5 November 2026 it was also read for a separate industry naming factor, so the score counted it twice; how FARM names each indicator is still recorded (rule 4.6), but it no longer ranks anything. |
| The four schemes | RSPCA Assured dairy cattle standards, April 2026 (UK); FARM v5 (US); Global Animal Partnership dairy standard version 2.0 (US), called GAP; Certified Humane dairy standards, Edition 23 (US). In the tables they are coded RSPCA_Assured, FARM_v5, GAP_dairy and Certified_Humane. |
| ICAR | The International Committee for Animal Recording. It keeps a list of validated sensor systems; the copy used here was saved on 16 September 2026. The three products in products.csv that are not in the Stygar list (P018 to P020) come from that list, and all three measure milk. P018, the Ekomilk Horizon Unlimited analyser, measures somatic cell count, which is indicators I057 and I058, and milk composition. P019, the Brolis BLH01 in line sensor, measures milk fat and protein, which EFSA uses for I021 and I025. P020, the Panazoo MMI sensor, measures milk yield. The Ekomilk report found that its somatic cell count met ICAR's accuracy limit only between 0 and 500,000 cells per ml, not over the full range. |

### Words for equipment

| Word | Meaning |
|---|---|
| Accelerometer | A small motion sensor, worn on a collar, ear tag or leg tag, that records movement such as steps or lying. |
| Bolus | A sensor placed in the cow's rumen or reticulum, parts of its stomach, where it stays and reports, for example, temperature or pH. It is usually swallowed. EFSA's rumen pH measure (I027, Table 46, PDF page 76) describes a bolus inserted into the reticulum through a rumen cannula, a surgically made opening into the rumen. A reticular bolus is one of these. |
| RFID | Radio tags that identify each cow automatically, for example at a water trough fitted with a flowmeter. |
| Inline analyser | A sensor fitted at the milking point that measures the milk as it passes, such as a spectrometer or a cell count sensor. |

### Codes in the tables

Each coded column takes only the values below. [check_tables.py](../3_code/check_tables.py) refuses any other value.

**sensor_evidence** (sensor_coverage.csv): can a product on the market measure the indicator? The full rule is [rule 4.2](#42-sensor-evidence-column-a).

| Value | Meaning | Label in the Excel file |
|---|---|---|
| validated_commercial | A product in the Stygar list measures the indicator, and Stygar code at least one external validation study for that product on that trait. | Tested |
| commercial_unvalidated | A product in the Stygar list states the indicator in its AIM, and no external study is coded. | Claimed |
| research_demonstrated | No product states the measure, and the sensor sources say a study they cite measured this indicator's own measure in cattle. | Shown in research |
| theoretically_measurable | No product states the measure, and the sources only propose a technology, report it shown only in another species or setting, or offer only a substitute measure. | Proposed only |
| none | No product, and Maroto Molina say sensors cannot provide it or do not discuss it: nothing in the two sources, as of their dates (2020 and 2021). | Nothing found |
| unsure | The sources do not settle it. See section 7. | Unclear |

**device_needed** (sensor_coverage.csv): the cheapest kind of equipment that would measure it, a stand in for cost and ease. The full rule is [rule 4.4](#44-device-needed).

| Value | Meaning |
|---|---|
| routine_data | Nothing extra: the value is already collected by the milking system or in herd or farm records. |
| farm_fixed | One device per farm or barn, such as a camera, a walkover scale or a trough meter. |
| animal_mounted | One device per animal, such as a collar, ear tag, leg tag or bolus. |
| sample_or_procedure | A blood or rumen sample, or a scoring done by a person, when the method cited for the row is of that kind. |
| none | No technology is named for the row by Stygar or Maroto Molina. |
| unsure | The rules do not settle it. See section 7. |

**measure_type** (indicators.csv): what kind of thing the indicator measures, in the source's own terms. Every EFSA measure here is animal based, because the EFSA rows come from its ABM tables. For Welfare Quality the label is read from the Scope line of each measure. For a sensor side row it follows from what the row records: the animal, the housing or equipment (I080, feed availability at the feed fence), or a practice of the farm (I067, animal identification, and I082, milk fed to each calf).

| Value | Meaning |
|---|---|
| animal_based | Observed or recorded on the animal. |
| resource_based | About the housing or equipment. |
| management_based | About how the farm is run. |
| none | No measure is defined. Only thermal comfort, I039, has this value. |

**maroto_molina_rating** (indicators.csv, copied into sensor_coverage.csv): this project's coding of what Maroto Molina say about the measure. The full rule is [rule 4.3](#43-maroto-molina-rating).

| Value | Meaning |
|---|---|
| yes | They identify commercially available technology: the passage says the technology is commercially available or in use on commercial farms. |
| partial | They name research level technology, technology that needs adaptation, or a substitute measure they propose. |
| no | They say sensors cannot provide it. |
| not_covered | The paper does not discuss the measure, or discusses it but names no technology for it. |

**listed_by** (indicators.csv): which of the two indicator sources lists the indicator, or plf_only for a sensor side row.

| Value | Meaning |
|---|---|
| joined | EFSA and Welfare Quality share the row. |
| efsa_only | Only EFSA lists it. |
| wq_only | Only Welfare Quality lists it. |
| plf_only | No protocol lists it: a sensor side row, a parameter that products in the Stygar list say they measure (rule 4.12). |

**welfare_relevance** (indicators.csv): column 1, whether the welfare sources treat the row as a measure of welfare. The full rule is [rule 4.14](#414-welfare-relevance-column-1). Since 5 November 2026 it is the gate of the priority list (section 5): rows graded no_welfare_validation or not_welfare_relevant leave the list.

| Value | Meaning | Label in the Excel file |
|---|---|---|
| established | A protocol row whose measure is animal based: EFSA's ABM tables or the Welfare Quality protocol list it as a measure taken on the animal. | Established |
| established_input | A protocol row whose measure is resource based or management based, or a criterion with no measure (thermal comfort): Welfare Quality lists it, but it describes the farm rather than the animal. | Established input |
| supported | A sensor side row that EFSA 2023, Welfare Quality or Linstädt 2024 links to a welfare problem, condition or state, with no passage in them questioning the link. | Supported |
| indirect_or_contested | A sensor side row for which one of those three sources says the link to welfare is indirect, insufficient on its own, weak, inconsistent, unclear or not fully understood. | Indirect or contested |
| no_welfare_validation | A sensor side row that none of the three sources links to welfare, but that a product's own description says is for health, welfare or a named disease or condition, or that is itself a health, welfare or condition status, or that a scheme requires. | No welfare validation |
| not_welfare_relevant | A sensor side row that no product's description, no scheme requirement and none of the three sources ties to health or welfare. | Not framed as welfare |
| unsure | The rules do not settle it. See section 7. | Unclear |

**efsa_sensitivity, efsa_specificity, efsa_feasibility** (indicators.csv): the level word EFSA's own ABM table uses for the measure. The full rule is [rule 4.9](#49-efsas-own-ratings). In the Excel file sensitivity and specificity show together as a validity flag, and feasibility shows read the other way, as manual burden (rule 4.9). The level words show as High, Medium, Low, "Mixed (EFSA gives two levels)" and "Not stated by EFSA".

| Value | Meaning |
|---|---|
| high | EFSA writes high. |
| medium | EFSA writes medium. The word is kept as EFSA writes it. |
| low | EFSA writes low. |
| mixed | EFSA gives two levels for the same property. Self grooming (I017) and brush use (I018) have specificity mixed: EFSA calls it low, but high in cows with healthy integument. |
| not_stated | EFSA gives no level word. Claw lesions (I003) have specificity not_stated, because EFSA says only that it is dependent on the lesion type. |

**requirement_status** (crosswalk.csv): does the scheme require the indicator? The full rule is [rule 4.8](#48-when-a-scheme-requirement-names-an-indicator).

| Value | Meaning | Label in the Excel file |
|---|---|---|
| required | A numbered requirement names the measure under rule 4.8 and applies to every certified farm. Only this value counts toward the schemes requiring an indicator. | Required |
| unsure | A candidate requirement exists, but the rules do not settle whether it names the measure. It does not count as required. It needs a line in open_questions.md naming the indicator and the scheme (section 7). | Unclear |
| not_required | No requirement names the measure. | Not required |

**how_checked** (crosswalk.csv): how a scheme checks a requirement it sets. The full rule is [rule 4.7](#47-schemes-requiring-it).

| Value | Meaning |
|---|---|
| visual_inspection | An assessor observes the animals or scores them or, for a resource based measure, observes the resource or equipment. |
| records_review | The assessor checks farm records. |
| sensor_accepted | The scheme text accepts sensor or automated data for the measure. |
| unspecified | The scheme requires it but does not say how it is checked. |
| unsure | The scheme requires it, but its text truly leaves the method open between two methods. It is never used because naming is unsettled; that is what requirement_status unsure is for. It needs a line in open_questions.md (section 7). |

**farm_naming** (crosswalk.csv, FARM v5 rows only): does the industry programme name the indicator? The full rule is [rule 4.6](#46-named-by-farm-a-record). It ranks nothing since 5 November 2026. It follows requirement_status: a required row is named or named_with_threshold, an unsure row is unsure, and a not_required row is related_resource or not_named.

| Value | Meaning |
|---|---|
| named_with_threshold | A FARM requirement names the measure and sets a number. |
| named | A FARM requirement names the measure, with no number. |
| related_resource | A FARM requirement about housing, equipment or practice bears on the indicator but does not name the measure. |
| not_named | FARM does not name it. |
| unsure | The rules do not settle whether FARM names it. It needs a line in open_questions.md (section 7). |

**stygar_performance** (sensor_coverage.csv): how well the tested products did in Stygar 2021, for a row whose 2021 grade is validated_commercial. The full rule is [rule 4.15](#415-validity-of-the-best-test).

| Value | Meaning |
|---|---|
| above_threshold | Stygar's Table 2 puts at least one trial of a tested product on the row's trait in its high performance column. |
| below_threshold | Every such trial is in the lower performance column. |
| not_tested | The 2021 grade is not validated_commercial. |

**since_2021_performance** (sensor_coverage.csv): how well the tested product did in the counted test since 2021, for a row whose grade since 2021 is validated_commercial, under Stygar's full test. The full rule is [rule 4.15](#415-validity-of-the-best-test).

| Value | Meaning |
|---|---|
| above_threshold | Every statistic of a kind Stygar's test covers that the study reports for the product, in every setting, meets the test; where several counted tests bear on the row, at least one product passes in full. |
| below_threshold | No product passes in full, and every counted test can be graded. |
| not_graded | The study reports no statistic of a kind the test covers (for example only bias, an error in the units of the measure or a share of animals identified), the full results are not on disk and every value that is on disk meets the test, or a report's regression does not name its axes. |
| not_tested | The grade since 2021 is not validated_commercial. |

**Validity of the best test** (Excel file only): computed by build_output.py from the stronger of the two grades and the two performance columns ([rule 4.15](#415-validity-of-the-best-test)). It is the first key of the priority list (section 5).

| Label in the Excel file | When |
|---|---|
| Tested: above Stygar's high performance bar | One of the two performance columns is above_threshold. |
| Tested: the results on disk cannot be graded against Stygar's full test | Neither is above_threshold, and one is not_graded. |
| Tested: below Stygar's high performance bar | Every graded result is below_threshold. |
| Claimed | The stronger grade is commercial_unvalidated. |
| Shown in research | The stronger grade is research_demonstrated. |
| Proposed only | The stronger grade is theoretically_measurable. |
| Nothing found | The stronger grade is none. |
| Unclear | The stronger grade is unsure. |

**signal_purpose** (sensor_coverage.csv): what the products that measure the row say the measurement is for. The full rule is [rule 4.16](#416-what-products-do-with-the-signal).

| Value | Meaning | Label in the Excel file |
|---|---|---|
| health_or_welfare | At least one product's description says the measurement is for health, welfare or wellbeing or for a named disease or condition, or the measurement is itself a health, welfare or condition status. | Used for health or welfare |
| production_only | No description gives it a health purpose, and at least one gives it a production, fertility, feeding or herd management purpose. | Used only for production, fertility or herd management |
| not_stated | Products name it but none says what it is for. | No purpose stated |
| unclear | A description the answer turns on can be read either way, or whether any product measures the row is itself open. It needs a line in open_questions.md (section 7). | Unclear |
| no_product | No product in the Stygar list names it, and no product since 2021 measures it. | No product in the Stygar list measures it |

**Kind of ask** (Excel file only): the kind of request a welfare state on the priority list supports, after the three worlds of the Claude summary Kevin forwarded (section 5).

| Label in the Excel file (shortened) | When |
|---|---|
| A: ask schemes to accept the sensor data | A row of the state is Tested or Claimed, and a scheme requires a row of the state. |
| Unclear: a sensor exists, and a scheme may require the state (a scheme row is unsure) | A row is Tested or Claimed, no scheme requires any row, and a scheme row of the state is unsure. |
| A: ask schemes to adopt the sensor data | A row is Tested or Claimed, no scheme requires any row or may require one, and a Tested or Claimed row is used for health or welfare. |
| C: ask for welfare alerts or thresholds on that signal | A row is Tested or Claimed, no scheme requires any row or may require one, and no Tested or Claimed row is used for health or welfare or unclear on it. |
| B: ask for new measurement | No row is Tested or Claimed, and none is unsure on sensor evidence. |
| Unclear: the sensor evidence is unsure | No row is Tested or Claimed, and a row is unsure on sensor evidence. |
| Unclear: what products do with the signal is unsure | As for C, except that a Tested or Claimed row is unclear on signal purpose. |

**validation_found** (products.csv): what Stygar found about validation of the product.

| Value | Meaning |
|---|---|
| none | In the Stygar list, with no external validation study. |
| external_self | Every study Stygar cite for it had a developer or company author. |
| external_independent | At least one study Stygar cite for it had no developer or company author. |
| not_listed | Not in the Stygar list. |

**sensor_type** (products.csv): the main sensing hardware. The values are collar_accelerometer, ear_tag, bolus, camera, milking_system and other. Other covers leg tags, the collar or leg CowScout, the load cell plate, milk analysers and the milk yield sensor.

**in_stygar_list** and **icar_validated** (products.csv): yes or no. In the Stygar list of 129; on the ICAR list of validated sensor systems.

### Other words

| Word | Meaning |
|---|---|
| Search words | The words written into each sensor_coverage.csv row and searched for in the AIM column of the Stygar list. They are fragments of text, matched anywhere in the description, with upper and lower case treated the same, so "injur" finds both injury and injuries. |
| Vendors naming it | How many of the 129 products in the Stygar list have an AIM that contains at least one of the row's search words. A count of claims, not of proof. |
| Named, validated (Sensors x products sheet) | In the Excel sheet that sets every indicator against every product, "named" means the product's description contains one of the row's search words, untested; "validated" means Stygar code a validation study for that product on that measure. |
| Unsure | The code for a cell the written rules do not settle. It is never a guess. See section 7. |
| Not yet checked | Shown in the Excel file for an indicator that has no row yet in sensor_coverage.csv, or no row yet for a scheme in crosswalk.csv. |
| Not yet known | Shown in the Excel file for Kevin's lists while not all four schemes have been read for an indicator and none read so far settles the answer: on list 1 for rows graded Tested or Claimed that no scheme read so far requires, on list 2 for rows that no scheme read so far requires and checks by hand, unless a requiring scheme's how_checked is unsure or a scheme row is unsure (those show Unclear). See section 6. Since 8 October 2026 all four schemes are read for every indicator, so no row shows it. |
| Unclear | Shown in the Excel file for a cell coded unsure, for a scheme row whose requirement_status is unsure, and on Kevin's lists where an unsure cell decides the answer (section 6). |
| Priority list | The welfare states, ranked by the ordered keys of section 5, after rows the welfare sources do not back have left. It is a sort order, not a welfare judgement. It replaced the ease of adoption score, a sum from 0 to 15, on 5 November 2026. |
| Rank | A welfare state's place on the priority list. Every row of a state that passes the gate shows its state's rank. |
| Gate | Column 1 used as a filter: a row graded no_welfare_validation or not_welfare_relevant leaves the priority list (section 5). |
| World A, B, C | The three kinds of ask in the Claude summary Kevin forwarded with his review of November 2026: A, the measure exists and is used, so ask schemes to accept the sensor data; B, no sensor, so ask for new measurement; C, the signal is on farms but nothing is built around it for welfare, so ask for software, alerts or welfare thresholds. Section 5 says how each state's is read. |
| Validity flag | EFSA's sensitivity and specificity, shown beside a row. It does not change the rank. A row EFSA does not rate shows Not rated, with no penalty (rule 4.9). |
| Manual burden | EFSA's feasibility read the other way: a measure EFSA rates low on feasibility on farm is a high burden to take by hand, which is the work a sensor would take away (rule 4.9). |
| BCS | Body condition score, a score of how much fat a cow carries (EFSA PDF page 76, Stygar page 4, Maroto Molina page 2). It is also part of product names such as DeLaval BCS. |
| BHB | Beta hydroxybutyrate (EFSA's list of abbreviations, PDF page 123). EFSA treats an elevated level as a sign of subclinical ketosis (PDF page 74). |
| CMT | California mastitis test. Stygar Table 2, page 7, lists the Lely on line California mastitis test (study 43) under mastitis detection. |
| DHIA | Dairy Herd Improvement Association, whose milk fat, protein and lactose observations Stygar reference 25 compares with a real time milk analyser (title on PDF page 13). |
| LDH | A level analysed in milk, named with progesterone and BHB in the aim of Herd Navigator in the Stygar list. No document in 1_sources spells it out. |
| NIRS | Near infrared spectroscopy. Maroto Molina, page 3, say milk somatic cell count can be monitored by it, even for the individual cow in milking robots. |
| SARA | Subacute ruminal acidosis, one of the metabolic disorders in EFSA Table 46 (PDF pages 75 and 76). |
| SCC | Somatic cell count, the number of cells per ml of milk; an elevated count is a sign of an inflammatory response such as mastitis (EFSA PDF page 42). Bulk milk SCC, also written bulk tank SCC, is the count for the milk in the farm's bulk tank (EFSA Table 27, PDF page 43). |

## 3. What each table holds

Six tables, each a CSV file (a plain spreadsheet file) with fixed column names in a fixed order. [check_tables.py](../3_code/check_tables.py) checks the columns, the codes and the links between tables after every edit. It checks that the tables are well formed and agree with each other; it does not check that a value is true. That is the job of the auditor and of a person reading the source page.

### indicators.csv: the welfare indicators (the rows, and column 1)

One row per indicator. There are 81 rows: the 58 protocol rows, carried over when this repository was set up on 25 September 2026 (decision_log.md, first entry) and corrected since, and 23 sensor side rows added on 17 October 2026. The rule for which protocol indicators belong is [rule 4.1](#41-which-indicators-are-in-the-table), and for the sensor side rows [rule 4.12](#412-the-sensor-side-rows).

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | The identifier, I001 onwards, used by the other tables. A removed row's number is not reused, so I042 is missing. | Never. |
| efsa_welfare_consequence | The EFSA welfare consequence. | On a Welfare Quality only row. |
| efsa_measure | The EFSA animal based measure. | On a Welfare Quality only row and a sensor side row. |
| wq_principle, wq_criterion | The Welfare Quality principle and criterion. | On an EFSA only row and a sensor side row. |
| wq_measure | The Welfare Quality measure. | On an EFSA only row, on a sensor side row, and on thermal comfort (I039), the one row where Welfare Quality defines no measure. |
| measure_type | animal_based, resource_based, management_based or none (section 2). | Never. |
| maroto_molina_technology | What Maroto Molina 2020 identify for the measure, in words. | Never; where they do not discuss it, the cell says so. |
| maroto_molina_rating | yes, partial, no or not_covered ([rule 4.3](#43-maroto-molina-rating)). | Never. |
| notes | The source table, the basis for joining an EFSA and a Welfare Quality measure, and open questions. | May be empty when there is nothing to add. |
| listed_by | joined, efsa_only, wq_only or plf_only. check_tables.py confirms it follows from which source columns are filled. | Never. |
| efsa_sensitivity | EFSA's level word for sensitivity: high, medium, low, mixed or not_stated ([rule 4.9](#49-efsas-own-ratings)). | On a Welfare Quality only row or a sensor side row, which EFSA does not rate. Filled on all 32 rows that come from EFSA. check_tables.py confirms both. |
| efsa_specificity | EFSA's level word for specificity, with the same values. | As for efsa_sensitivity. |
| efsa_feasibility | EFSA's level word for feasibility on farm, with the same values. | As for efsa_sensitivity. |
| efsa_ratings_quoted | EFSA's table and PDF page, and the passages the three ratings are read from, quoted. | As for efsa_sensitivity. |
| plf_parameter | The name of the parameter on a sensor side row, for example Rumination ([rule 4.12](#412-the-sensor-side-rows)). | On every protocol row. |
| welfare_state | The welfare state the row measures ([rule 4.13](#413-welfare-state)). | Never. |
| welfare_relevance | Column 1, the welfare relevance grade ([rule 4.14](#414-welfare-relevance-column-1)). check_tables.py confirms that a protocol row is established or established_input according to its measure_type. | Never. |
| welfare_relevance_evidence | What the grade rests on: the protocol table or page for a protocol row; for a sensor side row, the passages from the three sources, quoted with page, and, where none links it, the product descriptions that frame it. | Never. |

### products.csv: the profiled sensor products

One row per product. There are 20: 17 in the Stygar list, which carry Stygar's validation finding, and 3 from the ICAR list (P018 to P020), which are not in the Stygar list. The 17 came with the table when this repository was set up on 25 September 2026 (decision_log.md, first entry), and nothing here records how they were first picked; later corrections are recorded in the decision log. They are not a sample, and no grade or count depends on them: every grade and every count of products reads the full Stygar list of 129 directly from the spreadsheet. The Product list sheet of the Excel file marks which of the 129 are in products.csv.

| Column | What it holds | When empty |
|---|---|---|
| product_id | The identifier, P001 onwards, used in the products column of sensor_coverage.csv. | Never. |
| vendor | The company as it trades today. For P003, P010 and P017 it is the provider named in the Stygar list, because no source in 1_sources states the ownership those rows used to carry (decision log, 2 October 2026). | Never. |
| product | The product as the vendor names it. | Never. |
| appendix_name | The product's exact name in the Stygar list. | When the product is not in the Stygar list. |
| sensor_type | The main sensing hardware (section 2). | Never. |
| vendor_description | The stated aim, copied from the AIM column for products in the Stygar list. | Never. |
| country | The country. | When the source gives none (P019, P020). |
| in_stygar_list | yes or no. | Never. |
| validation_found | none, external_self, external_independent or not_listed (section 2). | Never. |
| icar_validated | yes or no. | Never. |
| link | The web link from Stygar 2021, as they printed it. What it opens today, and the product's current page, are in product_links.csv. | When the product is not in the Stygar list. |
| notes | Where the row comes from, and the study numbers behind the validation value. | Never. |

### sensor_coverage.csv: what sensors measure (column (a))

One row per indicator. Since 17 October 2026 there are 81 rows, one for each indicator. An indicator with no row here would not yet have been checked for sensors, and the Excel file would show it as not yet checked.

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | An id from indicators.csv. | Never. |
| sensor_evidence | The 2021 grade of column (a) ([rule 4.2](#42-sensor-evidence-column-a)). | Never. |
| products | Every product the row cites, separated by spaces. A product in products.csv is cited by its P number; a product in the Stygar list but not in products.csv is cited as appendix:Provider\|Name, for example appendix:Afimilk\|AfiLab. | When the row cites no product. It must be filled for the two commercial grades. |
| validated_products | Only the products with a validation study coded by Stygar for the row's trait, as Provider\|Name from the Stygar list, separated by semicolons. | On every row that is not validated_commercial. It must be filled on validated_commercial rows. |
| validated_trait | The Stygar Table 2 trait, or the AIM wording, that matched. | When nothing matched. |
| study_numbers | The validation studies, by Stygar's study number, separated by spaces. | When no study applies. It must be filled on validated_commercial rows. |
| maroto_molina_rating | Copied from indicators.csv for the same row. check_tables.py confirms the copy. | Never. |
| device_needed | The class of device ([rule 4.4](#44-device-needed)). | Never. |
| vendors_naming_it | A whole number ([rule 4.5](#45-vendors-naming-it)). check_tables.py confirms it equals a fresh count. | Never. |
| search_words | The search words, separated by semicolons. | Never. |
| where_to_check | Where each value was read: document, page, table, row. | Never. |
| reasoning | Alternatives, the other technologies, and the candidate readings on unsure rows. | May be empty when there is nothing to add. |
| since_2021_grade | The grade for evidence since 2021 ([rule 4.11](#411-evidence-since-2021-a-second-sensor-column)), using the codes of rule 4.2. | Never. |
| since_2021_evidence | The keys of the evidence in evidence_since_2021.csv behind that grade, separated by semicolons. | When nothing since 2021 was found, or when the grade rests only on a review's proposal named in since_2021_reasoning. |
| since_2021_reasoning | Which evidence decides the grade since 2021, and why. | Never. |
| stygar_performance | above_threshold, below_threshold or not_tested ([rule 4.15](#415-validity-of-the-best-test)). | Never. check_tables.py confirms it is not_tested exactly when sensor_evidence is not validated_commercial. |
| since_2021_performance | above_threshold, below_threshold, not_graded or not_tested ([rule 4.15](#415-validity-of-the-best-test)). | Never. check_tables.py confirms it is not_tested exactly when since_2021_grade is not validated_commercial. |
| since_2021_performance_reasoning | The studies, the statistics and their values, set against Stygar's full test. | Exactly when since_2021_performance is not_tested. |
| signal_purpose | health_or_welfare, production_only, not_stated, unclear or no_product ([rule 4.16](#416-what-products-do-with-the-signal)). | Never. check_tables.py confirms it is no_product exactly when no product in the Stygar list names the row and the grade since 2021 is not commercial, and that an unclear value has an open line in open_questions.md. |
| signal_purpose_evidence | The product descriptions the value is read from, quoted. | Never. |

### evidence_since_2021.csv: the studies and maker pages since 2021

One row per study or maker page that a grade since 2021 rests on, with its quality record ([rule 4.11](#411-evidence-since-2021-a-second-sensor-column)).

| Column | What it holds | When empty |
|---|---|---|
| evidence_key | A short key, first author and year for a study, Maker: and the snapshot name for a maker page. | Never. |
| kind | study, review or maker_page. | Never. |
| citation, doi_or_url, year | The study as published, or the maker and product. | Never. |
| found_via | The source read in this pass through which it was found, with table or section. | Never. |
| indicator_ids | The indicators it bears on, separated by semicolons. | Never. |
| product, on_sale | The product as the source names it, and yes, no or not_stated as a source says. | product when no product was used. |
| technology, setting, n_animals | The device, where it was done (laboratory, research_farm, commercial_farm, mixed, not_stated, or not_applicable for a maker page) and how many animals. | technology and n_animals when not given. |
| authors_independent, maker_involvement | yes, no or not_stated as the paper says (not_applicable for a maker page), and what the maker did (authorship, funding, approval of the manuscript, data). | maker_involvement when nothing is stated. |
| measure, reference_method, statistic | What was measured, against what, and the result as reported. | reference_method and statistic when there was none. |
| sections_read, source_file | What was read, and the file in 1_sources that holds it. | Never. |
| notes | Anything a reader checking the row needs. | May be empty. |

### crosswalk.csv: what schemes require (column (c))

One row per indicator per scheme. An indicator that no scheme requires still gets four rows, by rule. check_tables.py does not check that every indicator has all four rows, so the person filling the table checks that the row count is four times the number of indicators. build_output.py counts an indicator's schemes as read in full only when all four of its rows are present; a single required row already settles list 1 as No, and a required row checked by hand already settles list 2 as Yes. Since 8 October 2026 the table has had four rows for each of the 58 protocol indicators, and since 17 October 2026 four for each of the 23 sensor side rows, 324 in all: the four schemes were read in full against every indicator under rules 4.7 and 4.8.

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | An id from indicators.csv. | Never. |
| scheme | RSPCA_Assured, FARM_v5, GAP_dairy or Certified_Humane. | Never. |
| requirement_status | required, unsure or not_required ([rule 4.8](#48-when-a-scheme-requirement-names-an-indicator), section 2). | Never. |
| requirement_quote | On a required row, the requirement that names the indicator, quoted exactly. On an unsure row, the candidate requirement, quoted exactly. | On a not_required row. |
| section, page | Where the quoted requirement is in the scheme document. The page is written "PDF n (printed m)". | On a not_required row. Both must be filled on a required or unsure row. |
| number_in_requirement | Any number or frequency the requirement sets, exactly as written. | When the requirement sets none, and on every not_required row. It must be filled when farm_naming is named_with_threshold. |
| how_checked | How the scheme checks it ([rule 4.7](#47-schemes-requiring-it)). | On a not_required row. On an unsure row, when the scheme's text does not settle how the candidate would be checked. Never on a required row. |
| farm_naming | How FARM names the indicator, kept as a record ([rule 4.6](#46-named-by-farm-a-record)). | On every row that is not FARM_v5. It must be filled on every FARM_v5 row. |
| reasoning | On a required row, the other requirements that name the measure and the related ones. On an unsure row, the candidate readings and the rule that failed. On a not_required row, what was searched and the related requirements, with section and page. | Never. |

check_tables.py checks these links: a required or unsure row quotes a requirement with its section and page; a required row has how_checked; a not_required row has no quote, section, page, number or how_checked; an unsure row has a line in open_questions.md naming the indicator and the scheme; and a FARM_v5 row's farm_naming follows its requirement_status as section 2 says.

### product_links.csv: the product links today

One row for each of the 129 products in the Stygar list, in spreadsheet order. It records whether the link the Stygar team printed in 2021 still works, and where the product's page is today ([rule 4.10](#410-product-links-today)). It changes no grade, count or rank.

| Column | What it holds | When empty |
|---|---|---|
| appendix_row | The product's row in sheet 1 of the Stygar spreadsheet. | Never. |
| vendor, product, link_2021 | The provider, the name and the link, copied exactly from the Stygar spreadsheet. | Never. |
| link_2021_today | works, moved, wrong_page or broken (rule 4.10). | Never. |
| current_link | The page found today (rule 4.10). | When current_link_shows is none_found. |
| current_link_shows | product_page, related_page, product_not_listed or none_found (rule 4.10). | Never. |
| page_says | Words on the current page that name the product, copied exactly as the page has them. | When the page does not name the product. |
| checked | The date the links were opened, written YYYY-MM-DD. | Never. |
| notes | What changed, what was searched, or, on a related_page row, what the page names instead. | May be empty when there is nothing to add; never on a related_page row. |

## 4. The rules

### 4.1 Which indicators are in the table

**Question.** Which welfare indicators are in scope, and how are the two sources joined?

**Rule.** One row per indicator in [indicators.csv](indicators.csv). An indicator is a measure from the EFSA 2023 dairy cow opinion or the Welfare Quality dairy protocol version 3.2, chosen as follows.

The EFSA rows are every animal based measure in EFSA's ABM assessment tables for the five welfare consequences: Tables 16, 17, 18, 27, 31, 32, 33, 42 and 46, which give feasibility, sensitivity and specificity for each measure. Other EFSA tables are out of scope. These are Table 15 and Table 26, which list measures used in the literature to assess lameness and mastitis; the farm level Tables 51 to 59 of the risk based scheme; and Appendix K, whose Table K.1 lists the measures supplied to the expert elicitation.

The Welfare Quality rows are every measure in the version 3.2 protocol overview (PDF page 22, printed page 21). Most are animal based, and some are resource or management based, as the Scope line of each measure says. Three adjustments are made. The two lameness measures, loose housed and tied, share row I001. The one integument alterations measure is split into I004 and I005 to follow EFSA's hock and knee measures. Thermal comfort, a criterion for which the protocol defines no measure, has its own row, I039.

That gives 32 EFSA rows and 32 Welfare Quality rows, 6 of them joined, so 58 rows in all: 26 efsa_only, 26 wq_only and 6 joined. Each row carries its listed_by value: joined when EFSA and Welfare Quality share the row, efsa_only when only EFSA lists it, wq_only when only Welfare Quality lists it. It is shown so that a reader who takes Welfare Quality alone as the validated set can leave out the 26 efsa_only rows without the table changing. These 58 are the protocol side. Since 17 October 2026 the table also has sensor side rows, coded plf_only, for parameters that sensor products say they measure ([rule 4.12](#412-the-sensor-side-rows)); a reader who wants only the protocol side can leave them out the same way.

**Example.** I001 is joined: EFSA's Gait assessment, under Locomotory disorders, shares the row with Welfare Quality's Lameness. Its notes say that EFSA Table 16 defines the 3 point scale citing Welfare Quality 2009, and that the row merges the two Welfare Quality lameness measures. I039, thermal comfort, is wq_only with measure_type none.

**How to check.** Open the EFSA opinion at the nine tables named above and the Welfare Quality protocol at PDF page 22, and compare their measures with the rows. check_tables.py confirms that each listed_by value follows from which source columns are filled. The current counts are on the Read me sheet of the Excel file.

### 4.2 Sensor evidence (column (a))

**Question.** Does a commercial product measure the indicator, and how well has that been checked?

**Rule.** The value is read from Stygar 2021 (Table 1 on page 6 for the validated products and their study numbers, Table 2 on page 7 for the traits each was validated on, and the Stygar list for the 129 products and their stated aims), from Maroto Molina 2020 for measures with no product, together with Stygar's text (pages 9 to 11) and reference list, and from [products.csv](products.csv). The six grades:

validated_commercial: a product in the Stygar list measures the indicator and Stygar code at least one external validation study for that product on that trait. The row names the products and the study numbers.

commercial_unvalidated: a product in the Stygar list states the indicator in its aim, and no external study is coded. The row names the products.

research_demonstrated: no product in the Stygar list states the measure in its aim, and Maroto Molina 2020 or Stygar 2021 say that a study they cite measured this indicator's own measure in cattle, on a research farm, a commercial farm or in a trial, whatever feasibility rating they give it. Whether the study was in cattle and measured this measure is read from the source's own words, or from the cited reference's title as printed in the source's reference list, and from nothing else. The row names the study as the source cites it and the page. Kevin's change request has a cell for a commercial device used in research to measure an indicator that no product claims (device exists, measurability unclear); such a row is research_demonstrated and its reasoning names the device. On 15 October 2026 no row is of that kind.

theoretically_measurable: no product in the Stygar list states the measure, and the sources only propose a technology for it, or report it shown only in another species or setting (for example pigs, bird flocks, carcasses, human skin or a laboratory assay), or offer only a substitute measure, a different measure used in its place. A study of a substitute measure does not demonstrate the indicator, even in cattle. The row says which of these applies.

The two grades replace research_only, which until 15 October 2026 covered both (decision log, 15 October 2026). They differ in how certain the evidence is. Until 5 November 2026 both scored 1 point; on the priority list Shown in research ranks above Proposed only (rule 4.15, section 5). Where the source's words and the reference title do not settle which applies, the cell is unsure.

none: no product, and Maroto Molina say sensors cannot provide it or do not discuss it. None means nothing in these two sources as of their dates, not nothing anywhere.

unsure: the sources do not settle it. The candidate reading goes in the reasoning column and in [open_questions.md](open_questions.md).

When a validated trait counts. A trait validated by Stygar counts for an indicator only when Stygar's trait name and the indicator name are the same measure, or where Stygar's Table 2 category names the indicator directly, for example locomotion score for lameness. Stygar's trait names are not always word for word the indicator's. For EFSA's lying time, I012, the trait is "Non-active behavior (lying, lying and standing)", and the decision log entry of 29 September records that it maps to lying time. That trait covers lying, and lying and standing together, and Table 2 does not say which trial measured which. The same trait does not settle lying bouts, I013, which stays unsure (section 7). Rumination is not lameness, and activity is not oestrus. A product validated on one trait does not earn a grade on another.

Products and validated products. The products column names every product the row cites, whether or not it stands behind the grade. The validated_products column names only the products with a validation study coded by Stygar for the row's trait.

**Example.** I023, subclinical ketosis by body condition scoring, is validated_commercial. Its product is P009, the DeLaval body condition scoring camera, its study number is 48, and its validated_trait reads "Body condition scoring, Table 2 page 7, commercial farm, lower performance column". The products rule shows on I027, rumen pH by bolus: the row cites five products, but validated_products names only `eCow UK|eBolus`, the one with studies 50 and 51. The same measure rule shows on I030, water provision, which is theoretically_measurable. Maroto Molina propose individual water intake as a substitute, and a product validated for water intake exists (study 45), but the Welfare Quality measure is the water point itself, so the grade does not credit it.

**How to check.** Open [stygar_2021.pdf](../1_sources/stygar_2021.pdf) at Table 1 (page 6) and Table 2 (page 7) and find the study numbers the row gives. Open the Stygar list, find each product, and read its AIM. The row's where_to_check column names every page.

### 4.3 Maroto Molina rating

**Question.** What does Maroto Molina 2020 say about whether sensors can provide the measure?

**Rule.** maroto_molina_rating in indicators.csv, copied into sensor_coverage.csv, codes what Maroto Molina et al. 2020 say about each measure. They give no rating of their own, so the value is this project's coding of their text. yes: they identify commercially available technology. This is read literally: yes only where the passage says the technology is commercially available or in use on commercial farms. A technology named without those words, for example one cited from a research study, is partial. partial: they name research level technology, technology that needs adaptation, or a substitute measure they propose. no: they say sensors cannot provide it. not_covered: the paper does not discuss the measure, or discusses it but names no technology for it. In that case the notes say that they discuss it, and where.

**Example.** Maroto Molina page 3 says mortality, dystocia and downer cows are Welfare Quality measures based on farmer records, and names calving prediction systems for dystocia only. So I049, dystocia, is partial, a substitute. I048, mortality, is not_covered, and its notes say the measure is discussed on page 3 and no technology is named. I051, disbudding or dehorning, is no. The literal reading of yes shows on two rows. I023, body condition, is yes: page 2 says the Welfare Quality scoring is less precise than what "commercially available technologies" can provide, and names the DeLaval BCS camera. I012, lying time, is partial: page 3 says pedometers and accelerometers have been used for monitoring lying behaviour and can provide lying time, citing research studies, but does not say they are commercially available.

**How to check.** Open maroto_molina_2020.pdf (link only, see [1_sources/README.md](../1_sources/README.md)) at the page given in the row's notes or maroto_molina_technology column. check_tables.py confirms that the copy in sensor_coverage.csv matches indicators.csv.

### 4.4 Device needed

**Question.** How cheap and easy would it be to put in place? This is the stand in for implementability and cost.

**Rule.** The class is read from the sensor type that Stygar and Maroto Molina name for the technology that measures the indicator.

routine_data: already collected by the milking system or herd records, with no new device (milk yield, milk conductivity, somatic cell count from records, calving records).

farm_fixed: one device per farm or barn (camera, walkover scale or pressure mat, weather station, microphone, trough flowmeter with RFID).

animal_mounted: one device per animal (collar, ear tag, leg tag, reticular bolus).

sample_or_procedure: a blood or rumen sample, or a scoring done by a person, but only when a technology or method cited for the row is of that kind (rumenocentesis for rumen pH, body condition scored by eye where Maroto Molina name it).

none: no technology named by Stygar or Maroto Molina for the row. This includes measures EFSA scores by a person at inspection; the class follows the sensor sources, not EFSA's scoring method.

Several technologies. Where more than one technology measures the indicator, the class is the cheapest class that has a commercial product, and the reasoning lists the others. Where none has a commercial product, the class is the cheapest among the technologies the sources propose.

Milk analysers. An analyser added at the milking point (an inline spectrometer, viscosity or cell count sensor) is farm_fixed, one installation per parlour. routine_data is kept for what the milking system or the farm records produce with no added sensor.

The records rule. Where the indicator's own definition takes the value from routine milk recording or from farm records, the class is routine_data, because the value exists with no added device. An inline analyser that also measures it is listed in the reasoning as the added device alternative. This records rule applies to unsure rows too, ahead of the unsure fill below, since routine_data is also the cheapest class. So a row can be routine_data, shown as "Nothing extra" in the Excel file, while its sensor evidence is none: I024, I028 and I029 are such rows under this rule. I007, bulk milk somatic cell count, is routine_data through the class list above (somatic cell count from records), not through this rule, because EFSA names records only in its feasibility line. A class list item that names the measure sets the class where a source says the value is already in routine records, even though no sensor source names a technology for the row. That is why the class list applies to I007 and not to I006. The list names somatic cell count from records, and EFSA Table 27 (PDF page 43) rates the feasibility of bulk milk somatic cell count high, with the words "records readily available". Mastitis incidence, I006, is not in the class list, and EFSA calls its records "dependent on availability and accuracy of vet/farm records".

The unsure fill. On a row whose sensor evidence is unsure, the class is filled from the cheapest commercial candidate so the column stays usable, and the reasoning says so.

What commercial means here. Throughout this rule, commercial means a product in the Stygar list whose aim states the measurement, or on an unsure row the candidate measurement: the same test rule 4.2 applies. A product in the Stygar list of the same technology type but with a different aim does not count. Neither does a technology a source describes as in commercial use but which has no row in the Stygar list. The reasoning names both kinds where they exist.

Lower classes are cheaper to adopt. The table shows the class; it does not put a price on anything. On the priority list the device is the second key, in the order routine_data, farm_fixed, animal_mounted, sample_or_procedure, none, unsure (section 5).

**Example.** I020, clinical ketosis, is unsure on sensor evidence but routine_data on device needed. EFSA Table 46 (PDF page 75) defines the measure as the "Incidence rate of clinical ketosis (estimated from veterinary diagnoses, farm records or national databases)", so the records rule applies ahead of the unsure fill. The reasoning names AfiMilk MPC, an inline milk analyser, as the added device alternative. I006, clinical mastitis cases, shows where the records rule stops. EFSA Table 27 (PDF page 43) defines it as the "Incidence rate of clinical mastitis", and names vet or farm records only in its feasibility line, so the definition does not take the value from records. The unsure fill gives the class: the candidates, Lely MQC-C and the other products whose aims name mastitis or udder health, are milk quality sensors and thermal cameras, so I006 is farm_fixed. I039, thermal comfort, shows the meaning of commercial: it is animal_mounted, from the ten products whose aims name temperature: boluses, an ear tag and a collar. The thermal cameras in the Stygar list do not set the class, because their aims name udder health, mastitis, inflammation, fever or lameness, not temperature or thermal comfort.

**How to check.** Read the indicator's definition at the page named in where_to_check. Then read the reasoning column, which names the technologies and their classes, and check each candidate's AIM in the Stygar list.

### 4.5 Vendors naming it

**Question.** How many products on the market say they measure it?

**Rule.** The number of products among the 129 in the Stygar list whose stated aim names the measurement. It is counted by [count_vendors.py](../3_code/count_vendors.py) from the search words in the search_words column of sensor_coverage.csv, matched without regard to case against the AIM column of the Stygar list. The search words for each indicator are written into the row so the count can be reproduced and challenged. The reading: what many vendors already sell is what industry already buys, which is the visible form of Kevin's "won't strongly object" ([his words](../1_sources/kevin_slack_2026-09-25.md)). Since 5 November 2026 the count is shown beside the rank but is not a key of it: in the summary of an exchange with Claude that Kevin forwarded with his review, adding it let vendor count make up for rows with no welfare validation (section 5).

**Example.** I027, rumen pH by bolus, has the search words "rumen ph; ph," and a count of 5: eBolus, ET912 Fofia, Moow Rumen bolus, smaXtec basic and VitalHerd. Two other bolus aims name rumen acidosis monitoring, which is the condition, not the pH measurement, and the search words do not match them.

**How to check.** Open [stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), select column E (AIM), search for each word of the row, and count the products that match at least one word. Or run `python 3_code/count_vendors.py I027`, which lists the matching products and changes nothing. check_tables.py confirms every stored count equals a fresh count.

### 4.6 Named by FARM (a record)

**Question.** Does the industry's own programme name the indicator?

**Rule.** Whether the indicator is named in a requirement of the industry authored programme, FARM Animal Care Version 5 for dairy, written by the National Milk Producers Federation. The values are named_with_threshold (the requirement names the measure and sets a number), named (it names the measure, with no number), related_resource (a requirement about housing, equipment or practice that bears on the indicator but does not name the measure), not_named, and unsure where the rules do not settle it. An unsure cell needs a line in [open_questions.md](open_questions.md), like any unsure cell (section 7). The requirement is quoted with section and page in [crosswalk.csv](crosswalk.csv). Until 5 November 2026 this was the fourth factor of the score. Kevin asked in his review whether FARM was counted twice ("I think FARM is counted twice?"). It was, since FARM is also one of the four schemes of rule 4.7, so it was taken out of the ranking (section 5); the column is kept as a record. Whether a FARM requirement names the indicator is decided by rule 4.8, and farm_naming follows the row's requirement_status: required gives named or named_with_threshold, with the number in number_in_requirement; unsure gives unsure; not_required gives related_resource or not_named.

**Example.** The FARM_v5 row of I001 is the worked example in rule 4.8: FARM Animal Care v5, page 149, "Severe Lameness: 5% or less of the lactating cows observed score 3 on the FARM Locomotion Scorecard." That names lameness with a number, so the row is required and named_with_threshold. The FARM_v5 row of I028, milk fever, is not_required and related_resource: FARM names milk fever only in a treatment protocol standard, which rule 11 in rule 4.8 does not count.

**How to check.** Open the FARM v5 reference manual at the section and page given in the row and read the quoted requirement. Then apply rule 4.8.

### 4.7 Schemes requiring it

**Question.** How many of the four schemes require the indicator, and how does each one check it?

**Rule.** The count of the four schemes that require the indicator, and how each audits it. The schemes are RSPCA Assured dairy cattle April 2026, FARM v5, Global Animal Partnership dairy v2.0 and Certified Humane dairy Edition 23. Each scheme document is read in full against every indicator, and each indicator gets one row per scheme with its requirement_status under rule 4.8. Only a row with requirement_status required counts toward the number of schemes requiring an indicator; an unsure row does not.

how_checked, one per required row, is visual_inspection (an assessor observes the animals or scores them or, for a resource based measure, observes the resource or equipment), records_review (the assessor checks farm records), sensor_accepted (the scheme text accepts sensor or automated data for the measure), unspecified (the scheme requires it but does not say how it is checked), or unsure. how_checked is never unsure merely because naming is unsettled; that is what requirement_status unsure is for. how_checked unsure is kept only for a required row whose method the scheme's text truly leaves open between two methods, and it needs a line in [open_questions.md](open_questions.md), like any unsure cell (section 7). On an unsure row, how_checked is filled if the scheme's text settles how the candidate would be checked, and left empty otherwise. Since 5 November 2026 the count is not a measure of ease: following the summary of an exchange with Claude that Kevin forwarded with his review, whether a scheme requires a row of a welfare state decides the kind of ask the state supports (section 5), and it fills Kevin's two lists (section 6).

**Example.** The worked example in rule 4.8 is the RSPCA_Assured row of I001, standard H 3.5, which requires mobility scoring and has the results recorded, so the assessor checks the recorded scores: records_review. The FARM_v5 row of I031, cleanliness of water points, is visual_inspection on a resource: FARM checks it by "Observing all watering mechanisms for access and cleanliness" (PDF 31), which rule 8 in rule 4.8 counts as visual inspection. The RSPCA_Assured row of I030, water provision, is unspecified: FW 2.4 requires drinking space for at least 10% of a group, and no RSPCA text says how that is checked. On 8 October 2026 no scheme row is coded sensor_accepted and none has how_checked unsure.

**How to check.** Open each scheme document at the section and page given in the row, read the requirement, and see what it says about how it is checked.

### 4.8 When a scheme requirement names an indicator

**Question.** When does a requirement count as requiring the indicator, rather than just touching on it?

**Rule.** The requirement must name the indicator's own measure or a direct synonym. A requirement about housing, resources or practice that would affect the measure does not count as naming it. It is recorded as related_resource in the reasoning column so the reader can see it.

Fourteen reading rules, approved by Manisha Sarkar on 8 October 2026 ([decision_log.md](decision_log.md), entry of 8 October 2026), say when a requirement counts. They apply to every scheme row, settled rows included. Each has one example from [crosswalk.csv](crosswalk.csv).

1. **Status.** Every row has a requirement_status. required: a requirement names the measure under these rules and applies to every certified farm; requirement_quote, section, page and how_checked are filled. unsure: a candidate requirement exists, but these rules do not settle whether it names the measure; the candidate is quoted with section and page, how_checked is filled if the scheme's text settles how it would be checked and left empty otherwise, the reasoning gives the candidate readings and names the rule that failed, and the row has a line in open_questions.md. not_required: no requirement names the measure; requirement_quote, section, page, number_in_requirement and how_checked are empty, and the reasoning says what was searched and names related requirements with section and page. Only required counts toward the number of schemes requiring an indicator. *Example.* The RSPCA_Assured row of I038, cleanliness of lower legs, is unsure. Appendix 4 item 3 scores one area, "the hind quarters to coronary band and udder" (PDF 98, printed 96). Read one way, the span down to the coronary band takes in the lower legs; read the other, the lower legs are not listed. Rule 9 does not say whether a listed span names the parts inside it, so the row has a line in open_questions.md. The same item lists "hind quarters" by name, which is Welfare Quality's own name for the area of I037, so the RSPCA_Assured row of I037 is required.
2. **Only numbered requirements count.** Guidance in boxes, notes, rationale or explanatory text that the scheme marks as not a standard does not count; it is recorded in the reasoning. *Example.* On the RSPCA_Assured row of I015, getting up movement, the rising score protocol sits in the box below E 5.9.1, so it does not count, and the row is not_required.
3. **Appendices, scorecards and protocols.** One counts when a numbered requirement makes it binding. section then names both. *Example.* The RSPCA_Assured row of I036, cleanliness of udders, is required with section "WA 1.1 a); Appendix 4 item 3 (Cleanliness)": WA 1.1 a) (PDF 57, printed 55) makes the Appendix 4 protocol binding, and item 3 has the assessor visually score an area that names the udder.
4. **Every certified farm.** A requirement counts only if it applies to every certified farm. One limited to one housing type, triggered only above a target, placed in an optional module (for example a Grass-Fed section), or, for Global Animal Partnership, applying only at steps above Step 1, does not count; it is recorded in the reasoning. A condition that is only the practice the indicator itself measures does not limit a requirement, because a farm that does not carry out the practice has nothing for the row to measure: FARM's disbudding standard "if performed on-farm" (the FARM_v5 row of I051) and RSPCA's milk feeding standard for calves no longer with their dam (the RSPCA_Assured row of I082) are read as applying to every certified farm (Manisha Sarkar, 17 October 2026). *Example.* The Certified_Humane row of I041, access to an outdoor loafing area or pasture, is not_required. FW 27 a, "Cattle must have continuous access to pasture by the time they are weaned." (PDF 17, printed 8), is in Part 2 D, Grass-Fed Systems, which the heading marks Optional.
5. **A disease or condition named without its form.** It names only the clinical case or incidence row for that condition: ketosis names I020, hypocalcaemia or milk fever names I028, displaced abomasum names I024, mastitis names I006. It never names a subclinical row (for example I029) or a row defined by a test (for example I021, I022, I025, I026, I027, I056). *Example.* RSPCA H 1.5 a) lists hypocalcaemia among the metabolic disorders the VHWP must list (PDF 45, printed 43). So the RSPCA_Assured row of I028, clinical hypocalcaemia, is required, and the row of I029, subclinical hypocalcaemia, is not_required.
6. **Direct synonyms.** A direct synonym names the same measure in the same animals: adult dairy cows unless the indicator says otherwise. Broader wording (for example "problems at calving" for dystocia), other animals (for example "calf scours" for cow diarrhoea) or a different level do not count; they are recorded in the reasoning. A herd level or bulk tank somatic cell count names I007 (bulk milk somatic cell count), not the individual cow rows I057 and I058. *Example.* Certified Humane H 7 c reads "Herd somatic cell counts, individual clinical cases of mastitis, and mastitis tube usage must be monitored and recorded." (PDF 37, printed 28). Its herd count names I007, so that row is required, and it does not name I057 or I058.
7. **Resource and management measures.** The rule covers the indicator's own measure whatever its measure_type. A requirement that names a resource or management measure (water provision, cleanliness of water points, tethering, disbudding, tail docking, outdoor access) names it. *Example.* The RSPCA_Assured row of I030, water provision, is required on FW 2.4: "There must be sufficient drinking space (mm per head) for at least 10% of a group to drink at the same time." (PDF 10, printed 8).
8. **Inspecting a resource.** how_checked visual_inspection covers an assessor observing animals or, for a resource based measure, observing the resource or equipment. *Example.* The FARM_v5 row of I031, cleanliness of water points, is visual_inspection, because FARM's evaluator observes "all watering mechanisms for access and cleanliness" (PDF 31).
9. **Combined scores.** A combined score names each body region or part that its own text lists, including the text of a scorecard. A region shown only in a drawing or figure does not count. *Example.* The Global Animal Partnership swellings score (Appendix VI, PDF 69, printed 59) says in its text "Around the hock and the knee", so the GAP_dairy rows of I004, hock alterations, and I005, knee alterations, are required. The FARM Hygiene Scorecard (PDF 161) shows its areas only in a figure, so the FARM_v5 rows of I036, I037 and I038, the three cleanliness rows, are not_required.
10. **Housing, equipment and space provisions.** A requirement worded as a provision does not name an animal measure, even when it states the animal outcome it is meant to allow (for example "housing allows cows to lie down easily"). It is related, recorded in the reasoning. *Example.* FARM's "Housing allows all age classes to easily stand up, lie down, and have visual contact with other cattle without risk of injury." (PDF 41) is a housing provision, so the FARM_v5 row of I014, duration of the lying down movement, is not_required.
11. **Records of cases.** A requirement names a condition's case or incidence measure when it requires the farm to record, monitor or report cases of that named condition. A treatment protocol alone, or treatment records that name no condition, do not. *Example.* Global Animal Partnership 5.H.4 requires farms to report the "Incidence for each month (new cases) of" milk fever (PDF 37, printed 27), so the GAP_dairy row of I028 is required. FARM names milk fever only in a written treatment protocol (PDF 56), so the FARM_v5 row of I028 is not_required.
12. **Thermal comfort.** Thermal comfort (I039) has no measure in Welfare Quality, so no requirement can name it. The row is not_required, and any requirement on the thermal environment is recorded in the reasoning as related. *Example.* The RSPCA_Assured row of I039 is not_required, and its reasoning lists E 3.1, which says the thermal environment must not be so hot or so cold as to significantly affect production or cause distress (PDF 15, printed 13), as related.
13. **Numbers.** number_in_requirement holds any number or frequency the requirement sets, exactly as written. *Example.* The RSPCA_Assured row of I001 holds "at least four times a year", from H 3.5; the GAP_dairy row of I007 holds "Monthly", from 7.D.1.
14. **Global Animal Partnership at Step 1.** Global Animal Partnership is read at Step 1 only, a case of rule 4. *Example.* The GAP_dairy row of I001 quotes 5.B.1, marked at Steps 1, 2 and 3, which limits lameness score 3 to 2% (PDF 33, printed 23). 5.B.2, which sets 1% at Steps 4, 5 and 5+, is not counted.

Everything else in rules 4.6 to 4.8 still applies: quote exactly, write the page as "PDF n (printed m)", one requirement per row with the strongest (with a number if any) quoted and the others cited in the reasoning, no welfare science judgement, and no dashes as punctuation in the reasoning.

**Examples.** These three worked examples are part of the rule. The two quotations were checked against the scheme documents in 1_sources.

First, RSPCA Assured dairy cattle 2026, H 3.5, printed page 46: "All lactating cattle must be mobility scored at least four times a year by a mobility scorer registered with the Register of Mobility Scorers (RoMS) and the results recorded in the VHWP." That names lameness (Welfare Quality lameness, EFSA gait assessment, row I001). how_checked is records_review, since the assessor checks the recorded scores.

Second, "cubicle dimensions must be at least X" is related_resource for the comfort around resting measures. It is not a naming of time needed to lie down.

Third, FARM Animal Care v5, page 149: "Severe Lameness: 5% or less of the lactating cows observed score 3 on the FARM Locomotion Scorecard." That names lameness with a numeric threshold, named_with_threshold. The same page sets "Moderate Lameness: 15% or less" at score 2.

**How to check.** Read the requirement_status, then the quoted requirement in the row against the page. Ask whether it names the measure itself or a synonym, or only the housing, resource or practice around it, and which of the fourteen rules the reasoning names. For an unsure row, read its line in open_questions.md.

### 4.9 EFSA's own ratings

**Question.** How does EFSA itself rate each of its measures?

**Rule.** For each of the 32 rows that come from EFSA, efsa_sensitivity, efsa_specificity and efsa_feasibility in indicators.csv hold the level word that EFSA's ABM table uses for that measure, and efsa_ratings_quoted gives the table, the PDF page and the passages, quoted. The values are high, medium and low, as EFSA writes them. medium is kept as EFSA writes it. mixed is used where EFSA gives two levels for the same property, and not_stated where EFSA gives no level word. Welfare Quality only rows have no EFSA rating and stay empty. The ratings are EFSA's; this project adds no rating of its own.

How they are used. Since 5 November 2026, in two ways only, following Kevin's review: his own point on feasibility, and the summary of an exchange with Claude that Kevin forwarded with his review on sensitivity and specificity. Sensitivity and specificity are shown together as a validity flag beside the row and its state. They do not change the rank. A Welfare Quality only row or a sensor side row, which EFSA does not rate, shows "Not rated: not an EFSA measure", with no penalty. Feasibility rates how practical it is to take the measure on a farm, by a person. Kevin pointed out that this may cut the other way for this project ("I think EFSA's feasibility rating may point the wrong way"): a measure that is hard to take by hand is where a sensor adds the most. So feasibility is shown read the other way, as manual burden: low feasibility is High burden, medium is Medium, mixed is Mixed, and high is Low. Manual burden is the third key of the priority list (section 5), in the order High, Medium, Mixed, Low; a row whose feasibility is not_stated, or which EFSA does not rate, comes after them, the two alike.

**Example.** I023, body condition scoring, is medium, medium and high: EFSA Table 46 (PDF page 75) reads "Medium sensitivity and medium specificity" and rates feasibility high, as "already routinely done". I012, lying time, is high, low and low (Table 33, PDF page 54), so its manual burden is High. I017, self grooming, has specificity mixed, because EFSA writes "low specificity (in cows with healthy integument, specificity is high" (Table 42, PDF page 70).

**How to check.** Open the EFSA opinion at the table and page named in efsa_ratings_quoted and read the Sensitivity and Specificity line and the Feasibility line for the measure. check_tables.py confirms that the three ratings are filled exactly on the rows that come from EFSA and use only the five values.

### 4.10 Product links today

**Question.** Does the link the Stygar team printed for each product still open a page about that product, and where is the product's page today?

**Rule.** Each of the 129 products in the Stygar list is checked by opening its 2021 link on the date in the checked column. A link that loads for a person in a web browser but refuses scripts counts as live. link_2021_today is works when the link opens, directly or with only a change from http to https, a live page on the maker's own site, or the site of a company that sells the product under its own name, and that page names this exact product; moved when it is sent on (redirected) to such a page at another address; wrong_page when it opens a live page that does not name this exact product, including a page that names only its family, a dealer's, reseller's or other third party page, a parked domain (an address held by a domain seller, with no content of its own) or an unrelated site; and broken when it gives an error page, a dead address or no answer. So works and moved always go with product_page. Where the link does not work, the maker's current page is searched for, with at most three searches per product. A page is accepted only on the maker's own site, or the site of a company that sells the product under its own name, never a reseller's page, a news story, a file on a third party site or an archive copy. Another company's site counts as the maker's only where its own page says it owns or sells the product, or where the maker's own old address now sends visitors to it. A page that is only a notice sending visitors elsewhere is not the product's page, even if it names the product; such a row is related_page, and its note says what the notice names. A name counts wherever it appears in the page's visible text, including a menu or a customer quote, but not where it appears only in an image description or a file name. A new name counts as the same product only where the maker's page says so. current_link_shows is product_page when the page names the product, by Stygar's name, a spelling of it, or a new name the maker's page says replaces it; related_page when a maker's page names the product family, a close variant or a likely successor but not this exact product, and the notes say what it names; product_not_listed when a live maker page is given, often its home page, but the product is not named on it; and none_found when no live maker site is found, so current_link is empty.

This table records the web as it stood on the date checked. It is not a source for any grade, count or rank, which all read the Stygar list as published.

**Example.** Row 2, the WellCow bolus. Stygar printed a link to the design firm i4 Product Design; on 15 October 2026 it redirected to an error page, so it is broken. The product is not on the firm's site today, so the row gives the firm's home page as product_not_listed and says so in notes.

**How to check.** Open link_2021 and current_link and compare what they show with the two codes, then find page_says on the current page.


### 4.11 Evidence since 2021 (a second sensor column)

**Question.** What do studies and maker pages since 2021 add to the 2021 baseline of rule 4.2?

**Rule.** The baseline grade of rule 4.2 is never changed. A second grade, since_2021_grade, is read from sources published in 2021 or later, by the year of the journal issue: the reviews Lee et al. 2025 (with its dataset of 101 studies), Hudson et al. 2026, Islam et al. 2026, Silva et al. 2021 and Fuentes et al. 2026; a bounded search of Europe PMC for the milk and metabolic rows, whose protocol was written before it was run; studies one step through the reference list of any of these, read in full or as an abstract that states the product, the measure, the animals and the result; a vendor check of the makers' own current pages; and a test report from an independent test body, such as ICAR, that a maker's own page in the vendor check names. A study one step through a reference list counts; Kevin confirmed this in November 2026 ([his messages](../1_sources/kevin_slack_review_2026-11.md)). Such a study enters through a choice made here rather than through the review's own, so the route through which each one was found is recorded in found_via in evidence_since_2021.csv. A study that a review since 2021 only restates, but that was published before 2021, does not count. The grade uses the codes of rule 4.2:

validated_commercial: a study since 2021 tested a named product against a reference method on the indicator's own measure, and a source since 2021 (the study, a review or the maker's page) says the product is on sale. A test the maker was involved in counts, flagged, unless there is a clear conflict of interest or a flaw in the study that may have arisen from one. Kevin gave this answer for a study the maker funded ([his messages](../1_sources/kevin_slack_review_2026-11.md)); this rule applies it to any part the maker took in a study. The test is read from the study's own text: its conflict of interest statement, author affiliations, funding and contributions statements, and limitations. There is a clear conflict of interest when the conflict of interest statement declares a conflict with the maker; when an author is employed by the maker, which includes an author whose listed affiliation is the maker; or when the maker collected the reference measurements or the data, ran the analysis or controlled the results. Funding, devices, data or approval of the manuscript by the maker are not, by themselves, a clear conflict; they are recorded and flagged. A flaw counts where the study's own text reports a weakness tied to the maker's part in it. The maker's involvement and the result of the test, with the passages quoted, are recorded in the notes of the study's row in evidence_since_2021.csv and shown in the Excel file. A test that does not count leaves the grade to the rest of the evidence. The test decides whether a study counts as a test of a product; a study that fails it can still be read for what it shows about a measure, for example as a substitute measure under rule 4.2, and the row's reasoning says so (I028 and I029).

commercial_unvalidated: the maker's own current page names the product and says it measures the indicator's own measure, or a source since 2021 says a product on sale measures it, and no test against a reference was found. A page read by a person or saved by script is kept in 1_sources as a snapshot with a check phrase.

research_demonstrated, theoretically_measurable and none: as in rule 4.2, applied to the sources above. A test against a combined outcome of several measures (for example several foot lesions together) is a substitute for each one. Cattle includes beef cattle.

unsure: the sources above do not settle it. Where the baseline is unsure because the rules do not settle what the indicator's measure is (I006, clinical mastitis as an incidence rate; I039, thermal comfort with no defined measure), the grade since 2021 is unsure for the same reason unless the new evidence settles that question. The same holds where the measure is a change or a rate computed from repeated values and the evidence tests single values (I058, an increase in a cow's cell count between recordings).

**Which grade counts.** The validity key of the priority list (rule 4.15, section 5) and Kevin's list 1 (section 6) use the stronger of the two grades, in the order none, unsure, theoretically_measurable, research_demonstrated, commercial_unvalidated, validated_commercial; but where the 2021 grade is unsure and the grade since 2021 is not commercial, the result stays unsure, because the open question could still change the answer; and where only the grade since 2021 is unsure, the 2021 grade stands, so an unsure grade since 2021 never lowers the 2021 grade, unless the 2021 grade is none and one of the candidate readings in its open_questions.md line is commercial, in which case the result is unsure, because that reading could put the indicator on list 1. Both grades are shown in the Excel file.

**Example.** I013, frequency of lying bouts, is unsure in the 2021 baseline. Since 2021, the maker's page for the IDS i-QUBE leg sensor lists Lying Bouts as an output, so the grade since 2021 is commercial_unvalidated, and the stronger of the two is Claimed. No scheme requires it, so it is on Kevin's list 1.

**How to check.** Read the row's since_2021_evidence keys on the sheet Evidence since 2021, open each source file named there, and confirm the product, the measure, the reference method and the result.

### 4.12 The sensor side rows

**Question.** What do commercial sensor products say they measure that no protocol row covers?

**Rule.** Every parameter named in the AIM of a product in the Stygar list is either covered by a protocol row or has a row of its own, coded listed_by plf_only, so that no parameter is let in or kept out by judgement (Kevin's change request of 7 October 2026, and the fourth amendment in the decision log entry of that day). A parameter named in an aim is covered by a protocol row when one of that row's search words in sensor_coverage.csv matches it: the project's existing reading of which aims name which indicator (rule 4.5). Every other parameter named in an aim belongs to a parameter class, at the grain of Kevin's examples (activity, lying time, rumination, temperature, weight, location). Words join one class when they name the same quantity in other words or by another method: heat detection and milk progesterone for heat; positioning, GPS, tracking, a virtual fence, herd counting and theft alerts for location; rumen temperature and fever for body temperature. A general status a product claims (health, wellbeing, nutritional, reproductive) is a class of its own. A class is read in the animals its aims name: the automatic milk feeders, whose aims all name feeding fresh or replacement milk and none names cows, and whose product names call them calf feeders (for example Calf feeding system, Calf Star, Calfexpert), form their own row, I082, because rule 6 of rule 4.8 reads every row in its own animals. Where a single aim among a class's cow aims names calves (Medria Thermistor on I064, Förster Technik Smart Neckband on I067 and I071), the aim stays in the class, the row is read for adult cows, and its notes name the calf aim. Each class has search words that reproduce its product count, as every row does. One aim names no parameter, Mastiline Luci's "Milk analyzer", so it has no row; check_tables.py confirms that every other product in the list is named by at least one row. This gives 23 sensor side rows, I060 to I082.

A sensor side row gets every column a protocol row gets, with the class as its measure: the sensor evidence of rule 4.2 and the grade since 2021 of rule 4.11, the Maroto Molina rating of rule 4.3, device needed, vendors naming it, the FARM naming record and the four schemes of rules 4.4 to 4.8, the welfare state of rule 4.13, column 1 of rule 4.14 and the two columns of rules 4.15 and 4.16. Its EFSA ratings are empty, as on a Welfare Quality only row. For the grade since 2021 no new vendor check is made: every sensor side row is already at least Claimed in 2021, which is the most a vendor check can give (rule 4.11), so the grade is read from the other sources rule 4.11 names, already on disk.

**Example.** I060, rumination: 14 aims name it (search word ruminat). Stygar Table 2 (page 7) codes rumination studies for five products in the list, among them CowManager SensOor and RumiWatch, so it is validated_commercial. No scheme requires it.

**How to check.** Run `python 3_code/count_vendors.py I060`, or open the Sensors x products sheet, where every row marks the products whose aims its search words match. The product with no row is the one column left blank in every row.

### 4.13 Welfare state

**Question.** Which rows measure the same welfare state, so that Kevin's lists can be read once per state?

**Rule.** welfare_state is read from the sources, as the decision log entry of 7 October 2026 set out. For a row from EFSA (efsa_only or joined), it is the condition or problem that EFSA's ABM table names for the measure: the sub-heading in Table 46 (for example Subclinical ketosis, PDF 75), otherwise the table's title (Table 16, lameness; Table 17, claw conditions or claw diseases; Table 27, mastitis; Table 31, restriction of movement (locomotion); Table 32, restriction of movement (social behaviour); Table 33, resting problems (lying behaviour); Table 42, comfort behaviour). Table 18 lists hock and knee alterations but repeats Table 17's title (found_along_the_way.md, section 12), so its two rows take the name of the Welfare Quality measure they share, Integument alterations. For a Welfare Quality only row, it is the Welfare Quality criterion, the protocol's own grouping of measures (for example Absence of prolonged thirst for the four water point rows). One criterion is the exception. Absence of disease groups measures of separate conditions, and Welfare Quality scores each of them separately: "The prevalence of each health problem recorded is transformed into a score", and its scoring table lists the criterion's nine measures one by one, with Mastitis in the place of milk somatic cell count (section 5.2.1.7, PDF 48, printed 47; the nine measures are listed on the overview, PDF 22). The milk somatic cell count measure itself says counts above 400,000 "are considered to indicate subclinical inflammation" (PDF 35, printed 34). The criterion Absence of pain induced by management procedures also scores its two measures separately, but they are two procedures, disbudding or dehorning and tail docking, not conditions, so its rows keep the criterion as their state. So since 5 November 2026 each Absence of disease row takes the name of its own Welfare Quality measure (I043 Nasal discharge, I044 Ocular discharge, I045 Hampered respiration, I046 Diarrhoea, I047 Vulvar discharge, I048 Mortality, I049 Dystocia, I050 Downer cows), and I057, milk somatic cell count, takes Mastitis, which joins it to EFSA's Mastitis state. For a sensor side row, it is the row's own parameter, unless the parameter itself is a condition that an EFSA table heading names, in which case it takes that heading: I081, rumen acidosis, whose aims name rumen acidosis and SARA, is Subacute ruminal acidosis. A row whose aims also name a condition beside the parameter (for example lameness on the aims of I060 and I064) keeps its own parameter. The joined row I023, body condition scoring, sits in EFSA's Subclinical ketosis; Welfare Quality places the same measure under Absence of prolonged hunger, which its wq_criterion column shows.

**Example.** I021, I022 and I023 are EFSA's three tests for subclinical ketosis, and all three carry the state Subclinical ketosis.

**How to check.** Open the EFSA opinion at the table named in the row's efsa_ratings_quoted, or the Welfare Quality overview (PDF 22, printed 21), and read the heading or criterion. For an Absence of disease row, read the scoring table of the protocol's section 5.2.1.7 (PDF 48, printed 47).

### 4.14 Welfare relevance (column 1)

**Question.** Do the welfare sources treat the row as a measure of welfare? This is a different question from whether it can be measured, which is column (a).

**Rule.** No grade is a welfare judgement made here; every grade follows from the measure type or from the words of named sources (decision log, 7 October 2026, third amendment; Manisha's decisions of 17 October 2026).

Protocol rows. established when the measure_type is animal_based, because EFSA's ABM tables or the Welfare Quality protocol list it as a measure taken on the animal. established_input when it is resource_based, management_based or none: Welfare Quality lists it, but as a measure of the housing or the management, or as a criterion with no measure, which Kevin's change request calls validated protocol components rather than welfare outcomes. No protocol row is graded down from EFSA's own ratings; they stand beside the grade.

Sensor side rows. Kevin's change request names three sources for this column: EFSA's own sensitivity, specificity and feasibility ratings, Welfare Quality's validation history, and Linstädt et al. 2024, which it calls purpose built for grading the sensor side rows. EFSA's ratings and Welfare Quality cover only protocol measures, so for the sensor side rows Manisha decided on 17 October 2026 to use three documents only, each read in full: the EFSA 2023 opinion, the Welfare Quality protocol version 3.2, and Linstädt et al. 2024, including what it says about the studies it cites. Every passage about the parameter in cattle is sorted by its own words. A link says that the parameter, or a direct synonym of it, is a measure, indicator, sign or predictor of, or is associated with, or changes with, a welfare problem, a disease or condition, pain, stress, fear, comfort, an emotional state, or welfare itself; a table that lists it as a measure used to assess a welfare problem counts. A question says that the parameter's link to welfare, or its use as an indicator of welfare or of a welfare problem, is indirect, insufficient on its own, weak, inconsistent, unclear or not fully understood. A passage that names a different parameter (for example appetite for feed intake, or GPS only as a way to measure walking speed) is neither; nor is a passage saying that the condition a parameter detects is not a hazard for some other problem.

The grade, in this order: indirect_or_contested if any passage questions the link; otherwise supported if any passage links it; otherwise no_welfare_validation if the aim of a product that names it says the parameter is for health, welfare or wellbeing or for a named disease or condition, or the parameter is itself a health, welfare or condition status, or one of the four schemes requires it (requirement_status required), since the four schemes are animal welfare standards and a requirement frames the parameter as part of welfare; otherwise not_welfare_relevant. This follows Kevin's change request, which keeps not welfare relevant for parameters that no one credibly claims are welfare relevant. A product's aim that only lists the parameter beside health words, without saying it is for them, does not frame it. unsure when a passage the grade turns on is borderline under these words, with a line in open_questions.md.

Column 1 does not change Kevin's lists (Manisha's decision of 17 October 2026). It sits beside them, so a sensor side row on list 1 shows whether the welfare sources treat it as a welfare measure. Since 5 November 2026 it is the gate of the priority list. Kevin's comment is that welfare relevance must act as a gate, and that "if something is not welfare validated, it should rank low"; following the summary he forwarded, such a row leaves the list altogether: a row graded no_welfare_validation or not_welfare_relevant leaves the list and is shown on the sheet Not backed by welfare science, as a finding of what the market measures that the welfare sources do not back; a row graded indirect_or_contested or unsure stays, flagged (section 5). The gate adds no judgement: the grade still follows only the words of the named sources.

**Example.** I075, milk yield, is indirect_or_contested: Linstädt et al. 2024 (PDF 12) say that "relying solely on milk yield is insufficient for gauging the comprehensive welfare of the herd", and EFSA 2023 (section 5.7, PDF 80) finds "no clear evidence that herd size or milk yield could be useful characteristics to identify farms at risk of poor welfare", although both also link milk yield to lameness or disease. I060, rumination, is supported: Linstädt et al. 2024 (PDF 9) report that rumination time fell as heat stress rose, and nothing in the three sources questions the link. I077, blood in milk, is not_welfare_relevant: no passage links it to welfare, the one product description (Crystalab) does not say it is for health or welfare, and no scheme requires it. I067, animal identification, is no_welfare_validation: no passage links it, but FARM v5 and Global Animal Partnership require it, so the welfare schemes frame it as part of welfare.

**How to check.** Read the row's welfare_relevance_evidence, open each source at the page given and read the passage; then apply the order above.

### 4.15 Validity of the best test

**Question.** Where a product was tested against a reference, how well did it do?

**Rule.** The summary of an exchange with Claude that Kevin forwarded with his review asked that the single grade Tested be split by how the test went. The test is the one Stygar 2021 use to put a technology in their high performance column, applied in full (Manisha's decision of 6 November 2026). Their methods (page 4) say high performance "was reached when all indicators defined/selected by authors of studies fulfilled following criteria: r, rs, CCC, Se, and Sp, or AUC was >0.9, R2 and κ was >0.81, I/S did not differ significantly from 0 or 1, respectively, and B–A plot included zero with the 95% interval of agreement", and the footnote to Table 2 (page 7) gives the same criteria in words, naming the regression coefficient where page 4 names R2. So Pearson and Spearman correlation, concordance correlation, sensitivity, specificity and area under the curve must be above 0.9; R squared and kappa above 0.81; the intercept and slope of a regression of the product on the reference must not differ significantly from 0 and 1; and zero must lie within the 95% limits of agreement of a Bland–Altman analysis.

stygar_performance, for a row whose 2021 grade is validated_commercial, is read from Stygar's own columns: above_threshold when Table 2 puts at least one trial of a tested product on the row's trait in the high performance column, otherwise below_threshold. The row's validated_trait says which column each trial is in.

since_2021_performance, for a row whose grade since 2021 is validated_commercial, is read from the counted test (rule 4.11), as Stygar read every study: all the results count. It is above_threshold when every statistic of a kind the test covers that the study reports for the product meets the test, in every setting it reports (every place, herd, device position or device configuration); below_threshold when at least one does not; and not_graded when the study reports no statistic of those kinds, or when only a review's summary of it is on disk and every value the summary gives meets the test, because the rest cannot be read. Where several counted tests bear on the row, the column takes the best, as Stygar's own column does (the settings and software versions of one product within a study are read together, which is stricter than Stygar's table where it lists two versions apart): above_threshold when the test of at least one product passes in full; otherwise not_graded when one cannot be graded; otherwise below_threshold. Where a report prints a regression without saying which values are on which axes, so that it cannot be told whether it is the intercept and slope test, the test cannot be graded: not_graded, with a line in open_questions.md. since_2021_performance_reasoning names the study, the statistics and their values.

The validity of the best test, shown in the Excel file, is Tested above the bar when either column is above_threshold; otherwise Tested, results that cannot be graded against the test, when either is not_graded; otherwise Tested below the bar. A result the test cannot grade is not a result below it, so it ranks between the two. A row that is not Tested takes its level from the stronger grade (rule 4.11): Claimed, Shown in research, Proposed only, Nothing found or Unclear. This is the first key of the priority list (section 5).

**Example.** I057, milk somatic cell count, is Tested below the bar: Hubner et al. 2023 tested the LactiCyte HD against flow cytometry at 16 and 8 images; the concordance correlation (0.96) and sensitivity (92.0%) pass at both, but specificity is 85.7% at 8 images, and at 16 images the Deming regression has slope 1.3 and intercept -50.6, both differing significantly from 1 and 0. I021, subclinical ketosis by milk constituents, cannot be graded since 2021: ICAR's 2025 test of the Brolis BLH01 gives R squared of 98.2% for fat and 95.0% for protein, and zero lies within every Bland–Altman interval, but it also prints regression lines without saying which values are on which axes, and read one way they fail the intercept and slope test; its line in open_questions.md gives both readings. I060, rumination, is not_graded since 2021: of its five counted tests none passes in full, and Borchers 2021 cannot be graded, because only Lee 2025's summary is on disk, which gives a concordance correlation of 0.93 to 0.98 but no values for the Pearson correlation and Bland–Altman plots it says the study used; its 2021 column is above_threshold, so its validity is Tested above the bar.

**How to check.** For the 2021 grade, open Stygar Table 2 (page 7) at the trait in validated_trait and read the column. For the grade since 2021, open the study named in since_2021_performance_reasoning and find the statistic.

### 4.16 What products do with the signal

**Question.** When products measure it, do they say the measurement is for health or welfare?

**Rule.** The summary of an exchange with Claude that Kevin forwarded with his review points out that "a sensor can measure it" is not "PLF is built around it": column (a) says whether a product measures the row, but not what the product does with the measurement or what it is tuned for. signal_purpose reads that, as far as the sources say it, from the AIM of every product in the Stygar list that the row's search words match (rule 4.5), with the wording rule of column 1 (rule 4.14). health_or_welfare when at least one aim says the measurement is for health, welfare or wellbeing or for a named disease or condition, or when the measurement is itself a health, welfare or condition status. production_only when no aim gives it a health purpose and at least one gives it a production, fertility, feeding or herd management purpose. not_stated when the aims name it without saying what it is for. An aim that only lists the measurement beside other functions, such as heat detection or health alerts, gives it no purpose, as in column 1. unclear when an aim the value turns on can be read either way, or when whether any product measures the row is itself open (its sensor evidence since 2021 is unsure with a commercial candidate), with a line in open_questions.md. no_product when no product in the Stygar list names it and no product since 2021 measures it. Where no product in the Stygar list names the row but its grade since 2021 is commercial, the purpose is read in the same way from the maker's page that grade rests on (Manisha's decision of 5 November 2026). A maker's page since 2021 is not read for a row the Stygar list names, so a newer page that gives a health purpose does not change the code; the value says what the 2021 descriptions say. signal_purpose_evidence quotes the aims or the page.

This reads what products say they are for. It does not say what they do on a farm, and it is not a welfare judgement. It decides between World A and World C in section 5.

**Example.** I060, rumination, is not_stated: aims such as AfiCollar's "Heat detection, rumination, health alerts" list rumination beside health alerts without saying rumination is for them. I076, milk electrical conductivity, is health_or_welfare: SmartD-TECT "provides early warning of potential udder health issues". I062, individual feed intake, is production_only: the feeding stations feed "according to requirements". I002, claw conditions, has no product in the Stygar list; Hoofcount's page says PediVue's images "are analysed using computer vision to detect early signs of digital dermatitis", a named condition, so it is health_or_welfare.

**How to check.** Run `python 3_code/count_vendors.py <id>` to list the products whose aims the row's search words match, and read each aim in the Stygar list; for I002 and I059 read the maker's page in 1_sources named in signal_purpose_evidence.

## 5. The priority list

Until 5 November 2026 the rows were sorted by a score from 0 to 15, the sum of five factors. Kevin's review of November 2026 ([his messages](../1_sources/kevin_slack_review_2026-11.md)) said the ranking was invalid once it held rows that are not welfare validated, asked whether FARM was counted twice, which it was, and said that EFSA's feasibility may point the wrong way. In the summary of an exchange with Claude that Kevin forwarded with his review, adding the parts let cost and vendor count make up for irrelevance, and a ranking applied in order is proposed; Kevin's own comment on it is that welfare relevance must act as a gate. The score is gone. In its place is a ranking applied in order, not one number, in four steps.

**Step 1, the gate.** A row whose column 1 grade is no_welfare_validation or not_welfare_relevant leaves the priority list (rule 4.14). These rows are shown on the sheet Not backed by welfare science: what the market measures that the welfare sources do not back. A row graded indirect_or_contested or unsure stays, flagged beside its state.

**Step 2, welfare states.** The rows that pass are grouped by welfare state (rule 4.13), and each state carries forward its best row, the one that comes first under the keys of step 3. The state's other rows are named beside it.

**Step 3, the keys.** The states are ranked by their best row, on these keys in this order:

1. Validity of the best test (rule 4.15): Tested above the bar, Tested with results that cannot be graded against the test, Tested below the bar, Claimed, Shown in research, Proposed only, Nothing found, Unclear.
2. Device needed (rule 4.4): routine_data, farm_fixed, animal_mounted, sample_or_procedure, none, unsure.
3. Manual burden (rule 4.9): High, Medium, Mixed, Low, then not stated or not rated.
4. Indicator id, to break any tie left.

The summary gives the order as relevant state, impact tier, validity of the best test, marginal cost. The impact tier is left out. The summary proposed checking first whether EFSA 2023 ranks its welfare consequences by severity, prevalence or duration. Kevin's comment is that a tier "would be great if there is hard evidence on this", that "If this requires subjective welfare judgment, it's fine not to include it", and that the EFSA suggestion came from Claude and he did not check it. EFSA does not rank its consequences: it assessed five because the Commission's mandate asked for them (abstract, PDF page 1). Welfare Quality considers some criteria more important than others within each principle (for example Absence of disease above Absence of injuries above Absence of pain induced by management procedures, PDF 18 and 54, printed 17 and 53), and weights them when it combines criterion scores into a principle score. That orders only its own criteria, within one principle at a time; it does not compare principles, and it does not cover EFSA's states or the sensor side. Using it to rank the welfare states of this table would need choices that are welfare judgements, which hard rule 2 of this project rules out. Marginal cost is the device needed, and manual burden, the value of automating the measure, breaks ties within a device class. The vendor count, FARM naming and the number of schemes requiring a row are not keys. The vendor count and the schemes are shown in the Excel file; FARM naming is kept in crosswalk.csv.

**Step 4, the kind of ask.** The summary of an exchange with Claude that Kevin forwarded with his review names three asks. World A: the measure exists and is used, so ask schemes to accept the sensor data. World B: the welfare state matters but there is no sensor, so ask for new measurement. World C: the signal is already on the farm but nothing is built around it with welfare as the goal, so ask for software, alerts or welfare thresholds. Each state on the list gets one, read from its rows that pass the gate, using the stronger sensor grade (rule 4.11), the schemes (rule 4.8) and signal_purpose (rule 4.16), in this order. A, accept: a row is Tested or Claimed, and a scheme requires a row of the state. Unclear on schemes: a row is Tested or Claimed, no scheme requires any row, and a scheme row of the state is unsure, so a scheme may require it and the answer could be A, accept (Manisha's decision of 6 November 2026, as Kevin's lists show Unclear in section 6). A, adopt: a row is Tested or Claimed, no scheme requires or may require any row, and a Tested or Claimed row is used for health or welfare; the sensor data exists and is used for welfare, but no scheme asks for it. Unclear on purpose: as for C below, but a Tested or Claimed row is unclear on signal purpose. C: a row is Tested or Claimed, no scheme requires or may require any row, and no Tested or Claimed row is used for health or welfare. B: no row is Tested or Claimed and none is unsure on sensor evidence. Unclear on sensor evidence: no row is Tested or Claimed and a row is unsure. The kind of ask is shown beside the rank; it does not change it.

On 5 November 2026 there are 52 welfare states. Five hold only rows that leave at the gate (I063 individual water intake, I067 animal identification, I077 blood in milk, I078 LDH in milk and I082 milk fed to each calf), so 47 are on the priority list. On 6 November 2026, of those, 4 are A, accept; 8 are Unclear on schemes; 6 are A, adopt; 4 are C; 20 are B; 3 are Unclear on sensor evidence; and 2, location and oestrus detection, are Unclear on purpose.

The order of the keys is set here, and in build_output.py, which must match it. Only a decision log entry can change it. It is a sort order, not a welfare judgement and not a recommendation.

The keys are read independently of each other. So a row's validity can come from a tested product that is an added device while its device class is routine_data because the value is already in records. I021 and I025 work this way: the test is of an inline milk analyser fitted at the milking point, and the device class comes from routine milk recording, which EFSA's definition names.

Tested products and products whose description names it are separate columns. A product can be tested for a measure without its own description naming it, and the reverse. On I012, Track a))) Cow and RumiWatch were tested for lying, but their descriptions do not contain the search words, so they are among the tested products and not among the products that name it.

**Example.** Feeding behaviour and feeding time is rank 1 through I061: Tested above the bar in Stygar's 2021 column, on a farm_fixed device (a feeding station), named by products that do not say what it is for, and required by no scheme, so it is World C. It is flagged, because column 1 grades I061 indirect_or_contested: the gate keeps such a row and marks it. Subclinical ketosis is rank 6. Its best row is I021, milk constituents: Tested, results that cannot be graded (rule 4.15), routine_data, because EFSA's definition takes it from milk recording, and Low manual burden, because EFSA rates it high on feasibility. A scheme requires one of its rows, body condition scoring (I023), so its kind of ask is A, accept, although the row the schemes require is not the row the tested sensor measures; the Priority sheet names both. Mastitis is rank 8: its best test, of I057, is below the bar.

**How to check.** The Priority sheet of the Excel file lists the states in rank order with each state's best row, its validity, device and manual burden, and its kind of ask. The Answer sheet shows every row with its gate and its state's rank. In build_output.py the order is set in VALIDITY, DEVICE_ORDER and BURDEN.

## 6. Kevin's two lists

Kevin's item 13 names two valuable cells: "indicators already instrumented but not required, and indicators required but manually audited" ([his text](../1_sources/kevin_item_13.md)). Both lists are computed by build_output.py from the same rows as the ranked Answer sheet.

A scheme counts as requiring an indicator only when its row's requirement_status is required (rule 4.8). A scheme row coded unsure is neither required nor not required, so it makes the lists Unclear wherever it could change the answer, as set out below.

**List 1, instrumented but not required.** Sensor evidence, the stronger of the 2021 grade and the grade since 2021 (rule 4.11), is validated_commercial or commercial_unvalidated, and the schemes requiring it number 0. Yes is reported for an indicator only once all four schemes have been read for it, because before that a count of 0 means not yet read rather than not required. No is final as soon as one scheme is read and requires it, whatever the sensor evidence. An indicator whose sensor evidence is unsure shows Unclear, unless a scheme already requires it, because it could join the list once its question is settled. An indicator graded Tested or Claimed that no scheme requires, but that has a scheme row coded unsure, shows Unclear, because that scheme may require it.

**List 2, required but manually audited.** Kevin's "indicators required but manually audited". Per scheme row, the requirement is present (requirement_status required) and the scheme checks it by inspection or by records review (how_checked visual_inspection or records_review), not by accepting sensor data. The sensor evidence for the indicator is shown beside it. This replaces the earlier, narrower filter, which also required sensor evidence validated_commercial. When no scheme that requires the indicator checks it by inspection or records review, the list shows Unclear if a requiring scheme's how_checked is unsure, or if a scheme row is coded unsure, because either could put the indicator on the list. Where another scheme that requires it does check it by inspection or records review, the indicator is on the list, whatever the unsure row says.

On 5 November 2026, with all four schemes read for all 81 rows and the stronger of the two sensor grades used, the Read me sheet shows 21 indicators confirmed on list 1, the same rows as on 17 October 2026: the 9 protocol rows I002, I008, I012, I013, I021, I022, I025, I027 and I059, and 12 sensor side rows, I060 to I066, I068 and I076 to I079. Four more are Unclear because their sensor evidence is unsure (I009, I010, I039 and I056), and 8 sensor side rows are Unclear because a scheme row is unsure (I069 to I075 and I081). 24 are confirmed on list 2: 22 protocol rows, and I067 (animal identification) and I082 (milk fed to each calf) on the sensor side. On the protocol side the 5 scheme rows coded unsure fall on four indicators (I036, I037, I038 and I048), each already on list 2 through another scheme, so they change neither list. Read per welfare state, 15 of the 52 states are on list 1 and 10 are Unclear; 16 are on list 2 and 9 are Unclear. There are more states than the 45 of 17 October 2026 because the Absence of disease rows were split (rule 4.13). The two lists are Kevin's two cells of item 13 and do not use the gate of section 5, so a row that leaves the priority list, such as I063, individual water intake, can still be on list 1.

**The lists by welfare state.** The sheet By welfare state reads both lists once per welfare state (rule 4.13). A state is on list 1 when at least one of its rows is Tested or Claimed (the stronger of the two grades) and no scheme requires any of its rows; it is No as soon as a scheme requires one of its rows, and Unclear when a scheme row of the state is unsure and the state has a row that is Tested, Claimed or unsure on sensor evidence, or when its only candidate is a row whose sensor evidence is unsure. A state is on list 2 when at least one of its rows is on list 2, and Unclear when none is but one shows Unclear there. The sheet names the rows behind each answer, so a reader can see, for example, that subclinical ketosis is required through body condition scoring (I023) while its milk tests are not.

## 7. When the rules do not decide: unsure

Any cell the rules above do not settle is coded unsure. The candidate readings go in the row's reasoning column, and a line in [open_questions.md](open_questions.md) gives the indicator, the column and the candidates. It is resolved only by tightening the rule that failed, with a dated decision log entry. Otherwise it stays unsure in the published table, and the note says how many rows are unsure per column. On the priority list an unsure sensor grade ranks last on validity and an unsure device class last on device (section 5), and a state with no Tested or Claimed row but a row unsure on sensor evidence shows its kind of ask as Unclear. A scheme row whose requirement_status is unsure does not count its scheme as requiring the indicator, and it can make Kevin's lists Unclear (section 6). An unsure how_checked cell, which is kept only for a required row whose method the scheme truly leaves open, still counts its scheme as requiring the indicator and can show Unclear on Kevin's list 2 (section 6).

On 12 October 2026, seven rows are unsure on sensor evidence (I006, I009, I013, I020, I039, I057 and I058) and four on device needed (I043, I044, I047 and I059). On 5 November 2026, eleven rows are unsure on the grade since 2021 (I006, I010, I039, I045, I056 and I058 on the protocol side; I062, I065, I068, I080 and I082 on the sensor side, where the 2021 grade stands either way). I075 was the twelfth until the conflict test written into rule 4.11 after Kevin's answer settled it. In crosswalk.csv, 22 of the 324 scheme rows have requirement_status unsure. Five are on the protocol side: I036 for Certified Humane, I037 for Certified Humane, I038 for RSPCA Assured, and I048 for Global Animal Partnership and Certified Humane. Seventeen are on the sensor side: I067 for RSPCA Assured and Certified Humane; I069 and I070 for RSPCA Assured; I071 for RSPCA Assured, Global Animal Partnership and Certified Humane; I072 for RSPCA Assured and Global Animal Partnership; I073 and I074 for Certified Humane; I075 for RSPCA Assured and Certified Humane; I080 for FARM; I081 for RSPCA Assured and Certified Humane; and I082 for Certified Humane. Most turn on the same few points the reading rules do not settle: whether a general health inspection names a general health status, whether a farm's welfare outcome assessment names a welfare status, and whether acidosis named without its form names the acidosis row. No row has how_checked unsure. Two sensor side rows are unsure on column 1: I066, location, where one product's aim can be read either way, and I072, a welfare status, where the passages that might question the link speak of validation. On signal purpose, six rows are unclear: I066, location, for the same aim; I068, oestrus detection, and I069, pregnancy and reproductive status, whose aims can be read either way; and, on the protocol side, I010, I039 and I056, where whether any product measures the row is open (rule 4.16). The last three do not change a kind of ask, which reads signal purpose only on Tested or Claimed rows.

## 8. Change log

The rows before 0.2.1 use the file and column names of their day. definitions.md is now rules.md, notes/decisions.md is decision_log.md, and the column names are mapped in the decision log entry of 2 October 2026 on the reorganisation.

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-09-25 | 0.1 | Written from Kevin's steer of 25 September and the smaller scope analysis of 23 September | Fixed before extraction |
| 2026-09-25 | 0.1.1 | Hardware class: none when no sensor source names a technology even if EFSA scores by procedure; unsure rows take the class of the cheapest commercial candidate | Two rule gaps found by the first row audit |
| 2026-09-29 | 0.1.2 | Hardware class: tie break among proposed technologies when none is commercial; inline milk analysers are farm_fixed | Found by the batch 2 audit |
| 2026-09-30 | 0.1.3 | Hardware class: indicators defined from routine milk recording or farm records are routine_data | Batch 3, the milk constituent rows |
| 2026-09-30 | 0.1.4 | Commercial in the hardware class rules means an appendix product whose aim states the measurement, not one of the same technology type; research_only covers a substitute measure at any feasibility rating | Found by the batch 4 audit, two passes |
| 2026-10-02 | 0.2 | Unit states the indicator scope outright (the nine EFSA ABM assessment tables, the Welfare Quality v3.2 overview) with the row counts; maroto_molina_feasible gets a written definition; the records rule for the hardware class applies to unsure rows; the item 13 required but manually audited view follows Kevin's wording, and instrumented but not required waits until all four schemes are read; product_ids and validated_products are distinguished | The nine agent audit of 2 October |
| 2026-10-02 | 0.2.1 | Rewritten in plain language and merged with the column guide; no rule changed | A file that a reader who does not code can follow |
| 2026-10-02 | 0.2.2 | Wording only, no rule changed. The ICAR entry in section 2 no longer says that none of the three ICAR products measures a welfare indicator, which was wrong: it now names what each measures. The lying time example in rule 4.2 now quotes Stygar's real trait name. Rule 4.4 now says that a routine_data row can have sensor evidence none | Found by two cold readers of the rebuilt repository |
| 2026-10-03 | 0.3 | Changes of meaning. Rule 4.3 is read literally: yes only where Maroto Molina's passage says the technology is commercially available or in use on commercial farms, otherwise partial; I001, I012, I013, I057 and I058 move from yes to partial. The records rule of rule 4.4 applies only where the indicator's own definition takes the value from records, so it holds for I020, I024, I028 and I029 and not for I006, which returns to the unsure fill as farm_fixed; the rule 4.4 example now uses I020. unsure is a value of how_checked and farm_naming (rules 4.6 and 4.7, section 2), scores 0 on named by FARM, and needs a line in open_questions.md; version 0.2.1 already listed it in section 2 as allowed by check_tables.py, but it was formally added only in 0.3. Kevin's list 1 shows Unclear for a row whose sensor evidence is unsure, and list 2 shows Unclear when a required row's how_checked is unsure (section 6). Written down, with no change to any score: ties in the score are sorted by indicator id; the five factors are scored independently; tested products and products whose description names it are separate columns (section 5). Also recorded here: the measure_type column of indicators.csv, with its coding rule in section 2, was added on 2 October 2026 with the reorganisation, which the 0.2.1 row does not name. The bolus entry in section 2 now matches EFSA's description of the rumen pH bolus | Audit findings checked again by a second agent; decision_log.md, entries of 3 October 2026 |
| 2026-10-03 | 0.3.1 | Wording and clarification only, no change of meaning. The opening line says the rules were first fixed before any sensor row was graded, and that the indicator and product tables were copied from plf-audit. In the rule 4.4 example the I006 candidates are called milk quality sensors, as the Stygar list calls them, not inline milk sensors. The rule 4.4 sentence on I007 now says why the routine_data class list applies to I007 and not to I006: the list names somatic cell count from records, and EFSA calls bulk milk SCC records readily available, while mastitis incidence is not in the list and EFSA calls its records dependent on availability and accuracy. Section 6 says the 8 indicators waiting on list 1 are graded Tested or Claimed in column (a). The Other words table in section 2 gains BCS, BHB, CMT, DHIA, LDH, NIRS, SARA and SCC, the abbreviations used in table cells. Also recorded here, because the 0.3 row does not name them: in 0.3, I007 was explained by the class list item somatic cell count from records, which has been in the rules since 0.1 and was the basis of the published I007 row, instead of by the records rule, with no value or score changed; and the rule 4.3 How to check now says maroto_molina_2020.pdf is link only | Audit findings of 3 October 2026; decision_log.md, entry of 3 October 2026 on the wording fixes |
| 2026-10-03 | 0.3.2 | Change of meaning, narrower hold back on list 1 (section 6): an indicator is No as soon as one scheme is read and requires it, whatever its sensor evidence, since its count of requiring schemes can then never be 0; before, a list 1 row graded Tested or Claimed waited for all four schemes, an unsure row showed Unclear and a row not yet graded showed Not yet checked, whatever the schemes said. Yes still waits for all four schemes. The Not yet known glossary entry and the crosswalk.csv note were brought in line. | Third and fourth confirmation audits, 3 October 2026; decision_log.md entries of 3 October 2026 on Kevin's files, on the fourth confirmation audit and on the fifth confirmation audit |
| 2026-10-08 | 0.4 | Changes of meaning, for reading the certification schemes. crosswalk.csv gains the column requirement_status (required, unsure, not_required) after scheme, and only required counts toward the schemes requiring an indicator; section 3 describes the column and what an empty cell means, and says the table now has all 232 rows. Rules 4.7 and 4.8 now carry the fourteen reading rules approved by Manisha Sarkar on 8 October 2026, each with an example from crosswalk.csv; the three worked examples are kept. how_checked unsure is kept only for a required row whose method the scheme truly leaves open, no longer for naming that is unsettled, and visual_inspection covers observing a resource or equipment. farm_naming follows requirement_status (rule 4.6). Section 6 says a scheme row coded unsure makes Kevin's lists Unclear where it could change the answer. indicators.csv gains efsa_sensitivity, efsa_specificity, efsa_feasibility and efsa_ratings_quoted, with the new rule 4.9 for EFSA's own ratings (high, medium, low, mixed, not_stated) and section 3 rows for the four columns. Section 2 gains glossary rows for sensitivity, specificity and feasibility and code tables for requirement_status and the EFSA ratings. The section 5 example, section 7 and the Not yet known and Unclear entries are brought up to date with the read schemes | Four readers found 41 of the 232 scheme rows unsure under rules 0.3.2, almost all from situations those rules did not cover; Kevin's change request of 7 October asked for EFSA's ratings; decision_log.md, entries of 7 October 2026 and 8 October 2026 |
| 2026-10-12 | 0.4.1 | Wording only, no change of meaning. The opening line and the notes on indicators.csv and products.csv no longer point to another repository; the products.csv note says where its 17 Stygar products came from and that no grade or count depends on them; the Provisional rank entry and the counts in sections 3, 5 and 7 are brought up to date for the sensor rows of 9 October | Manisha asked that the repository stand alone; decision_log.md, 12 October 2026 |
| 2026-10-15 | 0.5 | New table product_links.csv (section 3) and rule 4.10, with its codes tightened after the audit of the same day (works and moved only with product_page; one code, product_not_listed, for a live maker page without the product; visible text only; http to https alone is works; a site the maker's own old address now sends visitors to counts as the maker's; a notice that only sends visitors elsewhere is not the product's page): the 129 links Stygar printed in 2021 are checked again and the products' current pages recorded. No grade, count or score changes | Manisha found a Stygar product link that no longer works and asked for every link to be checked; decision_log.md, 15 October 2026 |
| 2026-10-15 | 0.6 | Change of meaning: the sensor evidence grade research_only splits into research_demonstrated (a study the sources cite measured the indicator's own measure in cattle) and theoretically_measurable (only proposed, shown in another species or setting, or a substitute measure), both 1 point; none is defined as nothing in the two sources as of their dates | Kevin's change request of 7 October 2026 and the second of the three further points from the sense check in the decision_log entry of the same day; decision_log.md, 15 October 2026 |
| 2026-10-16 | 0.7 | Change of meaning: a second sensor grade, evidence since 2021 (rule 4.11), with a new table evidence_since_2021.csv and three new columns in sensor_coverage.csv; the score and Kevin's list 1 use the stronger of the two grades. Two points are provisional pending Kevin: studies one step through a review count, and tests involving the maker count as validated with the involvement recorded | Kevin's change request of 7 October 2026 (evidence update and vendor check) and Manisha's decisions of 16 October 2026; decision_log.md, 16 October 2026 |
| 2026-10-17 | 0.7.1 | Rule 4.11 made exact after the audit, no row's result changed: an unsure grade since 2021 makes a row unsure only when the 2021 grade is none; a measure computed from repeated values (I058) stays unsure on a test of single values, as on I006; a test report from an independent test body named on a maker's page (ICAR) is an admitted source; the one step point is marked provisional in the rule itself. Section 3 allows not_applicable for authors_independent on a maker page, and an empty since_2021_evidence where the grade rests only on a review's proposal | Audit of 17 October 2026; decision_log.md, 17 October 2026 |
| 2026-10-17 | 0.8 | Change of meaning: the rows come from two sides. New rule 4.12 adds 23 sensor side rows (listed_by plf_only, I060 to I082), one per parameter class named in the Stygar list's aims and covered by no protocol row; rule 4.13 adds the column welfare_state; rule 4.14 adds column 1, welfare_relevance, with its evidence; indicators.csv gains plf_parameter, welfare_state, welfare_relevance and welfare_relevance_evidence. Section 6 also reads Kevin's lists per welfare state. The score and the list rules are unchanged | Kevin's change request of 7 October 2026 and its four amendments; Manisha's decisions of 17 October 2026; decision_log.md, 17 October 2026 |
| 2026-10-17 | 0.8.1 | After the audit of efefe44. Rule 4.13 made exact, as it was applied: a sensor side row takes an EFSA heading only when the parameter itself is that condition. Rule 4.12 says a single calf aim among a class's cow aims stays in the class and the row is read for adult cows. Rule 4.14 says which sources Kevin's change request names and that using the three documents in full was Manisha's decision; its example uses I077. Section 2 says how measure_type is read on a sensor side row and aligns the welfare_relevance wording with rule 4.14; section 6 says when a state is Unclear exactly as build_output.py computes it; section 7 counts brought up to date | Audit of efefe44; decision_log.md, 17 October 2026, audit corrections |
| 2026-10-17 | 0.8.2 | Wording only, no change of meaning: rule 4.12 says the milk feeders' aims name milk feeding, not calves; the section 3 headings name the rows, column (a) and column (c); section 7 counts twelve rows unsure since 2021, adding I075 | Confirmation audit of ef45bf5; decision_log.md, 17 October 2026, second round of corrections |
| 2026-10-17 | 0.8.3 | Change of meaning: rule 4 of rule 4.8 says a condition that is only the practice the indicator itself measures does not limit a requirement, which writes down how the FARM_v5 row of I051 has been read since 8 October and makes the RSPCA_Assured row of I082 required. Rule 4.12 also names the product names that call the milk feeders calf feeders | Final confirmation audit of f924ad2; Manisha's decision of 17 October 2026; decision_log.md, 17 October 2026 |
| 2026-11-05 | 0.9 | Changes of meaning. The score of section 5 is replaced by the priority list: a gate on column 1 (no_welfare_validation and not_welfare_relevant rows leave it, to a sheet of their own), rows grouped by welfare state, states ranked by validity of the best test, then device, then manual burden, then id, and a kind of ask (World A, accept or adopt; B; C; or Unclear) per state. No impact tier, because EFSA does not rank its welfare consequences. Named by FARM is no longer a factor (it counted FARM twice) and is kept as a record; vendor count and the number of schemes requiring a row are no longer keys. Rule 4.9: sensitivity and specificity are a validity flag with no penalty where EFSA does not rate, and feasibility is read as manual burden. Rule 4.11: the two provisional points are confirmed, and a test the maker was involved in counts, flagged, unless the written conflict test finds a clear conflict of interest or a flaw arising from one. Rule 4.13: the Absence of disease rows take their own Welfare Quality measure as their state, and I057 joins Mastitis. Rule 4.14: column 1 is the gate. New rules 4.15 (validity of the best test, against Stygar's high performance bar) and 4.16 (what products do with the signal), with five new columns in sensor_coverage.csv and their codes in sections 2 and 3. Factor numbers are dropped from the headings of rules 4.2 and 4.4 to 4.7. Counts in sections 5 to 7 brought up to date | Kevin's review of November 2026 (kevin_slack_review_2026-11.md); Manisha's approval of the pre-flight on 5 November 2026 and her decisions of the same day on the state split and on reading a maker's page for signal purpose; decision_log.md, 5 November 2026 |
| 2026-11-06 | 0.9.1 | Changes of meaning, after the audit of d4b63fa and Manisha's decisions of 6 November 2026. Rule 4.15 applies Stygar's test in full: every statistic of a covered kind the study reports, in every setting, must meet it, with R squared above 0.81 (Stygar page 4), the intercept and slope tests and the Bland–Altman criterion; not_graded also covers a study whose full results are not on disk. Section 5 gains the kind of ask Unclear on schemes, for a state with a Tested or Claimed row, no required row and an unsure scheme row. Rule 4.16: unclear also where whether any product measures the row is open. Rule 4.11: Kevin's answer was for a study the maker funded, and the rule applies it to any part a maker took; a study that fails can still be read for another grade. Rule 4.13 says why the procedures criterion is not split. Section 5 records Welfare Quality's ordering of criteria within each principle and why it is not an impact tier. Wording: the points that come from the Claude summary Kevin forwarded are attributed to it, not to Kevin; leftovers of the score are removed; counts brought up to date | Five part audit of d4b63fa; Manisha's decisions of 6 November 2026; decision_log.md, 6 November 2026 |
| 2026-11-06 | 0.9.2 | Changes of meaning, after the confirmation audit of 06117c1. Rule 4.15: where several counted tests bear on a row, the column takes the best, as Stygar's column does; a report whose regression does not say which values are on which axes cannot be graded (not_graded, with an open question), replacing the reading of 0.9.1 that filed such a regression under Bland–Altman; I021 and I025 become not_graded since 2021. The validity label for not_graded and the kind of ask label are written as the Excel file shows them. Rule 4.14 quotes Kevin's own comment on the gate. Wording only elsewhere | Confirmation audit of 06117c1; decision_log.md, 6 November 2026, second entry |
| 2026-11-09 | 0.9.3 | Wording and clarification, no value or rank changed. Section 2 definitions of the performance codes state the take the best rule and the unnamed axes case; the kind of ask labels are marked as shortened; the three worlds are attributed to the Claude summary in section 2; rule 4.15 says one product's settings and versions within a study are read together; the rule 4.15 example gives I060's five counted tests. The 0.9.2 row's reading of 0.9.1 on regressions of differences is the sentence on them in rule 4.15 at 0.9.1, which the 0.9.1 row did not name | Second confirmation audit of c181006; decision_log.md, 9 November 2026 |
| 2026-11-09 | 0.9.4 | Wording and clarification, no value or rank changed. Rule 4.16 says a maker's page since 2021 is not read for a row the Stygar list names, as it has been applied. The label for kind of ask C says what it rests on, the 2021 product descriptions, and no longer says the hardware is on farms | Audit of e535326; decision_log.md, 9 November 2026, third entry |
