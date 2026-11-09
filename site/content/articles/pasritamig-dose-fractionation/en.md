Replace 300 mg every six weeks with 150 mg every three weeks. The dose administered over the long run is unchanged. Does that allow peak concentrations to fall while preserving the treatment’s effects?

On November 8, 2026, Mark Wildgust posted about pasritamig plus JNJ-9401 for prostate cancer [(1)](#ref-1). According to the sponsor release, 11 of 15 patients at the recommended regimen achieved a reduction of at least 50% in prostate-specific antigen (PSA). Both agents were given every six weeks: pasritamig 300 mg intravenously and JNJ-9401 200 mg subcutaneously [(2)](#ref-2).

I examine this development through a different question: dose fractionation. A hypothetical comparison changes pasritamig alone to half the dose at half the interval and asks what must be held constant to call exposure equivalent. The calculations show that equal steady-state mean concentrations do not imply equal mean concentrations during the first eight weeks. That initial window is also the exposure window used in a public exposure–response analysis.

## Scope and sources

The sponsor release was the source for clinical findings from combination trial NCT06095089. I could not examine the full SITC 2026 slides. The pharmacokinetic (PK) calculations below are not an analysis of combination-treated patients.

The pasritamig monotherapy phase I paper selected 3.5 mg on Day 1, 18 mg on Day 8 and 300 mg on Day 15, followed by dosing every six weeks. It reported a mean terminal half-life of approximately 15.2 days after intravenous administration [(3)](#ref-3).

A PAGE 2026 presentation subsequently described a population PK model with two compartments and linear and nonlinear elimination, together with an analysis relating mean exposure over the first eight weeks to confirmed PSA response. The authors concluded that their analyses supported 300 mg every six weeks [(4)](#ref-4). However, [Figures 1 and 3 of the public poster](https://www.page-meeting.org/wp-content/uploads/pdf_abstracts/2026/8ad6b057fde94ae2a2fa7c37f3925aac.pdf#page=1) do not provide a complete set of numerical PK parameters for reproducing the drug’s concentration profiles.

I do not fill those gaps to reconstruct that model. Instead, an explicitly linear comparison model examines how dosing history and the observation window change the meaning of the comparison. This does not establish the clinical efficacy or safety of 150 mg every three weeks.

## Methods

### Separating maintenance dose rate from concentration shape

The reference is 300 mg every 42 days; the split regimen is 150 mg every 21 days. Both maintenance dose rates are \(300/42=150/21=7.14\) mg/day. PK is assumed linear and time-invariant, with intravenous administration approximated as an instantaneous input.

In a monoexponential model, let \(k=\ln 2/t_{1/2}\) have units of day\(^{-1}\) and let \(\tau\) be the interval in days. Dividing concentrations by the common steady-state mean \(\bar C_{\mathrm{ss}}\), with \(t=0\) immediately after each dose, gives:

\[
\frac{C_{\mathrm{ss}}(t)}{\bar C_{\mathrm{ss}}}
=\frac{k\tau e^{-kt}}{1-e^{-k\tau}},\qquad 0\leq t<\tau
\]

Clearance and volume, which set absolute concentrations, are not used: they are held identical between regimens and cancel in the ratios. Concentrations in the figures are therefore dimensionless rather than µg/mL.

The central example uses a half-life of 15.2 days. Sensitivity scenarios also use 13.8 and 16.5 days from [Table 2 of the ASCO GU 2026 poster](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/asco-gu/phase-1-safety-efficacy-pharmacokinetics-pk-and-pharmacodynamics-pd-of-pas.pdf#page=1) [(5)](#ref-5), and 18.3 days from PAGE [(4)](#ref-4). These are representative summaries from different sources and analyses, not a distribution of patient variability or a confidence interval.

### Examining dependence on a distribution component

To avoid relying entirely on a single exponential, extend the unit-dose response to a nonnegative mixture of exponential components:

\[
h(t)=\sum_j w_j\lambda_j e^{-\lambda_j t},
\qquad w_j\geq0,\quad \sum_jw_j=1.
\]

Total AUC is normalized to one, so \(w_j\) is the fraction of AUC contributed by component \(j\), not its concentration amplitude fraction. The slow component uses the reported half-life scenarios. A hypothetical fast component has a half-life of one or three days and an AUC fraction of 0%, 25% or 50%, producing 24 combinations. Fast-component values are structural sensitivity assumptions, not empirical estimates.

### Calculating the first 56 days separately

Day 1 is \(t=0\), Day 8 is day 7 and Day 15 is day 14. Both regimens retain the same 3.5 mg and 18 mg step-up doses, then differ from the first target dose onward. The reference receives 300 mg on day 14; the split regimen receives 150 mg on days 14 and 35. Both next receive a dose on day 56, which is Day 57.

The integration window is \(0\leq t<56\) days. This defines a continuous 56-day window starting on Day 1; a dose at day 56 contributes no AUC to it. It does not reproduce every detail of patient-level processing in the published model.

Let \(F(s)=\int_0^s h(u)\,du\) be normalized AUC up to \(s\) days after a unit dose. The shared step-up contribution is \(S=3.5F(56)+18F(49)\), giving:

\[
A_{\mathrm{ref}}=S+300F(42),\qquad
A_{\mathrm{split}}=S+150F(42)+150F(21)
\]

Here \(A\) is normalized exposure with a common concentration-scaling factor omitted, not a patient AUC in h·µg/mL. Because both areas are divided by the same 56 days, their ratio is also a mean-concentration ratio. Equal maintenance dose rates do not give later doses the same amount of time to contribute within the window.

## Results

### Equal steady means can give opposite threshold coverage

For the monoexponential model, write \(a=e^{-21k}\). The split/reference peak ratio is \((1+a)/2\), and the trough ratio is \((1+1/a)/2\). In the central 15.2-day example, peaks fall to 0.692 times the reference and troughs rise to 1.803 times the reference. These are steady-state ratios, not values after the first dose.

A higher trough does not itself establish better efficacy. Table 1 treats an unknown activity threshold as a ratio to the common steady-state mean and calculates the fraction of time above it.

**Table 1. Fraction of time above hypothetical thresholds. Monoexponential model with a 15.2-day half-life.**

| Threshold / common steady mean | 300 mg every 6 weeks | 150 mg every 3 weeks |
| --- | ---: | ---: |
| 0.5 | 78.4% | 100.0% |
| 1.5 | 21.1% | 3.7% |

The thresholds are not measured efficacy values. Splitting favors coverage when the required concentration is low, but can shorten time above a threshold that requires a high peak. Neither time fraction is a patient response rate.

![Normalized steady concentrations and threshold-dependent coverage](shared/pasritamig-dose-fractionation/regimen-steady.png)

**Figure 1. Smoothing concentrations at an unchanged maintenance dose rate.** Original conditional calculations. The left panel normalizes concentrations by their common steady-state mean; the right shows time above hypothetical thresholds. No absolute effective concentration was estimated.

Smoothing is not specific to a single exponential. Under linear, time-invariant PK, the 21-day regimen’s concentration equals the average of the 42-day profile and a copy shifted by 21 days:

\[
C_{21}(t)=\frac{C_{42}(t)+C_{42}((t+21)\bmod42)}{2}.
\]

This preserves the steady mean while reducing the maximum and raising the minimum. The relation does not identify which concentration metric determines efficacy.

### Initial eight-week exposure is not equivalent

Table 2 reports the monoexponential scenarios. Splitting from the first target dose reduces initial AUC to 85.6–88.0% of the reference. Describing the maintenance dose rates as equal would omit this 12.0–14.4% difference.

**Table 2. Conditional fractionation calculations relative to 300 mg every six weeks. Initial AUC covers days 0–56 and includes step-up doses.**

| Half-life, days | Steady peak ratio | Steady trough ratio | First-56-day AUC ratio | Exposure-matching first target dose, mg |
| --- | ---: | ---: | ---: | ---: |
| 13.8 | 0.674 | 1.936 | 0.880 | 188.7 |
| 15.2 | 0.692 | 1.803 | 0.871 | 191.6 |
| 16.5 | 0.707 | 1.708 | 0.864 | 193.9 |
| 18.3 | 0.726 | 1.608 | 0.856 | 196.7 |

What if the initial target dose remains 300 mg, followed by 150 mg starting on day 35? Initial AUC then exceeds the reference, with ratios of 1.320–1.345. Target-dose input within the window rises from 300 mg to 450 mg, so this comparison does not preserve the initial total dose.

I therefore solved an inverse problem: use \(L\) mg for the first target dose and 150 mg 21 days later, choosing \(L\) to match initial AUC:

\[
S+LF(42)+150F(21)=S+300F(42),
\qquad
L=300-150\frac{F(21)}{F(42)}.
\]

The solutions are 188.7–196.7 mg, as shown in Table 2. These are exposure-matching solutions within the assumed model, not calculated safe or recommended doses. They do not imply that approximately 190 mg should be used clinically. They show how the initial target dose can add an early-exposure difference to a dosing-frequency comparison.

![Early exposure and structural sensitivity to a hypothetical fast component](shared/pasritamig-dose-fractionation/regimen-early.png)

**Figure 2. Matching initial exposure and testing structural sensitivity.** Original conditional calculations. Left: the 15.2-day model compares the reference, splitting from the first target dose, and splitting with an initial dose chosen to match early AUC. The pointwise jump after the Day 57 dose does not contribute to days 0–56 AUC. Right: hypothetical sensitivity with a one-day fast half-life and a continuous slow-half-life range of 12–22 days; the separation of the curves is not a confidence interval.

Initial split-regimen AUC remained below the reference across all 24 structural sensitivity scenarios. The direction actually follows from a stronger result than these selected numerical examples. For a nonnegative response, \(F(42)\geq F(21)\), so:

\[
A_{\mathrm{ref}}-A_{\mathrm{split}}
=150\{F(42)-F(21)\}\geq0.
\]

Within the linear model, any exposure between 21 and 42 days after a unit dose makes the difference positive. Increasing the contribution of a fast distribution component narrows the difference, but does not remove the distinction between a steady mean and an initial period that is still accumulating exposure.

## Discussion

### The exposure window changes the comparison

The PAGE exposure–response analysis uses individual mean exposure over the first eight treatment weeks [(4)](#ref-4). Explaining it with “half the dose at half the interval gives the same AUC” would substitute a steady-state mean for that initial mean. A comparison intended to isolate dosing frequency would also change exposure through the first target dose.

The useful distinction is between several conditions that can be held constant. Maintenance dose rate, steady-state mean concentration and initial eight-week mean concentration are not interchangeable. Even matching initial means does not match peaks, troughs or periods without activity.

I also do not translate the published exposure–response relationship into response rates for this hypothetical split regimen. The PAGE abstract describes the exposure metric as free drug, and the actual population model includes nonlinear target-mediated elimination [(4)](#ref-4). It is not identical to this normalized linear concentration model. The authors’ assessment of limited gains from increasing exposure near 300 mg does not validate half-dose fractionation as equivalent.

### One agent’s trough cannot explain the combination

Pasritamig targets KLK2×CD3, while JNJ-9401 targets PSMA×CD28. KLK2 denotes kallikrein-related peptidase 2, and PSMA denotes prostate-specific membrane antigen [(2)](#ref-2). Smoothing pasritamig concentrations does not establish that their temporal overlap with JNJ-9401 activity is preserved.

The PAGE authors also invoke reduced T-cell exhaustion and activation-induced cell death when discussing six-week dosing [(4)](#ref-4). That hypothesis differs from assuming that more time above a concentration threshold is always beneficial. The present threshold calculations do not model immune-cell recovery, so increased coverage at a low threshold cannot be read as a clinical benefit.

Likewise, PSA reductions in 15 combination-treated patients do not identify the causal effect of adding JNJ-9401 or establish a survival benefit [(2)](#ref-2). This analysis lacks individual PK observations, exposure–response covariates and JNJ-9401 absorption and elimination parameters. It cannot replace a drug-specific immune-response model by declaring one hypothetical regimen the clinical winner.

In this linear model, equal-dose fractionation preserves the maintenance mean exposure. It does not preserve concentration shape, threshold coverage or exposure during the first eight weeks. The question for evaluating six-week dosing therefore shifts from whether the interval looks long relative to the half-life to which exposure and time course the comparison actually holds constant. Without that distinction, correct PK arithmetic can answer the wrong question about dosing frequency.

## Data and code availability

The [calculation code](shared/pasritamig-dose-fractionation/regimen_model.py), unrounded [results](shared/pasritamig-dose-fractionation/regimen-results.json) and [analysis notes](shared/pasritamig-dose-fractionation/regimen-readme.md) provide the derivations and execution instructions. Assumed conditions are included in the code and results. Individual patient data and source figures are not redistributed.

[Download code, results and figures](shared/pasritamig-dose-fractionation/pasritamig-dose-fractionation.zip)

## References

<a id="ref-1"></a>
1. Wildgust M [@MAWildgust]. [Post describing pasritamig plus JNJ-9401 at SITC 2026; editorial description] [X post]. 2026 Nov 8 [cited 2026 Nov 9]. Available from: [original post](https://x.com/MAWildgust/status/2119408231529275687).

<a id="ref-2"></a>
2. Johnson & Johnson. Johnson & Johnson reports 73% PSA response rate with investigational pasritamig-based immunotherapy combination in advanced prostate cancer [press release]. PR Newswire. 2026 Nov 8 [cited 2026 Nov 9]. Available from: [sponsor release](https://www.prnewswire.com/news-releases/johnson--johnson-reports-73-psa-response-rate-with-investigational-pasritamig-based-immunotherapy-combination-in-advanced-prostate-cancer-302932750.html). Reporting SITC 2026 abstract 1175.

<a id="ref-3"></a>
3. Stein MN, Vinceneux A, Robbrecht D, Doger B, Autio KA, Schweizer MT, et al. Pasritamig, a first-in-class, bispecific T-cell engager targeting human kallikrein 2, in metastatic castration-resistant prostate cancer: a phase I study. J Clin Oncol. 2025;43(22):2515–2526. doi: [10.1200/JCO-25-00678](https://doi.org/10.1200/JCO-25-00678). [Open-access full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12288886/).

<a id="ref-4"></a>
4. T’jollyn H, Valenzuela B, Woot de Trixhe X, Jaiprasart P, Villalobos V, Wang SC, et al. Model-informed drug development to support dose selection of pasritamig, a KLK2×CD3 bispecific antibody, in metastatic castration-resistant prostate cancer [conference abstract and poster]. PAGE 34; 2026. Abstract 12211, poster III-036. Available from: [official abstract](https://www.page-meeting.org/Abstracts/model-informed-drug-development-to-support-dose-selection-of-pasritamig-a-klk2xcd3-bispecific-antibody-in-metastatic-castration-resistant-prostate-cancer/) and [poster PDF](https://www.page-meeting.org/wp-content/uploads/pdf_abstracts/2026/8ad6b057fde94ae2a2fa7c37f3925aac.pdf).

<a id="ref-5"></a>
5. Dai J, Liu N, Li Y, Yu Z, Zhang S, Kawahara T, et al. Phase 1 safety, efficacy, pharmacokinetics (PK) and pharmacodynamics (PD) of pasritamig in Asian population with metastatic castration-resistant prostate cancer (mCRPC) [conference poster]. ASCO Genitourinary Cancers Symposium; 2026 Feb 26–28; San Francisco, CA. Poster 172. Available from: [public poster](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/asco-gu/phase-1-safety-efficacy-pharmacokinetics-pk-and-pharmacodynamics-pd-of-pas.pdf). Table 2.
