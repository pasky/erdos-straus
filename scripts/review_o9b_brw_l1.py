"""R34b from-scratch check of OMEGA9 Lemma 2.1 on toy BRW minorants (O8 Lemma 3.1).

Coordinates X_l uniform on Z/q_l (small), random single-value events with
supports <= k, F = 1[no event], B = 1 - sum_i A_i (1 - v_i)^2,
v_i = sum_{j<i} A_j u_j, with u_j either random or the Efron-Stein truncation
of F^{(j)} (computed exactly on the product space).  Checks B <= F pointwise,
E|B| = EB + 2E[B^-], B^- <= F - B, and E|B| <= (1+2eta) EB, eta = E[F-B]/EB.
Usage: review_o9b_brw_l1.py [ntrials]
"""
import sys, itertools
import numpy as np

ntr = int(sys.argv[1]) if len(sys.argv) > 1 else 200
rng = np.random.default_rng(7)


def es_trunc(phi, shape, t):
    """Efron-Stein truncation at level t of phi (array on product space)."""
    n = len(shape)
    out = np.zeros(shape)
    for r in range(t + 1):
        for U in itertools.combinations(range(n), r):
            # phi^{=U} = sum_{W subset U} (-1)^{|U-W|} E[phi|X_W]
            comp = np.zeros(shape)
            for s in range(r + 1):
                for W in itertools.combinations(U, s):
                    other = tuple(a for a in range(n) if a not in W)
                    m = phi.mean(axis=other, keepdims=True) if other else phi
                    comp += (-1) ** (r - s) * np.broadcast_to(m, shape)
            out += comp
    return out


worst = -np.inf
minF_B = np.inf
cnt = 0
for tr in range(ntr):
    shape = tuple(int(x) for x in rng.integers(2, 5, size=int(rng.integers(3, 6))))
    n = len(shape)
    grids = np.meshgrid(*[np.arange(q) for q in shape], indexing="ij")
    m = int(rng.integers(2, 7))
    k = 2
    A = []
    for _ in range(m):
        supp = rng.choice(n, size=int(rng.integers(1, k + 1)), replace=False)
        ev = np.ones(shape, bool)
        for a in supp:
            ev &= grids[a] == rng.integers(shape[a])
        A.append(ev.astype(float))
    F = np.prod([1 - a for a in A], axis=0)
    mode = tr % 3
    v = np.zeros(shape)
    B = np.ones(shape)
    Fprev = np.ones(shape)
    for i in range(m):
        B -= A[i] * (1 - v) ** 2
        if mode == 0:
            u = rng.normal(size=shape)
        else:
            u = es_trunc(Fprev, shape, t=mode)  # crude: truncate F_{<i} itself
        v = v + A[i] * u
        Fprev = Fprev * (1 - A[i])
    minF_B = min(minF_B, (F - B).min())
    EB = B.mean()
    if EB <= 0:
        continue
    cnt += 1
    Bm = np.maximum(-B, 0)
    assert np.all(Bm <= F - B + 1e-12)
    assert abs(np.abs(B).mean() - (EB + 2 * Bm.mean())) < 1e-12
    eta = (F - B).mean() / EB
    worst = max(worst, np.abs(B).mean() - (1 + 2 * eta) * EB)
print(f"trials={ntr}, with EB>0: {cnt}; min(F-B)={minF_B:.3e} (>=0 expected); "
      f"max(E|B|-(1+2eta)EB)={worst:.3e} (<=0 expected)")
