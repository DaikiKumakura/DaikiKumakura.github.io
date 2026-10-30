[日本語](mrna-vaccine-rfs-comparison.html)

A cancer vaccine reduced recurrence risk by 42%. That does not mean that treating 100 people prevents 42 recurrences. It does not mean that mortality alone fell by 42%, either.

The 42% reported for INTerpath-001 is `1 − 0.58`, using the hazard ratio for time to recurrence or death. The same announcement gives two-year recurrence-free survival estimates of 82.2% and 70.0% ([1](#ref-1)). Their difference is 12.2 percentage points. Neither number corrects the other: they describe different quantities.

There is another complication. A separate trial of immunotherapy before surgery also reported a hazard ratio of 0.58. Does that make adding a vaccine equivalent to moving treatment before surgery? Before comparing the drugs, the starting point of each trial's clock needs attention.

## Scope and sources

I examined the 22 October 2026 INTerpath-001 announcement, the original abstracts for SWOG S1801 and NADINA, and the abstract of a methodological paper on S1801 endpoints. INTerpath-001 randomizes patients with resected stage IIB–IV melanoma to individualized mRNA therapy intismeran autogene added to pembrolizumab or to the control strategy ([1](#ref-1)).

The calculations below use printed two-year estimates for arithmetic and a hypothetical example of treatment timing. They are not patient-level reanalyses, digitized Kaplan–Meier curves, or an estimated indirect comparison. The scope of this review is narrower than one based on complete original articles and supplements.

## Separating 42% from 12.2 percentage points

Recurrence-free survival (RFS) counts recurrence and death as events. It differs from overall survival (OS). The INTerpath-001 announcement describes OS data as immature ([1](#ref-1)).

Write the two-year RFS estimates as \(S_1(2)=0.822\) for the combination and \(S_0(2)=0.700\) for the control. Their complements, the estimated probabilities of an event by two years, are 17.8% and 30.0%.

\[
\Delta(2)=S_1(2)-S_0(2)=0.122,
\]

\[
\mathrm{RR}(2)=\frac{1-S_1(2)}{1-S_0(2)}
=\frac{0.178}{0.300}=0.593.
\]

The relative risk reduction at this fixed time is approximately 40.7%. It is close to 42%, but it is not the same calculation. A hazard describes the immediate event rate among people still event-free. A cumulative event probability by a fixed time is a different quantity.

| Quantity | Calculation from printed estimates | Interpretation |
| --- | ---: | --- |
| Difference in two-year RFS | 12.2 percentage points | Between-group difference in the probability of being recurrence-free and alive at two years |
| Two-year event risk ratio | 0.593 | 17.8% divided by 30.0% |
| Corresponding relative reduction | 40.7% | Relative difference in cumulative event probability by two years |
| Reciprocal of the absolute difference | 8.20 | Point estimate of the number needed to treat at two years |

Table 1. Author calculations from rounded two-year RFS estimates. NNT denotes number needed to treat. The inputs are time-specific survival estimates accounting for censoring, not crude observed proportions calculated directly from patient counts.

Rounding NNT upward gives approximately nine. This is not a guarantee that treating nine particular people saves one life. The outcome is recurrence or death by two years, not lifetime mortality. Subtracting the endpoints of the two arm-specific confidence intervals also does not produce a valid 95% confidence interval for their difference. I have not estimated intervals for the difference or NNT; only point estimates are shown.

## A single number does not describe when benefit appears

In the announcement's prespecified sensitivity analysis, the RFS hazard ratio was 0.99 during the first six months and 0.42 thereafter, with respective 95% confidence intervals of 0.66–1.49 and 0.30–0.58 ([1](#ref-1)). The first interval including one does not establish exactly zero early effect. Equally, the overall hazard ratio cannot be read as a 42% reduction operating unchanged from the first day.

To show what a two-year estimate cannot identify, I constructed two time profiles. These are not reconstructions of the INTerpath-001 survival curves.

Assume a constant control hazard, \(\lambda_0=-\log(0.700)/2\), so that control RFS is 0.700 at two years. Model A reduces that hazard by a constant ratio from the start. Model B has the control hazard for the first 0.5 years and reduces it only afterwards. Time \(t\) is in years. Both treatment models are constrained to reach RFS 0.822 at two years.

\[
S_A(t)=\exp(-r_A\lambda_0 t),\qquad
r_A=\frac{-\log(0.822)}{-\log(0.700)}=0.550,
\]

\[
S_B(t)=\exp\left\{-\lambda_0\min(t,0.5)
-r_B\lambda_0\max(t-0.5,0)\right\},
\]

\[
r_B=\frac{-\log(0.822)-0.5\lambda_0}{1.5\lambda_0}=0.399.
\]

![Hypothetical constant-effect and delayed-effect curves reaching the same two-year RFS. These are not observed trial curves.](shared/mrna-vaccine-rfs-comparison/figures/same-endpoint-different-timing.png)

Figure 1. Author's illustrative calculation. Blue denotes a constant treatment effect, dashed orange no effect during the first six months followed by benefit, and gray the hypothetical control. Both treatment curves reach 82.2% at two years, but their six-month estimates are 95.2% and 91.5%. The figure shows neither confidence intervals nor observed trial data.

Identical two-year estimates can conceal different amounts of early event avoidance. Conversely, a two-year estimate alone cannot recover the onset of benefit. The ratios 0.550 and 0.399 belong to the assumed curves; they are not re-estimates of the trial's Cox hazard ratios.

Nor can the contrast between early and late estimates be attributed solely to the development of an mRNA-induced immune response. The composition of the event-free population also changes with time. A late hazard ratio compares those remaining event-free in each group; it is not a fixed potency coefficient for everyone randomized at baseline. Taking the later estimate out of context cannot justify delaying treatment initiation for six months.

## The same hazard ratio can compare different strategies

SWOG S1801 compared distributing pembrolizumab before and after surgery with giving it entirely after surgery. It enrolled patients with clinically detectable, resectable stage IIIB–IVC melanoma. Its original abstract reports two-year event-free survival of 72% versus 49%. Events also included failures to reach surgery or start postoperative treatment ([2](#ref-2)). The hazard ratio of 0.58 is corroborated in [SWOG's published slide](https://www.swog.org/sites/default/files/docs/2023-04/ScientificImpact_Spr23.pdf#page=1) ([3](#ref-3)).

| Comparison | INTerpath-001 | SWOG S1801 |
| --- | --- | --- |
| Randomization | After complete resection | Before surgery |
| Main question | Adding vaccine to postoperative pembrolizumab | Moving part of pembrolizumab treatment before surgery |
| Main population | Resected stage IIB–IV | Clinically detectable, resectable stage IIIB–IVC |
| Outcome | RFS | Event-free survival (EFS) |
| Failure to reach surgery | Resection completed before randomization | Included in the endpoint |

Table 2. Comparison of the questions addressed by the trials, based on the INTerpath-001 announcement and the S1801 original abstract ([1](#ref-1), [2](#ref-2)). Outcomes have not been standardized to a common population.

INTerpath-001 requires completed surgery before randomization. S1801 includes adverse outcomes on the path to surgery. Calling both control groups “pembrolizumab alone” overlooks this difference in selection and time.

The S1801 investigators' methodological paper argues for EFS measured from randomization when comparing preoperative and postoperative strategies, with attention to different event-measurement times between groups ([4](#ref-4)). The trial clock is not a minor reporting detail. It determines which benefits and harms of the treatment strategy are counted.

NADINA tested another strategy: preoperative nivolumab–ipilimumab followed by surgery and response-driven postoperative treatment, versus postoperative nivolumab. It enrolled resectable, macroscopic stage III melanoma, and postoperative treatment was not identical for every patient in the preoperative group ([5](#ref-5)). Treating “neoadjuvant immunotherapy” as a single intervention hides differences in drug combinations and response-adapted treatment.

Putting two identical hazard ratios beside one another does not demonstrate that adding a vaccine and moving treatment before surgery are equivalent. Dividing hazard ratios from separate trials does not create a direct comparison with aligned populations, endpoint definitions, and randomization times.

## Reading benefits and harms with their denominators

The INTerpath-001 announcement reports grade 3–5 treatment-related adverse events in 14.2% versus 13.4% ([1](#ref-1)). These are not the rates of all adverse events regardless of attribution. A classification asking whether an event is treatment-related differs from one recording events more broadly.

A small difference between those percentages does not prove equivalent safety. This is not an equivalence analysis with a specified margin, and one percentage cannot capture event type, severity, or observation time. When comparing an efficacy NNT with a reciprocal harm difference, the RFS analysis population and safety population must also not be assumed identical.

## What the 42% supports

The supported comparison is the addition of intismeran to pembrolizumab in the postoperative population studied, with improvement in the composite endpoint of recurrence or death. It is neither a 42% reduction in mortality alone nor evidence of equivalence to preoperative immunotherapy.

Separating the overall hazard ratio, the two-year absolute difference, and the timing of benefit makes the treatment result more concrete. Choosing between vaccination and preoperative therapy requires preserving the distinction between the incremental-effect question this trial addressed and the treatment-strategy comparison it did not directly test.

## Data and code availability

The [Python script](shared/mrna-vaccine-rfs-comparison/analysis.py), [calculation output](shared/mrna-vaccine-rfs-comparison/results/calculations.json), and [illustrative-curve CSV](shared/mrna-vaccine-rfs-comparison/results/illustrative-curves.csv) reproduce the arithmetic and Figure 1. They were run with Python 3.12.4 and Matplotlib 3.9.1. No random numbers are used. Patient data and original trial figures are not redistributed.

## References

1. <span id="ref-1"></span>Merck & Co., Inc., Moderna, Inc. Merck and Moderna Will Present Results From Landmark Phase 3 INTerpath-001 Trial for Intismeran Autogene Plus KEYTRUDA (pembrolizumab) at ESMO 2026 Presidential Symposium [Internet]. Merck; 2026 Oct 22 [cited 2026 Oct 30]. [Official announcement](https://www.merck.com/news/merck-and-moderna-will-present-results-from-landmark-phase-3-interpath-001-trial-for-intismeran-autogene-plus-keytruda-pembrolizumab-at-esmo-2026-presidential-symposium/).
2. <span id="ref-2"></span>Patel SP, Othus M, Chen Y, Wright GP Jr, Yost KJ, Hyngstrom JR, et al. Neoadjuvant-Adjuvant or Adjuvant-Only Pembrolizumab in Advanced Melanoma. N Engl J Med. 2023;388(9):813–823. [doi:10.1056/NEJMoa2211437](https://doi.org/10.1056/NEJMoa2211437). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/36856617/).
3. <span id="ref-3"></span>LeBlanc M. Scientific Impact of the CRA [Presentation]. SWOG Cancer Research Network; 2023 Apr 26. Slide 2 (PDF p. 1). [Presentation PDF](https://www.swog.org/sites/default/files/docs/2023-04/ScientificImpact_Spr23.pdf#page=1).
4. <span id="ref-4"></span>Othus M, Sharon E, Wu MC, Sondak VK, Ribas A, Patel SP. Design considerations for randomized comparisons of neoadjuvant-adjuvant versus adjuvant-only cancer immunotherapy when tumor measurement schedules do not align (SWOG S1801). Clin Trials. 2025;22(5):571–577. [doi:10.1177/17407745251321371](https://doi.org/10.1177/17407745251321371). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/40099861/).
5. <span id="ref-5"></span>Blank CU, Lucas MW, Scolyer RA, van de Wiel BA, Menzies AM, Lopez-Yurda M, et al. Neoadjuvant Nivolumab and Ipilimumab in Resectable Stage III Melanoma. N Engl J Med. 2024;391(18):1696–1708. [doi:10.1056/NEJMoa2402604](https://doi.org/10.1056/NEJMoa2402604). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/38828984/).
