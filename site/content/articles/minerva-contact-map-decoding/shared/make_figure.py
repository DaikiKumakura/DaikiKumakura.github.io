"""Optional rendering of the artificial matching example; matplotlib required."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from analysis import SEQUENCE,positive_candidates,greedy,exact_matching

ROOT=Path(__file__).resolve().parent
matrix,pool=positive_candidates()
fig,axs=plt.subplots(1,3,figsize=(10,3.2),layout='constrained')
axs[0].imshow(matrix,vmin=0,vmax=1,cmap='Greys',origin='lower')
for i,j,w in pool:axs[0].text(j,i,f'{w:.1f}',ha='center',va='center',color='white',fontsize=9)
axs[0].set(xlabel='Position (0-based)',ylabel='Position (0-based)',title='Artificial contact weights',xticks=[0,2,4,6,7],yticks=[0,2,4,6,7])
for ax,edges,title,color in [(axs[1],greedy(pool),'Greedy: total 0.9','#1f77b4'),(axs[2],exact_matching(pool),'Maximum weight: total 1.6','#b55a00')]:
    ax.plot(range(8),[0]*8,'ko',markersize=3)
    for k,ch in enumerate(SEQUENCE):ax.text(k,-.3,ch,ha='center',fontsize=12);ax.text(k,-.65,str(k),ha='center',fontsize=9)
    for i,j,w in edges:
        ax.add_patch(Arc(((i+j)/2,0),j-i,(j-i)*.7,theta1=0,theta2=180,color=color,linewidth=2))
        ax.text((i+j)/2,(j-i)*.35+.05,f'{w:.1f}',ha='center',fontsize=10)
    ax.set(xlim=(-.6,7.6),ylim=(-1,3.1),title=title);ax.axis('off')
(ROOT/'figures').mkdir(exist_ok=True)
fig.savefig(ROOT/'figures/decoding.png',dpi=180)
plt.close(fig)
