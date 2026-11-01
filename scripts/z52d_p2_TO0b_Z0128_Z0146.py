"""z52d pass2 TO0b.
Z0128: signed ES 4/p = 1/x + 1/y - 1/z (x,y,z positive integers). For small primes p, is there a solution with z in
[p^2, 4p^2] (size-controlled negative term)?  Reduction: 1/x+1/y = 4/p + 1/z = (4z+p)/(pz) (two-unit test).
Z0146: fraction of a/b (1 <= a <= b, gcd=1) with b <= 120 that are sums of three unit fractions, binned by a/b."""
import sys
from fractions import Fraction as Fr
from math import gcd
sys.path.insert(0, 'scripts')
from z52d_p2_TO0b_Z0053_weighted import two_unit
def isprime(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
res = []
for p in [q for q in range(5, 90) if isprime(q)]:
    zmax = None; cnt = 0; found = None
    for z in range(p * p, 4 * p * p + 1):
        r = Fr(4, p) + Fr(1, z)
        t = two_unit(r)
        if t is not None:
            cnt += 1
            if found is None: found = (z, t)
            zmax = z
    res.append((p, found is not None, zmax, cnt))
print('Z0128 signed ES with one negative term, z in [p^2, 4p^2], primes 5..89:')
print('  primes with a solution in that window:', sum(1 for r in res if r[1]), 'of', len(res))
print('  examples (p, z_max_found, count):', [(r[0], r[2], r[3]) for r in res][:12])
print('  failing primes:', [r[0] for r in res if not r[1]])
def three_unit(a, b):
    r = Fr(a, b)
    if r > 3: return False
    # first denominator x in [ceil(1/r), 3/r]
    import math
    for x in range(math.ceil(1 / r), int(3 / r) + 2):
        r1 = r - Fr(1, x)
        if r1 <= 0: continue
        t = two_unit(r1)
        if t is not None: return True
    return False
bins = {}
tot = 0; ok = 0
for b in range(2, 121):
    for a in range(1, b + 1):
        if gcd(a, b) != 1: continue
        tot += 1
        v = three_unit(a, b)
        ok += v
        key = round(a / b, 1)
        bins.setdefault(key, [0, 0])
        bins[key][0] += v; bins[key][1] += 1
print('Z0146 fraction of reduced a/b (b<=120, a<=b) representable as 3 unit fractions:', ok, '/', tot, '=', round(ok / tot, 4))
print('  by a/b bin (0.1 wide): ', {k: f'{v[0]}/{v[1]}' for k, v in sorted(bins.items())})
