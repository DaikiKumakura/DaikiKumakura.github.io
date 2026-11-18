In a phase 1 trial of pasritamig with JNJ-9401, prostate-specific antigen (PSA) fell by at least 50% (PSA50) in 11 of 15 patients at the recommended regimen ([1](#ref-1)). JNJ-9401 connects prostate-specific membrane antigen (PSMA) and CD28 to provide costimulation. The add-on question is how many percentage points the response rate changes relative to pasritamig alone under the same conditions.

## A single-group rate leaves the comparator open

In a target population with a fixed observation window and assessment rule, let $p_1$ be the combination PSA50 rate and $p_0$ the rate on pasritamig alone. The desired difference is $p_1-p_0$. Treating 11/15 as the point estimate of $p_1$, with no information about $p_0$, gives −26.7 to +73.3 percentage points. This range is conditional on the point estimate. The binomial Wilson 95% confidence interval of 48.0–89.1% is for the combination rate and gives no information about the missing monotherapy rate.

**Table 1.** Combination-minus-monotherapy differences under assumed monotherapy rates.

| Assumed monotherapy PSA50 | Combination minus monotherapy |
| ---: | ---: |
| 40.0% | +33.3 pp |
| 60.0% | +13.3 pp |
| 80.0% | −6.7 pp |

Table 1 gives a 13.3-point increase if monotherapy has a response rate of 60%, and a 6.7-point decrease if it has a rate of 80%. Adding a separate monotherapy cohort would mix treatment with selection and measurement if previous therapy, PSA assessment timing, or the handling of patients without a measurement differed.

Part 2 of phase 3 KLK2-comPAS randomizes between pasritamig alone, pasritamig with JNJ-9401, and placebo ([2](#ref-2)). The design includes the concurrent add-on comparator. Overall survival is the primary endpoint. To estimate the contribution to PSA50, we would need the results for both active arms under a common assessment rule.

## Data and code availability

The [reproducibility ZIP](shared/pasritamig-add-on-identification/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Johnson & Johnson. Johnson & Johnson reports 73% PSA response rate with investigational pasritamig-based immunotherapy combination in advanced prostate cancer [press release]. 2026 Nov 9.](https://www.jnj.com/media-center/press-releases/johnson-johnson-reports-73-psa-response-rate-with-investigational-pasritamig-based-immunotherapy-combination-in-advanced-prostate-cancer)
2. <a id="ref-2"></a> [Johnson & Johnson. KLK2-comPAS phase 3 trial design [conference poster]. ESMO 2026. Abstract 2388eTiP. Figure 2.](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/esmo/klk2compas-a-phase-3-randomized-doubleblind-placebocontrolled-study-of-a-p.pdf)
