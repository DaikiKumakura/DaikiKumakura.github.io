# Conditional pasritamig regimen comparison

## Scope

This analysis compares maintenance dosing of 300 mg every 42 days with 150 mg every 21 days. It is a conditional linear, time-invariant PK calculation, not a fit to patients or a reconstruction of the sponsor's model.

The actual PAGE population model includes two compartments and nonlinear target-mediated disposition. Complete numerical PK parameters were not available in the public poster. The calculations do not estimate response probabilities, toxicity, JNJ-9401 PK or a recommended dose.

## Reproduction

Run python regimen_model.py with Python 3.12 and matplotlib 3.9.1. Verified on CPython 3.12.4, matplotlib 3.9.1. The script resolves paths relative to itself, uses no network access and has no random sampling.

Outputs: regimen-results.json, regimen-steady.png/.svg, regimen-early.png/.svg. The right panel of regimen-early uses a separate continuous hypothetical slow-half-life sweep of 12–22 days, with a one-day fast component; the 24 parameter combinations in the JSON use the four reported slow-half-life scenarios and both fast-half-life settings.

## Source inputs

- 15.2-day mean terminal half-life after IV dosing, step-up doses and target-dose timing: Stein MN et al. J Clin Oncol. 2025;43:2515–2526. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12288886/), PK section and dosing schedule.
- 13.8- and 16.5-day half-life summaries: Dai J et al. ASCO GU 2026, poster 172, [Table 2](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/asco-gu/phase-1-safety-efficacy-pharmacokinetics-pk-and-pharmacodynamics-pd-of-pas.pdf#page=1).
- 18.3-day terminal half-life and first-eight-week exposure metric: T'jollyn H et al. PAGE 2026 abstract 12211. [Abstract](https://www.page-meeting.org/Abstracts/model-informed-drug-development-to-support-dose-selection-of-pasritamig-a-klk2xcd3-bispecific-antibody-in-metastatic-castration-resistant-prostate-cancer/), [poster](https://www.page-meeting.org/wp-content/uploads/pdf_abstracts/2026/8ad6b057fde94ae2a2fa7c37f3925aac.pdf).

These are separate reported summaries, not a pooled estimate or confidence interval. Fast half-lives of 1 and 3 days and fast-component AUC fractions of 0, 0.25 and 0.5 are hypothetical structural sensitivity inputs, not estimates. There are 24 parameter combinations; the zero-fast-fraction cases duplicate their profiles across the two irrelevant fast-half-life settings (20 distinct kernels).

## Definitions and derivations

For a monoexponential curve let k = ln(2)/half-life and let interval T be 42 or 21 days. With equal dose rate, concentration divided by the common steady mean is:

    c(t) = k T exp(−kt) / (1−exp(−kT)),  0 ≤ t < T.

Its mean over the period is one. Peak and trough are the right and left limits at the dosing event, respectively. Ratios of split/reference peaks and troughs simplify to (1+a)/2 and (1+1/a)/2, where a = exp(−21k).

For a threshold z relative to the common steady mean, the fraction of a period above it is:

    max(0, min(1, ln(peak/z)/(kT))).

This is a geometric coverage metric, not an established pharmacodynamic model or clinical response probability. Thresholds 0.5 and 1.5 are illustrative, not estimated effective concentrations.

The mixture response is h(t) = sum_j w_j lambda_j exp(−lambda_j t), with nonnegative weights summing to one. Its total integral is normalized to one. Weights are AUC fractions, not concentration-amplitude fractions. For actual concentration units this kernel would require an unknown scale; that scale is held constant and cancels in all reported ratios.

For s > 0, F(s) = sum_j w_j (1−exp(−lambda_j s)); F(s)=0 for s≤0. A dose D at time d contributes D F(56−d) to normalized initial AUC. Normalized AUC values in the JSON are not clinical h·µg/mL values.

Day 1 = time 0, Day 8 = time 7 and Day 15 = time 14. The endpoint time 56 is Day 57; its dose adds zero area to [0,56]. This continuous-time convention represents 56 days from treatment start and does not reproduce all patient-level time-stamp handling in the published analysis.

Shared step-up contribution S = 3.5 F(56)+18 F(49).

    Reference A = S + 300 F(42).
    Split A = S + 150 F(42)+150 F(21).
    Difference = 150 (F(42)−F(21)) ≥ 0.

The sign holds for any nonnegative linear unit-dose response, not just the chosen exponentials. Faster components shrink this particular early-exposure difference.

The exposure-matching first target dose is:

    L = 300−150 F(21)/F(42).

The two target doses in the window then sum to more than 300 mg. This matches early AUC, not early total dose, steady peaks, troughs, safety or response. The alternative first target dose of 300 mg followed by 150 mg on time 35 gives 450 mg of target-dose input inside the window and increases early AUC.

At steady state, linear superposition gives:

    C21(t) = [C42(t) + C42((t+21) mod 42)]/2.

This preserves the common mean and smooths extrema. It does not establish clinical equivalence. In particular, free-drug exposure, nonlinear disposition, immune-cell dynamics and the second agent are outside this comparison.

## Verification

The private editorial validator independently integrates concentration profiles numerically, checks threshold coverage by a dense time grid, verifies the steady-state phase identity and checks bilingual tables and equations. These verify arithmetic under the assumptions, not actual patient PK or clinical outcomes.
