"""R116 from-scratch exponent bookkeeping for EXCEPTIONAL_TYPEI_LOGLOG2 Thm 3.1 / Cor 3.2 / Thm 4.1.

Everything in log_N units; constants and log factors ignored (they are 𝓛^C).
Raw route (independent of the author's three-term simplification):
  Σ_d|E_d| ≤ q (Σ_d #Λ_d)^{1/2} (Σ_d V_d)^{1/2},  Σ_d #Λ_d ≈ D^{3/2},
  Σ_d V_d^gen ≈ D·(λ/Y0)(1+λ) + N^{ε1} q^{-3/2}/Y0               (TTL Prop 5.1 summed over d ≍ D),
  Σ_d 𝓔_d    ≈ N^{6ε} Y0^{-1}[λ₋ M0 + 1 + λ₋ Y0^{-1/2}]             (Prop 2.2),
  M0 = 8Dq², Y0 = 1/(2qF'√D), λ = A/(qF'), λ₋ = min(λ,1); relative error = Σ_d|E_d| / (A D).
Claims checked: rel ≤ q² N^{-δ/4} N^{3ε} (Cor 3.2) in cases (b2),(b3),(b5), and M0/(λ₋Y0) ≤ N³;
also the author's 3-term form of Thm 3.1 dominates the raw expression.
"""
import sys

import numpy as np

rng = np.random.default_rng(1162)
eta, eta1, eps1 = 0.02, 0.02, 0.01

def raw_rel(a, dD, fp, tq, eps):
    lam = a - tq - fp
    lam_m = min(lam, 0.0)
    y0inv = tq + fp + dD / 2
    M0 = dD + 2 * tq
    lam_over_Y0 = lam + y0inv
    Vgen = max(dD + lam_over_Y0 + max(0.0, lam), eps1 - 1.5 * tq + y0inv)
    Eexc = 6 * eps + y0inv + max(lam_m + M0, 0.0, lam_m + y0inv / 2)
    V = max(Vgen, Eexc)
    sumE = tq + 0.75 * dD + V / 2
    return sumE - (a + dD), lam_m, y0inv, M0

def author_terms(a, dD, fp, tq, eps):
    lam = a - tq - fp
    T1 = 2 * tq + (dD - a) / 2 + max(0.0, lam) / 2
    T2 = 1.5 * tq + fp / 2 - a + eps1 / 2
    T3 = 1.25 * tq + fp / 4 + dD / 8 - a / 2
    return max(T1, T2, T3) + 3 * eps

viol = {"b2": 0, "b3": 0, "b5": 0}
cnt = {"b2": 0, "b3": 0, "b5": 0}
worst_slack = {k: -9.0 for k in viol}
dom_fail = 0
n3_fail = 0
NSAMP = int(sys.argv[1]) if len(sys.argv) > 1 else 400000  # O119: optional reduced sample
for _ in range(NSAMP):
    gam = rng.uniform(0, eta)
    delta = rng.uniform(1e-4, 0.6)
    a = (1 - gam + delta) / 2              # δ = 2α − 1 + γ > 0  (D < A side)
    dD = 1 - a - gam
    if dD <= 0:
        continue
    tq = rng.uniform(0, delta / 64)
    eps = rng.uniform(0, delta / 128)
    case = rng.choice(["b2", "b3", "b5"])
    if case == "b2":
        if delta < 2 * gam:
            continue
        beta = rng.uniform(a - 1e-3, a + gam)  # α ≤ β < α+γ (and a/2 ≤ b < a cells)
        fp = beta - gam                     # F' = e ≍ N^{β−γ} ≤ 4A
    elif case == "b3":
        beta = rng.uniform(a + gam, 1)
        fe, ff = beta - gam, 1 + a - beta
        fp = min(fe, ff)
        if fp < a:                          # F' ≥ 8A off the bands
            continue
    else:
        beta = rng.uniform(1, 1 + 2 * eta1)
        if beta - 1 > delta / 2:            # (b5) spectral branch needs A/f ≤ N^{δ/2}
            continue
        fp = 1 + a - beta                   # F' = f ≤ A
    cnt[case] += 1
    r, lam_m, y0inv, M0 = raw_rel(a, dD, fp, tq, eps)
    target = 2 * tq - delta / 4 + 3 * eps
    if r > target + 1e-12:
        viol[case] += 1
    worst_slack[case] = max(worst_slack[case], r - target)
    if author_terms(a, dD, fp, tq, eps) < r - 1e-12:
        dom_fail += 1
    if M0 - lam_m + y0inv > 3:
        n3_fail += 1

print("cases sampled:", cnt)
print("Cor 3.2 violations (raw rel > 2θq − δ/4 + 3ε):", viol)
print("max(raw − target) per case (≤ 0 means OK):", {k: round(v, 5) for k, v in worst_slack.items()})
print("author 3-term form fails to dominate raw:", dom_fail)
print("M0/(λ₋Y0) > N^3:", n3_fail)

# Sieve total (Thm 4.1 proof): Σ_{q≤Q} 3^{ω(q)} q² · N^{-δ/4+4ε} with Q = N^{δ/64}, ε = w/128 ≤ δ/128
d = np.linspace(1e-3, 1, 1000)
tot = 3 * d / 64 - d / 4 + 4 * (d / 128)
print("max over δ of (sieve exponent + 11δ/64):", float(np.max(tot + 11 * d / 64)))
