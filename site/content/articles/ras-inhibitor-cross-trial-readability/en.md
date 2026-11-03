Reference date: the facts in this article are as of 3 November 2026.

On 2 November 2026, a figure titled "KRASzy Progress" (by Chris De Savi) that lines up the clinical results of eight RAS inhibitors was re-posted on X ([1](#ref-1)). For each drug it lists the objective response rate (ORR), progression-free survival and overall survival, and the numbers side by side look like a ranking of the drugs. For the numbers printed in the figure that could be checked against public sources, this note recalculates which comparisons can be read with intervals and which cannot.

## Scope and sources

The figure's image is not reproduced; the printed numbers were checked against public sources. Of the eight drugs, the results of five were checked (NSCLC is non-small cell lung cancer, PDAC is pancreatic ductal adenocarcinoma, and the FDA is the U.S. Food and Drug Administration).

- Sotorasib in CodeBreaK 200 (phase 3 against docetaxel, KRAS G12C-mutant NSCLC). I read the abstract of the paper ([2](#ref-2)) and an article reporting the paper ([3](#ref-3)); the response rate and overall survival come from the latter.
- Divarasib in Krascendo 1 (phase 3 against sotorasib or adagrasib, KRAS G12C-mutant NSCLC). I read the company's announcement ([4](#ref-4)); the peer-reviewed paper was not read.
- Daraxonrasib in RASolute 302 (phase 3 against chemotherapy, metastatic PDAC). I read the FDA approval information ([5](#ref-5)) and the abstract of the paper ([6](#ref-6)).
- Elironrasib in a phase 1 study (NSCLC after a KRAS G12C inhibitor). I read an article reporting the conference presentation ([7](#ref-7)) and a news item ([8](#ref-8)).
- Zoldonrasib in a phase 1 study (KRAS G12D NSCLC). I read an article reporting abstract CT021 of the 2026 meeting of the American Association for Cancer Research (AACR) ([9](#ref-9)); the abstract itself was not read.

The other three drugs (olomorasib, HRS-4642, setidegrasib) are left out of the tables because public sources could not be checked. For the same reason, the first-line combination of zoldonrasib and the combination data for elironrasib are not used.

For the calculations, I reconstructed responder counts from the reported response rate and patient number (rounded) and computed exact Clopper–Pearson 95% confidence intervals (CI) ([10](#ref-10)), which I compared with the reported intervals. Newcombe intervals ([11](#ref-11)) were used for differences between two randomized arms. The intervals are descriptive, with no adjustment for multiplicity.

## Discussion by issue

### Trials differ in population and design

The numbers lined up differ in tumor, line of therapy, comparator and analysis set (Table 1).

Table 1. Design of the trials checked (ORR: objective response rate; NSCLC: non-small cell lung cancer). Patient numbers are those randomized (experimental / control).

| Trial | Tumor | Comparator | Randomized n | ORR denominator |
| --- | --- | --- | ---: | --- |
| CodeBreaK 200 | KRAS G12C NSCLC, after prior therapy | Docetaxel | 171 / 174 | Randomized |
| Krascendo 1 | KRAS G12C NSCLC, after prior therapy | Sotorasib or adagrasib | 167 / 171 | Response-evaluable (161 / 167) |
| RASolute 302 | Pancreatic adenocarcinoma, after one line | Chemotherapy | 248 / 252 | Overall population |
| Elironrasib phase 1 | KRAS G12C NSCLC, after a G12C inhibitor | None | 24 | Treated |
| Zoldonrasib phase 1 | KRAS G12D NSCLC, after immunotherapy and platinum | None | 27 | Efficacy-evaluable |

The response rate in Krascendo 1 is for an evaluable set that excludes 10 patients without measurable disease (6 in the divarasib arm and 4 in the control arm), leaving 161 and 167 ([4](#ref-4)). The numbers for RASolute 302 are from the abstract of the paper ([6](#ref-6)).

### Comparisons within one trial can be read with intervals

Within a randomized trial, the difference between the two arms can be read with an interval (Table 2). In CodeBreaK 200, the response rate was 28.1% (95% CI 21.5–35.4) for sotorasib and 13.2% (8.6–19.2) for docetaxel, a difference of 14.9 percentage points (6.3–23.2) ([3](#ref-3)). In the overall population of RASolute 302, it was 30% (25–36) for daraxonrasib and 11% (7–15) for chemotherapy ([5](#ref-5)). The difference computed from reconstructed counts is 18.7 percentage points (11.7–25.6), but because the reported percentages are integers, it is not precise to the decimal (30 minus 11 is 19). Exact intervals from my reconstructed counts matched the reported ones exactly in CodeBreaK 200 and to within 0.8 points in RASolute 302 (how the FDA interval was computed is not stated in the text I read).

Table 2. Difference in response rate in the two randomized trials (reconstructed counts, Newcombe 95% interval).

| Trial | Experimental ORR | Control ORR | Difference (percentage points) | 95% interval |
| --- | ---: | ---: | ---: | --- |
| CodeBreaK 200 | 28.1% | 13.2% | 14.9 | 6.3 to 23.2 |
| RASolute 302 (overall) | 30% | 11% | 18.7 | 11.7 to 25.6 |

Hazard ratios with intervals are reported for progression-free and overall survival in each trial. CodeBreaK 200 had 0.66 (0.51–0.86) for progression-free survival and 1.01 (0.77–1.33) for overall survival ([2](#ref-2), [3](#ref-3)); Krascendo 1 had 0.58 (0.44–0.76) and 0.56 (0.41–0.78) ([4](#ref-4)); the overall population of RASolute 302 had 0.49 (0.38–0.64) and 0.40 (0.30–0.53) ([5](#ref-5)). A hazard ratio is a summary that assumes proportional hazards, and its meaning changes with the comparator and with subsequent therapy (whether patients in the control arm crossed over to the experimental drug was not stated in the text I read).

### Why comparisons across trials cannot be read

The control-arm response rates of the three trials differ widely: 13.2% (docetaxel), 32% (sotorasib or adagrasib) and 11% (chemotherapy) (Figure 1) ([3](#ref-3), [4](#ref-4), [5](#ref-5)). The differences combine the effect of the control treatment with differences in tumor and line of therapy, and the two cannot be separated. In either case, placing experimental-arm response rates or hazard ratios from different trials side by side does not show which drug is better. For example, the overall-survival hazard ratio of 0.40 for daraxonrasib and 1.01 for sotorasib come from different tumors and different comparators.

![Figure 1. Response rates (ORR) of the arms printed in the figure, with exact 95% intervals from reconstructed counts (blue: experimental, grey: control, orange: single arm). The Krascendo 1 values are proportions in the evaluable set (open circles). The plot is the author's own; the original figure's image is not reproduced.](shared/ras-inhibitor-cross-trial-readability/figures/01-orr-intervals.png)

Through a shared drug, whether trials can be compared can be checked to some extent. Sotorasib is in the experimental arm of CodeBreaK 200 and in the control arm of Krascendo 1 (sotorasib or adagrasib, split not given in the text I read). The response rate was 28.1% (21.5–35.4) and 32% (24.8–39.4), a difference of 3.7 percentage points (−6.1 to 13.3), and the median progression-free survival was 5.6 months (4.3–7.8) and 5.7 months ([2](#ref-2), [4](#ref-4)). No difference between the two trials is visible. However, the intervals are wide, so this is not evidence of no difference. The control arm includes adagrasib, and the trials differ in period and in assessment method (whether independent or investigator assessment was used was not stated in the text I read). All this comparison supports is that sotorasib's results did not differ greatly between the two trials.

### Single-arm phase 1 response rates have wide intervals and cannot be ranked

The response rate was 42% (22–63) for elironrasib (n = 24) and 52% (recomputed interval 32–71) for zoldonrasib (n = 27), with interval widths of about 40 percentage points (Figure 1) ([7](#ref-7), [9](#ref-9)). The two intervals overlap widely, and they partly overlap the interval for divarasib's 58% in Krascendo 1 (49.7–65.5). Overlap does not mean the response rates are equal. With these sample sizes, however, neither a difference nor a ranking can be claimed. In addition, the elironrasib population had all received a KRAS G12C inhibitor, and 92% had progressed on it ([8](#ref-8)); zoldonrasib targets a different mutation (KRAS G12D) in patients after immunotherapy and platinum ([9](#ref-9)). The progression-free survival values in the figure (6.2 months for elironrasib and 11.1 months for zoldonrasib) are not compared in the same way, because follow-up periods differ and intervals for the medians are not shown.

### Checking the figure's numbers

The checkable numbers agreed between the figure and the public sources. The response rate of 30% for the overall population of RASolute 302 matches the FDA value (25–36) ([5](#ref-5)). The full text of the NEJM paper and the Krascendo 1 paper were not read, so their values were not checked.

## Overall assessment

Of the figure's numbers, within-trial differences and comparisons against a randomized control can be read with intervals. Which drug is better across trials cannot be read, because, among other things, control-arm response rates differ widely (11–32%). The only case where a shared drug (sotorasib) allowed the closeness of results to be checked is one pair with the divarasib trial, and that closeness is weak because the intervals are wide. Single-arm phase 1 response rates, with intervals about 40 percentage points wide, cannot be ranked against each other or against the experimental arms of randomized trials.

## Limitations

Five of the eight drugs were checked, and the sources checked include news reports and company announcements; the full text of no paper was read. Responder counts were reconstructed from rounded values, and the intervals are descriptive. This note does not judge the relative efficacy of the drugs.

## Conclusion

For the five drugs checked, a figure that lines up RAS inhibitor results can be read as within-trial comparisons but not as comparisons of which drug is better across trials. Differences in response rate could be confirmed with intervals within one trial (14.9 percentage points in CodeBreaK 200 and about 19 percentage points in RASolute 302). Cross-trial comparison does not hold because of differences in control and population, and single-arm phase 1 response rates have intervals about 40 percentage points wide and cannot be ranked.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`), the input table (`inputs/arms.csv`, with source levels) and result tables are in the companion archive. Run with Python 3 (numpy, scipy, pandas, matplotlib): `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The inputs are values from published reports; no patient data were used. The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

The full re-run materials are in the [companion archive](shared/ras-inhibitor-cross-trial-readability/ras-inhibitor-cross-trial-readability-companion.zip).


## References

<span id="ref-1"></span>1. Scott KA [@Sculpturatus]. credit to chris de savi [X post]. X. 2026 Nov 2 [cited 2026 Nov 3]. The post shows the image "KRASzy Progress" © Chris De Savi. Available from: https://x.com/Sculpturatus/status/2117250509644198100

<span id="ref-2"></span>2. de Langen AJ, Johnson ML, Mazieres J, Dingemans AC, Mountzios G, Pless M, et al. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRAS G12C mutation: a randomised, open-label, phase 3 trial. Lancet. 2023;401(10378):733–746. [doi:10.1016/S0140-6736(23)00221-0](https://doi.org/10.1016/S0140-6736(23)00221-0)

<span id="ref-3"></span>3. The ASCO Post. Sotorasib improves progression-free survival vs docetaxel in previously treated advanced NSCLC with KRAS G12C mutation [Internet]. 2023 Mar 25 [cited 2026 Nov 3]. Available from: https://ascopost.com/issues/march-25-2023/sotorasib-improves-progression-free-survival-vs-docetaxel-in-previously-treated-advanced-nsclc-with-kras-g12c-mutation

<span id="ref-4"></span>4. Roche. Roche's divarasib demonstrated best-in-class efficacy, advancing the standard of care in previously treated KRAS G12C-mutated lung cancer [Press release]. Basel; 2026 Oct 25 [cited 2026 Nov 3]. Available from: https://www.roche.com/media/releases/med-cor-2026-10-25

<span id="ref-5"></span>5. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. FDA; 2026 [cited 2026 Nov 3]. Available from: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma

<span id="ref-6"></span>6. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555)

<span id="ref-7"></span>7. The ASCO Post. Elironrasib active in KRAS G12C–resistant NSCLC [Internet]. 2025 Oct 29 [cited 2026 Nov 3]. Reports the AACR-NCI-EORTC abstract LB-B024. Available from: https://ascopost.com/news/october-2025/elironrasib-active-in-kras-g12c-resistant-nsclc/

<span id="ref-8"></span>8. TheFly. Revolution Medicines: Elironrasib shows "compelling" antitumor activity in trial [Internet]. TipRanks; 2025 Oct 22 [cited 2026 Nov 3]. Available from: https://www.tipranks.com/news/the-fly/revolution-medicines-elironrasib-shows-compelling-antitumor-activity-in-trial-thefly

<span id="ref-9"></span>9. CancerNetwork. Zoldonrasib shows promising activity in KRAS G12D NSCLC [Internet]. 2026 May 12 [cited 2026 Nov 3]. Reports the AACR 2026 abstract CT021. Available from: https://www.cancernetwork.com/view/zoldonrasib-shows-promising-activity-in-kras-g12d-nsclc

<span id="ref-10"></span>10. Clopper CJ, Pearson ES. The use of confidence or fiducial limits illustrated in the case of the binomial. Biometrika. 1934;26(4):404–413. [doi:10.1093/biomet/26.4.404](https://doi.org/10.1093/biomet/26.4.404)

<span id="ref-11"></span>11. Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17(8):873–890. [doi:10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I](https://doi.org/10.1002/%28SICI%291097-0258%2819980430%2917%3A8%3C873%3A%3AAID-SIM779%3E3.0.CO%3B2-I)
