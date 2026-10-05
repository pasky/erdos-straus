#!/usr/bin/env python3
"""POINTWISE_OMEGA13 §0 (EVIDENCE): where the class-of-one inflation comes from.

For all atoms (M,D), M<=T, M=3 mod 4, D | A_M^2 (both halves), computes
  S_haar = sum 1/phi(M)                       (unconditioned Haar mass)
  S_g    = sum g/M,  g = gcd(M,4D+1)          (O11 uniform weight, no Euler factor)
  S_Y    = sum g_Y/M, g_Y = Y-smooth part of g, for Y = L^k
  R_Y    = residual mass after full class-of-one quarantine of all primes <= Y:
           sum over atoms with M_Y | 4D+1, M != M_Y, of 1/phi(M/M_Y)   (M_Y = Y-smooth part of M)
  Omega_Y= sum (g_Y/M) h_Y(M),  h_Y = sum_{l^i | M, l<=Y} 1/i
usage: omega13_inflation.py T
"""
import sys
from math import log, gcd

from pointwise_omega_S import spf_table, factor, divisors_from


def phi_from(fac):
    r = 1
    for p, v in fac.items():
        r *= (p - 1) * p ** (v - 1)
    return r


def main():
    T = int(sys.argv[1])
    L = log(T)
    ks = [1, 2, 3, 4, 5, 6]
    Ys = [L ** k for k in ks]
    spf = spf_table(T + 8)
    S_haar = S_g = 0.0
    S_Y = [0.0] * len(ks)
    R_Y = [0.0] * len(ks)
    Om_Y = [0.0] * len(ks)
    n_det = [0] * len(ks)
    for M in range(3, T + 1, 4):
        fM = factor(M, spf)
        phiM = phi_from(fM)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        MY = []
        hY = []
        phirest = []
        for Y in Ys:
            m = 1
            h = 0.0
            rest = {}
            for p, v in fM.items():
                if p <= Y:
                    m *= p ** v
                    h += sum(1.0 / i for i in range(1, v + 1))
                else:
                    rest[p] = v
            MY.append(m)
            hY.append(h)
            phirest.append(phi_from(rest))
        for D in divisors_from(fa):
            g = gcd(M, 4 * D + 1)
            S_haar += 1.0 / phiM
            S_g += g / M
            for j, Y in enumerate(Ys):
                gy = gcd(g, MY[j])
                S_Y[j] += gy / M
                Om_Y[j] += gy / M * hY[j]
                if (4 * D + 1) % MY[j] == 0:
                    if MY[j] == M:
                        n_det[j] += 1  # cannot happen (Fact 1.1)
                    else:
                        R_Y[j] += 1.0 / phirest[j]
    print(f"T={T} L={L:.3f} S_haar={S_haar:.3f} S_g={S_g:.3f} S_g/S_haar={S_g / S_haar:.3f}")
    for j, k in enumerate(ks):
        print(f"  Y=L^{k}={Ys[j]:.0f}: S_Y={S_Y[j]:.3f} (S_Y/S_haar={S_Y[j] / S_haar:.3f})"
              f"  R_Y={R_Y[j]:.3f} (R_Y/S_haar={R_Y[j] / S_haar:.3f})  Omega_Y={Om_Y[j]:.3f}"
              f"  mean h_Y={Om_Y[j] / S_Y[j]:.3f}  det={n_det[j]}")


if __name__ == "__main__":
    main()
