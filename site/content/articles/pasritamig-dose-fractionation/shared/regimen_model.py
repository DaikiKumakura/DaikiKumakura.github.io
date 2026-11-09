"""Conditional regimen comparison. No fitting or patient-level prediction.

Python 3.12; matplotlib 3.9.1. Execute: python regimen_model.py
Linear time-invariant impulse responses are normalized to unit total AUC.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LN2 = math.log(2)
HALF_LIVES = [13.8, 15.2, 16.5, 18.3]  # Separate reported summaries, not a CI.


def kernel(half, fast_fraction=0, fast_half=1):
    """AUC weights, not concentration amplitudes. Fast terms are hypothetical."""
    return [(1-fast_fraction, LN2/half), (fast_fraction, LN2/fast_half)]


def cumulative(age, terms):
    return sum(w*(-math.expm1(-rate*age)) for w, rate in terms) if age > 0 else 0.0


def area(doses, horizon, terms):
    return sum(dose*cumulative(horizon-day, terms) for day, dose in doses if day < horizon)


def concentration(t, doses, terms):
    return sum(dose*w*rate*math.exp(-rate*(t-day))
               for day, dose in doses if day <= t for w, rate in terms)


def steady(t, interval, terms):
    """Concentration / common maintenance mean; t is phase within the interval."""
    return interval*sum(w*rate*math.exp(-rate*t)/(-math.expm1(-rate*interval))
                        for w, rate in terms)


def above(threshold, interval, half):
    rate = LN2/half
    peak = rate*interval/(-math.expm1(-rate*interval))
    return max(0.0, min(1.0, math.log(peak/threshold)/(rate*interval)))


def comparison(half, fast_fraction=0, fast_half=1):
    terms = kernel(half, fast_fraction, fast_half)
    # Day 1 = t0; Day 8 = t7; Day 15 = t14; Day 57 = t56.
    # The endpoint dose contributes zero area to the [0,56] window.
    step = [(0,3.5),(7,18)]
    reference = step+[(14,300),(56,300)]
    split = step+[(14,150),(35,150),(56,150)]
    full_load = step+[(14,300),(35,150),(56,150)]
    matched_first = 300-150*cumulative(21,terms)/cumulative(42,terms)
    matched = step+[(14,matched_first),(35,150),(56,150)]
    base_area = area(reference,56,terms)
    return dict(half_life_days=half, fast_auc_fraction=fast_fraction,
                hypothetical_fast_half_days=fast_half,
                steady_peak_ratio=steady(0,21,terms)/steady(0,42,terms),
                steady_trough_ratio=steady(21,21,terms)/steady(42,42,terms),
                early_auc_split_ratio=area(split,56,terms)/base_area,
                early_auc_full_load_ratio=area(full_load,56,terms)/base_area,
                matched_first_target_mg=matched_first,
                matched_auc_ratio=area(matched,56,terms)/base_area,
                # Include exact inputs and normalized-AUC values for arithmetic checks.
                reference_doses=reference, split_doses=split,
                full_load_doses=full_load, matched_doses=matched,
                reference_normalized_auc=base_area)


def calculate():
    mono = [comparison(half) for half in HALF_LIVES]
    sensitivity = [comparison(h,f,fast) for h in HALF_LIVES
                   for f in [0,.25,.5] for fast in [1,3]]
    thresholds = [.5,1,1.5,2]
    central = 15.2
    return {
        'assumptions': ['Instantaneous IV input', 'Linear time-invariant PK',
                        'Nonnegative exponential components', 'No PK/PD fitting',
                        'No JNJ-9401 PK inferred'],
        'maintenance': {'reference_mg':300,'reference_interval_days':42,
                        'split_mg':150,'split_interval_days':21,
                        'common_rate_mg_day':300/42},
        'window': {'origin':'Day 1 = t0','horizon_days':56,
                   'target_start_days':14,'stepup_mg':[3.5,18],'stepup_days':[0,7]},
        'reported_half_life_scenarios':mono,
        'hypothetical_distribution_sensitivity':sensitivity,
        'central_half_life_days':central,
        'threshold_scenarios':[
            {'threshold_over_steady_mean':z,
             'reference_fraction_above':above(z,42,central),
             'split_fraction_above':above(z,21,central)} for z in thresholds],
        'interpretation':'These are conditional design calculations, not actual pasritamig '
                         'or combination exposure predictions or dose recommendations.'
    }


def plot(out):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                         'axes.spines.top':False,'axes.spines.right':False})
    fig, ax = plt.subplots(1,2,figsize=(10.4,4.4))
    terms = kernel(15.2)
    ts = [42*i/1200 for i in range(1200)]
    ax[0].plot(ts,[steady(t,42,terms) for t in ts],color='#225b78',
               label='300 mg every 6 weeks')
    ax[0].plot(ts,[steady(t%21,21,terms) for t in ts],color='#af5629',ls='--',
               label='150 mg every 3 weeks')
    ax[0].axhline(1,color='.5',lw=1,ls=':')
    ax[0].set(xlabel='Phase in 6-week period (days)',
              ylabel='Concentration / common steady mean',
              title='A. Equal maintenance dose rate')
    ax[0].legend(frameon=False,fontsize=9)
    thresholds = [0.1+i*.01 for i in range(300)]
    ax[1].plot(thresholds,[above(z,42,15.2)*100 for z in thresholds],
               color='#225b78',label='Every 6 weeks')
    ax[1].plot(thresholds,[above(z,21,15.2)*100 for z in thresholds],
               color='#af5629',ls='--',label='Half-dose every 3 weeks')
    ax[1].set(xlabel='Hypothetical threshold / common steady mean',
              ylabel='Time above threshold (%)',ylim=(-2,102),
              title='B. Threshold-dependent ordering')
    ax[1].legend(frameon=False,fontsize=9)
    fig.suptitle('Conditional monoexponential model; half-life 15.2 days',fontsize=13)
    fig.tight_layout(rect=(0,0,1,.95))
    for ext in ['png','svg']:
        fig.savefig(ROOT/f'regimen-steady.{ext}',dpi=180)
    plt.close(fig)

    fig,ax = plt.subplots(1,2,figsize=(10.4,4.4))
    central=out['reported_half_life_scenarios'][1]
    curves=[('Reference: 300 mg Q6W','reference_doses','#225b78','-'),
            ('150 mg Q3W from first target dose','split_doses','#af5629','--'),
            ('Matched first dose, then 150 mg Q3W','matched_doses','#38734a',':')]
    # Divide by a common reference steady mean; no absolute concentration asserted.
    mean=300/42
    times=sorted(set([i/20 for i in range(1121)]+[7,14,35,56]))
    for label,key,color,ls in curves:
        doses=central[key]
        ax[0].plot(times,[concentration(t,doses,terms)/mean for t in times],
                   color=color,ls=ls,label=label)
    ax[0].set(xlabel='Days since first step-up (Day 1 = 0)',
              ylabel='Concentration / reference steady mean',
              title='A. First 56 days; hypothetical profiles')
    ax[0].legend(frameon=False,fontsize=8)
    for f,style in [(0,'-'),(.25,'--'),(.5,':')]:
        hs=[12+i*.1 for i in range(101)]
        vals=[comparison(h,f,1)['early_auc_split_ratio'] for h in hs]
        ax[1].plot(hs,vals,ls=style,label=f'Fast AUC fraction {f:g}')
    ax[1].axhline(1,color='.5',lw=1,ls=':')
    ax[1].set(xlabel='Slow-component half-life (days)',
              ylabel='First-56-day AUC ratio: split / reference',
              ylim=(.78,1.02), title='B. Structural sensitivity (fast half-life 1 day)')
    ax[1].legend(frameon=False,fontsize=9)
    fig.suptitle('Initial exposure is a different comparison from maintenance mean',fontsize=13)
    fig.tight_layout(rect=(0,0,1,.95))
    for ext in ['png','svg']:
        fig.savefig(ROOT/f'regimen-early.{ext}',dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    result=calculate()
    (ROOT/'regimen-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    plot(result)
    print(json.dumps(result['reported_half_life_scenarios'],indent=2))
