# Sources

This folder lists the documents the research reads, with a link and a fingerprint for each; two of them are stored here and the rest are link only. Every fact in the tables in [`2_research`](../2_research) comes from one of them. Papers read only as abstracts in the literature check ([`2_research/literature_check_2026-09-29.md`](../2_research/literature_check_2026-09-29.md)), and candidate sources named in [`2_research/decision_log.md`](../2_research/decision_log.md), are cited by DOI and are not in the manifest; each gets a row here before any table cell, rule or count rests on it. The list of documents, with the web address each file came from, is [`manifest.csv`](manifest.csv). This page explains that list in plain words.

The project builds a table with three columns. Column 1 is the welfare indicators: the signs of a cow's welfare that scientists have agreed on, such as lameness or lying time. Column 2 is the sensors: whether a commercial device measures each indicator. Column 3 is the certification schemes: whether a farm assurance label requires the indicator, and how its auditors check it. Each document below is tied to one of these columns, or to the question itself.

## Why only two of the source documents are in the repository

There are 15 documents in the manifest. Two of them are stored in this repository: the Stygar 2021 paper and the spreadsheet published with it. The other thirteen are listed with a link and a fingerprint. For ten of them, a copy you download from the link gives the same fingerprint, which proves it is the identical document (see below); the FARM manual must be saved from a web browser. Three cannot be proved that way. Cambridge University Press stamps every download of the Maroto Molina paper with the date, the time and the downloader's IP address, so your copy will not match the fingerprint; the check instead compares its text, with the stamp lines removed, against the text the research read. The ICAR web page and the Wieck essay are snapshots: a copy saved today will not match, and the check only confirms that a set phrase is still on the live page.

A licence is the owner's statement of what others may do with a document. Three licences matter here.

- **CC BY 4.0** (Creative Commons Attribution) lets anyone share the document as long as they credit the authors.
- **CC BY-ND 4.0** (Attribution, No Derivatives) lets anyone share it unchanged, with credit.
- **All rights reserved**, or no licence at all, means only the owner may republish it. A document that states no licence is treated the same way.

The Stygar paper is CC BY 4.0. Its spreadsheet has no licence line of its own; it was published alongside the CC BY 4.0 article, so it is treated as CC BY 4.0. Two other papers have open licences but are still not stored here. The Maroto Molina paper is CC BY 4.0, but every copy downloaded from Cambridge University Press is stamped on each page with the date, the time and the downloader's IP address (an internet address that can identify who downloaded it), so the downloaded copy is kept out of a public repository. The EFSA opinion is CC BY-ND 4.0 for EFSA's own content, but six of its figures belong to other owners and are not covered by that licence, so the file is not republished whole. The other eleven are the Welfare Quality protocol, the ICAR web page and its three test reports, the five certification documents and one essay, whose owners reserve their rights or state no licence, which is treated the same way. Each table below says which is which.

## How to get a missing document

Open the link in the last column of the tables below. It is the exact address the original file came from, also given in the `url` column of [`manifest.csv`](manifest.csv). Save the file into this folder under the file name given in the first column. The name matters, because the scripts look for that exact name.

One site, the FARM programme, refuses downloads made by a program. Open its link in an ordinary web browser and save the file from there.

## How to prove your copy is the same document

Each row in the manifest records a fingerprint of the file. The fingerprint (a SHA256 hash) is a long code worked out from every byte of the file. If a single character in the file changes, the fingerprint changes completely. So if your copy gives the same fingerprint, it is the identical document the research read.

To check, run this from the top folder of the repository:

```
python 3_code/check_sources.py --local
```

It works out the fingerprint of every file in this folder and compares it with the manifest. A document you have not downloaded is reported as `absent`, which is not an error. Run it without `--local` and it also visits every link and checks that the web address still serves the same document. Cambridge University Press stamps each download of the Maroto Molina paper with the date, the time and the downloader's IP address, so a fresh download never has the same bytes as the copy the research read. For that one file the check compares the text with the stamp lines removed, both for your own downloaded copy and for the copy at the link. A match proves the document text is the same; it does not make the file byte for byte identical. The script is [`3_code/check_sources.py`](../3_code/check_sources.py); its first lines explain it in plain words.

## Kevin's question

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| [`kevin_item_13.md`](kevin_item_13.md) | Item 13 of Kevin Xia's Top 30 project list, as he wrote it | The question this project answers, and its two valuable cells | No open licence; not covered by this repository's licence | Here | None |
| [`kevin_call_2026-09-22.md`](kevin_call_2026-09-22.md) | Notes of a call with Kevin on 22 September 2026, written automatically by a meeting tool. They are not Kevin's own words | Where the smaller scope was first proposed | No open licence; not covered by this repository's licence | Here | None |
| [`kevin_slack_2026-09-25.md`](kevin_slack_2026-09-25.md) | Kevin's Slack reply of 25 September 2026, which quotes three of Manisha's questions | The steer that industry acceptability, and coverage by existing sensors or certification schemes, are soft factors that make adoption easier, not hard requirements | No open licence; not covered by this repository's licence | Here | None |

Kevin Xia is the mentor of this project in the Sentient Futures incubator. These three files record what was received from him or about him. The item 13 text was pasted from his project list.

The Slack message is copied word for word. It quotes three questions from Manisha's smaller scope analysis of 23 September without marking them as hers. They are the paragraphs that begin "Species:", "Yes or no: FARM v5" and "Yes or no: the four dairy schemes". The paragraph after each is Kevin's answer. The handover of 23 September in the predecessor repository says the analysis asked Kevin for three decisions on Slack ([handover](https://github.com/NewAi25/plf-audit/blob/master/docs/handover_2026-09-23.md), section Next steps). So the recommendation of dairy first, then broilers, was Manisha's, and Kevin agreed, adding laying hens as an option for the second unit.

The call is recorded as the meeting notes that Gemini, an AI note taker, wrote automatically, with survey and calendar links removed. They summarise what was said; they are not Kevin's words. They record Kevin proposing a table of welfare indicators that are measurable by artificial intelligence, acceptable to industry, and covered by certification schemes. Manisha wrote that proposal up in her smaller scope analysis of 23 September. The analysis is not a file in this folder; it can be read in this repository's history at commit 6384465, file docs/PLF_Smaller_Scope_Analysis_2026-09-23.pdf. The phrases "covered by existing sensors" and "covered by existing certification schemes" appear in the Slack reply, where Kevin quotes them. An author's note that had been added to one line of the call file was removed on 3 October 2026, because these files hold only what was received; [`decision_log.md`](../2_research/decision_log.md) records it under that date. The header of the call file points to the author's own account of the call, the handover named above; the predecessor repository is public, so anyone can read it.

These files have no row in the manifest, because they are not published documents. What was decided from them is in [`decision_log.md`](../2_research/decision_log.md).

## The welfare indicators (column 1)

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| `efsa_2023_dairy_cows.pdf` | EFSA AHAW Panel 2023, *Welfare of dairy cows*, the scientific opinion of the European Food Safety Authority's animal welfare panel | The EFSA animal based measures in the indicator list, [`indicators.csv`](../2_research/indicators.csv) | CC BY-ND 4.0 for EFSA's own content; six figures (Figures 2, 3, 4, 5, 7 and 8) belong to third parties and are not covered | Link only | [PDF](https://www.mapa.gob.es/dam/mapa/contenido/ganaderia/temas/produccion-y-mercados-ganaderos/bienestar-animal/en-la-granja/vacuno/efsa---welfare-of-dairy-cows.pdf) |
| `welfare_quality_dairy.pdf` | Welfare Quality Network, *Welfare Quality assessment protocol for dairy cows*, version 3.2 (2024), a method for assessing welfare on the farm | The Welfare Quality measures in the indicator list | No licence stated | Link only | [PDF](https://www.welfarequalitynetwork.net/media/1319/dairy-cattle-protocol.pdf) |

The EFSA copy is the published PDF, downloaded from Wiley Online Library and re-hosted by the Spanish agriculture ministry, because the publisher's site blocked automated download. It carries the same DOI, 10.2903/j.efsa.2023.7993.

## The sensors (column 2)

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| [`stygar_2021.pdf`](stygar_2021.pdf) | Stygar et al. 2021, a systematic review of commercially available and validated sensors for dairy cow welfare | Which products outside studies have tested, and on which trait, in [`sensor_coverage.csv`](../2_research/sensor_coverage.csv) | CC BY 4.0 | Here | [PDF](https://www.frontiersin.org/articles/10.3389/fvets.2021.634338/pdf) |
| [`stygar_2021_supplementary.xlsx`](stygar_2021_supplementary.xlsx) | The spreadsheet published with Stygar 2021: the 129 products and the validation studies | The product list, [`products.csv`](../2_research/products.csv), and the count of products naming each indicator, which [`count_vendors.py`](../3_code/count_vendors.py) recomputes | CC BY 4.0, from the article | Here | [Europe PMC zip](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8044875/supplementaryFiles), file `Data_Sheet_1.xlsx` inside it |
| `maroto_molina_2020.pdf` | Maroto Molina et al. 2020, *Welfare Quality for dairy cows: towards a sensor-based assessment* | Which technology could measure each Welfare Quality measure, and the evidence for indicators no product measures | CC BY 4.0 | Link only | [PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/77A030621073F6601CC76F8A66487FAD/S002202992000045Xa.pdf/welfare_quality_for_dairy_cows_towards_a_sensorbased_assessment.pdf) |

The Stygar spreadsheet comes inside a zip file. Download the zip, open it, and save the file `Data_Sheet_1.xlsx` under the name `stygar_2021_supplementary.xlsx`.

## The certification schemes (column 3)

Column 3 has not been started. These documents are collected and fingerprinted so that the work can begin on fixed versions.

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| `rspca_dairy_standards_2026.pdf` | RSPCA welfare standards for dairy cattle, April 2026, the rules behind the RSPCA Assured label | What RSPCA Assured requires and how it is checked | All rights reserved (RSPCA) | Link only | [PDF](https://science.rspca.org.uk/documents/d/science/1856_dairy_cattle_welfare_standards_2026_web) |
| `rspca_dairy_justification_2026.pdf` | Dairy cattle: RSPCA standards justification, 2026 | The RSPCA's stated reasons for its requirements, for the notes in [`crosswalk.csv`](../2_research/crosswalk.csv) | All rights reserved (RSPCA) | Link only | [PDF](https://science.rspca.org.uk/documents/d/science/dairy-sjd-2026) |
| `farm_animal_care_v5.pdf` | National Dairy FARM Program, Animal Care Reference Manual Version 5, July 2024 to June 2027, the US dairy industry's own programme | What FARM requires, and whether the industry itself names each indicator | © National Dairy FARM Program, no licence stated | Link only | [PDF](https://nationaldairyfarm.com/wp-content/uploads/2024/09/FARM-14787-2023-Animal-Care-Standards-Reference-Manual.pdf), open in a browser |
| `gap_dairy_standard.pdf` | Global Animal Partnership, 5-Step Animal Welfare Standards for Dairy Cattle v2.0, issued 1 June 2026 | What Global Animal Partnership requires and how it is checked | All rights reserved (Global Animal Partnership) | Link only | [PDF](https://globalanimalpartnership.org/wp-content/uploads/2026/06/G.A.P.-5-Step-Standards-for-Dairy-Cattle-v2.0_-Website.pdf) |
| `certified_humane_dairy.pdf` | Humane Farm Animal Care, welfare standards for dairy cattle, Edition 23, the rules behind the Certified Humane label | What Certified Humane requires and how it is checked | All rights reserved (Humane Farm Animal Care) | Link only | [PDF](https://certifiedhumane.org/wp-content/uploads/DAIRY_CATTLE_STANDARDS.pdf) |

How each scheme document will be read is set out in [`rules.md`](../2_research/rules.md), which already quotes the RSPCA and FARM documents in its worked examples.

## ICAR validated devices

ICAR is the international body for animal recording. Among other work, it tests devices used in milk recording. Its web page lists three devices it has validated. All three measure milk: one milk composition analyser, one milk fat and protein sensor, one milk yield sensor. They are products P018 to P020 in [`products.csv`](../2_research/products.csv). The analyser, Ekomilk, measures somatic cell count, which is an indicator in the table (I057 and I058), and EFSA reads two more indicators, I021 and I025, from milk fat and protein. The Ekomilk report found its somatic cell count met ICAR's accuracy limit only between 0 and 500,000 cells per ml, not over the full range. These three products are not on the Product list sheet of the Excel file, which shows only the Stygar list.

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| `icar_validated_sensors.html` | ICAR Validated Sensor Systems web page, saved 16 September 2026 | The list of the three validated devices | © ICAR, no licence stated | Link only | [Web page](https://www.icar.org/icar-validated-sensor-systems/) |
| `icar_ekomilk_report.pdf` | ACTALIA Cecalait 2025, evaluation report for ICAR of the Ekomilk Horizon Unlimited milk analyser | Evidence for product P018 | No licence stated | Link only | [PDF](https://www.icar.org/wp-content/uploads/documents/Ekomilk-evaluation-report.pdf) |
| `icar_brolis_report.pdf` | ICAR 2025, Brolis BLH01 validation test summary and fact sheet | Evidence for product P019 | No licence stated | Link only | [PDF](https://www.icar.org/wp-content/uploads/documents/Brolis-BLH01-Validation-Test-Summary-Fact-Sheet-Final-Website.pdf) |
| `icar_panazoo_report.pdf` | ICAR, Panazoo MMI validation test fact sheet (no date on the document) | Evidence for product P020 | No licence stated | Link only | [PDF](https://www.icar.org/wp-content/uploads/documents/Panazoo_Report_website.pdf) |

The saved web page is a snapshot. A live web page changes its layout often, so a copy you save today will not give the same fingerprint as the snapshot. The check therefore confirms only that the live page still contains the word Panazoo, the name of one of the three devices.

## Framing

| Document | What it is | Used for | Licence | Here or link only | Link |
|---|---|---|---|---|---|
| `wieck_2026_moral_catastrophe.md` | Clare Wieck, *Factory Farming is a Moral Catastrophe. Let's Give it AI and See What Happens*, The Piglet, 1 September 2026, an essay that, by the author's account, Kevin shared on 30 September 2026 (no record of the message is in this folder) | The framing of the write up only. It is not a source for any cell in the tables | No licence stated | Link only | [Essay](https://thepiglet.substack.com/p/factory-farming-is-a-moral-catastrophe) |

This file is the text of the essay as published, with the web page formatting stripped. Like the ICAR page, a copy you save yourself will not give the same fingerprint, so the check confirms only that the live essay still contains the phrase "Moral Catastrophe".
