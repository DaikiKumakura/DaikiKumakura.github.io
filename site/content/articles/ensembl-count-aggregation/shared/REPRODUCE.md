# Reproducing the count-aggregation examples

These are deterministic synthetic counterexamples, not observations of real genes or cells. The script calls no gene-mapping service and does not train scVI.

Requirements: Python 3.10 or later, standard library only. Verified with Python 3.12.4. No installation, network access or random seed is required.

```sh
python analysis.py
```

Run from the directory containing this file. The script creates `results/results.json` and `results/set-examples.csv` alongside itself. It can also be launched with its path from another directory.

The asserted distinct molecule counts are 13, 9 and 8 for the disjoint, overlapping and duplicated examples. A one-cell duplication produces an apparent normalized target fold change of 20/11 (approximately 1.81818). Dividing synthetic counts by their separate lengths and summing gives 10.5; dividing their sum by an arbitrary illustrative 1.5 kb gives 8.66667. The latter is not a valid recommendation for gene-length calculation.

Molecule labels represent already resolved identities, not raw UMI strings. Equal UMIs alone do not establish that molecules are identical. The examples demonstrate lost information in aggregate counts; they cannot infer overlap from a real count matrix, validate a gene-name conversion or replace transcript quantification.

The `python` field records the executing interpreter version. The numerical examples are independent of that field. The article rounds some outputs for display. All code and synthetic data in this package were created for the article and are available under the accompanying MIT license.
