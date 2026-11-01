A value called cell potency has been estimated from RNA-seq. Does it count the fates a cell can eventually adopt, or describe how many different genes were visible at the time of measurement? Those questions sound related, but they are not identical.

A review by Wang et al., published on October 29, 2026, organizes 16 computational methods for estimating potency from single-cell RNA sequencing (scRNA-seq). Its abstract emphasizes their differing, sometimes contrasting assumptions, and the importance of single-cell-resolution benchmarks and sensitivity analyses ([1](#ref-1)).

The question here is not which method ranks first. It is what must be established before a difference in expression diversity can be called a difference in differentiation potential. I start by calculating what happens when the same RNA composition is measured at different depths.

## Scope and sources

I verified the latest article's bibliographic information and abstract, but could not obtain the publisher's full text or the author-hosted PDF. This is therefore not a review of the implementations or comparative results of all 16 methods. The publicly available 2024 version covers 14 methods; it is a separate version and is not cited as the full text of the latest article ([2](#ref-2)).

The calculation below is limited to detected gene counts and a simple Shannon entropy. It does not reimplement or benchmark CytoTRACE or any other particular method. It also does not assert that normalization, neighborhood smoothing and gene-network approaches all have the same dependence on sequencing depth.

## The same cell can yield more detected genes

Let \(p_g\) be gene \(g\)'s fraction of the RNA pool being measured. In an idealized observation, \(n\) molecules are independently sampled from the same composition and counted after deduplication using unique molecular identifiers (UMIs). Capture and sequence-dependent biases are excluded.

The probability of missing the gene is \((1-p_g)^n\), so the expected detected gene count \(G\) is

\[
E[G\mid n,\boldsymbol p]=\sum_g\{1-(1-p_g)^n\}.
\]

This is an occupancy calculation, not a biological differentiation model.

Consider a hypothetical composition containing 100 genes, each with \(p_g=0.01\). Sampling 50, 100 and 500 UMIs gives expected detected gene counts of 39.5, 63.4 and 99.3. The composition never changes, yet the number of visible genes more than doubles.

This does not establish that methods using detected gene counts are unusable. It asks when their handling of measurement depth successfully separates it from biological state. A higher value in a more deeply measured group does not, by itself, establish higher potency.

## Entropy is not independent of sampling depth

Here Shannon entropy is defined for the relative gene proportions \(p_g\) as

\[
H(\boldsymbol p)=-\sum_g p_g\log p_g.
\]

Natural logarithms give units of nats. Equal proportions across 100 genes give a population entropy of \(\log100=4.605\).

An observation, however, substitutes \(\hat p_g=X_g/n\) for the true proportion. Undetected genes contribute zero. I used the marginal distribution \(X_g\sim\mathrm{Binomial}(n,p_g)\) of each gene under multinomial sampling and directly summed the expected entropy computed from observed proportions. No random simulation or fit to measured cells was performed.

Table 1. Expected observations of the same hypothetical composition at different UMI counts.

| UMI count | Detected genes | Observed entropy (nats) |
| ---: | ---: | ---: |
| 50 | 39.5 | 3.603 |
| 100 | 63.4 | 4.036 |
| 200 | 86.6 | 4.323 |
| 500 | 99.3 | 4.502 |
| 1000 | 100.0 | 4.555 |

These are expectations under multinomial sampling of 100 equally abundant genes. The final detected count of 100.0 is rounded from 99.9957. These are not interval estimates.

Entropy rises as more molecules are measured. Even with constant population entropy, the directly calculated finite-count value differs. Converting library counts into proportions does not eliminate sampling effects.

![UMI depth versus detected genes and entropy for two hypothetical expression compositions](shared/cell-potency-assumptions/depth-entropy.svg)

Figure 1. Exact sampling expectations for hypothetical compositions. In uniform, each of 100 genes has a proportion of 1%. In dominant, one gene has 80% and the remaining 20% is divided equally among 99 genes. The horizontal axis is logarithmic. No band is shown because expectations are directly calculated, rather than estimated with uncertainty intervals.

## Evenly distributed expression does not necessarily mean broader fate potential

In the dominant condition in Figure 1, one gene accounts for 80%. Its population entropy is 1.419 nats, below the uniform composition's 4.605 nats. Exponentiating gives effective gene counts of approximately 4.1 and 100. Both compositions nevertheless contain 100 genes with nonzero proportions.

This difference correctly represents unevenness in expression proportions. But the calculation contains no information about how many descendant cell types either cell can generate. With the same input composition, these two quantities return the same values regardless of the cell's history or culture conditions.

Moving from entropy to potency therefore requires an additional assumption or validation linking expression diversity to future fate. The name entropy does not itself establish biological possibility. Entropy on an expression network is also different from the entropy of gene proportions calculated here; the network definition and its assumptions require separate examination.

## Reading cancer stemness scores

When comparing cancer cell states, it is tempting to call a high-scoring group undifferentiated and a low-scoring group differentiated. The interpretation changes depending on whether the score captures RNA abundance, detection efficiency, a few dominant genes or differences between cell types.

For example, if both detected RNA counts and the score decline after a drug treatment, differentiation induction and changes in cell size or RNA recovery are different explanations. The hypothetical calculation cannot diagnose either, but shows why the declining score alone cannot select one of them.

Matching depth is not sufficient either. Downsampling can match observed molecule counts without restoring gene-specific capture biases or biological RNA abundance. An association with cell state does not validate the future fate of an individual cell.

Agreement with known cell-type orders or markers is informative. However, a score constructed from that information is not independently validated by agreeing with the same information. A claim about functional potency turns on its relationship to fate information obtained separately from the input expression measurements.

## Defining narrowly what the number means

The 100 genes and UMI depths here are hypothetical settings chosen to make the effect visible. Biases in actual scRNA-seq need not have the same magnitude. The results cannot be generalized to a benchmark of all 16 methods, including gene selection, smoothing and network approaches.

The calculation establishes two narrower points: observed gene counts and simple entropy change with depth despite identical expression composition, and the expression-diversity equations contain no future-fate information.

A potency score can be a useful summary for comparing cell states. The step from that summary to functional differentiation potential still needs validation. A precise-looking number does not mean equally precise knowledge of a cell's future.

## Data and code availability

The independent calculation uses hypothetical compositions throughout. The [analysis script](shared/cell-potency-assumptions/analysis.py), [output CSV](shared/cell-potency-assumptions/depth_entropy.csv) and [reproduction instructions](shared/cell-potency-assumptions/REPRODUCE.md) are provided. They contain no measured patient or cell data and no performance ranking of the 16 methods.

## References

1. <span id="ref-1"></span>Wang Q, Zhai Z, Lian Q, Song D, Li JJ. Categorization and analysis of 16 computational methods for estimating cell potency from single-cell RNA-seq data. Cell Systems. 2026:101762. Published online October 29. Abstract and bibliographic information consulted. [https://doi.org/10.1016/j.cels.2026.101762](https://doi.org/10.1016/j.cels.2026.101762).
2. <span id="ref-2"></span>Wang Q, Zhai Z, Lian Q, Song D, Li JJ. Categorization and analysis of 14 computational methods for estimating cell potency from single-cell RNA-seq data [Preprint]. arXiv; 2024. Version 2, August 31. Version identity and abstract consulted. [https://arxiv.org/abs/2309.13518v2](https://arxiv.org/abs/2309.13518v2).
