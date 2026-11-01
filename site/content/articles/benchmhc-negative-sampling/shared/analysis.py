"""Analytical shortcut example, not a reproduction of BenchMHC.

Python standard library only. Writes table1.csv next to this file.
The a,b values are conditional inputs; output AUCs are not observed model scores.
"""
from pathlib import Path
from itertools import product
import csv


def binary_auc(a, b):
    """AUC for score Z in {0,1}; ties receive 1/2 credit."""
    if not (0 <= a <= 1 and 0 <= b <= 1):
        raise ValueError("Probabilities must be in [0,1]")
    return 0.5 + 0.5 * (a - b)


def enumerated_auc(a, b):
    return sum(
        (a if pos else 1-a) * (b if neg else 1-b)
        * (1 if pos > neg else 0.5 if pos == neg else 0)
        for pos, neg in product((0, 1), repeat=2)
    )


def main():
    for a, b in product((0, 0.12, 0.5, 0.86, 0.99, 1), repeat=2):
        assert abs(binary_auc(a,b)-enumerated_auc(a,b)) < 1e-12
        assert 0 <= binary_auc(a,b) <= 1
        assert abs(binary_auc(a,a)-0.5) < 1e-12
    assert binary_auc(1,0) == 1
    assert binary_auc(0,1) == 0
    rows = [
        ('reported_lower', 0.86, 0.12),
        ('reported_upper', 0.99, 0.12),
        ('hypothetical_matched', 0.86, 0.86),
        ('hypothetical_all_match', 1.00, 1.00),
    ]
    with Path(__file__).with_name('table1.csv').open('w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['condition','positive_match_probability','decoy_match_probability','roc_auc'])
        for name,a,b in rows:
            writer.writerow([name,format(a,'.2f'),format(b,'.2f'),format(binary_auc(a,b),'.3f')])
    print('table1.csv written; analytical identity and boundary checks passed')


if __name__ == '__main__':
    main()
