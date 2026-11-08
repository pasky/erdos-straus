#!/usr/bin/env python3
"""Mordell-type covering by universal words.  Modulus L (8 | L).  Universal word = (A, u) with A | L, A >= 3,
u | A+1, 2 <= u <= (A+1)/2; it covers the class n = -u (mod A) (n = 1 mod 4) when (A/n) = -1 — which is a
function of n mod L (checked on several representatives).  Reports covered classes mod L and which classes
mod 840 are fully covered.  usage: cover.py L
"""
import sys
from math import gcd
from sympy import divisors

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def main():
    L = int(sys.argv[1]); assert L % 8 == 0
    covered = {}  # n0 mod L -> (A,u)
    words = []
    for A in divisors(L):
        if A < 3: continue
        for u in divisors(A + 1):
            if u < 2 or 2 * u > A + 1: continue
            words.append((A, u))
    words.sort()
    for A, u in words:
        t = (A + 1) // u
        # classes n0 mod L with n0 = -u mod A, n0 = 1 mod 4
        for n0 in range((-u) % A, L, A):
            if n0 % 4 != 1 or n0 in covered: continue
            # symbol on representatives n = n0 + kL, k=1..3 (must be constant)
            vals = set()
            for k in (1, 2, 3):
                n = n0 + k * L
                v = (n + u) // A
                assert t * u * v - u - v == n and v >= 2 and t >= 2
                assert gcd(A, n) == 1
                vals.add(jacobi(A, n))
            assert len(vals) == 1, (A, u, n0, vals)
            if vals == {-1}:
                covered[n0] = (A, u)
    nA = len(covered)
    # fixed-(u,v) universal words: uv | L/8, class n = -(u+v) mod uv, t = (n+u+v)/(uv); good iff 8 | (n+t)(n+u+v)
    # (Theorem 2.1; depends on n mod 8uv | L).  Cross-checked by direct Jacobi on representatives.
    uvwords = 0
    for uv in divisors(L // 8):
        for u in divisors(uv):
            v = uv // u
            if u < 2 or v < 2 or u > v: continue
            uvwords += 1
            for n0 in range((-(u + v)) % uv, L, uv):
                if n0 % 4 != 1 or n0 in covered: continue
                vals = set()
                for k in (1, 2, 3):
                    n = n0 + k * L
                    t = (n + u + v) // uv
                    assert t * u * v - u - v == n and t >= 2
                    A = t * u - 1
                    j = jacobi(A, n)
                    assert j == (-1 if ((n + t) * (n + u + v)) % 8 == 0 else 1)
                    vals.add(j)
                assert len(vals) == 1
                if vals == {-1}:
                    covered[n0] = ('uv', u, v)
    tot = L // 4
    print(f"L={L}: fixed-A universal words {len(words)} cover {nA}/{tot}; plus {uvwords} fixed-(u,v) words: covered {len(covered)}/{tot}")
    # classes mod 840
    full, part = [], []
    for r in range(1, 840, 4):
        cls = [n0 for n0 in range(r, L, 840)]
        c = sum(1 for n0 in cls if n0 in covered)
        if c == len(cls): full.append(r)
        else: part.append((r, c, len(cls)))
    print(f"fully covered classes mod 840: {len(full)}/210")
    print("NOT fully covered (r, covered, total):", part)
    # by mod 8 / mod 3
    unc = [n0 for n0 in range(1, L, 4) if n0 not in covered]
    import collections
    print("uncovered classes mod L by (n mod 8, n mod 3):", collections.Counter((n0 % 8, n0 % 3) for n0 in unc))
    # max denominator actually used
    print("max A used:", max(w[0] for w in covered.values() if w[0] != 'uv'), " max uv used:", max((w[1]*w[2] for w in covered.values() if w[0] == 'uv'), default=0))
    print("uncovered classes mod 840 list:", [r for r,_,_ in part])
    # fraction of n = 1 mod 24 covered, n = 9 mod 24 covered
    for r24 in (1, 9):
        cl = [n0 for n0 in range(r24, L, 24)]
        print(f"n = {r24} mod 24: covered {sum(1 for n0 in cl if n0 in covered)}/{len(cl)}")

if __name__ == '__main__':
    main()
