#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md Lemma 2.1 (prime-local reduction) and of the
definition of W (notes (51.1)/(51.2) vs (58.3)).  Independent code.

1. For M <= MMAX, M=3 (4): {-u v^{-1} mod M : uvw = (M+1)/4} == {-4D mod M : D | A^2}.
2. For T, y = sqrt(T): Q = lcm(24, l^{e_l} : l <= y);  F_l by projection of R(M).
   (i)  random n = 1 (mod Q): W(n) > T  <=>  n mod l not in F_l for all l in U;
   (ii) forced survivors (CRT, a_l not in F_l for all l): W(n) > T;
   (iii) forced single hits (one l with a_l in F_l, others avoiding): W(n) <= T (converse).
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_local.py T NRANDOM NFORCED [seed]
"""
import sys
import random
from math import gcd, isqrt
from sympy import factorint, primerange
from sympy.ntheory.modular import crt


def R_set(M):
    A = (M + 1) // 4
    f = factorint(A)
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return {(-4 * D) % M for D in ds}


def R_set_uvw(M):
    A = (M + 1) // 4
    out = set()
    for u in range(1, A + 1):
        if A % u:
            continue
        B = A // u
        for v in range(1, B + 1):
            if B % v:
                continue
            out.add((-u * pow(v, -1, M)) % M)
    return out


def main():
    T = int(sys.argv[1]); NR = int(sys.argv[2]); NF = int(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    rng = random.Random(seed)
    bad = 0
    for M in range(3, 1200, 4):
        if R_set(M) != R_set_uvw(M):
            bad += 1
    print(f"(58.3) vs (51.2) on M<1200: mismatches={bad}")
    y = T ** 0.5
    Q = 24
    for l in primerange(2, int(y) + 1):
        e = 1
        while l ** (e + 1) <= T:
            e += 1
        Q = Q * l ** e // gcd(Q, l ** e)
    assert Q % 840 == 0
    Rs = {M: R_set(M) for M in range(3, T + 1, 4)}
    U = list(primerange(int(y) + 1, T + 1))
    F = {l: set() for l in U}
    for M, R in Rs.items():
        lp = max(factorint(M))
        if lp <= y:
            continue
        m = M // lp
        for c in R:
            if c % m == 1 % m:
                F[lp].add(c % lp)

    def W_exceeds(n):
        for M, R in Rs.items():
            if n % M in R:
                return False
        return True

    def avoids(n):
        return all(n % l not in F[l] for l in U)

    mism = 0; surv = 0
    for _ in range(NR):
        n = 1 + Q * rng.randrange(1, 10 ** 40)
        a, b = W_exceeds(n), avoids(n)
        surv += a
        mism += (a != b)
    print(f"T={T} log Q={Q.bit_length()*0.6931:.1f} #U={len(U)}: random n=1 (Q): {NR} draws, {surv} with W>T, mismatches={mism}")
    mods = [Q] + U
    fs_bad = 0; hit_bad = 0
    for t in range(NF):
        res = [1]
        for l in U:
            allowed = [a for a in range(l) if a not in F[l]]
            res.append(rng.choice(allowed))
        n = int(crt(mods, res)[0])
        if not W_exceeds(n):
            fs_bad += 1
        # single hit
        j = rng.randrange(len(U))
        l = U[j]
        if F[l]:
            res2 = list(res)
            res2[j + 1] = rng.choice(sorted(F[l]))
            n2 = int(crt(mods, res2)[0])
            if W_exceeds(n2):
                hit_bad += 1
    print(f"forced survivors: {NF}, with W<=T: {fs_bad};  forced single hits with W>T: {hit_bad}")
    ok = bad == 0 and mism == 0 and fs_bad == 0 and hit_bad == 0
    print("ALL OK" if ok else "FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
