"""Check the closed-form steady-state Cavg against a numerical 3-compartment simulation (typical subject)."""
import json
import unittest
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

INP = json.loads((Path(__file__).resolve().parent / "inputs.json").read_text(encoding="utf-8"))


class TestCavg(unittest.TestCase):
    def test_closed_form_matches_ode(self):
        pk = INP["pk"]
        f, dose = np.exp(pk["Frel_fast2_exp"]), 600.0
        vc = pk["Vc_L"]
        ka = pk["ka_per_h"] * np.exp(pk["ka_fast2_exp"])
        k10, k12, k21, k13, k31 = pk["CL_L_h"] / vc, pk["Q3_L_h"] / vc, pk["Q3_L_h"] / pk["V3_L"], pk["Q4_L_h"] / vc, pk["Q4_L_h"] / pk["V4_L"]

        def rhs(t, y):
            d, c, p1, p2 = y
            return [-ka * d, ka * d - (k10 + k12 + k13) * c + k21 * p1 + k31 * p2, k12 * c - k21 * p1, k13 * c - k31 * p2]
        y = np.zeros(4)
        for day in range(60):
            y[0] += f * dose * 1e6
            sol = solve_ivp(rhs, (0, 24), y, t_eval=np.linspace(0, 24, 241), rtol=1e-8, atol=1e-6)
            y = sol.y[:, -1].copy()
        cavg_ode = np.trapz(sol.y[1] / (vc * 1000), sol.t) / 24
        cavg_cf = f * dose * 1e6 / (pk["CL_L_h"] * 1000 * 24)
        self.assertAlmostEqual(cavg_ode / cavg_cf, 1.0, delta=0.02)


if __name__ == "__main__":
    unittest.main()
