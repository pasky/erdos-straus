"""OMEGA9 Lemma 4.1 check: exact Efron-Stein energies of F = prod(1-A_i) for
disjoint single-value events (m events, k coords each, uniform on [q]) vs the
lower bound (1-pi)^{2m} sum_{j>t/k} C(m,j) rho^j.  Usage: omega9_junta_lb.py"""
import itertools, math
import numpy as np

def es_level_weights(F, n):
    # F: array of shape (q,)*n ; returns weight per level via Möbius over subsets
    w = np.zeros(n + 1)
    cond = {}
    for r in range(n + 1):
        for W in itertools.combinations(range(n), r):
            other = tuple(i for i in range(n) if i not in W)
            cond[W] = F.mean(axis=other, keepdims=True) if other else F
    for r in range(n + 1):
        for U in itertools.combinations(range(n), r):
            comp = 0
            for rr in range(r + 1):
                for W in itertools.combinations(U, rr):
                    comp = comp + (-1) ** (r - rr) * cond[W]
            comp = np.broadcast_to(comp, F.shape)
            w[r] += (comp ** 2).mean()
    return w

out = []
for q, k, m in [(5, 2, 3), (4, 3, 2), (7, 1, 6), (3, 2, 3)]:
    n = k * m
    grids = np.indices((q,) * n)
    F = np.ones((q,) * n)
    for i in range(m):
        A = np.ones((q,) * n, dtype=bool)
        for c in range(i * k, (i + 1) * k):
            A &= grids[c] == 0
        F = F * (1 - A)
    w = es_level_weights(F, n)
    pi = q ** -k
    rho = pi * (1 - 1 / q) ** k / (1 - pi) ** 2
    ok = True
    for t in range(n + 1):
        energy = w[t + 1:].sum()
        lb = (1 - pi) ** (2 * m) * sum(math.comb(m, j) * rho ** j for j in range(m + 1) if j > t / k)
        ok &= energy >= lb - 1e-12
        out.append(f"q={q} k={k} m={m} t={t}: energy={energy:.6e} lower_bound={lb:.6e}")
    out.append(f"  delta={F.mean():.6f} total={w.sum():.6f} ok={ok}")
    assert ok and abs(w.sum() - F.mean()) < 1e-9
print("\n".join(out))
