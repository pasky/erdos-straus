"""R38 from-scratch check of C-1 (Cor 3.5): G_F(lam) <= 1 when all w_E <= 2.

Independent of the author's scripts.  G_F = sum_V mu^V ||L_V F||^2 with
L_v = I - E_v (E_v = average over coordinate v), uniform measure on
prod [q_v].  Also checks the identity G_F = sum_U lam^U ||F^{=U}||^2
(Efron-Stein via inclusion-exclusion of conditional expectations) on small
cases, and does random search + hill-climbing for violations.

usage: review_o10_c1.py seed ntrials mode   (mode: rand | hc | exact)
"""
import sys, itertools, random
from fractions import Fraction
import numpy as np


def Lv(arr, v):
    return arr - arr.mean(axis=v, keepdims=True)


def G_float(F, lam):
    n = F.ndim
    tot = 0.0
    # iterate over subsets V via DFS applying L_v
    def rec(arr, v, coef):
        nonlocal tot
        if v == n:
            tot += coef * float((arr * arr).mean())
            return
        rec(arr, v + 1, coef)
        mu = lam[v] - 1.0
        if mu != 0:
            rec(Lv(arr, v), v + 1, coef * mu)
    rec(F.astype(float), 0, 1.0)
    return tot


def G_es(F, lam):
    """sum_U lam^U ||F^{=U}||^2 with F^{=U} = sum_{W subset U} (-1)^{|U-W|} E[F|W]."""
    n = F.ndim
    cond = {}
    for W in itertools.product([0, 1], repeat=n):
        axes = tuple(i for i in range(n) if not W[i])
        cond[W] = F.mean(axis=axes, keepdims=True) if axes else F.astype(float)
    tot = 0.0
    for U in itertools.product([0, 1], repeat=n):
        comp = 0.0
        Uset = [i for i in range(n) if U[i]]
        for r in range(len(Uset) + 1):
            for Ws in itertools.combinations(Uset, r):
                W = tuple(1 if i in Ws else 0 for i in range(n))
                comp = comp + (-1) ** (len(Uset) - r) * cond[W]
        comp = np.broadcast_to(comp, F.shape)
        tot += np.prod([lam[i] for i in Uset]) * float((comp * comp).mean())
    return tot


def build_F(qs, events):
    F = np.ones(qs, dtype=np.int8)
    for ev in events:  # ev: dict v->value
        idx = tuple(ev.get(v, slice(None)) for v in range(len(qs)))
        F[idx] = 0
    return F


def normalize_lam(lam_raw, events):
    """scale log lam so that max_E w_E == 2 exactly (boundary)."""
    logs = np.log(lam_raw).copy()
    used = set(v for ev in events for v in ev)
    for v in range(len(logs)):
        if v not in used:
            logs[v] = 0.0
    m = max(sum(logs[v] for v in ev) for ev in events)
    if m <= 1e-9:
        return None
    return np.exp(logs * (np.log(2) / m))


def rand_system(rng, n, qs, ne, kmax):
    evs = []
    for _ in range(ne):
        k = rng.randint(1, min(kmax, n))
        S = rng.sample(range(n), k)
        evs.append({v: rng.randrange(qs[v]) for v in S})
    return evs


def rand_lam(rng, n, style):
    if style == 0:
        return np.array([1 + rng.random() for _ in range(n)])
    if style == 1:  # very non-uniform
        return np.array([1 + rng.random() ** 4 * 10 for _ in range(n)])
    return np.array([rng.choice([1.0, 1.0001, 2.0, 1 + rng.random()]) for _ in range(n)])


def main():
    seed, ntr, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    worst = (-1, None)
    if mode == "exact":
        # identity check G_float == G_es on small cases
        mx = 0
        for t in range(ntr):
            n = rng.randint(1, 4)
            qs = [rng.randint(2, 4) for _ in range(n)]
            evs = rand_system(rng, n, qs, rng.randint(1, 6), n)
            F = build_F(qs, evs)
            lam = np.array([1 + 2 * rng.random() for _ in range(n)])
            mx = max(mx, abs(G_float(F, lam) - G_es(F, lam)))
        print("identity max discrepancy", mx)
        return
    for t in range(ntr):
        n = rng.randint(1, 7)
        qs = [rng.randint(2, 4) for _ in range(n)]
        if np.prod(qs) > 5000:
            continue
        ne = rng.randint(1, 3 * n + 4)
        evs = rand_system(rng, n, qs, ne, rng.randint(1, n))
        lam = normalize_lam(rand_lam(rng, n, t % 3), evs)
        if lam is None:
            continue
        g = G_float(build_F(qs, evs), lam)
        if mode == "hc":
            for it in range(60):
                evs2 = [dict(e) for e in evs]
                r = rng.random()
                if r < 0.3 and len(evs2) > 1:
                    evs2.pop(rng.randrange(len(evs2)))
                elif r < 0.6:
                    evs2 += rand_system(rng, n, qs, 1, n)
                else:
                    e = rng.choice(evs2)
                    v = rng.choice(list(e))
                    e[v] = rng.randrange(qs[v])
                lam2 = lam * np.exp(np.array([rng.gauss(0, 0.1) for _ in range(n)]))
                lam2 = np.maximum(lam2, 1.0)
                lam2 = normalize_lam(lam2, evs2)
                if lam2 is None:
                    continue
                g2 = G_float(build_F(qs, evs2), lam2)
                if g2 >= g:
                    evs, lam, g = evs2, lam2, g2
        if g > worst[0]:
            worst = (g, (qs, evs, list(lam)))
    print("max G =", worst[0])
    print("argmax", worst[1])


if __name__ == "__main__":
    main()
