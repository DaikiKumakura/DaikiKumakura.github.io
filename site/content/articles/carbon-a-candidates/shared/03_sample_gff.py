"""Download a stratified random sample of Carbon-A per-assembly predictions and summarise gene-model status.

Run: python 03_sample_gff.py   (network on first run; files cached under data/sample/)
Writes results/sample_assemblies.csv (one row per assembly) and data/sample_genes.csv.gz (one row per gene).
"""
from pathlib import Path
import csv
import gzip
import json
import re
import urllib.request

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
BASE = "https://huggingface.co/buckets/HuggingFaceBio/genbank-annotations/resolve/cds"
SEED = 20261018
PER_DIVISION = 20
EDGE_BP = 1000  # gene within this distance of a contig end
SAMPLE = ROOT / "data" / "sample"


def download(url: str, dest: Path) -> Path:
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".part")
        urllib.request.urlretrieve(url, tmp)
        tmp.replace(dest)
    return dest


def parse_gff(path: Path) -> pd.DataFrame:
    genes, cds_len, n_cds = {}, {}, {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 9:
                continue
            attrs = dict(kv.split("=", 1) for kv in f[8].split(";") if "=" in kv)
            if f[2] == "gene":
                genes[attrs["ID"]] = dict(gene_id=attrs["ID"], contig=f[0], start=int(f[3]), end=int(f[4]), strand=f[6],
                                          status=attrs.get("status"), reason=attrs.get("incomplete_reason", ""),
                                          confidence=float(attrs["confidence"]) if attrs.get("confidence", "NA") != "NA" else np.nan)
            elif f[2] == "CDS":
                tx = attrs["Parent"]
                gid = re.sub(r"_transcript(\d+)$", r"_gene\1", tx)
                cds_len[gid] = cds_len.get(gid, 0) + int(f[4]) - int(f[3]) + 1
                n_cds[gid] = n_cds.get(gid, 0) + 1
    cols = ["gene_id", "contig", "start", "end", "strand", "status", "reason", "confidence"]
    df = pd.DataFrame(list(genes.values()), columns=cols)  # empty GFF -> zero genes
    df["cds_len"] = df["gene_id"].map(cds_len)
    df["n_exons"] = df["gene_id"].map(n_cds)
    return df


def main() -> None:
    heads = pd.read_csv(ROOT / "data" / "cds_assemblies.csv").dropna(subset=["annotations_gff3_gz"])
    rng = np.random.default_rng(SEED)
    picks = []
    for div, g in heads.groupby("division", sort=True):
        idx = rng.choice(len(g), size=PER_DIVISION, replace=False)
        picks.append(g.iloc[np.sort(idx)])
    sample = pd.concat(picks)
    print("sample", len(sample), "gff MB", round(sample.annotations_gff3_gz.sum() / 1e6, 1),
          "metadata MB", round(sample.metadata_json.sum() / 1e6, 1))
    rows, gene_rows = [], []
    for r in sample.itertuples():
        d = SAMPLE / r.division / r.accession
        meta = json.loads(download(f"{BASE}/{r.division}/{r.accession}/metadata.json", d / "metadata.json").read_text(encoding="utf-8"))
        gff = download(f"{BASE}/{r.division}/{r.accession}/annotations.gff3.gz", d / "annotations.gff3.gz")
        g = parse_gff(gff)
        clen = {c["accession"]: c["annotated_length_bp"] for c in meta["contigs"]}
        g["contig_len"] = g["contig"].map(clen)
        g["near_edge"] = (g["start"] <= EDGE_BP) | (g["contig_len"] - g["end"] < EDGE_BP)
        assert len(g) == meta["gene_count"], (r.accession, len(g), meta["gene_count"])
        n_contigs = len(clen)
        bases = meta["annotated_bases"]
        lens = np.sort(np.array(list(clen.values()), dtype=np.int64))[::-1]  # int64: Windows default int32 overflows
        n50 = int(lens[np.searchsorted(np.cumsum(lens), lens.sum() / 2)]) if len(lens) else 0  # over listed contigs
        comp = g["status"] == "complete"
        if len(g) == 0:
            print("zero genes", r.accession)
        rows.append(dict(division=r.division, accession=r.accession, organism=meta["organism_name"], taxid=meta["taxid"],
                         paired_refseq=meta["paired_refseq_accession"], paired_comparison=meta["paired_assembly_comparison"],
                         annotated_bases=bases, contig_bases=int(lens.sum()), n_contigs=n_contigs, contig_n50=n50, genes=len(g),
                         frac_complete=comp.mean(), frac_near_edge=g["near_edge"].mean(),
                         frac_incomplete_near_edge=g.loc[~comp, "near_edge"].mean() if (~comp).any() else np.nan,
                         median_conf_complete=g.loc[comp, "confidence"].median(),
                         frac_conf_ge_0_5=(comp & (g["confidence"] >= 0.5)).mean(),
                         frac_conf_ge_0_1=(comp & (g["confidence"] >= 0.1)).mean(),
                         median_cds_len=g["cds_len"].median()))
        g["division"], g["accession"] = r.division, r.accession
        gene_rows.append(g[["division", "accession", "status", "reason", "confidence", "cds_len", "n_exons", "near_edge"]])
        print(r.division, r.accession, len(g), round(comp.mean(), 3))
    out = ROOT / "results"
    pd.DataFrame(rows).to_csv(out / "sample_assemblies.csv", index=False)
    pd.concat(gene_rows).to_csv(ROOT / "data" / "sample_genes.csv.gz", index=False, compression="gzip")


if __name__ == "__main__":
    main()
