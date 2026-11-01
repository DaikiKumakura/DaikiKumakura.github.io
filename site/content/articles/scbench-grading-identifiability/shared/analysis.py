"""Independent arithmetic model of published numeric grading conditions.

Python 3.10+; standard library only. No model, biological data, or vendor code.
The public configuration values are documented in REPRODUCE.md.
"""
from pathlib import Path
import csv,json,math,platform

ROOT=Path(__file__).resolve().parent
DE={'ground_truth':{'n_degs':1150},'tolerances':{'n_degs':350}}
QC={'ground_truth':{'median_genes_per_pbmc':68,'n_monocytes_pbmc':2592,'n_pbmcs_retained':14346},
    'tolerances':{'median_genes_per_pbmc':8,'n_monocytes_pbmc':1000,'n_pbmcs_retained':800}}

def numeric_check(answer,config):
    """Finite real numbers and symmetric absolute tolerances only.

    Not a reimplementation of parsing, extraction, all grader families, or harness.
    """
    for field,expected in config['ground_truth'].items():
        if field not in answer:return False
        value=answer[field]
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):return False
        if abs(value-expected)>config['tolerances'][field]:return False
    return True

def main():
    out=ROOT/'results';out.mkdir(exist_ok=True)
    rows=[{'n_degs':n,'passes_numeric_condition':numeric_check({'n_degs':n},DE)} for n in [799,800,1150,1500,1501]]
    assert [r['passes_numeric_condition'] for r in rows]==[False,True,True,True,False]
    # Artificial gene labels, not an inferred gene list from scBench data.
    first=set(range(1150));second=set(range(1150,2300));union=first|second
    result={'scope':'Published numeric conditions and artificial counterexamples; no biological or agent rerun',
       'python':platform.python_version(),'de_boundary_checks':rows,
       'set_counterexample':{'size_A':len(first),'size_B':len(second),'intersection':len(first&second),
       'union':len(union),'jaccard':len(first&second)/len(union),
       'answer_A_passes':numeric_check({'n_degs':len(first)},DE),'answer_B_passes':numeric_check({'n_degs':len(second)},DE)},
       'qc_same_summary':{'summary':QC['ground_truth'],'panel_aware_narrative_passes':numeric_check(dict(QC['ground_truth']),QC),
       'no_op_filter_narrative_passes':numeric_check(dict(QC['ground_truth']),QC),
       'note':'Narrative labels are not supplied to this numeric checker; this does not measure actual model reasoning.'},
       'missing_field_rejected':not numeric_check({},DE)}
    assert result['set_counterexample']['jaccard']==0 and result['missing_field_rejected']
    with(out/'de-boundaries.csv').open('w',newline='',encoding='utf-8')as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
