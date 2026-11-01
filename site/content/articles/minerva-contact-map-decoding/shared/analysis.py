"""Artificial contact-map decoding example, not Minerva inference.

Python 3.10+ standard library only. Scores are invented weights, not probabilities.
"""
from pathlib import Path
import csv,json,platform

ROOT=Path(__file__).resolve().parent
SEQUENCE='GGAAAACC'
EDGES=[(0,6,0.9),(0,7,0.8),(1,6,0.8)]

def candidates(matrix,min_separation=3):
    n=len(matrix);best={}
    for i in range(n):
        allowed=[j for j in range(n)if abs(i-j)>=min_separation and i!=j]
        if not allowed:continue
        # First index wins ties, matching argmax for this finite example.
        j=max(allowed,key=lambda k:max(matrix[i][k],matrix[k][i]))
        score=max(matrix[i][j],matrix[j][i]);edge=tuple(sorted((i,j)))
        best[edge]=max(score,best.get(edge,float('-inf')))
    return sorted((i,j,v)for(i,j),v in best.items())

def greedy(edges,threshold=.6):
    selected=[];used=set()
    for i,j,w in sorted((e for e in edges if e[2]>=threshold),key=lambda e:e[2],reverse=True):
        if i in used or j in used:continue
        selected.append((i,j,w));used.update((i,j))
    return sorted(selected)

def exact_matching(edges,threshold=.6):
    accepted=[e for e in edges if e[2]>=threshold];best=[];score=-1.
    for mask in range(1<<len(accepted)):
        chosen=[e for k,e in enumerate(accepted)if mask>>k&1];indices=[x for i,j,w in chosen for x in(i,j)]
        if len(indices)!=len(set(indices)):continue
        total=sum(w for i,j,w in chosen)
        if total>score:best,score=chosen,total
    return sorted(best)

def positive_candidates():
    matrix=[[0.]*len(SEQUENCE)for _ in SEQUENCE]
    for i,j,w in EDGES:matrix[i][j]=matrix[j][i]=w
    return matrix,[e for e in candidates(matrix)if e[2]>=.6]

def main():
    out=ROOT/'results';out.mkdir(exist_ok=True);matrix,pool=positive_candidates();assert pool==sorted(EDGES)
    rows=[]
    for threshold in [.6,.8,.9,.91]:
        a=greedy(pool,threshold);b=exact_matching(pool,threshold)
        rows.append({'threshold':threshold,'greedy_pairs':';'.join(f'{i}-{j}'for i,j,w in a),'greedy_weight_sum':sum(w for i,j,w in a),
        'exact_pairs':';'.join(f'{i}-{j}'for i,j,w in b),'exact_weight_sum':sum(w for i,j,w in b)})
    assert rows[0]['greedy_weight_sum']==.9 and rows[0]['exact_weight_sum']==1.6
    assert rows[-1]['greedy_weight_sum']==rows[-1]['exact_weight_sum']==0
    optimal=exact_matching(pool);assert optimal[0][0]<optimal[1][0]<optimal[1][1]<optimal[0][1]
    assert all(SEQUENCE[i]+SEQUENCE[j]=='GC'for i,j,w in EDGES)
    with(out/'decoding.csv').open('w',newline='',encoding='utf-8')as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    result={'scope':'Artificial map; independent arithmetic implementation; no Minerva model execution',
    'python':platform.python_version(),'sequence':SEQUENCE,'indexing':'0-based','positive_edges':EDGES,'threshold_checks':rows,
    'constraints':'one partner per position; only these three edges; exact solution is nested in this example',
    'not_claimed':['calibrated probabilities','minimum free energy','true biological structure','model accuracy improvement']}
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
