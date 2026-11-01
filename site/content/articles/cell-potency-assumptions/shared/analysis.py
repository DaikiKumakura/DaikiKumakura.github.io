"""Exact occupancy and expected plug-in entropy under multinomial sampling.

No potency method is fitted. Profiles and depths are hypothetical.
"""
from pathlib import Path
import csv, json, math, platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results';FIG=ROOT/'figures'
OUT.mkdir(exist_ok=True);FIG.mkdir(exist_ok=True)
profiles={'uniform':[.01]*100,'dominant':[.8]+[.2/99]*99}
def entropy(p):return -sum(x*math.log(x) for x in p if x)
def expected_entropy(p,n):
    total=0.
    for prob in p:
        for k in range(1,n+1):
            lp=math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)+k*math.log(prob)+(n-k)*math.log1p(-prob)
            total-=math.exp(lp)*(k/n)*math.log(k/n)
    return total
rows=[]
for name,p in profiles.items():
    for n in [50,100,200,500,1000]:
        rows.append({'profile':name,'umi_depth':n,'expected_detected_genes':sum(1-(1-x)**n for x in p),
                     'population_entropy_nats':entropy(p),'expected_observed_entropy_nats':expected_entropy(p,n)})
assert abs(rows[0]['expected_detected_genes']-100*(1-.99**50))<1e-9
assert all(r['expected_observed_entropy_nats']<=r['population_entropy_nats']+1e-10 for r in rows)
with (OUT/'depth_entropy.csv').open('w',newline='',encoding='utf-8')as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
fig,axs=plt.subplots(1,2,figsize=(8,3.5),layout='constrained')
for name in profiles:
    sub=[r for r in rows if r['profile']==name]
    marker,style=('o','-') if name=='uniform' else ('s','--')
    axs[0].plot([r['umi_depth'] for r in sub],[r['expected_detected_genes'] for r in sub],marker=marker,linestyle=style,label=name)
    axs[1].plot([r['umi_depth'] for r in sub],[r['expected_observed_entropy_nats'] for r in sub],marker=marker,linestyle=style,label=name)
for ax in axs:ax.set_xscale('log');ax.set_xlabel('Sampled UMI count');ax.spines[['top','right']].set_visible(False)
axs[0].set_ylabel('Expected detected genes');axs[1].set_ylabel('Expected plug-in entropy (nats)');axs[0].legend(frameon=False)
fig.savefig(FIG/'depth-entropy.svg');fig.savefig(FIG/'depth-entropy.png',dpi=160);plt.close(fig)
(OUT/'summary.json').write_text(json.dumps({'scope':'Hypothetical multinomial sampling; no biological potency labels or method benchmark','profiles':{k:{'entropy_nats':entropy(p),'effective_genes':math.exp(entropy(p))} for k,p in profiles.items()},'python':platform.python_version(),'matplotlib':matplotlib.__version__},indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))
