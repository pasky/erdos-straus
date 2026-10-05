#!/usr/bin/env python3
"""POINTWISE_OMEGA11 §4 (EVIDENCE): the weighted charge moment of Lemma 2.2.

S#     = sum over atoms (M,D) of s(M,D) = gcd(M,4D+1)/M * prod_{l|M} l/(l-1)   (the Euler factor
         replaces Lemma 2.1's C loglog T); also the pure g/M-weighted mean of h
Omega# = sum over atoms of s(M,D) * h(M),  h(M) = sum_{l|M} H_{v_l(M)}
Also the split of Omega# by prime size (l <= L^2, L^2 < l <= L^5, l > L^5) and the
s-weighted mean of h versus log2 tau(M) (the worst-case charge) and log log T.

usage: omega11_hmoment.py T1 [T2 ...]
"""
import sys
from math import log, gcd, log2

from pointwise_omega_S import spf_table, factor, divisors_from


def run(T, spf):
    L = log(T)
    S = Om = 0.0
    S0 = Om0 = 0.0
    split = [0.0, 0.0, 0.0]
    wc = 0.0
    for M in range(3, T + 1, 4):
        f = factor(M, spf)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        eul = 1.0
        tau = 1
        hp = []
        for p, e in f.items():
            eul *= p / (p - 1)
            tau *= e + 1
            hp.append((p, sum(1 / i for i in range(1, e + 1))))
        h = sum(x for _, x in hp)
        sm = 0.0
        for D in divisors_from(fa):
            sm += gcd(M, 4 * D + 1)
        s = sm * eul / M
        S += s
        S0 += sm / M
        Om0 += sm / M * h
        Om += s * h
        wc += s * log2(tau)
        for p, x in hp:
            split[0 if p <= L * L else (1 if p <= L ** 5 else 2)] += s * x
    print(f"T={T}: L={L:.2f} S#={S:.2f} Omega#={Om:.2f} mean h={Om/S:.3f} (g/M-weighted {Om0/S0:.3f}) "
          f"(worst-case log2 tau mean {wc/S:.3f}, L/logL={L/log(L):.2f}, loglogT={log(L):.2f}) "
          f"split l<=L^2:{split[0]:.1f} L^2<l<=L^5:{split[1]:.1f} l>L^5:{split[2]:.1f}")


def main():
    Ts = [int(x) for x in sys.argv[1:]]
    spf = spf_table(max(Ts) + 8)
    for T in Ts:
        run(T, spf)


if __name__ == "__main__":
    main()
