"""bsA_minkowski: exact checks of  r(n/A) = popcount(m)  where ?(A/n) = m/2^k (Minkowski question mark), and
(A, n) = (s(m), s(2^k+m)) with s = Stern's diatomic sequence. Then ES five-slice in Stern language: for primes
p = 1 (8) <= PMAX, find N = 2^k+m with popcount(m) <= 3, s(N) = p, (s(m)/p) = -1.
Usage: PYTHONPATH=scripts uv run python scripts/bsA_minkowski.py NMAX PMAX"""
import sys, functools
from fractions import Fraction as F
from math import gcd
from sympy import primerange, jacobi_symbol
from bsA_hjlen import hj_direct
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def s(n):
    if n < 2: return n
    return s(n // 2) if n % 2 == 0 else s(n // 2) + s(n // 2 + 1)
def mink(a, b):
    q = []; x, y = a, b
    while x: q.append(y // x); y, x = x, y % x
    r = F(0); S = 0; sg = 1
    for qq in q: S += qq; r += sg * F(2, 2 ** S); sg = -sg
    return r
NM, PM = int(sys.argv[1]), int(sys.argv[2])
bad = tot = 0
for n in range(3, NM):
    for A in range(1, n):
        if gcd(A, n) != 1: continue
        d = mink(A, n); m = d.numerator; k = d.denominator.bit_length() - 1; tot += 1
        bad += not (bin(m).count('1') == hj_direct(n, A) and s(m) == A and s(2 ** k + m) == n)
print("identity checks n <", NM, ":", tot, "failures", bad)
# Stern-side five-slice search: m = 2^a+2^b+2^c (popcount<=3) -- equivalently HJ words; confirm agreement
miss = 0; cnt = 0
for p in primerange(17, PM):
    if p % 8 != 1: continue
    cnt += 1
    hit = any(jacobi_symbol(A, p) == -1 and hj_direct(p, A) <= 3 for A in range(1, p))
    miss += not hit
print("primes p=1(8) <", PM, ":", cnt, "without a popcount<=3 QNR:", miss)
