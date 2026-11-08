"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

def information(counts):
    total = sum(map(sum, counts))
    rows = [sum(row) / total for row in counts]
    cols = [sum(row[j] for row in counts) / total for j in range(len(counts[0]))]
    entropy = lambda probs: -sum(p * math.log2(p) for p in probs if p)
    mi = sum((n / total) * math.log2((n / total) / (rows[i] * cols[j]))
             for i, row in enumerate(counts) for j, n in enumerate(row) if n)
    return {"n_cells": total, "counts": counts, "H_clone_bits": entropy(rows),
            "H_state_bits": entropy(cols), "MI_bits": mi,
            "H_state_given_clone_bits": entropy(cols) - mi}

result = {"independent": information([[25, 25], [25, 25]]),
          "associated": information([[50, 0], [0, 50]])}

output = {'TCR': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
