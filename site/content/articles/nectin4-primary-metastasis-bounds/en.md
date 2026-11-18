Among 137 paired primary and distant metastatic urothelial carcinoma specimens, membranous NECTIN-4 was classified as negative (H-score 0–14) in 27 primaries and 54 metastases. [Figure 1 of the paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10102834/#F1) shows the decline by site ([1](#ref-1)). If an archival primary substitutes for a metastasis, how many primary-positive cases could be negative at the metastatic site? I calculated what the published marginal counts alone imply.

## Marginal counts bound the paired transitions

If $a$ pairs were negative at both sites, $54-a$ would have a positive primary and a negative metastasis, and $27-a$ the reverse. The four nonnegative cell counts require $0\leq a\leq27$. There were 110 primary-positive pairs, so the implied fraction negative in the metastasis is 27/110 to 54/110, or 24.5–49.1%.

**Table 1.** Boundary tables compatible with the marginal counts alone. Neither row represents an observed cross-tabulation.

| Both negative | Primary negative only | Metastasis negative only | Both positive | Discordant |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 27 | 54 | 56 | 81 |
| 27 | 0 | 27 | 83 | 27 |

Every allocation in Table 1 has 27 more transitions from primary-positive to metastasis-negative than in the reverse direction. Yet the total number of discordant pairs ranges from 27 to 81. These are the limits of the site totals before adding information from the figure or individual cases. [Figure 1C of the paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10102834/#F1) shows at least one concordant negative pair. Adding that information lowers the upper bound to 53/110 (48.2%) ([1](#ref-1)). Positivity by site does not determine the classification error of substituting one specimen for another.

Negative status uses the study’s membranous staining definition. The calculation does not quantify unmeasured lesions or account for changes in lesion selection and staining thresholds. Associations in the separate enfortumab vedotin cohort address a different question from site discordance in the 137 pairs ([1](#ref-1)).

## Data and code availability

The [reproducibility ZIP](shared/nectin4-primary-metastasis-bounds/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Klümper N, Ralser DJ, Ellinger J, Roghmann F, Albrecht J, Below E, et al. Membranous NECTIN-4 expression frequently decreases during metastatic spread of urothelial carcinoma and is associated with enfortumab vedotin resistance. Clin Cancer Res. 2023;29(8):1496–1505.](https://doi.org/10.1158/1078-0432.CCR-22-1764)
