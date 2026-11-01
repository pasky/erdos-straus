#!/usr/bin/env python3
"""z53 LIT F2 follow-up (revised: t(n) uses the same window N = N(hard p) as the stored D values): is the excess inverse-discrepancy of hard primes explained by small divisors of p ± 1?
Reads data/z53/lit/inverse_window.tsv; for each hard prime and its 200 prime24 controls computes
t(n) = #{x ≤ N : x | n−1} + #{x ≤ N : x | n+1} (N = floor(log² n)), fits D ~ a + b·t on the controls (OLS),
and reports the hard prime's residual z-score. Also reports the rank of D among controls with |t_c − t| ≤ 1.
Usage: uv run python scripts/z53_lit_inverse_window_adjust.py
"""
import math, collections
rows = [l.rstrip("\n").split("\t") for l in open("data/z53/lit/inverse_window.tsv")][1:]
by = collections.defaultdict(list); hard = {}
for g, hp, m, N, Np, D, G in rows:
    hp, m, N, D = int(hp), int(m), int(N), float(D)
    if g in ("star0", "b1fail", "other"): hard[hp] = (g, N, D)
    elif g == "prime24": by[hp].append((m, D))
def t(n, N): return sum(1 for x in range(1, N + 1) if (n - 1) % x == 0) + sum(1 for x in range(1, N + 1) if (n + 1) % x == 0)
zs = []
for hp, (g, N, D) in hard.items():
    th = t(hp, N); xs = [(t(m, N), d) for m, d in by[hp]]
    n = len(xs); mx = sum(a for a, _ in xs) / n; my = sum(b for _, b in xs) / n
    sxx = sum((a - mx) ** 2 for a, _ in xs); b = sum((a - mx) * (d - my) for a, d in xs) / sxx; a0 = my - b * mx
    res = [d - a0 - b * a for a, d in xs]; sd = (sum(r * r for r in res) / (n - 2)) ** 0.5
    z = (D - a0 - b * th) / sd; zs.append(z)
    near = [d for a, d in xs if abs(a - th) <= 1]
    rk = (sum(1 for d in near if d >= D) / len(near)) if near else float('nan')
    print(f"{g:7s} {hp:8d} t={th:3d} ctrl_mean_t={mx:5.1f} slope={b:+.4f} resid_z={z:+.2f} matched(n={len(near)}) P(D_c>=D)={rk:.2f}")
print(f"mean residual z over {len(zs)} hard primes: {sum(zs)/len(zs):+.2f}  (sum/sqrt(n) = {sum(zs)/len(zs)**0.5:+.2f})")
