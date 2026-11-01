# Reproduce the hypothetical occupancy and entropy calculation

This original mathematical example does not implement or benchmark a cell-potency prediction method. All profiles are hypothetical and have no lineage or potency labels.

Two 100-gene profiles: uniform has probability 0.01 for every gene; dominant assigns 0.8 to one gene and 0.2/99 to each remaining gene. For n = 50, 100, 200, 500, 1000, detected gene expectations use the occupancy formula. Expected plug-in Shannon entropy is summed exactly over binomial marginals, up to floating-point precision. Logarithms are natural, giving nats. No random number generator is used.

Python 3.12.4 and matplotlib 3.9.1 were used. Run from the script directory:

```bash
python -m pip install matplotlib==3.9.1
python analysis.py
```

Outputs: `results/depth_entropy.csv`, `results/summary.json`, `figures/depth-entropy.svg`, `figures/depth-entropy.png`. In the uniform profile n=50 gives 39.4993932862 expected detected genes and 3.60331354172 expected observed entropy. The population entropy is 4.60517018599 nats. Assert checks verify occupancy and that the expected plug-in entropy does not exceed population entropy.

Included CSV and SVG are output copies. SVG metadata and Python-version strings may change on regeneration without changing numerical results.
