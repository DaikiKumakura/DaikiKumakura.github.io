"""Reproduce the article illustration; no empirical model fitting."""
import json
import math
from pathlib import Path

result = []
for n_donors, cells in [(50, 20), (50, 100), (100, 20)]:
    tau2, sigma2 = 1.0, 4.0
    result.append({"n_donors": n_donors, "cells_per_donor": cells,
                   "total_cells": n_donors * cells, "tau2": tau2, "sigma2": sigma2,
                   "se_beta": math.sqrt((tau2 + sigma2 / cells) / n_donors)})

output = {'donor_design': result}
target = Path(__file__).with_name("illustration.json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, ensure_ascii=False, indent=2))
