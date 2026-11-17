Suppose an AI model ranks 1,000 candidates. Assays on the top 100 yield 20 hits, a 20% hit rate in the selected group. What fraction of all hits on the list did those 100 candidates capture? In diagnostic research, verifying disease selectively after an initial test can bias performance estimates ([1](#ref-1)). A similar problem arises when ranked compounds outside the selected set remain untested.

## Twenty hits leave the denominator open

Assume every candidate could be evaluated with the same assay criterion and every measurement returns a result. If none of the lower 900 are tested, the list contains anywhere from 20 to 920 hits. Recall, the top-set hits divided by all hits, can then range from about 2.2% to 100%. If the lower set contains 18 hits, the overall hit rate is 3.8% and the recall at 100 is $20/38$ (about 52.6%). The 18 hits are a scenario assumption. Measuring the top set does not determine that number.

## Finding zero hits in a random sample

Take a simple random sample of $m$ candidates from the lower group without replacement. If $x$ are hits, estimate the total as $20+900x/m$. Across repeated samples, the estimator averages to the true total. If there are 18 hits in the lower group, the probability of finding none is the number of ways to draw $m$ candidates from the 882 negatives divided by the number of ways to draw from all 900.

**Table 1. Random sampling if the lower group contains 18 hits**

| Lower-ranked candidates assayed | Probability of no hits | Standard error of estimated total hits |
| ---: | ---: | ---: |
| 30 | 54.0% | 22.63 hits |
| 90 | 14.7% | 12.61 hits |
| 180 | 1.7% | 8.40 hits |

In Table 1, zero hits in 30 assays is compatible with 18 missed hits. Unbiased estimation of the total does not imply unbiased recall when that estimate is used as the denominator. If some assays fail, counting those results as negative can introduce a separate source of bias.

## Data and code availability

The calculation uses hypothetical inputs. [Download the Python code and output](shared/screening-rank-random-audit/companion.zip).

## References

1. <a id="ref-1"></a> [Begg CB, Greenes RA. Assessment of diagnostic tests when disease verification is subject to selection bias. Biometrics. 1983;39(1):207–215.](https://doi.org/10.2307/2530820)
