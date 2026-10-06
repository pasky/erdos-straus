"""R65 from-scratch checks for sieve-limits-note v5 Thm 14.12 (smooth-rough splitting).

(a) R_{p'}(pi) <= rho * E_{pi_s} R_{p'}(pi_c)  for pi = sum_c pi_s(c) delta_c x pi_c on Z/Ms x Z/Mr,
    rho = Ms * max pi_s.
(b) Hoelder: for weights w with sum w <= 1, w <= 1/N:  sum_theta w |pi^|^2 <= (R/N)^{1/(1+beta)}.
(c) single-prime-power uniform-off-set: sum_{a!=0} |phi(a)|^{p'} <= g^{1+2beta}, g = p/(1-p).
Random small instances; reports worst ratios (must be <= 1).
"""
import numpy as np

rng = np.random.default_rng(65)


def R(sig, pp):
    f = np.fft.fft(sig)  # unnormalised: hat sigma(theta) = sum sigma(x) e(-x theta)
    return np.sum(np.abs(f) ** pp)


worst_a = worst_b = worst_c = 0.0
for trial in range(3000):
    Ms = int(rng.integers(2, 12)); Mr = int(rng.integers(2, 12))
    beta = float(rng.uniform(0.01, 0.5)); pp = 2 + 2 * beta
    As = rng.random(Ms) < 0.7
    if not As.any():
        As[0] = True
    pis = np.where(As, rng.random(Ms) ** 3, 0.0); pis /= pis.sum()
    rho = Ms * pis.max()
    # joint measure on Z/(Ms*Mr) via CRT only if coprime; instead use product group Z/Ms x Z/Mr, 2D FFT
    pic = {}
    joint = np.zeros((Ms, Mr))
    for c in range(Ms):
        if pis[c] > 0:
            v = (rng.random(Mr) < 0.6) * rng.random(Mr) ** 2
            if v.sum() == 0:
                v[rng.integers(Mr)] = 1.0
            v /= v.sum(); pic[c] = v
            joint[c] = pis[c] * v
    Rjoint = np.sum(np.abs(np.fft.fft2(joint)) ** pp)
    ER = sum(pis[c] * R(pic[c], pp) for c in pic)
    worst_a = max(worst_a, Rjoint / (rho * ER))
    # (b) random admissible-style weights: sum<=1, each <=1/N
    N = int(rng.integers(Ms * Mr, 10 * Ms * Mr))
    F2 = (np.abs(np.fft.fft2(joint)) ** 2).ravel()
    w = rng.random(F2.size); w = np.minimum(w / w.sum(), 1.0 / N)
    lhs = np.sum(w * F2)
    rhs = (Rjoint / N) ** (1 / (1 + beta))
    worst_b = max(worst_b, lhs / rhs)
    # (c)
    L = int(rng.integers(2, 40)); k = int(rng.integers(1, max(2, L // 2 + 1)))
    S = np.ones(L); S[rng.choice(L, k, replace=False)] = 0
    sig = S / S.sum(); p = k / L; g = p / (1 - p)
    fa = np.abs(np.fft.fft(sig))[1:]
    worst_c = max(worst_c, np.sum(fa ** pp) / g ** (1 + 2 * beta))
print(f"(a) max R(pi)/(rho E R(pi_c)) = {worst_a:.6f}")
print(f"(b) max F_w/(R/N)^(1/(1+b))  = {worst_b:.6f}")
print(f"(c) max sum|phi|^p'/g^(1+2b) = {worst_c:.6f}")
assert worst_a <= 1 + 1e-9 and worst_b <= 1 + 1e-9 and worst_c <= 1 + 1e-9
print("OK")
