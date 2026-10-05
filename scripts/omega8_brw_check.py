#!/usr/bin/env python3
"""POINTWISE_OMEGA8 Lemma 3.1 brute-force check on small product systems.

For random event systems on Z/q^n, with u_j = Efron-Stein truncation at
level t of F^{(j)} (F_{<j} restricted to the subcube of E_j), build
    B = 1 - sum_i A_i (1 - v_i)^2,   v_i = sum_{j<i} A_j u_j
and check pointwise B <= F, the exact identity
    F - B = sum_i A_i (sum_{j<i} A_j e_j)^2,  e_j = F_{<j} - u_j,
and the bound E[F-B] <= m^2 sum_j P(E_j) energy(F^{(j)}; t).

usage: omega8_brw_check.py [trials] [seed]
"""
import sys
import numpy as np

n, q = 6, 5


def es_trunc(phi, t, axes):
    """Efron-Stein truncation of phi (array over all n axes) at level t,
    with respect to the given axes only (the others are pinned/irrelevant)."""
    M = len(axes) + 1
    out = np.zeros(phi.shape, dtype=np.complex128)
    for j in range(M):
        rho = np.exp(2j * np.pi * j / M)
        G = phi.astype(np.complex128)
        for ax in axes:
            G = rho * G + (1 - rho) * G.mean(axis=ax, keepdims=True)
        w = sum(np.exp(-2j * np.pi * j * l / M) for l in range(min(t, M - 1) + 1)) / M
        out += w * G
    return out.real


def event_indicator(ev):
    A = np.zeros((q,) * n)
    idx = [slice(None)] * n
    for (l, c) in ev:
        idx[l] = c
    A[tuple(idx)] = 1.0
    return A


def trial(rng, m, kmax, t):
    events = []
    for _ in range(m):
        k = rng.integers(1, kmax + 1)
        supp = rng.choice(n, size=k, replace=False)
        events.append(tuple((int(l), int(rng.integers(q))) for l in supp))
    A = [event_indicator(e) for e in events]
    Flt = [np.ones((q,) * n)]
    for a in A:
        Flt.append(Flt[-1] * (1 - a))
    F = Flt[-1]
    us, en = [], []
    for j, ev in enumerate(events):
        supp = [l for (l, c) in ev]
        others = [ax for ax in range(n) if ax not in supp]
        # F^{(j)} restricted to the subcube: take the slice and broadcast back
        idx = [slice(None)] * n
        for (l, c) in ev:
            idx[l] = slice(c, c + 1)
        phi = np.broadcast_to(Flt[j][tuple(idx)], (q,) * n).copy()
        u = es_trunc(phi, t, others)
        us.append(u)
        en.append(((phi - u) ** 2).mean())
    B = np.ones((q,) * n)
    rhs = np.zeros((q,) * n)
    for i in range(m):
        v = sum((A[j] * us[j] for j in range(i)), np.zeros((q,) * n))
        B -= A[i] * (1 - v) ** 2
        s = sum((A[j] * (Flt[j] - us[j]) for j in range(i)), np.zeros((q,) * n))
        rhs += A[i] * s ** 2
    viol = (B - F).max()
    ident = np.abs((F - B) - rhs).max()
    bound = m * m * sum(A[j].mean() * en[j] for j in range(m))
    return viol, ident, (F - B).mean(), bound, F.mean()


if __name__ == "__main__":
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    worst_v = worst_i = 0.0
    nb = 0
    for tr in range(trials):
        m = int(rng.integers(3, 25))
        t = int(rng.integers(0, n))
        v, i, err, bd, d = trial(rng, m, 3, t)
        worst_v, worst_i = max(worst_v, v), max(worst_i, i)
        nb += err <= bd + 1e-12
        print(f"trial {tr:3d} m={m:2d} t={t} E F={d:.4f} E[F-B]={err:.3e} bound={bd:.3e} "
              f"max(B-F)={v:+.1e} identity err={i:.1e}")
    print(f"SUMMARY trials={trials} max(B-F)={worst_v:.2e} (must be <=1e-9) "
          f"max identity err={worst_i:.2e} bound holds in {nb}/{trials}")
    ok = np.isfinite(worst_v) and np.isfinite(worst_i) and worst_v <= 1e-9 and worst_i <= 1e-9 and nb == trials
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
