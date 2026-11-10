"""Independent reanalysis of fixed author results; no model training or inference."""
from pathlib import Path
import ast,hashlib,json,re
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent
MODELS=['CheMeleon','RF','Chemprop']
SEED=20261110
B=10000

def parse_results(model):
    text=(ROOT/'source/analysis/moleculeace_results'/f'{model}.md').read_text(encoding='utf-8')
    rows=[]
    for chunk in re.split(r'^## Random Seed ',text,flags=re.M)[1:]:
        seed=int(chunk.splitlines()[0]);summary=chunk.split('results_dict =',1)[1].split('```',1)[0]
        labels=ast.literal_eval(summary.strip())
        for name,body in re.findall(r'### `([^`]+)`\s+(.*?)(?=\n### |\Z)',chunk,flags=re.S):
            match=re.search(r'\| overall test rmse\s*\|\s*([\d.e+-]+)',body)
            assert match,name
            rows.append(dict(model=model,benchmark=name,seed=seed,total=float(match[1]),**labels[name]))
    out=pd.DataFrame(rows)
    assert len(out)==150 and not out.duplicated(['model','benchmark','seed']).any()
    assert np.isfinite(out[['total','cliff','noncliff']]).all().all()
    assert (out[['total','cliff','noncliff']]>0).all().all()
    return out

def interval(values):return [float(x) for x in np.quantile(values,[.025,.975])]
def summarize(logs,draws):
    mean=float(np.mean(logs));boots=logs[draws].mean(axis=1)
    return dict(tasks=len(logs),geometric_rmse_ratio=float(np.exp(mean)),ratio_95ci=np.exp(interval(boots)).tolist(),
                relative_reduction_percent=float(100*(1-np.exp(mean))),
                reduction_95ci_percent=[float(100*(1-np.exp(x))) for x in interval(boots)[::-1]],
                strict_lower_mean_count=int((logs<0).sum()),higher_count=int((logs>0).sum()))

def main():
    manifests=[json.loads((ROOT/n).read_text()) for n in ['source-manifest.json','assay-manifest.json']]
    for manifest in manifests:
        for row in manifest['files']:
            assert hashlib.sha256((ROOT/'source'/row['path']).read_bytes()).hexdigest()==row['sha256']
    runs=pd.concat([parse_results(m) for m in MODELS],ignore_index=True)
    # Check precise subgroup summaries against the author's exported plot input.
    source=pd.read_csv(ROOT/'source/analysis/cliffs/source_data.csv')
    for model in MODELS:
        for benchmark,g in runs[runs.model==model].groupby('benchmark'):
            for subset in ['cliff','noncliff']:
                a=np.sort(g[subset].to_numpy());v=source[(source.model==model)&(source.benchmark==benchmark)&(source.subtask==subset)].score
                np.testing.assert_allclose(a,np.sort(v),atol=1e-13)
    counts=[]
    for benchmark in sorted(runs.benchmark.unique()):
        data=pd.read_csv(ROOT/'source/assays'/f'{benchmark}.csv');test=data[data.split=='test']
        assert set(data['split'])=={'train','test'} and not data.smiles.duplicated().any()
        n1=int((test.cliff_mol==1).sum());n0=int((test.cliff_mol==0).sum());assert n1 and n0 and n1+n0==len(test)
        g=runs[runs.benchmark==benchmark]
        pooled=np.sqrt((n1*g.cliff**2+n0*g.noncliff**2)/(n1+n0))
        np.testing.assert_allclose(pooled,g.total,atol=5.1e-6,rtol=0)
        runs.loc[g.index,'total_reconstructed']=pooled
        counts.append(dict(benchmark=benchmark,n_train=int((data.split=='train').sum()),n_test=len(test),n_cliff=n1,n_noncliff=n0))
    count=pd.DataFrame(counts).set_index('benchmark')
    means=runs.groupby(['benchmark','model'])[['total_reconstructed','cliff','noncliff']].mean().unstack('model')
    task=count.copy()
    for subset in ['total_reconstructed','cliff','noncliff']:
        label='total' if subset=='total_reconstructed' else subset
        for model in MODELS:task[model+'_'+label]=means[subset][model]
        for baseline in ['RF','Chemprop']:
            task['logratio_'+baseline+'_'+label]=np.log(means[subset].CheMeleon/means[subset][baseline])
    task['loginteraction_RF']=task.logratio_RF_cliff-task.logratio_RF_noncliff
    task['CheMeleon_cliff_penalty']=task.CheMeleon_cliff-task.CheMeleon_noncliff
    rng=np.random.default_rng(SEED);draws=rng.integers(0,len(task),size=(B,len(task)))
    results={}
    for baseline in ['RF','Chemprop']:
        results[baseline]={s:summarize(task['logratio_'+baseline+'_'+s].to_numpy(),draws) for s in ['total','cliff','noncliff']}
    logs=task.loginteraction_RF.to_numpy();boots=logs[draws].mean(axis=1)
    interaction={'ratio_of_ratios':float(np.exp(logs.mean())),'ratio_95ci':np.exp(interval(boots)).tolist(),
                 'definition':'(CheMeleon/RF on cliff) / (CheMeleon/RF on noncliff), geometric across tasks'}
    gap=task.CheMeleon_cliff_penalty.to_numpy();gap_boot=gap[draws].mean(axis=1)
    gap_summary={'mean_rmse_gap':float(gap.mean()),'mean_gap_95ci':interval(gap_boot),
                 'positive_gap_tasks':int((gap>0).sum()),'tasks':len(task)}
    # Exploratory fixed-budget strata, not a within-task learning curve.
    strata={}
    for label,mask in [('at_most_1000',task.n_train<=1000),('above_1000',task.n_train>1000)]:
        part=task[mask];idx=rng.integers(0,len(part),size=(B,len(part)))
        strata[label]=dict(n_train_min=int(part.n_train.min()),n_train_max=int(part.n_train.max()),
                          **summarize(part.logratio_RF_total.to_numpy(),idx))
    jackknife=[float(np.exp(np.delete(task.logratio_RF_total.to_numpy(),i).mean())) for i in range(len(task))]
    # Endpoint-name prefix sensitivity; does not establish full biological independence.
    prefix=task.index.to_series().str.split('_').str[0]
    groups=task.logratio_RF_total.groupby(prefix).mean();idx=rng.integers(0,len(groups),size=(B,len(groups)))
    sensitivity={'leave_one_task_out_ratio_range':[min(jackknife),max(jackknife)],
       'equal_name_prefix':dict(prefix_groups=len(groups),**summarize(groups.to_numpy(),idx)),
       'arithmetic_mean_total_RMSE':{m:float(task[m+'_total'].mean()) for m in MODELS}}
    # Additional released RF variants guard against using only one named baseline.
    sensitivity['other_published_RF_variants']={}
    for variant in ['RF_Morgan','RF_Mordred']:
        v=parse_results(variant)
        pooled=[]
        for row in v.itertuples():
            c=task.loc[row.benchmark]
            pooled.append(np.sqrt((c.n_cliff*row.cliff**2+c.n_noncliff*row.noncliff**2)/c.n_test))
        v['total_reconstructed']=pooled
        np.testing.assert_allclose(v.total_reconstructed,v.total,atol=5.1e-6,rtol=0)
        m=v.groupby('benchmark')[['total_reconstructed','cliff','noncliff']].mean().reindex(task.index)
        sensitivity['other_published_RF_variants'][variant]={}
        for label,col in [('total','total_reconstructed'),('cliff','cliff'),('noncliff','noncliff')]:
            logs=np.log(task['CheMeleon_'+label].to_numpy()/m[col].to_numpy())
            sensitivity['other_published_RF_variants'][variant][label]=summarize(logs,draws)
    # Seed ranges describe stochastic training variation on the same fixed test sets.
    seed_results=[]
    for seed,g in runs.groupby('seed'):
        pivot=g.pivot(index='benchmark',columns='model',values='total_reconstructed')
        seed_results.append(dict(seed=int(seed),geometric_ratio_RF=float(np.exp(np.log(pivot.CheMeleon/pivot.RF).mean()))))
    out=dict(source_commit=manifests[0]['commit'],assay_commit=manifests[1]['commit'],seed=SEED,bootstrap_draws=B,
       tasks=len(task),runs_per_model=150,replicates_per_task=5,seed_ids=sorted(runs.seed.unique().tolist()),
       estimand='Equal-task geometric mean of ratios of mean per-run RMSE on fixed released test sets.',
       uncertainty='Percentile task bootstrap; seeds are not independent tasks. Exploratory, not preregistered.',
       comparisons=results,interaction_RF=interaction,cliff_penalty=gap_summary,label_size_strata=strata,
       sensitivity=sensitivity,seed_sensitivity=seed_results,
       quality={'duplicate_model_task_seed':int(runs.duplicated(['model','benchmark','seed']).sum()),
                'required_missing':int(runs[['model','benchmark','seed','total','cliff','noncliff']].isna().sum().sum()),
                'training_size_range':[int(task.n_train.min()),int(task.n_train.max())],
                'pooled_RMSE_matches_rounded_author_overall':True,'subgroups_match_exported_CSV':True})
    task.to_csv(ROOT/'task-results.csv');runs.to_csv(ROOT/'run-results.csv',index=False)
    (ROOT/'results.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    make_figures(task,out)
    print(json.dumps(out,indent=2))

def make_figures(task,out):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    order=task.sort_values('logratio_RF_total');y=np.arange(len(order))
    fig,ax=plt.subplots(figsize=(8,8.5))
    for subset,marker,color,offset in [('total','o','#205c7a',0),('cliff','^','#a4592b',.20),('noncliff','s','#74854b',-.20)]:
        ax.scatter(np.exp(order['logratio_RF_'+subset]),y+offset,label=subset.capitalize(),s=25,marker=marker,color=color)
    ax.axvline(1,ls='--',color='.4');ax.set(yticks=y,yticklabels=[s.replace('CHEMBL','') for s in order.index],xlabel='Mean per-run RMSE ratio: CheMeleon / published RF',ylabel='MoleculeACE endpoint',title='Relative gains vary across tasks and activity-cliff subsets')
    ax.legend(frameon=False,loc='upper center',bbox_to_anchor=(.5,-.07),ncol=3);ax.invert_yaxis();fig.tight_layout()
    save(fig,'task-ratios')
    fig,axs=plt.subplots(1,2,figsize=(10,4.5))
    ax=axs[0]
    for j,subset in enumerate(['total','cliff','noncliff']):
        a=out['comparisons']['RF'][subset];v=a['geometric_rmse_ratio'];lo,hi=a['ratio_95ci'];ax.errorbar(v,j,xerr=[[v-lo],[hi-v]],fmt='o',color='#205c7a',capsize=4)
    ax.axvline(1,ls='--',color='.4');ax.set(yticks=range(3),yticklabels=['Total','Cliff','Noncliff'],xlabel='Geometric RMSE ratio: CheMeleon / RF',title='Equal-task effects, 95% task-bootstrap intervals')
    ax=axs[1];ax.scatter(task.n_train,np.exp(task.logratio_RF_total),color='#205c7a',s=28);ax.axhline(1,ls='--',color='.4');ax.axvline(1000,ls=':',color='.6');ax.set(xscale='log',xlabel='Released training-pool compounds',ylabel='Total RMSE ratio: CheMeleon / RF',title='Different tasks, not a learning curve')
    fig.tight_layout();save(fig,'aggregate-size')

def save(fig,name):
    import matplotlib.pyplot as plt
    for ext in ['png','svg']:
        f=ROOT/(name+'.'+ext);fig.savefig(f,dpi=180)
        if ext=='svg':f.write_text('\n'.join(s.rstrip() for s in f.read_text().splitlines())+'\n')
    plt.close(fig)

if __name__=='__main__':main()
