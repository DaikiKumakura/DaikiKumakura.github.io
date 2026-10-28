## Definition

The **C-index (concordance index)** measures how well a model orders patients by risk. Among all pairs of patients whose order of outcomes can be determined, it is the proportion in which the patient with the higher predicted risk had the shorter survival. **0.5** is no better than chance and **1** is a perfect ordering. Censored patients contribute only to pairs where the order is known (Harrell's C-index).

## Reading it

- It measures **discrimination** (ordering), not **calibration** (whether the predicted risks are correct).
- It depends on the cohort, so values from different datasets are not directly comparable.
- A small gain with a wide interval may not be distinguishable from no gain.

## On this site

The [early tumor change and survival analysis](../writing/tumor-dynamics-survival.html) fixes a [landmark](landmark-analysis.html) at week 16. In 128 patients, the C-index on held-out data rose from 0.532 to 0.581 when early tumor change was added, but the interval for the improvement included zero and calibration remained weak. The analysis concludes that this is a candidate for further study, not a surrogate or a decision rule.
