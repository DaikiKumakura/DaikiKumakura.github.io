"""Recalculate aggregate counts and logical examples; no model or raw corpus."""
import csv
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'

def main():
    n, agree = 10972, 8566
    disagree = n - agree
    q = Fraction(agree, n)
    cases = [
        dict(scenario='both_correct_on_agreement_neither_on_disagreement',
             agreement_both_correct=agree, disagreement_a_correct=0, disagreement_b_correct=0),
        dict(scenario='agreement_wrong_neither_correct_elsewhere',
             agreement_both_correct=0, disagreement_a_correct=0, disagreement_b_correct=0),
        dict(scenario='agreement_correct_a_correct_on_all_disagreements',
             agreement_both_correct=agree, disagreement_a_correct=disagree, disagreement_b_correct=0),
        dict(scenario='agreement_correct_b_correct_on_all_disagreements',
             agreement_both_correct=agree, disagreement_a_correct=0, disagreement_b_correct=disagree),
    ]
    for row in cases:
        assert 0 <= row['agreement_both_correct'] <= agree
        assert row['disagreement_a_correct'] + row['disagreement_b_correct'] <= disagree
        row['a_correct'] = row['agreement_both_correct'] + row['disagreement_a_correct']
        row['b_correct'] = row['agreement_both_correct'] + row['disagreement_b_correct']
        pa, pb = Fraction(row['a_correct'],n), Fraction(row['b_correct'],n)
        assert pa + pb <= 1 + q
        assert abs(pa - pb) <= 1 - q
        row['a_accuracy'] = float(pa)
        row['b_accuracy'] = float(pb)
    OUT.mkdir(exist_ok=True)
    with (OUT/'logical-cases.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(cases[0]))
        writer.writeheader(); writer.writerows(cases)
    result=dict(matched_measurements=n, agreement=agree, disagreement=disagree,
                agreement_fraction=float(q), disagreement_fraction=float(1-q),
                crossover_multiplier=float(q/(1-q)),
                interpretation='Logical constructions, not observed extraction accuracy or prediction loss.')
    (OUT/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
