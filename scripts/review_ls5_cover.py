"""Review R67b: independent re-computation of LS5 §5 [2] (covering correlation
ratios P(E_S)/prod P(l covered)) for the full R(M) family over a prime pool,
product model, exact enumeration with numpy (no selectors, as in LS5 §5).
"""
import itertools, sys
from math import prod
import numpy as np

POOL = [int(t) for t in (sys.argv[1] if len(sys.argv) > 1 else "7,11,19,23,31,43").split(",")]


def divisors(n):
    out, d = [], 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out


classes = []
for k in range(1, len(POOL) + 1):
    for Ps in itertools.combinations(POOL, k):
        M = prod(Ps)
        if M % 4 != 3:
            continue
        A = (M + 1) // 4
        for D in divisors(A * A):
            classes.append((Ps, {p: (-4 * D) % p for p in Ps}))
print(f"pool {POOL}: {len(classes)} classes; grid {prod(POOL):.3e} points")
shape = POOL
idx = {p: i for i, p in enumerate(POOL)}
cov = {p: np.zeros(shape, dtype=bool) for p in POOL}
# matched mask of a class = outer AND of 1-D indicator vectors
for Ps, b in classes:
    m = None
    for p in Ps:
        v = np.zeros(p, dtype=bool); v[b[p]] = True
        sh = [1] * len(POOL); sh[idx[p]] = p
        v = v.reshape(sh)
        m = v if m is None else (m & v)
    m = np.broadcast_to(m, shape)
    for p in Ps:
        cov[p] |= m
single = {p: cov[p].mean() for p in POOL}
print("P(l covered):", {p: round(float(single[p]), 4) for p in POOL})
for k in range(2, len(POOL) + 1):
    best = 0
    for S in itertools.combinations(POOL, k):
        E = np.logical_and.reduce([cov[p] for p in S])
        r = E.mean() / prod(single[p] for p in S)
        best = max(best, r)
    print(f"|S|={k}: max P(E_S)/prod = {best:.3f}, per prime {best ** (1 / k):.3f}")
