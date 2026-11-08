A million cells sounds impressive. For genotype–expression associations, however, the information depends on how many donors produced those cells. Sampling more cells from the same person does not add another person with a new genotype.

Published on November 6, 2026, the SAIGE-QTL paper directly models single-cell expression counts while accounting for repeated cells within donors and relationships between donors [(1)](#ref-1). Its significance is the ability to retain repeated observations in the model, not to turn them into independent samples.

## Scope and sources

This article examines the original methods and results and official documentation. An expression quantitative trait locus, or eQTL, is a genetic locus associated with expression. SAIGE-QTL was not rerun on empirical data. The calculation uses a linear random-intercept model to distinguish donor count from cell count; it does not reproduce the original Poisson model's performance.

## What cells share

For illustration, model a continuous expression measure from cell \(j\) of donor \(i\) as

\[
y_{ij}=\alpha+\beta g_i+b_i+\varepsilon_{ij}.
\]

Here \(\alpha\) is the baseline intercept, \(g_i\) centered genotype, \(\beta\) its effect, \(b_i\) a donor-specific deviation with variance \(\tau^2\), and \(\varepsilon_{ij}\) independent cell-specific error with variance \(\sigma^2\). Deviations and errors have mean zero. Donor deviations are independent across donors and independent of all cell-specific errors. Genotype is independent of deviations and errors. Expression uses arbitrary units; genotype is dimensionless.

Averaging \(m\) cells per donor reduces cell-specific error:

\[
\operatorname{Var}(\bar y_i\mid g_i)=\tau^2+\frac{\sigma^2}{m}.
\]

More cells reduce the second term, while the donor-specific first term remains. Additional cells cannot average away a shared donor deviation.

## Five times the cells or twice the donors

Set \(\tau^2=1\) and \(\sigma^2=4\). Assign half the donors \(g_i=-1\) and half \(g_i=+1\). This balanced two-genotype design is artificial and does not reproduce population genotype frequencies. Treat variance components as known.

Then \(\sum_i g_i^2=n\), and regression on donor means gives

\[
\mathrm{SE}(\hat\beta)=\sqrt{\frac{\tau^2+\sigma^2/m}{n}},
\]

where \(n\) is the number of donors. Table 1 shows the executed calculation.

Table 1. Standard error of the genotype effect in an artificial random-intercept model.

| Donors | Cells per donor | Total cells | SE of genotype effect |
| ---: | ---: | ---: | ---: |
| 50 | 20 | 1,000 | 0.155 |
| 50 | 100 | 5,000 | 0.144 |
| 100 | 20 | 2,000 | 0.110 |

SE: standard error. Expression is in arbitrary units and genotype is dimensionless; the effect and its standard error are therefore expressed in the arbitrary units of the expression measure.

With 50 donors, increasing cell count fivefold reduces the standard error from 0.155 to 0.144. Doubling donors instead gives 0.110 with only 2,000 total cells. Under these assumptions, more total cells do not guarantee a smaller standard error.

This does not imply that additional cells are worthless. When cells per donor are initially scarce, \(\sigma^2/m\) can dominate. More cells can also be needed to sample a rare cell type. The calculation shows why total count alone cannot compare these investments.

## Pseudobulk is not automatically a crude method

Pseudobulk analysis aggregates cells within a donor and cell type to obtain donor-level expression summaries.

The example has equal cell counts and cell-specific variances. Regression on donor means follows naturally. Rewriting it at cell level does not create additional genotype information.

Real single-cell data have unequal cell counts, sequencing depths, states and count distributions. SAIGE-QTL uses a Poisson mixed model for the repeated structure [(1)](#ref-1). Its documentation also emphasizes accounting for read depth through normalization or offsets [(2)](#ref-2).

The relevant comparison is therefore not simply raw cells versus discarded information. It is what a summary retains and which distributional assumptions it makes. An appropriately weighted donor-level analysis and an aggregation ignoring imbalance do not become equivalent comparisons merely because both are called pseudobulk.

Conditional Poisson equality of mean and variance must also be distinguished from the marginal distribution after integrating random effects. Observed marginal overdispersion alone does not invalidate a mixed model, and including random effects does not prove that all residual overdispersion has disappeared.

## Conclusion

Additional cells can improve measurement within donors. That improvement is different from information separating a genotype effect from between-donor variation. Direct cell-level modeling does not remove the distinction.

This calculation does not optimize budget allocation or power. Neither can an optimal cell count be inferred without allele frequency, effect size, cell-type frequency and empirical variance components. Putting donors and shared variation ahead of the headline cell count keeps methodological efficiency separate from study-design efficiency.

## Data and code availability

Table 1 corresponds to `donor_design` in the [script](shared/single-cell-eqtl-design/reproduce.py) and [recorded output](shared/single-cell-eqtl-design/illustration.json). These are analytical variance calculations without random sampling. Empirical cohort access and full-scale SAIGE-QTL execution were not validated.

[Download code and results](shared/single-cell-eqtl-design/single-cell-eqtl-design.zip).

## References

1. <a id="ref-1"></a> Zhou W, Cuomo ASE, Hu L, Xue A, Kanai M, Liu YC, et al. Efficient and accurate mixed model association tool for single-cell eQTL analysis. Nature Genetics. 2026 Nov 6. [https://doi.org/10.1038/s41588-026-02798-2](https://doi.org/10.1038/s41588-026-02798-2).

2. <a id="ref-2"></a> SAIGE-QTL developers. SAIGE-QTL documentation [Internet]. Version 0.3.6.0 release notes dated 2026 Apr 15 [cited 2026 Nov 8]. [Official documentation](https://weizhou0.github.io/SAIGE-QTL-doc/).
