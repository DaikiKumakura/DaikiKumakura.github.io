Literature and public materials checked on 2026-10-14. This is a literature-based essay and contains no new analysis.

Suppose we know the response to knocking down a gene in one cell line. What happens when the same gene is knocked down in another? This cross-context prediction is becoming central to Virtual Cell models that predict cellular interventions. The 2026 Virtual Cell Challenge asks for zero-shot predictions in cell backgrounds without perturbation data [1].

Is cross-context prediction difficult because the models are immature, or because the responses themselves change with context? Before answering, there is a more basic question: **how reproducible is the response when the same experiment is repeated in the same cell line?**

## Raw correlations substantially underestimate reproducibility {#_1}

While preparing this article, I calculated correlations between responses to the same knockdowns in public data from four cell lines. I nearly interpreted their small size as evidence that responses change greatly across backgrounds. A review comment sent me back to the original paper, where I found that this interpretation was wrong.

Nadig and colleagues had already studied the question using essential-gene Perturb-seq in K562, RPE1, HepG2 and Jurkat [2]. First, they compared log-fold-change correlations for the same knockdowns between two independent K562 screens: a genome-wide screen and an essential-gene screen. The median correlation between point estimates was only 0.16. Modeling estimation error with TRADE raised the estimated median correlation between true effects to 0.90.

Thus, even the same knockdown in the same cell line can have a low raw correlation. Read depth per cell is limited, and estimation error obscures changes in many genes. Uncorrelated errors attenuate correlation toward zero. A low raw correlation is not itself evidence of a large biological difference.

## Error correction also raises cross-cell-line correlations {#_2}

The paper also estimates corrected correlations across the four cell lines [2]. Of 2,053 shared essential genes, the comparison uses 1,660 perturbations with detectable effects in all four lines under the permissive criterion Z > 0.5. Median correlations were 0.74 for K562–Jurkat, 0.75 for HepG2–RPE1, 0.64 for K562–HepG2 and 0.69 for Jurkat–HepG2. K562–RPE1 (0.40) and Jurkat–RPE1 (0.56) were lower.

The authors describe K562 and Jurkat as p53-mutant suspension blood-cell lines, and HepG2 and RPE1 as p53-wild-type adherent epithelial lines. Response similarity appears structured by cell-line properties. With only four lines, however, p53 status, lineage, adherence and malignant status overlap, so their causal contributions cannot be separated. Experimental differences, including CRISPRi systems, may contribute too.

The reference is not one, but 0.90 between independent screens in the same cell line. Cross-line values of 0.40–0.75 are lower and are consistent with context-dependent responses. Yet the correlations may include responses shared by many perturbations; they do not reveal how similar the perturbation-specific component is.

The conclusion is neither that context changes responses enormously nor that it hardly changes them. **The size of the difference can be measured only after accounting for estimation error.**

## Reproducibility bounds and simple comparators {#_3}

This directly affects evaluation of cross-context prediction.

**Within-context reproducibility provides a correlation bound.** A prediction–observation correlation of 0.2 cannot be judged without knowing the noise in the observations. The relevant bound depends on what is compared. For two measurements, such as copying an observed response from another cell line, the raw correlation r between within-context replicates is a reference. For a noise-free prediction against a noisy observation, the bound is approximately \(\sqrt{r}\) when the two measurements have comparable noise; \(r=0.16\) gives about 0.40. The value 0.16 belongs to this dataset and processing procedure, not to Perturb-seq generally. A bound has to be estimated for each dataset, for example through split-half replicates.

**A simple comparator depends on the available information.** Copying a response measured in another line is a minimal cross-context baseline. If other perturbations have been observed in the target background, its common response can also serve as a baseline. That second comparator is unavailable in settings such as the 2026 Virtual Cell Challenge, which excludes target-background perturbation data [1].

**Shared responses differ from perturbation-specific responses.** Essential-gene knockdowns can produce common changes such as reduced proliferation and stress. Systema shows how predicting systematic variation can inflate evaluation scores [3]. Miller and colleagues show that some metrics, conversely, have low sensitivity to predictions that contain real information [4]. The distinction becomes especially relevant across backgrounds because the common response can itself differ between cell lines.

**Response strength affects interpretation.** For weak perturbations, much of the observed change is estimation error. Pooling weak and strong responses obscures both model performance and biological context differences.

In the [article on PIE's public evaluation tables](pie-deg-prioritization.html), performance declined when the background was held out. That decline may reflect model limitations, genuine response differences or measurement noise. Calling cross-context prediction difficult without distinguishing these three leaves the source of the difficulty unresolved.

## References {#_5}

1. Arc Institute. [The 2026 Virtual Cell Challenge](https://arcinstitute.org/news/virtual-cell-challenge-2026) (2026-08-20).
2. Nadig A, Replogle JM, et al. Transcriptome-wide analysis of differential expression in perturbation atlases. *Nature Genetics*. 2025;57:1228–1237. [10.1038/s41588-025-02169-3](https://doi.org/10.1038/s41588-025-02169-3). Numerical results checked in [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13063516/).
3. Viñas Torné R, et al. Systema: a framework for evaluating genetic perturbation response prediction beyond systematic variation. *Nature Biotechnology*. 2026;44(6):1050–1059. [10.1038/s41587-025-02777-8](https://doi.org/10.1038/s41587-025-02777-8).
4. Miller HE, et al. Deep learning perturbation models can outperform baselines on calibrated metrics. *Nature Biotechnology*. Published online 2026-10-01. [10.1038/s41587-026-03307-w](https://doi.org/10.1038/s41587-026-03307-w).

<span id="_4"></span>
