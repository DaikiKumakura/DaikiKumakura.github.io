"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

result = [{"fm": fm, "I_over_Ki": 1.0,
           "AUCR": 1 / ((1 - fm) + fm / (1 + 1.0))} for fm in (0.2, 0.9)]

output = {'DDI': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
