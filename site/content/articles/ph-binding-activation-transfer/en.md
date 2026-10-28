[日本語](ph-binding-activation-transfer.html)

If an antibody preferentially binds CD3 under acidic conditions, does its pH selectivity predict T-cell activation? The source study already reports that binding selectivity and activation selectivity do not match. This article does not present that mismatch as a discovery. It tests how accurately a simple conversion calibrated on the parental antibody predicts activation EC50s of engineered variants.

At neutral pH, predicted Q90LE EC50s were approximately 59 and 46 times the published values. Adding binding measurements did not reduce overall log error below a baseline that predicted no effect of engineering.

## The antibody format is matched but the assays are not identical

The source is Figure 10 of a pH-responsive anti-CD3 study published in April 2026. It compares parental 40G5c, Q90LE, and T89LD in the same bivalent IgG format. Binding is measured as Jurkat-cell mean fluorescence intensity. Activation is CD69 expression on primary CD4-positive T cells after 48 hours, using two donors. Plotted symbols are means of technical duplicates; the biological donor count for activation is two ([La Sala et al., 2026, Figure 10](https://pmc.ncbi.nlm.nih.gov/articles/PMC13128029/#f0010)).

| Antibody | Binding EC50, pH 6.5 | Binding EC50, pH 7.4 | Activation EC50, pH 6.5 (D1/D2) | Activation EC50, pH 7.4 (D1/D2) |
| --- | ---: | ---: | ---: | ---: |
| Parental | 0.078 | 0.106 | 6.31 / 7.03 | 10.42 / 8.15 |
| Q90LE | 0.17 | 136.64 | 20.07 / 17.82 | 227.82 / 230.85 |
| T89LD | 1.96 | 103.74 | 33.94 / 30.82 | 300.19 / 230.65 |

Units are nM. Values are transcribed from the numeric tables embedded in the original figure. They are EC50 estimates from the source concentration–response fits, not estimates refitted from raw observations in this reanalysis.

The binding assay incubates soluble antibody with Jurkat cells at 4°C. The activation assay coats plates with antibody, washes them, and then cultures T cells. Its concentration axis denotes antibody concentration during coating, not free drug concentration during culture. These EC50s cannot be treated as one shared mechanistic parameter ([source Binding assay on Jurkat cells and Primary T cell activation assay](https://pmc.ncbi.nlm.nih.gov/articles/PMC13128029/)).

The question is whether the parent's binding-to-activation ratio transfers unchanged to the engineered variants. The context of use is evaluating predictability between these assay systems for an antibody module. It does not predict tumor killing by a complete tumor×CD3 TCE or safe clinical concentrations.

## Calibrating only on the parental antibody

For donor \(d\) and pH condition \(h\), let \(B_{0h}\) be parental binding EC50 and \(A_{0dh}\) parental activation EC50. The scaling factor is

\[
r_{dh}=\frac{A_{0dh}}{B_{0h}}.
\]

Variant \(v\) is then predicted by

\[
\widehat A_{vdh}=r_{dh}B_{vh}.
\]

On a log scale, the slope is fixed at one and the parent determines the intercept. There is only one parental anchor per condition, so a slope was not estimated from those data. Engineered-variant activation EC50s do not enter calibration.

The comparator ignores binding and predicts \(\widehat A_{vdh}=A_{0dh}\). Both methods are evaluated on eight published summaries: two donors, two variants, and two pH conditions. These are not eight independent donors. The analysis is a retrospective, post-publication variant-extrapolation benchmark.

## Neutral-pH predictions failed

![Figure 1. Parent-calibrated activation EC50 predictions versus published EC50s](shared/ph-binding-activation-transfer/figures/transfer-prediction.svg)

| Donor | Variant and pH | Published activation EC50 | Prediction from binding EC50 | Predicted / published |
| --- | --- | ---: | ---: | ---: |
| D1 | Q90LE, 6.5 | 20.07 | 13.75 | 0.69 |
| D1 | Q90LE, 7.4 | 227.82 | 13,431.97 | 58.96 |
| D1 | T89LD, 6.5 | 33.94 | 158.56 | 4.67 |
| D1 | T89LD, 7.4 | 300.19 | 10,197.84 | 33.97 |
| D2 | Q90LE, 6.5 | 17.82 | 15.32 | 0.86 |
| D2 | Q90LE, 7.4 | 230.85 | 10,505.81 | 45.51 |
| D2 | T89LD, 6.5 | 30.82 | 176.65 | 5.73 |
| D2 | T89LD, 7.4 | 230.65 | 7,976.24 | 34.58 |

Concentration units are nM; see `outputs/tables/heldout-variants.csv`. Acidic-pH Q90LE predictions were relatively close, but that relationship did not transfer to neutral pH or T89LD. Applying the parent's conversion to weak neutral-pH binding greatly overpredicted the coating concentration required for activation.

![Figure 2. Binding and activation pH selectivity](shared/ph-binding-activation-transfer/figures/selectivity-transfer.svg)

Selectivity is the pH 7.4 EC50 divided by the pH 6.5 EC50. For Q90LE, the ratio recomputed from the printed binding EC50s was approximately 804. The parent-calibrated activation-selectivity predictions were approximately 977 for D1 and 686 for D2, versus published activation-EC50 ratios of approximately 11.35 and 12.95.

The source binding fold-change field reports 789.83, slightly different from 136.64 divided by the printed 0.17. Additional unprinted precision is a possible explanation. I did not silently replace that reported field: calculations use printed EC50s and retain the source-reported fold separately.

## Binding did not outperform the baseline

| Donor | Parent-calibrated binding-transfer log RMSE | Parent-only-baseline log RMSE |
| --- | ---: | ---: |
| D1 | 2.809 | 2.499 |
| D2 | 2.748 | 2.520 |

Each metric is \(\sqrt{\mathrm{mean}\{\log(\widehat A/A)^2\}}\) across four variant-by-pH summaries in that donor (`outputs/tables/comparison.csv`). The baseline also has large errors and is not supported as a practical predictor.

![Figure 3. Variant prediction errors in two donors](shared/ph-binding-activation-transfer/figures/prediction-errors.svg)

In 2,000 scenarios perturbing input EC50s by half their last printed decimal, the neutral-Q90LE predicted-to-published ratio ranged from 58.65 to 59.26 for D1 and from 45.28 to 45.75 for D2. These are not confidence intervals for source-fit uncertainty or donor variability, but rounding alone did not explain the discrepancy (`outputs/tables/rounding-sensitivity.csv`).

At neutral pH in D1, T89LD had the lower binding EC50, whereas Q90LE had the lower activation EC50. The D2 activation EC50s, 230.85 and 230.65, were essentially tied; that small difference is not interpreted as a reliable ranking. EC50 is the midpoint of each curve's own response range, not a shared absolute CD69-positive fraction. Maximal responses also differ, so EC50 rankings alone cannot select practical activation concentrations or a safety window.

## What the transfer rule does not establish

This calculation tests a single-factor link between two assays of bivalent anti-CD3 antibodies. It quantifies the binding–activation mismatch already described by the source as a withheld-variant prediction error. Monovalent Figure 11 constructs and SPR measurements at pH 6.0 were not mixed into it. With only pH 6.5 and 7.4, neither a continuous pH-response model nor activation kinetics was estimated.

Raw observations and EC50 estimation uncertainty could not be recovered from the public table, and no confidence intervals were reconstructed from the eight summaries. CD69 expression measures T-cell activation, not tumor-cell lysis. The result supports a narrow conclusion: weaker binding does not directly establish functional inactivity, and the relationship must be checked in the relevant assay system.

## Reproducibility

[Code, transcribed values, and result tables](shared/ph-binding-activation-transfer/ph-binding-activation-transfer-analysis.zip). Run `analysis/download_sources.py` to verify public Figure 10 and `analysis/run.py` to reproduce calibration, withheld-variant predictions, and figures. `python -m unittest discover -s tests` checks parent-anchor recovery and separation of held-out outcomes. The original image is not redistributed; its URL and SHA-256 are recorded.

## References

La Sala G, Kroell KB, Pincha M, et al. Engineering of acidic pH-responsive anti-CD3 binding antibodies. *mAbs*. 2026;18(1):2658902. [doi:10.1080/19420862.2026.2658902](https://doi.org/10.1080/19420862.2026.2658902).

## Cite this article

Kumakura D. Can pH-selective binding predict primary T-cell activation? 2026. A parent-calibrated transfer benchmark using published EC50 summaries.
