"""Descriptive cross-source ratios, not patient-level external validation.

Run from the original restart-analysis ZIP's extracted folder, or supply
the path to outputs/results.json as the first argument. Uses standard Python.
Reported phase 1 values are geometric means from the cited abstracts.
"""
from pathlib import Path
import json
import math
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('outputs/results.json')
b = json.loads(path.read_text(encoding='utf-8'))['benchmark']
studies = {
    'Japan n=6': (10400, 18310, 630.9, 1056),
    'China n=9': (9575, 18340, 633.2, 1035),
}
for name, (a1, ar, c1, cr) in studies.items():
    print(name)
    print('repeated/first AUC, Cmax:', ar/a1, cr/c1)
    print('model/observed first AUC, Cmax:', b['typical_auc_first']/a1,
          b['typical_cmax_first']/c1)
    print('model periodic/observed repeated AUC, Cmax:',
          b['typical_auc_periodic']/ar, b['typical_cmax_periodic']/cr)
    print('first/repeated AUC (conditional inverse-accumulation illustration):', a1/ar)
print('model inverse AUC accumulation:', 1/b['typical_accum_auc'])
print('label inverse AUC accumulation (rounded):', 1/1.4)
print('lognormal arithmetic/central AUC factor:', math.exp(0.192/2))
print('Cross-source ratios do not identify restart prediction bias.')
