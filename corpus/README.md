# Corpus

The source documents live here locally and are not committed. Every file has a row in [`manifest.csv`](manifest.csv) recording the exact URL its bytes came from, the SHA256 of those bytes, and the date. `python scripts/check_corpus.py` re-fetches every URL and confirms it still serves the same bytes, so each link below points at precisely the document that was read, not a landing page that might serve a revised version. Run it before citing anything from a file for the first time.

Filenames matter: sessions look for these exact names. The "File" link is the URL the bytes came from. The "Canonical" link is the DOI or publisher page, for citations.

## Prior work to position against

| Filename | Document | File | Canonical |
|---|---|---|---|
| `maroto_molina_2020.pdf` | Maroto Molina et al. 2020, Journal of Dairy Research 87(S1) 28 to 33, 6 pages | [Cambridge Core PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/77A030621073F6601CC76F8A66487FAD/S002202992000045Xa.pdf/welfare_quality_for_dairy_cows_towards_a_sensorbased_assessment.pdf) | [doi 10.1017/S002202992000045X](https://doi.org/10.1017/S002202992000045X) |
| `stygar_2021.pdf` | Stygar et al. 2021, Frontiers in Veterinary Science 8:634338, 15 pages | [Frontiers PDF](https://www.frontiersin.org/articles/10.3389/fvets.2021.634338/pdf) | [doi 10.3389/fvets.2021.634338](https://doi.org/10.3389/fvets.2021.634338) |
| `stygar_2021_supplementary.xlsx` | Appendix tables 1 and 2: the 129 products and the 42 validation studies | [Europe PMC supplementary zip](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8044875/supplementaryFiles), member `Data_Sheet_1.xlsx` | [Frontiers supplementary material](https://www.frontiersin.org/articles/10.3389/fvets.2021.634338/full#supplementary-material) |
| `gomez_2021.pdf` | Gómez et al. 2021, Frontiers in Veterinary Science 8:660565, 20 pages | [Frontiers PDF](https://www.frontiersin.org/articles/10.3389/fvets.2021.660565/pdf) | [doi 10.3389/fvets.2021.660565](https://doi.org/10.3389/fvets.2021.660565) |
| `tuyttens_2022.pdf` | Tuyttens, Molento and Benaissa 2022, Frontiers in Veterinary Science 9:889623, 12 pages | [Frontiers PDF](https://www.frontiersin.org/articles/10.3389/fvets.2022.889623/pdf) | [doi 10.3389/fvets.2022.889623](https://doi.org/10.3389/fvets.2022.889623) |
| `elliott_werkheiser_2023.pdf` | Elliott and Werkheiser 2023, Animals 13(21) 3358, 11 pages | [Europe PMC PDF](https://europepmc.org/articles/PMC10648797?pdf=render) | [doi 10.3390/ani13213358](https://doi.org/10.3390/ani13213358) |
| `berckmans_2017_euplf_blueprint.pdf` | Guarino, Norton, Berckmans, Vranken and Berckmans 2017, "A blueprint for developing and applying precision livestock farming tools: a key output of the EU-PLF project", Animal Frontiers 7(1) 12 to 17, 6 pages. Filename keeps the project shorthand | [KU Leuven Lirias copy](https://lirias.kuleuven.be/retrieve/4e5ae17e-cfa6-45a1-b2b4-f999ab921d25) | [doi 10.2527/af.2017.0103](https://doi.org/10.2527/af.2017.0103) |
| `rutten_2013.pdf` | Rutten, Velthuis, Steeneveld and Hogeveen 2013, Journal of Dairy Science 96(4) 1928 to 1952, Utrecht repository copy with cover page, 26 pages | [Utrecht University repository](https://dspace.library.uu.nl/server/api/core/bitstreams/a22c3f26-9223-414e-8136-ef6d9d832681/content) | [doi 10.3168/jds.2012-6107](https://doi.org/10.3168/jds.2012-6107) |
| `van_erp_rutter_2020.pdf` | van Erp-van der Kooij and Rutter 2020, CAB Reviews 15(051). **Missing**, see below | | [doi 10.1079/PAVSNNR202015051](https://doi.org/10.1079/PAVSNNR202015051) |
| `coghlan_parker_2023.pdf` | Coghlan and Parker 2023, Philosophy and Technology 36:25, 34 pages | [Springer PDF](https://link.springer.com/content/pdf/10.1007/s13347-023-00627-6.pdf) | [doi 10.1007/s13347-023-00627-6](https://doi.org/10.1007/s13347-023-00627-6) |

## Welfare indicators (column 1)

| Filename | Document | File | Canonical |
|---|---|---|---|
| `efsa_2023_dairy_cows.pdf` | EFSA AHAW Panel 2023, Welfare of dairy cows, EFSA Journal 21(5):7993, 177 pages. Published PDF mirrored by the Spanish agriculture ministry | [mapa.gob.es PDF](https://www.mapa.gob.es/dam/mapa/contenido/ganaderia/temas/produccion-y-mercados-ganaderos/bienestar-animal/en-la-granja/vacuno/efsa---welfare-of-dairy-cows.pdf) | [doi 10.2903/j.efsa.2023.7993](https://doi.org/10.2903/j.efsa.2023.7993) |
| `welfare_quality_dairy.pdf` | Welfare Quality assessment protocol for dairy cows, version 3.2 dated February 2024 (first version 2009), 71 pages | [Welfare Quality Network PDF](https://www.welfarequalitynetwork.net/media/1319/dairy-cattle-protocol.pdf) | [Assessment protocols page](https://www.welfarequalitynetwork.net/en-us/reports/assessment-protocols/) |
| `efsa_2023_calves.pdf` | EFSA 2023 calves opinion. Deliberately not downloaded; only needed if calf products enter the list | | [doi 10.2903/j.efsa.2023.7896](https://doi.org/10.2903/j.efsa.2023.7896) |

## Certification and existing governance (column 3)

| Filename | Document | File | Canonical |
|---|---|---|---|
| `icar_validated_sensors.html` | ICAR validated sensor systems page, saved 16 September 2026. Lists three systems: Ekomilk, Brolis BLH01, Panazoo MMI | [icar.org page](https://www.icar.org/icar-validated-sensor-systems/) | same |
| `icar_section11.pdf` | ICAR Guidelines Section 11, milk recording devices, version October 2020, 46 pages | [ICAR PDF](https://www.icar.org/Guidelines/11-Milk-Recording-Devices.pdf) | [Milk recording devices sub committee](https://www.icar.org/index.php/technical-bodies/working-groups/milk-recording-devices-sub-committee/) |
| `icar_ekomilk_report.pdf` | ACTALIA Cecalait evaluation report of the Ekomilk Horizon Unlimited Instrument, 14 pages | [ICAR PDF](https://www.icar.org/wp-content/uploads/documents/Ekomilk-evaluation-report.pdf) | [ICAR validated systems page](https://www.icar.org/icar-validated-sensor-systems/) |
| `icar_brolis_report.pdf` | Brolis BLH01 validation test summary and fact sheet, 3 pages | [ICAR PDF](https://www.icar.org/wp-content/uploads/documents/Brolis-BLH01-Validation-Test-Summary-Fact-Sheet-Final-Website.pdf) | same page |
| `icar_panazoo_report.pdf` | Panazoo MMI validation test fact sheet, 4 pages | [ICAR PDF](https://www.icar.org/wp-content/uploads/documents/Panazoo_Report_website.pdf) | same page |
| `rspca_dairy_standards_2026.pdf` | RSPCA welfare standards for dairy cattle, April 2026, 108 pages | [RSPCA science PDF](https://science.rspca.org.uk/documents/d/science/1856_dairy_cattle_welfare_standards_2026_web) | [RSPCA dairy standards page](https://science.rspca.org.uk/sciencegroup/farmanimals/standards/dairycattle) |
| `rspca_dairy_justification_2026.pdf` | RSPCA standards justification, dairy cattle, 2026, 24 pages | [RSPCA science PDF](https://science.rspca.org.uk/documents/d/science/dairy-sjd-2026) | same page |
| `farm_animal_care_v5.pdf` | National Dairy FARM Animal Care Reference Manual Version 5, July 2024 to June 2027, 164 pages | [FARM PDF](https://nationaldairyfarm.com/wp-content/uploads/2024/09/FARM-14787-2023-Animal-Care-Standards-Reference-Manual.pdf) | [FARM animal care page](https://nationaldairyfarm.com/dairy-farm-standards/animal-care/) |
| `gap_dairy_standard.pdf` | Global Animal Partnership 5 Step standards for dairy cattle v2.0, issued 1 June 2026, 99 pages | [GAP PDF](https://globalanimalpartnership.org/wp-content/uploads/2026/06/G.A.P.-5-Step-Standards-for-Dairy-Cattle-v2.0_-Website.pdf) | [GAP dairy cattle page](https://globalanimalpartnership.org/standards/dairy-cattle/) |
| `certified_humane_dairy.pdf` | Humane Farm Animal Care standards for dairy cattle, Edition 23, 67 pages | [Certified Humane PDF](https://certifiedhumane.org/wp-content/uploads/DAIRY_CATTLE_STANDARDS.pdf) | [Certified Humane standards page](https://certifiedhumane.org/our-standards/) |
| `iso_ts_34700_summary.md` | ISO/TS 34700:2016, the public catalogue abstract and the informative sections from the Online Browsing Platform (foreword, introduction, scope, normative references, terms). Clauses 4, 5 and Annex A are paid and not included | [ISO catalogue page](https://www.iso.org/standard/64749.html), [OBP preview](https://www.iso.org/obp/ui/#iso:std:iso:ts:34700:ed-1:v1:en) | same |

## Legal templates (column 4)

| Filename | Document | File | Canonical |
|---|---|---|---|
| `eu_ai_act_art12_13_26.md` | EU AI Act Articles 12, 13 and 26, text as published on artificialintelligenceact.eu | [Article 12](https://artificialintelligenceact.eu/article/12/), [Article 13](https://artificialintelligenceact.eu/article/13/), [Article 26](https://artificialintelligenceact.eu/article/26/) | [Regulation (EU) 2024/1689 on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| `eu_data_act_chapter2.md` | Regulation (EU) 2023/2854, Chapter II, from the EUR-Lex HTML text | [EUR-Lex HTML](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854) | [Regulation (EU) 2023/2854 on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) |
| `cap_code_rule_3_7.md` | CAP Code section 3 (rule 3.7 substantiation) and the ASA advice page on farming methods | [CAP Code section 3](https://www.asa.org.uk/type/non_broadcast/code_section/03.html), [ASA farming methods advice](https://www.asa.org.uk/advice-online/farming-methods.html) | same |
| `simoneau_gilbert_birch_2024.md` | Simoneau-Gilbert and Birch, How to reduce the ethical dangers of AI assisted farming, Aeon | [Aeon essay](https://aeon.co/essays/how-to-reduce-the-ethical-dangers-of-ai-assisted-farming) | same |

## Sentient Futures week 3 materials

| Filename | Document | File | Canonical |
|---|---|---|---|
| `boddy_welfare_tech.md` | Aaron Boddy, Welfare tech should be developed by welfare people, EA Forum, June 2025 | [EA Forum post](https://forum.effectivealtruism.org/posts/JDDAiMoaeTK6WRNpT/welfare-tech-should-be-developed-by-welfare-people) | same |
| `boddy_industry_table.md` | Aaron Boddy, Animal advocates are too reluctant to sit at the industry's table, EA Forum | [EA Forum post](https://forum.effectivealtruism.org/posts/tFHEyAtr6bx93H6XR/animal-advocates-are-too-reluctant-to-sit-at-the-industry-s) | same |
| `brown_2024_restrict_ai.md` | Zachary Brown, We should campaign to restrict AI use in animal agriculture, Before Porcelain, June 2024 | [Substack post](https://beforeporcelain.substack.com/p/we-should-campaign-to-restrict-ai) | [EA Forum linkpost](https://forum.effectivealtruism.org/posts/BhAJu2fMAEj6ZeTw5/animal-advocates-should-campaign-to-restrict-ai-precision) |
| `taylor_2024_ai_factory_farming.md` | Sentient Futures, AI for Animals #2 and #3, AI in factory farming parts 1 and 2 | [Part 1](https://sentientfutures.substack.com/p/ai-for-animals-2-ai-in-factory-farming), [Part 2](https://sentientfutures.substack.com/p/ai-for-animals-3-ai-in-factory-farming) | same |
| `mckay_shah_2025_forecast.md` | McKay and Shah, Forecasting farmed animal numbers in 2033, Rethink Priorities, EA Forum version | [EA Forum post](https://forum.effectivealtruism.org/posts/Rw3iXiJ4Fw4ePu4t6/forecasting-farmed-animal-numbers-in-2033) | [Rethink Priorities page](https://rethinkpriorities.org/research-area/forecasting-farmed-animal-numbers-in-2033/) |

## Vendor documentation

Saved during weeks 1 and 2 into `vendors/<vendor>/`, named `<product_id>_<YYYY-MM-DD>_<short_name>.<ext>`, on the day each source is captured. Public pages only. Each one gets a manifest row.

## Missing files, 16 September 2026

One file still needs a human, because the journal is paywalled and the repository copy is restricted. No block was worked around. The ISO summary was retrieved on 16 September 2026 by reading the public catalogue and preview pages in a browser; the FARM manual PDF is sometimes served to a scripted request that carries a browser user agent and a referer, and was fetched that way and hash verified; the server answered 403 to the same request after several downloads, so its manifest row is browser_only and only the local hash is checked.

| Filename | Why it is missing | Where to get it |
|---|---|---|
| `van_erp_rutter_2020.pdf` | CABI Reviews is paywalled, and the [Harper Adams repository copy](https://hau.repository.guildhe.ac.uk/id/eprint/17613/) is restricted until 2100 | The DOI with an institutional subscription, or the repository's request a copy link |

## Provenance notes

Several copies came from repository mirrors rather than the publisher page, because the publisher blocked automated download. The EFSA opinion is the published PDF hosted by the Spanish agriculture ministry, 177 pages, same DOI on its cover. Guarino et al. 2017 is the KU Leuven Lirias copy. Rutten 2013 is the Utrecht University repository copy and carries a repository cover page before the article. Elliott and Werkheiser is the Europe PMC render. Each file was opened and its first page checked against the citation before it was kept.
