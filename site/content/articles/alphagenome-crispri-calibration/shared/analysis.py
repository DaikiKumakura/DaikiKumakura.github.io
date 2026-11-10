"""Reanalyze pinned author prediction CSVs; does not rerun genomic model inference.

Python 3.12, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1.
Run fetch_inputs.py first, then python analysis.py.
"""
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import pearsonr,spearmanr

ROOT=Path(__file__).resolve().parent
SEED=20261110
B=2000
MODELS=['AlphaGenome','Borzoi','Enformer','NTv3']
FILES={
 'Fulco':[
  'test_Fulco_alphagenome/Fulco_AlphaGenome_base_rna_seq_results.csv',
  'test_Fulco_borzoi/Fulco_Borzoi_base_flashzoi_rna_ensemble_results.csv',
  'test_Fulco_enformer/Fulco_base_enformer_results.csv',
  'test_Fulco_ntv3/Fulco_NTv3_InstaDeepAI_NTv3_tracks_1mb_rna_results.csv'],
 'Gasperini':[
  'test_Gasperini_alphagenome/Gasperini_AlphaGenome_base_rna_seq_results.csv',
  'test_Gasperini_borzoi/Gasperini_Borzoi_base_flashzoi_rna_ensemble_results.csv',
  'test_Gasperini_enformer/Gasperini_base_enformer_results.csv',
  'test_Gasperini_ntv3/Gasperini_NTv3_InstaDeepAI_NTv3_tracks_1mb_rna_results.csv']
}
KEY=['gene_id','enh_loc']


def read_tables(dataset):
    tables={}
    for model,path in zip(MODELS,FILES[dataset]):
        f=ROOT/'source/results'/path
        data=pd.read_csv(f)
        assert not data[KEY].isna().any().any()
        assert not data.duplicated(KEY).any()
        assert np.isfinite(data[['y_delta','pred_delta','enh_dist']]).all().all()
        assert (data.enh_dist>0).all()
        assert ((data.y_delta>0)&(data.y_delta<1)).all()
        if {'pred_wt','pred_crispri_mean'} <= set(data.columns):
            np.testing.assert_allclose(data.pred_delta,
               (data.pred_wt-data.pred_crispri_mean)/(data.pred_wt+1e-8),rtol=2e-6,atol=2e-7)
        tables[model]=data
    joined=tables[MODELS[0]][KEY+['gene_name','y_delta','enh_dist','pred_delta']].rename(
        columns={'pred_delta':MODELS[0]})
    for model in MODELS[1:]:
        other=tables[model][KEY+['y_delta','enh_dist','pred_delta']].rename(
            columns={'pred_delta':model,'y_delta':'y_other','enh_dist':'d_other'})
        joined=joined.merge(other,on=KEY,how='inner',validate='one_to_one')
        np.testing.assert_allclose(joined.y_delta,joined.y_other,atol=1e-7)
        np.testing.assert_allclose(joined.enh_dist,joined.d_other,atol=1)
        joined=joined.drop(columns=['y_other','d_other'])
    return tables,joined.sort_values(KEY).reset_index(drop=True)


def components(data):
    parent={}
    def find(x):
        parent.setdefault(x,x)
        if parent[x]!=x:parent[x]=find(parent[x])
        return parent[x]
    for row in data.itertuples():
        a=find('g:'+row.gene_id);b=find('e:'+row.enh_loc)
        parent[a]=b
    return np.array([find('g:'+g) for g in data.gene_id])


def oof(data,groups,column=None,kind='affine',weights=None):
    """Leave one group out; duplicates of a resampled group never enter its training set."""
    y=data.y_delta.to_numpy(float)
    weights=np.ones(len(data)) if weights is None else weights
    if kind=='mean':x=np.ones((len(y),1))
    elif kind=='distance':x=np.column_stack([np.ones(len(y)),np.log10(data.enh_dist)])
    else:x=np.column_stack([np.ones(len(y)),data[column].to_numpy(float)])
    prediction=np.empty(len(y))
    rank_deficient=0
    for g in np.unique(groups):
        test=groups==g;train=(~test)&(weights>0)
        if weights[test].sum()==0:prediction[test]=np.nan;continue
        assert weights[train].sum()>0
        a=x[train]*np.sqrt(weights[train,None])
        z=y[train]*np.sqrt(weights[train])
        beta,_,rank,_=np.linalg.lstsq(a,z,rcond=None)
        rank_deficient+=int(rank<x.shape[1])
        prediction[test]=x[test]@beta
    return prediction,rank_deficient


def metrics(y,p):
    return {'rmse':float(np.sqrt(np.mean((p-y)**2))),
            'mae':float(np.mean(np.abs(p-y))),
            'bias':float(np.mean(p-y)),
            'pearson':float(pearsonr(y,p).statistic),
            'spearman':float(spearmanr(y,p).statistic),
            'outside_0_1':int(((p<0)|(p>1)).sum())}


def weighted_bootstrap(data,groups,seed):
    """Resample genes and refit every LOOG training regression for each draw.

    Sufficient statistics remove the entire test gene before solving the training fit.
    The same cluster draws are used for all comparisons.
    """
    labels,idx=np.unique(groups,return_inverse=True)
    G=len(labels);y=data.y_delta.to_numpy(float)
    rng=np.random.default_rng(seed)
    weights=rng.multinomial(G,np.ones(G)/G,size=B).astype(float)
    group_n=np.bincount(idx,minlength=G)
    denominator=weights@group_n
    results={};ranks={}
    def aggregate(v):
        a=np.zeros((G,)+v.shape[1:],float)
        np.add.at(a,idx,v)
        return a
    for name in ['mean','distance']+[m+'_raw' for m in MODELS]+[m+'_affine' for m in MODELS]:
        if name.endswith('_raw'):
            p=np.broadcast_to(data[name[:-4]].to_numpy(float),(B,len(y)))
        else:
            if name=='mean':x=np.ones((len(y),1))
            elif name=='distance':x=np.column_stack([np.ones(len(y)),np.log10(data.enh_dist)])
            else:x=np.column_stack([np.ones(len(y)),data[name[:-7]].to_numpy(float)])
            xx=aggregate(x[:,:,None]*x[:,None,:]);xy=aggregate(x*y[:,None])
            allxx=np.einsum('bg,gij->bij',weights,xx)
            allxy=np.einsum('bg,gi->bi',weights,xy)
            trainxx=allxx[:,None,:,:]-weights[:,:,None,None]*xx[None,:,:,:]
            trainxy=allxy[:,None,:]-weights[:,:,None]*xy[None,:,:]
            rank=np.linalg.matrix_rank(trainxx)
            ranks[name]=int(((rank<x.shape[1])&(weights>0)).sum())
            beta=np.einsum('bgij,bgj->bgi',np.linalg.pinv(trainxx),trainxy)
            p=np.einsum('bni,ni->bn',beta[:,idx,:],x)
        error=p-y[None,:]
        mse=np.einsum('bn,bn->b',weights[:,idx],error**2)/denominator
        mae=np.einsum('bn,bn->b',weights[:,idx],np.abs(error))/denominator
        results[name]={'rmse':np.sqrt(mse),'mae':mae}
    return results,ranks


def interval(x):
    return [float(v) for v in np.quantile(x,[.025,.975])]


def analyze_dataset(dataset):
    tables,d=read_tables(dataset)
    groups=d.gene_id.to_numpy();y=d.y_delta.to_numpy(float)
    comp=components(d)
    pred={'mean':oof(d,groups,kind='mean')[0],
          'distance':oof(d,groups,kind='distance')[0]}
    for model in MODELS:
        pred[model+'_raw']=d[model].to_numpy(float)
        pred[model+'_affine']=oof(d,groups,column=model)[0]
    boot,ranks=weighted_bootstrap(d,groups,SEED+(0 if dataset=='Fulco' else 1))
    scores={}
    for name,p in pred.items():
        row=metrics(y,p)
        row['rmse_95ci']=interval(boot[name]['rmse'])
        row['mae_95ci']=interval(boot[name]['mae'])
        g_mse=pd.DataFrame({'g':groups,'e':(p-y)**2}).groupby('g').e.mean()
        row['gene_uniform_rmse']=float(np.sqrt(g_mse.mean()))
        scores[name]=row
    comparisons={}
    for model in MODELS:
        name=model+'_affine'
        for baseline in ['mean','distance',model+'_raw']:
            key=name+'_minus_'+baseline
            comparisons[key]={'rmse_difference':scores[name]['rmse']-scores[baseline]['rmse'],
              'rmse_difference_95ci':interval(boot[name]['rmse']-boot[baseline]['rmse'])}
    for model in MODELS[1:]:
        comparisons['AlphaGenome_affine_minus_'+model+'_affine']={
            'rmse_difference':scores['AlphaGenome_affine']['rmse']-scores[model+'_affine']['rmse'],
            'rmse_difference_95ci':interval(boot['AlphaGenome_affine']['rmse']-boot[model+'_affine']['rmse'])}
    # Sensitivity: no gene or enhancer can appear on both sides of a split.
    cc_pred=oof(d,comp,column='AlphaGenome')[0]
    cc_mean=oof(d,comp,kind='mean')[0]
    # Native AlphaGenome coverage sensitivity; same selection, wider distance coverage.
    full=tables['AlphaGenome'].sort_values(KEY).reset_index(drop=True)
    full_pred=oof(full,full.gene_id.to_numpy(),column='pred_delta')[0]
    # Fixed distance bands are descriptive, not fitted or optimized.
    bands=[]
    for lower,upper,label in [(0,10000,'<10 kb'),(10000,50000,'10-50 kb'),(50000,np.inf,'>=50 kb')]:
        keep=(d.enh_dist>=lower)&(d.enh_dist<upper)
        part=d.loc[keep];mask=keep.to_numpy()
        bands.append({'band':label,'pairs':len(part),'genes':part.gene_id.nunique(),
                      'raw_bias':float(np.mean(pred['AlphaGenome_raw'][mask]-y[mask])),
                      'affine_bias':float(np.mean(pred['AlphaGenome_affine'][mask]-y[mask]))})
    output=d.copy()
    for name,p in pred.items():output[name+'_oof' if not name.endswith('_raw') else name]=p
    output['component_id']=comp
    output.to_csv(ROOT/f'{dataset.lower()}-oof.csv',index=False)
    result={'dataset':dataset,'pairs':len(d),'genes':int(d.gene_id.nunique()),
       'enhancers':int(d.enh_loc.nunique()),'components':len(np.unique(comp)),
       'source_counts':{m:len(t) for m,t in tables.items()},
       'source_gene_counts':{m:int(t.gene_id.nunique()) for m,t in tables.items()},
       'shared_enhancers':int((d.groupby('enh_loc').gene_id.nunique()>1).sum()),
       'mean_observed_decrease':float(y.mean()),'median_observed_decrease':float(np.median(y)),
       'mean_AlphaGenome_prediction':float(d.AlphaGenome.mean()),
       'scores':scores,'paired_comparisons':comparisons,'bootstrap_rank_deficiencies':ranks,
       'distance_bands':bands,
       'sensitivity':{
         'component_holdout':{'alpha_affine':metrics(y,cc_pred),'mean':metrics(y,cc_mean)},
         'native_alpha_coverage':{'pairs':len(full),'genes':int(full.gene_id.nunique()),
              'raw':metrics(full.y_delta.to_numpy(),full.pred_delta.to_numpy()),
              'affine':metrics(full.y_delta.to_numpy(),full_pred)}
       }}
    return result


def make_figures(results):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                         'axes.spines.top':False,'axes.spines.right':False})
    fig,axs=plt.subplots(1,2,figsize=(10.2,4.3))
    for ax,r in zip(axs,results):
        d=pd.read_csv(ROOT/f"{r['dataset'].lower()}-oof.csv")
        ax.scatter(d.y_delta*100,d.AlphaGenome*100,c=d.enh_dist/1000,cmap='viridis',
                   norm=LogNorm(vmin=1,vmax=100),s=24,alpha=.8,edgecolors='none')
        ax.plot([0,100],[0,100],ls='--',color='.4',lw=1)
        ax.set(xlabel='Measured RNA decrease (%)',ylabel='Published AlphaGenome prediction (%)',
               xlim=(0,100),ylim=(-30,100),
               title=f"{r['dataset']}: {r['pairs']} pairs, {r['genes']} genes")
    fig.suptitle('Association and absolute effect size are different questions',fontsize=13)
    fig.tight_layout(rect=(0,0,1,.93))
    from matplotlib.cm import ScalarMappable
    # Explicit separate colorbar avoids covering a data panel.
    fig.subplots_adjust(right=.88)
    cbax=fig.add_axes([.91,.19,.017,.59])
    fig.colorbar(ScalarMappable(norm=LogNorm(1,100),cmap='viridis'),cax=cbax,
                 label='Enhancer-TSS distance (kb)')
    for ext in ['png','svg']:fig.savefig(ROOT/f'raw-calibration.{ext}',dpi=180)
    plt.close(fig)

    fig,axs=plt.subplots(1,2,figsize=(10.2,4.5))
    colors=['#205c7a','#a4592b']
    for ax,r in zip(axs,results):
        for j,suffix in enumerate(['raw','affine']):
            vals=np.array([r['scores'][m+'_'+suffix]['rmse']*100 for m in MODELS])
            cis=np.array([r['scores'][m+'_'+suffix]['rmse_95ci'] for m in MODELS])*100
            # Percentile intervals may be asymmetric around the point estimate.
            x=np.arange(4)+(j-.5)*.34
            ax.bar(x,vals,width=.32,color=colors[j],label='Uncalibrated' if j==0 else 'Gene-held-out affine')
            ax.vlines(x,cis[:,0],cis[:,1],color='black',lw=1)
            ax.plot(x,cis[:,0],'_',color='black',ms=5)
            ax.plot(x,cis[:,1],'_',color='black',ms=5)
        ax.axhline(r['scores']['mean']['rmse']*100,color='.3',ls='--',label='Gene-held-out mean')
        ax.set(xticks=np.arange(4),xticklabels=MODELS,ylabel='RMSE (percentage points)',
               title=r['dataset'],ylim=(0,40))
        ax.tick_params(axis='x',labelrotation=20)
    axs[0].legend(frameon=False,fontsize=8,loc='upper left')
    fig.suptitle('Calibration evaluated on genes excluded from its training',fontsize=13)
    fig.tight_layout(rect=(0,0,1,.94))
    for ext in ['png','svg']:fig.savefig(ROOT/f'heldout-calibration.{ext}',dpi=180)
    plt.close(fig)


if __name__=='__main__':
    manifest=json.loads((ROOT/'source-manifest.json').read_text())
    for entry in manifest['files']:
        assert hashlib.sha256((ROOT/'source'/entry['path']).read_bytes()).hexdigest()==entry['sha256']
    results=[analyze_dataset(name) for name in FILES]
    out={'source_commit':manifest['commit'],'seed':SEED,'bootstrap_draws':B,
         'primary_estimand':'Pair-weighted error among selected experimentally validated pairs, common published coverage.',
         'calibration':'Leave-one-gene-out affine ordinary least squares, without clipping.',
         'bootstrap':'Gene-cluster resampling with full weighted leave-one-gene-out refitting.',
         'datasets':results}
    (ROOT/'results.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    make_figures(results)
    print(json.dumps([{'dataset':r['dataset'],'pairs':r['pairs'],'genes':r['genes'],
         'AG_raw':r['scores']['AlphaGenome_raw']['rmse'],'AG_affine':r['scores']['AlphaGenome_affine']['rmse'],
         'mean':r['scores']['mean']['rmse'],'paired':r['paired_comparisons']['AlphaGenome_affine_minus_mean']} for r in results],indent=2))
