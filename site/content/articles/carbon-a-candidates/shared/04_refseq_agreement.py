"""Compare Carbon-A predictions with NCBI RefSeq annotation on assemblies whose paired RefSeq copy is identical.

Run: python 04_refseq_agreement.py   (network on first run; cached under data/refseq/)
Writes results/refseq_agreement.csv (per assembly) and results/refseq_by_confidence.csv.
Selection: up to 3 distinct species per division at random among identical pairs (no size filter).
RefSeq annotations were the training labels of Carbon-A, so agreement here is an in-distribution upper bound.
"""
from bisect import bisect_left
from pathlib import Path
import gzip
import json
import re
import urllib.request

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
CADB = "https://huggingface.co/buckets/HuggingFaceBio/genbank-annotations/resolve/cds"
SEED = 20261018
PER_DIVISION = 3
CONF_BINS = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0001]
CACHE = ROOT / "data" / "refseq"


def download(url: str, dest: Path) -> Path:
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".part")
        urllib.request.urlretrieve(url, tmp)
        tmp.replace(dest)
    return dest


def ncbi_dir(gcf: str, asm_name: str) -> str:
    d = gcf.split("_")[1].split(".")[0]
    return f"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/{d[0:3]}/{d[3:6]}/{d[6:9]}/{gcf}_{asm_name}"


def cds_chains(path: Path, refseq: bool, contig_map: dict | None = None) -> dict:
    """{chain_id: (contig, strand, sorted tuple of (start, end))} from CDS features grouped by parent transcript."""
    segs: dict[str, list] = {}
    where: dict[str, tuple] = {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 9 or f[2] != "CDS":
                continue
            contig = contig_map.get(f[0]) if contig_map is not None else f[0]
            if contig is None:
                continue
            attrs = dict(kv.split("=", 1) for kv in f[8].split(";") if "=" in kv)
            key = attrs.get("Parent") or attrs.get("ID")
            if refseq:
                key = f"{key}|{attrs.get('protein_id', '')}"
            segs.setdefault(key, []).append((int(f[3]), int(f[4])))
            where[key] = (contig, f[6])
    return {k: (where[k][0], where[k][1], tuple(sorted(v))) for k, v in segs.items()}


def interval_index(chains: dict) -> dict:
    idx: dict[tuple, list] = {}
    for contig, strand, segs in chains.values():
        idx.setdefault((contig, strand), []).extend(segs)
    out = {}
    for k, v in idx.items():
        v.sort()
        merged: list[list[int]] = []
        for s, e in v:
            if merged and s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        out[k] = (np.array([m[0] for m in merged]), np.array([m[1] for m in merged]))
    return out


def overlaps(idx: dict, contig: str, strand: str, segs: tuple) -> bool:
    if (contig, strand) not in idx:
        return False
    starts, ends = idx[(contig, strand)]
    for s, e in segs:
        i = bisect_left(ends, s)
        if i < len(starts) and starts[i] <= e:
            return True
    return False


def stop_variants(strand: str, segs: tuple) -> set:
    """The chain plus the chain with its 3' end extended or trimmed by one stop codon (3 bp)."""
    out = {segs}
    for d in (3, -3):
        s = list(segs)
        if strand == "+":
            s[-1] = (s[-1][0], s[-1][1] + d)
        else:
            s[0] = (s[0][0] - d, s[0][1])
        out.add(tuple(s))
    return out


def gene_status(path: Path) -> dict:
    out = {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 9 and f[2] == "gene":
                a = dict(kv.split("=", 1) for kv in f[8].split(";") if "=" in kv)
                c = a.get("confidence", "NA")
                out[a["ID"]] = (a.get("status"), float(c) if c != "NA" else np.nan)
    return out


def main() -> None:
    heads = pd.read_csv(ROOT / "data" / "metadata_heads.csv")
    sizes = pd.read_csv(ROOT / "data" / "cds_assemblies.csv")[["accession", "annotations_gff3_gz"]]
    heads = heads.merge(sizes, on="accession", how="left")
    cand = heads[(heads.paired_assembly_comparison == "identical")
                 & heads.paired_refseq_accession.str.startswith("GCF_", na=False)]
    print("identical paired assemblies by division:", cand.groupby("division").size().to_dict())
    rng = np.random.default_rng(SEED)
    picks = []
    for _, g in cand.groupby("division", sort=True):
        # Simple random order without a size filter; skip a species already picked so the units are distinct species
        chosen, seen = [], set()
        for i in rng.permutation(len(g)):
            if g.iloc[i].taxid not in seen:
                chosen.append(i)
                seen.add(g.iloc[i].taxid)
            if len(chosen) == PER_DIVISION:
                break
        picks.append(g.iloc[sorted(chosen)])
    picks = pd.concat(picks)
    per_asm, per_bin = [], []
    for r in picks.itertuples():
        d = CACHE / r.accession
        pred_gff = download(f"{CADB}/{r.division}/{r.accession}/annotations.gff3.gz", d / "carbon.gff3.gz")
        meta = json.loads(download(f"{CADB}/{r.division}/{r.accession}/metadata.json", d / "metadata.json").read_text(encoding="utf-8"))
        gca_dir = meta["source_assembly_url"].rstrip("/")
        lens = np.sort(np.array([c["annotated_length_bp"] for c in meta["contigs"]], dtype=np.int64))[::-1]
        record_n50 = int(lens[np.searchsorted(np.cumsum(lens), lens.sum() / 2)]) if len(lens) else 0
        asm_name = gca_dir.rsplit("/", 1)[1].split("_", 2)[2]
        base = ncbi_dir(r.paired_refseq_accession, asm_name)
        stem = base.rsplit("/", 1)[1]
        try:
            rep = download(f"{base}/{stem}_assembly_report.txt", d / "assembly_report.txt")
            ref_gff = download(f"{base}/{stem}_genomic.gff.gz", d / "refseq.gff.gz")
        except Exception as e:  # missing RefSeq files are counted, not hidden
            print("skip", r.accession, e)
            per_asm.append(dict(division=r.division, accession=r.accession, refseq=r.paired_refseq_accession, skipped=str(e)))
            continue
        cmap = {}
        for line in rep.read_text(encoding="utf-8", errors="replace").splitlines():
            f = line.split("\t")
            if not line.startswith("#") and len(f) > 6 and f[4] != "na" and f[6] != "na":
                cmap[f[6]] = f[4]  # RefSeq sequence accession -> GenBank accession
        ref = cds_chains(ref_gff, True, cmap)
        pred = cds_chains(pred_gff, False)
        if not ref:
            per_asm.append(dict(division=r.division, accession=r.accession, refseq=r.paired_refseq_accession, skipped="no RefSeq CDS"))
            continue
        ref_set = set(ref.values())
        ref_idx, pred_idx = interval_index(ref), interval_index(pred)
        status = gene_status(pred_gff)
        rows = []
        for key, (c, s, segs) in pred.items():
            st, cf = status.get(re.sub(r"_transcript(\d+)$", r"_gene\1", key), (None, np.nan))
            rows.append(dict(status=st, confidence=cf, exact=(c, s, segs) in ref_set,
                             exact_stop_tolerant=any((c, s, v) in ref_set for v in stop_variants(s, segs)),
                             overlap=overlaps(ref_idx, c, s, segs)))
        p = pd.DataFrame(rows)
        # Recall over RefSeq coding loci: transcript spans merged per contig and strand
        loci = interval_index({k: (c, s, ((segs[0][0], segs[-1][1]),)) for k, (c, s, segs) in ref.items()})
        n_loci = sum(len(v[0]) for v in loci.values())
        hit = sum(overlaps(pred_idx, c, s, ((int(a), int(b)),)) for (c, s), (st_, en_) in loci.items() for a, b in zip(st_, en_))
        sel = (p.status == "complete") & (p.confidence >= 0.1)
        per_asm.append(dict(division=r.division, accession=r.accession, refseq=r.paired_refseq_accession, organism=r.organism_name,
                            taxid=r.taxid, record_n50=record_n50, predicted=len(p), refseq_cds_chains=len(ref), refseq_coding_loci=n_loci,
                            precision_exact=p.exact.mean(), precision_exact_stop_tolerant=p.exact_stop_tolerant.mean(),
                            precision_overlap=p.overlap.mean(), frac_complete_conf_ge_0_1=sel.mean(),
                            precision_exact_stop_tolerant_complete_conf_ge_0_1=p[sel].exact_stop_tolerant.mean(),
                            precision_overlap_complete_conf_ge_0_1=p[sel].overlap.mean(),
                            recall_loci_overlap=hit / n_loci))
        p["bin"] = pd.cut(p.confidence, CONF_BINS, right=False)
        b = (p[p.status == "complete"].groupby("bin", observed=False)
             .agg(n=("exact", "size"), exact_stop_tolerant=("exact_stop_tolerant", "sum"), overlap=("overlap", "sum")).reset_index())
        b["division"], b["accession"] = r.division, r.accession
        per_bin.append(b)
        print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in per_asm[-1].items()})
    out = ROOT / "results"
    pd.DataFrame(per_asm).to_csv(out / "refseq_agreement.csv", index=False)
    pb = pd.concat(per_bin)
    pb["bin"] = pb["bin"].astype(str)
    pb.to_csv(out / "refseq_by_confidence.csv", index=False)


if __name__ == "__main__":
    main()
