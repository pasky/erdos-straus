#!/usr/bin/env python3
"""z71 LIT: windows (n, c) that fail the Type II e-slice test (-1 not in D(K) mod c, K=(n+c)/4)
although no odd character mod c has multiplicity-weighted phase sum < pi (Dahan II Thm 9.6(b) certificate).
c prime, c = 3 (mod 4).  Exact integer arithmetic.  Usage: z71_lit_phasecert.py [NMAX] [CMAX]"""
import sys
from sympy import primerange, factorint, primitive_root, isprime

def window(n, c):
    """returns (fails, certified, K-factorisation) or None if not admissible"""
    if (n + c) % 4: return None
    K = (n + c) // 4
    if K % c == 0: return None
    m = c - 1
    g = primitive_root(c)
    dl = {}; x = 1
    for i in range(m):
        dl[x] = i; x = x * g % c
    f = factorint(K)
    gens = [(dl[q % c], v) for q, v in f.items()]
    reach = {0}
    for xq, v in gens:
        reach = {(r + e * xq) % m for r in reach for e in range(-v, v + 1)}
    fails = (m // 2) not in reach
    # odd characters: j odd; phase of q is j*xq/m turns; certificate iff sum v*dist(j*xq, m) < m/2
    best = min(sum(v * min(j * xq % m, m - j * xq % m) for xq, v in gens) for j in range(1, m, 2))
    return fails, 2 * best < m, f, best, m

if __name__ == '__main__':
    print('31121/43:', window(31121, 43))
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    CMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    tot = fail = unc = 0; ex = []
    for n in primerange(25, NMAX):
        if n % 24 != 1: continue
        for c in primerange(3, CMAX):
            if c % 4 != 3 or pow(n, (c - 1) // 2, c) != c - 1: continue   # c in PNR(n): (n/c) = -1
            w = window(n, c)
            if w is None: continue
            tot += 1
            if w[0]:
                fail += 1
                if not w[1]:
                    unc += 1
                    if len(ex) < 8: ex.append((n, c, dict(w[2]), f'min phase sum {w[3]}/{w[4]} turns'))
    print(f'primes n=1 (24) < {NMAX}, prime shifts c=3 (4) < {CMAX} with (n/c)=-1: windows {tot}, failing {fail}, failing without certificate {unc}')
    for e in ex: print(' ', e)
