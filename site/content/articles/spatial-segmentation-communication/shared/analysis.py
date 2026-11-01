"""Deterministic transcript reassignment example; not a Giotto reproduction."""
from pathlib import Path
import csv, json, platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
FIG = ROOT / 'figures'
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)
rows = []
for i in range(21):
    a = i / 100
    la, ra, lb, rb = 50*(1-a), 50*a, 50*a, 50*(1-a)
    rows.append(dict(reassigned_fraction=a, ligand_A=la, receptor_A=ra,
                     ligand_B=lb, receptor_B=rb, A_to_B=la*rb,
                     B_to_A=lb*ra, A_to_A=la*ra, B_to_B=lb*rb,
                     total_ligand=la+lb, total_receptor=ra+rb))
assert all(abs(r['total_ligand']-50)<1e-10 and abs(r['total_receptor']-50)<1e-10 for r in rows)
assert rows[0]['B_to_A'] == 0 and rows[10]['A_to_A'] == 225
assert rows[10]['A_to_B'] == 2025 and rows[10]['B_to_A'] == 25
with (OUT/'reassignment.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
fig,ax=plt.subplots(figsize=(6.8,4.2),layout='constrained')
for key,label,style in [('A_to_B','A to B','-'),('B_to_A','B to A','--'),('A_to_A','A to A (B to B identical)',':')]:
    ax.plot([r['reassigned_fraction']*100 for r in rows], [r[key]/2500 for r in rows],style,label=label,linewidth=2)
ax.set(xlabel='Transcripts reassigned to the neighboring type (%)',ylabel='Expression product / original A-to-B product',ylim=(-.02,1.03))
ax.legend(frameon=False);ax.spines[['top','right']].set_visible(False)
fig.savefig(FIG/'reassignment.svg');fig.savefig(FIG/'reassignment.png',dpi=160);plt.close(fig)
(OUT/'summary.json').write_text(json.dumps({'example':'Hypothetical symmetric reassignment; no signaling dynamics', 'at_10_percent':rows[10], 'python':platform.python_version(),'matplotlib':matplotlib.__version__},indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows[10]))
