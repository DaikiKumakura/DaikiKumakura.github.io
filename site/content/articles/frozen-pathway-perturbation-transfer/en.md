When a gene expression score separates stimulated cells from untreated cells, it can still be hard to tell which stimulus produced the response. IFN-β and IFN-γ, for example, both induce interferon responses. I tested whether frozen scores transfer to other experiments by including a treatment worth distinguishing from the target as well as an untreated control.

## Taking fixed weights to another experiment

For each axis I ranked absolute effects within each development study on a percentile scale and restored their signs. I averaged the signed ranks for genes whose signs agreed across the two studies and kept the 50 with the largest absolute mean rank. MAPK used [GSE312195](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312195) and [GSE87419](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87419). IFN-I and IFN-II used [GSE185200](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185200) and [GSE236156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE236156). The evaluation data did not change the gene selection or weights. For each sample I rescaled within-sample ranks over all measured genes to −0.5 through 0.5, using average ranks for ties. I divided the signed weighted sum by the sum of absolute weights for the measured signature genes.

I evaluated IFN using HeLa cells from GSE103363, with three biological replicates each of unstimulated cells, IFN-β and IFN-γ ([1](#ref-1)). I retained probes with one Entrez ID in the Affymetrix GPL6244 annotation, mapped those to one-to-one HGNC Ensembl IDs, and took the median when several probes mapped to one gene. This left 18,664 genes for ranking ([2](#ref-2), [3](#ref-3)). For MAPK I used the 51T-2D pancreatic cancer cell line from GSE301146. I selected three replicates each of sotorasib, palbociclib and vehicle at 48 hours, ranking 26,485 genes in the released normalized matrix ([4](#ref-4)). Sotorasib inhibits the upstream target KRAS G12C. The comparison with palbociclib does not directly measure ERK activity.

## Separating the target from the other treatment

Table 1 shows the full-sample contrasts and the omission check.

**Table 1.** Contrasts from fixed scores and the number of omissions preserving both directions.

| Axis | Absolute weight coverage | Target minus control | Target minus other treatment | Both signs under omissions |
| --- | ---: | ---: | ---: | ---: |
| IFN-I (IFN-β) | 100.0% | +0.1799 | +0.0713 | 27/27 |
| IFN-II (IFN-γ) | 94.0% | +0.1102 | +0.1074 | 27/27 |
| MAPK (sotorasib) | 100.0% | −0.1212 | −0.0898 | 27/27 |

For IFN-I, the gap was smaller against IFN-γ than against untreated cells. The two signs survived all 27 ways of leaving out one sample per arm. The minimum IFN-I difference against untreated cells was +0.1720, and the minimum against IFN-γ was +0.0650. These are separate minima and need not come from the same omission.

The 27 combinations reuse the same nine samples. Each axis was tested in one cell line, leaving transfer across doses, timings and species untested. Absolute scores also depend on the measured gene universe and should not be treated as a common scale across experiments. The result is confined to these two experiments outside development: each frozen score moved in the expected direction against both its control and its comparison treatment.

## Data and code availability

The [companion ZIP](shared/frozen-pathway-perturbation-transfer/companion.zip) contains the weights, source locations, preprocessing and scoring code, and final table.

## References

1. <a id="ref-1"></a> Randow F, Wandel MP. Expression data from HeLa cells upon interferon-gamma or interferon-beta treatment. NCBI Gene Expression Omnibus. [GSE103363](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103363).
2. <a id="ref-2"></a> NCBI Gene Expression Omnibus. Affymetrix Human Gene 1.0 ST Array. [GPL6244](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6244).
3. <a id="ref-3"></a> HUGO Gene Nomenclature Committee. HGNC complete set. [HGNC download archive](https://www.genenames.org/download/archive/).
4. <a id="ref-4"></a> Paulsohn MB, Frahnert KH, Schlösser D, Oschwald J, Kopp W, Fang X, et al. Simultaneous targeting of KRAS and CDK4 synergistically induces durable growth arrest in pancreatic cancer cells. Cell Death Dis. 2026;17:129. [doi:10.1038/s41419-025-08362-w](https://doi.org/10.1038/s41419-025-08362-w) · [Figure 3](https://www.nature.com/articles/s41419-025-08362-w/figures/3) · [GSE301146](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301146).
