Enter a body weight to see how often the exposure of pembrolizumab or nivolumab falls outside the range confirmed in clinical trials under each dosing regimen. The numbers come from the [published-model simulation described in this article](../writing/fixed-vs-weight-dosing-en.html); this page only looks them up and recalculates nothing.

<div id="exposure-tool" data-lang="en" data-src="../assets/tools/anti-pd1-exposure-data.json"></div>
<noscript><p class="notice">This explorer needs JavaScript. The same numbers are in the tables of the <a href="../writing/fixed-vs-weight-dosing-en.html">article</a>.</p></noscript>
<script src="../assets/tools/anti-pd1-exposure.js" defer></script>

## How to read it

- **Body weight** selects one of seven weight bands (under 50, 50–60, 60–80, 80–100, 100–120, 120–150 and 150 kg and above). The band shows the share of simulated adults in it whose exposure left the range.
- **Below the lower limit** is the share of patients whose steady-state trough is below the 5th percentile of the reference weight-based regimen (pembrolizumab 2 mg/kg every 3 weeks, nivolumab 3 mg/kg every 2 weeks). **Above the upper limit** is the share whose steady-state peak exceeds the median peak at the highest tested dose, 10 mg/kg every 2 weeks.
- **Stays in range** applies the rule fixed before the analysis: at most 10% below the lower limit and at most 5% above the upper limit. You can change both allowances to see how the verdict depends on them.
- **Scenario** switches to the sensitivity analyses of the article: the weight exponent at either end of its 95% interval, the Asian weight distribution, ignoring sex, and the drug-specific alternatives (the table-footnote values and low albumin for pembrolizumab, time-varying clearance ignored for nivolumab).

## What the numbers are

- Two published population PK models were re-implemented: pembrolizumab (Ahamadi et al., 2017) and nivolumab (Bajaj et al., 2017).
- 20,000 virtual adults were drawn from the body weights of NHANES 2017 to March 2020 (a US survey), and exposure was computed in the first dosing interval from week 52 on.
- The lower and upper limits are proxies for the exposure used in the trials. They are not thresholds for efficacy or toxicity.
- The source of the numbers is the [distribution file](../writing/shared/fixed-vs-weight-dosing/fixed-vs-weight-dosing-companion.zip) of the article (`results/bands.csv`, `thresholds.csv`, `extreme-weights.csv`).

## Limits

This is a comparison of exposure in a simulation, not a dosing tool. It does not say which dose a patient should receive, and exposure differences are not shown to be differences in effect. NHANES is a US general adult population, not a cancer population. See the [article](../writing/fixed-vs-weight-dosing-en.html) for the full list of what can and cannot be concluded.
