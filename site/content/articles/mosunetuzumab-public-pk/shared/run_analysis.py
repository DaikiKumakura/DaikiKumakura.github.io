"""Independent public-model reconstruction; educational simulation, not clinical advice."""
from pathlib import Path
import json, csv, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'; FIG=ROOT/'figures'
OUT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
P=np.array([1.08,5.49,.584,16.3,6.17,1.46]) # CLbase,V1,CLss,HLtrans,V2,Q
NAMES=['CLbase','V1','CLss','HLtrans','V2','Q']
CI=np.array([[.962,1.20],[5.221,5.76],[.561,.607],[14.026,18.6],[5.729,6.61],[1.354,1.57]])
OMEGA=np.diag([.426,.0981,.0343,.739,.0621]); OMEGA[0,1]=OMEGA[1,0]= .1804; OMEGA[2,3]=OMEGA[3,2]=-.08925
assert np.linalg.eigvalsh(OMEGA).min()>0
SCENARIOS=[('Reference',1,2,7),('First 0.5 mg',.5,2,7),('First 2 mg',2,2,7),('Second 1 mg',1,1,7),('Second 4 mg',1,4,7),('Interval 3.5 d',1,2,3.5),('Interval 14 d',1,2,14)]
def regimen(first=1,second=2,interval=7,end=84):
    third=2*interval
    return [(0,first,4/24),(interval,second,4/24),(third,60,4/24),(third+7,60,2/24)]+[(t,30,2/24) for t in np.arange(third+28,end,21)]
def simulate(pars,first=1,second=2,interval=7,end=42,dt=1/96,keep=False):
    p=np.atleast_2d(pars); cb,v1,cs,hl,v2,q=p.T
    events=regimen(first,second,interval,end)
    # RK4 split exactly at infusion boundaries. Dose input constant per step.
    times=np.arange(0,end+dt/2,dt); n=len(p); a=np.zeros((2,n)); auc=np.zeros(n); peak=np.zeros(n)
    c1max=np.zeros(n); c1auc=None; c1trough=None; auc63=None; auc84=None; pre=None; history=[]
    def rhs(t,a,rate):
        cl=cs+(cb-cs)*np.exp(-np.log(2)*t/hl)
        return np.array([rate-(cl+q)/v1*a[0]+q/v2*a[1],q/v1*a[0]-q/v2*a[1]])
    for j,t in enumerate(times):
        c=a[0]/v1
        if keep: history.append(c.copy())
        if t<=4/24+1e-9: peak=np.maximum(peak,c)
        if t<21: c1max=np.maximum(c1max,c)
        if abs(t-2*interval)<1e-8: pre=c.copy()
        if abs(t-21)<1e-8: c1auc=auc.copy(); c1trough=c.copy()
        if abs(t-63)<1e-8: auc63=auc.copy()
        if abs(t-84)<1e-8: auc84=auc.copy()
        if j==len(times)-1: break
        rate=sum(d/dur for start,d,dur in events if start<=t+dt/2<start+dur)
        k1=rhs(t,a,rate); k2=rhs(t+dt/2,a+dt*k1/2,rate); k3=rhs(t+dt/2,a+dt*k2/2,rate); k4=rhs(t+dt,a+dt*k3,rate)
        new=a+dt*(k1+2*k2+2*k3+k4)/6
        auc+=dt*(c+new[0]/v1)/2; a=new
    result={'first_peak':peak,'pre60':pre,'auc42':auc if end==42 else None,'c1_auc':c1auc,'c1_max':c1max,'c1_trough':c1trough,'c4_auc':auc84-auc63 if end==84 else None}
    return result,(times,np.array(history)) if keep else None
def write(name,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160,'svg.fonttype':'none','svg.hashsalt':'mosunetuzumab-public-pk'})
base,trace=simulate(P,end=84,keep=True); early,_=simulate(P)
validation=[]
for key,published in [('c1_auc',35.2),('c1_max',11.1),('c1_trough',2.6),('auc42',126),('c4_auc',52.9)]:
    value=float((early if key=='auc42' else base)[key][0]);validation.append({'endpoint':key,'published_geometric_mean':published,'typical_reconstruction':value,'difference_pct':100*(value/published-1)})
write('benchmark.csv',validation)
# Event-aware independent adaptive solver comparison at 42 d and tighter RK4.
strict,_=simulate(P,dt=1/192)
assert max(abs(float(strict[k][0]/early[k][0]-1)) for k in ['first_peak','pre60','auc42'])<.0001
state=np.zeros(3)
for lo,hi in zip(sorted({0,42,*[x for t,d,h in regimen(end=42) for x in (t,t+h) if x<42]}),sorted({0,42,*[x for t,d,h in regimen(end=42) for x in (t,t+h) if x<42]})[1:]):
    rate=sum(d/h for t,d,h in regimen(end=42) if t<=(lo+hi)/2<t+h)
    def f(t,a):
        cl=P[2]+(P[0]-P[2])*np.exp(-np.log(2)*t/P[3]);return [rate-(cl+P[5])/P[1]*a[0]+P[5]/P[4]*a[1],P[5]/P[1]*a[0]-P[5]/P[4]*a[1],a[0]/P[1]]
    state=solve_ivp(f,[lo,hi],state,rtol=1e-10,atol=1e-12).y[:,-1]
assert abs(state[2]/early['auc42'][0]-1)<.0001
rng=np.random.default_rng(20261002); eta=rng.multivariate_normal(np.zeros(5),OMEGA,2000)
pop=np.tile(P,(len(eta),1));pop[:,:5]*=np.exp(eta)
ref,_=simulate(pop); write('population_reference.csv',[dict(endpoint=k,p025=float(np.quantile(ref[k],.025)),median=float(np.median(ref[k])),p975=float(np.quantile(ref[k],.975))) for k in ['first_peak','pre60','auc42']]); rows=[]; fig,axes=plt.subplots(1,3,figsize=(11,4),layout='constrained')
for name,d1,d2,gap in SCENARIOS:
    result,_=simulate(pop,d1,d2,gap)
    row={'scenario':name,'first_mg':d1,'second_mg':d2,'interval_days':gap,'n':len(eta)}
    for key in ['first_peak','pre60','auc42']:
        ratio=100*(result[key]/ref[key]-1); low,median,high=np.quantile(ratio,[.025,.5,.975]);row.update({key+'_pct_median':median,key+'_pct_p025':low,key+'_pct_p975':high})
    rows.append(row)
write('paired_regimens.csv',rows)
for ax,key,title in zip(axes,['first_peak','pre60','auc42'],['First-dose peak','Before first 60 mg dose','AUC 0–42 days']):
    for i,r in enumerate(rows[1:]):
        med=r[key+'_pct_median'];ax.errorbar(med,i,xerr=[[med-r[key+'_pct_p025']],[r[key+'_pct_p975']-med]],fmt='o',color='#25577b',capsize=3)
    ax.set_yticks(range(6),[r['scenario'] for r in rows[1:]] if ax==axes[0] else []);ax.axvline(0,color='gray',lw=1);ax.set_xlabel('Paired change vs reference (%)');ax.set_title(title)
fig.savefig(FIG/'paired.png');fig.savefig(FIG/'paired.svg',metadata={'Date':None});plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4),layout='constrained');t,c=trace;ax.plot(t,c[:,0],color='#25577b');ax.set(xlabel='Time since first dose (days)',ylabel='Mosunetuzumab (µg/mL)',title='Reference regimen: typical-parameter reconstruction')
for td,d,dur in regimen():ax.axvline(td,color='gray',lw=.6,alpha=.4);ax.annotate(f'{d:g} mg',(td,0),xytext=(3,6),textcoords='offset points',fontsize=8)
fig.savefig(FIG/'pk.png');fig.savefig(FIG/'pk.svg',metadata={'Date':None});plt.close(fig)
sens=[]
for i,name in enumerate(NAMES):
    for bound,value in zip(['lower','upper'],CI[i]):
        p=P.copy();p[i]=value;r,_=simulate(p)
        sens.append({'parameter':name,'bound':bound,'value':value,**{k+'_pct':100*(r[k][0]/early[k][0]-1) for k in ['first_peak','pre60','auc42']}})
write('parameter_sensitivity.csv',sens)
fig,ax=plt.subplots(figsize=(8,4),layout='constrained')
for j,key in enumerate(['first_peak','pre60','auc42']):ax.plot([r[key+'_pct'] for r in sens],np.arange(12)+.15*j,'o',label=key)
ax.set_yticks(np.arange(12),[r['parameter']+' '+r['bound'] for r in sens]);ax.axvline(0,color='gray');ax.set_xlabel('Change at marginal parameter CI bound (%)');ax.legend();fig.savefig(FIG/'sensitivity.png');fig.savefig(FIG/'sensitivity.svg',metadata={'Date':None});plt.close(fig)
anti=[]; tt,cc=simulate(P,keep=True)[1];cc=cc[:,0]
for drug,level in [('None',0),('RTX',10),('OBI',10),('RTX',305)]:
    for coupling in ['binding only','binding + CLbase covariate']:
        pp=P.copy()
        if coupling!='binding only':pp[0]*=(np.log(max(level*1000,500))/np.log(500))**(-.573)
        t,c=simulate(pp,keep=True)[1];c=c[:,0]; half=24 if drug=='RTX' else 28;kd=.675 if drug=='RTX' else .600
        residual=level*np.exp(-np.log(2)*t/half);ro=100*c/(c+10.2+10.2/kd*residual); rm=ro.max();prob=1/(1+np.exp(-(-2.64+.0196*rm)))
        anti.append({'drug':drug,'baseline_ug_ml':level,'assumption':coupling,'ro_max_pct':rm,'crs_model_probability_pct':100*prob})
write('anti_cd20_sensitivity.csv',anti)
fig,axes=plt.subplots(1,2,figsize=(9,4),layout='constrained')
for assumption,marker in [('binding only','o'),('binding + CLbase covariate','s')]:
    rs=[r for r in anti if r['assumption']==assumption]
    for ax,key in zip(axes,['ro_max_pct','crs_model_probability_pct']):ax.plot(range(4),[r[key] for r in rs],marker+'-',label=assumption)
for ax,label in zip(axes,['Maximum CD20 occupancy (%)','CRS logistic-model output (%)']):ax.set_xticks(range(4),['None','RTX 10','OBI 10','RTX 305']);ax.set_ylabel(label);ax.set_ylim(bottom=0);ax.set_xlabel('Baseline anti-CD20 (µg/mL)')
axes[0].legend(fontsize=8);fig.savefig(FIG/'ro-crs.png');fig.savefig(FIG/'ro-crs.svg',metadata={'Date':None});plt.close(fig)
meta={'seed':20261002,'n':2000,'dt_days':1/96,'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,'python':sys.version,'omega_min_eigenvalue':float(np.linalg.eigvalsh(OMEGA).min()),'adaptive_auc42':float(state[2]),'rk4_auc42':float(early['auc42'][0])}
(OUT/'run_metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print(json.dumps({'benchmark':validation,'paired':rows,'anti':anti},indent=2))




