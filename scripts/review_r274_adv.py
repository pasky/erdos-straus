"""R274 from-scratch recount of DISPROOF_AVENUES §5 S(p) = sum_{e<=2047, e≡3 (4)} (X_e^I + X_e^II).
Type II e-slice: 4abd = p + e, a + b = c e (count ordered (a,b), gcd(a,c) = 1).
Type I  e-slice: 4abd = p e + 1, a + b = c e (ordered, gcd(a,b,c) = 1).
Factorisation by python-flint (library); the enumeration is ordered (a over all divisors, b over divisors in the
residue class -a mod e with b | N/a), different from the author's a <= b loop.  Every counted tuple is checked in
the ET equation for the first 50 e; one solution per prime is checked as 4/p = 1/x + 1/y + 1/z in exact rationals.
Usage: uv run --with python-flint --with sympy python scripts/review_r274_adv.py p [p ...]"""
import sys
from math import gcd
from fractions import Fraction
from collections import defaultdict
from flint import fmpz
import sympy

def divisors(n):
    ds = [1]
    for q, k in fmpz(n).factor():
        q = int(q); ds = [d*q**j for d in ds for j in range(k + 1)]
    return ds

def count(p, e, typ, check):
    M = p + e if typ == 'II' else p*e + 1
    assert M % 4 == 0
    N = M // 4; ds = divisors(N); res = defaultdict(list)
    for b in ds: res[b % e].append(b)
    n = 0; first = None
    for a in ds:
        Na = N // a
        for b in res[(-a) % e]:
            if Na % b: continue
            c = (a + b)//e; d = Na // b
            if typ == 'II' and gcd(a, c) != 1: continue
            if typ == 'I' and gcd(gcd(a, b), c) != 1: continue
            if check:
                assert 4*a*b*c*d == ((a + b + c*p) if typ == 'II' else p*(a + b) + c)
            n += 1
            if first is None: first = (a, b, c, d)
    return n, first

def S(p, E=2047):
    tot = 0; W = None; sol = None; S127 = 0
    for e in range(3, E + 1, 4):
        n2, f2 = count(p, e, 'II', e < 200); n1, f1 = count(p, e, 'I', e < 200)
        tot += n1 + n2
        if e <= 127: S127 += n1 + n2
        if W is None and (n1 or n2):
            W = e; sol = ('II', f2) if n2 else ('I', f1)
    typ, (a, b, c, d) = sol
    x, y, z = (a*b*d, a*c*d*p, b*c*d*p) if typ == 'II' else (a*b*d*p, a*c*d, b*c*d)
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    return tot, S127, W, typ

if __name__ == '__main__':
    for p in map(int, sys.argv[1:]):
        print(p, 'p%4 =', p % 4, 'BPSW(sympy) =', sympy.isprime(p), 'flint =', fmpz(p).is_prime(),
              '(S, S127, W, type) =', S(p), flush=True)
