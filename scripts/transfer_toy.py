"""O42 toy check of the abstract transfer machinery (POINTWISE_TRANSFER §§2-3).

Exact Haar computation on prod_l (Z/l)^x for a few small primes, with
*general* events (several classes, width <= 2). Checks, for random systems:
  * BRW sandwich over atoms: B <= F pointwise, identity
    F-B = sum_i A_i (sum_{j<i} A_j e_j)^2, and E[F-B] <= m_a^2 sum_j P(C_j) En(F^(j);t)
  * l1-tightness  E|B| <= E B + 2E[F-B]
  * Lemma 3.2 chain: |E[F psi]| <= delta^(l0) - delta for every real primitive
    psi (products of Legendre symbols) and every l0 | cond(psi)
  * least prime p avoiding all events vs Haar density (sanity only).
Run: PYTHONPATH=scripts uv run python scripts/transfer_toy.py   (~seconds)
"""
import itertools, random
import numpy as np

PR = [5, 7, 11, 13, 17]
n = len(PR)
shape = tuple(l - 1 for l in PR)            # index v <-> unit v+1

def legendre(a, l):
    r = pow(int(a), (l - 1) // 2, l)
    return -1 if r == l - 1 else r

def cond_exp(phi, W):
    ax = tuple(i for i in range(n) if i not in W)
    return phi.mean(axis=ax, keepdims=True) if ax else phi

def trunc(phi, t):
    out = np.zeros(shape)
    from math import comb
    for r in range(n + 1):
        for W in itertools.combinations(range(n), r):
            c = sum(comb(n - r, i) * (-1) ** i for i in range(0, t - r + 1)) if t >= r else 0
            if c:
                out = out + c * cond_exp(phi, W)
    return out

def cell(supp, vals):
    a = np.zeros(shape)
    idx = [slice(None)] * n
    for i, v in zip(supp, vals):
        idx[i] = v
    a[tuple(idx)] = 1.0
    return a

def run(seed, t):
    rng = random.Random(seed)
    events = []
    for _ in range(rng.randint(6, 14)):
        w = rng.choice([1, 2, 2])
        supp = tuple(sorted(rng.sample(range(n), w)))
        allv = list(itertools.product(*[range(shape[i]) for i in supp]))
        events.append((supp, set(map(tuple, rng.sample(allv, rng.randint(1, 2 if w == 1 else 4))))))
    atoms = sorted({(s, v) for s, vs in events for v in vs})
    A = [cell(s, v) for s, v in atoms]
    F = np.ones(shape)
    for a in A:
        F = F * (1 - a)
    delta = F.mean()
    # sandwich
    Flt = np.ones(shape); us = []; es_bound = 0.0
    for (s, v), a in zip(atoms, A):
        idx = [slice(None)] * n
        for i, x in zip(s, v):
            idx[i] = slice(x, x + 1)
        Fj = np.broadcast_to(Flt[tuple(idx)], shape).copy()   # F^(j)
        u = trunc(Fj, t)
        es_bound += a.mean() * ((Fj - u) ** 2).mean()
        us.append(u)
        Flt = Flt * (1 - a)
    B = np.ones(shape); rhs = np.zeros(shape); acc = np.zeros(shape); v = np.zeros(shape)
    for a, u, (s, vv) in zip(A, us, atoms):
        B -= a * (1 - v) ** 2
        rhs += a * acc ** 2
        Fl = np.ones(shape)
        v = v + a * u
    # recompute e_j-based identity
    Flt = np.ones(shape); acc = np.zeros(shape); rhs = np.zeros(shape)
    for a, u in zip(A, us):
        rhs += a * acc ** 2
        acc = acc + a * (Flt - u)
        Flt = Flt * (1 - a)
    assert (B <= F + 1e-9).all()
    assert np.allclose(F - B, rhs)
    gap = (F - B).mean(); ma = len(atoms)
    assert gap <= ma ** 2 * es_bound + 1e-12
    assert np.abs(B).mean() <= B.mean() + 2 * gap + 1e-12
    # Lemma 3.2 chain
    leg = []
    for i, l in enumerate(PR):
        sh = [1] * n; sh[i] = l - 1
        leg.append(np.array([legendre(a, l) for a in range(1, l)], float).reshape(sh))
    Fp = {}
    for l0 in range(n):
        G = np.ones(shape)
        for (s, vs) in events:
            if l0 not in s:
                for vv in vs:
                    G = G * (1 - cell(s, vv))
        Fp[l0] = G.mean()
    worst = 0.0
    for r in range(1, n + 1):
        for f in itertools.combinations(range(n), r):
            psi = np.ones(shape)
            for i in f:
                psi = psi * leg[i]
            EFpsi = abs((F * psi).mean())
            for l0 in f:
                assert EFpsi <= Fp[l0] - delta + 1e-12
            worst = max(worst, EFpsi / delta if delta else 0)
    # least prime avoiding
    def avoids(p):
        x = tuple(p % l - 1 for l in PR)
        return all(tuple(x[i] for i in s) not in vs for s, vs in events)
    p = max(PR) + 1
    while delta > 0 and p < 10**7:
        p += 1
        if all(p % q for q in range(2, int(p ** .5) + 1)) and avoids(p):
            break
    return dict(seed=seed, atoms=ma, S=sum(len(vs) / np.prod([shape[i] for i in s]) for s, vs in events),
                delta=round(delta, 4), gap=round(gap, 5), A=round(np.abs(B).mean() / B.mean(), 4) if B.mean() > 0 else None,
                max_twist=round(worst, 3), least_p=p if delta > 0 else None)

if __name__ == "__main__":
    for seed in range(6):
        for t in (1, 2, 3):
            print(t, run(seed, t), flush=True)
