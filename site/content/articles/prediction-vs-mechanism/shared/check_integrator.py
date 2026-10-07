"""Compare the exponential integrator in identifiability_demo.py with SciPy's Radau solver.

Run: python check_integrator.py  (prints the maximum absolute difference in R)
"""
import numpy as np
from scipy.integrate import solve_ivp

import identifiability_demo as d

TIMES = np.array([0.25, 1, 7, 28.0, 60, 84])

for kout, s in [(2.0, 0.075), (1000.0, 0.073)]:
    grid, r = d.simulate(kout, s, d.NEW_REGIMEN, 84.0)
    ours = np.interp(TIMES, grid, r)
    rhs = lambda t, y: kout * d.R0 - kout * (1 + s * d.conc(np.array([t]), d.NEW_REGIMEN)[0]) * y
    ref = solve_ivp(rhs, (0, 84), [d.R0], t_eval=TIMES, method="Radau", rtol=1e-10, atol=1e-10, max_step=0.01)
    assert ref.success, ref.message
    print(f"k_out = {kout:g}/day, S = {s}: max |difference| = {np.max(np.abs(ours - ref.y[0])):.2e}")
