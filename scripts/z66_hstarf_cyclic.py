#!/usr/bin/env python3
"""z66 HSTARF: does every prime p = 1 (4) have a Type II triple (x,y,z) realisable by a CYCLIC group Z_N?
Harvey's criterion for signature (0; m1,m2,m3) and G = Z_N: lcm of any two periods = N (= lcm of all three),
and if N is even, the number of periods divisible by 2^{v2(N)} is even.
Also brute-force verifies the criterion for small N by searching alpha,beta in Z/N (cross-check).
usage: uv run scripts/z66_hstarf_cyclic.py PMAX [--verify VMAX]
"""
import sys
from math import gcd
from sympy import primerange

def lcm(a, b): return a * b // gcd(a, b)

def type2_triples(p, amax=None):
    out = []
    a = 1
    while 4 * a * a <= p + 2 * a:
        d = 1
        while 4 * a * a * d <= p + 2 * a:
            n = 4 * a * d; N = 4 * a * a * d + p
            q = n - 1
            while q <= N:
                if N % q == 0:
                    c = (q + 1) // n; b = (a + p * c) // q
                    out.append((a, b, c, d, b * c * d * p, a * c * d * p, a * b * d))
                q += n
            d += 1
        a += 1
    return out

def harvey(x, y, z):
    N = lcm(lcm(x, y), z)
    if lcm(x, y) != N or lcm(x, z) != N or lcm(y, z) != N: return None
    if N % 2 == 0:
        t = N & -N
        if sum(1 for m in (x, y, z) if m % t == 0) % 2: return None
    return N

def brute_cyclic(x, y, z, N):
    # exists alpha,beta in Z/N with N/gcd(N,alpha)=x, N/gcd(N,beta)=y, N/gcd(N,alpha+beta)=z ?
    for al in range(1, N):
        if N // gcd(N, al) != x: continue
        for be in range(1, N):
            if N // gcd(N, be) != y: continue
            if N // gcd(N, (al + be) % N) == z: return True
    return False

def main():
    pmax = int(sys.argv[1]); verify = int(sys.argv[sys.argv.index('--verify') + 1]) if '--verify' in sys.argv else 0
    bad = []; stats = {}
    for p in primerange(5, pmax + 1):
        if p % 4 != 1: continue
        tr = type2_triples(p)
        ok = None
        for (a, b, c, d, x, y, z) in tr:
            N = harvey(x, y, z)
            if N:
                ok = (a, b, c, d, x, y, z, N); break
        if ok is None:
            bad.append(p); print("NO_CYCLIC", p, "n_typeII_triples", len(tr), tr[:3])
        elif verify and ok[7] <= verify:
            a, b, c, d, x, y, z, N = ok
            if not brute_cyclic(x, y, z, N): print("HARVEY_MISMATCH", p, ok)
    print(f"done pmax={pmax} primes_without_cyclic_realisation={len(bad)}: {bad[:30]}")

main()
