"""Expected shared detections in a hypothetical proteomics comparison.

Not fitted to scpLASP data. N=8000 is an illustrative universe, not a human
proteome estimate. Detection is homogeneous and independent across cells.
"""
from pathlib import Path
from itertools import product
import csv


def shared(n, p, cells):
    if n < 0 or not 0 <= p <= 1 or cells < 1:
        raise ValueError('Invalid universe, probability or cell count')
    return n * p ** cells


def main():
    n=8000
    for p in (0,0.5,0.75,0.9,1):
        enumerated = sum(
            (p if x else 1-p) * (p if y else 1-p) * (x*y)
            for x,y in product((0,1),repeat=2)
        )
        assert abs(shared(n,p,2)-n*enumerated) < 1e-9
        assert all(shared(n,p,m+1) <= shared(n,p,m)+1e-9 for m in range(1,10))
        assert all(0 <= shared(n,p,m) <= n for m in (1,2,10))
    assert shared(n,0,10)==0
    assert shared(n,1,10)==n
    with Path(__file__).with_name('table1.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['hypothetical_universe','detection_probability','one_cell_expected','two_cells_shared_expected','ten_cells_shared_expected'])
        for p in (0.5,0.75,0.9):
            writer.writerow([n,format(p,'.2f'),*[format(shared(n,p,m),'.1f') for m in (1,2,10)]])
    print('table1.csv written; enumeration, boundary and monotonicity checks passed')


if __name__ == '__main__':
    main()
