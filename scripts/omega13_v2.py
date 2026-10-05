#!/usr/bin/env python3
"""POINTWISE_OMEGA13 §2 (EVIDENCE): late-prime masses V#(l) = sum_{atoms, l|M} g/M  (beta=1, C_1=1),
over all atoms (M,D), M<=T, M=3 mod 4, D | A_M^2.  Reports S#, sum_{l>Y} V#(l)^2 for Y=L^k,
the heuristic S#^2/(Y log Y), max_{l>Y} l*V#(l)/S#, and the largest V#(l) for l>L^2.
usage: omega13_v2.py T
"""
import sys
from math import log, gcd
from collections import defaultdict
from pointwise_omega_S import spf_table, factor, divisors_from


def main():
    T = int(sys.argv[1]); L = log(T)
    spf = spf_table(T + 8)
    V = defaultdict(float); S = 0.0
    for M in range(3, T + 1, 4):
        fM = factor(M, spf)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        tot = 0.0
        for D in divisors_from(fa):
            tot += gcd(M, 4 * D + 1) / M
        S += tot
        for p in fM:
            V[p] += tot
    print(f"T={T} L={L:.3f} S#={S:.3f}")
    for k in [2, 3, 4, 5]:
        Y = L ** k
        sq = sum(v * v for p, v in V.items() if p > Y)
        mx = max((p * v / S for p, v in V.items() if p > Y), default=0)
        print(f"  Y=L^{k}={Y:.0f}: sum_(l>Y) V^2={sq:.4e}  S#^2/(Y logY)={S*S/(Y*log(Y)):.4e}"
              f"  max l*V/S#={mx:.3f}")
    top = sorted(((v, p) for p, v in V.items() if p > L * L), reverse=True)[:5]
    print("  top V(l), l>L^2:", ", ".join(f"l={p}: V={v:.4f} (lV/S#={p*v/S:.2f})" for v, p in top))


if __name__ == "__main__":
    main()
