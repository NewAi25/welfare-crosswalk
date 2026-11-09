# Which dairy welfare signs to push for when steering farm sensors

Manisha Sarkar. Sentient Futures incubator, mentor Kevin Xia. November 2026.

## The question

Farms can now buy sensors and cameras that watch cows. Welfare labels send inspectors to check how cows are kept. The two have grown up apart. Kevin Xia's list of research projects asks for a crosswalk, a table that lines up three things for one species: validated welfare indicators, what commercial sensors measure, and what certification schemes require and audit. In his words, the goal is to be able to say "these are the priority welfare indicators to push for when steering PLF". PLF is precision livestock farming: sensors and data analysis used on farms.

This note gives the answer for dairy cows and says how it was reached. The short answer is the [priority table](priority_table.md). The full evidence, with a source for every value, is in the [Excel file](welfare_crosswalk_dairy.xlsx).

## What was done

The table has 81 rows. Fifty eight are measures from two welfare protocols: the 2023 opinion on dairy cows from EFSA, the European Food Safety Authority, and the Welfare Quality assessment protocol. The other 23 are things sensors on sale say they measure that no protocol covers, such as rumination or body temperature.

Each row was asked four questions. Do the welfare sources treat it as a sign of welfare? Can a sensor measure it, and how did the sensor do when tested? How cheaply could a farm adopt it? Do the schemes require it, and how do they check it?

The sensor evidence starts from Stygar and colleagues 2021, a review that found 129 sensor technologies on the market, of which 18 had been externally validated. Reviews, a bounded literature search and makers' own pages since 2021 sit beside that baseline. Four schemes were read in full against every row: RSPCA Assured, FARM version 5 (the US dairy industry's own programme), Global Animal Partnership and Certified Humane.

Every value follows a written rule and names its source. Where the rules do not settle a value, it is marked unclear and the possible readings are listed; it is never guessed. Only public documents were used, and no maker was contacted. No welfare judgement was made in this project.

## How the ranking works

An earlier version added five factors into a score. Kevin's review said the ranking was invalid once it held rows that are not welfare validated, and it caught the industry's FARM programme being counted twice. The score is gone. In its place are four steps, taken in order and drawn from his review and from a summary he forwarded of an exchange with Claude.

The first step is a gate. Five rows that the welfare sources read here do not tie to welfare leave the list. Rows whose link to welfare is questioned or unclear stay, with a flag.

The second step groups the rows into welfare states, so that three tests for one condition count once. There are 52 states, of which 47 pass the gate. Each carries forward its best test.

The third step ranks the states. First comes how well the best test did. The bar is the one Stygar and colleagues use for high performance, and every result a study reports must meet it: a correlation above 0.9, for example, or a kappa, a measure of agreement, above 0.81. Next comes the cheapest device the measure needs. Last comes how hard the measure is to take by hand. EFSA rates how feasible each of its measures is on a farm, and a measure that is hard to take by hand is where a sensor adds the most.

The fourth step says what to ask for. There are three kinds of ask. World A: a sensor exists and is used, so ask schemes to take its data, either accepting it for something they already require or adopting it for something they do not. World B: there is no sensor product, so ask for new measurement. World C: the signal is already on farms, but no product says it is for health or welfare, so ask for welfare alerts or thresholds on hardware farms already own.

Tests that makers took part in needed care. Kevin's answer on a study the maker funded was to "count it but flag it", unless there were clear conflicts of interest or flaws arising from them. Ten such studies were checked against a written test built on that answer. Three count and seven do not.

One thing is deliberately missing. The list has no measure of how much each state matters to the cow. EFSA does not rank its welfare consequences; it assessed the five the European Commission asked for. Welfare Quality orders its criteria only within each of its four principles. Using either across this table would need a welfare judgement. So the list says where the evidence and the equipment are ready. It does not say which problem hurts cows most.

## What it found

These are the eleven states whose best sensor has been tested in a published study.

| Rank | Welfare state | Best test | Device needed | Kind of ask |
|---|---|---|---|---|
| 1 | Feeding behaviour and feeding time (flagged) | Passed the bar | One per farm or barn | C |
| 2 | Individual feed intake | Passed the bar | One per farm or barn | C |
| 3 | Resting problems (lying time) | Passed the bar | One per animal | A, adopt |
| 4 | Rumination | Passed the bar | One per animal | C |
| 5 | Standing (flagged) | Passed the bar | One per animal | Unclear |
| 6 | Subclinical ketosis | Cannot be graded yet | Nothing extra | A, accept |
| 7 | Subacute ruminal acidosis | Cannot be graded yet | Nothing extra | Unclear |
| 8 | Mastitis | Fell short of the bar | Nothing extra | A, accept |
| 9 | Lameness | Fell short of the bar | One per farm or barn | A, accept |
| 10 | General health status (flagged) | Fell short of the bar | One per farm or barn | Unclear |
| 11 | Restriction of movement (step activity) | Fell short of the bar | One per animal | A, adopt |

The main finding is a mismatch. The five states whose sensors passed the bar are not ones any scheme is known to require, though for standing a scheme's wording may name it. The four states schemes do require, with a sensor on offer, have weaker evidence: subclinical ketosis cannot yet be graded, mastitis and lameness fell short of the bar, and feed availability is only claimed by a product. What sensors do well is not what schemes ask for, and what schemes ask for sensors do not yet do well enough.

Kevin's item names two valuable cells. The first is indicators already measured by sensors but required by no scheme, a set he said could be large. It holds 21 rows, and 12 more are unclear. Three of the 21 are rows the welfare sources do not back, so the set of interest is 18. Read by welfare state, 15 of the 52 states are in this cell and 10 are unclear. The second cell is indicators required by schemes but checked by hand. It holds 24 rows. No scheme's numbered standards accept sensor data as the way an inspector checks any row.

Five things that products measure are not backed by the welfare sources read here. Individual water intake passed the bar, but neither those sources nor the product describes it as about welfare. Animal identification and milk fed to each calf are required by schemes, yet those sources do not link them to welfare. Blood in milk and LDH in milk are the other two. A link may exist in a source not read here.

For 20 states there is no sensor product at all.

## Recommendations

These follow from the table. They do not weigh one welfare problem against another.

Start with the signals farms already have. Feeding time, feed intake and rumination all passed the bar, and no product says it uses them for welfare. Body weight is in the same position, though it is only claimed. Asking makers for welfare alerts or thresholds on these signals needs new software rather than new hardware. The summary Kevin forwarded called this set probably the cheapest and most novel, and the table bears out that it exists. One caution applies: the welfare sources question how much feeding time says about welfare, so it is flagged at rank 1.

Next, ask schemes to adopt lying time. It is the one state in World A, adopt whose sensors passed the bar. EFSA also rates it low on feasibility, so it is hard to take by hand. The other five states in that group, step activity, body temperature, inflammation, milk conductivity and claw conditions, need better evidence first: their sensors fell short of the bar or have no test recorded.

Do not yet ask schemes to accept sensor data for what they already require. Ask first for independent validation against the bar. Lameness is the clearest case: all four schemes require it and all four check it by hand, so a sensor that passed would open the ask in every scheme. For subclinical ketosis the need is narrower. A 2025 test by ICAR, the International Committee for Animal Recording, reports strong results, but it does not say what its regression lines plot, so the test cannot yet be graded. Note too that the schemes require body condition scoring, while the tested sensor reads milk.

Ask the schemes to clarify their wording. For eight states a sensor exists and a scheme's rule may name the state, but the rule does not say so plainly. Among them are standing, subacute ruminal acidosis and general health. A sentence from a scheme would settle each one.

Finally, where there is no sensor, ask for new measurement, starting with what is closest. Social behaviour and comfort behaviour have been measured in cattle in research, but no product offers them.

## What this does not show

The sensor evidence rests on a 2021 baseline and on named sources since, not on the whole market. "Tested" means a published study tested a product, and many tests fell short. What products do with a signal is read from their one line descriptions, and for two rows from makers' pages, not from what happens on farms. The welfare relevance of the sensor rows rests on three documents only. Of the questions the rules could not settle, 54 remain open, each listed with its possible readings.

The checks were done by scripts and by an AI agent working from a fixed checklist. No welfare scientist has reviewed the table. This covers dairy cows only. Poultry is future scope, and the same tables and rules can be used for it.
