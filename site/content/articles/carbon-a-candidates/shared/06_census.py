"""Decompose the Carbon-A candidate count: publication status, species redundancy, confidence, RefSeq agreement and gaps.

Run: python 06_census.py   (after 00-05; no network)
Writes results/census.json, results/species_redundancy.csv, results/low_yield_assemblies.csv and figures/carbon_a_census.png.
"""
from pathlib import Path
import json
import re
import sqlite3

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
SEED = 20261018
N_BOOT = 2000
REPORTED = dict(loci=566_000_000, assemblies=48_167, taxa=22_617)
CONF_CUTS = [0.1, 0.5, 0.9]
BIN_EDGES = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0001]
AVES = 8782  # NCBI taxid of class Aves
LOW_YIELD_VERTEBRATE = 3000  # predicted genes; vertebrates typically carry ~15,000-25,000 protein-coding genes
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9", "#999999"]


def load_taxonomy(db: Path) -> tuple[dict, dict]:
    con = sqlite3.connect(db)
    taxa = pd.read_sql("select taxid, parent_id, rank from taxa", con).set_index("taxid")
    return taxa["parent_id"].to_dict(), taxa["rank"].to_dict()


def lineage(t: int, parent: dict) -> list[int]:
    out, seen = [t], 0
    while t in parent and parent[t] != t and seen < 80:
        t, seen = parent[t], seen + 1
        out.append(t)
    return out


def species_of(t: int, parent: dict, rank: dict) -> int:
    for a in lineage(t, parent):
        if rank.get(a) == "species":
            return a
    return t


def accession_key(acc: str) -> tuple[int, int]:
    m = re.match(r"GCA_(\d+)\.(\d+)", acc)
    return int(m.group(1)), int(m.group(2))


def joint_bootstrap(genes: pd.DataFrame, totals: dict, rng: np.random.Generator) -> dict:
    """Fractions by division from the sample; totals = genes per division to scale. Resample assemblies in all strata at once."""
    per = {}
    for div, g in genes.groupby("division"):
        per[div] = g.groupby("accession").agg(n=("complete", "size"),
                                              **{f"c{c}": ("confidence", lambda s, c=c: int((s >= c).sum())) for c in CONF_CUTS})
    point = {c: sum(totals[d] * per[d][f"c{c}"].sum() / per[d]["n"].sum() for d in per) for c in CONF_CUTS}
    boots = {c: [] for c in CONF_CUTS}
    for _ in range(N_BOOT):
        tot = {c: 0.0 for c in CONF_CUTS}
        for d, p in per.items():
            b = p.iloc[rng.integers(0, len(p), len(p))]
            for c in CONF_CUTS:
                tot[c] += totals[d] * b[f"c{c}"].sum() / b["n"].sum()
        for c in CONF_CUTS:
            boots[c].append(tot[c])
    return {f"conf_ge_{c}": dict(genes=int(point[c]), lo=int(np.percentile(boots[c], 2.5)), hi=int(np.percentile(boots[c], 97.5)))
            for c in CONF_CUTS}


def main() -> None:
    rng = np.random.default_rng(SEED)
    heads = pd.read_csv(ROOT / "data" / "metadata_heads.csv")
    listing = pd.read_csv(ROOT / "data" / "cds_listing.csv")
    assert heads["accession"].is_unique
    out: dict = {"metadata_parsed": len(heads), "missing_gene_count": int(heads["gene_count"].isna().sum())}
    up = pd.to_datetime(listing["uploaded"], utc=True)
    out["upload_first_day"], out["upload_last_day"] = str(up.min().date()), str(up.max().date())
    out["upload_days_with_files"] = int(up.dt.date.nunique())
    heads = heads.dropna(subset=["gene_count", "taxid"]).copy()
    heads["gene_count"] = heads["gene_count"].astype(np.int64)
    heads["taxid"] = heads["taxid"].astype(np.int64)
    out["total_genes"] = int(heads["gene_count"].sum())
    out["share_of_reported_loci"] = out["total_genes"] / REPORTED["loci"]
    out["zero_gene_assemblies"] = int((heads["gene_count"] == 0).sum())
    out["by_division"] = heads.groupby("division").agg(assemblies=("accession", "size"), genes=("gene_count", "sum"),
                                                      median_genes=("gene_count", "median")).astype(int).to_dict("index")

    # Species redundancy under three selection rules (primary = latest accession, as in the analysis plan)
    parent, rank = load_taxonomy(ROOT / "data" / "explorer_taxonomy.sqlite")
    heads["species"] = heads["taxid"].map(lambda t: species_of(int(t), parent, rank))
    out["distinct_taxids"], out["distinct_species"] = int(heads["taxid"].nunique()), int(heads["species"].nunique())
    per_sp = heads.groupby("species").agg(assemblies=("accession", "size"), genes=("gene_count", "sum"),
                                          median_genes=("gene_count", "median"), max_genes=("gene_count", "max"))
    out["species_with_multiple_assemblies"] = int((per_sp["assemblies"] > 1).sum())
    heads["key"] = heads["accession"].map(accession_key)
    latest = heads.sort_values("key").groupby("species").tail(1)
    most_bases = heads.sort_values("annotated_bases").groupby("species").tail(1)
    h2 = heads.merge(per_sp["median_genes"], left_on="species", right_index=True)
    h2["dev"] = (h2["gene_count"] - h2["median_genes"]).abs()
    typical = h2.sort_values(["dev", "key"]).groupby("species").head(1)
    out["one_per_species"] = {"latest_accession": int(latest["gene_count"].sum()),
                              "most_annotated_bases": int(most_bases["gene_count"].sum()),
                              "closest_to_species_median": int(typical["gene_count"].sum())}
    human = heads[heads["species"] == 9606]
    out["human"] = dict(assemblies=len(human), genes=int(human["gene_count"].sum()), median=int(human["gene_count"].median()),
                        max=int(human["gene_count"].max()))
    per_sp.reset_index().to_csv(ROOT / "results" / "species_redundancy.csv", index=False)

    # Confidence: sample fractions scaled to all assemblies and to one-assembly-per-species (latest), joint stratified bootstrap
    sample = pd.read_csv(ROOT / "results" / "sample_assemblies.csv")
    genes = pd.read_csv(ROOT / "data" / "sample_genes.csv.gz")
    genes["complete"] = genes["status"] == "complete"
    out["sample_complete_fraction_by_division"] = genes.groupby("division")["complete"].mean().round(4).to_dict()
    out["sample_conf_fraction_by_division"] = {d: {c: float((g["confidence"] >= c).mean()) for c in CONF_CUTS}
                                               for d, g in genes.groupby("division")}
    tot_all = {d: v["genes"] for d, v in out["by_division"].items()}
    tot_one = latest.groupby("division")["gene_count"].sum().to_dict()
    out["extrapolated_all_assemblies"] = joint_bootstrap(genes, tot_all, rng)
    out["extrapolated_one_per_species_latest"] = joint_bootstrap(genes, tot_one, rng)
    out["sample_human_assemblies_in_mammal_sample"] = int((sample["taxid"] == 9606).sum())

    # Gaps: minimum processed record length, processed share of the genome, zero-gene assemblies (sample)
    stats = pd.read_csv(ROOT / "data" / "ncbi_assembly_stats.csv").drop_duplicates("accession")
    mins, recs = [], []
    for r in sample.itertuples():
        meta = json.loads((ROOT / "data" / "sample" / r.division / r.accession / "metadata.json").read_text(encoding="utf-8"))
        lens = [c["annotated_length_bp"] for c in meta["contigs"]]
        mins.append(min(lens) if lens else np.nan)
    sample["min_record_bp"] = mins
    s2 = sample.merge(stats[["accession", "total_sequence_length", "contig_n50"]].rename(columns={"contig_n50": "ncbi_contig_n50"}),
                      on="accession", how="left")
    s2["frac_genome_processed"] = s2["annotated_bases"] / s2["total_sequence_length"]
    out["sample_min_record_bp"] = dict(min=float(s2["min_record_bp"].min()), max=float(s2["min_record_bp"].max()),
                                       n_eq_8000=int((s2["min_record_bp"] == 8000).sum()), n=int(s2["min_record_bp"].notna().sum()))
    out["sample_frac_genome_processed"] = dict(median=float(s2["frac_genome_processed"].median()),
                                               n_lt_0_9=int((s2["frac_genome_processed"] < 0.9).sum()),
                                               n=int(s2["frac_genome_processed"].notna().sum()))
    z = s2[s2["genes"] == 0]
    out["sample_zero_gene"] = dict(n=len(z), frac_genome_processed=z["frac_genome_processed"].round(3).tolist(),
                                   processed_mb=(z["annotated_bases"] / 1e6).round(1).tolist(), organisms=z["organism"].tolist())

    # Low-yield vertebrate assemblies across all public files, with bird membership and accession era
    vert = heads[heads["division"].str.startswith("vertebrate")].copy()
    vert["is_bird"] = vert["taxid"].map(lambda t: AVES in lineage(int(t), parent))
    low = vert[vert["gene_count"] < LOW_YIELD_VERTEBRATE].copy()
    low["accession_number"] = low["key"].map(lambda k: k[0])
    out["low_yield_vertebrate"] = dict(threshold=LOW_YIELD_VERTEBRATE, n=len(low), of_vertebrate=len(vert),
                                       zero=int((low["gene_count"] == 0).sum()), birds=int(low["is_bird"].sum()),
                                       identical_refseq_pair=int((low["paired_assembly_comparison"] == "identical").sum()),
                                       identical_pair_birds=int(((low["paired_assembly_comparison"] == "identical") & low["is_bird"]).sum()))
    ip = low[(low["paired_assembly_comparison"] == "identical") & (low["gene_count"] > 0)]
    out["low_yield_identical_nonzero"] = dict(n=len(ip), birds=int(ip["is_bird"].sum()),
                                              accession_number_range=[int(ip["accession_number"].min()), int(ip["accession_number"].max())]
                                              if len(ip) else None)
    ipb = ip[ip["is_bird"]].merge(stats[["accession", "release_date", "submitter", "contig_n50"]], on="accession", how="left")
    out["low_yield_identical_birds"] = dict(n=len(ipb), release_first=str(ipb["release_date"].min()), release_last=str(ipb["release_date"].max()),
                                            submitters=ipb["submitter"].value_counts().to_dict(),
                                            median_ncbi_contig_n50=float(ipb["contig_n50"].median()),
                                            accession_first=ipb["accession"].min(), accession_last=ipb["accession"].max())
    low.drop(columns=["key"]).to_csv(ROOT / "results" / "low_yield_assemblies.csv", index=False)

    # RefSeq agreement: per assembly, and pooled by confidence bin with an assembly-bootstrap interval
    agree = pd.read_csv(ROOT / "results" / "refseq_agreement.csv")
    bins = pd.read_csv(ROOT / "results" / "refseq_by_confidence.csv")
    out["refseq_compared"] = int(agree["predicted"].notna().sum())
    for col in ["precision_overlap", "precision_exact_stop_tolerant", "recall_loci_overlap"]:
        out[f"refseq_{col}"] = dict(median=float(agree[col].median()), min=float(agree[col].min()), max=float(agree[col].max()))
    out["refseq_low_yield"] = agree.loc[agree["predicted"] < 0.2 * agree["refseq_coding_loci"], ["organism", "predicted", "refseq_coding_loci"]].to_dict("records")
    order = list(dict.fromkeys(bins["bin"]))
    piv = {k: bins.pivot_table(index="accession", columns="bin", values=k, aggfunc="sum")[order] for k in ("n", "exact_stop_tolerant", "overlap")}
    pooled = []
    accs = piv["n"].index.to_numpy()
    for b in order:
        n, e, o = piv["n"][b].sum(), piv["exact_stop_tolerant"][b].sum(), piv["overlap"][b].sum()
        bo = []
        for _ in range(N_BOOT):
            idx = rng.integers(0, len(accs), len(accs))
            nn = piv["n"][b].to_numpy()[idx].sum()
            bo.append(piv["exact_stop_tolerant"][b].to_numpy()[idx].sum() / nn if nn else np.nan)
        pooled.append(dict(bin=b, n=int(n), exact_rate=float(e / n), exact_lo=float(np.nanpercentile(bo, 2.5)),
                           exact_hi=float(np.nanpercentile(bo, 97.5)), overlap_rate=float(o / n)))
    out["refseq_by_confidence_pooled"] = pooled
    lt = [p for p in pooled if p["bin"] in order[:3]]
    out["refseq_exact_rate_conf_lt_0_5"] = sum(p["exact_rate"] * p["n"] for p in lt) / sum(p["n"] for p in lt)
    out["refseq_per_assembly"] = agree.to_dict("records")
    out["reported"] = REPORTED
    (ROOT / "results" / "census.json").write_text(json.dumps(out, indent=2, default=float), encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "refseq_per_assembly"}, indent=1, default=float))
    plot(out)


def plot(out: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6), constrained_layout=True)
    labels = ["All loci", "Confidence >= 0.5", "Confidence >= 0.9"]
    ea, eo = out["extrapolated_all_assemblies"], out["extrapolated_one_per_species_latest"]
    allv = [(out["total_genes"], None, None)] + [(ea[k]["genes"], ea[k]["lo"], ea[k]["hi"]) for k in ("conf_ge_0.5", "conf_ge_0.9")]
    onev = [(out["one_per_species"]["latest_accession"], None, None)] + [(eo[k]["genes"], eo[k]["lo"], eo[k]["hi"]) for k in ("conf_ge_0.5", "conf_ge_0.9")]
    xs = np.arange(3)
    for off, vals, color, lab in ((-0.2, allv, OKABE_ITO[0], f"all {out['metadata_parsed']:,} public assemblies"),
                                  (0.2, onev, OKABE_ITO[2], f"one assembly per species ({out['distinct_species']:,})")):
        h = [v[0] / 1e6 for v in vals]
        err = np.array([[0 if v[1] is None else (v[0] - v[1]) / 1e6 for v in vals], [0 if v[2] is None else (v[2] - v[0]) / 1e6 for v in vals]])
        ax[0].bar(xs + off, h, width=0.4, color=color, label=lab, yerr=err, capsize=3)
        for x_, v in zip(xs + off, h):
            ax[0].text(x_, v + 8, f"{v:.0f}M", ha="center", va="bottom", fontsize=8)
    ax[0].axhline(REPORTED["loci"] / 1e6, color=OKABE_ITO[6], lw=0.8, ls="--")
    ax[0].text(2.45, REPORTED["loci"] / 1e6 + 6, "announced 566M", fontsize=8, color="#555555", ha="right")
    ax[0].set_xticks(xs, labels, fontsize=9)
    ax[0].set(ylabel="Protein-coding loci (millions)", ylim=(0, 620), title="a. What the public predictions contain")
    ax[0].legend(fontsize=8, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.86))
    p = pd.DataFrame(out["refseq_by_confidence_pooled"])
    x = np.arange(len(p))
    ax[1].bar(x - 0.2, p["overlap_rate"], width=0.4, color=OKABE_ITO[5], label="overlaps a RefSeq CDS (same strand)")
    ax[1].bar(x + 0.2, p["exact_rate"], width=0.4, color=OKABE_ITO[0], label="same exon structure as a RefSeq transcript",
              yerr=[p["exact_rate"] - p["exact_lo"], p["exact_hi"] - p["exact_rate"]], capsize=3)
    for xi, n in zip(x, p["n"]):
        ax[1].text(xi, 1.02, f"n={n:,}", ha="center", fontsize=7, color="#555555")
    ax[1].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax[1].set_xticks(x, [b.replace("[", "").replace(")", "").replace(", ", "-") for b in p["bin"]], fontsize=8)
    ax[1].set(ylim=(0, 1.32), xlabel="Carbon-A confidence (complete gene models)", ylabel="Fraction of predictions",
              title=f"b. Agreement with RefSeq ({out['refseq_compared']} assemblies)")
    ax[1].legend(fontsize=8, frameon=False, loc="upper left")
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures" / "carbon_a_census.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
