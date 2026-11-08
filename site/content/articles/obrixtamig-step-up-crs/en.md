**QOI: Does starting from a low dose reduce CRS?**

**COU: To examine the relationship between dosing schedule and CRS.**

QOI (Question of Interest) is the question this article answers, and COU (Context of Use) is what the result is for. Within the public data, the answer is that cytokine release syndrome (CRS) looked lower with B3, which started at a lower dose, but this cannot be attributed to the starting dose. With B3 (first dose 10 µg/kg), CRS per patient looked lower than with B2 (first dose 30 µg/kg), 50.9% versus 68.4%, while grade ≥3 CRS was the same. However, B3 was a non-concurrent cohort opened after B2, and it also differs in the number of step-up doses, the doses reached, patient characteristics and enrollment period. A causal claim cannot be made.

T-cell engagers (TCEs) can cause CRS with administration, and step-up dosing, which starts at a low dose and increases in stages to the target dose, is used. Obrixtamig (BI 764532) is an IgG-like bispecific TCE that binds DLL3 (delta-like ligand 3) and CD3 (a T-cell surface molecule), and four dosing regimens were evaluated in its phase 1 trial ([1](#ref-1)).

## Abstract

CRS occurred in 54/79 patients (68.4%; 95% credible interval 57.6–77.8) with B2 (two step-up doses, then weekly dosing) and 28/55 (50.9%; 37.9–63.7) with B3 (three step-up doses, three weekly doses, then every 3 weeks). The B3 − B2 difference was −17.3 points (−33.6 to −0.7), and Fisher's exact test gave p = 0.049, a borderline value. This p value is nominal, without correction for multiple comparisons. Grade ≥3 CRS was nearly the same (3/79 and 2/55). Reconstructed from the percentages of a published figure, CRS by administration was concentrated at the first administration (B2: 63% at the first, then 29%, 14% and 3%) and became less frequent at later ones. The denominator is the patients dosed at each administration, not a follow-up of the same patients. The B3 difference disappears if a bias of 0.75 on the logit scale (an odds ratio of about 2.1) is assumed for B3 alone, but there is no empirical basis for a bias of that size. The difference between regimens cannot be attributed to the starting dose.

## Background and objective

Among the 168 patients in phase 1, CRS occurred in 96 (57.1%) and grade ≥3 CRS in 5 (3.0%) ([1](#ref-1), [Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/table/T2/)). The regimens were not assigned concurrently in parallel but were switched in sequence on the basis of earlier cohorts ([1](#ref-1)). Differences in the observed proportions of CRS therefore cannot be called causal effects of step-up dosing. This article sorts out how far the published tallies alone can say anything about the relationship between dosing schedule and CRS. The mathematical models serve to organize the structure of the observations and to show what can be judged.

The analysis plan was not fixed before computing. The per-administration analysis and the conditional PK (pharmacokinetics) contrast were added while looking at published figures and tables, so they are exploratory.

## Methods

### Data

I used [Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/table/T1/) (baseline characteristics), [Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/table/T2/) (CRS by regimen), the descriptions of the regimens in the text and Appendix 2, and the PK description of the phase 1 article ([1](#ref-1)) (data cutoff February 21, 2024). CRS by administration was read from the integer percentages printed in the image of [Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/figure/F1/) of the article and from the numbers of patients at each administration shown in the panel headers. The reading was done on November 7, 2026, with the image (3,968 × 3,049 pixels) displayed, and counts were reconstructed as the rounded product of percentage and number of patients. They are not individual-level data or counts supplied by the authors. Appendix Tables A3 to A7 (corticosteroid and tocilizumab use by grade, ICANS (immune effector cell-associated neurotoxicity syndrome) and others) and individual PK, cytokine and T-cell measurements were not used.

The regimens were defined as follows ([1](#ref-1)). A was a fixed dose every 3 weeks; B1 a fixed dose weekly; B2 two step-up doses on Day 1 and Day 8 followed by the target dose weekly; B3 three weekly step-up doses, three weekly target doses and then target doses every 3 weeks from Week 7. The B2 step-up doses were 30 and 90 µg/kg, and B3 added a 10 µg/kg step-up dose (Appendix 2). The dose ranges were 0.03–90 µg/kg every 3 weeks for A, 0.9–30 µg/kg weekly for B1, and target doses up to 1,530 µg/kg and 1,080 µg/kg (weekly) for B2 and B3 ([1](#ref-1)). Regimens were opened sequentially from A. The original article states that the switch from B1 to B2 and B3 was based on grade ≥2 toxicity from CRS or related symptoms in the previous cohort, and that the switch from A to B1 was triggered by emerging PK data ([1](#ref-1), Methods, Appendix 2).

### Patient-level analysis

With patients as the unit, the number of patients with CRS in regimen $r$, $Y_r$, was modeled as $Y_r \sim \mathrm{Binomial}(n_r, p_r)$ with a Beta(0.5, 0.5) (Jeffreys) prior on $p_r$, treating the regimens independently. Posteriors were summarized with 200,000 draws (seed 20261107). As frequentist references, Fisher's exact test and the Newcombe 95% interval are reported. For the B2 versus B3 comparison, as a sensitivity analysis for non-exchangeability (the cohorts are not in a state where patients and conditions can be swapped and compared), a constant $b$ on the logit (log-odds) scale was added to the B3 posterior and the posterior probability that the true B3 CRS probability is below that of B2 was computed. $b > 0$ corrects for a bias that makes B3 look as if it has less CRS than it truly has. $b$ is an assumed value that stands for several unknown biases in a single constant, and the posterior probability of 0.98 is the value under $b = 0$ (no bias).

### Per-administration analysis

Counts per administration were reconstructed by rounding for each grade from the number of patients at each administration and the percentages. I examined whether the rounding range (±0.5 points) changes any per-grade count; every bar had a single possible per-grade count. The all-grade total, however, is the sum of per-grade rounded counts and can differ by one patient from the count implied by the printed total percentage (at the first administration, 50 versus 51 for B2 and 23 versus 24 for B3). I checked whether this changes the conclusion by repeating the analysis with the counts from the printed totals. The reconstructed grade ≥3 counts summed over administrations matched the Table 2 counts (3 for B2, 2 for B3), and the maximum count at one administration did not exceed the number of patients with CRS in Table 2 (54 for B2 and 28 for B3). These show only that nothing is inconsistent, not that the reconstruction is correct.

Administrations are repeated measurements, and the same patient appears in several administrations, so per-administration proportions are not independent of one another. The denominator of each administration is the patients dosed at that administration, so the population changes. A comparison between regimens at the same administration (for example, the first step-up dose) compares different patients and can be treated as independent.

### Conditional PK

The original article reports from 138 patients that Cmax (maximum concentration) and AUC (area under the concentration–time curve) were dose-proportional and that the terminal half-life was about 7 days (range 5–10 days) ([1](#ref-1)). Individual concentrations are not published and no PK model was fitted. Instead, a conditional schematic calculation was made assuming a 2-hour infusion, one compartment, dose proportionality and half-lives of 5, 7 and 10 days, with concentration expressed in units of dose over volume of distribution (µg/kg equivalents). B2 was given step-up doses of 30 and 90 µg/kg, and B3 10, 30 and 90 µg/kg (apart from the 10 µg/kg step, the B3 step levels are an assumption, because I did not read the dose table of the source). The target dose is an illustrative 360 µg/kg and not a reported value. This calculation shows only accumulation from dosing history and does not reproduce measured concentrations.

## Results

### Dosing schedules of the four regimens

Figure 1 shows the timing of administration in the four regimens.

![Dosing days of regimens A, B1, B2 and B3, separated into step-up doses and target doses.](shared/obrixtamig-step-up-crs/figures/fig1_schedules.png)

Figure 1. Dosing schedules of the four regimens (timing only; the doses differ and are not shown). Constructed from the description in the original article ([1](#ref-1)).

### CRS by regimen

Figure 2 and Table 1 show the probability of CRS by regimen.

![Posterior median and 95% credible interval of CRS probability by regimen, with observed proportions, for any grade and for grade 3 or higher.](shared/obrixtamig-step-up-crs/figures/fig2_regimen_crs.png)

Figure 2. CRS probability by regimen (beta-binomial model, Jeffreys prior). The left panel is CRS of any grade and the right panel grade ≥3 CRS; circles are posterior medians, lines 95% credible intervals and crosses observed proportions. Numbers in parentheses are events/patients.

Table 1. CRS by regimen (`analysis/01_regimen_crs.py`; counts from the original article ([1](#ref-1), [Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/table/T2/))).

| Regimen | Patients | CRS any grade, n (%) | 95% credible interval | CRS grade ≥3, n | 95% credible interval, grade ≥3 |
| --- | ---: | --- | --- | ---: | --- |
| A | 24 | 11 (45.8) | 27.4–65.3 | 0 | 0.0–9.8 |
| B1 | 10 | 3 (30.0) | 9.3–60.7 | 0 | 0.0–21.7 |
| B2 | 79 | 54 (68.4) | 57.6–77.8 | 3 | 1.1–9.8 |
| B3 | 55 | 28 (50.9) | 37.9–63.7 | 2 | 0.8–11.2 |
| A + B1 (no step-up) | 34 | 14 (41.2) | 25.9–57.9 | 0 | 0.0–7.1 |
| B2 + B3 (step-up) | 134 | 82 (61.2) | 52.8–69.2 | 5 | 1.4–8.0 |
| All | 168 | 96 (57.1) | not computed | 5 | not computed |

That CRS in A and B1, which had no step-up (41%), looks lower than in B2 and B3, which did (61%), may reflect the difference in dose. The maximum doses of A and B1 are 90 and 30 µg/kg, far below the maximum target doses of 1,530 and 1,080 µg/kg in B2 and B3. A and B1 were the earliest cohorts and moved on to the next regimen because of toxicity or PK, so differences in enrollment period, patient selection and management are mixed in as well. Comparing A and B1 as low-dose administration without step-up with B2 and B3 does not demonstrate an effect of step-up. Grade ≥3 CRS was rare, 0 to 3 patients, and the intervals are wide (for grade ≥3, 3/79 for B2 and 2/55 for B3).

### B2 versus B3

B2 and B3 differ in the first step-up dose (30 versus 10 µg/kg), the number of step-up doses (two versus three), the range of target doses and the enrollment period. Figure 3 and Table 2 show CRS by administration and Figure 4 the B3 − B2 difference.

![Stacked bars of CRS by grade at each administration for B2 and B3 with 95% credible intervals; the highest value is at the first step-up dose and it falls with later administrations.](shared/obrixtamig-step-up-crs/figures/fig3_crs_by_administration.png)

Figure 3. CRS by administration (counts reconstructed from the percentages of the original [Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/figure/F1/) ([1](#ref-1)); bars are proportions, colors are CRS grades, and lines are 95% credible intervals). The intervals come from a beta-binomial model (Jeffreys prior) that treats each administration independently, but the same patient appears in several administrations, so the administrations are not independent. The number of patients at each administration is shown on the horizontal axis.

Table 2. CRS by administration in B2 and B3 (reconstructed counts; `analysis/02_by_administration.py`). Patients at risk are the patients dosed at that administration, not a follow-up of the same patients.

| Regimen | Administration | Patients at risk | CRS, n (%) | 95% credible interval |
| --- | --- | ---: | --- | --- |
| B2 | Step-up 1 | 79 | 50 (63.3) | 52.4–73.3 |
| B2 | Step-up 2 | 72 | 21 (29.2) | 19.6–40.4 |
| B2 | Target 1 | 66 | 9 (13.6) | 7.0–23.4 |
| B2 | Target 2 | 61 | 2 (3.3) | 0.7–10.1 |
| B2 | Target 3 | 60 | 0 (0.0) | 0.0–4.1 |
| B2 | Continuous target | 55 | 1 (1.8) | 0.2–8.2 |
| B3 | Step-up 1 | 55 | 23 (41.8) | 29.5–54.9 |
| B3 | Step-up 2 | 49 | 10 (20.4) | 11.0–33.2 |
| B3 | Step-up 3 | 45 | 7 (15.6) | 7.2–28.2 |
| B3 | Target 1 | 42 | 5 (11.9) | 4.7–24.1 |
| B3 | Target 2 | 38 | 2 (5.3) | 1.1–15.8 |
| B3 | Target 3 | 34 | 0 (0.0) | 0.0–7.2 |
| B3 | Continuous target | 30 | 1 (3.3) | 0.4–14.5 |

At the patient level, the observed proportion of CRS with B3 was 17.3 points lower than with B2 (posterior median, 95% credible interval −33.6 to −0.7; Newcombe 95% interval −33.2 to −0.7), the posterior probability that B3 is lower under $b = 0$ was 0.98 and Fisher's exact test gave p = 0.049. This p value is borderline, is one of several comparisons (any grade, grade ≥3, first administration) and is nominal, with no correction for multiple comparisons. Grade ≥3 CRS was 3/79 (3.8%) with B2 and 2/55 (3.6%) with B3, a difference of −0.1 points (−6.7 to 7.7; Newcombe interval −7.4 to 8.9). At the first administration the observed proportion with B3 was 21.3 points lower than with B2 (−37.4 to −4.3), with a posterior probability of 0.99 that B3 is lower under $b = 0$. Using the counts implied by the printed total percentages (51/79 for B2 and 24/55 for B3), the difference is −20.7 points (−37.0 to −3.8), and the conclusion does not change.

![B3 minus B2 differences for any-grade CRS by patient, grade 3 or higher CRS by patient and CRS at the first administration, and the posterior probability that B3 CRS is lower than B2 under an assumed bias.](shared/obrixtamig-step-up-crs/figures/fig4_b2_vs_b3.png)

Figure 4. Observed differences between regimens (left) and sensitivity to non-exchangeability (right; any-grade CRS). The horizontal axis $b$ on the right is a constant added to the logit (log-odds) of the B3 CRS probability; $b = 0$ is no bias, and $b > 0$ corrects for a bias that makes B3 look as if it has less CRS than it truly has.

In the sensitivity analysis, the posterior probability that B3 has lower CRS moves from 0.98 with no bias to 0.74 at a bias of 0.5, 0.48 at 0.75 and 0.23 at 1.0. A logit value of 0.75 corresponds to an odds ratio of about 2.1. Regarding B3 as equivalent to B2 requires a bias in which the CRS odds of B3 are underestimated about twofold. The value $b$ stands for unknown, combined confounding in a single constant; its actual size has no empirical basis, and a twofold figure carries no judgment on whether it is large or small. On baseline characteristics, the proportions of ECOG (Eastern Cooperative Oncology Group performance status) 0 are close at 27.8% (22/79) and 29.1% (16/55), and prior PD-1/PD-L1 inhibitor use is close at 50.6% and 49.1%. However, B3 has 14.5% (8/55) missing ECOG, fewer brain metastases (23.6%, 13/55, versus 38.0%, 30/79 in B2), a lower share of small cell lung cancer (41.8% versus 51.9%) and a higher median age (64 versus 60 years) ([Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/table/T1/) of the original article ([1](#ref-1))). Which of these relates to CRS cannot be confirmed from the public data.

### CRS falls with repeated administration (the rise in concentration is an assumed calculation)

In B2, CRS fell from 63% at the first step-up dose (30 µg/kg) to 29% at the second (90 µg/kg), 14% at the first target dose and 3% at the second target dose. The dose rose threefold and then further toward the target dose. In B3, too, it fell: 42%, 20%, 16%, 12% and 5%. Concentrations are not measured; they come from a conditional schematic calculation with assumed doses and half-lives. With the assumed target dose of 360 µg/kg and B2 step-up doses of 30 and 90 µg/kg (half-life 7 days), the end-of-infusion concentration at the second step-up dose is 3.50 times that at the first, and at the first target dose 13.75 times (3.38–3.62 times and 13.28–14.23 times for half-lives of 5–10 days; `analysis/03_conditional_pk.py`). In B3, with assumed step-up doses of 10, 30 and 90 µg/kg and a target dose of 360 µg/kg, the first target dose gives 41.37 times the first administration (39.9–42.9 times). These ratios depend on the assumed dose steps.

![CRS proportion at each administration for B2 and B3 together with an assumed dose-proportional conditional concentration on a logarithmic axis for half-lives of 5, 7 and 10 days; CRS proportion falls while concentration rises.](shared/obrixtamig-step-up-crs/figures/fig5_crs_vs_conditional_pk.png)

Figure 5. CRS at each administration and an illustrative concentration (a schematic calculation from assumed doses and half-lives, not measured concentrations).

What is observed is that CRS concentrates at the first administration and rarely occurs at later ones. Of the 54 patients with CRS in B2, 50 had it at the first administration (reconstructed from the figure percentages). The original article also states that CRS occurred mainly at the first two to three infusions and almost entirely during step-up dosing, with onset at a median of 16 hours after infusion (range 3–54 hours) and resolution within a median of 2 days ([1](#ref-1)).

Several explanations are possible for this concentration. The first is a reduced response with repeated dosing (mechanism unidentified). The second is selection, in which patients prone to CRS leave early and CRS looks less frequent among those who remain. The third is a change in tumor burden, in which the first administration reduces the target cells available for T-cell activation. The fourth is redistribution of T cells at the first administration or reduced expression of the target; the fifth is the effect of management such as premedication and early intervention; and the sixth is a difference in assessment or reporting. In B2 the number evaluated falls from 79 to 72, 66 and 61, and treatment discontinuations for CRS, ICANS and infusion-related reaction each occurred at the 30 µg/kg step-up dose in B2 ([1](#ref-1)). However, I did not check the numbers of patients leaving by reason, so the contribution of CRS-related discontinuation to the decrease across administrations is unknown. The public data cannot separate these. A model with the immune response state as a latent variable (CRS probability depending on exposure and response state) was not fitted, because per-administration public data alone cannot identify the rates of decline and recovery.

## Discussion

To the question of whether starting low reduces CRS, the public data give three observations. First, with B3, whose first dose was 10 µg/kg, CRS looked lower at the first administration (42%) and overall (51%) than with B2, whose first dose was 30 µg/kg (63%, 68%). Grade ≥3 CRS was the same (3.6% and 3.8%). Second, in both B2 and B3 CRS concentrated at the first administration and was less frequent at later administrations even as the dose rose. Third, CRS in A and B1, which had no step-up, looks low, but their maximum doses are lower by orders of magnitude.

The lower CRS in B3 cannot be specified as an effect of the starting dose. B3 has more step-up doses (three), was opened after B2, differs in the range of target doses, has lower proportions of brain metastases and small cell lung cancer and has more missing ECOG. Because B3 was opened later, changes over calendar time, such as premedication, CRS management, practice in grading and reporting, site experience and selection of enrolled patients, cannot be separated from the starting dose. I did not check in the public material whether these differed. In the sensitivity analysis, a roughly twofold bias in the CRS odds of B3 was needed to bring it back to equality with B2. The public data cannot establish whether a bias of that size exists. Grade ≥3 CRS was about the same in B2 and B3, and these few events give no evidence that the number of step-up doses or the starting dose reduced severe CRS.

The difference between patient-level and administration-level units also needs care. Table 1 and Figure 4 use patients as the unit and compare independent patients. Table 2 and Figure 3 use administrations as the unit, and the same patient appears in several administrations. Per-administration intervals do not account for correlation between administrations. This analysis compares CRS frequencies across administrations; it does not estimate recurrence of CRS within the same patient.

The B2 versus B3 comparison changed more than the starting dose. The public data also do not allow the effect of step-up to be evaluated against a regimen with the same target dose and no step-up.

## Limitations

- **Non-concurrent, non-randomized:** the regimens were opened in sequence and switched on the basis of the preceding cohort. Differences between cohorts are not an effect of the starting dose.
- **Confounding over time:** because B3 was opened after B2, changes over calendar time in premedication, CRS management, practice in grading and reporting, site experience and selection of enrolled patients cannot be separated from the starting dose. I did not check these in the public material.
- **Confounding by dose:** the maximum doses of A and B1 are lower than those of B2 and B3 by orders of magnitude. The low CRS in A and B1 does not show an effect of step-up.
- **Reconstructed counts:** the per-administration counts were reconstructed from the integer percentages of the original Figure 1 and the numbers of patients. They are not counts supplied by the authors. They did not contradict the grade ≥3 counts of Table 2, but that is not a validation. The all-grade total can differ by one patient from the count implied by the printed total.
- **Sensitivity analysis:** $b$ is a single constant with no empirical basis for the size of the unknown combined bias. The posterior probability of 0.98 is the value under $b = 0$, and Fisher's p = 0.049 is a nominal borderline value without correction for multiple comparisons.
- **Discontinuation:** I did not check how much of the decrease in the number of patients across administrations is due to CRS-related discontinuation.
- **CRS by dose level:** CRS at each dose level and the distribution of target doses in each regimen were not used. The relationship between dose and CRS was not estimated quantitatively.
- **PK:** there are no individual concentrations and no PK model was fitted. The conditional schematic calculation rests on assumed doses and half-lives. The step-up doses other than the 10 µg/kg of B3 and the target dose are assumptions, and the ratios depend on them. With target-mediated clearance, anti-drug antibodies, dependence on tumor burden or T-cell redistribution, linear accumulation may not hold.
- **Latent variable:** the model of immune response state was not fitted because it is not identifiable. Reduced response, selection and change in tumor burden, among others, cannot be separated.
- **Follow-up:** the median follow-up at data cutoff was 29 days (range 3–408 days), which is short ([1](#ref-1)).
- **Scope checked:** data on other TCEs such as tarlatamab were not included in the range I checked. I also did not read Appendix Tables A3 to A7 of the original article.
- **Exploratory:** the analysis plan was not fixed in advance. The p value is exploratory.

## Conclusion

On the QOI (does starting from a low dose reduce CRS), the public data support the following. With B3, whose first dose was 10 µg/kg, CRS looked lower at the first administration (42%) and overall (51%) than with B2 at 30 µg/kg (63%, 68%), while grade ≥3 CRS was the same (3.6% and 3.8%). The lower value for B3 is a comparison between non-concurrent cohorts, and the number of step-up doses, the doses reached, patient characteristics and enrollment period also differ, so it cannot be attributed to the starting dose. In each of B2 and B3, CRS concentrates at the first administration and is less frequent at later ones even as the dose increases. This is consistent with step-up dosing being a design that places a low dose at the first administration, when CRS occurs, but reduced response, selection and change in tumor burden, among others, cannot be separated. A causal claim that starting low reduces CRS cannot be made from the public data.

## Data and code availability

The re-run materials (scripts in `analysis/`, input CSVs and the provenance record in `inputs/`, tables, figures and logs in `outputs/`) are in the [companion archive](shared/obrixtamig-step-up-crs/obrixtamig-step-up-crs-companion.zip). `crs_regimen.csv` and `baseline_table1.csv` hold counts transcribed from the tables of the original article ([1](#ref-1)), and `crs_by_administration.csv` holds percentages and patient numbers read from Figure 1 (the reading method is in `inputs/PROVENANCE.md`). Re-run: `python analysis/01_regimen_crs.py && python analysis/02_by_administration.py && python analysis/03_conditional_pk.py && python analysis/04_figures.py` (Windows 11, Python 3.12.4, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). The random seed is 20261107.

## References

<span id="ref-1"></span>1. Wermke M, Gambardella V, Kuboki Y, Felip E, Sanmamed MF, Alese OB, et al. Phase I dose-escalation results for the delta-like ligand 3/CD3 IgG-like T-cell engager obrixtamig (BI 764532) in patients with delta-like ligand 3+ small cell lung cancer or neuroendocrine carcinomas. J Clin Oncol. 2025;43(27):3021–3031. [doi:10.1200/JCO-25-00363](https://doi.org/10.1200/JCO-25-00363). [PMC12440289](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440289/).
