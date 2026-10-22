"""Build the data file of the anti-PD-1 exposure explorer from the companion zip of the article.

The explorer only re-presents numbers that the article's analysis already computed
(results/*.csv in the zip); nothing is recalculated here.

    python make_tool_data.py
"""
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
ZIP = BASE / 'content/articles/fixed-vs-weight-dosing/shared/fixed-vs-weight-dosing-companion.zip'
OUT = BASE / 'assets/tools/anti-pd1-exposure-data.json'

BANDS = ['<50', '50-60', '60-80', '80-100', '100-120', '120-150', '>=150']
LOWER = [0, 50, 60, 80, 100, 120, 150]


def read_csv(archive, name):
    with archive.open('results/' + name) as handle:
        return list(csv.DictReader(io.TextIOWrapper(handle, encoding='utf-8')))


def number(value, digits):
    return round(float(value), digits)


def build():
    raw = ZIP.read_bytes()
    archive = zipfile.ZipFile(io.BytesIO(raw))
    bands, thresholds, extremes, population = (read_csv(archive, n) for n in ('bands.csv', 'thresholds.csv', 'extreme-weights.csv', 'population-weights.csv'))
    cavg = read_csv(archive, 'posthoc-cavg.csv')
    data = dict(source=dict(file=ZIP.name, sha256=hashlib.sha256(raw).hexdigest()), bands=BANDS, lower=LOWER, drugs={})
    for row in bands:
        drug = data['drugs'].setdefault(row['drug'], dict(scenarios={}, thresholds={}, extremes=[], regimens=[]))
        scenario = drug['scenarios'].setdefault(row['scenario'], {})
        if row['regimen'] not in drug['regimens']:
            drug['regimens'].append(row['regimen'])
        scenario.setdefault(row['band'], {})[row['regimen']] = dict(
            below=number(row['below_floor'], 6), above=number(row['above_ceiling'], 6), first=number(row['below_floor_cycle1'], 6),
            n=int(row['n']), cmin=number(row['cmin_ss'], 2), cavg=number(row['cavg_ss'], 2), cmax=number(row['cmax_ss'], 2))
    for row in thresholds:
        data['drugs'][row['drug']]['thresholds'][row['scenario']] = dict(floor=number(row['floor'], 2), first=number(row['floor1'], 2), ceiling=number(row['ceiling'], 1))
    for row in extremes:
        data['drugs'][row['drug']]['extremes'].append(dict(regimen=row['regimen'], wt=int(row['wt']), below=number(row['below_floor'], 6), above=number(row['above_ceiling'], 6), first=number(row['below_floor_cycle1'], 6)))
    data['cavg'] = {}
    for row in cavg:
        entry = data['cavg'].setdefault(row['drug'], dict(floor=number(row['cavg_floor'], 2), rows={}))
        entry['rows'].setdefault(row['band'], {})[row['regimen']] = number(row['below_cavg_floor'], 6)
    data['population'] = {row['population']: {k: float(v) for k, v in row.items() if k != 'population'} for row in population}
    for name, drug in data['drugs'].items():
        for scenario, table in drug['scenarios'].items():
            assert set(table) == set(BANDS), (name, scenario)
    return data


if __name__ == '__main__':
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('wrote', OUT.relative_to(BASE), OUT.stat().st_size, 'bytes')
