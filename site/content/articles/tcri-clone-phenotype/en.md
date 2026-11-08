What is diverse when we describe T cells as diverse: their receptors, their transcriptional states, or the states occupied by cells with the same receptor? Without this distinction, apparently opposing response associations can be forced into one diversity narrative.

Published on November 5, 2026, TCRi uses a hierarchical Bayesian model for the joint distribution of T cell receptor, or TCR, clonotype and phenotype inferred from ribonucleic acid (RNA) expression. The authors report an association between lower pretreatment normalized mutual information and response to immune checkpoint blockade [(1)](#ref-1). Rephrasing this as “more diversity means better response” would merge the quantities the method separates.

## Scope and sources

This article uses the original methods, results and public materials together with software documentation. TCRi was not reapplied to patient data. The table below is an artificial example demonstrating that identical marginal diversities can coexist with different clone–state relationships.

## Two populations with identical diversity

Let clonotype be \(C\in\{A,B\}\) and transcriptional state be \(S\in\{0,1\}\). Table 1 specifies two populations of 100 cells. States zero and one are explanatory labels with no assigned biological value such as activation or exhaustion.

Table 1. Artificial populations with identical marginal distributions.

| Population | Clonotype | State 0 cells | State 1 cells |
| --- | --- | ---: | ---: |
| Independent | A | 25 | 25 |
| Independent | B | 25 | 25 |
| Associated | A | 50 | 0 |
| Associated | B | 0 | 50 |

Both populations contain 50 cells of each clonotype and 50 cells of each state. A diversity measure based only on clonotype frequencies, or only on state frequencies, cannot distinguish them.

In the Independent population, knowing clonotype leaves state equally uncertain. In the Associated population, knowing clonotype determines state. This is dependence between clonotype and state.

## What mutual information measures

Probabilities are obtained by dividing the table counts by 100. With logarithms to base two, define entropy and mutual information as

\[
H(C)=-\sum_c p(c)\log_2p(c),\qquad
I(C;S)=\sum_{c,s}p(c,s)\log_2\frac{p(c,s)}{p(c)p(s)}.
\]

Zero terms contribute zero by their limit. Units are bits.

Both populations have \(H(C)=H(S)=1\) bit, but mutual information is zero in Independent and one bit in Associated. Since \(H(S\mid C)=H(S)-I(C;S)\), within-clone state uncertainty is one and zero bits respectively.

Identical clonotype diversity can therefore conceal different within-clone state heterogeneity. Even this 100-cell calculation shows why diversity alone cannot describe the entire response question.

These are not TCRi estimates. They are count-based calculations with fixed clone and state definitions. In real data, phenotype boundaries are ambiguous and sparsely sampled clones have uncertain distributions. TCRi explicitly treats assignments probabilistically [(2)](#ref-2).

## Low information does not automatically mean effective immunity

Zero bits in the artificial example means only that state variation is unrelated to clonotype. The table does not reveal tumor killing, tumor-antigen recognition or treatment-driven expansion. High information likewise means only that states differ by clone.

Interpreting the reported response association requires tissue, time point and treatment context. An indicator estimated using post-treatment information cannot automatically be used for pretreatment selection. The original study does, however, include retraining on pretreatment data alone [(1)](#ref-1). The issue is not an absence of temporal checks, but the distinction between those checks and pretreatment prediction in independent patients.

Mutual information also has several normalization conventions. A normalized value is not on the same numerical scale as this bit-based example. Refining phenotype categories or changing priors can alter estimated dependence. Comparisons across studies require matching distribution weights and estimation methods.

## More cells are not more patients

Additional cells can improve estimation of one patient's clone–state distribution. They do not increase the number of independent patients available to estimate response differences.

Pooling cells without respecting patients gives greater influence to heavily sampled patients. It can also mix between-patient state differences with within-patient clone–state dependence. Equalizing cell counts does not itself remove differences in tissue or sampling time.

The original study includes clonotype-permutation null models and cell-subsampling analyses [(1)](#ref-1). It would be inaccurate to claim that sampling effects were never examined. Nevertheless, within-cohort robustness and prospective prediction in independent patients remain different questions.

## Conclusion

TCRi decomposes the question of T cell diversity into the distributions involved. The marginal distributions of clonotype and state do not establish how they are connected.

The association between low mutual information and response concerns that connection. It is neither a general law that greater diversity improves treatment response nor an established patient-selection threshold. Biological interpretation requires keeping the patients, time points and conditioning information attached to the estimated distribution.

## Data and code availability

The counts and information measures are in `TCR` in the [calculation script](shared/tcri-clone-phenotype/reproduce.py) and [output](shared/tcri-clone-phenotype/illustration.json). This is not a TCRi implementation. The original processed data and acceptance-time code are available through [Zenodo](https://doi.org/10.5281/zenodo.21723747), with software in the [official repository](https://github.com/nceglia/tcri) [(1)](#ref-1).

[Download code and results](shared/tcri-clone-phenotype/tcri-clone-phenotype.zip).

## References

1. <a id="ref-1"></a> Ceglia N, Salehi S, Sethna ZM, Elhanati Y, Freeman SS, Lyudovyk O, et al. An information-theoretic framework for inferring T cell dynamics from single-cell RNA and T cell receptor sequencing. Nature Genetics. 2026 Nov 5. [https://doi.org/10.1038/s41588-026-02781-x](https://doi.org/10.1038/s41588-026-02781-x).

2. <a id="ref-2"></a> TCRi developers. TCRi: Information Theoretic Framework for Paired Single Cell Gene Expression and TCR Sequencing [Software documentation]. GitHub [cited 2026 Nov 8]. [Repository](https://github.com/nceglia/tcri).
