"""Independent CFk AND CFh period-normalisation diagnostic, prime-cluster delta SE.
Usage: timeout 600 uv run python this.py raw_ph3_H.jsonl.gz raw_ph3_C.jsonl.gz
Memory O(number of primes/records), not O(sum of periods). No PARI required.
This is a diagnostic, not a correctly specified probabilistic CF model.
"""
import collections
import functools
import gzip
import json
import math
import sys

@functools.lru_cache(maxsize=50000)
def period(n):
    a0 = math.isqrt(n)
    m, d, a, length = 0, 1, a0, 0
    while True:
        m = d*a-m
        d = (n-m*m)//d
        a = (a0+m)//d
        length += 1
        if a == 2*a0:
            return length

for fn in sys.argv[1:]:
    D = {fam: collections.defaultdict(lambda: [0.,0.,0.,0.]) for fam in ('CFk','CFh')}
    with gzip.open(fn,'rt') as stream:
        for line in stream:
            r = json.loads(line)
            if r['p'] < 10000 or not r['ph']: continue
            K = len(r['ph']); f = r['f']
            er = period(r['p'])/f
            ep = sum(period(ph['q']) for ph in r['ph'])/K/f
            for fam, out in D.items():
                key=f'{fam}:divf'
                vals = [r['real'].get(key,0), sum(ph['h'].get(key,0) for ph in r['ph'])/K, er, ep]
                v=out[r['p']]
                for i in range(4): v[i] += vals[i]
    print(fn)
    for fam, out in D.items():
        R,P,ER,EP=[sum(v[i] for v in out.values()) for i in range(4)]
        # log[(R/ER)/(P/EP)], influence of each independent prime cluster.
        lr=math.log(R/ER)-math.log(P/EP)
        se=math.sqrt(sum((r/R-er/ER-p/P+ep/EP)**2 for r,p,er,ep in out.values()))
        print(fam, f'obs {R:.1f}/{P:.1f}; exposure {ER:.2f}/{EP:.2f}; rates {R/ER:.4f}/{P/EP:.4f};',
              f'normalised ratio {math.exp(lr):.4f}; diagnostic 2SE CI [{math.exp(lr-2*se):.4f},{math.exp(lr+2*se):.4f}]')
