"""O249 (ASTRA_BRIDGE Thm 2.1 / Cor 2.2 / Prop 3.3): Type I levels e (prime, e = 3 mod 4, e <= EM).
For primes p = 1 (4) <= P:
  alive_pred  := H = (pe+1)/4 has a prime factor s with Kronecker (s/p) = -1;
  alive_brute := some r | H^2 with -4r a nonzero square mod e;  assert equal.
  If alive: least twist n (gcd(n,e)=1, some r | H^2 with e | n^2+4r, gcd(r,n)=1); build the twisted point
  (U/n^2, HU/r, pH) and check 4/p exactly and tau = n; ES at level e <=> n = 1 possible.
T1 control: odd squares a^2 <= A2 (gcd(a, e) = 1): alive_brute must be False for every level.
Usage: z21_typeI.py P EM A2
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt
from sympy import primerange, factorint, divisors
from sympy.ntheory import legendre_symbol
from sympy.functions.combinatorial.numbers import kronecker_symbol as kron

P, EM, A2 = (int(a) for a in sys.argv[1:4])
levels = [e for e in primerange(3, EM + 1) if e % 4 == 3]
st = dict(pairs=0, alive=0, es=0, maxtw=0, built=0)
twist_hist = {}
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for e in levels:
        if e == p:
            continue
        H = (p * e + 1) // 4
        fac = factorint(H)
        pred = any(kron(s, p) == -1 for s in fac)
        rs = divisors(H * H)
        sq = {(x * x) % e for x in range(1, e)}
        brute = any(((-4 * r) % e) in sq for r in rs)
        assert pred == brute, (p, e)
        st['pairs'] += 1
        if not brute:
            continue
        st['alive'] += 1
        best = None
        for n in range(1, e):
            if gcd(n, e) != 1:
                continue
            for r in rs:
                if (n * n + 4 * r) % e == 0 and gcd(r, n) == 1:
                    best = (n, r); break
            if best:
                break
        n, r = best
        U = (n * n * H + r) // e
        v = F(H * U, r)
        assert v.denominator == 1
        pts = [F(U, n * n), v, F(p * H)]
        assert sum(1 / x for x in pts) == F(4, p)
        tau = 1
        while any((tau * tau * x).denominator != 1 for x in pts):
            tau += 1
        assert tau == n
        st['built'] += 1
        st['es'] += (n == 1)
        st['maxtw'] = max(st['maxtw'], n)
        twist_hist[n] = twist_hist.get(n, 0) + 1
t1 = 0
for a in range(3, isqrt(A2) + 1, 2):
    n2 = a * a
    for e in levels:
        if gcd(a, e) != 1:
            continue
        H = (n2 * e + 1) // 4
        sq = {(x * x) % e for x in range(1, e)}
        assert not any(((-4 * r) % e) in sq for r in divisors(H * H)), (a, e)
        t1 += 1
print(st)
print('least-twist histogram (alive levels):', dict(sorted(twist_hist.items())[:12]))
print('T1 control: odd squares x levels checked, none alive:', t1)
