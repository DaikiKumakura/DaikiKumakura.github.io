"""Spearman of log half-life with each of the 13 descriptors, on all 658 parent compounds and on TDC's train_val only (no test labels).

Run: python rules_all_descriptors.py   (needs the same data files as half_life_analysis.py; ~1 min)
Writes results/rules_all_descriptors.csv. Shows how the three features of the prior-sign regression compare with the others and
that selecting them from train_val alone gives the same choice as selecting from all compounds.
"""
import pandas as pd

import half_life_analysis as h


def main() -> None:
    log: dict = {}
    pool = h.load_pool("half_life_obach", log)
    tv, te = h.load_fixed(log)
    rows = []
    sets = {"all_658": (pool, None), "train_val_532": (tv, None), "fixed_test_135": (te, None)}
    for name, (df, _) in sets.items():
        d = pd.DataFrame(h.desc_matrix(list(df["mol"])), columns=h.DESC_NAMES)
        y = df["logy"].to_numpy()
        for c in h.DESC_NAMES:
            rows.append(dict(set=name, descriptor=c, n=len(df), spearman=h.rho(d[c].to_numpy(), y)))
    out = pd.DataFrame(rows)
    wide = out.pivot(index="descriptor", columns="set", values="spearman").loc[h.DESC_NAMES]
    wide["abs_train_val"] = wide["train_val_532"].abs()
    (h.ROOT / "results").mkdir(exist_ok=True)
    wide.drop(columns="abs_train_val").round(3).to_csv(h.ROOT / "results" / "rules_all_descriptors.csv")
    print(wide.sort_values("abs_train_val", ascending=False).round(3).to_string())


if __name__ == "__main__":
    main()
