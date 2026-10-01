#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md §6.1 (Prop 6.1 combinatorics) and §6.3 EVIDENCE
(irredundant multi-prime atoms, hub classes).  Independent code.

Prop 6.1: for every pair of odd primes l1<l2<=sqrt(T/3) some M<=T, M=3 (4) has l1 l2 | M.
§6.3: y=T^theta; atoms (M,c), c in R(M), compatible with n=1 mod (y-smooth part m) i.e.
c = 1 mod m; single-prime atoms (rough part = one prime l) give F_l; a multi-prime atom
(rough part has >=2 distinct primes) is redundant if c mod l in F_l for some rough prime l.
Hub graph for class -d: edges {l1,l2} from irredundant atoms with rough part l1*l2, c = -d.
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_pairs.py T theta
"""
import sys
from math import isqrt
from sympy import factorint, primerange


def main():
    T = int(sys.argv[1]); theta = float(sys.argv[2])
    # Prop 6.1
    P = [p for p in primerange(3, isqrt(T // 3) + 1)]
    bad = 0
    for i, a in enumerate(P):
        for b in P[i + 1:]:
            if not ((a * b) % 4 == 3 and a * b <= T) and not ((3 * a * b) % 4 == 3 and 3 * a * b <= T):
                bad += 1
    print(f"Prop 6.1 T={T}: {len(P)} odd primes <= sqrt(T/3), uncovered pairs: {bad}")
    y = T ** theta
    F = {}
    multi = []
    for M in range(3, T + 1, 4):
        f = factorint(M)
        rough = sorted(p for p in f if p > y)
        if not rough:
            continue
        r = 1
        for p in rough:
            r *= p ** f[p]
        m = M // r
        A = (M + 1) // 4
        ds = [1]
        for p, e in factorint(A).items():
            ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
        R = {(-4 * D) % M for D in ds}
        comp = {c % r for c in R if c % m == 1 % m}
        if len(rough) == 1 and f[rough[0]] == 1:
            F.setdefault(rough[0], set()).update(comp)
        elif len(rough) >= 2:
            multi.append((r, tuple(rough), comp))
    nat = nirr = 0
    hubs = {}
    for r, rough, comp in multi:
        for c in comp:
            nat += 1
            if not any(c % l in F.get(l, ()) for l in rough):
                nirr += 1
                if len(rough) == 2 and r == rough[0] * rough[1] and r - c <= 60:
                    hubs.setdefault(r - c, set()).add(rough)
    print(f"T={T} theta={theta}: multi-prime atoms={nat}, irredundant={nirr} ({100 * nirr / max(nat, 1):.1f}%)")
    for d, E in sorted(hubs.items(), key=lambda t: -len(t[1]))[:4]:
        V = {l for e in E for l in e}
        deg = {}
        for a, b in E:
            deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
        print(f"   hub -{d}: {len(E)} edges on {len(V)} primes, max degree {max(deg.values())}")


if __name__ == "__main__":
    main()
