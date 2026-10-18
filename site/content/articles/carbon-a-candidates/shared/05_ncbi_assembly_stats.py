"""Fetch NCBI assembly statistics (total length, contig N50, RefSeq annotation gene counts) for the sampled and RefSeq-compared assemblies.

Run: python 05_ncbi_assembly_stats.py   (network; NCBI Datasets v2 API, batches of 20 accessions)
Writes data/ncbi_assembly_stats.csv.
"""
from pathlib import Path
import json
import time
import urllib.request

import pandas as pd

ROOT = Path(__file__).resolve().parent
API = "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/{}/dataset_report"
BATCH = 20


def fetch(accs: list[str]) -> list[dict]:
    url = API.format(",".join(accs))
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read()).get("reports", [])
        except Exception as e:
            print("retry", attempt, e)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(url)


def main() -> None:
    sample = pd.read_csv(ROOT / "results" / "sample_assemblies.csv")
    agree = pd.read_csv(ROOT / "results" / "refseq_agreement.csv")
    accs = sample["accession"].tolist() + [a for a in agree["accession"] if a not in set(sample["accession"])]
    low = ROOT / "results" / "low_yield_assemblies.csv"  # written by 06; rerun 05 then 06 to include these
    if low.exists():
        lo = pd.read_csv(low)
        accs += [a for a in lo.loc[(lo.paired_assembly_comparison == "identical") & (lo.gene_count > 0), "accession"] if a not in set(accs)]
    paired = [a for a in sample["paired_refseq"].dropna() if str(a).startswith("GCF_")] + agree["refseq"].dropna().tolist()
    rows = []
    for i in range(0, len(accs + paired), BATCH):
        for rep in fetch((accs + paired)[i:i + BATCH]):
            st = rep.get("assembly_stats", {})
            ann = rep.get("annotation_info", {})
            rows.append(dict(accession=rep.get("accession"), total_sequence_length=int(st.get("total_sequence_length", 0)),
                             contig_n50=st.get("contig_n50"), number_of_contigs=st.get("number_of_contigs"),
                             assembly_level=rep.get("assembly_info", {}).get("assembly_level"),
                             release_date=rep.get("assembly_info", {}).get("release_date"),
                             submitter=rep.get("assembly_info", {}).get("submitter"),
                             annotation_name=ann.get("name"),
                             annotated_protein_coding_genes=ann.get("stats", {}).get("gene_counts", {}).get("protein_coding")))
        time.sleep(0.4)  # stay under the anonymous rate limit
    pd.DataFrame(rows).to_csv(ROOT / "data" / "ncbi_assembly_stats.csv", index=False)
    print(len(rows), "reports")


if __name__ == "__main__":
    main()
