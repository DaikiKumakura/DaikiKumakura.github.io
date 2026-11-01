"""Arithmetic audit of reported aggregate medians; not a survival analysis."""
import csv
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    with (ROOT / 'cohort-medians.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    second = [r for r in rows if r['cohort'] == 'second-line']
    assert len(second) == 5 and len({r['target'] for r in second}) == 5
    result = {'method': 'Unweighted minima/maxima and overlapping-cohort arithmetic only; no causal comparison, pooling, hazard ratio, CI or statistical test computed.',
              'second_line_report_count': len(second), 'range_months': {}, 'within_report_differences_months': {}}
    for endpoint in ('pfs', 'os'):
        values = [Decimal(r[f'{endpoint}_months']) for r in second]
        result['range_months'][endpoint] = [str(min(values)), str(max(values))]
    for subset in second:
        parents = [r for r in rows if r['drug'] == subset['drug'] and r['cohort'] == 'mixed-line']
        if parents:
            parent, = parents
            result['within_report_differences_months'][subset['drug']] = {
                endpoint: str(Decimal(subset[f'{endpoint}_months']) - Decimal(parent[f'{endpoint}_months']))
                for endpoint in ('pfs', 'os')}
    (ROOT / 'summary.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
