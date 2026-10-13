"""O176 DIFF_DEEP §2.5: does ONE canonical supersingular curve carry a Type II configuration?
Ibukiyama's maximal order O(q,r) of B = (-p,-q) (p = 1 mod 8, q = 3 mod 8 prime, (p/q) = -1, r^2 = -p mod q):
  O = Z<1, (1+j)/2, i(1+j)/2, (r+i)j/q>,  i^2=-p, j^2=-q, k=ij  (End of a curve defined over F_p, i = Frobenius).
O^0 = Z j + Z (i+k)/2 + Z (r j + k)/q.  For pure x = x1 i + x2 j + x3 k: nrd = p x1^2 + q x2^2 + pq x3^2,
<x,y> = p x1y1 + q x2y2 + pq x3y3.
Enumerate x in O^0 with nrd <= B (B = BF * p), all pairs with <x,y> = 1, f = nrd x <= f' = nrd y, and test DIFF_DEEP
Thm 2.1: 4h | gcd(h,G)^2, h = (ff'-1)/p, G = gcd(f+1,f'+1).  Report per prime: found / not found, and #certificate
values (f,f') of p with f' <= B (from the divisor criterion, all slices) for comparison.
Run: PYTHONPATH=scripts uv run python scripts/bsC_canonical_curve.py PMAX BF
"""
import sys
import numpy as np
from math import gcd, isqrt
from fractions import Fraction as Fr
from sympy import primerange, isprime, sqrt_mod, legendre_symbol, divisors

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 800
BF = int(sys.argv[2]) if len(sys.argv) > 2 else 6


def vectors(p, q, r, B):
    out = []
    bmax = 2 * isqrt(B // p) + 2
    for be in range(-bmax, bmax + 1):
        x1 = Fr(be, 2)
        if p * x1 * x1 > B:
            continue
        rem1 = B - p * x1 * x1
        # k-coef x3 = be/2 + ga/q, need pq x3^2 <= rem1
        t = (rem1 / (p * q)) ** 0.5
        glo = int((-t - be / 2) * q) - 1
        ghi = int((t - be / 2) * q) + 1
        for ga in range(glo, ghi + 1):
            x3 = Fr(be, 2) + Fr(ga, q)
            rem2 = rem1 - p * q * x3 * x3
            if rem2 < 0:
                continue
            s = (rem2 / q) ** 0.5
            c0 = Fr(ga * r, q)
            for al in range(int(-s - c0) - 1, int(s - c0) + 2):
                x2 = al + c0
                n = p * x1 * x1 + q * x2 * x2 + p * q * x3 * x3
                if 0 < n <= B and (be, ga, al) != (0, 0, 0):
                    out.append((x1, x2, x3, int(n)))
    return out


def certs(p, B):  # Type II certificate pairs (f, f') with f <= f' <= B, any slice
    res = set()
    for f in range(3, B + 1, 4):
        if f % p == 0:
            continue
        r0 = pow(f, -1, p)
        for fp in range(r0 + ((f - r0 + p - 1) // p) * p if r0 < f else r0, B + 1, p):
            h = (f * fp - 1) // p
            g = gcd(h, gcd(f + 1, fp + 1))
            if (g * g) % (4 * h) == 0:
                res.add((f, fp))
    return res


tally = [0, 0]
for p in primerange(5, PMAX):
    if p % 24 != 1:
        continue
    q = next(q for q in primerange(3, 10**6) if q % 8 == 3 and legendre_symbol(p, q) == -1)
    r = sqrt_mod(-p % q, q)
    B = BF * p
    V = vectors(p, q, r, B)
    S = np.array([[int(2 * v[0]), int(q * v[1]), int(2 * q * v[2])] for v in V], dtype=np.int64)
    W = S * np.array([p * q, 4, p], dtype=np.int64)
    nr = np.array([v[3] for v in V], dtype=np.int64)
    found = set()
    for a in range(len(V)):
        hits = np.nonzero((W @ S[a]) == 4 * q)[0]
        f = int(nr[a])
        for b in hits:
            fp = int(nr[b])
            if fp < f:
                continue
            h = (f * fp - 1) // p
            g = gcd(h, gcd(f + 1, fp + 1))
            if h > 0 and (g * g) % (4 * h) == 0:
                found.add((f, fp))
    C = certs(p, B)
    assert found <= C, (p, found - C)
    tally[0] += 1; tally[1] += bool(found)
    print(p, 'q', q, '#O0 vectors', len(V), '| Type II pairs (f,f\') on this curve, f\'<=B:', sorted(found),
          '| all certificate pairs of p with f\'<=B:', len(C))
print('primes p = 1 (24) <', PMAX, ':', tally[0], ' canonical curve carries a Type II pair with f\' <= BF*p:', tally[1])
