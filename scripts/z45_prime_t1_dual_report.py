"""Compact, reproducible tables from the exact scan (no large allocations)."""
import json
from collections import Counter
from pathlib import Path
P=Path('data/z45_prime_t1_dual')
S=json.loads((P/'summary.json').read_text())
for fam in ['full8','full15','star','b1']:
    a=[r for r in S if r['family']==fam]
    f=Counter(); c=Counter()
    for r in a: f.update(r['counts']); c.update(r['control']['counts'])
    print(fam,'failure',dict(f),'control',dict(c))
    for r in a:
        print(r['n'],r['fibres'],r['counts'], 'best',r['best_quadratic'],
              'control',r['control']['n'],r['control']['best_quadratic'])
for n in [11,17,131,241]:
    rows=json.loads((P/f'full8_{n}.json').read_text())
    print('FULL8',n,'quadratic rows',[(r['x'],r['modulus'],r['quadratic']) for r in rows if r['quadratic']])
    print('first budget',next(r for r in rows if r['kind']=='budget'))
for fam,n in [('full15',137),('star',5569),('b1',66529)]:
    rows=json.loads((P/f'{fam}_{n}.json').read_text())
    print('HIGHER',fam,n,next(r for r in rows if r['kind']=='higher'))
print('FOREST')
for r in json.loads((P/'forest.json').read_text()):
    print(r['n'],r['root'],len(r['vertices']),r['component_edges'],r['component_good'],r['all_good'],r['component_colours'], 'nonunit',r['nonunit_edges'])
