"""O197: residue classes mod L covered by ET-shaped identities (atoms) for m/n, primes n.
Type II atom (PW Cor 2.4 / TRANSFER 5.0): u,v,w >= 1, M = m*u*v*w - 1, event n = -u * v^{-1} (mod M)   [M | L]
Type I  atom (PW Cor 2.2): a,d >= 1, K = m*a*d, f | m*a^2*d + 1, event n = -f (mod K)                  [K | L]
Every prime n in an event class (n > the atom's tiny exceptions) has a solution, so classes hit are 'covered'.
usage: ms_cover.py m L   -> number of unit classes mod L, uncovered unit classes, and how many are squares."""
import sys
from math import gcd
from sympy import divisors

def covered(m, L):
    import numpy as np
    covarr = np.zeros(L, dtype=bool)
    def add(mod, r):
        covarr[r % mod::mod] = True   # all classes mod L lifting r mod `mod`
    for M in divisors(L):
        if (M + 1) % m: continue
        Aq = (M + 1) // m
        for u in divisors(Aq):
            for v in divisors(Aq // u):
                if gcd(v, M) != 1: continue
                add(M, (-u * pow(v, -1, M)) % M)
    for K in divisors(L):
        if K % m: continue
        ad = K // m
        for a in divisors(ad):
            d = ad // a
            for f in divisors(m * a * a * d + 1):
                add(K, (-f) % K)
    return set(np.nonzero(covarr)[0].tolist())

if __name__ == '__main__':
    m, L = int(sys.argv[1]), int(sys.argv[2])
    cov = covered(m, L)
    units = [r for r in range(L) if gcd(r, L) == 1]
    sq = {(x * x) % L for x in units}
    unc = [r for r in units if r not in cov]
    print(f"m={m} L={L}: units {len(units)}, uncovered {len(unc)}, of which squares {sum(r in sq for r in unc)}; "
          f"square classes {len(sq)}")
    if len(unc) <= 60: print("  uncovered:", unc)
    for p in map(int, sys.argv[3:]):
        print(f"  n={p}: class {p % L} {'COVERED' if p % L in cov else 'uncovered'}{' (square class)' if p % L in sq else ''}")
