"""Enumerate all integer (n, responders) per dose group consistent with the reported abstract percentages and totals.
Run: python n_uniqueness_check.py. Shows whether the derived n of the monotherapy (HARMONi-5 abstract) and SCLC groups are unique."""
import itertools

def cands(pct, nmax=80, tol=0.05):
    return [(n, r) for n in range(1, nmax) for r in range(n + 1) if abs(100 * r / n - pct) <= tol]

# Monotherapy, PD-L1+ first-line: 67 patients; ORR 33.3/52.6/60.0/75.0 (10 Q3W, 20 Q2W, 20 Q3W, 30 Q3W)
mono = [cands(p) for p in (33.3, 52.6, 60.0, 75.0)]
sol = [c for c in itertools.product(*mono) if sum(x[0] for x in c) == 67]
print("monotherapy: total n=67 only ->", len(sol), "solutions")
sol2 = [c for c in sol if c[0][0] == 21 and c[2][0] == 15 and c[1][0] + c[3][0] == 31 and sum(x[1] for x in c[1:2] + c[3:]) == 19]
print("  adding the editorial table (n=21, 15, and 31 for the two groups sharing 10 mg/kg/week; 19/31=61.3%) ->", sol2)
# SCLC: 35 patients; ORR 66.7/90.9/76.2 (3, 10, 20 mg/kg); overall 80% (28/35)
sclc = [cands(p) for p in (66.7, 90.9, 76.2)]
s3 = [c for c in itertools.product(*sclc) if sum(x[0] for x in c) == 35 and sum(x[1] for x in c) == 28]
print("SCLC: total n=35, 28/35 responders ->", s3)
