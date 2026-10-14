"""R216: from-scratch check of the cd | 6 'genus' criterion (BRIDGE_WORLDS §3 / y3_frob_infinity).
Slice (c,d), m = 4cd, M = n + 4c^2 d.  Type II fires on the slice iff some divisor h of M has h ≡ -1 (mod m).
Claim (m | 24): fires iff NO odd real/quadratic character chi mod m (chi(-1) = -1) has chi(q) = 1 for all primes q | M.
Characters of (Z/m)^* for m | 24 are products of chi_{-4}, chi_8 (= (2/.)), chi_{-3}... enumerated here directly as all
homomorphisms (Z/m)^* -> {±1} (the group is elementary 2-abelian, so all characters are ±1-valued).
"""
import sys
from itertools import product
from sympy import factorint, primerange, divisors
from math import gcd

def chars(m):
    G = [a for a in range(1, m) if gcd(a, m) == 1]
    # all ±1 functions that are homomorphisms
    out = []
    for vals in product([1, -1], repeat=len(G)):
        f = dict(zip(G, vals))
        if all(f[(a * b) % m] == f[a] * f[b] for a in G for b in G):
            out.append(f)
    return out

def main(N):
    slices = [(c, d) for c in range(1, 7) for d in range(1, 7) if 6 % (c * d) == 0]
    CH = {}
    for c, d in slices:
        m = 4 * c * d
        CH[m] = chars(m)
        assert len(CH[m]) == len([a for a in range(1, m) if gcd(a, m) == 1])  # elementary 2-group
    inst = mism = fires = 0
    for p in primerange(5, N):
        for c, d in slices:
            m = 4 * c * d
            M = p + 4 * c * c * d
            assert gcd(M, m) == 1
            inst += 1
            direct = any(h % m == m - 1 for h in divisors(M))
            qs = list(factorint(M))
            blocked = any(ch[m - 1] == -1 and all(ch[q % m] == 1 for q in qs) for ch in CH[m])
            fires += direct
            if direct == blocked:
                mism += 1
                print("MISMATCH", p, c, d, M)
    print("slices", slices)
    print(f"instances {inst}, firing {fires}, mismatches {mism}")

if __name__ == "__main__":
    main(int(sys.argv[1]))
