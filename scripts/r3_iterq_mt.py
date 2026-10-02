#!/usr/bin/env python3
"""Reviewer r3, independent check of POINTWISE_OMEGA2 §11 (Lemmas 11.1-11.2, Thm 11.3).

Written from the statements only (does not import any subject code):
  * S* by brute force over all subsets of the prime factors of M (max over Pi);
  * iterated quarantine (Lemma 11.2), with the per-stage and final counting inequalities;
  * exact asymmetric-LLL check on the final event graph (union of neighbours, x_E = 2P(E));
  * certified Haar bound  log phi(Q_Pi) - log 8 - sum log(1-x_E);
  * Moser-Tardos: construct actual residues X_l (l free) with no event, then verify directly,
    for EVERY M <= T, M = 3 (4), that n mod M is not in R(M) = {-4D mod M : D | A^2}
    (n = 1 mod l^{e_l} for l in Pi).  This tests coverage (I) end to end.

usage: r3_iterq_mt.py T z [c0] [seeds]
"""
import sys, random
from math import log, gcd
from itertools import combinations


def sieve_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def fac(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def divs(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def phi_f(f):
    r = 1
    for p, e in f.items():
        r *= (p - 1) * p ** (e - 1)
    return r


def main():
    T, z = int(sys.argv[1]), int(sys.argv[2])
    k = int(log(T) / log(z))
    while z ** (k + 1) <= T:
        k += 1
    while z ** k > T:
        k -= 1
    c0 = float(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != '-' else 1 / (8 * k)
    nseeds = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    spf = sieve_spf(T + 2)
    emax = {}
    atoms = []  # (M, fM, D)
    wstar = []
    for M in range(3, T + 1, 4):
        fM = fac(M, spf)
        A = (M + 1) // 4
        fA2 = {p: 2 * e for p, e in fac(A, spf).items()}
        ps = list(fM)
        for D in divs(fA2):
            assert (4 * D + 1) % M != 0  # Fact 1.1
            best = 0.0
            for s in range(len(ps) + 1):
                for P in combinations(ps, s):
                    m = 1
                    for p in P:
                        m *= p ** fM[p]
                    if m == M or (4 * D + 1) % m:
                        continue
                    fr = {p: e for p, e in fM.items() if p not in P}
                    best = max(best, 1 / phi_f(fr))
            atoms.append((M, fM, D))
            wstar.append(best)
    Sstar = sum(wstar)
    primes = [p for p in range(2, T + 1) if spf[p] == p]
    for p in primes:
        e = 1
        while p ** (e + 1) <= T:
            e += 1
        emax[p] = e
    Pi = {p for p in primes if p <= z}
    rounds_add = 0
    stage_ok = True
    while True:
        ev = {}  # r -> (fr, set of classes)
        for M, fM, D in atoms:
            m = 1
            fr = {}
            for p, e in fM.items():
                if p in Pi:
                    m *= p ** e
                else:
                    fr[p] = e
            if not fr or (4 * D + 1) % m:
                continue
            r = M // m
            ev.setdefault(r, (fr, set()))[1].add((-4 * D) % r)
        w = {}
        for r, (fr, cl) in ev.items():
            pr = len(cl) / phi_f(fr)
            for p in fr:
                w[p] = w.get(p, 0.0) + pr
        bad = {p for p, v in w.items() if v > c0}
        if not bad:
            break
        # per-stage inequality of Lemma 11.2: w_l(Pi_i) <= sum_{atoms, l|M} wt*
        for l in bad:
            rhs = sum(ws for (M, fM, D), ws in zip(atoms, wstar) if M % l == 0)
            if not (w[l] <= rhs + 1e-12):
                stage_ok = False
        rounds_add += 1
        Pi |= bad
    B = sorted(p for p in Pi if p > z)
    charge = sum(ws * sum(1 for l in fM if l in Pi and l > z) for (M, fM, D), ws in zip(atoms, wstar))
    maxprimes = max(sum(1 for l in fM if l > z) for (M, fM, D) in atoms)
    # events list
    E = []
    for r, (fr, cl) in ev.items():
        mods = {p: p ** e for p, e in fr.items()}
        for a in cl:
            E.append((tuple(sorted(fr)), {p: a % mods[p] for p in fr}, 1 / phi_f(fr)))
    byp = {}
    for i, (ps, _, _) in enumerate(E):
        for p in ps:
            byp.setdefault(p, []).append(i)
    x = [2 * P for (_, _, P) in E]
    minprod = 1.0
    lll_ok = True
    for i, (ps, _, P) in enumerate(E):
        nb = set()
        for p in ps:
            nb.update(byp[p])
        nb.discard(i)
        prod = 1.0
        for j in nb:
            prod *= 1 - x[j]
        minprod = min(minprod, prod)
        if P > x[i] * prod:
            lll_ok = False
    Sev = sum(P for (_, _, P) in E)
    logphiQ = sum(log(p - 1) + (emax[p] - 1) * log(p) for p in Pi)
    cert = logphiQ - log(8) - sum(log(1 - xi) for xi in x)
    thm = (sum(1 for p in primes if p <= z) + k * Sstar / c0) * log(T) + 4 * Sstar
    print(f"T={T} z={z} k={k} (max #primes>z in M: {maxprimes}) c0={c0:.4f}  S*={Sstar:.3f}")
    print(f"  addition rounds={rounds_add} |B|={len(B)}  c0|B|={c0*len(B):.2f} <= charge={charge:.2f} <= k S*={k*Sstar:.2f}"
          f"  stage-ineq ok={stage_ok}")
    print(f"  final max w_l={max(w.values()):.4f}  #events={len(E)} S_ev={Sev:.3f}  LLL min prod={minprod:.4f} ok={lll_ok}")
    print(f"  certified log(1/delta*) <= {cert:.1f}   (Thm 11.3 explicit bound {thm:.1f})")
    # Moser-Tardos + direct verification
    free = [p for p in primes if p not in Pi]
    for seed in range(nseeds):
        rng = random.Random(seed)
        X = {}

        def draw(p):
            q = p ** emax[p]
            while True:
                v = rng.randrange(1, q)
                if v % p:
                    return v
        for p in free:
            X[p] = draw(p)

        def occurs(i):
            ps, cls, _ = E[i]
            return all(X[p] % (p ** (fr_e(i, p))) == cls[p] for p in ps)
        # exponent of p in r for event i: recover from class modulus via phi; store explicitly
        expo = []
        for r, (fr, cl) in ev.items():
            for a in cl:
                expo.append(fr)

        def fr_e(i, p):
            return expo[i][p]
        drop = float(__import__('os').environ.get('DROP', '0'))  # negative control: ignore a fraction of events
        keep = [rng.random() >= drop for _ in E]
        queue = {i for i in range(len(E)) if keep[i]}
        resamples = 0
        while queue:
            i = queue.pop()
            if occurs(i):
                resamples += 1
                for p in E[i][0]:
                    X[p] = draw(p)
                    queue.update(j for j in byp[p] if keep[j])
        # direct check of W(n) > T
        hits = 0
        for M, fM, D in atoms:
            # n mod M by CRT from coordinates
            ok = True
            for p, e in fM.items():
                q = p ** e
                xp = 1 if p in Pi else X[p] % q
                if xp != (-4 * D) % q:
                    ok = False
                    break
            if ok:
                hits += 1
        print(f"  MT seed {seed}: resamples={resamples}; direct check: atoms hit by n = {hits} (must be 0)")


if __name__ == "__main__":
    main()
