#!/usr/bin/env python3
"""Lemma 1.6 check at the 38 G*-zero primes: levels C=1,2,3 must fail; print the norm-form representations."""
from sympy import factorint, isprime
from math import isqrt
zeros = [int(x) for x in open('data/z57/bff/gstar_zeros_le1e8.txt')] + [564661441]
def has_div_class(N, mod, cls):
    # any divisor d of N with d % mod == cls ?
    from sympy import divisors
    return any(d % mod == cls for d in divisors(N))
def two_sq(N, k):
    # N = a^2 + k b^2 with gcd(a,b)=1 ?
    from math import gcd
    b = 1
    while k*b*b < N:
        r = N - k*b*b; a = isqrt(r)
        if a*a == r and gcd(a,b) == 1: return (a,b)
        b += 1
    return None
for p in zeros:
    f1 = has_div_class(4*p+1, 4, 3); f2 = has_div_class(8*p+1, 8, 7); f3 = has_div_class(12*p+1, 12, 11)
    r1 = two_sq(4*p+1, 1); r2 = two_sq(8*p+1, 1) or ('x2',)+ (two_sq(8*p+1, 2) or ()); r3 = two_sq(12*p+1,1) or ('x3',)+(two_sq(12*p+1,3) or ())
    if r1 and r1[0]%2==0: r1=(r1[1],r1[0])
    t = (r1[0]-1)//2 if r1 else None; s = r1[1]//2 if r1 else None
    assert not f1 and not f2 and not f3, p
    assert r1 and t*(t+1)+s*s == p
    print(p, 'levels1-3 fail OK;', '4p+1=a^2+b^2', r1, 'p=t(t+1)+s^2', (t, s), '8p+1:', r2, '12p+1:', r3)
