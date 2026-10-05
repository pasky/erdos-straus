#!/usr/bin/env python3
"""POINTWISE_OMEGA8 §4: exact Efron-Stein level weights of good-indicators
of small product systems, versus event-level Bonferroni errors.

Coordinates X_0..X_{n-1}, each uniform on Z/q. Events are conjunctions
"X_l = c_l for l in supp". F = 1[no event occurs].

Level weights W_j = sum_{|U|=j} ||F^{=U}||^2 are computed exactly from
Phi(rho) = E[F * T_rho F] = sum_j rho^j W_j at the (n+1)-th roots of unity,
where T_rho acts on each axis by f -> rho f + (1-rho) mean_axis(f).

energy(F;t) = sum_{j>t} W_j is the optimal L2 error of a junta-t
approximation (Efron-Stein). We compare it with the L2 error of
event-level Bonferroni truncated at L events (junta <= kL).

usage: omega8_levels.py [model] ; models: disjoint, hub, all
"""
import itertools, math, sys
import numpy as np


def good_indicator(n, q, events):
    shape = (q,) * n
    F = np.ones(shape, dtype=np.float64)
    N = np.zeros(shape, dtype=np.int32)
    for ev in events:
        idx = [slice(None)] * n
        for (l, c) in ev:
            idx[l] = c
        N[tuple(idx)] += 1
    F = (N == 0).astype(np.float64)
    return F, N


def level_weights(F):
    n = F.ndim
    M = n + 1
    phis = []
    for j in range(M):
        rho = np.exp(2j * np.pi * j / M)
        G = F.astype(np.complex128)
        for ax in range(n):
            G = rho * G + (1 - rho) * G.mean(axis=ax, keepdims=True)
        phis.append((F * G).mean())
    phis = np.array(phis)
    W = np.array([(phis * np.exp(-2j * np.pi * np.arange(M) * l / M)).sum() / M
                  for l in range(M)])
    return W.real


def bonferroni_err(F, N, L):
    # event-level Bonferroni: sum_{j<=L} (-1)^j binom(N, j)
    B = np.zeros_like(F)
    for j in range(L + 1):
        B += (-1) ** j * comb_arr(N, j)
    return ((F - B) ** 2).mean(), (F - B).mean()


def comb_arr(N, j):
    out = np.ones(N.shape, dtype=np.float64)
    for i in range(j):
        out *= (N - i) / (i + 1)
    out[N < j] = 0.0
    return out


def report(name, n, q, events, k):
    F, N = good_indicator(n, q, events)
    delta = F.mean()
    W = level_weights(F)
    S = sum(q ** (-len(e)) for e in events)
    print(f"## {name}: n={n} q={q} #events={len(events)} k={k} S={S:.3f} delta=E F={delta:.5f}"
          f"  sum W={W.sum():.5f}")
    tail = np.cumsum(W[::-1])[::-1]  # tail[j] = sum_{i>=j} W_i
    print(" j   W_j/delta   energy(F;j)/delta   | L  bonf_L2err/delta (junta<=kL)")
    for j in range(n + 1):
        en = tail[j + 1] / delta if j + 1 <= n else 0.0
        line = f"{j:2d}  {W[j]/delta:10.3e}  {en:12.3e}"
        L = j
        if L <= 12:
            e2, e1 = bonferroni_err(F, N, L)
            line += f"   | {L:2d}  {e2/delta:10.3e}  (mean err {e1/delta:+.2e})"
        print(line)
    return W, delta


def model_disjoint():
    n, q, k = 9, 5, 3
    events = []
    for blk in range(3):
        coords = [3 * blk, 3 * blk + 1, 3 * blk + 2]
        for cs in itertools.product(range(q), repeat=3):
            if sum(cs) % q == 0 and cs[0] < 2:  # a spread family of patterns
                events.append(tuple(zip(coords, cs)))
    return n, q, events, k


def model_hub():
    # seeds 0..s-1, privates s..n-1; hub value 0 at seeds.
    # events {seed a=0, seed b=0, private w=c_{abw}}: all pairs, all privates
    n, q, s = 9, 5, 5
    events = []
    for a, b in itertools.combinations(range(s), 2):
        for w in range(s, n):
            c = (a + 2 * b + w) % q
            events.append(((a, 0), (b, 0), (w, c)))
    return n, q, events, 3


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("disjoint", "all"):
        n, q, ev, k = model_disjoint()
        report("disjoint supports", n, q, ev, k)
    if which in ("hub", "all"):
        n, q, ev, k = model_hub()
        report("hub cluster (two layers)", n, q, ev, k)
