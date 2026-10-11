"""R135 from-scratch recomputation of full-coset covers (P: Sigma_e(N) ⊇ -K_e) and transparent covers
(TP: R = Sigma_e(L)·{M^-1,1,M} ⊇ -K_e, L = part of N on primes < e) for given primes p ≡ 1 (4), e ≤ E.
Usage: review_r135_covers.py E p1 p2 ...    No author code reused."""
import sys
from math import gcd
from sympy import factorint, jacobi_symbol


def sigma(fac, e):
    S = {1}
    for l, v in fac.items():
        g = l % e; gi = pow(g, -1, e)
        A = {1}; x = y = 1
        for _ in range(v):
            x = x * g % e; y = y * gi % e; A |= {x, y}
        S = {s * a % e for s in S for a in A}
    return S


def run(p, E):
    res = []
    for e in range(3, E + 1, 4):
        if e % p == 0: continue
        target = {g for g in range(1, e) if gcd(g, e) == 1 and jacobi_symbol(g, e) == -1}
        for T, N in (("I", (p * e + 1) // 4), ("II", (p + e) // 4)):
            fac = factorint(N)
            S = sigma(fac, e)
            hit = (e - 1) in S
            P = target <= S
            Lfac = {l: v for l, v in fac.items() if l < e}
            M = N
            for l, v in Lfac.items(): M //= l ** v
            m = M % e; mi = pow(m, -1, e)
            SL = sigma(Lfac, e)
            R = SL | {s * m % e for s in SL} | {s * mi % e for s in SL}
            TP = target <= R
            res.append((e, T, hit, P, TP, len(target), len(fac)))
    return res


if __name__ == "__main__":
    E = int(sys.argv[1])
    for p in map(int, sys.argv[2:]):
        r = run(p, E)
        sol = sum(x[2] for x in r); P = [x for x in r if x[3]]; TP = [x for x in r if x[4]]
        P20 = [x for x in P if x[5] >= 20]; TP20 = [x for x in TP if x[5] >= 20]
        big = max((x[5] for x in P), default=0); bigT = max((x[5] for x in TP), default=0)
        print(f"p={p} E={E} sol_slices={sol} P={len(P)} TP={len(TP)} P20={len(P20)} TP20={len(TP20)} "
              f"maxcovered={big} maxcoveredTP={bigT} maxomega={max(x[6] for x in r)}")
        assert all((not x[3]) or x[2] for x in r)  # P implies hit
        assert all((not x[4]) or x[3] for x in r)  # TP implies P
