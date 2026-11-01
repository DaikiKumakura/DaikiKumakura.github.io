# Reproduce the hypothetical reassignment calculation

This is an original explanatory model, not a reproduction of the published segmentation benchmark or Giotto analysis. A and B have equal cell numbers with one-to-one adjacency. Per-cell means are L=50/R=0 in A and L=0/R=50 in B. A symmetric fraction of transcripts is reassigned to the other type. Cell numbers and expression totals remain fixed.

Python 3.12.4 and matplotlib 3.9.1 were used. No external data are required. Run from the directory containing the script:

```bash
python -m pip install matplotlib==3.9.1
python analysis.py
```

Outputs: `results/reassignment.csv`, `results/summary.json`, `figures/reassignment.svg`, `figures/reassignment.png`. PNG is an alternative rendering of the same figure. At 10% reassignment the A-to-B, B-to-A and each within-type product are 2025, 25 and 225. Products are arbitrary units, not communication rates. No random number generator is used.

The included CSV and SVG are copies of these outputs. Regenerated SVG metadata and Python-version strings can differ without changing numerical results.
