"""Illustrative calculations, not a fit to CAR-T patient or single-cell data.

Run: python analysis.py
Requires Python 3.12, numpy, matplotlib (versions recorded in results.json).
All reported inputs are printed aggregate values from Bai et al. (2026).
"""
from pathlib import Path
import csv
import json
import math
import platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
FIG = ROOT / 'figures'
FIG.mkdir(exist_ok=True)
reported = {'icd_aa_reference':154, 'icd_aa_compact':45,
            'antigen_ec50_reference_molecules_per_target':650,
            'antigen_ec50_compact_molecules_per_target':1130}
gain = 8.4
result = {'inputs': reported,
          'icd_reduction_percent':100*(1-45/154),
          'antigen_ec50_ratio':1130/650,
          'illustrative_initial_gain':gain,
          'illustrative_extension_in_half_lives':math.log2(gain),
          'illustrative_half_lives_days':[1,2,3],
          'illustrative_extension_days':[h*math.log2(gain) for h in [1,2,3]],
          'versions':{'python':platform.python_version(),'numpy':np.__version__,
                      'matplotlib':matplotlib.__version__}}
(OUT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# These are Hill=1 explanatory curves anchored at published EC50s, not fitted curves.
A = np.geomspace(10, 100000, 241)
yref = A/(650+A)
ycompact = A/(1130+A)
with (OUT/'antigen_illustration.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['antigen_molecules_per_target','reference_normalized','compact_normalized'])
    w.writerows(zip(A,yref,ycompact))
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,
                     'savefig.dpi':180,'figure.constrained_layout.use':True})
fig,ax=plt.subplots(figsize=(7.6,4.5))
ax.semilogx(A,yref,label='Reference: EC50 = 650',color='#245d81',linewidth=2.2)
ax.semilogx(A,ycompact,label='Compact: EC50 = 1,130',color='#bd5a28',linestyle='--',linewidth=2.2)
ax.axhline(.5,color='#777777',linewidth=.7,linestyle=':')
ax.scatter([650,1130],[.5,.5],color=['#245d81','#bd5a28'],zorder=3)
ax.set(xlabel='Antigen molecules per target cell',ylabel='Fraction of each construct\'s response span',ylim=(0,1.04))
ax.set_title('Illustration with Hill slope fixed at 1',loc='left',fontsize=12)
ax.legend(loc='upper left',frameon=False)
fig.savefig(FIG/'antigen-normalized.png');plt.close(fig)

# Hypothetical decay starts at the end of production: R/R_threshold = 2 or 16.8.
# A higher initial level delays threshold crossing without changing the decay slope.
t=np.linspace(0,16,321);half=2.0;k=math.log(2)/half
rref=2*np.exp(-k*t);rcompact=2*gain*np.exp(-k*t)
with (OUT/'decay_illustration.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['time_days','reference_R_over_threshold','higher_initial_R_over_threshold'])
    w.writerows(zip(t,rref,rcompact))
fig,ax=plt.subplots(figsize=(7.6,4.5))
ax.semilogy(t,rref,label='Initial level = 2 thresholds',color='#245d81',linewidth=2.2)
ax.semilogy(t,rcompact,label='Initial level = 16.8 thresholds',color='#bd5a28',linestyle='--',linewidth=2.2)
ax.axhline(1,color='#555555',linestyle=':',label='Functional threshold (assumed)')
ax.axvline(2,color='#245d81',linewidth=.8,alpha=.5)
ax.axvline(2+2*math.log2(gain),color='#bd5a28',linewidth=.8,alpha=.5)
ax.set(xlabel='Days after the assumed end of production',ylabel='Surface receptor / assumed threshold',ylim=(.005,30))
ax.set_title('Hypothetical example: both receptor half-lives = 2 days',loc='left',fontsize=12)
ax.legend(frameon=False,loc='upper right')
fig.savefig(FIG/'threshold-duration.png');plt.close(fig)
assert math.isclose(result['icd_reduction_percent'],70.77922077922078)
assert math.isclose(math.exp(-k*2)*2,1.0)
assert math.isclose(2*gain*math.exp(-k*(2+2*math.log2(gain))),1.0)
print(json.dumps(result,ensure_ascii=False,indent=2))
