## Definition

In a **landmark analysis**, a time point (the landmark) is fixed in advance. Only patients still at risk at the landmark are included, only information available up to the landmark is used as predictors, and the outcome is followed from the landmark onward.

## Why it is used

A tempting analysis relates a patient's best response, wherever it occurred, to survival from the start of treatment. That uses information that was not available at the time of prediction, and patients who survive longer have more opportunities to have a response recorded. This produces immortal-time bias: the association looks stronger than anything that could be used at the landmark.

## Example

The [analysis of early tumor change and survival](../writing/tumor-dynamics-survival.html) fixes a landmark at week 16, uses only earlier tumor measurements, and evaluates the added value on held-out data. In 128 patients at the 16-week landmark, the C-index rose from 0.532 to 0.581, but the interval for the improvement included zero.

## Related

The [tumor-kinetic model analysis](../writing/tumor-kinetics-landmark.html) asks whether a model adds anything beyond a single early tumor change at a landmark, and the [dropout analysis](../writing/tumor-dropout-sensitivity.html) asks how patients who stop being measured affect the estimate.
