# Kevin's answers and review, Slack, received between 1 and 5 November 2026

Verbatim, as pasted by Manisha Sarkar on 5 November 2026 from the Slack direct messages with Kevin Xia: four messages. Slack showed times but not dates in the paste; the "Message of" labels are added to separate the messages. The paste kept the text and its indentation but not its bold formatting.

**Message of 6:45 PM**

> Hey Manisha! Sorry for the late response, your first message came while I was at a conference and then I saw in your second message that you'd be off, so I didn't rush to get back to you.
> Is this the right set? Is there a review or dataset you'd add, or one you'd drop?
>
> All of the articles mentioned seem generally useful, whether they prove crucial can only be said once you have read them, I think. I don't know whether there are any out there that I would add.
> Can a study count if I reach it one step through a review's citations, rather than it being in the review itself? Example: Anagnostopoulos et al. 2023, the CattleEye lameness validation (https://doi.org/10.3389/fvets.2023.1111057), is cited by a 2025 paper that Islam lists, not by Islam directly.
>
> Sure, don't see a reason why not. Can you share why you would consider not counting it?
> Should a maker funded study count as a validation? CattleEye funded that 2023 study and approved the manuscript, though none of the authors work for them and they declare no conflicts. I'd record it as validated but flag the funding, the same way Stygar counted self validations in the baseline.
>
> I agree, count it but flag it - unless you can find clear conflicts of interest or flaws in the study itself that may have arisen from such conflict

**Message of 8:29 PM**

> A couple of points I came across in reviewing your work:
>
> * I think the ranking is invalid now that there are things in there that are not welfare validated; this is minor but worth flagging
> * I think the crosswalk as it stands now is probably a bit overengineered and overwhelming, it would be good to have a much simpler table that only scores the welfare indicators on the relevant measures and reference the big excel as an accompanying doc, together with a write up of the methodology and recommendations
> * I think FARM is counted twice? It has its own 0–3 factor and is also one of the four schemes in "schemes requiring"
> * I think EFSA's feasibility rating may point the wrong way. It rates how feasible it is to assess the measure on farm, presumably by a person? But low manual feasibility combined with a sensor that measures it is exactly where automation adds the most value. So for your purposes, a "Low" feasibility rating on a sensor-measurable indicator is arguably a reason to rank it higher. The project transcribed the ratings without asking which way they cut.

**Message of 8:33 PM**

> There is a bigger point about scoring structure that I think needs addressing. I had a bit of a back and forth with Claude about it, this is the summary, with comments from me bolded
>
> 1. What needs to be done about the score
>
> The core problem isn't a missing term in the sum. Adding scores is the wrong structure for these criteria. When parts are added, cost and vendor count can make up for irrelevance, which is how a row with no welfare validation reaches rank 3. Welfare relevance should act as a gate, not a weight. In order:
>
> * Allow labelled judgement columns. This comes first, because everything else depends on it. Hard rule 2 ("never make a welfare science judgement") makes a priority list impossible. Keep the sourced/decided/unknown discipline, but add a fourth kind of value: judged, with who judged it and on what basis. The project already makes judgements, in the score weights and the 14 reading rules. This change makes them visible instead of hidden.
>    * I am not sure this needs to be done or is in scope of this particular project. I think it's fine if you don't have Claude make welfare judgments given neither of us, including Claude, would have the right expertise. I do think you need to make sure that welfare relevance does act as a gate - if something is not welfare validated, it should rank low.
> * Aggregate to welfare states before anything else. Rank states, not assays. For each state, carry forward the best available assay.
>    * I am not sure this would be possible with the above. If it is, I do think it is important - but it might not be.
> * Gate on welfare relevance. Rows graded No welfare validation or Not framed as welfare leave the priority list. They become their own finding: what the market measures that the welfare literature doesn't back. Indirect or contested rows stay, but flagged.
> * Add an impact tier for each welfare state. This is the missing input. First check whether EFSA 2023 ranks its welfare consequences by severity, prevalence or duration. If it does, transcribe that as sourced. If not, use a three-level judged tier, stated as such.
>    * I think this would be great if there is hard evidence on this. There is a missing component in the existing crosswalk about how much specific indicators matter and making sure we have that would be great. If this requires subjective welfare judgment, it's fine not to include it. The EFSA 2023 recommendation came from Claude, I didn't check it.
> * Grade measurement validity properly. The data is already there: the "What was tested, and how well" column records Stygar's performance category. So the grade can be tested and met the threshold / tested but below it / claimed only, instead of a single "Tested".
> * Use EFSA's ratings correctly:
>    * Sensitivity and specificity become a validity flag where they exist, with "not rated" for Welfare Quality–only rows. Missing ratings should not count as a penalty.
>    * Feasibility comes out of any cost logic. Reinterpret it as manual burden, which is the value of automating the measure.
> * Fix the arithmetic:
>    * Remove the double count of FARM.
>    * Move "schemes requiring it" out of the ease score. It decides what kind of ask an indicator supports (World A vs B vs C), not how easy adoption is.
>
> The result is a ranking applied in order: relevant state → impact tier → validity of the best assay → marginal cost (point 3 below). It is not one number.

**Message of 8:40 PM**

> There is another one around sensor measurability and what the project aims to be. To recap, the goal of the project is to be able to say: "these are the priority welfare indicators to push for when steering PLF", meaning measurable, validated and cheap to implement, with the method as a secondary output. Once again, I had a bit of a back and forth with Claude, here is the summary:
>
> The potential gap: "a sensor can measure it" is not "PLF is built around it"
>
> There are at least four layers:
>
> 1. Signal: hardware captures raw data (acceleration, conductivity, images).
> 2. Inference: an algorithm turns that into an indicator (lying bouts, a lameness score).
> 3. Action: the system alerts, recommends or controls something.
> 4. Objective: the system is tuned toward welfare, or toward production with welfare as a side effect.
>
> Column (a) grades layers 1 and 2 together. Layers 3 and 4 aren't in the table. A collar that records lying time for heat detection and a system that alerts on low lying time for welfare reasons get the same grade.
>
> This matters because "push for" covers three different asks:
>
> * World A: the measure exists and is used. Ask schemes to accept the sensor data (today: lameness, BCS).
> * World B: the welfare state matters but there's no sensor. Ask for new measurement.
> * World C: the signal is already on the farm, but nothing is built around it with welfare as the goal. Ask for software, alerts or welfare thresholds on hardware farms already own.
>
> World C is probably the cheapest and most novel set, and right now the project can't see it.
