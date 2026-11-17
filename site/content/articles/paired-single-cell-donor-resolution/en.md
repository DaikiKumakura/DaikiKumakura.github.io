In a paired single-cell study, cells from each donor can be split between two treatments. With a fixed cell budget, should we measure more cells per donor or recruit more donors? Ignoring biological replication can generate false differential-expression discoveries ([1](#ref-1)). I used a simple design based on donor-level treatment differences to calculate two constraints that extra cells alone cannot remove.

## Donor count sets the resolution of the test

For example, assign the two treatments at random within each donor, independently across donors, and assume under the null that treatment has no effect on any sample. The labels can then be swapped within each donor, and $d$ independent donors give $2^d$ equally likely assignments. For the absolute sum of donor differences, reversing every sign gives the same statistic. With all differences nonzero, the most extreme case therefore gives a two-sided p-value of $2/2^d$. The minimum is 0.0625 at five donors and 0.03125 at six.

The minimum is a limit on resolution. For six differences of 0.20, 0.16, 0.12, 0.10, 0.08 and −0.01, enumerating all 64 assignments gives a two-sided p-value of 4/64, or 0.0625. More cells can improve the measurement of each difference, while leaving the number of possible assignments unchanged.

## Allocating a fixed cell budget

In a variance example, I set the between-donor standard deviation of true treatment differences to 0.20 and the within-donor, within-treatment cell measurement standard deviation to one. With $m$ independent cells per donor per treatment and an equally weighted donor mean, its variance is $0.20^2/d+2/(dm)$. Table 1 fixes the total at 12,000 cells. The cell-measurement term stays the same and the between-donor term falls.

**Table 1.** Calculated precision for two allocations of the same cell total.

| Donors | Cells per donor per treatment | Total cells | SE of mean difference | Smallest two-sided p |
| --- | ---: | ---: | ---: | ---: |
| 6 | 1,000 | 12,000 | 0.08367 | 0.03125 |
| 12 | 500 | 12,000 | 0.06055 | 0.000488 |

The test relies on a design and null that allow within-donor exchanges. The variance calculation assumes independent cell errors, balanced cell numbers, equal variances, and independence between donor effects and cell errors. Rare cell types, uneven cell counts and multiple testing can change the practical allocation. The table uses assumed variances rather than estimating power from measured data.

## Data and code availability

The differences and variances are hypothetical. The [companion ZIP](shared/paired-single-cell-donor-resolution/companion.zip) contains the complete enumeration and variance calculation.

## References

1. <a id="ref-1"></a> Squair JW, Gautier M, Kathe C, Anderson MA, James ND, Hutson TH, et al. Confronting false discoveries in single-cell differential expression. Nat Commun. 2021;12:5692. [doi:10.1038/s41467-021-25960-2](https://doi.org/10.1038/s41467-021-25960-2).
