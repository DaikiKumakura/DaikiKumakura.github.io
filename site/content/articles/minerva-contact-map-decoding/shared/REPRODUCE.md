# Reproduce the artificial contact-map example

Numeric calculation uses Python 3.12.4 and the standard library only:

```bash
python analysis.py
```

Outputs: `results/decoding.csv` and `results/results.json`. No model is loaded and no network request is made. Sequence `GGAAAACC` and weights (0,6)=0.9, (0,7)=0.8, (1,6)=0.8 are artificial; all other weights are zero. Indices are zero-based. Candidate generation uses a symmetric elementwise maximum, minimum position separation 3 and first-index tie breaking. Only the three candidates at or above 0.6 are compared. Exact matching enumerates all eight subsets, rejecting reuse of positions. It does not solve a general thermodynamic RNA-folding problem.

Optional figure rendering used matplotlib 3.9.1:

```bash
python make_figure.py
```

It writes `figures/decoding.png`. The arcs identify selected pairs, not physical molecular geometry. Figure rendering is independent of the numeric calculation.

In a separate local verification, four unchanged function definitions (`_as_numpy`, `pair_candidates`, `match_candidates`, `call_base_pairs`) were extracted with Python's AST from [Minerva rna_structure.py](https://github.com/garykbrixi/minerva/blob/900fb32a427f2ebed601569257877167ea45c9ed/minerva/rna_structure.py), commit `900fb32a427f2ebed601569257877167ea45c9ed`, Git blob `7d97d12bf8d909c0bbd7e74025cae789e29a0bd7`. They were executed with NumPy and their documented constants/type names supplied, without importing model or visualization modules. Their outputs agree with the independent greedy implementation at thresholds 0.6, 0.8, 0.9 and 0.91. See `upstream-verification.json` for the record and NumPy version.

Upstream source is not bundled. To repeat that separate comparison, obtain the identified file from its original repository and execute those definitions with NumPy; no model weights are needed. The distributed independent calculation is reproducible without upstream code.

No randomness is used. The example does not estimate model accuracy, probabilities of base pairs, thermodynamic stability, or the frequency of greedy/optimal disagreement in real predictions. The Python version string can differ on another interpreter while numeric outputs remain identical.
