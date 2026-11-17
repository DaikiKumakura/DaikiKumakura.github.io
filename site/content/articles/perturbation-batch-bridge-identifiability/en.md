Suppose a single-cell perturbation experiment measures the controls in batch 1 and treated samples in batch 2. If the means differ, how much of the difference can be attributed to perturbation or to measurement batch? Song and colleagues established conditions for identifying cell-type and batch effects in their BUSseq model under designs with reference panels or connections between batches ([1](#ref-1)). This example shows which comparisons a shared control makes possible and which remain outside the observed design.

## Adding a control identifies the treatment contrast in batch 2

Consider the group means of a gene score. If the batch 1 control mean is 2 and the batch 2 treated mean is 5, their difference of 3 is the sum of a batch difference and a treatment difference in an additive model. A treatment difference of 2 with a batch difference of 1 gives the same observations as a treatment difference of −1 with a batch difference of 4.

Now add a batch 2 control with mean 3. The treatment contrast within batch 2 is $5-3=2$. Assuming the same contrast in both batches predicts a treated mean of $2+2=4$ in batch 1. Allowing a batch-by-treatment interaction allows the batch 1 treated mean to be 0 or 4, among other values, with all three observed means unchanged.

**Table 1. Observed conditions and design matrix rank**

| Observed conditions | Additive model | With interaction |
| --- | ---: | ---: |
| Batch 1 control and batch 2 treated | 2/3 | 2/4 |
| Add a batch 2 control | 3/3 | 3/4 |
| Control and treated in both batches | 3/3 | 4/4 |

The denominators in Table 1 count model coefficients. Matrix rank addresses identifiability in this simple linear model for the means and says nothing about precision. Comparing treatment contrasts across the two batches requires the treated condition in batch 1 as well. Generalization to other donors or analysis of changes in cell composition still needs the relevant donors and experimental replication.

## Data and code availability

The calculation uses hypothetical inputs. [Download the Python code and output](shared/perturbation-batch-bridge-identifiability/companion.zip).

## References

1. <a id="ref-1"></a> [Song F, Chan GMA, Wei Y. Flexible experimental designs for valid single-cell RNA-sequencing experiments allowing batch effects correction. Nat Commun. 2020;11:3274.](https://doi.org/10.1038/s41467-020-16905-2)
