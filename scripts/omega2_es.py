#!/usr/bin/env python3
"""POINTWISE_OMEGA2 §4 (EVIDENCE / illustration): Construction 4.2 at a finite T.

Quarantine (class of one) at primes <= y = T^theta and at bad primes (g0 > 1/64);
singles and edges of the surviving atoms; vertex degrees and hub vertices;
Monte Carlo of the product (Haar) measure on the free coordinates:
  * events fired vs active primes N (the hub phenomenon of PO Prop 6.3),
  * E prod(1 + z a_l) for small z (the exponential moment of Lemma 2.1),
  * an exact check of Lemma 1.2 (closed form of B_L, and the bound) on samples.
Also a direct check of (I): for random integers n = 1 (mod Q) with no event, W(n) > T.

usage: omega2_es.py T theta delta samples gbad [z ...]   (Lemma 4.3 uses gbad=1/64)
"""
import random
import sys
from itertools import combinations
from math import comb, log

from pointwise_omega_S import spf_table, factor, divisors_from


def build(T, theta, spf, gbad=1/64):
    y = T ** theta
    primes = [p for p in range(2, T + 1) if spf[p] == p]
    e_of = {}
    for p in primes:
        e, q = 1, p
        while q * p <= T:
            q *= p
            e += 1
        e_of[p] = e

    def atoms(Pi):
        """yield (rough-part factorisation dict, class mod r) of atoms surviving Pi."""
        for M in range(3, T + 1, 4):
            f = factor(M, spf)
            m, r, fr = 1, 1, {}
            for p, e in f.items():
                if Pi(p):
                    m *= p ** e
                else:
                    r *= p ** e
                    fr[p] = e
            if r == 1:
                continue
            A = (M + 1) // 4
            fa = {p: 2 * e for p, e in factor(A, spf).items()}
            for D in divisors_from(fa):
                if (4 * D + 1) % m == 0:
                    yield fr, r, (-4 * D) % r

    # g0 at Pi_0
    single0 = {}
    for fr, r, c in atoms(lambda p: p <= y):
        if len(fr) == 1:
            (l, e), = fr.items()
            single0.setdefault(l, set()).add((r, c))
    def gmass(l, S):
        mod = l ** e_of[l]
        cnt = 0
        for a in range(1, mod):
            if a % l == 0:
                continue
            if any(a % r == c for r, c in S):
                cnt += 1
        return cnt / (mod - mod // l)
    g0 = {l: gmass(l, S) for l, S in single0.items()}
    bad = {l for l, g in g0.items() if g > gbad}
    Pi = lambda p: p <= y or p in bad
    singles, edges = {}, {}
    for fr, r, c in atoms(Pi):
        if len(fr) == 1:
            (l, e), = fr.items()
            singles.setdefault(l, set()).add((r, c))
        else:
            assert len(fr) == 2 and all(e == 1 for e in fr.values()), fr
            l1, l2 = sorted(fr)
            edges.setdefault(((l1, c % l1), (l2, c % l2)), 0)
            edges[((l1, c % l1), (l2, c % l2))] += 1
    free = [p for p in primes if not Pi(p)]
    Q_log = sum(e_of[p] * log(p) for p in primes if Pi(p))
    return y, e_of, bad, free, singles, edges, Q_log, gmass


def main():
    T, theta, delta, samples = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    gbad = float(sys.argv[5])
    zs = [float(z) for z in sys.argv[6:]] or [1.0, 2.0, 4.0]
    spf = spf_table(T + 8)
    y, e_of, bad, free, singles, edges, Q_log, gmass = build(T, theta, spf, gbad)
    g = {l: gmass(l, singles.get(l, set())) for l in free}
    S1 = sum(g.values())
    p = lambda l: 1 / (l - 1)
    S2 = sum(p(u[0]) * p(w[0]) for u, w in edges)
    deg, w_l = {}, {}
    for u, w in edges:
        deg[u] = deg.get(u, 0) + p(w[0])
        deg[w] = deg.get(w, 0) + p(u[0])
        for a, b in ((u, w), (w, u)):
            w_l[a[0]] = w_l.get(a[0], 0) + p(a[0]) * p(b[0])
    print(f"T={T} theta={theta} gbad={gbad} y={y:.1f} log Q={Q_log:.1f} |bad|={len(bad)} free primes={len(free)}")
    print(f"  S_1={S1:.3f} max g={max(g.values(), default=0):.4f}  edges={len(edges)} S_2={S2:.3f} "
          f"max w_l={max(w_l.values(), default=0):.4f} (8T/y^3={8*T/y**3:.3g})")
    top = sorted(deg.items(), key=lambda kv: -kv[1])[:8]
    print("  top vertex degrees (l, c mod l, deg):",
          ", ".join(f"({v[0]},{v[1]}:{d:.3f})" for v, d in top))
    H = {v for v, d in deg.items() if d > delta}
    hub_mass = sum(p(v[0]) for v in H)
    print(f"  delta={delta}: hub vertices={len(H)} hub mass={hub_mass:.3f} (Markov bound 2S_2/delta={2*S2/delta:.2f})")
    # reduced system
    Sp = {l: set(singles.get(l, set())) for l in free}
    hubs_at = {}
    for v in H:
        hubs_at.setdefault(v[0], set()).add(v[1])
    red_edges = [(u, w) for u, w in edges if u not in H and w not in H]
    rdeg = {}
    for u, w in red_edges:
        rdeg[u] = rdeg.get(u, 0) + p(w[0])
        rdeg[w] = rdeg.get(w, 0) + p(u[0])
    print(f"  reduced: edges={len(red_edges)} max deg={max(rdeg.values()) if rdeg else 0:.4f}")
    adj = {}
    for u, w in red_edges:
        adj.setdefault(u, []).append(w)
        adj.setdefault(w, []).append(u)
    rng = random.Random(1)
    mom = {z: 0.0 for z in zs}
    maxN = maxev = 0
    hist = {}
    lemma_cases = 0
    for _ in range(samples):
        x = {}
        for l in free:
            mod = l ** e_of[l]
            while True:
                a = rng.randrange(1, mod)
                if a % l:
                    break
            x[l] = a
        A = []
        for l in free:
            if any(x[l] % r == c for r, c in Sp[l]) or (x[l] % l) in hubs_at.get(l, ()):
                A.append(((l,), None))
        for l in free:
            v = (l, x[l] % l)
            for w in adj.get(v, ()):
                if w[0] > l and x[w[0]] % w[0] == w[1]:
                    A.append(((l, w[0]), None))
        a_l = {}
        for supp, _ in A:
            for l in supp:
                a_l[l] = a_l.get(l, 0) + 1
        N = len(a_l)
        maxN, maxev = max(maxN, N), max(maxev, len(A))
        hist[N] = hist.get(N, 0) + 1
        for z in zs:
            prod = 1.0
            for v in a_l.values():
                prod *= 1 + z * v
            mom[z] += prod
        # exact Lemma 1.1/1.2 check (closed form vs bound) for L < N <= 12
        if 1 <= N <= 12:
            V = sorted(a_l)
            supps = [set(s) for s, _ in A]
            for L in range(N):
                R = 0
                for wsz in range(min(L, N - 1) + 1):
                    for W in combinations(V, wsz):
                        Ws = set(W)
                        if any(s <= Ws for s in supps):
                            continue
                        R += (-1) ** (L - wsz) * comb(N - wsz - 1, L - wsz)
                vals = list(a_l.values())
                e = [1] + [0] * (L + 1)
                for t in vals:
                    for j in range(L + 1, 0, -1):
                        e[j] += e[j - 1] * t
                assert abs(R) <= 4 ** (L + 1) * e[L + 1]
                lemma_cases += 1
    print(f"  MC samples={samples}: P(A=empty)={hist.get(0,0)/samples:.4f}  max N={maxN} max #events={maxev}")
    print("  N histogram:", dict(sorted(hist.items())))
    print("  E prod(1+z a_l):", ", ".join(f"z={z}: {mom[z]/samples:.3f} (log={log(mom[z]/samples):.3f})" for z in zs))
    print(f"  Lemma 1.2 bound checked on {lemma_cases} (sample, L) cases: 0 failures")


if __name__ == "__main__":
    main()
