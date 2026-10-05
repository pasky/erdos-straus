"""OMEGA10: exact Efron-Stein generating function G_F(lam) = sum_U lam^|U| ||F^{=U}||^2
for good-indicators F of single-value systems on [q]^n.  Library + random search.
Usage: omega10_gen.py [trials] [seed]"""
import itertools, math, sys
import numpy as np


def subset_norms(F):
    """N[W] = ||E[F | X_W]||^2 for all W (bitmask over n coords)."""
    n = F.ndim
    N = np.zeros(1 << n)
    for W in range(1 << n):
        other = tuple(i for i in range(n) if not (W >> i) & 1)
        c = F.mean(axis=other) if other else F
        N[W] = (c ** 2).mean()
    return N


def es_weights(F):
    """w[U] = ||F^{=U}||^2 via Moebius inversion over subsets."""
    n = F.ndim
    w = subset_norms(F).copy()
    for i in range(n):
        bit = 1 << i
        for W in range(1 << n):
            if W & bit:
                w[W] -= w[W ^ bit]
    return w


def level_weights(F):
    n = F.ndim
    w = es_weights(F)
    lv = np.zeros(n + 1)
    for U in range(1 << n):
        lv[bin(U).count("1")] += w[U]
    return lv


def G(lv, lam):
    return sum(lv[s] * lam ** s for s in range(len(lv)))


def good_indicator(q, n, events):
    """events: list of dicts {coord: value}."""
    grids = np.indices((q,) * n)
    F = np.ones((q,) * n)
    for E in events:
        A = np.ones((q,) * n, dtype=bool)
        for c, v in E.items():
            A &= grids[c] == v
        F = F * (1 - A)
    return F


def random_system(rng, q, n, k, m):
    ev = []
    for _ in range(m):
        r = rng.integers(1, k + 1)
        cs = rng.choice(n, size=r, replace=False)
        ev.append({int(c): int(rng.integers(q)) for c in cs})
    return ev


def mass(q, events):
    return sum(q ** -len(E) for E in events)


if __name__ == "__main__":
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rng = np.random.default_rng(seed)
    worst = []
    for t in range(trials):
        q = int(rng.choice([3, 4, 5, 6]))
        n = int(rng.integers(3, 8 if q <= 4 else 7))
        k = int(rng.integers(1, min(n, 4) + 1))
        m = int(rng.integers(1, 4 * n))
        ev = random_system(rng, q, n, k, m)
        kk = max(len(E) for E in ev)
        F = good_indicator(q, n, ev)
        lv = level_weights(F)
        g2 = G(lv, 2 ** (1 / kk))
        worst.append((g2, q, n, kk, m, mass(q, ev), F.mean()))
    worst.sort(reverse=True)
    for row in worst[:15]:
        print("G(2^(1/k))=%.4f q=%d n=%d k=%d m=%d S=%.3f delta=%.4f" % row)


def hillclimb(rng, q, n, k, lam, steps=400, m0=6, weights=None):
    """Greedy/annealed search maximising G(lam) over systems of width <= k."""
    def score(ev):
        if not ev:
            return 1.0
        F = good_indicator(q, n, ev)
        if weights is None:
            return G(level_weights(F), lam)
        w = es_weights(F)
        return sum(w[U] * np.prod([weights[i] for i in range(n) if (U >> i) & 1]) for U in range(1 << n))
    ev = random_system(rng, q, n, k, m0)
    best = score(ev)
    for s in range(steps):
        new = [dict(E) for E in ev]
        r = rng.random()
        if r < 0.35 or not new:
            new += random_system(rng, q, n, k, 1)
        elif r < 0.55:
            new.pop(rng.integers(len(new)))
        else:
            i = rng.integers(len(new))
            E = new[i]
            c = int(rng.integers(n))
            if c in E and (len(E) > 1) and rng.random() < 0.3:
                del E[c]
            elif len(E) < k or c in E:
                E[c] = int(rng.integers(q))
        if not new:
            continue
        sc = score(new)
        if sc >= best or rng.random() < 0.02:
            ev, best = new, sc
    return best, ev
