#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md §5 (Brun/Bonferroni minorant, mean, mass, twist).
Independent code.

Part 1 (brute force, tiny system): explicit expansion of B into (c_i, b_i, d_i);
  check B(n) <= 1[N(n)=0] for every n mod prod(U); mu = sum c_i/phi(d_i) equals the
  unit-average of B; mu_psi from the definition (Jacobi symbol) equals the product formula
  (-1)^r prod h * sum_{P' subset U\\P_f, |P'|<=J-1-r} (-1)^{|P'|} prod g.
Part 2 (random g <= 1/16, high precision): J = least even >= 22S+10;
  |mu - V| <= e_J(g) <= (eS/J)^J <= e^{-2J};  mu >= 0.99 V;  M_1 <= e^S;
  worst-case |mu_psi| (h = g, P_f = r largest g's) <= mu/4 for r = 1..J.
Part 3 (actual F_l at T, y = sqrt T, where g_max <= 1/16 FAILS): actual mu, V, r=1 twist.
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_bonf.py [T=10000]
"""
import sys
import itertools
import random
from math import prod
import mpmath as mp
from sympy import jacobi_symbol, primerange, factorint
from sympy.ntheory.modular import crt

mp.mp.dps = 400


def esym(gs, J):
    e = [mp.mpf(0)] * (J + 1)
    e[0] = mp.mpf(1)
    for g in gs:
        for j in range(J, 0, -1):
            e[j] += e[j - 1] * g
    return e


def part1():
    rng = random.Random(3)
    U = [11, 13, 17, 19, 23]
    F = {l: set(rng.sample(range(1, l), rng.randint(1, 3))) for l in U}
    Pn = prod(U)
    ok = True
    for J in (2, 4):
        terms = []  # (c, b, d)
        for k in range(J):
            for P in itertools.combinations(U, k):
                d = prod(P)
                for tup in itertools.product(*[sorted(F[l]) for l in P]):
                    b = int(crt(list(P), list(tup))[0]) if P else 0
                    terms.append(((-1) ** k, b, d))
        # pointwise
        for n in range(Pn):
            N = sum(1 for l in U if n % l in F[l])
            B = sum(c for c, b, d in terms if n % d == b % d)
            if B > (1 if N == 0 else 0):
                ok = False
        mu = sum(mp.mpf(c) / prod(p - 1 for p in factorint(d)) if d > 1 else mp.mpf(c) for c, b, d in terms)
        units = [n for n in range(Pn) if all(n % l for l in U)]
        avg = mp.mpf(sum(sum(c for c, b, d in terms if n % d == b % d) for n in units)) / len(units)
        if abs(mu - avg) > mp.mpf(10) ** -50:
            ok = False
        g = {l: mp.mpf(len(F[l])) / (l - 1) for l in U}
        h = {l: mp.mpf(sum(jacobi_symbol(a, l) for a in F[l])) / (l - 1) for l in U}
        for r in range(1, len(U) + 1):
            for Pf in itertools.combinations(U, r):
                f = prod(Pf)
                direct = sum(mp.mpf(c) * jacobi_symbol(b, f) / prod(p - 1 for p in factorint(d))
                             for c, b, d in terms if d % f == 0)
                rest = [l for l in U if l not in Pf]
                inner = sum((-1) ** k * prod((g[l] for l in P), start=mp.mpf(1))
                            for k in range(0, J - r) for P in itertools.combinations(rest, k))
                formula = (-1) ** r * prod((h[l] for l in Pf), start=mp.mpf(1)) * inner
                if J - 1 - r < 0:
                    formula = mp.mpf(0)
                if abs(direct - formula) > mp.mpf(10) ** -50:
                    ok = False
                    print("twist formula mismatch", J, Pf, direct, formula)
    print(f"Part 1 (tiny system, exhaustive): {'OK' if ok else 'FAILURE'}")
    return ok


def check_family(gs, label):
    S = sum(gs)
    J = int(22 * S + 10)
    J += J % 2
    if J < 22 * S + 10:
        J += 2
    mp.mp.dps = int(2 * J / 2.302) + 120  # |mu - V| ~ e^{-2J}: enough digits to resolve it
    e = esym(gs, J)
    mu = sum((-1) ** j * e[j] for j in range(J))
    M1 = sum(e[j] for j in range(J))
    V = prod((1 - g for g in gs), start=mp.mpf(1))
    ok = (abs(mu - V) <= e[J] <= (mp.e * S / J) ** J <= mp.exp(-2 * J)) and mu >= mp.mpf('0.99') * V \
        and M1 <= mp.exp(S) and V >= mp.exp(-2 * S)
    # worst-case twist: h = g on the r largest g's
    gsorted = sorted(gs, reverse=True)
    worst = mp.mpf(0)
    for r in range(1, J + 1):
        if r > len(gs):
            break
        rest = gsorted[r:]
        er = esym(rest, max(J - 1 - r, 0) + 1)
        inner = sum((-1) ** j * er[j] for j in range(J - r)) if J - 1 - r >= 0 else mp.mpf(0)
        mpsi = abs(prod(gsorted[:r], start=mp.mpf(1)) * inner)
        worst = max(worst, mpsi / mu)
    ok = ok and worst <= mp.mpf(1) / 4
    print(f"{label}: #U={len(gs)} S={float(S):.3f} J={J} mu/V={float(mu / V):.6f} "
          f"log(M1/mu)={float(mp.log(M1 / mu)):.2f} (<=3S+1={float(3 * S + 1):.2f}) "
          f"max_r |mu_psi|/mu={float(worst):.4f} -> {'OK' if ok else 'FAIL'}")
    return ok


def part2():
    rng = random.Random(5)
    ok = True
    for n, S_target in ((40, 1.0), (200, 4.0), (600, 10.0), (3000, 20.0)):
        gs = [rng.random() for _ in range(n)]
        sc = S_target / sum(gs)
        gs = [mp.mpf(min(x * sc, 1 / 16)) for x in gs]
        ok &= check_family(gs, f"random S~{S_target}")
    # extremal: all g = 1/16
    ok &= check_family([mp.mpf(1) / 16] * 160, "all g=1/16 (S=10)")
    return ok


def part3(T):
    y = T ** 0.5
    U = list(primerange(int(y) + 1, T + 1))
    F = {l: set() for l in U}
    for M in range(3, T + 1, 4):
        lp = max(factorint(M))
        if lp <= y:
            continue
        m = M // lp
        A = (M + 1) // 4
        f = factorint(A)
        ds = [1]
        for p, e in f.items():
            ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
        for D in ds:
            if (4 * D + 1) % m == 0:
                F[lp].add((-4 * D) % lp)
    gs = [mp.mpf(len(F[l])) / (l - 1) for l in U]
    hs = [mp.mpf(sum(jacobi_symbol(a, l) for a in F[l])) / (l - 1) for l in U]
    S = sum(gs)
    J = int(22 * S + 10); J += J % 2
    e = esym(gs, J)
    mu = sum((-1) ** j * e[j] for j in range(J))
    V = prod((1 - g for g in gs), start=mp.mpf(1))
    nbig = sum(1 for g in gs if g > mp.mpf(1) / 16)
    # r = 1 twists, exact
    worst = mp.mpf(0)
    for i in range(len(U)):
        rest = gs[:i] + gs[i + 1:]
        er = esym(rest, J - 1)
        inner = sum((-1) ** j * er[j] for j in range(J - 1))
        worst = max(worst, abs(hs[i] * inner) / mu)
        if i > 400:
            break
    print(f"Part 3 (actual F_l, T={T}, y=sqrt T): S={float(S):.3f}, #(g>1/16)={nbig}, J={J}, "
          f"mu/V={float(mu / V):.6f}, -log V={float(-mp.log(V)):.2f}, "
          f"max over first 400 l of |mu_psi|/mu (r=1) = {float(worst):.4f}")


if __name__ == "__main__":
    T = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 10000
    ok = part1()
    ok &= part2()
    if '--no-part3' not in sys.argv:
        part3(T)
    print("ALL OK" if ok else "FAILURE")
    sys.exit(0 if ok else 1)
