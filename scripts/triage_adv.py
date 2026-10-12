"""O157 independent, bounded spot checks; no full large-prime counter rerun.
Run: ulimit -v 4000000; timeout 600 env OPENBLAS_NUM_THREADS=1
     OMP_NUM_THREADS=1 PYTHONPATH=scripts uv run python scripts/triage_adv.py
The O154 validation already compares full counts; here check claims, slices,
and independently reproject the read-only feature cache (not a raw-data rerun).
"""
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
from sympy import divisors, factorint, isprime, primerange


def slice_solutions(p, e):
    assert (p + e) % 4 == 0
    n = (p + e) // 4
    for a in divisors(n):
        if a * a > n:
            continue
        for b in divisors(n // a):
            if b < a or (a + b) % e:
                continue
            c, d = (a + b) // e, n // (a * b)
            if math.gcd(a, c) == 1:
                assert Fraction(4, p) == (Fraction(1, a*b*d)
                    + Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p))
                yield int(a), int(b), int(c), int(d)


# Re-derive the {a,c} identity independently over a small box.
checks = 0
for p in primerange(5, 200):
    for a in range(1, 9):
        for c in range(1, 9):
            for d in range(1, 9):
                f = 4*a*c*d - 1
                assert ((p + 4*a*a*d) % f == 0) == ((c*p + a) % f == 0)
                assert c*(p + 4*a*a*d) - a*f == c*p + a
                if (c*p + a) % f == 0:
                    b = (c*p + a) // f
                    assert (a+b) % c == 0
                    assert 4*a*b*d == p + (a+b)//c
                checks += 1
print('slice identity checks:', checks)

# D3 is not a consequence of primality of N_e.
p, e = 433, 19
assert isprime(p) and isprime((p+e)//4) and p % 24 == 1
print('prime-shift counterexample:', p, e, (p+e)//4, list(slice_solutions(p, e)))

# Recheck claimed empty slices and least witness of the highlighted prime.
p = 1180607468041
assert isprime(p)
small = {e: list(slice_solutions(p, e)) for e in range(3, 48, 4)}
assert all(not v for e, v in small.items() if e < 47)
assert small[47]
witnesses = []
for f in range(3, 48, 4):
    for a in divisors((f+1)//4):
        for c in divisors((f+1)//(4*a)):
            d = (f+1)//(4*a*c)
            if math.gcd(a, c) == 1 and (c*p+a) % f == 0:
                b = (c*p+a)//f
                if b >= a:
                    witnesses.append((f, int(a), int(b), int(c), int(d)))
assert witnesses and min(t[0] for t in witnesses) == 47
print('hardest: normalized logged count', 538/math.log(p)**3,
      'first slice', small[47], 'first witnesses', witnesses)

records = []
for path in sorted(Path('logs').glob('bs_adv_*.jsonl')):
    records.extend(json.loads(line) for line in path.read_text().splitlines())
assert all(math.isclose(r['fL3'], r['f']/math.log(r['p'])**3) for r in records)
print('observations / unique primes:', len(records), len({r['p'] for r in records}))
for tag in ('C0_8', 'C0_10', 'C0_12', 'C0_14', 'C0_16',
            'Asmooth_10', 'Asmooth_12', 'Asmooth_14', 'Asmooth_16', 'maxstack_14'):
    rows = [r for r in records if r['tag'] == tag]
    v = np.array([r['fL3'] for r in rows])
    print(tag, len(v), 'mean', v.mean(), 'SE', v.std()/math.sqrt(len(v)),
          'share<=31', np.mean([sum(r['Xs'])/r['f'] for r in rows]))
print('repeated observations:', {p: n for p, n in Counter(r['p'] for r in records).items() if n > 1})

# Cache is ~3 MB, not the ~70 MB raw dump; no Cartesian-product arrays.
cache = np.load('/tmp/bs_adv_drivers_feat.npy', mmap_mode='r')
assert cache.shape == (20000, 19)
y = cache[:, 1]
basecols = [2, 3, 4]
stagecols = [2, 3, 4, 6, 7, 5, 11, 9, 13, 12, 14]
for name, cols in [('baseline', basecols), ('stage2', stagecols)]:
    x = np.column_stack([np.ones(len(y)), cache[:, cols]])
    targets = cache[:, [1, 16, 17, 18]]
    residual = targets - x @ np.linalg.lstsq(x, targets, rcond=None)[0]
    print(name, 'R2', 1-residual[:, 0].var()/y.var(),
          'global partials', np.corrcoef(residual.T)[0, 1:])

# Audit ten raw feature values independently, especially the mislabeled smooth tau.
qs = list(primerange(3, 20000))
for row in cache[::2000]:
    p = int(row[0])
    fac = factorint(p-1)
    smooth_log = sum(v*math.log(q) for q, v in fac.items() if q <= 100)
    smooth_tau_log = sum(math.log(v+1) for q, v in fac.items() if q <= 100)
    assert math.isclose(row[9], smooth_log)
    lpos = 0.0
    for q in qs:
        r = pow(p % q, (q-1)//2, q)
        chi = 1 if r == 1 else -1 if r == q-1 else 0
        lpos -= math.log1p(-chi/q)
    assert math.isclose(lpos, row[13])
    print('feature audit:', p, 'stored smooth feature', row[9],
          'actual log tau(smooth part)', smooth_tau_log)
print('all assertions passed')
