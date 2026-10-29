A published population pharmacokinetic (PopPK) model was used to compare hypothetical redistributions of gedatolisib 540 mg per 28 days, as 180 mg × 3 doses or 135 mg × 4 doses. In the periodic state, the maximum concentration ratio was about 0.75 and the cycle AUC ratio was 1.000. The equal cycle AUC is an identity of mass balance in a linear model, so a different distribution shows up in the peak and in week-4 exposure. The share of cycle AUC falling in week 4 (from the Day 22 dose start to just before the next cycle) rose from about 1.9% to 25%. Across 2,048 conditional virtual individuals, the within-individual ratio of week-4 AUC had a median of 13.2 (5th–95th percentile 7.6–25.0). An exposure–response analysis that uses cycle AUC as its only exposure metric therefore cannot distinguish the two distributions. Efficacy, toxicity, mucosal recovery and the superiority of either regimen were not calculated.

Public materials were checked on October 29, 2026. The numbers below were newly calculated from published coefficients. This is neither a re-estimation from patient-level data nor a proposal for a regimen to replace the approved one.

## Introduction {#article-introduction}

On July 14, 2026, the US Food and Drug Administration (FDA) approved gedatolisib with fulvestrant, with or without palbociclib, for adults with HR (hormone receptor)-positive, HER2-negative locally advanced or metastatic breast cancer without a detected PIK3CA mutation whose disease had progressed after endocrine therapy ([1](#ref-1)). The regimen is 180 mg as a 30-minute intravenous infusion on Days 1, 8 and 15 of a 28-day cycle, with no dose in week 4 ([1](#ref-1)). Gedatolisib was created as a dual PI3K and mTOR inhibitor (development code PKI-587) ([2](#ref-2), [3](#ref-3)). A conference abstract describes it as targeting all class I PI3K isoforms and both mTORC1 and mTORC2 ([4](#ref-4)). In the phase 3 trial VIKTORIA-1, patients with PIK3CA wild-type disease that had progressed after a CDK4/6 inhibitor and an aromatase inhibitor received 180 mg once weekly for 3 weeks followed by 1 week off (Days 1, 8 and 15) ([5](#ref-5)). In that trial stomatitis was reported in 69.2% of the gedatolisib–palbociclib–fulvestrant group and 56.9% of the gedatolisib–fulvestrant group, with grade 3 in 19.2% and 12.3% ([5](#ref-5)).

As the basis for 3 weeks on and 1 week off, the applicant cites reports that synchronized, intermittent inhibition of the PI3K/AKT/mTOR pathway and CDK4/6 could allow the immune system to recover during the off week and support antitumor activity ([3](#ref-3), PDF p. 87). In the phase 1b study B2151009, the applicant states that the 3-weeks-on, 1-week-off group (Arm D) had a higher overall response rate (56% vs 25%) and a longer median progression-free survival (12.9 vs 5.1 months) than the 180 mg weekly group (Arm C) ([3](#ref-3), PDF p. 97). The FDA noted that the two groups were not randomized, had different eligibility criteria, and that follow-up in the weekly group was shorter (3.4 vs 9.5 months), so the comparison should be interpreted with caution ([3](#ref-3), PDF p. 98).

Splitting these 540 mg into four doses of 135 mg lowers the peak immediately after each infusion in proportion to the single dose under linear PK. But the fourth dose is also a dose in the rest week. Is its effect settled by saying that the 4-week AUC is the same? AUC is the area under the concentration–time curve.

Optimization of the regimen is also an open issue on the regulatory side. The FDA assessed that the approved dosage is not optimized and said it will require, as a postmarketing requirement, a randomized dosage-comparison trial to evaluate whether an alternative dosage provides comparable activity with a better safety and tolerability profile ([3](#ref-3), PDF p. 88). One reason is that an exposure–safety analysis using Cmax (maximum concentration) as the metric showed positive relationships with Grade ≥3 stomatitis/mucositis and other events across the wide range of 10–319 mg ([3](#ref-3), PDF p. 88). If this relationship is causal and transfers to a new schedule, a distribution that lowers Cmax moves toward lower risk on that side. On the other hand, a distribution that also doses in the rest week moves in the opposite direction from the rationale the applicant gives for the rest week. This article counts how large, in PK terms, these two movements are.

### Question and comparison conditions {#_1}

The quantity of interest (QOI) is how the peak and week-4 exposure change when the same 540 mg per 28 days is divided into three or four doses.

The context of use (COU) is a simulation from public information to organize, in pharmacokinetic (PK) terms, how redistributing doses including the rest week changes exposure. It does not estimate parameters from new patient data. It must not be used to choose a therapeutic or trial dose, to conclude that efficacy is maintained, that stomatitis improves, or that a rest week is unnecessary.

**Table 1. Dosing conditions compared**

| Condition | Dosing days | 28-day total | Role |
| --- | --- | ---: | --- |
| 180 mg × 3 | Day 1, 8, 15 | 540 mg | Reference to the recommended regimen |
| 135 mg × 4 | Day 1, 8, 15, 22 | 540 mg | Hypothetical redistribution of the same total |
| 180 mg × 4 | Day 1, 8, 15, 22 | 720 mg | Condition to separate the effect of a larger total |

All doses are 30-minute infusions. The dose and days of the reference condition follow the labeled regimen ([1](#ref-1), [6](#ref-6)). The weekly 135 mg condition is the hypothesis compared in this analysis and is not an approved alternative regimen. The 180 mg × 4 condition corresponds in dose and interval to the 180 mg weekly group of B2151009 (Arm C) ([3](#ref-3), PDF p. 87); how that group's cycles were delimited was not checked. Concomitant-drug PK and dosing schedules were not calculated.

## Methods {#article-methods}

### Sources and scope of checking {#sources-scope}

The materials whose full text I checked are the prescribing information ([6](#ref-6)), the FDA review ([3](#ref-3)) and the VIKTORIA-1 paper ([5](#ref-5)). I converted the review PDF to text and searched all of it, and checked the table of model coefficients against the page image. The ASCO 2026 abstract ([4](#ref-4)) was checked in its abstract only, and the other papers ([2](#ref-2), [7](#ref-7), [8](#ref-8), [9](#ref-9)) were checked within their abstracts and bibliographic information. The FDA approval notice ([1](#ref-1)) was retrieved on October 29, 2026 to check approval date, indication and dosing days, and compared with the prescribing information ([6](#ref-6)). An erratum to VIKTORIA-1 was issued in 2026; I did not check its content. The review mixes the applicant's statements (Applicant's Position) with the FDA's assessments, and I cite them separately.

### Implementation of the published model {#_2}

The pharmacokinetics section of the prescribing information lists a volume of distribution of 393 L, clearance of 8 L/h and a half-life of 36 h ([6](#ref-6), section 12.3). The same section states that Cmax and AUC increase dose-proportionally over 10–319 mg and that no accumulation is seen with once-weekly dosing ([6](#ref-6), section 12.3). The linear model here assumes proportionality over this range. A one-compartment model built only from these summary values misses the concentration immediately after infusion by a wide margin. I therefore implemented the four-compartment model published in the FDA review, which is based on 4,238 observations from 605 participants ([3](#ref-3), PDF pp. 86, 227–228). The FDA reproduced the applicant's analysis without significant discordance and judged the model appropriate for deriving individual exposure metrics ([3](#ref-3), PDF p. 239).

Let A1 be the amount in the central compartment and A2, A3 and A4 the amounts in the peripheral compartments. Amounts are in mg, time in h and volumes in L.

\[
\frac{dA_1}{dt}=R_{\mathrm{in}}(t)-\frac{CL+Q_2+Q_3+Q_4}{V_1}A_1+
\sum_{j=2}^4\frac{Q_j}{V_j}A_j,
\]
\[
\frac{dA_j}{dt}=\frac{Q_j}{V_1}A_1-\frac{Q_j}{V_j}A_j,\quad j=2,3,4,
\qquad C(t)=1000\frac{A_1}{V_1}.
\]

C is the plasma concentration in ng/mL. Rin is D/0.5 mg/h during the infusion and 0 otherwise. The coefficients were reused from [Table 66](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219908Orig1s000MultidisciplineR.pdf#page=236) of the review (PDF page 236, printed page 235) ([3](#ref-3), Table 66). CL is clearance, V is volume and Q is intercompartmental clearance.

**Table 2. Published coefficients used**

| Published coefficient | Estimate | Published 95% interval / treatment here | Unit |
| --- | ---: | --- | --- |
| cl | 7.99 | 7.77–8.22 | L/h |
| v1 | 7.31 | 6.86–7.75 | L |
| q2 | 4.77 | 4.33–5.21 | L/h |
| v2 | 8.21 | 7.7–8.73 | L |
| q3 | 3.46 | 3.29–3.62 | L/h |
| v3 | 98.1 | 90.1–106 | L |
| q4 | 0.741 | 0.671–0.812 | L/h |
| v4 | 279 | 236–322 | L |
| Variance of ηcl | 0.0507 | Fixed here | log scale |
| Variance of ηv1 | 0.195 | Fixed here | log scale |
| Variance of ηq4 | 0.204 | Fixed here | log scale |

The covariate effect on CL was

\[
CL_i=7.99\left(\frac{WT_i}{70}\right)^{0.246}
\left(\frac{AST_i}{32}\right)^{-0.124}\exp(\eta_{CL,i})
\]

where WT is body weight (kg) and AST is aspartate aminotransferase (IU/L). The main analysis fixes 70 kg and AST 32 IU/L, and places log-normal variability with the published variances on V1 and Q4 as well. The original observations, individual estimates and the joint distribution of patient characteristics were not obtained. This is neither a new nonlinear mixed-effects (NLME) estimation nor a reconstruction of the source population.

Table 2 gives three variances but no covariances. The main analysis assumes independence, and I also examined correlations of −0.5 and +0.5 between CL and Q4. Residual error is not added to the latent exposures.

The review also cautions that the model's simulations may produce wider variability than observed: in a prediction-corrected visual predictive check ([9](#ref-9)), the observed 95% interval was narrower than the predicted interval ([3](#ref-3), PDF p. 228). The 5th–95th percentiles below describe conditional virtual individuals. They are neither validated prediction intervals for a clinical population nor confidence intervals for the coefficients.

### Periodic state and first cycle {#auc}

The cycle AUC is calculated in the periodic state, in which dosing has continued for many cycles and the state after 28 days equals the state at the start of the cycle. In a linear model,

\[
AUC_{28\mathrm{d}}=1000\frac{\text{total dose over 28 days}}{CL}
\]

where the numerator is the total dose over 28 days. For the same individual receiving 540 mg, this is identical for three and four doses. It is a mass-balance identity and not a finding that efficacy is the same.

The first cycle starts with a zero body amount and adds no carryover from earlier cycles. Because of the amount remaining in slow distribution phases, the AUC over the first 28 days then differs even for the same total dose. Week 4 is defined as 504–672 h after the start of the cycle.

### Virtual individuals and sensitivity analyses {#article-virtual-individuals}

The random seed was fixed at 20261023, and the two 540 mg conditions were applied to the same 2,048 virtual individuals. Generating virtual individuals from the estimates of a published population model and simulating with them is a general use of population modeling ([7](#ref-7)). For each individual, the metric for 135 mg × 4 was divided by that for 180 mg × 3 to give a within-individual ratio, and the median and 5th–95th percentiles of the 2,048 ratios are reported. Coefficient uncertainty was examined by replacing each of eight distribution and elimination coefficients (cl, v1, q2, v2, q3, v3, q4, v4) one at a time with an end of its published 95% interval. Body weight of 50 and 100 kg and AST of 16 and 64 IU/L were also varied separately. The covariate exponents and the variances of interindividual variability were fixed in this sensitivity analysis.

## Results {#article-results}

### The label's 393 L is not the central volume {#393-l}

In the review's model, the central volume is 7.31 L and the sum with the three peripheral volumes is 392.62 L ([3](#ref-3), Table 66). The labeled 393 L is close to this sum and is not the central volume.

![Difference between the published model and a simple model that uses 393 L as the central volume.](shared/gedatolisib-rest-week/figures/model-check.png)

**Figure 1.** Left: calculation for a single 180 mg infusion. The dotted line is the labeled mean Cmax (maximum concentration), a summary value and not an observed curve. Right: the tail of the published model after a single dose. Both are calculations for the reference individual (70 kg, AST 32 IU/L, no interindividual variability), and the figure shows neither a threshold nor clinical washout.

The simple model that uses 393 L as the central volume gave a peak of about 456 ng/mL, whereas the published four-compartment model gave about 14,791 ng/mL for the reference individual. This is about 8% higher than the labeled mean Cmax of 13,700 ng/mL ([6](#ref-6), section 12.3). Because this compares a reference individual with a clinical population mean, it is not called an independent predictive validation. The value for the reference individual also does not equal the population mean that includes interindividual variability; I did not calculate the population mean Cmax in the virtual individuals.

### Lower peak, with exposure shifted to week 4 {#4}

Table 3 shows the metrics in the periodic state.

**Table 3. Exposure of the reference individual under periodic conditions**

| Periodic condition | Maximum concentration (ng/mL) | End-of-cycle concentration (ng/mL) | AUC 28 d (ng·h/mL) | Week 4 AUC (ng·h/mL) |
| --- | ---: | ---: | ---: | ---: |
| 180 mg × 3 | 14,802 | 5.80 | 67,584 | 1,288 |
| 135 mg × 4 | 11,103 | 9.16 | 67,584 | 16,896 |
| 180 mg × 4 | 14,803 | 12.22 | 90,113 | 22,528 |

Values are from `outputs/tables/typical-regimens.csv`. The periodic maximum (14,802 ng/mL) includes carryover from the previous cycle and therefore differs slightly from the single-dose peak (14,791 ng/mL).

Dividing 540 mg into four doses lowered the peak by about 25%. Week-4 AUC, however, rose from about 1,288 to 16,896 ng·h/mL. As a share of the cycle AUC, this is a change from about 1.9% (1,288/67,584) to 25% (16,896/67,584). That each week carries 25% of the AUC when the same dose is repeated weekly follows from the symmetry of the cycle and is not a drug-specific finding. By contrast, the reference share of about 1.9% and the magnitude of the low concentrations depend on the model. The roughly 13-fold ratio of week-4 AUC should be read with the small denominator of the reference condition in mind. The numerator (the 135 mg single dose divided by clearance) is stable because the relative standard error of the clearance estimate is small at 1.44% ([3](#ref-3), Table 66). The denominator depends on the amount remaining in the slow distribution phases, and its estimate depends on the volume and clearance of the slow peripheral compartment (relative standard errors 7.84% and 4.84%) ([3](#ref-3), Table 66).

At the end of the cycle, the interval since the last infusion is about 14 days for 180 mg × 3 and about 7 days for 135 mg × 4. The higher end-of-cycle concentration follows from this difference in interval and does not indicate improved efficacy. The 180 mg × 4 condition has a 33% larger total and is therefore kept separate from comparisons of the same total with a different distribution.

This condition corresponds to the 180 mg weekly group of the phase 1b study. For the reference individual, compared with 180 mg × 3 the cycle AUC is 33% higher and the week-4 AUC is about 17-fold (22,528/1,288). The difference in clinical outcomes between this group and the 3-weeks-on, 1-week-off group therefore includes these differences in exposure as well as the presence or absence of the rest week ([3](#ref-3), PDF pp. 97–98).

In the first cycle, the 28-day AUC is not identical even with the same total. For the reference individual it was about 65,670 ng·h/mL for 180 mg × 3 and about 65,057 ng·h/mL for 135 mg × 4.

![Periodic dosing and the first two cycles starting from a zero body amount.](shared/gedatolisib-rest-week/figures/regimen-profiles.png)

**Figure 2.** The shaded area on the left is week 4, the 168 h from the Day 22 dose start to just before the next cycle. The right panel runs from the first dose to day 56. The vertical axes are logarithmic. Both panels are model calculations for the reference individual and are not measured concentration curves.

### Differences that persist in virtual individuals and what remains uncertain {#_3}

Table 4 shows within-individual ratios of 135 mg × 4 to 180 mg × 3 in 2,048 virtual individuals (seed 20261023).

**Table 4. Within-individual ratios in virtual individuals (CL–Q4 correlation 0)**

| 135 mg × 4 / 180 mg × 3 | Median within-individual ratio | 5th–95th percentile |
| --- | ---: | --- |
| Maximum concentration | 0.750 | 0.750–0.750 |
| Minimum concentration in the cycle | 1.613 | 1.543–1.909 |
| Cycle AUC 0–28 d | 1.000 | 1.000–1.000 |
| Week 4 AUC | 13.170 | 7.602–24.997 |
| First-cycle AUC 0–28 d | 0.991 | 0.981–0.996 |

Values are from `outputs/tables/paired-summary.csv`. The peak ratio clusters near 0.75, which I interpret as follows: in a linear model the single dose is reduced by 25%, and the residual contribution to the peak one week later is small. A narrow range of ratios does not mean that highly precise clinical predictions were validated.

![Conditional ratios when the correlation between CL and distribution to the slow peripheral compartment is varied.](shared/gedatolisib-rest-week/figures/paired-sensitivity.png)

**Figure 3.** Points are medians and lines are the 5th–95th percentiles (n = 2,048). The vertical axis is the within-individual ratio of 135 mg × 4 to 180 mg × 3. The correlations are sensitivity conditions for an unpublished covariance, not estimates.

The week-4 AUC ratio had a median of about 13.2 (5th–95th percentile about 7.6–25.0) at correlation 0. At −0.5 it was about 13.2 (about 6.7–28.6), and at +0.5 about 13.2 (about 9.0–20.7) (`outputs/tables/paired-summary.csv`). The direction of the effect of redistribution did not change with the correlation, but the width of tail-dependent metrics moved. The three interindividual variabilities and covariates alone do not reproduce the joint distribution of real patients.

Table 5 shows the range of ratios when each of the eight distribution and elimination coefficients was replaced one at a time with an end of its published 95% interval.

**Table 5. Range of ratios when coefficients are changed one at a time**

| Metric | Range of ratios when coefficients are changed one at a time |
| --- | --- |
| Maximum concentration ratio | 0.750–0.750 |
| End-of-cycle concentration ratio | 1.511–1.674 |
| Week 4 AUC ratio | 12.391–13.987 |

Values are from `outputs/tables/fixed-parameter-sensitivity.csv`. This is neither a joint confidence interval nor a range covering all structural uncertainty. When body weight of 50 and 100 kg or AST of 16 and 64 IU/L were varied separately, the week-4 AUC ratio was about 12.0–14.4 (`outputs/tables/covariate-scenarios.csv`). Correlations among background factors and clinical dosing decisions were not modeled.

### The slow tail does not match the labeled 36 h half-life {#36}

The half-lives obtained from the eigenvalues of the four-compartment model were about 0.27, 1.78, 27.7 and 286 h. The slowest mathematical phase does not match the labeled 36 h. The slowest eigenvalue of a multiphase model is not automatically identified with the elimination half-life observed clinically. The terminal half-life is a quantity governed by the extent of distribution as well as by clearance, and it contributes to accumulation and the time to equilibrium ([8](#ref-8)). The materials I checked do not state from which interval of the observed time series the labeled 36 h was obtained.

The review describes the clinical AUC of 21,400 ng·h/mL as a steady-state 0–168 h value ([3](#ref-3), PDF p. 40). In the reference condition of the implemented model, the 168 h AUC of each of weeks 1–3 was about 21,870–22,277 ng·h/mL, which is of the same order but not identical. The source does not give a value for a specific week or for the same reference individual, so this too is not used as independent validation. The single-dose AUC∞ of about 22,528 ng·h/mL should not be compared directly with the 168 h AUC.

In particular, low concentrations during the rest period depend on the slow compartments and on the carryover assumption. Because this is not an analysis that revalidated the tail against re-obtained observed time series, these concentrations do not allow calculation of how many days until the pharmacological effect disappears or the mucosa recovers.

## Discussion {#article-discussion}

### Rest-week exposure and existing exposure–response analyses {#_4}

With weekly 135 mg dosing, the peak fell while week-4 exposure increased. The number of doses per cycle also rose from three to four. The difference from the current 3-weeks-on, 1-week-off regimen cannot be expressed by the peak alone.

An ASCO 2026 abstract reported that in PopPK and exposure analyses pooling phase 1b, phase 3 and other trials, using Cmax, Cmin and cumulative first-cycle AUC, no clear relationship was found with change in tumor size, progression-free survival or best overall response, and no statistically significant and/or clinically relevant relationship was found with safety endpoints. It concluded that the current 180 mg, 3-weeks-on/1-week-off schedule is supported ([4](#ref-4)). The FDA also assessed the exposure–response for efficacy as flat but asked for cautious interpretation because the data come from a single dose level ([3](#ref-3), PDF p. 98). For safety, in an analysis using Cmax, the FDA reported positive relationships over the wide range of 10–319 mg with Grade ≥3 stomatitis/mucositis, any-grade nausea and vomiting, and Grade ≥3 events leading to dose reduction or discontinuation ([3](#ref-3), PDF pp. 88, 258). The FDA also stated that some safety endpoints that were significant in the pooled analysis were not significant within the individual arms of CELC-G-301 ([3](#ref-3), PDF p. 245). The abstract and the FDA statements differ in dose range, exposure metric and treatment of strata, and do not reach the same conclusion. Because I checked only the abstract, the cause of the difference cannot be identified. However, the absence of a clear association does not mean that a rest week is unnecessary.

The PK model here contains neither the onset nor the recovery of events such as stomatitis. Whether exposure shifted into week 4 would impede recovery or contribute to maintaining efficacy was not calculated, and no clinical superiority of weekly 135 mg is shown. Within the materials I checked, I found no report that calculated week-by-week exposure when the same total dose is given in a different distribution. This article provides only the minimal PK numbers that fill that gap.

### What this calculation changes {#implications}

An exposure–response analysis that uses cycle AUC as its exposure metric cannot distinguish the two distributions in this article. For the same individual the ratio of cycle AUC is 1.000, whereas the maximum concentration is 0.75-fold, the minimum concentration in the cycle is about 1.6-fold and the week-4 AUC is about 13-fold. To evaluate a difference in distribution, one must therefore first decide which exposure metric determines the response. In the FDA's analysis showing a relationship between Cmax and safety ([3](#ref-3)), a distribution that lowers Cmax moves toward lower risk if the relationship is causal and transfers to the new schedule. In the applicant's hypothesis that bases efficacy on the existence of a rest week ([3](#ref-3)), a distribution that increases week-4 exposure moves in the opposite direction. The two grounds point in opposite directions, and PK alone does not decide which prevails.

The assessment that the exposure–response for efficacy is flat is based on the spread of exposure within the trial population on 3 weeks on and 1 week off ([3](#ref-3), PDF p. 98). In this calculation, the week-4 exposure of 135 mg × 4 is about 13-fold that of 180 mg × 3 in the same individual (5th–95th percentile 7.6–25.0). This within-individual ratio and the spread of between-individual exposure are different quantities; their magnitudes were not compared. Carrying this flat relationship over to a distribution that also doses in week 4 and reading it as "efficacy does not change" is therefore not supported within the scope of this article.

The comparison of the weekly and rest-week groups in B2151009 likewise does not show the contribution of the rest week alone. Weekly dosing has a 33% larger cycle AUC and an about 17-fold week-4 AUC. The comparison was not randomized and the follow-up differed ([3](#ref-3), PDF p. 98). The difference in clinical outcomes therefore combines the presence of a rest week, the total dose and differences between populations. The PK difference separates into total dose and last-week exposure, and this article supplies only the size of that difference.

### Limitations {#article-limitations}

The calculation reuses published coefficients without patient-level observations. The tail and the low concentrations during the rest period were not validated against observed time series. The size of the week-4 AUC ratio depends on the small week-4 AUC of the reference condition, that is, on the estimate of the slow distribution phases. The covariance is unpublished and was set as a sensitivity condition. The virtual individuals are conditional and are not a predictive distribution for a clinical population. Joint confidence intervals were not calculated.

Linearity assumes the dose proportionality over 10–319 mg shown in the prescribing information and time-invariant clearance. The calculation concerns plasma concentration and is not linked to concentration at the site of action, the duration of inhibition of the PI3K/mTOR pathway, or the onset and recovery of stomatitis. Concomitant-drug PK, treatment interruptions and pharmacodynamics (PD) were not evaluated. The applicant's statements in the review are cited separately from the FDA's assessments, but the details of the applicant's analyses were not checked.

## Conclusion {#article-conclusion}

In the virtual conditions from the published PopPK model, redistributing 540 mg per 28 days as 135 mg × 4 lowered the peak by about 25%, while the share of cycle AUC in week 4 rose from about 1.9% to 25%. The equal cycle AUC is a mass balance of the linear model and does not mean that rest-week exposure is preserved. Because of this difference, an exposure–response analysis that uses cycle AUC as its only exposure metric cannot distinguish the two distributions. Which distribution is better depends on whether Cmax or rest-week exposure determines the response, and the materials I checked do not settle this. This conclusion depends on the published coefficients, on the interindividual variability assumed independent, and on the carryover assumption. Recovery from stomatitis, efficacy and the superiority of either regimen lie outside the scope of this PK calculation.

## Data and code availability {#_5}

The distribution contains the JSON recording the published coefficients and assumptions, the calculation code, the test code, seven CSV files, three figures, and records of results and the Python environment (Python 3.12.4, numpy 1.26.4, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). The random seed is 20261023. The analysis is run with `python analysis/run_analysis.py` and the tests with `python -m unittest discover -s analysis -p "test_model.py"`; neither requires a network connection or the original FDA PDF. The original FDA PDF, original figures and individual data are not redistributed. The SHA-256 of the consulted PDF is recorded. The code is under the MIT license.

The periodic solution of the linear system was checked against an independent dosing-event calculation by matrix exponential, in nine implementation tests covering first-cycle and periodic AUC, the weekly representation, and peak and minimum values. The implementation tests are distinct from clinical predictive validation of a new regimen.

[Analysis code, inputs, summary tables and rerun instructions](shared/gedatolisib-rest-week/schedule-analysis.zip)

## References {#_6}

1. <span id="ref-1"></span>U.S. Food and Drug Administration. FDA approves gedatolisib with fulvestrant, with or without palbociclib, for HR-positive, HER2-negative locally advanced or metastatic breast cancer [Internet]. Silver Spring (MD): FDA; 2026 Jul 14 [cited 2026 Oct 29]. Available from: [https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-gedatolisib-fulvestrant-or-without-palbociclib-hr-positive-her2-negative-locally](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-gedatolisib-fulvestrant-or-without-palbociclib-hr-positive-her2-negative-locally)
2. <span id="ref-2"></span>Venkatesan AM, Dehnhardt CM, Delos Santos E, Chen Z, Dos Santos O, Ayral-Kaloustian S, et al. Bis(morpholino-1,3,5-triazine) derivatives: potent adenosine 5'-triphosphate competitive phosphatidylinositol-3-kinase/mammalian target of rapamycin inhibitors: discovery of compound 26 (PKI-587), a highly efficacious dual inhibitor. J Med Chem. 2010;53(6):2636–2645. [doi:10.1021/jm901830p](https://doi.org/10.1021/jm901830p).
3. <span id="ref-3"></span>U.S. Food and Drug Administration, Center for Drug Evaluation and Research. NDA/BLA multi-disciplinary review and evaluation, NDA 219908, REVTORPYK (gedatolisib) [Internet]. Silver Spring (MD): FDA; 2026 [cited 2026 Oct 29]. Available from: [https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219908Orig1s000MultidisciplineR.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219908Orig1s000MultidisciplineR.pdf)
4. <span id="ref-4"></span>Pistilli B, Hurvitz SA, Gunn L, Cacovean A, Rajagopalan P, Gorbatchevsky I, et al. Assessment of gedatolisib (geda) pharmacokinetics (PK), drug-drug interactions (DDI), and exposure-safety and exposure-efficacy relationships [conference abstract]. J Clin Oncol. 2026;44(16_suppl):e13069. [doi:10.1200/JCO.2026.44.16_suppl.e13069](https://doi.org/10.1200/JCO.2026.44.16_suppl.e13069).
5. <span id="ref-5"></span>Hurvitz SA, Layman RM, Curigliano G, André F, Cristofanilli M, Kim SB, et al. VIKTORIA-1 trial of gedatolisib plus fulvestrant with or without palbociclib in hormone receptor-positive/HER2-negative/PIK3CA wild-type advanced breast cancer. J Clin Oncol. 2026;44(12):1108–1119. [doi:10.1200/JCO-25-02643](https://doi.org/10.1200/JCO-25-02643).
6. <span id="ref-6"></span>Celcuity Inc. REVTORPYK (gedatolisib) for injection, for intravenous infusion: prescribing information [Internet]. Bethesda (MD): DailyMed; revised 2026 Jul [cited 2026 Oct 29]. Available from: [https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=959d73ef-831f-4005-956c-210702270bda](https://www.dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=959d73ef-831f-4005-956c-210702270bda)
7. <span id="ref-7"></span>Mould DR, Upton RN. Basic concepts in population modeling, simulation, and model-based drug development. CPT Pharmacometrics Syst Pharmacol. 2012;1:e6. [doi:10.1038/psp.2012.4](https://doi.org/10.1038/psp.2012.4).
8. <span id="ref-8"></span>Toutain PL, Bousquet-Mélou A. Plasma terminal half-life. J Vet Pharmacol Ther. 2004;27(6):427–439. [doi:10.1111/j.1365-2885.2004.00600.x](https://doi.org/10.1111/j.1365-2885.2004.00600.x).
9. <span id="ref-9"></span>Bergstrand M, Hooker AC, Wallin JE, Karlsson MO. Prediction-corrected visual predictive checks for diagnosing nonlinear mixed-effects models. AAPS J. 2011;13(2):143–151. [doi:10.1208/s12248-011-9255-z](https://doi.org/10.1208/s12248-011-9255-z).
