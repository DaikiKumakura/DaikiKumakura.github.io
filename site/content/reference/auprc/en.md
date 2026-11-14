AUPRC is the area under the precision–recall curve. It summarizes how well a classifier ranks the positive cases above the negative ones, with attention to precision, the share of predicted positives that are correct, rather than to the true-negative rate.

## Definition

The precision–recall curve plots precision against recall (sensitivity) as the decision threshold changes. AUPRC is the area under it. It is often computed as average precision, the sum over thresholds of the precision weighted by the increase in recall; interpolating linearly between points, as the trapezoidal rule does, can make it look too high.

A classifier that ranks at random has an AUPRC equal to the prevalence, the share of positives in the data. The baseline therefore changes with the data set, whereas the AUROC baseline is always 0.5.

## How it is used

AUPRC is preferred over AUROC when positives are rare and the question is how many of the top-ranked candidates are real, as in picking genes or compounds for follow-up. In imbalanced data, a large number of negatives can keep AUROC high even when precision among the top candidates is low (Saito and Rehmsmeier, 2015).

## Common pitfalls

- Comparing AUPRC across data sets with different prevalence. A value of 0.3 is well above baseline at 1% prevalence and below it at 50%.
- Treating a high AUPRC as the number of correct top candidates. Report precision at the number of candidates that will actually be tested.
- Averaging over classes or contexts without stating the weights, or without a simple baseline such as the mean profile for comparison.

## Related topics

- [C-index](c-index.html)

## References

- [Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLOS ONE. 2015.](https://doi.org/10.1371/journal.pone.0118432)
