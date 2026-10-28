"""Stream the census; select adversarial inputs and summarize kernel diagnostics.
Run with uv run python; standard library only. Does not run C programs itself.
"""
from pathlib import Path
import csv
import gzip
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/z48_ltastra'


def rows(path):
    with path.open() as f:
        return list(csv.DictReader(line for line in f if not line.startswith('#')))


def main():
    census = rows(DATA / 'census.csv')
    failures = {key: [int(r['p']) for r in census if int(r[key]) == 0]
                for key in ('R', 'B', 'T')}
    selected = set(failures['R'] + failures['B'])
    selected.update(int(r['p']) for r in sorted(
        census, key=lambda r: int(r['T']) / math.log(int(r['p']))**2)[:32])
    for x in (1000, 10000, 100000, 1000000, 3000000, 9000000):
        selected.update(int(r['p']) for r in census if x < int(r['p']) < x + 1000)
    selected.update((9, 25, 49, 121, 961, 10201, 998001, 3161**2))
    (DATA / 'detail_inputs.txt').write_text(''.join(f'{n}\n' for n in sorted(selected)))
    minimum_bound = min(census, key=lambda r: int(r['T']) / float(r['MBM_upper']))
    assert all(16*int(r['T']) >= float(r['MBM_upper']) for r in census)
    result = {'census_size': len(census), 'failures': failures, 'bins': [], 'covers': [],
        'uniform_T_over_MBM_lower_bound': '1/16 (via outward upper bound)',
        'min_T_over_upper': {'p':int(minimum_bound['p']),
            'ratio':int(minimum_bound['T'])/float(minimum_bound['MBM_upper'])}}
    for lo, hi in ((0, 10000), (10000, 100000), (100000, 1000000), (1000000, 10000000)):
        block = [r for r in census if lo < int(r['p']) <= hi]
        low = min(block, key=lambda r: int(r['T']) / math.log(int(r['p']))**2)
        result['bins'].append({'range': [lo, hi], 'count': len(block),
            'min_T_log2': {'p': int(low['p']), 'R': int(low['R']), 'B': int(low['B']),
                'ratio': int(low['T']) / math.log(int(low['p']))**2},
            'mean_T_log2': sum(int(r['T']) / math.log(int(r['p']))**2 for r in block) / len(block),
            'Rzeros': sum(int(r['R']) == 0 for r in block),
            'Bzeros': sum(int(r['B']) == 0 for r in block)})
    for path in sorted(DATA.glob('cover_*.csv')):
        rr = rows(path)
        result['covers'].append({'Q': int(path.stem.split('_')[1]), 'cells': len(rr),
            'zero_R_cells': sum(int(r['minR']) == 0 for r in rr),
            'zero_T_masks': [int(r['mask']) for r in rr if int(r['minT']) == 0],
            'max_mean_at_zero_minT': max(float(r['meanR']) + float(r['meanB'])
                for r in rr if int(r['minT']) == 0)})
    if (DATA / 'detail.csv').exists():
        cr = {int(r['p']): r for r in census}
        detail = rows(DATA / 'detail.csv')
        for r in detail:
            n = int(r['n'])
            if n in cr:
                assert int(r['R']) == int(cr[n]['R']), (n, r, cr[n])
            if math.isqrt(n)**2 == n:
                for key in ('R', 'MBM', 'Mgen', 'Rsmall', 'M2small', 'M6small', 'M12small', 'M60small'):
                    assert float(r[key]) == 0, (n, key, r[key])
            assert float(r['M2small']) <= float(r['Mgen']) + 1e-8
        result['detail_rows'] = len(detail)
        result['hard_details'] = [r for r in detail if int(r['n']) in failures['R'] + failures['B']]
    full_path = DATA / 'census_mod4.csv.gz'
    if full_path.exists():
        blocks = {}
        full_count = 0
        cr = {int(r['p']): r for r in census}
        with gzip.open(full_path, 'rt') as f:
            for r in csv.DictReader(f):
                p,t = int(r['p']),int(r['T'])
                assert 16*t >= float(r['MBM_upper'])
                full_count += 1
                if p in cr:
                    assert r == cr[p], p
                j = p.bit_length()-1
                if not 8 <= j <= 22:
                    continue
                L = j*math.log(2)
                m = .15*L*L
                k = math.ceil(L/math.log(L))
                block = blocks.setdefault(j, {'X':2**j,'count':0,'k':k,'m':m,
                    'neg_sum':0.0,'abs_sum':0.0,'deficits':0})
                block['count'] += 1
                block['neg_sum'] += max(m-t,0)**(2*k)
                block['abs_sum'] += abs(m-t)**(2*k)
                block['deficits'] += t < m
        moment_rows = []
        for j,b in sorted(blocks.items()):
            k,m,n = b['k'],b['m'],b['count']
            moment_rows.append({'X':b['X'],'count':n,'k':k,'m':m,'deficits':b['deficits'],
                'empirical_C_negative':(b['neg_sum']/n)**(1/k)/(k*m),
                'empirical_C_absolute':(b['abs_sum']/n)**(1/k)/(k*m)})
        result['full_mod4_count'] = full_count
        result['moment_diagnostic'] = {'c':.15,'leading_order_constant':1.0,
            'normalization':'number of p=1 mod4 in block, smaller than pi(2X)',
            'rows':moment_rows}
    (DATA / 'summary.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2) if '--verbose' in sys.argv else
          f"{len(census)} census rows, {len(selected)} selected inputs; summary.json updated")


if __name__ == '__main__':
    main()
