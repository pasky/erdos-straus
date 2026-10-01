#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md §§3-5: numeric constants used in Lemma 3.2,
Theorem 4.1 and Theorem 5.1.  Each line prints a claim and True/False.
Also: at which T does the theorem's y = sqrt(T) exp(3L/log L) drop below T (U nonempty),
and below T^{0.9}?
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_constants.py
"""
import math
import numpy as np

ok = True


def claim(name, val):
    global ok
    ok &= bool(val)
    print(f"{'OK ' if val else 'BAD'} {name}")


claim("1 - 1/(13 log 6) > 1/2  (beta_1 > 1/2, so 1/beta_1 < 2)", 1 - 1 / (13 * math.log(6)) > 0.5)
# lambda_* = 1 - x^{b-1}/b > 0 for log x > 2, b in [1/2, 1)
b = np.linspace(0.5, 1 - 1e-12, 200001)
for lx in (2.0001, 3, 10, 100, 1e4):
    claim(f"lambda_*>0 at log x={lx} for all beta in [1/2,1)", np.all(1 - np.exp((b - 1) * lx) / b > 0))
u = np.exp(np.linspace(0, 200, 200001))
claim("u^{3/5}/(log u)^{1/5} >= u^{1/2} for u in (1, e^200]",
      np.all(u[1:] ** 0.6 / np.log(u[1:]) ** 0.2 >= u[1:] ** 0.5))
claim("e/22 <= e^{-2}  (so (eS/J)^J <= e^{-2J} for J >= 22S+10)", math.e / 22 <= math.exp(-2))
claim("(1/2) log(11/e) >= 0.69", 0.5 * math.log(11 / math.e) >= 0.69)
claim("0.69*(22S+10) >= 15S+6 for S>=0", 0.69 * 22 >= 15 and 0.69 * 10 >= 6)
claim("(1/2)log16*(22S+10) - S >= 29S", 0.5 * math.log(16) * 22 - 1 >= 29)
# |mu_psi| <= V/15 + e^{-15S-6} <= mu/4 with mu >= 0.99V, V >= e^{-2S}
claim("V/15 + e^{-6}e^{-13S} V <= 0.99V/4 (worst S=0)", 1 / 15 + math.exp(-6) <= 0.99 / 4)
claim("1-g >= e^{-2g} for g<=1/16", all(1 - g >= math.exp(-2 * g) for g in np.linspace(0, 1 / 16, 1001)))
claim("e^{-44S-20} <= 0.01 e^{-2S}", math.exp(-20) <= 0.01)
# Theorem 4.1 conclusion: E <= mu/(8(C0+1)M1) makes both brackets positive
for C0 in (0.5, 1, 10, 1e6):
    mu, M1 = 1.0, 1.0
    E = mu / (8 * (C0 + 1) * M1)
    claim(f"Case A/B brackets positive at C0={C0}", mu - C0 * E * M1 > 0 and mu / 2 - M1 * (2 * C0 * E + 2 * E) > 0)
# Prop 6.3 constant
claim("(2 sqrt2 /log 4)^2 = 4.16...", abs((2 * math.sqrt(2) / math.log(4)) ** 2 - 4.163) < 1e-3)
print(f"(2 sqrt2/log4)^2 = {(2 * math.sqrt(2) / math.log(4)) ** 2:.4f}")
# Where does the theorem's parameter become non-degenerate?
for target, lab in ((1.0, "y < T (U nonempty)"), (0.9, "y < T^0.9")):
    # sqrt(T) exp(3L/log L) < T^target  <=>  3/log L < target - 1/2
    L = math.exp(3 / (target - 0.5))
    print(f"theorem's y = sqrt(T)exp(3L/logL): {lab} iff log L > {3 / (target - 0.5):.2f}, i.e. log T > {L:.4g}")
print("ALL OK" if ok else "FAILURE")
