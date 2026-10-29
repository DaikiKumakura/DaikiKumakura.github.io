"""Extra checks for the dll3-ctc-count-precision deep pass (read-only on the analysis zip).

Reads the transcribed Mishra et al. Table S3 and src/precision.py directly from the
published analysis zip; prints numbers used in the article. No random numbers.
"""
import csv, io, json, types, zipfile
from math import ceil, floor
from pathlib import Path
import numpy as np
from scipy.stats import beta, binom, norm

import argparse
parser = argparse.ArgumentParser(description="Reproduce supplementary count-precision checks from the published analysis archive.")
parser.add_argument("--archive", type=Path, default=Path(__file__).with_name("dll3-ctc-count-precision-analysis.zip"))
ZIP = parser.parse_args().archive
z = zipfile.ZipFile(ZIP)
mod = types.ModuleType("precision")
exec(z.read("dll3-ctc-count-precision/src/precision.py").decode(), mod.__dict__)
rows = list(csv.DictReader(io.StringIO(z.read("dll3-ctc-count-precision/data/processed/table_s3_transcription.csv").decode())))
C = {r["patient_id"]: int(r["count_per_20ml"]) for r in rows}
R = {r["patient_id"]: int(r["dll3_percent"]) for r in rows}

# 1. pooled totals vs the paper's response-group totals (1868+182+52) and marker classes (1727+328)
tot = sum(C.values()); pos = sum(C[i]*R[i]/100 for i in C)
print("sum normalized", tot, "sum c*r/100 = %.2f" % pos, "paper by response 1868+182+52 =", 1868+182+52,
      "paper by marker class 1727+328 =", 1727+328, "difference", (1868+182+52)-(1727+328))

# 2. where do the crossing envelopes sit
def lo_hi(k, n, kind):
    if kind == "cp":
        lo = 0 if k == 0 else beta.ppf(.025, k, n-k+1); hi = 1 if k == n else beta.ppf(.975, k+1, n-k); return lo, hi
    if kind == "jeffreys":
        return beta.ppf(.025, k+.5, n-k+.5), beta.ppf(.975, k+.5, n-k+.5)
    if kind == "wilson":
        z_ = norm.ppf(.975); ph = k/n; d = 1+z_**2/n
        c = (ph+z_**2/(2*n))/d; h = z_*np.sqrt(ph*(1-ph)/n+z_**2/(4*n**2))/d; return c-h, c+h
for kind in ["cp", "jeffreys", "wilson"]:
    cross = []
    for i in C:
        pairs = mod.compatible_pairs(C[i], R[i])
        lo = min(lo_hi(k, n, kind)[0] for k, n in pairs); hi = max(lo_hi(k, n, kind)[1] for k, n in pairs)
        if lo <= .25 <= hi: cross.append(i)
    pos_cross = [i for i in cross if R[i] >= 25]
    print(kind, "crossing", len(cross), cross, "positive:", pos_cross, "low:", [i for i in cross if R[i] < 25])

# 3. healthy-donor background scale (paper Methods: median 0.2/mL, mean 0.18/mL, range 0-3/10 mL)
print("background per 20 mL: median %.1f mean %.1f max %.1f" % (0.2*20, 0.18*20, 3/10*20))
print("patients with normalized count <= 6:", [(i, C[i]) for i in C if C[i] <= 6])

# 4. gap in displayed percentages
low = [R[i] for i in R if R[i] < 25]; hi_ = [R[i] for i in R if R[i] >= 25]
print("largest low", max(low), "smallest positive", min(hi_), "n low", len(low), "n pos", len(hi_))

# 5. effective n under exchangeable correlation
for n in (100, 200, 500):
    print(n, {rho: round(n/(1+(n-1)*rho), 1) for rho in (.01, .05)})

# 6. distance from 25% at which mismatch <= 5% (independent cells)
def mism(n, p):
    q = binom.cdf(ceil(n*.25-1e-12)-1, n, p)
    return q if p > .25 else 1-q
for n in (20, 50, 100, 200, 500, 1000):
    ps = np.arange(0.0005, 0.9995, 0.0005)
    lo_ok = max([p for p in ps if p < .25 and mism(n, p) <= .05], default=None)
    hi_ok = min([p for p in ps if p > .25 and mism(n, p) <= .05], default=None)
    print(n, "p<= %s or p>= %s" % (lo_ok, hi_ok))
