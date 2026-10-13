"""R177 from-scratch recount of bsD_missed_primes (O177): primes p = 1 (24) < X missed by the quadratic slices
cd | 6 (Type I and Type II), and by the layers cd | 60 (exp 4), cd | 126 (exp 6), cd | 16380 (exp 12).

Slice (c,d), M = 4cd.  A hit is converted into an explicit ES solution and checked in exact rationals:
  Type II: f | 1 + 4c^2 d p, f = -1 (M):  a=(f+1)/M, b=(N/f+1)/M, 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp)
  Type I : f | p^2 + 4c^2 d, f = -p (M):  a=(f+p)/M, b=(N/f+p)/M, 4/p = 1/(abdp) + 1/(acd) + 1/(bcd)
Run: PYTHONPATH=scripts uv run python scripts/review_ld_missed.py X
"""
import sys, statistics
from fractions import Fraction
from sympy import factorint, primerange

X = int(sys.argv[1])


def divs(n):
    ds = [1]
    for l, v in factorint(n).items():
        ds = [d * l ** k for d in ds for k in range(v + 1)]
    return ds


def slices(L):
    S = []
    for cd in range(1, L + 1):
        if L % cd: continue
        for c in range(1, cd + 1):
            if cd % c == 0: S.append((c, cd // c))
    return S  # sorted by cd


def hit(p, c, d):
    M = 4 * c * d
    N = p * p + 4 * c * c * d
    for f in divs(N):
        if (f + p) % M == 0:
            a, b = (f + p) // M, (N // f + p) // M
            assert Fraction(4, p) == Fraction(1, a * b * d * p) + Fraction(1, a * c * d) + Fraction(1, b * c * d)
            return 'I'
    N = 1 + 4 * c * c * d * p
    for f in divs(N):
        if (f + 1) % M == 0:
            a, b = (f + 1) // M, (N // f + 1) // M
            assert Fraction(4, p) == Fraction(1, a * b * d) + Fraction(1, a * c * d * p) + Fraction(1, b * c * d * p)
            return 'II'
    return None


def covered(p, S):
    return any(hit(p, c, d) for c, d in S)


S6, S60, S126, S16380 = slices(6), slices(60), slices(126), slices(16380)
print('#slices cd|6, cd|60, cd|126, cd|16380:', len(S6), len(S60), len(S126), len(S16380))
ps = [p for p in primerange(5, X) if p % 24 == 1]
typeI6 = sum(1 for p in ps for c, d in S6 if hit(p, c, d) == 'I')
print('primes', len(ps), ' Type I hits in cd|6 slices (should be 0, BM-blocked):', typeI6)
miss = [p for p in ps if not covered(p, S6)]
print('missed by cd|6:', len(miss))
m60 = [p for p in miss if not covered(p, S60)]
m126 = [p for p in miss if not covered(p, S126)]
m12 = [p for p in m60 + m126 if not covered(p, S16380)]
print('missed by cd|60:', len(m60), m60)
print('missed by cd|126:', len(m126), m126)
print('missed by cd|16380 (checked on the cd|60 and cd|126 survivors; others are covered a fortiori):', m12)


def lqnr(p):
    q = 2
    while pow(q, (p - 1) // 2, p) == 1: q += 1
    return q


def stat(name, fn):
    print(f'{name}: missed {statistics.mean(fn(p) for p in miss):.3f}  all p=1(24) {statistics.mean(fn(p) for p in ps):.3f}')


stat('mean least QNR', lqnr)
stat('frac (p/5)=(p/7)=1', lambda p: int(pow(p, 2, 5) == 1 and pow(p, 3, 7) == 1))
stat('frac 2 cubic residue', lambda p: int(pow(2, (p - 1) // 3, p) == 1))
stat('frac 3 cubic residue', lambda p: int(pow(3, (p - 1) // 3, p) == 1))
stat('frac p cube mod 7', lambda p: int(pow(p, 2, 7) == 1))
stat('frac p cube mod 9', lambda p: int(p % 9 in (1, 8)))
