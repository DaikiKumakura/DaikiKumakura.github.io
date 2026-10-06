"""Synthetic counterexample, not a reproduction of the competition pipeline.

Run: python toy_metrics.py
Requires NumPy and Pillow. All arrays represent control-relative effects.
"""
from pathlib import Path
import csv
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
TRUTH = np.array([[-5, 0, 0, 1, 0], [0, -5, 0, 0, 1], [0, 0, -5, -1, -1]], float)
SPIKE = np.array([[0, 10, 10, 0, 0], [10, 0, 10, 0, 0], [10, 10, 0, 0, 0]], float)
DOWNSTREAM = TRUTH.copy()
DOWNSTREAM[:, :3] = 0
MODELS = {'Control / zero': np.zeros_like(TRUTH), 'Other-target spike': SPIKE,
          'Downstream oracle': DOWNSTREAM, 'Perfect oracle': TRUTH.copy()}

def distance(a, b):
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    return 1.0 if denominator == 0 else float(1 - np.clip(a @ b / denominator, -1, 1))

def win(own, competitor):
    if np.isclose(own, competitor, atol=1e-12, rtol=0):
        return 0.5
    return float(own < competitor)

def score(pred, truth, scope):
    n, g = truth.shape
    outcomes = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                continue
            keep = np.ones(g, bool)
            if scope == 'row':
                keep[i] = False
            elif scope == 'panel':
                keep[:n] = False
            elif scope == 'pairwise':
                keep[[i, j]] = False
            else:
                raise ValueError(scope)
            row.append(win(distance(pred[i, keep], truth[i, keep]),
                           distance(pred[i, keep], truth[j, keep])))
        outcomes.append(float(np.mean(row)))
    return float(np.mean(outcomes))

def font(size):
    for name in ['C:/Windows/Fonts/arial.ttf', 'DejaVuSans.ttf']:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default(size=size)

def figures(rows):
    out = ROOT / 'figures'
    out.mkdir(exist_ok=True)
    im = Image.new('RGB', (1400, 680), 'white')
    d = ImageDraw.Draw(im)
    d.text((45, 25), 'Synthetic effects: same target list, no downstream prediction', fill='#172b4d', font=font(30))
    for panel, (title, matrix) in enumerate([('Observed effects', TRUTH), ('Other-target spike', SPIKE)]):
        x0 = 75 + panel * 685
        d.text((x0, 100), title, fill='#172b4d', font=font(27))
        for k, label in enumerate(['A', 'B', 'C', 'D', 'E']):
            d.text((x0 + 75 + k * 96, 158), label, fill='#172b4d', font=font(23))
        for i in range(3):
            d.text((x0 - 35, 233 + i * 104), 'ABC'[i], fill='#172b4d', font=font(24))
            for k in range(5):
                value = matrix[i, k]
                color = '#2d6096' if value < 0 else '#a34d24' if value > 0 else '#eff2f6'
                x, y = x0 + 48 + k * 96, 207 + i * 104
                d.rectangle((x, y, x + 88, y + 94), fill=color)
                d.text((x + 29, y + 33), f'{value:g}', fill='white' if value else '#172b4d', font=font(25))
    d.text((45, 570), 'Rows: perturbation targets. Columns A-C: panel targets; D-E: downstream genes.', fill='#34445c', font=font(23))
    d.text((45, 615), 'Arbitrary control-relative units; constructed example, not experimental measurements.', fill='#34445c', font=font(23))
    im.save(out / 'toy-effects.png')
    im = Image.new('RGB', (1400, 800), 'white')
    d = ImageDraw.Draw(im)
    d.text((45, 25), 'An uninformative spike wins under the row-mask rule', fill='#172b4d', font=font(30))
    colors = ['#a34d24', '#2d6096', '#327862']
    for q, label in enumerate(['Row mask', 'Panel mask', 'Pairwise mask']):
        x = 430 + q * 290
        d.text((x, 107), label, fill=colors[q], font=font(24))
    for r, row in enumerate(rows):
        y = 185 + r * 125
        d.text((45, y + 13), row['model'], fill='#172b4d', font=font(25))
        for q, scope in enumerate(['row', 'panel', 'pairwise']):
            x = 430 + q * 290
            d.rectangle((x, y, x + 205, y + 42), fill='#eff2f6')
            d.rectangle((x, y, x + 205 * row[scope], y + 42), fill=colors[q])
            d.text((x + 213, y + 8), f"{row[scope]:.2f}", fill='#172b4d', font=font(22))
    d.text((45, 700), 'Each bar uses the same 0-1 scale. Ties count as 0.5; zero-vector cosine distance is 1.', fill='#34445c', font=font(23))
    d.text((45, 748), 'Oracles use synthetic truth and are positive controls, not trained forecasting models.', fill='#34445c', font=font(23))
    im.save(out / 'toy-scores.png')

def main():
    rows = [{'model': name, **{s: score(pred, TRUTH, s) for s in ['row', 'panel', 'pairwise']}}
            for name, pred in MODELS.items()]
    assert rows[1]['row'] == 1 and rows[1]['panel'] == rows[1]['pairwise'] == 0.5
    assert all(rows[-1][s] == rows[-2][s] == 1 for s in ['row', 'panel', 'pairwise'])
    # Common profiles must average to 0.5 when every head-to-head comparison uses symmetric coordinates.
    rng = np.random.default_rng(20261006)
    for _ in range(100):
        common = np.repeat(rng.normal(size=(1, 5)), 3, axis=0)
        assert np.isclose(score(common, TRUTH, 'panel'), 0.5)
        assert np.isclose(score(common, TRUTH, 'pairwise'), 0.5)
    with (ROOT / 'toy-results.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['model', 'row', 'panel', 'pairwise'])
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / 'toy-data.json').write_text(json.dumps({'truth': TRUTH.tolist(), 'spike': SPIKE.tolist(),
        'targets': ['A', 'B', 'C'], 'genes': ['A', 'B', 'C', 'D', 'E']}, indent=2) + '\n', encoding='utf-8')
    figures(rows)
    print(json.dumps(rows, indent=2))
    print('Synthetic checks passed, including 100 shared-profile controls.')

if __name__ == '__main__':
    main()
