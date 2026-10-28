## Introduction {#article-introduction}

The approved intermittent relacorilant–nab-paclitaxel regimen does not involve taking the oral drug every day. Relacorilant is given the day before, on the day of, and the day after each infusion; nab-paclitaxel is administered on Days 1, 8, and 15 of a 28-day cycle. The combination received US approval in March 2026 for platinum-resistant ovarian cancer and related indications ([1](#ref-1)).

Relacorilant antagonizes the glucocorticoid receptor (GR). Its effects on taxane response through GR and changes in paclitaxel exposure through drug interactions require separate consideration ([2](#ref-2)).

Two pharmacokinetic questions arise: how much the combination changes paclitaxel exposure, and how relacorilant's own exposure is positioned around the infusion. Observations addressing the first question do not necessarily predict the interaction after changing the timing of the second drug.

I reanalyzed published aggregate PK from the phase II trial and used relacorilant PopPK coefficients in the FDA review to quantify this distinction. **Dose-normalized paclitaxel AUC₀–₆ was 1.66 times higher with intermittent combination therapy than with monotherapy. Shifting the same nine relacorilant doses by 24 hours changed parent-drug concentrations at infusion without changing cycle AUC.**

Sources were checked on October 22, 2026. Timing changes here are research comparisons using public information, not proposed changes to clinical treatment.

## Question and intended use {#_1}

The **question of interest** is whether the observed increase in early paclitaxel exposure can be evaluated separately from the timing of parent relacorilant exposure, and whether that distinction identifies measurements needed for regimen comparisons.

The **context of use** is public-data PK comparison and clarification of conditions for additional PK sampling. The analysis does not predict the optimal start day, duration of GR inhibition, incidence of myelosuppression, or preservation of clinical efficacy.

The ROSELLA trial and approval materials establish the clinical setting ([1](#ref-1), [3](#ref-3)). I do not decompose the combination's overall clinical effect into GR-mediated pharmacology and increased paclitaxel exposure.

## Observed PK in the phase II trial {#iipk}

The phase II study included intermittent relacorilant, continuous relacorilant, and nab-paclitaxel monotherapy arms ([4](#ref-4)). Geometric means, geometric CVs, and evaluable counts were transcribed from [Supplementary Table S3 of the original study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10602497/).

**Table 1.** Published aggregate paclitaxel PK by treatment arm.

| Arm | Relacorilant | Nab-paclitaxel | Paclitaxel Cmax: geometric mean (geometric CV), n | Paclitaxel AUC₀–₆: geometric mean (geometric CV), n |
| --- | --- | --- | --- | --- |
| Monotherapy | None | 100 mg/m² | 1,038 ng/mL (96.3%), 49 | 1,964 ng·h/mL (83.4%), 43 |
| Intermittent combination | 150 mg the day before, on, and after infusion | 80 mg/m² | 1,574 ng/mL (88.8%), 50 | 2,606 ng·h/mL (70.4%), 33 |
| Continuous combination | 100 mg daily | 80 mg/m² | 1,639 ng/mL (88.1%), 40 | 2,689 ng·h/mL (66.4%), 28 |

All arms used nab-paclitaxel on Days 1, 8, and 15 of 28-day cycles. These concentrations and AUCs concern paclitaxel, not the relacorilant calculations below. The different sample sizes for Cmax and AUC preclude treating them as two measurements from identical sets of individuals.

Intensive samples were collected before dosing and 1, 2, 4, and 6 hours after dosing on Cycle 1 Day 15. The analysis includes treated participants with evaluable PK, not every randomized participant ([4](#ref-4), Supplementary Methods pp. 5, 8). Aggregate tables cannot establish the representativeness of evaluable participants or differences in missingness between arms, and individual covariate adjustment is unavailable. The approximate intervals below correct for neither selection nor missingness. Observed Cmax also need not capture the true peak. This trial analysis and the later periodic steady-state model involve different dosing histories and different drugs; they do not validate each other under matched conditions.

I estimated ratios of dose-normalized geometric means. For geometric mean \(G_g\) and nab-paclitaxel dose \(D_g\) in arm \(g\),

\[
\widehat R_g=\frac{G_g/D_g}{G_0/D_0}.
\]

Writing the geometric CV as a fraction \(v_g\), an independent-arm lognormal approximation gives

\[
SE(\log \widehat R_g)=\sqrt{\frac{\log(1+v_g^2)}{n_g}+\frac{\log(1+v_0^2)}{n_0}}
\]

The 95% interval is \(\exp\{\log\widehat R_g\pm1.96SE\}\). These approximate intervals are reconstructed from aggregate data, not adjusted estimates from original participant records. Comparisons are exploratory without multiplicity correction.

**Table 2.** Dose-normalized ratios versus monotherapy.

| Combination versus monotherapy | Cmax (approximate 95% interval) | AUC₀–₆ (approximate 95% interval) |
| --- | --- | --- |
| Intermittent | 1.90 (1.39–2.58) | 1.66 (1.22–2.25) |
| Continuous | 1.97 (1.42–2.74) | 1.71 (1.25–2.34) |

![Dose-normalized geometric-mean ratios and approximate intervals for paclitaxel](shared/relacorilant-paclitaxel-timing/figures/paclitaxel-contrasts.png)

**Figure 1.** Dose-normalized paclitaxel geometric-mean ratios and approximate 95% intervals calculated from endpoint-specific aggregate phase II results.

These values agree with the approximately twofold dose-normalized Cmax and 1.7-fold AUC increases in the current label ([2](#ref-2)). They come from the same trial, however, and are not an independent validation. Dividing by dose is also a descriptive comparison, not proof of dose proportionality between 80 and 100 mg/m².

**AUC₀–₆ is a partial AUC, not AUC∞.** Inverting its ratio as a clearance ratio would confuse distribution and sampling-window effects with elimination changes. Two aggregate PK endpoints cannot identify a time-dependent model connecting relacorilant concentration, CYP inhibition, and paclitaxel concentration.

## Calculating relacorilant exposure timing {#relacorilant}

The FDA review provides the final coefficients of a two-compartment relacorilant PopPK model ([5](#ref-5)). Absorption combines zero-order input over a finite duration with subsequent first-order absorption.

With dose time \(t_k\), dose \(D_k\), and input duration \(D_1\), input into the gut is

\[
R_g(t)=\sum_k\frac{F_{\rm rel}D_k}{D_1}\mathbf{1}(t_k\le t<t_k+D_1)
\]

For amounts \(A_g,A_c,A_p\),

\[
\begin{aligned}
\frac{dA_g}{dt}&=R_g(t)-k_aA_g,\\
\frac{dA_c}{dt}&=k_aA_g-\frac{CL+Q}{V_c}A_c+\frac{Q}{V_p}A_p,\\
\frac{dA_p}{dt}&=\frac{Q}{V_c}A_c-\frac{Q}{V_p}A_p,\\
C(t)&=1000\frac{A_c(t)}{V_c}\quad[\mathrm{ng/mL}].
\end{aligned}
\]

Amounts are in mg, volumes in L, and time in h. The apparent parameters \(CL,V_c,Q,V_p\) use fasting conditions as their reference. Relative bioavailability \(F_{\rm rel}\) is applied once on the input side relative to that reference.

**Table 3.** Parameters used for the fed-condition reconstruction.

| Parameter | Input for fed conditions | Interpretation |
| --- | --- | --- |
| CL/F | 46.7 L/h | Published final value |
| Vc/F | 220 L | Published final value |
| Q/F | 45.0 L/h | Published final value |
| Vp/F | 850 L | Published final value |
| ka | 0.775 h⁻¹ | Published fed value |
| D₁ | 1.66 h | Published fed value |
| Frel | 2.13 | Fed relative to fasting; not absolute F |

Because I could not establish the original covariate centering and correlation structure, BMI and age multipliers were fixed at 1. This is a conditional reconstruction, not an identified “average patient” or a complete reproduction of the original PopPK analysis. I use fed administration to match the current regimen and do not compare switching to fasting administration.

The implementation convolves inputs through the eigendecomposition of the linear system and includes accumulation from previous cycles. It was checked against independent ODE integration, prolonged repeat-dose calculations, and the relationship between total dose and cycle AUC.

### Agreement with published concentration summaries {#_2}

Starting with zero drug, three fed 150 mg doses 24 hours apart produced a third-dose Cmax of **767 ng/mL** at **2.72 hours** after that dose. The label reports third-dose Cmax of 720 ng/mL and median Tmax of 2.5 hours ([2](#ref-2)).

The Cmax difference was +6.5%. This compares a fixed-condition model with a population summary, not individual-level external validation. I could not establish the integration window for the label AUC of 5,686 ng·h/mL in this check, so I did not treat it as the same endpoint as the calculated 48–72-hour AUC of 6,194 ng·h/mL or score their difference as an error. No parameters were retuned to match the summaries.

The phase II Supplementary Table S3 also reports relacorilant PK in the intermittent arm: C1D15 Cmax of 668 ng/mL and AUC₀–₂₄ of 3,668 ng·h/mL ([4](#ref-4)). Applying the first-cycle dosing history and integrating the same infusion-day 24-hour window gave 744 ng/mL and 5,742 ng·h/mL, respectively, 11.3% and 56.5% above the published geometric means. Although fixed values and population geometric means are different quantities, the AUC discrepancy is substantial. Covariates, food conditions, and individual records could not be matched, leaving its cause unresolved. **This reconstruction has not been validated for absolute exposure.** The ratios below are sensitivities within the model, not predictions of changed patient dosing times with established accuracy.

## Shifting the same nine doses by 24 hours {#924}

Nab-paclitaxel infusions occur at 0, 168, and 336 h in a repeating 28-day cycle. Aligning the infusion start and same-day oral dose is a standardization used here; it does not imply that the label mandates their timing to the hour.

**Table 4.** Dosing conditions compared in the reconstruction.

| Condition | Relacorilant dosing relative to each infusion | Amount per 28 days |
| --- | --- | --- |
| Intermittent, reference | 150 mg at −24, 0, and +24 h | 1,350 mg |
| Early, hypothetical | 150 mg at −48, −24, and 0 h | 1,350 mg |
| Late, hypothetical | 150 mg at 0, +24, and +48 h | 1,350 mg |
| Continuous, published daily condition | 100 mg every 24 hours | 2,800 mg |

Early and Late shift the whole three-dose window; they do not describe management of a missed dose.

![Fixed-condition parent relacorilant concentrations over a cycle and around the first infusion](shared/relacorilant-paclitaxel-timing/figures/parent-timecourse.png)

**Figure 2.** Fixed-condition parent relacorilant concentrations over the 28-day cycle, above, and around the first infusion, below. Gray shading marks the first six hours after infusion starts; vertical lines mark infusion times.

Endpoints are parent-drug cycle AUC, the sum of the three 0–6 h post-infusion AUCs, and mean concentration at the three infusion starts. The six-hour window matches the published paclitaxel partial AUC as a sampling-design choice. It does not assume that GR activity or CYP inhibition is determined exclusively within that window.

**Table 5.** Parent-drug exposure under fixed conditions.

| Condition | Cycle AUC (ng·h/mL) | Sum of 0–6 h post-infusion AUCs (ng·h/mL) | Mean concentration at infusion (ng/mL) |
| --- | --- | --- | --- |
| Intermittent | 61,574 | 9,229 | 58.6 |
| Early | 61,574 | 9,706 | 87.1 |
| Late | 61,574 | 8,354 | 6.1 |
| Continuous | 127,709 | 6,852 | 80.9 |

At periodic steady state in a linear time-invariant model,

\[
AUC_{\rm cycle}=\frac{1000F_{\rm rel}\sum_kD_k}{CL}
\]

Equal cycle AUCs for the three intermittent conditions are therefore required by the model structure, not a new clinical finding. Equal total exposure can coexist with different exposure at and after infusion.

Early increases concentration at infusion, but increases the six-hour post-infusion AUC by only about 5%. Late greatly lowers concentration at infusion, but subsequent absorption of the same-day dose limits the six-hour AUC reduction to about 10%. **One pre-infusion concentration cannot substitute for AUC over the same treatment window.**

Continuous dosing has a larger total dose and 2.07 times the reference cycle AUC. Its six-hour post-infusion parent-drug AUC is nevertheless lower, reflecting the 100 versus 150 mg same-day dose and the arrangement of doses. These calculations do not rank efficacy or safety.

## Conditional simulation of 4,096 individuals {#4096}

I used published IIV values of 54% for CL, 40% for Vc, 30% for Vp, 62% for fed ka, 59% for D₁, and 31% for fed relative F ([5](#ref-5)). Treating these as CVs, I converted them using \(\omega^2=\log(1+CV^2)\) and generated \(\theta_i=\theta\exp(\eta_i)\) from independent normal draws \(\eta\).

This does not reconstruct the full original Ω matrix or joint covariate distribution. It is a conditional sensitivity analysis using published variability, not a virtual cohort established to represent actual patients. There is no residual error; the same draws are paired across all four conditions. Fixed-effect estimation uncertainty is also excluded. Intervals below are between-individual 5th–95th percentiles, not confidence intervals for estimated parameters.

**Table 6.** Paired within-individual exposure ratios relative to Intermittent.

| Endpoint: median [5th–95th percentiles] | Early | Late | Continuous |
| --- | --- | --- | --- |
| Cycle AUC | 1.00 [1.00–1.00] | 1.00 [1.00–1.00] | 2.07 [2.07–2.07] |
| Sum of 0–6 h post-infusion AUCs | 1.05 [1.02–1.13] | 0.90 [0.79–0.96] | 0.75 [0.69–0.95] |
| Mean concentration at infusion | 1.47 [1.33–1.51] | 0.11 [0.01–0.37] | 1.39 [1.01–1.83] |

![Paired parent-drug exposure ratios within conditional individuals](shared/relacorilant-paclitaxel-timing/figures/paired-window-ratios.png)

**Figure 3.** Parent-drug exposure ratios paired within the same conditional individuals. Points show medians; lines show between-individual 5th–95th percentiles.

Cycle AUC ratios have no variability because the shared CL and relative F cancel. This does not imply predictions of this precision for real individuals.

For structural sensitivity, I varied D₁ over 0.5–3 h, ka over 0.4–1.2 h⁻¹, and CL and Vp separately over 0.75–1.25 times their published central values. These ranges are exploratory conditions, not confidence intervals. Six-hour AUC ratios were 1.04–1.07 for Early and 0.88–0.92 for Late, retaining direction over these ranges. They do not encompass the full uncertainty of a population with correlated effects.

## Parent half-life is not the recovery half-life of an interaction {#_3}

I did not directly connect simulated relacorilant concentrations to the observed paclitaxel results. High parent concentrations need not coincide with maximal CYP inhibition or GR effects. The active metabolite CORT125295 is also absent from this model ([2](#ref-2)).

Under Late dosing, the changes in concentration at infusion and six-hour AUC were not proportional. One pre-infusion sample cannot represent the whole effect of shifting dosing times.

The analysis does not estimate the onset or recovery of inhibition. It consequently provides no basis for interpreting parent terminal half-life as the recovery half-life of CYP inhibition. It identifies differences in parent-drug exposure timing, not improvements in drug interactions or GR activity.

## Discussion {#_4}

Published aggregate data show higher early paclitaxel exposure with intermittent combination treatment even after dose normalization. Partial AUC does not, however, establish the change in systemic clearance.

The published relacorilant PopPK coefficients demonstrate how intermittent regimens with equal total doses can change infusion-time concentration and post-infusion exposure differently. Cycle AUC, pre-infusion concentration, and post-infusion AUC answer different questions.

The analysis supports clarification of PK endpoints and sampling conditions. It does not conclude that Early is superior, Late preserves efficacy, or continuous dosing should be avoided.

## Data and code availability {#_5}

`analysis/run_analysis.py` generates aggregate ratios, the conditional 4,096-individual simulation, sensitivity analyses, six CSV files, three figures, and `results.json`. `analysis/test_model.py` checks the ODE implementation, periodic steady state, AUC balance, and aggregate ratios. No new individual-level NLME estimation was performed; the work estimates log-mean differences from aggregate data and simulates published model coefficients.

The distribution excludes original paper figures, supplementary-material figures, regulatory-review figures, and patient data. It contains input coefficients, calculation code, original figures and tables, source details, and file hashes.

[Analysis code, inputs, output tables, and rerun instructions](shared/relacorilant-paclitaxel-timing/relacorilant-analysis.zip)

## References {#article-references}

1. <span id="ref-1"></span>US Food and Drug Administration. FDA approves relacorilant with nab-paclitaxel for platinum-resistant epithelial ovarian, fallopian tube, or primary peritoneal cancer. 2026 Mar 25. [Approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-relacorilant-nab-paclitaxel-platinum-resistant-epithelial-ovarian-fallopian-tube-or).
2. <span id="ref-2"></span>LIFYORLI (relacorilant): US prescribing information. 2026 Mar. [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6fcebfb5-19d6-4f63-b852-999d68a13729). Sections 2 and 12.3.
3. <span id="ref-3"></span>Olawaiye AB, Gladieff L, O'Malley DM, Kim JW, Garbaos G, Salutari V, et al. Relacorilant and nab-paclitaxel in patients with platinum-resistant ovarian cancer (ROSELLA): an open-label, randomised, controlled, phase 3 trial. The Lancet. 2025;405(10496):2205–2216. [doi:10.1016/S0140-6736(25)01040-2](https://doi.org/10.1016/S0140-6736(25)01040-2).
4. <span id="ref-4"></span>Colombo N, Van Gorp T, Matulonis UA, Oaknin A, Grisham RN, Fleming GF, et al. Relacorilant + Nab-Paclitaxel in Patients With Recurrent, Platinum-Resistant Ovarian Cancer: A Three-Arm, Randomized, Controlled, Open-Label Phase II Study. Journal of Clinical Oncology. 2023;41(30):4779–4789. [doi:10.1200/JCO.22.02624](https://doi.org/10.1200/JCO.22.02624). Supplementary Table S3, p. 18.
5. <span id="ref-5"></span>US Food and Drug Administration. LIFYORLI, NDA 220641: Multi-Discipline Review. 2026. [Review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220641Orig1s000MultidisciplineR.pdf). PDF pp. 280–285, especially 283–284.
