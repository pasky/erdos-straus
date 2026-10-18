"""O262 adversarial search engine (python-flint).  For a prime p ≡ 1 (mod 4) and E, computes for every e ≤ E,
e ≡ 3 (mod 4), the e-slice counts
   X_e^II = #{(a,b): a<=b, ab | N, e | a+b} (weight 2 if a<b), N = (p+e)/4   (Type II: 4abd = p+e, a+b = ce)
   X_e^I  = same with N = (pe+1)/4                                          (Type I: 4abd = pe+1, a+b = ce)
(primitive: gcd(a,c) = 1 for Type II as bs_adv_count, gcd(a,b,c) = 1 for Type I as R123), W(p) = least e with a solution, and one verified solution
(x,y,z) with 4/p = 1/x+1/y+1/z checked in exact rational arithmetic.
Usage as module: slices(p, E) -> dict."""
from fractions import Fraction
from flint import fmpz
from collections import defaultdict
from math import gcd
def divisors(n):
    ds = [1]
    for q, k in fmpz(n).factor():
        q = int(q); ds = [d*q**j for d in ds for j in range(k + 1)]
    return ds
def slice_count(N, e, typ):
    ds = divisors(N); byres = defaultdict(list)
    for d in ds: byres[d % e].append(d)
    tot = 0; sol = None
    for a in ds:
        if a*a > N: continue
        M = N // a
        for b in byres[(-a) % e]:
            if b >= a and M % b == 0:
                c = (a + b)//e
                if (gcd(a, c) if typ == 'II' else gcd(gcd(a, b), c)) != 1: continue
                tot += 2 if b > a else 1
                if sol is None: sol = (a, b, (a + b)//e, M//b)
    return tot, sol
def verify(p, typ, e, a, b, c, d):
    x, y, z = ((a*b*d, a*c*d*p, b*c*d*p) if typ == 'II' else (a*b*d*p, a*c*d, b*c*d))
    assert 4*a*b*c*d == ((a + b + c*p) if typ == 'II' else (p*(a + b) + c))
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    return (x, y, z)
def slices(p, E):
    assert p % 4 == 1
    out = {'p': p, 'X2': {}, 'X1': {}, 'W': None, 'sol': None}
    for e in range(3, E + 1, 4):
        n2, s2 = slice_count((p + e)//4, e, 'II'); n1, s1 = slice_count((p*e + 1)//4, e, 'I')
        out['X2'][e] = n2; out['X1'][e] = n1
        if out['W'] is None and (n2 or n1):
            out['W'] = e
            typ, s = ('II', s2) if n2 else ('I', s1)
            out['sol'] = (typ, e, verify(p, typ, e, *s))
    out['S'] = sum(out['X2'].values()) + sum(out['X1'].values())
    return out
