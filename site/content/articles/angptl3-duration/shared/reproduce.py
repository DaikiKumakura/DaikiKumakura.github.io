"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

result = [{"half_lives_elapsed": t, "production_fraction": 0.1,
           "P_over_P0": 0.1 + 0.9 * 2 ** (-t)} for t in (0, 1, 3, 5)]

output = {'protein_turnover': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
