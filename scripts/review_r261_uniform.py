"""R261: from-scratch check of CAP_BOUNDED Prop 2.1 (uniform certificate <=> m | N-list) and Prop 2.3 (odd-order witness).
Usage: PMAX MMAX JMAX
(1) For primes p = 1 (4) <= PMAX and windows m = 3 (4) <= MMAX, gcd(m,p)=1: brute-force existence of a uniform certificate
    (delta_s = j b_s on odd s | K, delta_2 = a in [-t,t], delta_p = eps), admissible j in [-1, JMAX], split cap0 / cap>=1,
    vs. the author's N-lists (a)-(d) (with the same j-range).
(2) Prop 2.3: for p = 1 (8) <= PMAX, primes q = 3 (8) with (q/p) = -1, q <= MMAX: o = odd part of ord_q(p/4); check
    q | p^o + 4^o with o least odd, rebuild the j = o certificate, Def 1.1 check at cap (o-1)/2 max b_s, and
    least_cap <= that bound.
"""
import sys
from math import gcd, isqrt
from sympy import primerange, factorint, jacobi_symbol
from sympy.ntheory import n_order
from review_r261_windows import least_cap, rebuild, check_def11

PMAX, MMAX, JMAX = map(int, sys.argv[1:4])


def is_sq(n):
    return isqrt(n) ** 2 == n


def brute(p, m):
    K = (p + m) // 4
    t = (K & -K).bit_length() - 1
    Kp = K >> t
    fac = factorint(Kp)
    sq = all(b % 2 == 0 for b in fac.values())
    c0 = c1 = False
    for j in range(-1, JMAX + 1):
        if j >= 2 and j % 2 == 0 and not sq:
            continue
        if Kp == 1 and j >= 2:
            continue  # no odd primes: same values as j in {-1,0,1}
        v = pow(Kp, j, m)
        for a in range(-t, t + 1):
            for e in (-1, 0, 1):
                if v * pow(2, a, m) * pow(p, e, m) % m == m - 1:
                    if j <= 1:
                        c0 = True
                    else:
                        c1 = True
    return c0, c1, t, Kp, sq


def lists(p, m, t, Kp, sq):
    """author's N-lists; returns (cap0 predicted, cap>=1 predicted)."""
    d = lambda N: N % m == 0
    if t == 0:
        c0 = d(p + 4) or d(p + 1) or d(p * p + 4) or d(5)
        js = [j for j in range(2, JMAX + 1) if j % 2 == 1 or sq] if Kp > 1 else []
        c1 = any(d(p ** (j + e) + 4 ** j) for j in js for e in (-1, 0, 1))
    else:
        c0 = (any(d(2 ** c * p + 1) for c in range(0, t + 1)) or any(d(p + 2 ** c) for c in range(1, 2 * t + 3))
              or any(d(p * p + 2 ** c) for c in range(2, 2 * t + 3)) or any(d(2 ** c + 1) for c in range(1, 2 * t + 3)))
        js = [j for j in range(2, JMAX + 1) if j % 2 == 1 or sq] if Kp > 1 else []
        c1 = any(d(p ** (j + e) + 2 ** c) for j in js for e in (-1, 0, 1)
                 for c in range(j * (t + 2) - t, j * (t + 2) + t + 1))
    return c0, c1


bad = n = 0
for p in primerange(5, PMAX):
    if p % 4 != 1:
        continue
    for m in range(3, MMAX + 1, 4):
        if gcd(m, p) != 1:
            continue
        b0, b1, t, Kp, sq = brute(p, m)
        l0, l1 = lists(p, m, t, Kp, sq)
        n += 1
        if (b0, b1) != (l0, l1):
            bad += 1
            if bad <= 10:
                print('MISMATCH', p, m, 't', t, 'Kp', Kp, 'brute', b0, b1, 'lists', l0, l1)
print('Prop 2.1: pairs', n, 'mismatches', bad)

n = bad = 0; worse = 0
for p in primerange(17, PMAX):
    if p % 8 != 1:
        continue
    for q in primerange(3, MMAX):
        if q % 8 != 3 or jacobi_symbol(q, p) != -1:
            continue
        g = p * pow(4, -1, q) % q
        o = n_order(g, q)
        while o % 2 == 0:
            o //= 2
        lo = next(k for k in range(1, q, 2) if (p ** k + 4 ** k) % q == 0)
        K = (p + q) // 4
        fac = factorint(K)
        cap = (o - 1) // 2 * max(fac.values())
        vec = tuple((s, o * b) for s, b in fac.items())
        x, y, z = rebuild(p, q, vec)
        ok = lo == o and check_def11(p, x, y, z, cap) and (cap == 0 or not check_def11(p, x, y, z, cap - 1))
        lc = least_cap(p, q, cap)
        n += 1
        if not ok or lc is None:
            bad += 1
            print('FAIL', p, q, o, lo, cap, lc)
print('Prop 2.3: (p,q) pairs', n, 'failures', bad)
