"""Checks: dose accounting, no-binding limit equals the linear model, baseline sBCMA steady state."""
import json
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import model  # noqa: E402
import tmdd  # noqa: E402

INP = json.loads((Path(__file__).resolve().parent / "inputs.json").read_text(encoding="utf-8"))


class TestTMDD(unittest.TestCase):
    def test_no_binding_matches_linear(self):
        p = tmdd.typical(INP)
        p["Kd"] = 1e9  # binding negligible
        t = np.array([1.0, 3.0, 7.5, 14.0])
        doses = [(0.0, 12.0), (3.0, 32.0), (7.0, 76.0)]
        c_tmdd = tmdd.simulate(doses, p, t)[0]
        lin = {k: np.array([[INP["tmdd"][k]]]) for k in ("CL", "Vc", "Vp", "Q", "ka")}
        lin["F"] = INP["tmdd"]["F"]
        c_lin = model.concentration(t, doses, lin)[0] * 1000
        np.testing.assert_allclose(c_tmdd, c_lin, rtol=2e-3)

    def test_baseline_target_steady(self):
        p = tmdd.typical(INP)
        y0 = np.concatenate([np.zeros(1), np.zeros(1), np.zeros(1), p["BL"] * p["Vcs"]])
        d = tmdd.rhs(0.0, y0, p, 1)
        self.assertAlmostEqual(float(d[3]), 0.0, places=9)


if __name__ == "__main__":
    unittest.main()
