"""Recalculate printed RFS estimates and draw explicitly illustrative curves.

Run: python analysis.py
Requires matplotlib 3.9.1. No patient data, curve digitization, or statistical fit.
"""
from pathlib import Path
import csv
import json
import math
import platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
FIG = (ROOT / 'figures' if ROOT.parent.name == 'shared'
       else ROOT / 'shared' / 'mrna-vaccine-rfs-comparison' / 'figures')
OUT.mkdir(exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)
S0, S1, T, DELAY = .700, .822, 2., .5
risk0, risk1 = 1-S0, 1-S1
delta = S1-S0
lc = -math.log(S0)/T
la = -math.log(S1)/T
lb = (-math.log(S1)-lc*DELAY)/(T-DELAY)
constant_r = la/lc
delayed_r = lb/lc

def treated_delayed(t):
    return math.exp(-lc*min(t, DELAY)-lb*max(0, t-DELAY))

rows = []
for i in range(241):
    t = T*i/240
    rows.append([t*12, math.exp(-lc*t), math.exp(-la*t), treated_delayed(t)])
with (OUT/'illustrative-curves.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['month','control','constant_effect','delayed_effect']);w.writerows(rows)
result = {
    'method':'Arithmetic on printed 24-month estimates; hypothetical constant and piecewise exponential models',
    'not_a_trial_curve_reconstruction':True,
    'source_rfs_control':S0,'source_rfs_combination':S1,
    'risk_control':risk0,'risk_combination':risk1,
    'absolute_risk_reduction':delta,'risk_ratio_at_24_months':risk1/risk0,
    'relative_risk_reduction_at_24_months':1-risk1/risk0,
    'reciprocal_absolute_risk_reduction_at_24_months':1/delta,
    'control_hazard_per_year':lc,'constant_effect_ratio':constant_r,
    'delayed_effect_ratio_after_six_months':delayed_r,
    'hypothetical_rfs_at_6_months_constant':math.exp(-la*DELAY),
    'hypothetical_rfs_at_6_months_delayed':treated_delayed(DELAY),
    'checks':{'control_24m':rows[-1][1], 'constant_24m':rows[-1][2], 'delayed_24m':rows[-1][3]},
    'environment':{'python':platform.python_version(),'matplotlib':matplotlib.__version__},
}
assert math.isclose(delta,.122,abs_tol=1e-12)
assert math.isclose(rows[-1][2],S1,abs_tol=1e-12)
assert math.isclose(rows[-1][3],S1,abs_tol=1e-12)
(OUT/'calculations.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(8.6,5.4),layout='constrained')
months=[r[0] for r in rows]
ax.plot(months,[r[1]*100 for r in rows],color='#777777',lw=2,label='Hypothetical control')
ax.plot(months,[r[2]*100 for r in rows],color='#156082',lw=2.7,label='Constant treatment effect')
ax.plot(months,[r[3]*100 for r in rows],color='#c46b28',lw=2.7,ls='--',label='No effect for 6 months, then benefit')
ax.axvline(6,color='#bcbcbc',lw=1,ls=':')
ax.scatter([24],[82.2],color='#182a3a',s=28,zorder=5)
ax.annotate('Same 24-month RFS: 82.2%',(24,82.2),xytext=(12,88),arrowprops={'arrowstyle':'-','color':'#444'},fontsize=10)
ax.set(xlabel='Months from a hypothetical baseline',ylabel='Event-free proportion (%)',xlim=(0,24.5),ylim=(65,101),xticks=[0,6,12,18,24])
ax.set_title('Two time profiles can give the same 24-month estimate',loc='left',pad=12,fontweight='bold')
ax.grid(axis='y',alpha=.18)
ax.legend(loc='lower left',frameon=False,fontsize=10)
fig.text(.02,-.025,'Illustration only. Not Kaplan-Meier curves or fitted INTerpath-001 hazards.',fontsize=9,color='#555')
fig.savefig(FIG/'same-endpoint-different-timing.png',dpi=180,bbox_inches='tight')
fig.savefig(FIG/'same-endpoint-different-timing.svg',bbox_inches='tight')
plt.close(fig)
print(json.dumps(result,ensure_ascii=False,indent=2))
