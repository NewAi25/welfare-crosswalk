# Kevin Xia, revised table spec (change request), 7 October 2026

Source: Google Doc shared by Kevin Xia on Slack on 7 October 2026, https://docs.google.com/document/d/1OEHDbuVBISX3ljNRHaDZ9d6v3gKjhwFKQGKj9Hihjo4/edit?usp=sharing. Text pasted by Manisha Sarkar on 7 October 2026. Kevin's covering Slack message, verbatim:

> Hey Manisha! I had a bit of a discussion with Claude about your repository to get a better sense of what I think is missing and what next steps are - here is the summary. I would flag that:
>
> * The gaps are real and identified by me
> * The general recommendations of how I think the table should ultimately look like is also real and identified by me
> * The concrete recommendations for "next steps" are Claude-generated, worth sense-checking

The document, as pasted (table layout flattened by the paste):

---

Welfare crosswalk — revised table spec (change request)
Oct 7, 2026 · @Kevin

Summary
This is a change request against NewAi25/welfare-crosswalk, agreed with Kevin on 7 October 2026. It revises the table design in three ways: the row universe becomes two-sided (protocol-listed indicators plus parameters claimed by commercial PLF products), a new column 1 scores each indicator's welfare relevance separately from measurability, and the sensor column is regraded into an explicit two-dimensional scheme (device existence × evidence strength) with a post-2021 evidence pass. Everything else stays: the provenance machinery, manifest, audit flow, rules.md structure, the scheme-reading plan, and the existing 58 rows. The scheme reading remains the critical path and should not wait on any of this.

The question and the four columns
The product answers: which welfare indicators are (a) measurable by AI, (b) acceptable to industry, and (c) already covered by existing sensors or certification schemes — for the dairy unit. The revised table factors this into four columns, each answering one question per row:

Column | Question | Decomposes
1. Welfare relevance | Is this indicator validated in veterinary/welfare science as actually mattering for welfare? | new — currently implicit in row inclusion
2. AI measurability | Can AI/sensors measure it, with what device status and what evidence? | (a), plus the sensor half of (c)
3. Industry acceptability | Would industry adopt it — cost, implementability, own-program endorsement? | (b)
4. Scheme assessment | Do the four certification schemes assess it, and by what method? | the scheme half of (c)

Sensor coverage moves entirely into column 2; column 4 is purely about schemes. The original (c) then decomposes with no remainder.

Rows: revised inclusion rule (amends rule 4.1)
The row universe becomes the union of two sides, so that market-discussed parameters can be tested for welfare relevance rather than excluded by construction:
Protocol side (unchanged): every measure in the EFSA 2023 ABM tables for the five welfare consequences, and every measure in the Welfare Quality 3.2 overview — the current 58 rows, including the 10 resource/management/none rows, which stay but keep their measure_type flag.
PLF side (new): every parameter class that commercial PLF products claim to measure, where anyone — vendor, literature, or scheme — frames it as welfare-relevant, or a reasonable observer would assume it is. Pure production/reproduction parameters with no welfare framing anywhere (e.g. oestrus detection marketed solely for fertility) may be excluded; including them anyway is acceptable when the marginal cost is low. Granularity is the parameter class (activity, lying time, rumination, temperature, weight, location…), never the individual product — Stygar's 129 products collapse to roughly 15–25 classes.
Mechanics: listed_by gains a plf_only value; PLF-side rows are sourced from Stygar's own product table (already fingerprinted in the manifest) plus a dated vendor check for post-2021 entrants. Add a welfare_state grouping column across all rows so the output lists can be read at the welfare-state level (subclinical ketosis is one state, not three independent rows) — this fixes the assay-level double counting in the current top ranks.
The intended finding this unlocks: PLF-discussed parameters that turn out to have no welfare validation (column 1) are a result of the project, not noise to be filtered out at the door.

Column 1: welfare relevance (new)
The question: is this indicator validated in veterinary/welfare science as actually relevant for welfare? This is distinct from whether it can be measured reliably — measurement evidence lives in column 2. Activity is the canonical case: excellently measured by validated commercial sensors, but its link to welfare is indirect; the two facts must land in different columns or the table becomes unfalsifiable.
Suggested grades:
Grade | Meaning
established | Protocol-validated as a welfare measure
supported | Peer-reviewed evidence links it to welfare, outside the two protocols
indirect or contested | A proxy whose welfare link is debated or mediated (e.g. activity, production drops)
no welfare validation | Claimed or implied welfare-relevant by industry only; no scientific support found
not welfare-relevant | Measured by PLF, no one credibly claims welfare relevance (only present if the row was kept under the low-cost clause)

Sources, all already identified: EFSA's own sensitivity/specificity/feasibility ratings, which sit in the fingerprinted ABM tables but are currently not transcribed into indicators.csv — transcribe them as three columns; Welfare Quality's validation history for the WQ side; and Linstädt et al. 2024 (Frontiers in Veterinary Science 11:1429097), the systematic review of dairy ABM validity and practicality that the 29 September literature check already flagged, which is purpose-built for grading the PLF-side rows.
The headline output of this column: the list of PLF-discussed parameters graded "no welfare validation" — the suss-out Kevin asked for.

Column 2: AI measurability (regrade of the current sensor column)
What the two current sources actually are, since the grades inherit their character: Stygar et al. 2021 did two separable things — a PRISMA review of externally validated sensor technologies (evaluator independent of the manufacturer) and a market search finding 129 retailed products, 18 of them externally validated. Maroto Molina et al. 2020 is a six-page Research Reflection — an opinion piece proposing which technologies could address each WQ measure, including technology borrowed from pigs, carcasses and human skin. Stygar supports evidence; Maroto Molina supports possibility. The regrade makes that difference explicit as two dimensions:

(rows: device status; columns: evidence strength)
 | Externally validated | Manufacturer claim only | Demonstrated in research | Proposed only
Commercial device exists | measurable — validated | claimed measurable | device exists, measurability unclear | —
No commercial device | — | — | research-demonstrated | theoretically measurable

Two changes from the current Tested/Claimed/Research only/Nothing found/Unclear scheme: the current "research only" splits into research-demonstrated (a study did it) and theoretically measurable (Maroto Molina proposed it) — these differ enormously in certainty and are currently one grade; and "nothing found" stays, explicitly meaning "nothing in the sources consulted as of their dates".
Evidence update, following the design in literature_check_2026-09-29.md (a second dated evidence column beside the frozen 2021 baseline, never overwriting it): Lee et al. 2025 (Animal 19:101613) for the wearable behaviour rows, Hudson et al. 2026 (Animals 16:2643) for lameness and the camera rows, the bounded protocol search for the milk/metabolic rows, roughly 6–8 hours total per the check's own estimate. One addition the check scoped out: a targeted vendor check — not a new 129-product market scan — only for rows that end up as List 1 candidates or remain "nothing found", since validation literature lags the market and post-2021 commercial products won't enter through any review. Products found this way take the existing manufacturer-claim grade; no new rules machinery needed.

Columns 3 and 4
Column 3, industry acceptability: unchanged for now, discussion parked. The current proxies — cheapest device class plus FARM v5 naming — stay until columns 1 and 2 are settled. One known limit to carry forward in the read-me: these proxies capture implementability, not political acceptability. A cheap walkway camera that makes lameness prevalence legible may be less acceptable to industry than an expensive collar that boosts productivity; a high column-3 grade means "industry could do this cheaply", never "industry won't object".
Column 4, scheme assessment: scope unchanged, one addition. The column records whether each of the four schemes assesses the indicator and by what method — annual manual audit, records review, or sensor data accepted. The method is not optional detail: List 2 (required but manually audited) is defined by the method, not by coverage. The planned scheme reading already captures this; it stays the critical path and the single highest-value outstanding task.

Other gaps that need addressing
1. The sensor baseline is 2020–2021, and the bias runs exactly against your valuable cells. "Measurable by AI" is answered from Stygar's 2021 market snapshot plus Maroto Molina 2020. Computer-vision welfare monitoring has moved substantially since; "Nothing found" means "not in two five-year-old papers," which the README states honestly but which systematically understates (a) and therefore shrinks List 1 — the already-instrumented-but-not-required set whose size was your stated unknown. A dated update pass is "planned for later." I'd argue it's not optional: without it, the headline finding ("the cheap-ask set has N members") will be a lower bound stale enough to be misleading. If hours are constrained, a targeted update only for the 12 "nothing found" + 5 "unclear" rows would be the efficient version.
2. The indicator universe is narrower than item 13. You named Welfare Quality, AWIN, and species literature. Dropping AWIN for dairy is correct (AWIN has no dairy cattle protocol). Dropping "species literature" is a real narrowing with a directional bias: the universe is now defined by what assessment protocols list, which skews toward manually-scoreable measures and can exclude sensor-native validated indicators (e.g., continuous rumination/activity patterns as indicators in their own right) — again shrinking List 1 specifically. The EFSA addition partially compensates. This is a legitimate scope call, but it was carried over from the predecessor project rather than argued; if you accept it, accept it knowingly.

The problems with the current list of welfare indicators:
1. "Validated" is operationalized as provenance, not checked. The inclusion rule is "listed in one of two documents." That's an appeal to the sources' authority, which is reasonable for WQ (its measures went through a decade of validity/reliability work) but weaker for EFSA: EFSA's ABM tables themselves rate each measure for sensitivity, specificity, and on-farm feasibility, and some ratings are low — the README's own example is lying time rated low-feasibility. Those ratings are the per-indicator validation evidence that actually exists, and the table drops them. The one thing the sources say about how good each indicator is doesn't make it into the crosswalk. That's the cheapest high-value fix: three columns, already sitting in tables the project has fingerprinted.
2. Ten rows aren't welfare indicators in the animal-based sense at all. 6 are resource-based (water provision, water flow, cleanliness of water points...), 3 management-based (disbudding, tail docking, pasture access), and I039 — thermal comfort — is a WQ criterion for which no measure is defined: a row with literally nothing to measure, included anyway. These are validated protocol components, but calling them validated welfare indicators smuggles inputs into the outcome category. It also distorts your question (a): "can a sensor measure lameness" and "can a sensor verify tail-docking policy" are different question-types, and the second will mechanically populate "nothing found."
3. The unit of analysis mixes welfare states with assays for them. EFSA contributes three separate rows for subclinical ketosis (milk constituents / BHB / body condition) and three for ruminal acidosis, including "rumen pH by rumenocentesis" — a diagnostic puncture, a research procedure, not a farm welfare indicator. Meanwhile WQ's two lameness measures got merged into one row. So "indicator" sometimes means a welfare state and sometimes means one detection method for a state, inconsistently. This matters for your lists: if ketosis-via-BHB is sensor-covered but ketosis-via-BCS is "nothing found," the state-level answer is "covered" while the table reports a gap — and three of your current top-5 ranked rows are ketosis/SARA assay-variants of this kind, partially double-counting one opportunity.
