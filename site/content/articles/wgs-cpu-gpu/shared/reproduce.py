"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

result = {"source": "Reddit post; not reproduced",
          "reported_cpu_hours": 3.0, "reported_gpu_hours": 3.2,
          "reported_cpu_over_gpu_time": 3.0 / 3.2,
          "cost_break_even_gpu_over_cpu_hourly_price": 3.0 / 3.2}

output = {'WGS': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
