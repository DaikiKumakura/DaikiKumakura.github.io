"""Linear two-compartment model with first-order SC absorption (analytic superposition).

Units: dose mg, volumes L, clearances L/day, time day -> concentration mg/L (x1000 = ng/mL).
"""
from __future__ import annotations

import numpy as np


def unit_response(t: np.ndarray, cl, vc, vp, q, ka) -> np.ndarray:
    """Central concentration (mg/L) after 1 mg absorbed-amount input into depot (F applied outside).

    Parameters may be arrays (one value per subject, shape (n,1)) broadcast against t (shape (m,)).
    """
    k10, k12, k21 = cl / vc, q / vc, q / vp
    s = k10 + k12 + k21
    disc = np.sqrt(s * s - 4 * k10 * k21)
    alpha, beta = (s + disc) / 2, (s - disc) / 2
    tt = np.maximum(t, 0.0)
    a = ka * (k21 - alpha) / ((ka - alpha) * (beta - alpha))
    b = ka * (k21 - beta) / ((ka - beta) * (alpha - beta))
    c = ka * (k21 - ka) / ((alpha - ka) * (beta - ka))
    out = (a * np.exp(-alpha * tt) + b * np.exp(-beta * tt) + c * np.exp(-ka * tt)) / vc
    return np.where(t >= 0, out, 0.0)


def concentration(t: np.ndarray, doses: list[tuple[float, float]], p: dict) -> np.ndarray:
    """Superpose SC doses [(time_day, mg), ...]; returns mg/L with shape broadcast of params x t."""
    total = 0.0
    for td, mg in doses:
        total = total + p["F"] * mg * unit_response(t - td, p["CL"], p["Vc"], p["Vp"], p["Q"], p["ka"])
    return total


def sample_subjects(inp: dict, n: int, rng: np.random.Generator) -> dict:
    pk = inp["pk_free_drug_linear_approx"]
    female = rng.random(n) < inp["population"]["female_fraction"]
    high_tb = rng.random(n) < inp["population"]["high_tumor_burden_fraction_known"]

    def lognorm(cv_pct: float) -> np.ndarray:
        omega2 = np.log(1 + (cv_pct / 100) ** 2)
        return np.exp(rng.normal(0, np.sqrt(omega2), n))

    cv = pk["iiv_cv_pct"]
    cl = pk["CL_L_day"] * np.where(female, 1 + pk["sex_on_CL_female"], 1.0) * lognorm(cv["CL"])
    return {
        "CL": cl[:, None], "Vc": (pk["Vc_L"] * lognorm(cv["Vc"]))[:, None],
        "Vp": (pk["Vp_L"] * lognorm(cv["Vp"]))[:, None], "Q": (pk["Q_L_day"] * lognorm(cv["Q"]))[:, None],
        "ka": np.full((n, 1), pk["ka_per_day"]), "F": pk["F"], "female": female, "high_tb": high_tb,
    }


def crs_probability(c_day4_ng_ml: np.ndarray, high_tb: np.ndarray, b0: float, b_tb: float, b_c: float) -> np.ndarray:
    logit = b0 + b_tb * high_tb + b_c * np.log(c_day4_ng_ml)
    return 1 / (1 + np.exp(-logit))
