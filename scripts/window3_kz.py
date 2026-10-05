#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §4.1: constants K(zeta) of the switched upper sieve that also sifts the
other window to x^zeta (composition: linear upper sieve for primality of p at level x^{th1},
semi-linear upper sieve for n_q' at level x^{th2}, th1+th2=1/2).
  K(zeta) = min_{th2} (2/th1) * F_half(th2/zeta) / sigma_even(zeta)
F_half: Iwaniec's semi-linear upper function (beta=1): F=2(e^g/(pi s))^{1/2} on (0,2],
  (s^{1/2}F)'=(1/2)s^{-1/2}f(s-1), (s^{1/2}f)'=(1/2)s^{-1/2}F(s-1) (s>1 for f), f=0 on (0,1].
sigma_even(zeta) = [mu_even(no point < zeta)/M_even] * (zeta/eps)^{1/2}  (model truth, even law).
Usage: window3_kz.py EPS K [N]
"""
import sys, numpy as np
from math import exp, pi, sqrt
import window3_model as M
EG = exp(0.5772156649015329)
h = 1e-4; S = np.arange(1, 400001) * h          # s in (0, 40]
F = np.zeros_like(S); f = np.zeros_like(S)
F[S <= 2] = 2 * np.sqrt(EG / (pi * S[S <= 2]))
m13 = (S > 1) & (S <= 3)
u = S[m13]; f[m13] = np.sqrt(EG / (pi * u)) * 2 * np.log(np.sqrt(u) + np.sqrt(u - 1))  # ∫_1^u dt/sqrt(t(t-1)) = 2 acosh(sqrt u)
def lag(arr, s):  # arr(s-1)
    i = int(round((s - 1) / h)) - 1
    return arr[i] if i >= 0 else 0.0
# integrate F for s>2 and f for s>3 (trapezoid on the delay equations)
i2 = int(round(2 / h)) - 1; i3 = int(round(3 / h)) - 1
for i in range(min(i2, i3) + 1, len(S)):
    s = S[i]; sp_ = S[i - 1]
    if s > 2:
        F[i] = (sqrt(sp_) * F[i - 1] + 0.25 * h * (lag(f, s) / sqrt(s) + lag(f, sp_) / sqrt(sp_))) / sqrt(s)
    if s > 3:
        f[i] = (sqrt(sp_) * f[i - 1] + 0.25 * h * (lag(F, s) / sqrt(s) + lag(F, sp_) / sqrt(sp_))) / sqrt(s)
def Fh(s):
    return float(np.interp(s, S, F)) if s <= S[-1] else 1.0
if __name__ == "__main__":
    print("F_half(s):", {s: round(Fh(s), 4) for s in (0.5, 1, 1.5, 2, 3, 4, 6, 10)},
          " f(3),f(6):", round(float(np.interp(3, S, f)), 4), round(float(np.interp(6, S, f)), 4))
    eps, K = float(sys.argv[1]), int(sys.argv[2]); N = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    L = M.Law(eps, K, N); W = M.window_configs(L.e, 0); mu = np.array([L.mu(m) for m in W])
    for j in range(K + 1):
        z = L.e[j]
        okZ = np.array([all(C[k] == 0 for k in range(j)) for C in W])
        P = mu[okZ].sum() / mu.sum(); sig = P * sqrt(z / eps)
        best = min(((2 / (0.5 - t2)) * Fh(t2 / z) / sig, t2) for t2 in np.arange(0.0005, 0.4995, 0.0005)) if j > 0 else (4.0, 0)
        print(f"zeta={z:.4f}  P(no bad point<zeta)={P:.4f}  sigma_even={sig:.4f}  K(zeta)={best[0]:.3f} at th2={best[1]:.3f}")
