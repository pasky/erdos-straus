# z14_mu0.py — window classes at the profinite unit-square point mu = 0 of n_s = c0*4^s + k with c0 + k = 4^J.
# At mu = 0 the window m = c0*4^j*t - k (h = 1, Y = 4^r + t, r = s - j) evaluates to S-integers: n -> 4^J,
# Y -> R/4^j with R = 1 + 4^j t, and every prime power q^v || R divides Y on a neighbourhood of mu = 0 (v_q(Y) = v
# there).  So the window class (with R's primes split off as pieces) contains mu = 0 iff there are d1, d2 among the
# divisors of 2^{E}*n*c0_odd*R (2-exponent in [0,E] plus optionally the whole piece n) with d1 + d2 = 0 (mod m).
# Usage: PYTHONPATH=scripts uv run python scripts/z14_mu0.py c0 k JMAX TMAX
import sys
from math import gcd
from sympy import factorint, divisors
c0, k, JMAX, TMAX = map(int, sys.argv[1:5])
J = (c0 + k).bit_length() // 2
assert 4 ** J == c0 + k
oc = c0
while oc % 2 == 0: oc //= 2
v2c = (c0 & -c0).bit_length() - 1
found = []
for j in range(1, JMAX + 1):
    E = 2 * j - 2 + v2c
    for t in range(1, TMAX + 1):
        m = c0 * 4 ** j * t - k
        if m <= 1: continue
        R = 1 + 4 ** j * t
        odd = [d for d in divisors(oc * R) if gcd(d, m) == 1]
        two = [pow(2, i, m) for i in range(0, E + 1)] + [pow(2, 2 * J + i, m) for i in range(0, E + 1)]
        res = {}
        for d in odd:
            for tw in two: res.setdefault(d * tw % m, d)
        hit = next(((r, res[r]) for r in res if (m - r) % m in res), None)
        if hit: found.append((j, t, m, hit[1], res[(m - hit[0]) % m])); print('FIRE', j, t, m, 'odd parts', hit[1], res[(m - hit[0]) % m], flush=True)
print(c0, k, 'J =', J, 'windows firing at mu = 0 (h = 1, R split):', len(found))
