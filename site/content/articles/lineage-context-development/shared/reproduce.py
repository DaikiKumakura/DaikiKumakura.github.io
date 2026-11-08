"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

trees_a = [{"X": 0, "S": s, "Y": s, "probability": 0.5} for s in (0, 1)]
trees_b = [{"X": 0, "S": s, "Y": 1 - s, "probability": 0.5} for s in (0, 1)]
def marginal_y(rows):
    return [sum(row["probability"] for row in rows if row["Y"] == y) for y in (0, 1)]
def conditional(rows):
    selected = [row for row in rows if row["X"] == 0 and row["S"] == 0]
    return sum(row["probability"] for row in selected if row["Y"] == 1) / sum(row["probability"] for row in selected)
result = {"same_marginals": marginal_y(trees_a) == marginal_y(trees_b),
          "P_Y1_given_X0_S0_model_A": conditional(trees_a),
          "P_Y1_given_X0_S0_model_B": conditional(trees_b),
          "definition": "X=0 always; S fair binary; A: Y=S; B: Y=1-S",
          "joint_model_A": trees_a, "joint_model_B": trees_b}

output = {'lineage': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
