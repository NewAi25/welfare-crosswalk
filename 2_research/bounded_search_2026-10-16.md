# Bounded search for the milk and metabolic rows, 16 October 2026

Part of the evidence since 2021 (rules.md, rule 4.11). No review found by the literature check of 29 September 2026 covers the milk and metabolic rows, so a bounded search of Europe PMC was run. The protocol below was written before the search, and an amendment was written before the extra queries were run. The search was run and the records screened by AI agents working from fixed instructions. The studies a grade rests on are in [evidence_since_2021.csv](evidence_since_2021.csv), with their full text or abstract in 1_sources.

## Protocol, as written

```
Bounded search protocol, milk and metabolic rows. Written 16 October 2026 10:17 IST, before any search was run.

Scope: I006, I007, I020, I021, I022, I024, I025, I026, I027, I028, I029, I056, I057, I058, I059.

Endpoint: https://www.ebi.ac.uk/europepmc/webservices/rest/search
Parameters: query=<string below>, resultType=core, format=json, pageSize=40, sort = Europe PMC default (relevance). The hit count is hitCount from the response.

Common clauses appended to every query:
 SENSOR = (TITLE_ABS:sensor OR TITLE_ABS:sensors OR TITLE_ABS:automated OR TITLE_ABS:automatic OR TITLE_ABS:"in-line" OR TITLE_ABS:inline OR TITLE_ABS:"on-farm" OR TITLE_ABS:bolus OR TITLE_ABS:boluses)
 ANIMAL = (TITLE_ABS:cow OR TITLE_ABS:cows OR TITLE_ABS:dairy)
 LIMITS = OPEN_ACCESS:y AND PUB_YEAR:[2021 TO 2026]

Indicator groups and measure clauses (query = MEASURE AND SENSOR AND ANIMAL AND LIMITS):
 G1 clinical mastitis (I006): (TITLE_ABS:"clinical mastitis")
 G2 somatic cell count (I007, I057, I058): (TITLE_ABS:"somatic cell count" OR TITLE_ABS:"somatic cell counts" OR TITLE_ABS:"somatic cells")
 G3 bacterial culture (I059): (TITLE_ABS:"bacterial culture" OR TITLE_ABS:"bacteriological culture" OR TITLE_ABS:"milk culture" OR TITLE_ABS:"on-farm culture") AND (TITLE_ABS:mastitis OR TITLE_ABS:milk)
 G4 ketosis (I020, I021, I022): (TITLE_ABS:ketosis OR TITLE_ABS:hyperketonemia OR TITLE_ABS:hyperketonaemia OR TITLE_ABS:"beta-hydroxybutyrate" OR TITLE_ABS:"β-hydroxybutyrate" OR TITLE_ABS:BHB OR TITLE_ABS:"fat to protein ratio" OR TITLE_ABS:"fat-to-protein ratio")
 G5 displaced abomasum (I024): (TITLE_ABS:"displaced abomasum" OR TITLE_ABS:"abomasal displacement" OR TITLE_ABS:"displacement of the abomasum")
 G6 ruminal acidosis and rumen pH (I025, I026, I027): (TITLE_ABS:"ruminal acidosis" OR TITLE_ABS:"rumen acidosis" OR TITLE_ABS:"rumen pH" OR TITLE_ABS:"ruminal pH" OR TITLE_ABS:"reticuloruminal pH" OR TITLE_ABS:"reticular pH" OR TITLE_ABS:SARA)
 G7 hypocalcaemia (I028, I029, I056): (TITLE_ABS:hypocalcemia OR TITLE_ABS:hypocalcaemia OR TITLE_ABS:"milk fever" OR TITLE_ABS:"blood calcium" OR TITLE_ABS:"serum calcium" OR TITLE_ABS:"parturient paresis")

Screening: the first 40 records per group in relevance order (all records when fewer than 40), title and abstract only, as Europe PMC returns them. Keep a study when its title or abstract says it measured or validated this measure (the group's measure) with a sensor, an in line analyser, a bolus or another automated system in cattle. Not kept: reviews and meta analyses (noted if they bear on a grade), studies where the sensor measures something else and the group's measure is only the outcome being predicted from another trait (for example activity or rumination used to predict ketosis), which are kept only as substitute measure evidence and labelled so, studies in other species, laboratory reference methods with no sensor or automated system, and simulations. Each kept study is then mapped to the indicators of its group by the indicator's own measure in indicators.csv, under the trait rule of rules.md 4.2.

Full text: Europe PMC fullTextXML (https://www.ebi.ac.uk/europepmc/webservices/rest/PMCxxxxxx/fullTextXML), open access only, only for studies a grade would rest on, at most about 15 in total, saved to scratchpad/step3/primary/. For each: whether the product is commercial and whether the authors work for the maker, from affiliations and the conflict of interest statement.

Deviation rule: any change to a query after it is run is reported as an amendment, with the reason and both hit counts.

AMENDMENT 1, written 16 October 2026 after the seven runs and before running these. Reason: in G1, G2 and G6 the relevance order put many studies first whose only sensor word is "on-farm" or "automatic" used loosely (farm surveys, pathogen genomics), so the first 40 of G2 hold almost no SCC sensor study, and G6 returned only 23 hits. Three narrower title-only queries are added, screened under the same rule and the same cap of 40, and reported separately with their own hit counts. The original seven queries and counts stand.
 A1 clinical mastitis: (TITLE:mastitis) AND (TITLE:sensor OR TITLE:sensors OR TITLE:"in-line" OR TITLE:inline OR TITLE:"automatic milking" OR TITLE:"automated" OR TITLE:"milking robot" OR TITLE:conductivity OR TITLE:detection) AND (TITLE:cow OR TITLE:cows OR TITLE:dairy) AND LIMITS
 A2 somatic cell count: (TITLE:"somatic cell" OR TITLE:"somatic cells" OR TITLE:SCC) AND (TITLE:sensor OR TITLE:sensors OR TITLE:"in-line" OR TITLE:inline OR TITLE:"on-line" OR TITLE:automatic OR TITLE:automated OR TITLE:"milking robot" OR TITLE:"cell counter" OR TITLE:validation OR TITLE:accuracy OR TITLE:comparison) AND LIMITS (no animal term, since milk SCC is almost always cattle; non-cattle studies are screened out)
 A6 rumen pH: (TITLE:pH OR TITLE:acidosis) AND (TITLE:bolus OR TITLE:boluses OR TITLE:sensor OR TITLE:sensors OR TITLE:wireless OR TITLE:continuous OR TITLE:indwelling OR TITLE:telemetric OR TITLE:validation) AND (TITLE_ABS:cow OR TITLE_ABS:cows OR TITLE_ABS:dairy OR TITLE_ABS:cattle) AND LIMITS
```

The folder named in the protocol was a working folder; the full texts read are now in 1_sources, named ev_ and the study key, with fingerprints in manifest.csv.

## Screening counts, mastitis and cell count groups

```
SCREENING COUNTS (records screened / kept)
G1 clinical mastitis, hitCount 73: screened 40 (first 40), kept 4.
G2 somatic cell count, hitCount 135: screened 40 (first 40), kept 2.
G3 bacterial culture, hitCount 22: screened 22 (all), kept 1.
A1 clinical mastitis, title query, hitCount 21: screened 21 (all), kept 3, all already kept in G1.
A2 somatic cell count, title query, hitCount 21: screened 21 (all), kept 2.
Totals: 144 records screened across the five groups; 12 keeps, 8 unique studies after duplicates.
```

## Screening counts, ketosis, abomasum, acidosis and calcium groups

```
SCREENING COUNTS (records screened / kept on the group measure / labelled substitute)
G4 ketosis (I020, I021, I022): hitCount 86; screened 40 (cap); kept 10; substitute 2.
  Kept: 2 Arlauskaite 2025 (in line FPR, ML), 5 supervised ML 2025 (automated FPR), 9 precision monitoring FPR 2025 (Brolis HerdLine), 23 in line lactose 2025 (FPR in line), 24 in line FPR and inflammation 2025, 27 Chick 2024 Keto-sensor (lab), 34 De Jong 2023 (Herd Navigator milk BHB), 35 Antanaitis 2023 (Brolis FPR), 37 Antanaitis 2024 (FPR and bolus pH), 39 lactose and behaviour 2024 (Brolis FPR).
  Substitute: 14 Robles-Trillo 2026 (collar and conductivity vs urine ketones), 40 rumination and bolus vs postpartum disorders 2025.
  Reviews noted, not kept: 13, 21 (KOL consensus, comment), 33. All others not kept (genetics, prevalence, treatment trials, lab lipidomics, methane).
G5 displaced abomasum (I024): hitCount 13; screened 13; kept 0; substitute 2.
  Substitute: 3 Suzuki 2026 (U-motion rumination predicts LDA), 9 prepartum alerts from a commercial monitoring system 2023.
  Not kept: 12 is a correction notice; 10 is a review; the rest are trials or records studies.
G6 ruminal acidosis and rumen pH (I025, I026, I027): hitCount 23; screened 23; kept 7; substitute 1.
  Kept: 1 Grige 2026 (bolus pH), 2 primiparous transition 2026 (intraruminal sensors, rumen pH), 4 Arlauskaite 2025 (in line FPR, LGRA), 6 precision monitoring FPR 2025 (LGRA by FPR), 9 SARA and claw health 2023 (intraruminal pH sensors), 11 heat stress smaXtec 2023, 12 marine algae buffer 2024 (rumen pH by "barn technologies").
  Substitute: 16 ear tag rumination alerts vs stomach tube rumen fluid 2023.
  Not kept: 5 and 19 (rumen pH method not stated in the abstract), 3 (cannulated cows, laboratory analysis), reviews 7, 15, 20, 21, and studies in ewes, goats, calves or cell lines.
A6 rumen pH, amendment query (I026, I027): hitCount 4; screened 4; kept 2 (1 Grige 2026, a duplicate of G6 record 1; 2 Fromm 2025 fattening bulls); not kept 2 (yogurt pH, urine pH).
G7 hypocalcaemia (I028, I029, I056): hitCount 42; screened 40 (cap); kept 5; substitute 3.
  Kept: 3 milk fever sensor 2025 (3D printed, milk ionized calcium to phosphate ratio, lab prototype), 14 Cao 2025, 25 paper based FET biosensor 2022 (blood Ca2+, lab prototype), 31 Leal Yepes 2023, 37 Suzuki 2021.
  Substitute: 4 Gleissenberger 2025, 7 subclinical hypocalcaemia with in line milk and rumination 2025, 23 prepartum alerts 2023.
  Not kept: 17 and 30 (FTIR milk analysis, laboratory prediction of dyscalcaemia; would be substitutes if automated), 18 case report, 10 review, the rest trials and records studies.
Total: 120 records screened, 24 kept (21 unique after duplicates across groups: Grige 2026, Arlauskaite 2025, precision monitoring 2025), 8 substitute.
```

In all, 264 records were screened (144 and 120). Manual culture kits for milk samples (I059) were screened out under the rule that only sensors and automated systems are kept.
