"""Extra descriptive checks for the cellpainting-2d-3d deep pass (not in the shared zip).
Usage: python -X utf8 extra-descriptive-checks.py <path to the unzipped cellpainting-2d-3d analysis folder>
"""
import sys, itertools
from pathlib import Path
import numpy as np, pandas as pd
root = Path(sys.argv[1]) / 'inputs'
def cos(a, b): return float(a @ b / np.linalg.norm(a) / np.linalg.norm(b))
p = pd.read_csv(root / 'Fig5d.csv')
d = p['difference']
i = p[((p.Drug1 == 'Fluor') & (p.Drug2 == 'Olapa')) | ((p.Drug2 == 'Fluor') & (p.Drug1 == 'Olapa'))].index[0]
print('pairs', len(p), 'median diff', d.median(), 'Q1', d.quantile(.25), 'Q3', d.quantile(.75),
      'n negative', int((d < 0).sum()), 'n positive', int((d > 0).sum()),
      'rank by |diff|', int(d.abs().rank(ascending=False)[i]), 'diff', d[i])
z2 = np.load(root / '2D.npz'); z3 = np.load(root / '3D.npz')
common = sorted(set(z2['features'].tolist()) & set(z3['features'].tolist()))
res = {}
for fmt, z in [('2D', z2), ('3D', z3)]:
    x = z['x']; f = list(z['features']); m = pd.read_csv(root / f'{fmt}_wells.csv')
    x = x[:, [f.index(c) for c in common]]
    prof = {}
    for drug, dose in [('5-FU', 10.0), ('Olaparib', 3.0)]:
        sel = ((m.drug == drug) & (m.dose_uM == dose)).to_numpy()
        xs = x[sel]; ms = m[sel]; pl = sorted(ms.plate.unique())
        a = np.median(xs[(ms.plate == pl[0]).to_numpy()], 0); b = np.median(xs[(ms.plate == pl[1]).to_numpy()], 0)
        wp = [cos(xs[u], xs[v]) for u, v in itertools.combinations(range(len(xs)), 2)]
        prof[drug] = np.median(xs, 0)
        res[fmt, drug] = cos(a, b)
        print(fmt, drug, 'n wells', len(xs), 'plate-split cosine', round(res[fmt, drug], 3),
              'well-pair cosine min/max', round(min(wp), 2), round(max(wp), 2))
    obs = cos(prof['5-FU'], prof['Olaparib'])
    ceil = (res[fmt, '5-FU'] * res[fmt, 'Olaparib']) ** .5
    print(fmt, 'observed', round(obs, 3), 'ceiling sqrt(r1*r2)', round(ceil, 3), 'ratio', round(obs / ceil, 2))
