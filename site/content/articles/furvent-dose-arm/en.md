Sources checked on October 14, 2026. FURVENT results were available as a company topline announcement and trial registration, not a complete scientific report. Reported values, approximations calculated from them and my interpretations are distinguished below.

On October 6, 2026, ArriVent announced that the phase 3 FURVENT trial had missed its primary endpoint in first-line NSCLC with EGFR exon 20 insertion mutations ([1](#ref-1)). The trial compared firmonertinib 240 mg, 160 mg and chemotherapy. Discussion on X suggested that adding the lower-dose arm in the spirit of FDA's Project Optimus reduced the high-dose sample and compromised power.

Public numbers allow an approximate event-count and fixed-enrollment power comparison. They do not reveal enough of the design to establish why the trial failed.

## Reported results

FURVENT was an open-label randomized phase 3 trial, originally planning approximately 375 patients allocated 1:1:1. It began in June 2023. The primary endpoint was progression-free survival (PFS) by blinded independent central review (BICR) ([2](#ref-2)). The company reported 398 enrolled patients ([1](#ref-1)).

Table 1. Company-reported FURVENT topline results ([1](#ref-1)).

| | 240 mg | 160 mg | Chemotherapy |
|---|---|---|---|
| Median PFS, BICR | 11.0 months | 8.4 months | 9.5 months |
| HR vs chemotherapy, BICR (95% CI) | 0.75 (0.55–1.02), p=0.0654 | 0.91 (0.67–1.25) | — |
| Median PFS, investigator assessment | 11.1 months | 8.3 months | 7.1 months |
| HR vs chemotherapy, investigator assessment | 0.61 (0.46–0.81) | 0.86 (0.65–1.14) | — |
| Confirmed response rate, BICR | 60% | 35% | 33% |
| Grade ≥3 adverse events, any causality | 52% | 53% | 55% |
| Grade ≥3 treatment-related adverse events | 26% | 22% | 40% |

Overall survival was immature and no numerical result was given. Alpha allocation across comparisons, the assumed effect and planned event count were not public. These omissions limit every calculation below. The reported p=0.0654 exceeds 0.05 even without splitting alpha between the two doses.

## Inferring the event count

A conventional 95% HR interval is the log estimate plus or minus 1.96 standard errors. The interval 0.55–1.02 for 240 mg versus chemotherapy gives a log-HR standard error of approximately 0.158. Inverting p=0.0654 gives approximately 0.156, a similar value.

For a balanced comparison, Schoenfeld's approximation gives log-HR variance of approximately \(4/D\), where \(D\) is the event count ([3](#ref-3)). This implies approximately 161 events for 240 mg versus chemotherapy. Rounding the interval limits to two decimal places alone permits roughly 154–169 events. The 160 mg comparison gives approximately 158.

At this information size, two-sided significance at alpha 0.05 requires an observed HR below approximately 0.734. The reported 0.75 lies just outside. About 161 events provide 80% power for a true HR around 0.64, or 90% for around 0.60.

These are approximations from public summary statistics. Stratified log-rank and Cox analyses can make the exact event count differ.

## A hypothetical two-arm design

Suppose the same 398 patients had been allocated only to 240 mg and chemotherapy. Holding follow-up and per-patient event probability constant gives 1.5 times as many events in that comparison, approximately 242.

This scenario fixes enrollment. Many phase 3 trials instead specify the necessary event count and continue recruitment or follow-up until it is reached. Under that design, an additional dose arm costs patients and time rather than power at the final information size.

![Approximate power of the high-dose comparison in three-arm and hypothetical two-arm designs](shared/furvent-dose-arm/figures/power.png)

Figure 1. Two-sided Schoenfeld power calculations across assumed true HRs. Solid blue: three arms, approximately 161 events, alpha 0.05. Dashed blue: alpha 0.025 per dose comparison. Orange: hypothetical two-arm design with approximately 242 events and alpha 0.05. The horizontal dotted line marks 80% power. Vertical lines mark observed HRs in FURVENT (solid) and the separate-drug WU-KONG28 trial (dashed). The actual multiplicity procedure is not public.

Table 2. Approximate power at fixed enrollment; actual alpha allocation is unknown.

| True HR | Three arms (alpha 0.05) | Three arms (alpha 0.025) | Hypothetical two arms (alpha 0.05) |
|---|---|---|---|
| 0.75 | 45% | 34% | 61% |
| 0.65 | 78% | 69% | 92% |
| 0.60 | 90% | — | 98% |

Outputs: `results/summary.json` and `results/power_curves.csv`.

For true HRs of 0.65–0.75, the three-arm design costs approximately 14–17 percentage points of power under these assumptions. Thus, the direction of the criticism is reasonable when enrollment is fixed.

The observed HR of 0.75 is not the true HR. Power computed at the observed estimate is largely a mechanical restatement of the p value and does not prove that two arms would have succeeded. Estimates vary around the true effect in a two-arm trial too. The table is a prospective comparison under assumed effects, not a retrospective verdict.

## Other trials in the same population

In May 2026, WU-KONG28 reported a first-line comparison of sunvozertinib with chemotherapy in EGFR exon 20 insertion NSCLC ([4](#ref-4)). It randomized 324 patients 1:1. Median BICR PFS was 10.3 versus 7.5 months, HR 0.65 (95% CI 0.50–0.85). The conference/media p value was 0.0008; the paper reports P<0.001. The primary endpoint was met.

The same inversion implies approximately 218–242 events, depending on whether the CI or p value is used. That resembles the hypothetical two-arm FURVENT comparison's approximately 242 events.

Table 3. First-line median BICR PFS across trials; differences between trials are unadjusted.

| Trial | Active-arm median PFS, BICR | Chemotherapy median PFS, BICR |
|---|---|---|
| PAPILLON, amivantamab plus chemotherapy ([5](#ref-5)) | 11.4 months | 6.7 months |
| WU-KONG28, sunvozertinib ([4](#ref-4)) | 10.3 months | 7.5 months |
| EXCLAIM-2, mobocertinib ([6](#ref-6)) | 9.6 months | 9.6 months |
| FURVENT, firmonertinib 240 mg ([1](#ref-1)) | 11.0 months | 9.5 months (7.1 months by investigators) |

FURVENT's high-dose median resembles those of the two successful trials. Its chemotherapy BICR median is 2–3 months longer than in PAPILLON and WU-KONG28, but similar to EXCLAIM-2's 9.6 months. Chemotherapy medians span 6.7–9.6 months. EXCLAIM-2 stopped after crossing an interim futility boundary; a long control-arm median alone does not determine failure.

Patient populations, chemotherapy regimens, scan schedules and censoring rules can differ, and a median is only one point on a survival curve. The relatively favorable BICR control result nevertheless belongs alongside active-drug efficacy when considering FURVENT's HR. It lies near the upper end of previous trials in this setting. Declaring the effect assumption too optimistic without the original design risks hindsight bias.

## Information gained from the second dose

The FDA's August 2024 final guidance recommends identifying an optimized oncology dose before registration; it is nonbinding guidance ([7](#ref-7)). FURVENT began in June 2023. Public materials do not establish whether FDA requested the 160 mg arm. The information gained can be examined without assigning that motive.

In phase 1b FAVOUR, only 240 mg was evaluated first line, with confirmed response of 78.6% among 28 patients. Previously treated patients received 160 or 240 mg, with response rates of 38.5% and 46.2%, respectively, in 26 patients each ([8](#ref-8)). FURVENT therefore supplied a randomized first-line comparison involving 160 mg.

Because both dose arms share chemotherapy as control, their reported HR ratio approximates 240 versus 160 mg: 0.75/0.91 ≈0.82 by BICR. Assuming equal event allocation gives an approximate 95% CI of 0.60–1.12. The PFS dose difference is inconclusive.

Confirmed BICR response was 60% versus 35%. Assuming approximately 133 patients per arm gives a 25-percentage-point difference, with an approximate 95% CI of 13–37 points. Response favored 240 mg.

Grade ≥3 adverse events of any causality were similar at 52%, 53% and 55%. Treatment-related rates were 26%, 22% and 40%; relatedness judgments may be biased in an open-label trial, and exposure duration may differ ([1](#ref-1)). The topline does not clearly establish a safety difference between doses.

The added arm showed lower response at 160 mg than at 240 mg in first-line treatment, at a cost to information in the primary comparison under fixed enrollment. Whether that exchange was worthwhile depends partly on whether the dose information could have been obtained earlier in a randomized phase 2 comparison. These materials do not settle that question.

## Central versus investigator assessment

For 240 mg, the BICR HR was 0.75 and the investigator HR 0.61: a ratio of approximately 1.23. For 160 mg, the values were 0.91 and 0.86, a ratio of approximately 1.06.

A Roche-supported meta-analysis of 49 trials estimated a pooled ratio of 1.062 (95% CI 1.016–1.110) in open-label trials ([9](#ref-9)). Investigator assessment was modestly more favorable on average. This CI describes precision of the mean, not dispersion among trials. In the same paper, 17 of 55 comparisons exceeded 1.15. A ratio of 1.23 is above average but not rare for an individual comparison.

![Reported HRs and median PFS by central and investigator assessment](shared/furvent-dose-arm/figures/assessment.png)

Figure 2. Company-reported values: (a) PFS HRs and 95% confidence intervals on a logarithmic scale; (b) median PFS by arm.

Only chemotherapy shows a large median difference, 9.5 versus 7.1 months; the dose-arm medians barely change (Figure 2b). That does not locate all disagreement in chemotherapy. The 160 mg comparison shares that control, yet its HR barely changes. HRs depend on the survival experience beyond the median.

One possible mechanism is informative censoring. An investigator progression decision may prompt treatment change and cessation of scans. If BICR does not confirm progression at that time, the BICR analysis may censor the patient, potentially lengthening its median ([9](#ref-9)). Scan timing and open-label assessment bias are other possibilities. Patient-level agreement and censoring reasons are needed to identify the cause. The primary endpoint remains BICR PFS; assessment disagreement does not change that endpoint's result.

## Treatment context

First-line treatment has changed since FURVENT was planned. Following PAPILLON's PFS HR of 0.40, the US approved amivantamab plus chemotherapy first line in March 2024 ([5](#ref-5)). This affects the relevance of chemotherapy-only control trials. Oral sunvozertinib 300 mg beat chemotherapy in WU-KONG28 ([4](#ref-4)), but was not first-line approved at the source-check date. Its US accelerated approval was after chemotherapy, at 200 mg. FURVENT belongs in this evolving treatment context.

## Dose information and the cost in power

The approximately 160-event high-dose comparison had 14–17 percentage points less power than the fixed-enrollment hypothetical two-arm comparison for assumed true HRs of 0.65–0.75. The 160 mg arm supplied dose–response information that concentrating patients in the primary comparison would not provide.

Without the reason for adding 160 mg, assumed effect, alpha allocation or planned event count, the failure cannot be attributed to Project Optimus. Treating the observed HR as truth cannot establish two-arm success. The favorable BICR control result and assessment discrepancy also remain unexplained by topline data.

Adding a dose-optimization arm to phase 3 exchanges dose information for primary-comparison power, or for additional patients and time in an event-driven design. Figure 1 shows how that cost depends on the assumed effect.

## Data and code availability

Extract the [reproduction ZIP](shared/furvent-dose-arm/furvent-dose-arm.zip) and run in its directory. The [calculation script](shared/furvent-dose-arm/furvent_power.py) uses reported summary values to generate `results/summary.json`, `results/power_curves.csv` and Figures 1–2. Tested NumPy, SciPy and Matplotlib versions are pinned in `requirements.txt`.

```sh
python -m pip install -r requirements.txt
python furvent_power.py
```

Inputs are public topline and other summary results; complete reports may revise them. Event inversion assumes proportional hazards and balanced allocation and does not reproduce stratification or interim-analysis adjustment. The hypothetical two-arm scenario assumes equal enrollment and per-patient event probability; an event-driven design changes the cost to patients and time. Dose HR and response-rate comparisons assume equal arm sizes and events. Cross-trial comparisons do not adjust population or assessment differences.

## References

1. <span id="ref-1"></span>ArriVent BioPharma. ArriVent announces program update from the phase 3 FURVENT trial of firmonertinib in first-line EGFR exon 20 insertion mutant NSCLC. 2026 Oct 6. [Company announcement](https://www.biospace.com/press-releases/arrivent-announces-program-update-from-the-phase-3-furvent-trial-of-firmonertinib-in-first-line-egfr-exon-20-insertion-mutant-nsclc).
2. <span id="ref-2"></span>ClinicalTrials.gov. NCT05607550: FURVENT. [Trial registration](https://clinicaltrials.gov/study/NCT05607550). Accessed 2026 Oct 14.
3. <span id="ref-3"></span>Schoenfeld DA. Sample-Size Formula for the Proportional-Hazards Regression Model. Biometrics. 1983;39(2):499–503. [doi:10.2307/2531021](https://doi.org/10.2307/2531021).
4. <span id="ref-4"></span>Zhou C, Greillier L, Liu G, John T, Xing L, Kowalski D, et al. First-Line Sunvozertinib in NSCLC with EGFR Exon 20 Insertion Mutations. New England Journal of Medicine. 2026;395(8):765–775. [doi:10.1056/NEJMoa2604461](https://doi.org/10.1056/NEJMoa2604461).
5. <span id="ref-5"></span>Zhou C, Tang KJ, Cho BC, Liu B, Paz-Ares L, Cheng S, et al. Amivantamab plus Chemotherapy in NSCLC with EGFR Exon 20 Insertions. New England Journal of Medicine. 2023;389(22):2039–2051. [doi:10.1056/NEJMoa2306441](https://doi.org/10.1056/NEJMoa2306441).
6. <span id="ref-6"></span>Jänne PA, Wang BC, Cho BC, Zhao J, Li J, Hochmair M, et al. First-Line Mobocertinib Versus Platinum-Based Chemotherapy in Patients With EGFR Exon 20 Insertion–Positive Metastatic Non–Small Cell Lung Cancer in the Phase III EXCLAIM-2 Trial. Journal of Clinical Oncology. 2025;43(13):1553–1563. [doi:10.1200/JCO-24-01269](https://doi.org/10.1200/JCO-24-01269).
7. <span id="ref-7"></span>US Food and Drug Administration. Optimizing the dosage of human prescription drugs and biological products for the treatment of oncologic diseases. Final guidance. 2024 Aug. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/optimizing-dosage-human-prescription-drugs-and-biological-products-treatment-oncologic-diseases).
8. <span id="ref-8"></span>Allist Pharmaceuticals and ArriVent BioPharma. Interim results from the phase Ib FAVOUR trial presented at the 2023 World Conference on Lung Cancer. 2023 Sep 10. [Sponsor announcement](https://www.allist.com.cn/en/newsd/102/1052.html).
9. <span id="ref-9"></span>Lian Q, Fredrickson J, Boudier K, Rothkegel C, Hilton M, Hillebrecht A, et al. Meta-Analysis of 49 Roche Oncology Trials Comparing Blinded Independent Central Review (BICR) and Local Evaluation to Assess the Value of BICR. The Oncologist. 2024;29(8):e1073–e1081. [doi:10.1093/oncolo/oyad012](https://doi.org/10.1093/oncolo/oyad012).
