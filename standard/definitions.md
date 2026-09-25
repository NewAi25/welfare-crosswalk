# Definitions

Version 0.1, 25 September 2026. Fixed before any extraction. Every column in the adoption table is defined here, with the rule that fills it and the source it is read from. Kevin's steer of 25 September is that the three criteria in the question are factors that make adoption easier, not filters, so each factor is a graded column, every indicator stays in the table, and the rank is a stated heuristic that any reader can re sort. Changes to this file get a dated entry in notes/decisions.md and a row in the change log at the end.

## Unit

One row per indicator in data/indicators.csv. An indicator is an animal based measure from the EFSA 2023 dairy cow opinion or the Welfare Quality dairy protocol, as built in the plf-audit repository and documented in docs/decisions_from_plf_audit.md. Each row carries a tier: joined when EFSA and Welfare Quality share the row, efsa_only when only EFSA lists it, wq_only when only Welfare Quality lists it. The tier is shown so that a reader who takes Welfare Quality alone as the validated set can exclude the 24 efsa_only rows without the table changing.

## Factor 1. Sensor coverage

Whether a commercial product measures the indicator, and how well that has been checked. Read from Stygar et al. 2021 (Table 1 page 6 for the validated products and their reference numbers, Table 2 page 7 for the traits each was validated on, the supplementary appendix for the 129 products and their stated aims), from Maroto Molina et al. 2020 for measures with no product, and from data/products.csv.

validated_commercial: a product in the Stygar appendix measures the indicator and Stygar code at least one external validation study for that product on that trait. The row names the product ids and reference numbers. commercial_unvalidated: a product in the appendix states the indicator in its aim and no external study is coded. The row names the product ids. research_only: no product, but Maroto Molina identify research level technology or a substitute measure, their partial. none: no product, and Maroto Molina say sensors cannot provide it or do not discuss it. unsure: the sources do not settle it; the candidate reading goes in notes and notes/unsure.md.

A trait validated by Stygar counts for an indicator only when Stygar's trait name and the indicator name are the same measure, for example lying time and lying time, or where Stygar's Table 2 category names the indicator directly, for example locomotion score for lameness. Rumination is not lameness, activity is not oestrus; a product validated on one trait does not earn a grade on another.

## Factor 2. Hardware class

The implementability and cost proxy, read from the sensor type Stygar and Maroto Molina name for the technology that measures the indicator. routine_data: already collected by the milking system or herd records, no new device (milk yield, milk conductivity, somatic cell count from records, calving records). farm_fixed: one device per farm or barn (camera, walkover scale or pressure mat, weather station, microphone, trough flowmeter with RFID). animal_mounted: one device per animal (collar, ear tag, leg tag, reticular bolus). sample_or_procedure: a blood or rumen sample, or a scoring done by a person, but only when a technology or method cited for the row is of that kind (rumenocentesis for rumen pH, body condition scored by eye where Maroto Molina name it). none: no technology named by Stygar or Maroto Molina for the row, including measures EFSA scores by a person at inspection; the class follows the sensor sources, not EFSA's scoring method. Where more than one technology measures the indicator, the class is the cheapest class that has a commercial product, and notes list the others. On an unsure row the class is filled from the cheapest commercial candidate so the factor stays usable, and notes say so. Lower classes are cheaper to adopt. The table shows the class; it does not put a price on anything.

## Factor 3. Market breadth

The number of products among the 129 in the Stygar appendix whose stated aim names the measurement. Counted by scripts/market_breadth.py from the keywords in the market_keywords column of data/sensor_coverage.csv, matched without regard to case against the AIM column of the appendix. The keywords for each indicator are written into the row so the count can be reproduced and challenged. The reading: what many vendors already sell is what industry already buys, which is the visible form of Kevin's "will not strongly object".

## Factor 4. Industry naming

Whether the indicator is named in a requirement of the industry authored programme, FARM Animal Care Version 5 for dairy, written by the National Milk Producers Federation. Values: named_with_threshold (the requirement names the measure and sets a number), named (names it, no number), related_resource (a requirement about housing, equipment or practice that bears on the indicator but does not name the measure), not_named. The requirement is quoted with section and page in data/crosswalk.csv. A factor, not a gate.

## Factor 5. Certification coverage

How many of the four schemes require the indicator, and how each audits it. Schemes: RSPCA Assured dairy cattle April 2026, FARM v5, Global Animal Partnership dairy v2.0, Certified Humane dairy Edition 23. audit_method per scheme row: visual_inspection (an assessor observes animals or scores them), records_review (the assessor checks farm records), sensor_accepted (the scheme text accepts sensor or automated data for the measure), unspecified (the scheme requires it but does not say how it is checked). A factor, not a gate.

## When a scheme requirement names an indicator

The requirement must name the animal based measure or a direct synonym. A requirement about housing, resources or practice that would affect the measure does not count as naming it; it is recorded as related_resource in notes so the reader can see it. Three worked examples. First, RSPCA Assured dairy cattle 2026, H 3.5, printed page 46: "All lactating cattle must be mobility scored at least four times a year by a mobility scorer registered with the Register of Mobility Scorers (RoMS) and the results recorded in the VHWP." That names lameness (Welfare Quality lameness, EFSA gait assessment), audit_method records_review, since the assessor checks the recorded scores. Second: "cubicle dimensions must be at least X" is related_resource for the comfort around resting measures, not a naming of time needed to lie down. Third, FARM Animal Care v5, page 149: "Severe Lameness: 5% or less of the lactating cows observed score 3 on the FARM Locomotion Scorecard." That names lameness with a numeric threshold, named_with_threshold, and the same page sets "Moderate Lameness: 15% or less" at score 2.

## Adoption ease rank

Each factor is mapped to 0 to 3 as follows and the five are summed to a score from 0 to 15. Sensor coverage: validated_commercial 3, commercial_unvalidated 2, research_only 1, none or unsure 0. Hardware class: routine_data 3, farm_fixed 2, animal_mounted 1, sample_or_procedure, none or unsure 0. Market breadth: 10 or more products 3, 3 to 9 products 2, 1 or 2 products 1, none 0. Industry naming: named_with_threshold 3, named 2, related_resource 1, not_named 0. Certification coverage: all four schemes 3, two or three 2, one 1, none 0. The sum is a heuristic and is labelled as one in every output. It is not a welfare judgement and not a recommendation; it is a sort order. Every factor stays visible in the table so a reader can re sort by any one of them. This mapping is the only place a decisions entry can change the ranking.

## The two item #13 views

Instrumented but not required: sensor coverage validated_commercial or commercial_unvalidated and certification coverage 0. Required but manually audited: per scheme row, requirement present, audit_method visual_inspection, and sensor coverage validated_commercial. Both are computed by scripts/stats.py from the same rows as the adoption table.

## Unsure

Any cell the rules above do not settle is coded unsure, with the candidate readings in notes and a line in notes/unsure.md giving the indicator, the factor and the candidates. It is resolved only by tightening the rule that failed, with a dated decisions entry, or it stays unsure in the published table and the note says how many rows are unsure per factor.

## Change log

| Date | Version | Change | Reason |
|---|---|---|---|
| 2026-09-25 | 0.1 | Written from Kevin's steer of 25 September and the smaller scope analysis of 23 September | Fixed before extraction |
| 2026-09-25 | 0.1.1 | Hardware class: none when no sensor source names a technology even if EFSA scores by procedure; unsure rows take the class of the cheapest commercial candidate | Two rule gaps found by the first row audit |
