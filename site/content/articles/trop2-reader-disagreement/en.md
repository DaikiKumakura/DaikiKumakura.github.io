A report says that TROP2 classifications disagreed in 67% of cases. The first question is what was compared. If five pathologists read the same specimen and any dissent makes the case discordant, the result differs from the proportion of reader pairs that disagree. It also does not mean that 67% of patients were misclassified.

The starting point was Raffaele Colombo's post about TROP2 antibody–drug conjugates (ADCs). Colombo argued that target expression should be considered alongside ADC half-life and stability, linking to an editorial by He and Rimm ([1](#ref-1)). I examined half-life measurement definitions in a [separate article](trop2-payload-exposure-en.html). Here I consider the reader disagreement reported in that editorial.

## Scope and sources

On November 1, 2026, I read the post and visible replies, and the editorial's text and Figure 1 caption. Publisher access was intermittent, so I used the portions available through the search index. For the related assay study, I checked the bibliographic record, abstract and indexed methods and results. I did not obtain and recompute the individual reader scores ([2](#ref-2), [3](#ref-3)).

The editorial's [Figure 1](https://doi.org/10.1093/jnci/djag275) describes 72 specimens evaluated by five pathologists, with classifications compared at different H-score cutoffs. The H-score weights percentages of cells at different staining intensities and ranges from 0 to 300. It is not a molecule count. At a cutoff of 220, approximately 67% of specimens had classifications that were not unanimous ([2](#ref-2)).

The arithmetic below is conditional on that approximately 67% input. It does not reconstruct specimen-level scores or treatment outcomes. At cutoff 100, the editorial's text reports 13% while its caption reports 12%. I do not resolve that discrepancy by choosing one as correct, and do not use it in the main calculation.

## Any dissent among five readers versus a disagreeing pair

Suppose five readers make a binary classification for one specimen, and \(k\) call it high. There are

\[
\binom52=10
\]

possible reader pairs. A pair disagrees when one reader calls high and the other low, giving \(k(5-k)\) disagreeing pairs. The pair disagreement fraction \(d(k)\) for that specimen is therefore

\[
d(k)=\frac{k(5-k)}{10}.
\]

Table 1 groups the outcomes by the number of high calls. I verified them by enumerating all 32 possible voting patterns in Python. The enumeration does not assign equal probabilities to these patterns in patients.

**Table 1. Exhaustive five-reader binary decisions grouped by the number of high calls**

| Readers calling high | Number of patterns | Any dissent? | Disagreeing reader pairs | Pair disagreement |
| ---: | ---: | --- | ---: | ---: |
| 0 | 1 | No | 0/10 | 0% |
| 1 | 5 | Yes | 4/10 | 40% |
| 2 | 10 | Yes | 6/10 | 60% |
| 3 | 10 | Yes | 6/10 | 60% |
| 4 | 5 | Yes | 4/10 | 40% |
| 5 | 1 | No | 0/10 | 0% |

A 4-to-1 split and a 3-to-2 split both contribute one discordant specimen to an any-dissent count. Their pair disagreement fractions are nevertheless 40% and 60%. The aggregate any-dissent count does not identify this composition.

## What approximately 67% can bound

Let \(D\) be the fraction of specimens with any dissent. If specimens receive equal weight and two readers are selected uniformly from each specimen's five readers, the overall pair disagreement fraction \(\bar d\) satisfies

\[
0.4D\leq\bar d\leq0.6D.
\]

Unanimous specimens contribute zero; discordant specimens contribute either 40% or 60% pair disagreement.

Substituting the reported rounded value of 67% as a point input gives **26.8–40.2%**. This is neither a confidence interval nor an estimate of the original study's pair disagreement rate. It is the range imposed by the definition and the available aggregate. Rounding of the input and uncertainty arising from specimen selection remain separate issues.

Thus, disagreement in 67% of specimens can coexist with disagreement in roughly three out of ten reader pairs. The choice of denominator changes how the difficulty of transferring a classification between laboratories appears. Disagreement rates cannot be compared without the number of readers and the observational unit.

## A majority vote is not a reference standard

The votes still do not establish which classification is correct. If four readers call high and one calls low, majority voting can select high. The votes alone do not show that this classification better predicts drug benefit.

Conversely, all readers could share a systematic measurement bias. Agreement could then be complete without accurately measuring a reference quantity. Agreement informs reproducibility; it does not encompass accuracy or treatment-selection utility. Nor have I assumed independent reader errors. People evaluating the same staining with shared conventions do not constitute five independent diagnostic tests.

The related quantitative-assay paper itself distinguishes analytical validation from clinical validation ([3](#ref-3)). A high correlation or good repeat-measurement reproducibility does not by itself establish a cutoff for choosing an ADC. Replacing readers with image AI leaves calibration to reference material, transfer across laboratories and validation against outcomes as separate questions.

## Changing the cutoff changes the disagreement

If H-scores cluster around a cutoff, small reading differences can split high and low calls. If scores are far from it, comparable reading differences may leave binary calls unchanged. High disagreement at 220 therefore does not establish the same rate at every cutoff or in another population.

The editorial also questions whether TROP2-high and TROP2-low, defined using different cutoffs across trials, can be treated as common population labels ([2](#ref-2)). The enumeration here does not reanalyse clinical effect modification. It does not address treatment interactions, missing specimens or selection into biomarker testing.

The reported 67% disagreement deserves attention. Its definition is part of the result. Unanimity among five readers, agreement between two readers, agreement with a reference standard and improved treatment selection are different quantities. Combining them into one measure obscures what an improved assay still needs to establish.

## Data and code availability

The [enumeration code](shared/trop2-reader-disagreement/analysis.py), [CSV of 32 patterns](shared/trop2-reader-disagreement/five-reader-patterns.csv), [summary JSON](shared/trop2-reader-disagreement/summary.json) and [reproduction instructions](shared/trop2-reader-disagreement/REPRODUCE.md) are available. The calculation uses only the Python standard library and no random numbers. Original specimen scores and figures are not redistributed.

## References

1. <span id="ref-1"></span>Colombo R [@raffcolo]. Target expression should be considered with ADC half-life and stability [X post; editorial description]. 2026 Oct 31 [cited 2026 Nov 1]. [Original post](https://x.com/raffcolo/status/2116207047066956046).
2. <span id="ref-2"></span>He M, Rimm DL. The right drug, the wrong assay: TROP2-ADC assessment in breast cancer. J Natl Cancer Inst. 2026 Oct 27:djag275. [doi:10.1093/jnci/djag275](https://doi.org/10.1093/jnci/djag275).
3. <span id="ref-3"></span>He M, Chan NNN, Liu M, Robbins CJ, Bates K, Benanto J, et al. Quantitative Assays for TROP2 Measurement in Breast Cancer and Comparison to H-Score. Appl Immunohistochem Mol Morphol. 2026;34(3):143–154. [doi:10.1097/PAI.0000000000001311](https://doi.org/10.1097/PAI.0000000000001311).
