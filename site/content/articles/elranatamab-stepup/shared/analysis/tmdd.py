"""Quasi-equilibrium sBCMA binding model of elranatamab, transcribed from the public paper's equations.

States (nmol): A1 central drug (free + complex), A2 peripheral drug, A3 SC depot, A4 sBCMA (free + complex).
Volumes L, clearances L/day, Kd and baseline sBCMA nM. Output free drug concentration in ng/mL (MW 148 kDa).
All subjects are integrated together as one vectorised ODE system.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

MW_KDA = 148.0
NMOL_PER_MG = 1e6 / (MW_KDA * 1000)  # 1 mg / 148,000 g/mol = 6.757 nmol
NG_ML_PER_NM = MW_KDA  # 1 nM = 148 ng/mL


def complex_amount(a1, a4, p):
    k = p["Kd"] * p["Vc"] * p["Vcs"] / p["Vcx"]
    s = k + a1 + a4
    return 0.5 * (s - np.sqrt(np.maximum(s * s - 4 * a1 * a4, 0.0)))


def free_drug_nm(a1, a4, p):
    return (a1 - complex_amount(a1, a4, p)) / p["Vc"]


def rhs(_t, y, p, n):
    a1, a2, a3, a4 = y[:n], y[n:2 * n], y[2 * n:3 * n], y[3 * n:]
    x = complex_amount(a1, a4, p)
    cf = (a1 - x) / p["Vc"]
    cfs = (a4 - x) / p["Vcs"]
    cx = x / p["Vcx"]
    k12, k21 = p["Q"] / p["Vc"], p["Q"] / p["Vp"]
    da1 = p["ka"] * a3 - k12 * (a1 - x) + k21 * a2 - p["CL"] * cf - p["CLx"] * cx
    da2 = k12 * (a1 - x) - k21 * a2
    da3 = -p["ka"] * a3
    da4 = p["ksyn"] - p["CLs"] * cfs - p["CLx"] * cx
    return np.concatenate([da1, da2, da3, da4])


def simulate(doses: list[tuple[float, float]], p: dict, t_obs: np.ndarray) -> np.ndarray:
    """Free drug (ng/mL), shape (n_subjects, len(t_obs)). doses: [(day, mg)] SC bolus into depot."""
    n = len(p["CL"])
    y = np.concatenate([np.zeros(n), np.zeros(n), np.zeros(n), p["BL"] * p["Vcs"]])
    out = np.full((n, len(t_obs)), np.nan)
    pc = {k: (v[:, None] if isinstance(v, np.ndarray) else v) for k, v in p.items()}
    bounds = sorted({d for d, _ in doses} | {float(t_obs.max())})
    dose_at = {}
    for d, mg in doses:
        dose_at[d] = dose_at.get(d, 0.0) + mg
    t_now = 0.0
    dosed = set()
    for tb in bounds:
        if t_now in dose_at and t_now not in dosed:
            y[2 * n:3 * n] += p["F"] * dose_at[t_now] * NMOL_PER_MG
            dosed.add(t_now)
        if tb > t_now:
            mask = (t_obs >= t_now) & (t_obs < tb)
            te = np.unique(np.concatenate([t_obs[mask], [tb]]))
            sol = solve_ivp(rhs, (t_now, tb), y, args=(p, n), method="RK45", rtol=1e-6, atol=1e-9, t_eval=te)
            ys = sol.y
            idx = np.searchsorted(te, t_obs[mask])
            out[:, mask] = free_drug_nm(ys[:n][:, idx], ys[3 * n:][:, idx], pc) * NG_ML_PER_NM
            y = ys[:, -1].copy()
            t_now = tb
    last = t_obs == t_now
    if last.any():
        out[:, last] = (free_drug_nm(y[:n][:, None], y[3 * n:][:, None], pc) * NG_ML_PER_NM)
    return out


def sample(inp: dict, n: int, rng: np.random.Generator) -> dict:
    t = inp["tmdd"]
    iiv = t["iiv_cv_pct"]

    def ln(cv):
        return np.exp(rng.normal(0, np.sqrt(np.log(1 + (cv / 100) ** 2)), n))

    female = rng.random(n) < inp["population"]["female_fraction"]
    high_tb = rng.random(n) < inp["population"]["high_tumor_burden_fraction_known"]
    pop = inp["population"]
    m, sd = pop["weight_mean_sd_kg"]
    s2 = np.log(1 + (sd / m) ** 2)
    wt = np.clip(np.exp(rng.normal(np.log(m) - s2 / 2, np.sqrt(s2), n)), *pop["weight_range_kg"])
    age = np.clip(rng.normal(*pop["age_mean_sd_y"], n), *pop["age_range_y"])
    p = {
        "CL": t["CL"] * np.where(female, 1 + t["sex_on_CL_female"], 1.0) * ln(iiv["CL"]),
        "Vc": t["Vc"] * (wt / t["wt_ref_kg"]) ** t["wt_on_Vc_power"] * ln(iiv["Vc"]), "Vp": t["Vp"] * ln(iiv["Vp"]), "Q": t["Q"] * ln(iiv["Q"]),
        "Vcs": t["Vcs"] * ln(iiv["Vcs"]), "CLs": t["CLs"] * ln(iiv["CLs"]),
        "CLx": t["CLx"] * ln(iiv["CLx"]), "Vcx": t["Vcx"] * ln(iiv["Vcx"]), "BL": t["BL"] * ln(iiv["BL"]),
        "ka": t["ka"] * (age / t["age_ref_y"]) ** t["age_on_ka_power"], "Kd": t["Kd"], "F": t["F"],
    }
    p["ksyn"] = p["CLs"] * p["BL"]
    p["female"], p["high_tb"] = female, high_tb
    return p


def typical(inp: dict, n: int = 1) -> dict:
    t = inp["tmdd"]
    p = {k: np.full(n, t[k]) for k in ("CL", "Vc", "Vp", "Q", "Vcs", "CLs", "CLx", "Vcx", "BL", "ka")}
    p.update(Kd=t["Kd"], F=t["F"])
    p["ksyn"] = p["CLs"] * p["BL"]
    return p
