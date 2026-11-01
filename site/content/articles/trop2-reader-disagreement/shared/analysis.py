"""Enumerate five-reader binary decisions, not clinical observations.

Python 3.10+ standard library only. Run: python analysis.py
No independence assumption or random generation is used.
"""
from itertools import product, combinations
from pathlib import Path
import csv, json, platform

def main():
    out=Path(__file__).resolve().parent/'results'
    out.mkdir(exist_ok=True)
    rows=[]
    for votes in product([0,1],repeat=5):
        k=sum(votes)
        discordant=sum(a!=b for a,b in combinations(votes,2))
        assert discordant==k*(5-k)
        rows.append({'votes':''.join(map(str,votes)),'positive_readers':k,
                     'any_disagreement':int(0<k<5),
                     'discordant_reader_pairs':discordant,'all_reader_pairs':10,
                     'pair_disagreement_fraction':discordant/10,
                     'majority_label':int(k>=3)})
    values=[r['pair_disagreement_fraction'] for r in rows if r['any_disagreement']]
    assert min(values)==.4 and max(values)==.6
    assert sum(r['any_disagreement'] for r in rows)==30
    reported_fraction=.67
    summary={'scope':'Exhaustive possible voting patterns, not a uniform probability distribution over patients',
             'readers':5,'patterns_enumerated':len(rows),
             'reported_any_disagreement_input':reported_fraction,
             'pair_disagreement_lower_bound':reported_fraction*min(values),
             'pair_disagreement_upper_bound':reported_fraction*max(values),
             'gold_standard':'not specified; diagnostic error not identified',
             'python':platform.python_version()}
    assert abs(summary['pair_disagreement_lower_bound']-.268)<1e-12
    assert abs(summary['pair_disagreement_upper_bound']-.402)<1e-12
    with (out/'five-reader-patterns.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
