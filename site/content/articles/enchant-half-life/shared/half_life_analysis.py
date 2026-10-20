"""What does a Spearman of 0.74 for human half-life measure? Public TDC data (Obach half-life, Lombardo Vss).

Run: python half_life_analysis.py   (needs data/half_life_obach.tab, data/vdss_lombardo.tab, data/tdc_admet_half_life/{train_val,test}.csv; ~20 min)
Writes results/summary.json, results/*.csv and figures/half_life_analysis.png.
No Enchant predictions are used or available; the baselines are plain scikit-learn models and simple rules.
"""
from pathlib import Path
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from rdkit import Chem, DataStructs, RDLogger
from rdkit.Chem import AllChem, Descriptors, Lipinski, rdMolDescriptors
from rdkit.Chem.MolStandardize import rdMolStandardize
from rdkit.Chem.Scaffolds import MurckoScaffold
from scipy.optimize import nnls
from scipy.stats import spearmanr
from sklearn.ensemble import RandomForestRegressor

RDLogger.DisableLog("rdApp.*")
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
SEED = 20261020
N_SPLIT_SEEDS = 30  # re-splits of the 658 parent compounds (random and TDC-style scaffold)
N_DECOMP_SEEDS = 10
KNN_K = 5
RF_TREES = 300
TRAIN_SIZES = [5, 10, 20, 50, 100, 200]
N_DRAWS = 100
N_BOOT = 2000
FRAC = (0.7, 0.1, 0.2)  # TDC scaffold split fractions (train, validation, test); validation is merged into training here
CLAIM, PREV_BEST = 0.74, 0.58
TDC_TOP = 0.576  # TDC leaderboard first place on 2026-05-28 (benchmarklist.com snapshot)
MODEL_RHO = (0.3, 0.5, 0.7, 0.9)  # assumed rank correlation between the two models' predictions
N_TEST_TDC, N_ALL = 135, 667
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9", "#999999"]
SMARTS = {
    "acid": ["[CX3](=O)[OX2H1,OX1-]", "c1nn[nH]n1", "[SX4](=O)(=O)[NH]C(=O)", "[SX4](=O)(=O)[OH]"],
    "base": ["[NX3;H2,H1,H0;!$(NC=[O,S,N]);!$(N-[SX4]);!$(N-a);!$(N-[#7,#8]);!$(N#*);!$(N=*);!$(N-C=C)]",
             "[NX3][CX3]=[NX2,NX3+]", "c1ncc[nH]1"],
}
PATTERNS = {k: [Chem.MolFromSmarts(s) for s in v] for k, v in SMARTS.items()}
DESC_NAMES = ["logP", "TPSA", "MW", "HBD", "HBA", "RotB", "Rings", "AromRings", "Fsp3", "HeavyAtoms", "Charge", "nAcid", "nBase"]
RULE_NAMES = ["logP", "TPSA", "MW", "HBD", "Fsp3", "nBase", "nAcid", "Charge"]  # all eight tried; reported together


def largest_fragment(smiles: str) -> Chem.Mol:
    return rdMolStandardize.LargestFragmentChooser().choose(Chem.MolFromSmiles(smiles))


def descriptors(mol: Chem.Mol) -> list[float]:
    n_acid = sum(len(mol.GetSubstructMatches(p)) for p in PATTERNS["acid"])
    n_base = sum(len(mol.GetSubstructMatches(p)) for p in PATTERNS["base"])
    return [Descriptors.MolLogP(mol), rdMolDescriptors.CalcTPSA(mol), Descriptors.MolWt(mol), Lipinski.NumHDonors(mol),
            Lipinski.NumHAcceptors(mol), Lipinski.NumRotatableBonds(mol), rdMolDescriptors.CalcNumRings(mol),
            rdMolDescriptors.CalcNumAromaticRings(mol), rdMolDescriptors.CalcFractionCSP3(mol), mol.GetNumHeavyAtoms(),
            Chem.GetFormalCharge(mol), n_acid, n_base]


def ionisation_class(n_acid: float, n_base: float) -> str:
    return {(True, True): "zwitterion", (True, False): "acid", (False, True): "base", (False, False): "neutral"}[(n_acid > 0, n_base > 0)]


def parent_key(mol: Chem.Mol) -> str:
    return Chem.inchi.MolToInchiKey(mol)[:14]


def load_pool(name: str, log: dict) -> pd.DataFrame:
    """One row per parent compound (stereoisomers and salts merged, median log10 value)."""
    df = pd.read_csv(DATA / f"{name}.tab")
    assert {"ID", "X", "Y"} <= set(df.columns) and (df["Y"] > 0).all()
    mols = df["X"].map(largest_fragment)
    df["key"] = mols.map(parent_key)
    df["logy"] = np.log10(df["Y"])
    dup = df[df["key"].duplicated(keep=False)].groupby("key")["logy"].agg(["min", "max", "size"])
    log[f"{name}_rows"] = len(df)
    log[f"{name}_duplicate_parent_groups"] = int(len(dup))
    if name == "half_life_obach":
        log["duplicate_log10_halflife_range_median"] = float((dup["max"] - dup["min"]).median())
        log["duplicate_log10_halflife_range_max"] = float((dup["max"] - dup["min"]).max())
    out = df.groupby("key").agg(smiles=("X", "first"), logy=("logy", "median")).reset_index()
    out["mol"] = out["smiles"].map(largest_fragment)
    log[f"{name}_parent_compounds"] = len(out)
    return out


def load_fixed(log: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """TDC ADMET-group Half_Life_Obach: the fixed test set used by the leaderboard, and train_val."""
    out = []
    for f in ("train_val", "test"):
        df = pd.read_csv(DATA / "tdc_admet_half_life" / f"{f}.csv")
        assert {"Drug_ID", "Drug", "Y"} <= set(df.columns) and (df["Y"] > 0).all()
        df["mol"] = df["Drug"].map(largest_fragment)
        df["key"] = df["mol"].map(parent_key)
        df["logy"] = np.log10(df["Y"])
        out.append(df.reset_index(drop=True))
    tv, te = out
    log["tdc_train_val"], log["tdc_test"] = len(tv), len(te)
    log["tdc_test_parent_in_train_val"] = int(te["key"].isin(set(tv["key"])).sum())
    return tv, te


def fingerprints(mols: list[Chem.Mol]) -> list:
    gen = AllChem.GetMorganGenerator(radius=2, fpSize=2048)
    return [gen.GetFingerprint(m) for m in mols]


def desc_matrix(mols: list[Chem.Mol]) -> np.ndarray:
    return np.array([descriptors(m) for m in mols], dtype=float)


def scaffold_groups(mols: list[Chem.Mol]) -> list[list[int]]:
    groups: dict[str, list[int]] = {}
    for i, m in enumerate(mols):
        groups.setdefault(MurckoScaffold.MurckoScaffoldSmiles(mol=m, includeChirality=False), []).append(i)
    return list(groups.values())


def tdc_scaffold_split(groups: list[list[int]], n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """TDC-style: groups larger than half of the validation or test size go first (shuffled), then the rest (shuffled);
    train, then validation, then test are filled in order. Validation is merged into training. Own implementation, not TDC's code."""
    train_n, val_n, test_n = (f * n for f in FRAC)
    big = [g for g in groups if len(g) > val_n / 2 or len(g) > test_n / 2]
    small = [g for g in groups if g not in big]
    order = [big[i] for i in rng.permutation(len(big))] + [small[i] for i in rng.permutation(len(small))]
    train, val, test = [], [], []
    for g in order:
        if len(train) + len(g) <= train_n:
            train += g
        elif len(val) + len(g) <= val_n:
            val += g
        else:
            test += g
    return np.array(sorted(train + val)), np.array(sorted(test))


def random_split(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    idx = rng.permutation(n)
    n_test = int(round(FRAC[2] * n))
    return np.sort(idx[n_test:]), np.sort(idx[:n_test])


def knn_predict(fps: list, y: np.ndarray, train: np.ndarray, test: np.ndarray, test_fps: list | None = None) -> tuple[np.ndarray, np.ndarray]:
    train_fps = [fps[i] for i in train]
    query = test_fps if test_fps is not None else [fps[i] for i in test]
    pred, nearest = [], []
    for q in query:
        sims = np.array(DataStructs.BulkTanimotoSimilarity(q, train_fps))
        top = np.argsort(-sims)[: min(KNN_K, len(train))]
        w = sims[top] + 1e-6
        pred.append(float(np.sum(w * y[train][top]) / np.sum(w)))
        nearest.append(float(sims.max()))
    return np.array(pred), np.array(nearest)


def rf_predict(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray, seed: int) -> np.ndarray:
    return RandomForestRegressor(n_estimators=RF_TREES, random_state=seed, n_jobs=1).fit(x_train, y_train).predict(x_test)


class PriorRidge:
    """Few-shot baseline with prior knowledge of signs only: log half-life rises with logP and basicity and falls with acidity.
    Magnitudes are learned from the training drugs by non-negative least squares on sign-flipped, standardised features."""

    SIGNS = np.array([1.0, -1.0, 1.0])

    def __init__(self, ref_desc: np.ndarray):
        f = self._features(ref_desc)
        self.mu, self.sd = f.mean(0), f.std(0) + 1e-9  # feature scaling from unlabeled drugs only

    @staticmethod
    def _features(d: np.ndarray) -> np.ndarray:
        return np.column_stack([d[:, 0], (d[:, 11] > 0).astype(float), (d[:, 12] > 0).astype(float)])

    def _z(self, d: np.ndarray) -> np.ndarray:
        return (self._features(d) - self.mu) / self.sd * self.SIGNS

    def fit_predict(self, d_train: np.ndarray, y_train: np.ndarray, d_test: np.ndarray) -> np.ndarray:
        zt = self._z(d_train)
        m, ym = zt.mean(0), y_train.mean()
        coef, _ = nnls(zt - m, y_train - ym)
        return (self._z(d_test) - m) @ coef + ym


def rho(a: np.ndarray, b: np.ndarray) -> float:
    """Spearman; 0.0 when one input is constant (no ranking information)."""
    if np.ptp(a) == 0 or np.ptp(b) == 0:
        return 0.0
    return float(spearmanr(a, b).statistic)


def bonett_wright(r: float, n: int) -> tuple[float, float]:
    se = np.sqrt((1 + r ** 2 / 2) / (n - 3))
    return float(np.tanh(np.arctanh(r) - 1.96 * se)), float(np.tanh(np.arctanh(r) + 1.96 * se))


def zou_difference(r1: float, r2: float, r12: float, n: int) -> tuple[float, float]:
    """Zou (2007) interval for the difference of two dependent correlations sharing the outcome (Pearson-based, applied to Spearman)."""
    assert np.linalg.det(np.array([[1, r1, r2], [r1, 1, r12], [r2, r12, 1]])) > 0, "inconsistent correlations"
    l1, u1 = bonett_wright(r1, n)
    l2, u2 = bonett_wright(r2, n)
    c = ((r12 - 0.5 * r1 * r2) * (1 - r1 ** 2 - r2 ** 2 - r12 ** 2) + r12 ** 3) / ((1 - r1 ** 2) * (1 - r2 ** 2))
    lo = r1 - r2 - np.sqrt((r1 - l1) ** 2 + (u2 - r2) ** 2 - 2 * c * (r1 - l1) * (u2 - r2))
    hi = r1 - r2 + np.sqrt((u1 - r1) ** 2 + (r2 - l2) ** 2 - 2 * c * (u1 - r1) * (r2 - l2))
    return float(lo), float(hi)


def boot_ci(pred: np.ndarray, y: np.ndarray, rng: np.random.Generator) -> tuple[float, float]:
    vals = [rho(pred[i], y[i]) for i in (rng.integers(0, len(y), len(y)) for _ in range(N_BOOT))]
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def main() -> None:
    log: dict = {}
    hl, vs = load_pool("half_life_obach", log), load_pool("vdss_lombardo", log)
    tv, te = load_fixed(log)
    y_all = hl["logy"].to_numpy()
    n_all = len(hl)
    fps_all, desc_all = fingerprints(list(hl["mol"])), desc_matrix(list(hl["mol"]))
    groups = scaffold_groups(list(hl["mol"]))
    log["scaffold_groups"] = len(groups)
    log["largest_scaffold_group"] = int(max(len(g) for g in groups))
    log["singleton_scaffold_groups"] = int(sum(len(g) == 1 for g in groups))
    print(json.dumps(log, indent=1), flush=True)

    # A. Precision and the difference between 0.74 and 0.58
    precision = {f"rho_{r}": {f"n_{m}": bonett_wright(r, m) for m in (N_TEST_TDC, N_ALL)} for r in (CLAIM, PREV_BEST)}
    zou = [dict(n=m, assumed_model_rank_corr=r12, lo=zou_difference(CLAIM, PREV_BEST, r12, m)[0], hi=zou_difference(CLAIM, PREV_BEST, r12, m)[1])
           for m in (N_TEST_TDC, N_ALL) for r12 in MODEL_RHO]

    # B. Plain baselines on the fixed TDC test set
    fps_tv, fps_te = fingerprints(list(tv["mol"])), fingerprints(list(te["mol"]))
    d_tv, d_te = desc_matrix(list(tv["mol"])), desc_matrix(list(te["mol"]))
    y_tv, y_te = tv["logy"].to_numpy(), te["logy"].to_numpy()
    rng = np.random.default_rng([SEED, 0])
    p_knn, nearest_te = knn_predict(fps_tv, y_tv, np.arange(len(tv)), np.arange(len(te)), fps_te)
    p_rf = np.mean([rf_predict(d_tv, y_tv, d_te, SEED + s) for s in range(5)], axis=0)
    rf_seed_values = [rho(rf_predict(d_tv, y_tv, d_te, SEED + s), y_te) for s in range(5)]
    cls_tv = pd.Series([ionisation_class(a, b) for a, b in zip(d_tv[:, 11], d_tv[:, 12])])
    med = pd.Series(y_tv).groupby(cls_tv.to_numpy()).median()
    cls_te = [ionisation_class(a, b) for a, b in zip(d_te[:, 11], d_te[:, 12])]
    p_cls = np.array([med[c] for c in cls_te])
    fixed = {
        "kNN (Morgan)": dict(spearman=rho(p_knn, y_te), ci=boot_ci(p_knn, y_te, rng)),
        "RF (descriptors)": dict(spearman=rho(p_rf, y_te), ci=boot_ci(p_rf, y_te, rng), seed_values=rf_seed_values),
        "rule: logP": dict(spearman=rho(d_te[:, 0], y_te), ci=boot_ci(d_te[:, 0], y_te, rng)),
        "rule: acid groups (negative sign)": dict(spearman=rho(-d_te[:, 11], y_te), ci=boot_ci(-d_te[:, 11], y_te, rng)),
        "rule: ionisation-class median (train_val medians)": dict(spearman=rho(p_cls, y_te), ci=boot_ci(p_cls, y_te, rng)),
    }
    diff_vals = [rho(p_rf[i], y_te[i]) - rho(p_knn[i], y_te[i]) for i in (rng.integers(0, len(y_te), len(y_te)) for _ in range(N_BOOT))]
    fixed_diff_rf_knn = dict(mean=float(np.mean(diff_vals)), lo=float(np.percentile(diff_vals, 2.5)), hi=float(np.percentile(diff_vals, 97.5)))
    fixed_context = dict(nearest_similarity_median=float(np.median(nearest_te)), nearest_similarity_p10=float(np.percentile(nearest_te, 10)),
                         nearest_similarity_p90=float(np.percentile(nearest_te, 90)), test_parent_in_train_val=log["tdc_test_parent_in_train_val"],
                         frac_nearest_ge_0_6=float(np.mean(nearest_te >= 0.6)), class_median_half_life_h=(10 ** med).round(2).to_dict())
    print("fixed", json.dumps(fixed, default=float), flush=True)

    # C. Split design: 30 re-splits, random vs TDC-style scaffold
    rows, nn_rows = [], []
    largest = set(max(groups, key=len))
    n_big_in_test = 0
    for i in range(N_SPLIT_SEEDS):
        r_split = np.random.default_rng([SEED, 1, i])
        rf_seed = int(np.random.default_rng([SEED, 2, i]).integers(1, 2 ** 31 - 1))
        for split_name, (tr, tt) in (("random", random_split(n_all, r_split)), ("scaffold", tdc_scaffold_split(groups, n_all, r_split))):
            n_big_in_test += int(split_name == "scaffold" and largest <= set(tt.tolist()))
            pk, nearest = knn_predict(fps_all, y_all, tr, tt)
            pr = rf_predict(desc_all[tr], y_all[tr], desc_all[tt], rf_seed)
            pl = desc_all[tt, 0]
            rows += [dict(seed=i, split=split_name, model="kNN (Morgan)", n_test=len(tt), spearman=rho(pk, y_all[tt])),
                     dict(seed=i, split=split_name, model="RF (descriptors)", n_test=len(tt), spearman=rho(pr, y_all[tt])),
                     dict(seed=i, split=split_name, model="rule: logP", n_test=len(tt), spearman=rho(pl, y_all[tt]))]
            nn_rows += [dict(seed=i, split=split_name, nearest_similarity=s) for s in nearest]
    res, nn = pd.DataFrame(rows), pd.DataFrame(nn_rows)
    split_summary = res.groupby(["split", "model"])["spearman"].agg(["mean", "std", "min", "max",
                                                                       lambda s: s.quantile(0.1), lambda s: s.quantile(0.9)]).reset_index()
    split_summary.columns = ["split", "model", "mean", "std", "min", "max", "p10", "p90"]
    wide = res.pivot_table(index=["seed", "model"], columns="split", values="spearman").reset_index()
    wide["random_minus_scaffold"] = wide["random"] - wide["scaffold"]
    gap = {m: dict(mean=float(g["random_minus_scaffold"].mean()),
                   lo=float(np.percentile([g["random_minus_scaffold"].sample(len(g), replace=True, random_state=b).mean() for b in range(N_BOOT)], 2.5)),
                   hi=float(np.percentile([g["random_minus_scaffold"].sample(len(g), replace=True, random_state=b).mean() for b in range(N_BOOT)], 97.5)))
           for m, g in wide.groupby("model")}
    nn_summary = nn.groupby("split")["nearest_similarity"].describe(percentiles=[0.1, 0.5, 0.9]).reset_index()
    big_in_test = int(n_big_in_test)
    print("split done", flush=True)

    # D. Training-size curve on the fixed TDC test set
    curve = []
    rng_c = np.random.default_rng([SEED, 3])
    prior = PriorRidge(d_tv)
    for size in TRAIN_SIZES + [len(tv)]:
        for d in range(N_DRAWS if size < len(tv) else 1):
            sub = rng_c.choice(len(tv), size=size, replace=False) if size < len(tv) else np.arange(len(tv))
            pk, _ = knn_predict(fps_tv, y_tv, sub, np.arange(len(te)), fps_te)
            pr = rf_predict(d_tv[sub], y_tv[sub], d_te, SEED + d)
            pp = prior.fit_predict(d_tv[sub], y_tv[sub], d_te)
            curve += [dict(size=size, draw=d, model="kNN (Morgan)", spearman=rho(pk, y_te)),
                      dict(size=size, draw=d, model="RF (descriptors)", spearman=rho(pr, y_te)),
                      dict(size=size, draw=d, model="sign-constrained regression (prior signs)", spearman=rho(pp, y_te))]
        print("size", size, flush=True)
    cur = pd.DataFrame(curve)
    curve_summary = cur.groupby(["model", "size"])["spearman"].agg(["mean", "std", "min", "max", lambda s: s.quantile(0.1), lambda s: s.quantile(0.9)]).reset_index()
    curve_summary.columns = ["model", "size", "mean", "std", "min", "max", "p10", "p90"]
    rule_level = fixed["rule: logP"]["spearman"]
    frac_above_rule = {f"{m}_{s}": float((cur[(cur.model == m) & (cur["size"] == s)]["spearman"] >= rule_level).mean())
                       for m in cur.model.unique() for s in (5, 20)}

    # E. Rules over all parent compounds (eight tried; none fitted except the class medians)
    d = pd.DataFrame(desc_all, columns=DESC_NAMES)
    all_rules = {c: dict(spearman=rho(d[c].to_numpy(), y_all), p=float(spearmanr(d[c], y_all).pvalue)) for c in RULE_NAMES}
    d["class"] = [ionisation_class(a, b) for a, b in zip(d["nAcid"], d["nBase"])]
    cls = d.assign(logy=y_all).groupby("class")["logy"].agg(["size", "median"]).reset_index()
    cls["median_half_life_h"] = 10 ** cls["median"]

    # F. Volume versus clearance (identity; derived CL assumes Vz = Vss)
    both = hl.merge(vs[["key", "logy"]], on="key", suffixes=("_hl", "_vss"))
    both["log_cl"] = np.log10(np.log(2)) + both["logy_vss"] - both["logy_hl"]
    var_hl, var_v, var_cl = (float(both[c].var(ddof=1)) for c in ("logy_hl", "logy_vss", "log_cl"))
    cov_v_cl = float(np.cov(both["logy_vss"], both["log_cl"])[0, 1])
    deco = dict(n=len(both), var_log_half_life=var_hl, var_log_vss=var_v, var_log_cl=var_cl, cov_log_vss_log_cl=cov_v_cl,
                pearson_log_vss_log_cl=float(np.corrcoef(both["logy_vss"], both["log_cl"])[0, 1]),
                share_logV=float(np.cov(both["logy_hl"], both["logy_vss"])[0, 1] / var_hl),
                share_logCL=float(-np.cov(both["logy_hl"], both["log_cl"])[0, 1] / var_hl),
                spearman_half_life_vss=rho(both["logy_hl"].to_numpy(), both["logy_vss"].to_numpy()),
                spearman_half_life_cl=rho(both["logy_hl"].to_numpy(), both["log_cl"].to_numpy()))
    assert abs(deco["share_logV"] + deco["share_logCL"] - 1) < 1e-9 and abs(var_hl - (var_v + var_cl - 2 * cov_v_cl)) < 1e-9
    desc_b, groups_b = desc_matrix(list(both["mol"])), scaffold_groups(list(both["mol"]))
    comp = []
    for i in range(N_DECOMP_SEEDS):
        tr, tt = tdc_scaffold_split(groups_b, len(both), np.random.default_rng([SEED, 4, i]))
        for name, col in (("half-life", "logy_hl"), ("Vss (measured)", "logy_vss"), ("CL (derived from Vss and half-life)", "log_cl")):
            yy = both[col].to_numpy()
            comp.append(dict(seed=i, target=name, spearman=rho(rf_predict(desc_b[tr], yy[tr], desc_b[tt], SEED + i), yy[tt])))
    comp = pd.DataFrame(comp)
    comp_summary = comp.groupby("target")["spearman"].agg(["mean", "std"]).reset_index()

    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    res.to_csv(out / "split_baselines.csv", index=False)
    cur.to_csv(out / "learning_curve.csv", index=False)
    nn.to_csv(out / "nearest_similarity.csv", index=False)
    comp.to_csv(out / "component_predictability.csv", index=False)
    summary = dict(counts=log, precision=precision, zou_difference=zou, fixed_tdc_test=fixed, fixed_rf_minus_knn=fixed_diff_rf_knn,
                   fixed_context=fixed_context, split_summary=split_summary.to_dict("records"), random_minus_scaffold=gap,
                   nearest_similarity=nn_summary.to_dict("records"), scaffold_splits_with_largest_group_in_test=big_in_test,
                   curve_summary=curve_summary.to_dict("records"), frac_draws_at_or_above_logP_rule_fixed_test=frac_above_rule,
                   all_compound_rules=all_rules, ionisation_class_table=cls.to_dict("records"), decomposition=deco,
                   component_summary=comp_summary.to_dict("records"),
                   parameters=dict(seed=SEED, split_seeds=N_SPLIT_SEEDS, decomposition_seeds=N_DECOMP_SEEDS, draws=N_DRAWS, knn_k=KNN_K,
                                   rf_trees=RF_TREES, frac=FRAC))
    (out / "summary.json").write_text(json.dumps(summary, indent=2, default=float), encoding="utf-8")
    plot(summary, res, cur, fixed, comp_summary, deco)
    print(json.dumps({k: summary[k] for k in summary if k != "counts"}, indent=1, default=float))


def plot(s: dict, res: pd.DataFrame, cur: pd.DataFrame, fixed: dict, comp: pd.DataFrame, deco: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(11, 8.8), constrained_layout=True)
    ax = ax.ravel()
    ns = np.array([20, 40, 80, 135, 250, 667])
    for r, color in ((CLAIM, OKABE_ITO[0]), (PREV_BEST, OKABE_ITO[1])):
        ci = np.array([bonett_wright(r, int(m)) for m in ns])
        ax[0].fill_between(ns, ci[:, 0], ci[:, 1], color=color, alpha=0.25)
        ax[0].plot(ns, [r] * len(ns), color=color, label=f"Spearman {r}")
    ax[0].axvline(N_TEST_TDC, color=OKABE_ITO[6], lw=0.8, ls="--")
    ax[0].text(140, 0.93, "TDC test set (135)", fontsize=8, color="#555555")
    ax[0].set(xscale="log", xticks=ns, xticklabels=[str(v) for v in ns], ylim=(0.1, 0.95), xlabel="Number of test drugs",
              ylabel="Spearman (95% interval)", title="a. Precision of 0.74 and 0.58")
    ax[0].legend(fontsize=8, frameon=False, loc="lower right")
    pos = {("random", "kNN (Morgan)"): 0, ("scaffold", "kNN (Morgan)"): 1, ("random", "RF (descriptors)"): 3, ("scaffold", "RF (descriptors)"): 4,
           ("random", "rule: logP"): 6, ("scaffold", "rule: logP"): 7}
    rng = np.random.default_rng(1)
    for (sp, m), x in pos.items():
        g = res[(res.split == sp) & (res.model == m)]["spearman"].to_numpy()
        ax[1].scatter(x + rng.uniform(-0.2, 0.2, len(g)), g, color=OKABE_ITO[0] if sp == "random" else OKABE_ITO[4], s=14, alpha=0.7)
        ax[1].plot([x - 0.3, x + 0.3], [g.mean()] * 2, color="#333333", lw=1.5)
    for m, x in (("kNN (Morgan)", 1), ("RF (descriptors)", 4), ("rule: logP", 7)):
        key = {"kNN (Morgan)": "kNN (Morgan)", "RF (descriptors)": "RF (descriptors)", "rule: logP": "rule: logP"}[m]
        ax[1].scatter([x + 0.45], [fixed[key]["spearman"]], marker="D", color="#000000", s=34, zorder=5)
    ax[1].axhline(PREV_BEST, color=OKABE_ITO[6], lw=0.8, ls="--")
    ax[1].set_xticks([0, 1, 3, 4, 6, 7], ["kNN\nrandom", "kNN\nscaffold", "RF\nrandom", "RF\nscaffold", "logP\nrandom", "logP\nscaffold"], fontsize=8)
    ax[1].set(ylabel="Test Spearman (30 re-splits)", ylim=(-0.05, 0.8), title="b. Same models, 30 splits (diamond: fixed TDC test set)")
    colors = {"kNN (Morgan)": OKABE_ITO[2], "RF (descriptors)": OKABE_ITO[3], "sign-constrained regression (prior signs)": OKABE_ITO[4]}
    for m, color in colors.items():
        g = cur[cur.model == m].groupby("size")["spearman"].agg(["mean", "std"]).reset_index()
        ax[2].errorbar(g["size"], g["mean"], yerr=g["std"], color=color, marker="o", ms=4, capsize=3, label=m.replace(" (prior signs)", ""))
    ax[2].axhline(fixed["rule: logP"]["spearman"], color=OKABE_ITO[0], lw=1, ls=":")
    ax[2].text(60, fixed["rule: logP"]["spearman"] - 0.045, "logP rule (no training)", fontsize=8, color=OKABE_ITO[0])
    ax[2].axhline(PREV_BEST, color=OKABE_ITO[6], lw=0.8, ls="--")
    ax[2].set(xscale="log", xlabel="Number of training drugs", ylabel="Test Spearman, fixed TDC test set (mean +/- SD)", ylim=(-0.25, 0.8),
              title="c. Few training drugs vs a no-training rule")
    ax[2].legend(fontsize=7, frameon=False, loc="lower right")
    names = ["half-life", "Vss (measured)", "CL (derived from Vss and half-life)"]
    c = comp.set_index("target").loc[names]
    ax[3].bar(range(3), c["mean"], yerr=c["std"], color=[OKABE_ITO[0], OKABE_ITO[2], OKABE_ITO[4]], capsize=3)
    ax[3].set_xticks(range(3), ["half-life", "Vss\n(measured)", "CL\n(derived)"], fontsize=9)
    ax[3].set(ylabel="Scaffold-split Spearman, RF (10 re-splits)", ylim=(0, 0.8),
              title=f"d. n = {deco['n']}: var(log t1/2) = var(log V) + var(log CL) - 2cov")
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures" / "half_life_analysis.png", dpi=160)
    plt.close(fig)


def replot() -> None:
    """Redraw the figure from saved results without refitting."""
    out = json.loads((ROOT / "results" / "summary.json").read_text(encoding="utf-8"))
    comp = pd.read_csv(ROOT / "results" / "component_predictability.csv").groupby("target")["spearman"].agg(["mean", "std"]).reset_index()
    plot(out, pd.read_csv(ROOT / "results" / "split_baselines.csv"), pd.read_csv(ROOT / "results" / "learning_curve.csv"),
         out["fixed_tdc_test"], comp, out["decomposition"])


if __name__ == "__main__":
    import sys

    replot() if "--replot" in sys.argv else main()
