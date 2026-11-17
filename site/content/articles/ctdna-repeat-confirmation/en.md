When circulating tumor DNA (ctDNA) is measured after surgery, calling a patient positive after one result and waiting for two consecutive positives can yield different groups of trial candidates. In IMvigor011, patients with muscle-invasive bladder cancer underwent serial ctDNA testing after cystectomy. Those who became ctDNA-positive and met the eligibility criteria were randomized to atezolizumab or placebo ([1](#ref-1)). The calculation below compares two hypothetical rules independently of that trial.

## Holding single-draw specificity fixed

I kept molecular residual disease (MRD) status fixed from the first draw to the last. In patients with MRD, the per-draw probability of a positive result was 70%, with independent results across draws. Among patients without MRD, a fraction `f` always tested positive. I compared 0%, 0.5%, and 1%. For the remaining patients, tests were independent across draws with positive probability `q = (0.01 − f) / (1 − f)`. This kept the false-positive probability at 1% at every draw across all patients without MRD.

FDA guidance lists assay performance and sampling timing among the considerations for ctDNA-based selection in early-stage solid tumors ([2](#ref-2)). A study of patients with metastatic cancer and controls sequenced plasma and matched white blood cells and traced some variants detected in plasma to clonal hematopoiesis ([3](#ref-3)). The 0.5% and 1% values here are assumptions for examining how persistent false positives affect classification. Neither estimates the false-positive rate of a postoperative assay.

The rule across draws is distinct from the threshold within one sample. The FDA review describes Signatera CDx as calling a sample positive when at least two of 16 targeted variants are detected. It also uses whole-blood sequencing to filter candidate variants that may arise from clonal hematopoiesis or other non-tumor sources ([4](#ref-4)). In the calculation below, two consecutive positives means that two separately collected samples in a row have each tested positive.

## Classification after eight draws

I tracked the current run of positives and classified a patient as positive once that run reached the required length. Before classification, a negative draw resets the run to zero. Summing the probabilities of first meeting the rule at each draw gives the probability of classification by the final draw. In patients without MRD, that probability is the always-positive fraction `f` plus the remaining fraction `1 − f` times the probability of meeting the rule in that group. Table 1 assumes that 5% of patients have MRD.

**Table 1. False-positive patients and positive predictive value after eight draws**

| Always positive among patients without MRD | False-positive patients per 1,000 (one positive) | False-positive patients per 1,000 (two consecutive positives) | Positive predictive value (one positive) | Positive predictive value (two consecutive positives) |
| --- | ---: | ---: | ---: | ---: |
| 0% | 73.4 | 0.7 | 40.5% | 98.7% |
| 0.5% | 42.1 | 4.9 | 54.3% | 90.8% |
| 1% | 9.5 | 9.5 | 84.0% | 83.5% |

False-positive patient counts are expected values per 1,000 patients tested. Positive predictive value is the proportion with MRD among those classified positive.

The rules classified 99.99% and 96.48% of patients with MRD as positive, respectively. Among those classified by draw eight under each respective rule, classification took an average of 1.43 and 3.20 draws. With only two scheduled draws, 49% of patients with MRD met the rule requiring consecutive positives. Each mean uses a different group of patients, so their difference cannot be interpreted as a delay within the same patient or as time to treatment.

With independent false positives, each extra draw increases the chance that a patient without MRD tests positive at least once. In the 1% scenario, where false positives are confined to the same patients, requiring a second positive still leaves 9.5 false-positive patients per 1,000 tested. Meanwhile, the number of patients with MRD who are classified positive falls from 50.0 to 48.2 per 1,000. Even at the same single-draw specificity, the value of another draw for confirmation depends on whether false positives persist in the same patients.

The model omits the onset of MRD during surveillance, treatment between draws, and cessation of sampling after clinical recurrence. It also assumes independent measurements in patients with MRD. The calculation cannot estimate how many people would qualify for treatment in a particular trial or how waiting for confirmation would affect treatment benefit.

## Data and code availability

No patient data were used. The [companion ZIP](shared/ctdna-repeat-confirmation/ctdna-repeat-confirmation-companion.zip) contains the code and results for all 36 scenarios. Run `python analysis.py > results.csv` with the Python 3.12.4 standard library to regenerate the table. The calculation uses no random numbers.

## References

1. <a id="ref-1"></a> Powles T, Kann AG, Castellano D, Gross-Goupil M, Nishiyama H, Bracarda S, et al. ctDNA-guided adjuvant atezolizumab in muscle-invasive bladder cancer. N Engl J Med. 2025;393(24):2395–2408. [doi:10.1056/NEJMoa2511885](https://doi.org/10.1056/NEJMoa2511885).
2. <a id="ref-2"></a> US Food and Drug Administration. Use of circulating tumor DNA for curative-intent solid tumor drug development: guidance for industry. 2024. [FDA guidance](https://www.fda.gov/media/183874/download).
3. <a id="ref-3"></a> Razavi P, Li BT, Brown DN, Jung B, Hubbell E, Shen R, et al. High-intensity sequencing reveals the sources of plasma circulating cell-free DNA variants. Nat Med. 2019;25(12):1928–1937. [doi:10.1038/s41591-019-0652-7](https://doi.org/10.1038/s41591-019-0652-7).
4. <a id="ref-4"></a> US Food and Drug Administration. Signatera CDx: Summary of Safety and Effectiveness Data. P260004. 2026. [FDA review, Section V](https://www.accessdata.fda.gov/cdrh_docs/pdf26/P260004B.pdf#page=3).
