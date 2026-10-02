# Rules

Version 0.3.2, 3 October 2026. First fixed as version 0.1 on 25 September 2026, before any sensor row was graded; the indicator and product tables were copied from plf-audit. Every change is dated in the [change log](#8-change-log) at the end.

## 1. In one page

This project answers item 13 on Kevin Xia's Top 30 list for dairy cows ([his text](../1_sources/kevin_item_13.md)). It sets three things side by side: validated welfare indicators, what commercial farm sensors measure, and what certification schemes require and how they check it. The research sits in four tables in this folder. This file is the rulebook for those tables. For every column it says what the column means, which rule fills it, and which source the value is read from.

The three part question, indicators that are (a) measurable by AI, (b) acceptable to industry and (c) covered by existing sensors or certification schemes, comes from Kevin's proposal on the call of 22 September ([automated notes](../1_sources/kevin_call_2026-09-22.md)), as written up in Manisha's smaller scope analysis, which Kevin quotes in his Slack reply of 25 September ([his words](../1_sources/kevin_slack_2026-09-25.md)). In that reply he calls industry acceptability, and coverage by existing sensors and by existing certification schemes, soft factors that make adoption easier rather than hard requirements. So each factor is a graded column, every indicator stays in the table, and the rank is a stated rule of thumb that any reader can sort again by any single factor.

The answer itself is the Excel file [welfare_crosswalk_dairy.xlsx](../4_output/welfare_crosswalk_dairy.xlsx). Nothing in it is typed by hand. The script [build_output.py](../3_code/build_output.py) writes it from the four tables using the rules below.

How to use this file. If a word or a code puzzles you, look it up in section 2. If you want to know what a column holds, or what an empty cell means, see section 3. If you want to know why a cell has its value, find the rule in section 4, then open the page named in that row's where_to_check column and read it. Section 5 explains the score, section 6 defines Kevin's two lists, and section 7 says what happens when the rules cannot decide.

How this file changes. A rule changes only through a dated entry in [decision_log.md](decision_log.md) and a new row in the change log at the end of this file. A rewording keeps the meaning unless the decision log entry says the meaning changes. Older entries in the decision log use the file and column names of their day; its entry of 2 October 2026 on the reorganisation gives the old and new names.

## 2. Words used here

### Sources and the bodies behind them

| Word | Meaning |
|---|---|
| EFSA | The European Food Safety Authority. Its 2023 scientific opinion on the welfare of dairy cows (EFSA Journal 21(5):7993) is one of the two sources of indicators. |
| Welfare consequence | EFSA's name for a kind of welfare problem, such as Locomotory disorders or Mastitis. The EFSA indicators here belong to five of them. |
| ABM | Animal based measure: a measure taken on the animal itself, such as how it walks, rather than on its housing or on how the farm is run. EFSA's "ABM assessment tables" list these measures and rate each one. |
| Welfare Quality | The Welfare Quality assessment protocol for dairy cattle, version 3.2, February 2024: the second source of indicators. It is built in layers. Four principles (Good feeding, Good housing, Good health, Appropriate behaviour) are split into criteria, and each criterion is assessed by one or more measures. |
| Resource based, management based | Welfare Quality's labels for a measure of the housing or equipment (resource based) or of a farm practice (management based), as opposed to a measure taken on the animal. |
| Stygar 2021 | Stygar et al. 2021, Frontiers in Veterinary Science 8:634338, a review of sensor technologies for dairy cow welfare. They found 129 technologies on the market, of which 18 had been externally validated. |
| Stygar list, appendix | The spreadsheet that comes with Stygar 2021 ([stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), sheet "Appendix table 1"). It lists the 129 products with their name, provider, web link, sensor type, AIM, country and a column on validation studies. "The appendix" and "the Stygar list" mean the same thing. |
| AIM | The column of the Stygar list that holds a one line description of what each product does, as stated for that product. It is the only column searched when counting vendors. |
| Stygar Table 1, Table 2 | Table 1 (page 6) summarises the externally validated technologies and puts each study under independent validation or self validation. Table 2 (page 7) gives the results of the validation trials by measured trait, says whether each trial took place on a research farm or a commercial farm, and places each technology in a high performance or a lower performance column. |
| Study number | The number Stygar give a study in their reference list, for example 48. The tables call it a study number; older notes call it a reference number or ref. |
| Validated | In this repository the word has one narrow meaning: Stygar code at least one external validation study for that product on that trait. It never means more than that here. The one exception is the icar_validated column of products.csv, which means the product is on ICAR's list. |
| Maroto Molina 2020 | Maroto Molina et al. 2020, Journal of Dairy Research 87(S1). They go through the Welfare Quality measures and say which sensor technologies could provide each one. They give no rating of their own, so the rating column here is this project's coding of their text. |
| Substitute measure | Something Maroto Molina propose measuring in place of the protocol's own measure, for example water intake in place of the water point measures. |
| PLF | Precision livestock farming: sensors, cameras and data analysis used on farms. |
| FARM v5 | FARM Animal Care Version 5, the US dairy industry's own animal care programme, written by the National Milk Producers Federation. It is read twice: for the industry naming factor, and as one of the four schemes. |
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

**sensor_evidence** (sensor_coverage.csv): can a product on the market measure the indicator? The full rule is [rule 4.2](#42-sensor-evidence-factor-1).

| Value | Meaning | Label in the Excel file |
|---|---|---|
| validated_commercial | A product in the Stygar list measures the indicator, and Stygar code at least one external validation study for that product on that trait. | Tested |
| commercial_unvalidated | A product in the Stygar list states the indicator in its AIM, and no external study is coded. | Claimed |
| research_only | No product, but Maroto Molina identify research level technology or a substitute measure. | Research only |
| none | No product, and Maroto Molina say sensors cannot provide it or do not discuss it. | Nothing found |
| unsure | The sources do not settle it. See section 7. | Unclear |

**device_needed** (sensor_coverage.csv): the cheapest kind of equipment that would measure it, a stand in for cost and ease. The full rule is [rule 4.4](#44-device-needed-factor-2).

| Value | Meaning |
|---|---|
| routine_data | Nothing extra: the value is already collected by the milking system or in herd or farm records. |
| farm_fixed | One device per farm or barn, such as a camera, a walkover scale or a trough meter. |
| animal_mounted | One device per animal, such as a collar, ear tag, leg tag or bolus. |
| sample_or_procedure | A blood or rumen sample, or a scoring done by a person, when the method cited for the row is of that kind. |
| none | No technology is named for the row by Stygar or Maroto Molina. |
| unsure | The rules do not settle it. See section 7. |

**measure_type** (indicators.csv): what kind of thing the indicator measures, in the source's own terms. Every EFSA measure here is animal based, because the EFSA rows come from its ABM tables. For Welfare Quality the label is read from the Scope line of each measure.

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

**listed_by** (indicators.csv): which of the two indicator sources lists the indicator.

| Value | Meaning |
|---|---|
| joined | EFSA and Welfare Quality share the row. |
| efsa_only | Only EFSA lists it. |
| wq_only | Only Welfare Quality lists it. |

**how_checked** (crosswalk.csv): how a scheme checks a requirement it sets. The full rule is [rule 4.7](#47-schemes-requiring-it-factor-5).

| Value | Meaning |
|---|---|
| visual_inspection | An assessor observes the animals or scores them. |
| records_review | The assessor checks farm records. |
| sensor_accepted | The scheme text accepts sensor or automated data for the measure. |
| unspecified | The scheme requires it but does not say how it is checked. |
| unsure | The scheme requires it, but its text does not settle how it is checked. It needs a line in open_questions.md (section 7). |

**farm_naming** (crosswalk.csv, FARM v5 rows only): does the industry programme name the indicator? The full rule is [rule 4.6](#46-named-by-farm-factor-4).

| Value | Meaning |
|---|---|
| named_with_threshold | A FARM requirement names the measure and sets a number. |
| named | A FARM requirement names the measure, with no number. |
| related_resource | A FARM requirement about housing, equipment or practice bears on the indicator but does not name the measure. |
| not_named | FARM does not name it. |
| unsure | The rules do not settle whether FARM names it. It scores 0 points and needs a line in open_questions.md (section 7). |

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
| Not yet known | Shown in the Excel file for Kevin's lists while not all four schemes have been read for an indicator and none read so far settles the answer: on list 1 for rows graded Tested or Claimed that no scheme read so far requires, on list 2 for rows that no scheme read so far requires and checks by hand. See section 6. |
| Unclear | Shown in the Excel file for a cell coded unsure, and on Kevin's lists where an unsure cell decides the answer (section 6). |
| Ease of adoption score | A number from 0 to 15 used only to sort the table. Not a welfare judgement and not a recommendation. See section 5. |
| Provisional rank | The rank while some rows are incomplete. The Excel file says how many. |
| BCS | Body condition score, a score of how much fat a cow carries (EFSA PDF page 76, Stygar page 4, Maroto Molina page 2). It is also part of product names such as DeLaval BCS. |
| BHB | Beta hydroxybutyrate (EFSA's list of abbreviations, PDF page 123). EFSA treats an elevated level as a sign of subclinical ketosis (PDF page 74). |
| CMT | California mastitis test. Stygar Table 2, page 7, lists the Lely on line California mastitis test (study 43) under mastitis detection. |
| DHIA | Dairy Herd Improvement Association, whose milk fat, protein and lactose observations Stygar reference 25 compares with a real time milk analyser (title on PDF page 13). |
| LDH | A level analysed in milk, named with progesterone and BHB in the aim of Herd Navigator in the Stygar list. No document in 1_sources spells it out. |
| NIRS | Near infrared spectroscopy. Maroto Molina, page 3, say milk somatic cell count can be monitored by it, even for the individual cow in milking robots. |
| SARA | Subacute ruminal acidosis, one of the metabolic disorders in EFSA Table 46 (PDF pages 75 and 76). |
| SCC | Somatic cell count, the number of cells per ml of milk; an elevated count is a sign of an inflammatory response such as mastitis (EFSA PDF page 42). Bulk milk SCC, also written bulk tank SCC, is the count for the milk in the farm's bulk tank (EFSA Table 27, PDF page 43). |

## 3. What each table holds

Four tables, each a CSV file (a plain spreadsheet file) with fixed column names in a fixed order. [check_tables.py](../3_code/check_tables.py) checks the columns, the codes and the links between tables after every edit. It checks that the tables are well formed and agree with each other; it does not check that a value is true. That is the job of the auditor and of a person reading the source page.

### indicators.csv: the welfare indicators (column 1 of the crosswalk)

One row per indicator. There are 58 rows. The table was copied from the predecessor project, plf-audit, and corrected since; the rule for which indicators belong is [rule 4.1](#41-which-indicators-are-in-the-table).

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | The identifier, I001 onwards, used by the other tables. A removed row's number is not reused, so I042 is missing. | Never. |
| efsa_welfare_consequence | The EFSA welfare consequence. | On a Welfare Quality only row. |
| efsa_measure | The EFSA animal based measure. | On a Welfare Quality only row. |
| wq_principle, wq_criterion | The Welfare Quality principle and criterion. | On an EFSA only row. |
| wq_measure | The Welfare Quality measure. | On an EFSA only row, and on thermal comfort (I039), the one row where Welfare Quality defines no measure. |
| measure_type | animal_based, resource_based, management_based or none (section 2). | Never. |
| maroto_molina_technology | What Maroto Molina 2020 identify for the measure, in words. | Never; where they do not discuss it, the cell says so. |
| maroto_molina_rating | yes, partial, no or not_covered ([rule 4.3](#43-maroto-molina-rating)). | Never. |
| notes | The source table, the basis for joining an EFSA and a Welfare Quality measure, and open questions. | May be empty when there is nothing to add. |
| listed_by | joined, efsa_only or wq_only. check_tables.py confirms it follows from which source columns are filled. | Never. |

### products.csv: the profiled sensor products

One row per product. There are 20: 17 in the Stygar list, which carry Stygar's validation finding, and 3 from the ICAR list (P018 to P020), which are not in the Stygar list. Copied from the predecessor project with later corrections recorded in the decision log. The full Stygar list of 129 is not copied here; it is read directly from the spreadsheet.

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
| link | The web link from Stygar 2021, not checked again since. | When the product is not in the Stygar list. |
| notes | Where the row comes from, and the study numbers behind the validation value. | Never. |

### sensor_coverage.csv: what sensors measure (column 2 of the crosswalk)

One row per indicator. There are 40 rows so far, I001 to I040. An indicator with no row here has not yet been checked for sensors, and the Excel file shows it as not yet checked.

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | An id from indicators.csv. | Never. |
| sensor_evidence | The grade for factor 1 ([rule 4.2](#42-sensor-evidence-factor-1)). | Never. |
| products | Every product the row cites, separated by spaces. A product in products.csv is cited by its P number; a product in the Stygar list but not in products.csv is cited as appendix:Provider\|Name, for example appendix:Afimilk\|AfiLab. | When the row cites no product. It must be filled for the two commercial grades. |
| validated_products | Only the products with a validation study coded by Stygar for the row's trait, as Provider\|Name from the Stygar list, separated by semicolons. | On every row that is not validated_commercial. It must be filled on validated_commercial rows. |
| validated_trait | The Stygar Table 2 trait, or the AIM wording, that matched. | When nothing matched. |
| study_numbers | The validation studies, by Stygar's study number, separated by spaces. | When no study applies. It must be filled on validated_commercial rows. |
| maroto_molina_rating | Copied from indicators.csv for the same row. check_tables.py confirms the copy. | Never. |
| device_needed | The class for factor 2 ([rule 4.4](#44-device-needed-factor-2)). | Never. |
| vendors_naming_it | A whole number for factor 3 ([rule 4.5](#45-vendors-naming-it-factor-3)). check_tables.py confirms it equals a fresh count. | Never. |
| search_words | The search words, separated by semicolons. | Never. |
| where_to_check | Where each value was read: document, page, table, row. | Never. |
| reasoning | Alternatives, the other technologies, and the candidate readings on unsure rows. | May be empty when there is nothing to add. |

### crosswalk.csv: what schemes require (column 3 of the crosswalk)

One row per indicator per scheme. An indicator that no scheme requires still gets four rows, by rule. check_tables.py does not check that every indicator has all four rows, so the person filling the table checks that the row count is four times the number of indicators. build_output.py counts an indicator's schemes as read in full only when all four of its rows are present; a single row that quotes a requirement already settles list 1 as No, and a requirement checked by hand already settles list 2 as Yes. The table has no rows yet: the schemes have not been read.

| Column | What it holds | When empty |
|---|---|---|
| indicator_id | An id from indicators.csv. | Never. |
| scheme | RSPCA_Assured, FARM_v5, GAP_dairy or Certified_Humane. | Never. |
| requirement_quote | The requirement that names the indicator, quoted exactly ([rule 4.8](#48-when-a-scheme-requirement-names-an-indicator)). | When the scheme does not require the indicator. |
| section, page | Where the requirement is in the scheme document. | May be empty when requirement_quote is empty. Both must be filled when it is filled. |
| number_in_requirement | Any number the requirement sets, exactly as written. | When the requirement sets no number. It must be filled when farm_naming is named_with_threshold. |
| how_checked | How the scheme checks it ([rule 4.7](#47-schemes-requiring-it-factor-5)). | Exactly when requirement_quote is empty. |
| farm_naming | The value for factor 4 ([rule 4.6](#46-named-by-farm-factor-4)). | On every row that is not FARM_v5. It must be filled on every FARM_v5 row. |
| reasoning | Related resource requirements, the reasoning from a scheme's justification document, and alternatives. | May be empty when there is nothing to add. |

check_tables.py also refuses a FARM_v5 row that quotes a requirement but is not coded named, named_with_threshold or unsure, and a FARM_v5 row coded named or named_with_threshold that quotes nothing.

## 4. The rules

### 4.1 Which indicators are in the table

**Question.** Which welfare indicators are in scope, and how are the two sources joined?

**Rule.** One row per indicator in [indicators.csv](indicators.csv). An indicator is a measure from the EFSA 2023 dairy cow opinion or the Welfare Quality dairy protocol version 3.2, chosen as follows.

The EFSA rows are every animal based measure in EFSA's ABM assessment tables for the five welfare consequences: Tables 16, 17, 18, 27, 31, 32, 33, 42 and 46, which give feasibility, sensitivity and specificity for each measure. Other EFSA tables are out of scope. These are Table 15 and Table 26, which list measures used in the literature to assess lameness and mastitis; the farm level Tables 51 to 59 of the risk based scheme; and Appendix K, whose Table K.1 lists the measures supplied to the expert elicitation.

The Welfare Quality rows are every measure in the version 3.2 protocol overview (PDF page 22, printed page 21). Most are animal based, and some are resource or management based, as the Scope line of each measure says. Three adjustments are made. The two lameness measures, loose housed and tied, share row I001. The one integument alterations measure is split into I004 and I005 to follow EFSA's hock and knee measures. Thermal comfort, a criterion for which the protocol defines no measure, has its own row, I039.

That gives 32 EFSA rows and 32 Welfare Quality rows, 6 of them joined, so 58 rows in all: 26 efsa_only, 26 wq_only and 6 joined. Each row carries its listed_by value: joined when EFSA and Welfare Quality share the row, efsa_only when only EFSA lists it, wq_only when only Welfare Quality lists it. It is shown so that a reader who takes Welfare Quality alone as the validated set can leave out the 26 efsa_only rows without the table changing.

**Example.** I001 is joined: EFSA's Gait assessment, under Locomotory disorders, shares the row with Welfare Quality's Lameness. Its notes say that EFSA Table 16 defines the 3 point scale citing Welfare Quality 2009, and that the row merges the two Welfare Quality lameness measures. I039, thermal comfort, is wq_only with measure_type none.

**How to check.** Open the EFSA opinion at the nine tables named above and the Welfare Quality protocol at PDF page 22, and compare their measures with the rows. check_tables.py confirms that each listed_by value follows from which source columns are filled. The current counts are on the Read me sheet of the Excel file.

### 4.2 Sensor evidence (factor 1)

**Question.** Does a commercial product measure the indicator, and how well has that been checked?

**Rule.** The value is read from Stygar 2021 (Table 1 on page 6 for the validated products and their study numbers, Table 2 on page 7 for the traits each was validated on, and the Stygar list for the 129 products and their stated aims), from Maroto Molina 2020 for measures with no product, and from [products.csv](products.csv). The five grades:

validated_commercial: a product in the Stygar list measures the indicator and Stygar code at least one external validation study for that product on that trait. The row names the products and the study numbers.

commercial_unvalidated: a product in the Stygar list states the indicator in its aim, and no external study is coded. The row names the products.

research_only: no product, but Maroto Molina identify research level technology or a substitute measure, whatever feasibility rating they give it.

none: no product, and Maroto Molina say sensors cannot provide it or do not discuss it.

unsure: the sources do not settle it. The candidate reading goes in the reasoning column and in [open_questions.md](open_questions.md).

When a validated trait counts. A trait validated by Stygar counts for an indicator only when Stygar's trait name and the indicator name are the same measure, or where Stygar's Table 2 category names the indicator directly, for example locomotion score for lameness. Stygar's trait names are not always word for word the indicator's. For EFSA's lying time, I012, the trait is "Non-active behavior (lying, lying and standing)", and the decision log entry of 29 September records that it maps to lying time. That trait covers lying, and lying and standing together, and Table 2 does not say which trial measured which. The same trait does not settle lying bouts, I013, which stays unsure (section 7). Rumination is not lameness, and activity is not oestrus. A product validated on one trait does not earn a grade on another.

Products and validated products. The products column names every product the row cites, whether or not it stands behind the grade. The validated_products column names only the products with a validation study coded by Stygar for the row's trait.

**Example.** I023, subclinical ketosis by body condition scoring, is validated_commercial. Its product is P009, the DeLaval body condition scoring camera, its study number is 48, and its validated_trait reads "Body condition scoring, Table 2 page 7, commercial farm, lower performance column". The products rule shows on I027, rumen pH by bolus: the row cites five products, but validated_products names only `eCow UK|eBolus`, the one with studies 50 and 51. The same measure rule shows on I030, water provision, which is research_only. Maroto Molina propose individual water intake as a substitute, and a product validated for water intake exists (study 45), but the Welfare Quality measure is the water point itself, so the grade does not credit it.

**How to check.** Open [stygar_2021.pdf](../1_sources/stygar_2021.pdf) at Table 1 (page 6) and Table 2 (page 7) and find the study numbers the row gives. Open the Stygar list, find each product, and read its AIM. The row's where_to_check column names every page.

### 4.3 Maroto Molina rating

**Question.** What does Maroto Molina 2020 say about whether sensors can provide the measure?

**Rule.** maroto_molina_rating in indicators.csv, copied into sensor_coverage.csv, codes what Maroto Molina et al. 2020 say about each measure. They give no rating of their own, so the value is this project's coding of their text. yes: they identify commercially available technology. This is read literally: yes only where the passage says the technology is commercially available or in use on commercial farms. A technology named without those words, for example one cited from a research study, is partial. partial: they name research level technology, technology that needs adaptation, or a substitute measure they propose. no: they say sensors cannot provide it. not_covered: the paper does not discuss the measure, or discusses it but names no technology for it. In that case the notes say that they discuss it, and where.

**Example.** Maroto Molina page 3 says mortality, dystocia and downer cows are Welfare Quality measures based on farmer records, and names calving prediction systems for dystocia only. So I049, dystocia, is partial, a substitute. I048, mortality, is not_covered, and its notes say the measure is discussed on page 3 and no technology is named. I051, disbudding or dehorning, is no. The literal reading of yes shows on two rows. I023, body condition, is yes: page 2 says the Welfare Quality scoring is less precise than what "commercially available technologies" can provide, and names the DeLaval BCS camera. I012, lying time, is partial: page 3 says pedometers and accelerometers have been used for monitoring lying behaviour and can provide lying time, citing research studies, but does not say they are commercially available.

**How to check.** Open maroto_molina_2020.pdf (link only, see [1_sources/README.md](../1_sources/README.md)) at the page given in the row's notes or maroto_molina_technology column. check_tables.py confirms that the copy in sensor_coverage.csv matches indicators.csv.

### 4.4 Device needed (factor 2)

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

The unsure fill. On a row whose sensor evidence is unsure, the class is filled from the cheapest commercial candidate so the factor stays usable, and the reasoning says so.

What commercial means here. Throughout this factor, commercial means a product in the Stygar list whose aim states the measurement, or on an unsure row the candidate measurement: the same test factor 1 applies. A product in the Stygar list of the same technology type but with a different aim does not count. Neither does a technology a source describes as in commercial use but which has no row in the Stygar list. The reasoning names both kinds where they exist.

Lower classes are cheaper to adopt. The table shows the class; it does not put a price on anything.

**Example.** I020, clinical ketosis, is unsure on sensor evidence but routine_data on device needed. EFSA Table 46 (PDF page 75) defines the measure as the "Incidence rate of clinical ketosis (estimated from veterinary diagnoses, farm records or national databases)", so the records rule applies ahead of the unsure fill. The reasoning names AfiMilk MPC, an inline milk analyser, as the added device alternative. I006, clinical mastitis cases, shows where the records rule stops. EFSA Table 27 (PDF page 43) defines it as the "Incidence rate of clinical mastitis", and names vet or farm records only in its feasibility line, so the definition does not take the value from records. The unsure fill gives the class: the candidates, Lely MQC-C and the other products whose aims name mastitis or udder health, are milk quality sensors and thermal cameras, so I006 is farm_fixed. I039, thermal comfort, shows the meaning of commercial: it is animal_mounted, from the ten products whose aims name temperature: boluses, an ear tag and a collar. The thermal cameras in the Stygar list do not set the class, because their aims name udder health, mastitis, inflammation, fever or lameness, not temperature or thermal comfort.

**How to check.** Read the indicator's definition at the page named in where_to_check. Then read the reasoning column, which names the technologies and their classes, and check each candidate's AIM in the Stygar list.

### 4.5 Vendors naming it (factor 3)

**Question.** How many products on the market say they measure it?

**Rule.** The number of products among the 129 in the Stygar list whose stated aim names the measurement. It is counted by [count_vendors.py](../3_code/count_vendors.py) from the search words in the search_words column of sensor_coverage.csv, matched without regard to case against the AIM column of the Stygar list. The search words for each indicator are written into the row so the count can be reproduced and challenged. The reading: what many vendors already sell is what industry already buys, which is the visible form of Kevin's "won't strongly object" ([his words](../1_sources/kevin_slack_2026-09-25.md)).

**Example.** I027, rumen pH by bolus, has the search words "rumen ph; ph," and a count of 5: eBolus, ET912 Fofia, Moow Rumen bolus, smaXtec basic and VitalHerd. Two other bolus aims name rumen acidosis monitoring, which is the condition, not the pH measurement, and the search words do not match them.

**How to check.** Open [stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), select column E (AIM), search for each word of the row, and count the products that match at least one word. Or run `python 3_code/count_vendors.py I027`, which lists the matching products and changes nothing. check_tables.py confirms every stored count equals a fresh count.

### 4.6 Named by FARM (factor 4)

**Question.** Does the industry's own programme name the indicator?

**Rule.** Whether the indicator is named in a requirement of the industry authored programme, FARM Animal Care Version 5 for dairy, written by the National Milk Producers Federation. The values are named_with_threshold (the requirement names the measure and sets a number), named (it names the measure, with no number), related_resource (a requirement about housing, equipment or practice that bears on the indicator but does not name the measure), not_named, and unsure where the rules do not settle it. An unsure cell scores 0 points and needs a line in [open_questions.md](open_questions.md), like any unsure cell (section 7). The requirement is quoted with section and page in [crosswalk.csv](crosswalk.csv). This is a factor, not a gate.

**Example.** No crosswalk row has been filled yet. The worked example in rule 4.8 is the one to follow: FARM Animal Care v5, page 149, "Severe Lameness: 5% or less of the lactating cows observed score 3 on the FARM Locomotion Scorecard." That names lameness with a number, so it is named_with_threshold.

**How to check.** Open the FARM v5 reference manual at the section and page given in the row and read the quoted requirement. Then apply rule 4.8.

### 4.7 Schemes requiring it (factor 5)

**Question.** How many of the four schemes require the indicator, and how does each one check it?

**Rule.** The count of the four schemes that require the indicator, and how each audits it. The schemes are RSPCA Assured dairy cattle April 2026, FARM v5, Global Animal Partnership dairy v2.0 and Certified Humane dairy Edition 23. how_checked, one per scheme row, is visual_inspection (an assessor observes animals or scores them), records_review (the assessor checks farm records), sensor_accepted (the scheme text accepts sensor or automated data for the measure), unspecified (the scheme requires it but does not say how it is checked), or unsure (the scheme requires it, but its text does not settle how it is checked). An unsure cell needs a line in [open_questions.md](open_questions.md), like any unsure cell (section 7). This is a factor, not a gate.

**Example.** No crosswalk row has been filled yet. The worked example in rule 4.8 is RSPCA Assured standard H 3.5, which requires mobility scoring and has the results recorded, so the assessor checks the recorded scores: records_review.

**How to check.** Open each scheme document at the section and page given in the row, read the requirement, and see what it says about how it is checked.

### 4.8 When a scheme requirement names an indicator

**Question.** When does a requirement count as requiring the indicator, rather than just touching on it?

**Rule.** The requirement must name the animal based measure or a direct synonym. A requirement about housing, resources or practice that would affect the measure does not count as naming it. It is recorded as related_resource in the reasoning column so the reader can see it.

**Examples.** These three worked examples are part of the rule. The two quotations were checked against the scheme documents in 1_sources.

First, RSPCA Assured dairy cattle 2026, H 3.5, printed page 46: "All lactating cattle must be mobility scored at least four times a year by a mobility scorer registered with the Register of Mobility Scorers (RoMS) and the results recorded in the VHWP." That names lameness (Welfare Quality lameness, EFSA gait assessment, row I001). how_checked is records_review, since the assessor checks the recorded scores.

Second, "cubicle dimensions must be at least X" is related_resource for the comfort around resting measures. It is not a naming of time needed to lie down.

Third, FARM Animal Care v5, page 149: "Severe Lameness: 5% or less of the lactating cows observed score 3 on the FARM Locomotion Scorecard." That names lameness with a numeric threshold, named_with_threshold. The same page sets "Moderate Lameness: 15% or less" at score 2.

**How to check.** Read the quoted requirement in the row against the page. Ask whether it names the measure itself or a synonym, or only the housing, resource or practice around it.

## 5. The score

Each factor is turned into 0 to 3 points as follows, and the five are added to a score from 0 to 15.

| Factor | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| Sensor evidence | validated_commercial | commercial_unvalidated | research_only | none or unsure |
| Device needed | routine_data | farm_fixed | animal_mounted | sample_or_procedure, none or unsure |
| Vendors naming it | 10 or more products | 3 to 9 products | 1 or 2 products | none |
| Named by FARM | named_with_threshold | named | related_resource | not_named or unsure |
| Schemes requiring it | all four schemes | two or three | one | none |

The sum is a rule of thumb, and it is labelled as one in every output. It is not a welfare judgement and not a recommendation; it is a sort order. Every factor stays visible in the table, so a reader can sort again by any one of them. This mapping is the only place a decision log entry can change the ranking. Rows with the same score are sorted by indicator id.

The five factors are scored independently of each other. So one row can earn sensor evidence points from a tested product that is an added device, and device needed points because the value is already in records. I021 and I025 work this way: the sensor points come from AfiLab, an inline milk analyser fitted at the milking point, and the device points from routine milk recording, which EFSA's definition names.

Tested products and products whose description names it are separate columns. A product can be tested for a measure without its own description naming it, and the reverse. On I012, Track a))) Cow and RumiWatch were tested for lying, but their descriptions do not contain the search words, so they are among the tested products and not among the products that name it.

**Example.** I023, body condition scoring, scores 3 for a validated product, 2 for a farm camera, 2 for three vendors naming it, 0 for FARM and 0 for schemes: 7 in all. The last two parts are 0 because the schemes have not been read yet, so its rank is provisional.

**How to check.** The Answer sheet of the Excel file shows each row's five parts in the order sensor + device + vendors + FARM + schemes, next to the sum.

## 6. Kevin's two lists

Kevin's item 13 names two valuable cells: "indicators already instrumented but not required, and indicators required but manually audited" ([his text](../1_sources/kevin_item_13.md)). Both lists are computed by build_output.py from the same rows as the ranked Answer sheet.

**List 1, instrumented but not required.** Sensor evidence is validated_commercial or commercial_unvalidated, and the schemes requiring it number 0. Yes is reported for an indicator only once all four schemes have been read for it, because before that a count of 0 means not yet read rather than not required. No is final as soon as one scheme is read and requires it, whatever the sensor evidence. An indicator whose sensor evidence is unsure shows Unclear, unless a scheme already requires it, because it could join the list once its question is settled.

**List 2, required but manually audited.** Kevin's "indicators required but manually audited". Per scheme row, the requirement is present and the scheme checks it by inspection or by records review (how_checked visual_inspection or records_review), not by accepting sensor data. The sensor evidence for the indicator is shown beside it. This replaces the earlier, narrower filter, which also required sensor evidence validated_commercial. When a scheme requires the indicator and its how_checked is unsure, the list shows Unclear, unless another scheme that requires it checks it by inspection or records review, in which case the indicator is on the list.

On 3 October 2026 the Read me sheet shows 0 confirmed in either list, because no scheme has been read. On list 1, 8 indicators are graded Tested or Claimed in column (a) and wait for the scheme check, and 5 more show Unclear because their sensor evidence is unsure.

## 7. When the rules do not decide: unsure

Any cell the rules above do not settle is coded unsure. The candidate readings go in the row's reasoning column, and a line in [open_questions.md](open_questions.md) gives the indicator, the factor and the candidates. It is resolved only by tightening the rule that failed, with a dated decision log entry. Otherwise it stays unsure in the published table, and the note says how many rows are unsure per factor. On sensor evidence, device needed and named by FARM, an unsure cell scores 0 points (section 5). An unsure how_checked cell still counts its scheme as requiring the indicator, since the requirement is quoted, and shows Unclear on Kevin's list 2 (section 6).

On 3 October 2026, five rows are unsure on sensor evidence (I006, I009, I013, I020 and I039), none is unsure on device needed, and crosswalk.csv has no rows yet.

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
| 2026-10-03 | 0.3.2 | Change of meaning, narrower hold back on list 1 (section 6): an indicator is No as soon as one scheme is read and requires it, whatever its sensor evidence, since its count of requiring schemes can then never be 0; before, every list 1 answer waited for all four schemes, and unsure rows showed Unclear. Yes still waits for all four schemes. The Not yet known glossary entry and the crosswalk.csv note were brought in line. | Third and fourth confirmation audits, 3 October 2026; decision_log.md entries of 3 October 2026 on Kevin's files and on the fourth confirmation audit |
