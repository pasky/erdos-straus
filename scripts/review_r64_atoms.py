"""R64 from-scratch check of (A1): at fixed prime l, atoms (k,l,u,v) with
k = 1 mod 4, k<=K, H<u,v<=z, gcd(u,v)=gcd(uv,k)=1, 4uv | kl+1 have pairwise
distinct residues -u/v mod l, provided z^2 < l and 4H^2 > K.  Also check the
"active iff k | u+cv" rule and that every n in an atom class has W(n) <= kl
(multiplier identity), and Bonferroni Q_r properties."""
from math import gcd, comb
from fractions import Fraction
from sympy import primerange
import random

def atoms(K, H, z, l):
    out = []
    for k in range(1, K + 1, 4):
        if (k * l) % 4 != 3: continue
        for u in range(H + 1, z + 1):
            for v in range(H + 1, z + 1):
                if gcd(u, v) != 1 or gcd(u * v, k) != 1: continue
                if (k * l + 1) % (4 * u * v): continue
                out.append((k, u, v))
    return out

bad = 0; tot = 0
for K, H in [(9, 2), (13, 2), (21, 3), (33, 3)]:
    for z in range(H + 1, H + 12):
        for l in primerange(z * z + 1, z * z + 4000):
            A = atoms(K, H, z, l)
            res = [(-u * pow(v, -1, l)) % l for k, u, v in A]
            tot += len(A)
            if len(set(res)) != len(res): bad += 1; print("COLLISION", K, H, z, l, A)
            assert len(A) <= z * z
            for k, u, v in A:
                M = k * l; w = (M + 1) // (4 * u * v)
                assert u * v * w == (M + 1) // 4
                n0 = (-u * pow(v, -1, M)) % M
                for n in (n0, n0 + M, n0 + 7 * M):
                    if n == 0: continue
                    s = (n * v + u) // M
                    assert (n * v + u) % M == 0
                    assert Fraction(4, n) == Fraction(1, s*u*w) + Fraction(1, n*s*v*w) + Fraction(1, n*u*v*w)
                # activity: n = c mod k is in atom's k-component iff k | u + c v
                for c in range(k):
                    assert ((c * v + u) % k == 0) == (k == 1 or c == (-u * pow(v, -1, k)) % k)
print("atoms checked", tot, "collisions", bad)
# Bonferroni Q_r
for r in range(0, 12, 2):
    for h in range(0, 40):
        Q = sum((-1) ** j * comb(h, j) for j in range(r + 1))
        assert Q == (1 if h == 0 else comb(h - 1, r))
        assert (1 if h == 0 else 0) <= Q <= (1 if h == 0 else 0) + comb(h, r + 1)
# odd r gives minorant
for r in range(1, 12, 2):
    for h in range(0, 40):
        Q = sum((-1) ** j * comb(h, j) for j in range(r + 1))
        assert Q <= (1 if h == 0 else 0)
print("Bonferroni ok")
