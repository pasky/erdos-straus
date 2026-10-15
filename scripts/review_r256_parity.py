"""R256 from-scratch check of the r-generic window parity law (s7_sibling_certificate Lemma 2).

At the r-generic point (p = 1 at every prime l != r, p = u at r) window m (m = 3 mod 4, r not| m) has K_m = (p+m)/4 = 1/4 (mod m),
known part K0 = r-free part of (1+m)/4, and fires at r-exponent c iff some d = delta * r^c, delta | K0^2, d = -1/4 (mod m).
Claim: every such c is odd (and c >= 1 needs (-m/r) = -1).
usage: review_r256_parity.py r Mmax Cmax
"""
import sys
from math import isqrt


def factor(x):
    f, q = {}, 2
    while q*q <= x:
        while x % q == 0:
            f[q] = f.get(q, 0) + 1; x //= q
        q += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def legendre(a, r):
    a %= r
    return 0 if a == 0 else (1 if pow(a, (r-1)//2, r) == 1 else -1)


r, Mmax, Cmax = map(int, sys.argv[1:4])
viol, nfire, csets = 0, 0, {}
for m in range(3, Mmax + 1, 4):
    if m % r == 0:
        continue
    k = (1 + m)//4
    while k % r == 0:
        k //= r
    res = {1 % m}
    for q, e in factor(k).items():
        res = {(x*pow(q, j, m)) % m for x in res for j in range(2*e + 1)}
    target = (-pow(4, -1, m)) % m
    cs = [c for c in range(Cmax + 1) if any((x*pow(r, c, m)) % m == target for x in res)]
    if cs:
        nfire += 1
        csets[m] = cs
        if any(c % 2 == 0 for c in cs) or legendre(-m, r) != -1:
            viol += 1; print('VIOLATION', m, cs, legendre(-m, r))
print(f'r={r} m<={Mmax} c<={Cmax}: windows with some c: {nfire}, violations: {viol}')
print('least c histogram:', sorted({c: sum(1 for v in csets.values() if v[0] == c) for c in range(Cmax+1)}.items()))
print('m=11:', csets.get(11), ' small firing windows with least c=1:', [m for m, v in csets.items() if v[0] == 1][:10])
