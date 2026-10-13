"""Reproduce the 60 mg QD FVC summary from the paper's Source Data (individual dFVC values in the proteomics/PK sheets) and compare
the published 95% CI with normal- and t-based intervals. Needs the paper's Source Data XLSX (MOESM3) in data/raw_tmp/ (not redistributed).
Run: python source_data_check.py"""
import json
import math
import statistics
import sys
from pathlib import Path

from scipy import stats

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from xlsx_min import read

sh = read(HERE / "data/raw_tmp/MOESM3.xlsx")
vals = set()
rows = sh["Fig.4D"]
cols = sorted(rows[1].keys())
for r in rows[2:]:
    for i in range(0, len(cols), 5):
        t, d = r.get(cols[i]), r.get(cols[i + 1])
        if t == "INS018_055 60 mg QD" and d not in (None, "NA"):
            vals.add(float(d))
v = sorted(vals)
n, m, sd = len(v), statistics.mean(v), statistics.stdev(v)
se = sd / math.sqrt(n)
z, t = stats.norm.ppf(0.975), stats.t.ppf(0.975, n - 1)
out = dict(n=n, mean=round(m, 1), sd=round(sd, 1), se=round(se, 1),
           ci_normal_1p96=[round(m - z * se, 1), round(m + z * se, 1)], ci_t_df9=[round(m - t * se, 1), round(m + t * se, 1)],
           published_ci=[10.9, 185.9], published_mean=98.4, note="Individual values are not redistributed; run with the downloaded Source Data to reproduce.")
(HERE / "results/source_data_check.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
