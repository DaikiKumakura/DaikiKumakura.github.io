"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

groups = [dict(group="familiar", selected=100, acceptable=90),
          dict(group="novel", selected=100, acceptable=50)]
for group in groups:
    group["precision"] = group["acceptable"] / group["selected"]
result = dict(selected=groups,
              pooled_precision=sum(x["acceptable"] for x in groups) / sum(x["selected"] for x in groups),
              illustrative_novel_fraction=0.8,
              target_precision=0.2 * groups[0]["precision"] + 0.8 * groups[1]["precision"])

output = {'AF3_threshold_illustration': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
