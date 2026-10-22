## Definition

In Bayesian trials, data from an earlier study (here, an existing drug) can be borrowed as a prior. A **robust mixture prior** is a weighted mixture of

- an **informative component** based on the existing data, with weight ω, and
- a **vague component**, with weight 1 − ω.

ω is the **borrowing weight**: 0 means no borrowing and 1 means full borrowing. When the new data disagree with the existing data, the posterior weight of the informative component should fall, so the existing data influence the result less (Schmidli et al., 2014).

## What the site's analysis found

The [analysis of borrowing an existing drug's dose comparison](../writing/borrowing-prior-dose-selection-en.html) used published comparisons of sotorasib and ifinatamab deruxtecan as priors for a hypothetical new drug with 40 patients per arm.

- If the new drug behaved like the existing drug, borrowing improved correct dose selection by 6 to 10 points, but expected regret by only about 1 point.
- If the new drug favored the opposite dose, full borrowing lowered correct selection to 28 to 42%.
- With 40 patients per arm the conflict was hardly detected, so the mixture prior did not protect automatically. A borrowing weight of 0.25 to 0.5 kept the loss within 1 point.

The existing drug's [sotorasib dose comparison](../writing/sotorasib-dose-comparison-en.html) is one of the two inputs.
