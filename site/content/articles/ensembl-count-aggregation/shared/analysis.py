"""Deterministic counting counterexamples; Python 3.10+, standard library only.

Run: python analysis.py
All molecule IDs, gene labels and counts are synthetic. No mapping API is called.
"""
from pathlib import Path
import csv
import json
import platform


def main():
    out = Path(__file__).resolve().parent / 'results'
    out.mkdir(exist_ok=True)
    # Sets refer to already deduplicated molecule identities within one cell.
    cases = {
        'disjoint': (set(range(8)), set(range(8, 13))),
        'overlap': (set(range(8)), set(range(4, 9))),
        'duplicated': (set(range(8)), set(range(8))),
    }
    rows = []
    for name, (a, b) in cases.items():
        row = dict(case=name, row_a=len(a), row_b=len(b),
                   naive_sum=len(a)+len(b), shared=len(a & b),
                   distinct_molecules=len(a | b))
        assert row['distinct_molecules'] == row['naive_sum']-row['shared']
        rows.append(row)
    # A duplicated target row exists only in cell 1; real target/background equal.
    target = [10, 10]
    background = [90, 90]
    displayed = [target[0], target[1]*2]
    libraries = [displayed[i]+background[i] for i in range(2)]
    cpt = [displayed[i]/libraries[i]*10000 for i in range(2)]
    bg_cpt = [background[i]/libraries[i]*10000 for i in range(2)]
    # Gene-length normalization and aggregation differ when lengths differ.
    counts = [8, 5]
    lengths_kb = [1, 2]
    before = sum(c/l for c, l in zip(counts, lengths_kb))
    arbitrary_after = sum(counts)/1.5
    result = {
        'data_type': 'synthetic deterministic examples, not biological observations',
        'python': platform.python_version(),
        'set_examples': rows,
        'duplicate_bias': {'true_target': target, 'background': background,
                           'displayed_target': displayed,
                           'displayed_library': libraries, 'target_per_10000': cpt,
                           'background_per_10000': bg_cpt,
                           'apparent_fold_change': cpt[1]/cpt[0]},
        'length_example': {'counts': counts, 'lengths_kb': lengths_kb,
                           'normalize_then_sum': before,
                           'sum_then_divide_by_arbitrary_1_5_kb': arbitrary_after},
    }
    assert [r['distinct_molecules'] for r in rows] == [13, 9, 8]
    assert abs(result['duplicate_bias']['apparent_fold_change']-20/11)<1e-12
    assert before == 10.5
    with (out/'set-examples.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    (out/'results.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
