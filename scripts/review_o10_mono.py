"""R38: from-scratch check of the MONO counterexample (§2) and the
single-event formula G_{1_C}=pi*prod(lam-(lam-1)/q)."""
import itertools, numpy as np
from review_o10_c1 import G_float, build_F

def mono(q, n):
    lam = np.array([2 ** (1 / n)] * n)
    qs = [q] * n
    evs = []
    for c in itertools.product(range(q), repeat=n):
        mis = sum(1 for x in c if x != 0)
        if mis >= 2 and mis % 2 == 0:
            evs.append(dict(enumerate(c)))
    g0 = G_float(build_F(qs, evs), lam)
    g1 = G_float(build_F(qs, evs + [dict(enumerate([0] * n))]), lam)
    return g0, g1

for q, n in [(8, 2), (5, 3)]:
    print("MONO cex q=%d n=%d: G_F=%.5f  G_F(1-A)=%.5f" % ((q, n) + mono(q, n)))
rng = np.random.default_rng(0)
mx = 0
for _ in range(200):
    n = rng.integers(1, 5); qs = list(rng.integers(2, 5, n)); lam = 1 + 2 * rng.random(n)
    c = {v: int(rng.integers(qs[v])) for v in range(n)}
    C = 1 - build_F(qs, [c])
    pi = 1 / np.prod(qs)
    mx = max(mx, abs(G_float(C, lam) - pi * np.prod(lam - (lam - 1) / np.array(qs))))
print("single-event formula max err", mx)
