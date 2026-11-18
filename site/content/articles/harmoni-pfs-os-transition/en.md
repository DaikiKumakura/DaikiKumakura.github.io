HARMONi compared ivonescimab plus chemotherapy with placebo plus chemotherapy in advanced EGFR-mutant non-squamous non-small-cell lung cancer that progressed after a third-generation EGFR tyrosine kinase inhibitor. Median progression-free survival (PFS) was 6.8 versus 4.4 months, and median overall survival (OS) was 16.8 versus 14.0 months. The primary OS hazard ratio was 0.79 (95% confidence interval 0.62–1.01) ([1](#ref-1)). To see how far a progression delay could carry through to OS, I constructed a model with the same post-progression survival in both groups.

## Holding post-progression survival fixed

Assume every death follows progression. Time to progression and time from progression to death are independent exponentials with rates $a,b$. The OS survival function of their sum is $[b e^{-at}-a e^{-bt}]/(b-a)$. Use the control PFS median of 4.4 months to set $a$ and the control OS median of 14.0 to set $b$. Keep $b$ fixed and match the treatment PFS median of 6.8 months. The calculation conditions on group medians and uses neither patient-level fitting nor statistical testing.

**Table 1.** Medians in months with shared or separate post-progression survival.

| Scenario | Control post-progression | Treatment post-progression | Treatment OS |
| --- | ---: | ---: | ---: |
| Shared rate | 7.32 | 7.32 | 17.10 |
| Separate rates calibrated to the two OS medians | 7.32 | 7.08 | 16.80 |

In Table 1, the shared model gives a treatment OS median of 17.10 months, 0.30 months above the reported 16.8. Under these assumptions a progression delay alone can produce a value close to the trial median. Fitting the two groups separately gives post-progression medians of 7.32 and 7.08 months, which also differ from the result of subtracting the reported medians.

In the trial, deaths without prior progression also count toward PFS. Separating those deaths, subsequent therapy, and departures from exponential survival requires information on event order and times. The model does not estimate a post-progression treatment effect or replace the trial’s statistical analysis. At a June 2026 cutoff in a later post hoc analysis, the OS hazard ratio changed to 0.76 (95% confidence interval 0.61–0.95), while both medians stayed unchanged ([2](#ref-2)). A model calibrated only to those medians gives the same result.

## Data and code availability

The [reproducibility ZIP](shared/harmoni-pfs-os-transition/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Le X, Passaro A, Zhao Y, Huang Y, Laskin J, Rodriguez-Abreu D, et al. Ivonescimab plus chemotherapy versus placebo plus chemotherapy in patients with advanced EGFR-mutated non-small-cell lung cancer after disease progression on EGFR tyrosine kinase inhibitor therapy (HARMONi). Lancet Oncol. 2026;27(9):1094–1109.](https://doi.org/10.1016/S1470-2045(26)00282-2)
2. <a id="ref-2"></a> [Summit Therapeutics Inc. Updated HARMONi data presented at WCLC 2026 [Form 8-K exhibit]. 2026 Sep.](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000081/a2026_prx0915xharmoniltf.htm)
