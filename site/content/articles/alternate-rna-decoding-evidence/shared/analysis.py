"""Audit observation units and overlap in published supplementary tables.

Read-only XLSX extraction; no spectra, DNA or RNA sequences are reanalysed.
Run fetch_supplement.py first, then python analysis.py.
"""
from pathlib import Path
import collections,csv,hashlib,json,platform
import openpyxl

ROOT=Path(__file__).resolve().parent
SOURCES=ROOT/'sources'
OUT=ROOT/'results'

def load(number):
    path=next(SOURCES.glob(f'Supplementary_Data_{number}.*.xlsx'))
    book=openpyxl.load_workbook(path,read_only=True,data_only=True)
    values=book['Sheet1'].iter_rows(values_only=True)
    headers=next(values)
    rows=[dict(zip(headers,row)) for row in values]
    assert all(isinstance(r['SAAP'],str) and isinstance(r['BP'],str) and isinstance(r['Dataset'],str) for r in rows)
    return path,rows

def pair(row):return row['SAAP'],row['BP']
def observation(row):return row['Dataset'],row['SAAP'],row['BP'],str(row['TMT/Tissue']),row['Digest']

def main():
    OUT.mkdir(exist_ok=True)
    loaded={n:load(n) for n in [2,3,8]}
    data={n:x[1] for n,x in loaded.items()}
    sets={n:set(map(pair,rows)) for n,rows in data.items()}
    key3=set(map(observation,data[3]));key8=set(map(observation,data[8]))
    assert key8<=key3,'Table 8 observations are not contained in Table 3'
    inter=sets[2]&sets[8];extra=sets[8]-sets[2]
    by_dataset=[]
    for ds in sorted({r['Dataset'] for r in data[2]}|{r['Dataset'] for r in data[8]}):
        sub2=[r for r in data[2] if r['Dataset']==ds];sub8=[r for r in data[8] if r['Dataset']==ds]
        by_dataset.append(dict(dataset=ds,table2_rows=len(sub2),table8_rows=len(sub8),table8_unique_pairs=len(set(map(pair,sub8))),table8_pairs_absent_from_table2=len(set(map(pair,sub8))-sets[2])))
    table_counts=[dict(table=n,rows=len(data[n]),unique_sequence_pairs=len(sets[n]),unique_dataset_sequence_pairs=len({(r['Dataset'],*pair(r)) for r in data[n]})) for n in [2,3,8]]
    summary={
        'scope':'Published spreadsheet audit only, not validation of mass spectra or translation mechanisms',
        'pair_key':['SAAP','BP'],
        'table3_and_8_observation_key':['Dataset','SAAP','BP','TMT/Tissue','Digest'],
        'table_counts':table_counts,
        'overlap':{'table2_and_table8':len(inter),'table2_only':len(sets[2]-sets[8]),'table8_only':len(extra),'table8_only_rows':sum(pair(r) in extra for r in data[8])},
        'table8_all_observations_present_in_table3':True,
        'table3_to_8_row_retention_percent':100*len(data[8])/len(data[3]),
        'table3_to_8_pair_retention_percent':100*len(sets[8])/len(sets[3]),
        'table8_exported_probability_equal_0_9_rows':sum(r['Positional probability']==.9 for r in data[8]),
        'table8_exported_probability_below_0_9_rows':sum(isinstance(r['Positional probability'],(int,float)) and r['Positional probability']<.9 for r in data[8]),
        'sources':{str(n):{'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}for n,(path,rows) in loaded.items()},
        'environment':{'python':platform.python_version(),'openpyxl':openpyxl.__version__},
    }
    assert sum(r['table2_rows'] for r in by_dataset)==len(data[2])
    assert sum(r['table8_rows'] for r in by_dataset)==len(data[8])
    assert len(inter)+len(extra)==len(sets[8])
    assert len(inter)+len(sets[2]-sets[8])==len(sets[2])
    for name,rows in [('table-counts.csv',table_counts),('dataset-counts.csv',by_dataset)]:
        with (OUT/name).open('w',newline='',encoding='utf-8')as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
