# ec_survey2.py — survey of n = k*2^m + 1 for odd k with 3 | k (the only k whose members can lie in Mordell's hard classes).
# For each k: integer square points (k*2^l + 1 = s^2, l >= 0; k + 4^j = s^2), unit-square obstruction (k = 4^j - 1), and
# least L (from a list, augmented by orders of primes dividing s) admitting an ET+divisor exponent covering with moduli <= Mmax.
# Usage: ec_survey2.py kmin kmax Mmax
import sys, functools
from math import isqrt, lcm
import mordell_lib as ML
import ec_cover as EC
ML.residue_table = functools.lru_cache(maxsize=4000)(ML.residue_table)
kmin, kmax, Mmax = map(int, sys.argv[1:4])
BASE = [12, 24, 36, 48, 60, 72, 120, 144, 180, 240, 360]
def ordp(q):
    o, x = 1, 2 % q
    while x != 1:
        x = x * 2 % q; o += 1
    return o
stats = {}
for k in range(kmin, kmax + 1):
    if k % 6 != 3:
        continue
    pts = []
    for l in range(0, 80):
        v = k * 2 ** l + 1
        if isqrt(v) ** 2 == v:
            pts.append(('mu=%d' % l, isqrt(v)))
    for j in range(1, 40):
        v = k + 4 ** j
        if isqrt(v) ** 2 == v:
            pts.append(('mu=-%d' % (2 * j), isqrt(v)))
    unit_obs = any(s & (s - 1) == 0 for _, s in pts)   # s a power of 2
    extra = set()
    for _, s in pts:
        for q in ML.factor_small(s):
            if q > 2:
                extra.add(ordp(q))
    Ls = list(BASE)
    for o in sorted(extra):
        Ls += [lcm(L, o) for L in (12, 36, 60, 72) if lcm(L, o) <= 3000]
    Ls = sorted(set(Ls))
    found = None
    if not unit_obs:
        for L in Ls:
            ch = EC.search(k, L, Mmax, verbose=False)
            if ch:
                found = (L, len(ch), max(M for M, _, _ in ch))
                break
    tag = 'OBSTRUCTED(unit square)' if unit_obs else ('COVER L=%d classes=%d maxM=%d' % found if found else 'OPEN')
    stats[tag.split()[0]] = stats.get(tag.split()[0], 0) + 1
    print(k, tag, pts, flush=True)
print('STATS', stats)
