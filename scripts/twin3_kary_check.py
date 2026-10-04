"""EXCEPTIONAL_TWIN3 Lemma 6.1 check: exact log(Z2/Z1^2) vs (1+25δ) Σ_σ π_σ ρ̃^σ D_σ^2
on small random hypergraph systems (events of arity 2..4, some with forced shared sub-stars
to create codegree hubs). Also checks Lemma 6.2 (promotion) bound (3).
usage: uv run --with numpy python scripts/twin3_kary_check.py [trials] [seed]"""
import sys, itertools
import numpy as np

def Zs(sizes, events, nus, rho):
    k = len(sizes); A = np.ones(sizes)
    for E in events:
        idx = [slice(None)] * k
        for (l, c) in E: idx[l] = c
        A[tuple(idx)] = 0.0
    P = np.ones(sizes)
    for l in range(k):
        sh = [1] * k; sh[l] = sizes[l]; P = P * nus[l].reshape(sh)
    Z1 = float((A * P).sum()); T = A.copy()
    for l in range(k):
        nu = nus[l]; M = rho[l] * np.diag(nu) + (1 - rho[l]) * np.outer(nu, nu)
        T = np.moveaxis(np.tensordot(M, T, axes=([1], [l])), 0, l)
    return Z1, float((T * A).sum())

def pi(s, nus): return float(np.prod([nus[l][c] for (l, c) in s])) if s else 1.0

def star_sum(events, nus, rho, cap):
    stars = set()
    for E in events:
        for r in range(1, len(E) + 1):
            for s in itertools.combinations(E, r): stars.add(frozenset(s))
    tot = 0.0
    for s in stars:
        D = sum(pi(E - s, nus) for E in events if s <= E)
        if cap and len(s) >= 2: D = min(D, 1.0)
        tot += pi(s, nus) * np.prod([rho[l] for (l, _) in s]) * D * D
    return tot

def promote(events, nus):
    ev = set(events)
    while True:
        ev = {E for E in ev if not any(F < E for F in ev)}  # drop redundant
        hub = None
        for E in ev:
            for r in range(2, len(E)):
                for s in itertools.combinations(E, r):
                    s = frozenset(s)
                    if s in ev: continue
                    if sum(pi(F - s, nus) for F in ev if s <= F) > 1: hub = s; break
                if hub: break
            if hub: break
        if not hub: return ev
        ev = {E for E in ev if not hub <= E} | {hub}

def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    worst = 0.0; worst2 = 0.0; inside = 0; npromo = 0
    for _ in range(trials):
        k = int(rng.integers(3, 6)); sizes = [int(rng.integers(3, 8)) for _ in range(k)]
        nus = [rng.dirichlet(np.ones(s) * rng.uniform(0.5, 3)) for s in sizes]
        rho = rng.uniform(0, 1, k)
        events = set(); base = None
        for _ in range(int(rng.integers(2, 12))):
            r = int(rng.integers(2, min(4, k) + 1))
            if base is not None and rng.random() < 0.5:   # share a sub-star -> codegree hub
                E = dict(base)
                extra = [l for l in range(k) if l not in E]
                for l in rng.permutation(extra)[: max(0, r - len(E))]: E[int(l)] = int(rng.integers(sizes[l]))
            else:
                ls = rng.choice(k, r, replace=False); E = {int(l): int(rng.integers(sizes[l])) for l in ls}
                if base is None: base = dict(list(E.items())[:2])
            if len(E) >= 2: events.add(frozenset(E.items()))
        events = {E for E in events if not any(F < E for F in events)}
        w = np.zeros(k)
        for E in events:
            for (l, _) in E: w[l] += pi(E, nus)
        delta = max(sum(w[l] for (l, _) in E) for E in events)
        Z1, Z2 = Zs(sizes, events, nus, rho); lhs = np.log(Z2 / Z1 ** 2)
        rhs = star_sum(events, nus, rho, cap=False)
        ev2 = promote(events, nus); npromo += (ev2 != events)
        Z1p, Z2p = Zs(sizes, ev2, nus, rho); lhs2 = np.log(Z2p / Z1p ** 2)
        rhs2 = star_sum(events, nus, rho, cap=True)
        if delta <= 1 / 16:
            inside += 1
            worst = max(worst, lhs / ((1 + 25 * delta) * rhs))
            worst2 = max(worst2, lhs2 / ((1 + 25 * delta) * rhs2))
    print(f"trials={trials} inside(H_δ)={inside} promoted={npromo} "
          f"max lhs/((1+25δ)rhs) Lemma6.1={worst:.4f}  Lemma6.2(3)={worst2:.4f}")

main()
