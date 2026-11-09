# Which dairy cow welfare indicators are ready for farm sensors?

Manisha Sarkar. Sentient Futures Project Incubator, mentored by Kevin Xia. November 2026.

## Question

Which welfare indicators for dairy cows should we push for first when steering precision livestock farming?

## Why this matters

Precision livestock farming means using sensors, cameras and data analysis on farms. Dairy farms can already buy these systems, and some are sold as welfare tools. Certification schemes, the standards behind welfare labels, send inspectors to check farms. Welfare scientists keep their own lists of what should be measured. These three lists have grown up separately, so it was hard to see which welfare problems sensors can already pick up, which of those anyone requires, and where a sensor could save an inspector's work.

## Method

I built a table for dairy cows with 81 rows. Fifty eight come from two welfare protocols: the 2023 opinion on dairy cows from the European Food Safety Authority (EFSA) and the Welfare Quality protocol. The other 23 are things sensors say they measure that neither protocol covers, such as rumination (chewing the cud) or body temperature.

For each row I recorded whether the welfare sources treat it as a sign of welfare, whether a sensor can measure it, how the sensor did when tested, what device it needs, and what certification schemes require. The sensor evidence starts from the 2021 review by Stygar and colleagues, which found 129 technologies on the market, of which 18 had been externally validated, meaning tested on data from herds not used to develop them. I added studies and makers' pages from 2021 onward. Four schemes were read in full: RSPCA Assured, FARM version 5 (the US dairy industry's own programme), Global Animal Partnership and Certified Humane.

Every value follows a written rule and cites its source. If the rules could not settle a value, it is marked unclear. I made no welfare judgements.

The ranking works in steps. First, 6 rows that the welfare sources I read do not link to welfare came off the list. Rows with a questioned or unclear link stayed, with a flag. Next, I grouped rows into welfare states, so that three tests of one condition count once. That gives 52 states, and 46 remain on the list.

Each state is then ranked by its best sensor test. I used the bar Stygar and colleagues set for high performance, where every result a study reports has to pass, for example a correlation above 0.9. A correlation measures how closely two sets of readings move together. Ties are broken by the cheapest device needed, and then by how hard the measure is to take by hand, using EFSA's feasibility ratings. A measure that is hard to take by hand is where a sensor helps most.

Ten of the studies involved the maker of the product. I checked them against a written conflict of interest test, and three count.

The list cannot tell you which problem matters most to the cow. EFSA does not rank its welfare consequences, and Welfare Quality only orders its criteria within each of its four principles. Using either across this table would have needed a welfare judgement.

## Results

The table shows the eleven states whose best sensor has a test that counts, in a published study or a test report. Mastitis is inflammation of the udder. Subclinical ketosis and subacute ruminal acidosis are metabolic disorders. A flag means the welfare sources question how much the measure says about welfare.

| Rank | Welfare state | Best test | Kind of ask |
|---|---|---|---|
| 1 | Feeding behaviour and feeding time (flagged) | Passed | World C: add welfare alerts |
| 2 | Individual feed intake | Passed | World C: add welfare alerts |
| 3 | Resting problems (lying time) | Passed | World A: add to schemes |
| 4 | Rumination | Passed | World C: add welfare alerts |
| 5 | Standing (flagged) | Passed | Unclear: a scheme may require it |
| 6 | Subclinical ketosis | Cannot be graded | World A: accept sensor data |
| 7 | Subacute ruminal acidosis | Cannot be graded | Unclear: a scheme may require it |
| 8 | Mastitis | Fell short | World A: accept sensor data |
| 9 | Lameness | Fell short | World A: accept sensor data |
| 10 | General health status (flagged) | Fell short | Unclear: a scheme may require it |
| 11 | Restriction of movement (step activity) | Fell short | World A: add to schemes |

| Kind of ask | What it means |
|---|---|
| World A: accept sensor data | A scheme requires part of the state and a sensor exists. |
| World A: add to schemes | A product's description says the sensor is for health or welfare, but no scheme requires the state. |
| World B: new measurement needed | No product is graded as measuring the state. |
| World C: add welfare alerts | A product collects the signal and no scheme requires it, but no description in the 2021 product list says it is for health or welfare. |
| Unclear: a scheme may require it | A sensor exists, but a scheme's wording may or may not name the state. |

Across all 46 states, 4 are World A: accept sensor data, 6 are World A: add to schemes, 4 are World C, 20 are World B and 12 are unclear. The World labels came out of my mentor's review.

The main result is a mismatch. The five states whose sensors passed the bar are not known to be required by any scheme, although one scheme's wording may cover standing. Schemes do require four states that have a sensor on offer, but the evidence there is weaker. Subclinical ketosis cannot be graded, mastitis and lameness fell short, and feed availability is only claimed by a product.

Sensors measure or claim to measure 21 rows that no scheme requires, and 12 more are unclear. Four of the 21 are rows the welfare sources do not back. Schemes require another 24 rows but check them by hand, with an inspector looking at the cows or reading farm records. No scheme's numbered standards accept sensor data as the way an inspector checks anything.

Six things products measure have no backing in the welfare sources I read. Individual water intake is one of them, even though its sensor passed the bar.

## Recommendations

Start with signals that products already collect. Feeding time, feed intake and rumination all passed the bar, and no description in the 2021 product list says they are for welfare, although most descriptions of rumination or feeding time mention health or welfare alongside. One maker's page now says that tracking rumination and eating time helps "overall cow health and welfare", so part of this gap may already be closing. On farms that own the devices, welfare alerts or thresholds would need new software and no new hardware. I have no cost data and no record of what farms own, so this needs checking with farmers and makers.

Next, ask schemes to adopt lying time. Its sensors passed the bar, and EFSA rates it low on feasibility. The other five states in that group need better evidence first, because their sensors fell short or have no test that counts.

I would not yet ask schemes to accept sensor data for what they already require. Independent validation should come first. Lameness is the clearest case, since all four schemes require it and check it by hand, so a sensor that passed would open the way in every scheme. Subclinical ketosis is less clear. A 2025 test of a milk analyser by ICAR, the International Committee for Animal Recording, reports strong results for milk fat and protein, but the report does not say what its regression lines plot, so I could not grade it. What the schemes require for this state is a score of how much fat a cow carries, while the tested sensor reads milk.

Schemes could also clarify their wording for the eight states where a sensor exists and a rule may name the state.

For the 20 states where no product is graded as measuring them, the ask is new measurement. Social and comfort behaviour are the closest, since they have been measured in cattle in research.

## Limitations and next steps

The sensor evidence rests on a 2021 baseline and the sources I read since then, not the whole market. What products do with a signal comes from their one line descriptions and, for two rows, makers' pages, so it does not show what happens on farms. Welfare relevance for the sensor rows rests on three documents. Of the questions the rules could not settle, 54 are still open and are published as open.

AI agents did much of the reading and all of the checking against sources so far, working to written rules. No welfare scientist has reviewed the table. Poultry is the natural next unit, using the same tables and rules.
