#!/usr/bin/env python3
"""POINTWISE_OMEGA11 Lemma 1.1 (filtration C-1): exact check on random digit systems.

Coordinates ("primes") l = 0..P-1, each with f_l digits, every digit uniform on [q_l].
Events fix an initial segment of digits 0..v-1 at each l in their support.
G'_F = sum_U prod_l Lambda_{l, max U_l} ||F^{=U}||^2 with Lambda_{l,i} = lam_l^(i+1).
Lemma 1.1: if every event has prod_l lam_l^(2 v_l) <= 2 then G' <= 1.
Also tested: the hypergraph form (edge weight prod (1+mu') <= 2), conditioned systems
(F restricted to an event cylinder, as O8's F^(j)), and the rho=1 scaling
(prod lam^v <= 2) to see whether the factor 2 is needed.

usage: omega11_filtration.py SEED NTRIALS
"""
import sys
import itertools
import random
import numpy as np


def es_energies(Fa, ndig):
    """Fa: array of shape (q_1,...,q_n). Return dict U(bitmask)->||F^{=U}||^2."""
    n = ndig
    # conditional expectations E[F | X_W] as arrays broadcast over full space
    cond = {}
    for W in range(1 << n):
        axes = tuple(i for i in range(n) if not (W >> i) & 1)
        cond[W] = Fa.mean(axis=axes, keepdims=True) if axes else Fa
    out = {}
    for U in range(1 << n):
        acc = np.zeros(Fa.shape)
        W = U
        while True:
            sign = (-1) ** (bin(U).count("1") - bin(W).count("1"))
            acc = acc + sign * cond[W]
            if W == 0:
                break
            W = (W - 1) & U
        out[U] = float((acc ** 2).mean())
    return out


def trial(rng, mode):
    P = rng.randint(1, 3)
    f = [rng.randint(1, 3) for _ in range(P)]
    while sum(f) > 7:
        f = [rng.randint(1, 3) for _ in range(P)]
    q = [rng.choice([2, 3]) for _ in range(P)]
    digs = [(l, i) for l in range(P) for i in range(f[l])]
    n = len(digs)
    shape = tuple(q[l] for (l, i) in digs)
    if np.prod(shape) > 3000:
        return None
    nev = rng.randint(1, 6)
    events = []
    for _ in range(nev):
        supp = [l for l in range(P) if rng.random() < 0.6] or [rng.randrange(P)]
        v = {l: rng.randint(1, f[l]) for l in supp}
        val = {(l, i): rng.randrange(q[l]) for l in supp for i in range(v[l])}
        events.append((v, val))
    lam = [1 + rng.random() * 2 for _ in range(P)]
    # scale so the binding constraint is tight
    power = 1 if mode == "rho1" else 2
    worst = max(sum(power * v[l] * np.log(lam[l]) for l in v) for v, _ in events)
    s = np.log(2) / worst
    lam = [float(np.exp(np.log(x) * s)) for x in lam]
    grids = np.indices(shape)
    F = np.ones(shape)
    for v, val in (events[1:] if mode == "cond" else events):
        hit = np.ones(shape, dtype=bool)
        for (l, i), c in val.items():
            hit &= grids[digs.index((l, i))] == c
        F[hit] = 0
    if mode == "cond":
        # restrict to first event's cylinder: fix its digits, keep remaining digits
        v0, val0 = events[0]
        idx = tuple(val0.get(d, slice(None)) for d in digs)
        F = F[idx]
        digs = [d for d in digs if d not in val0]
        n = len(digs)
        if n == 0:
            return None
    en = es_energies(F, n)
    G = 0.0
    for U, e in en.items():
        w = 1.0
        for l in range(P):
            mx = -1
            for b, (ll, i) in enumerate(digs):
                if ll == l and (U >> b) & 1:
                    mx = max(mx, i)
            if mx >= 0:
                w *= lam[l] ** (mx + 1)
        G += w * e
    return G


def main():
    seed, N = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    for mode in ["rho2", "cond", "rho1"]:
        mx, cnt = 0.0, 0
        for _ in range(N):
            G = trial(rng, mode)
            if G is None:
                continue
            cnt += 1
            mx = max(mx, G)
        print(f"mode={mode}: {cnt} systems, max G' = {mx:.6f}")


if __name__ == "__main__":
    main()
