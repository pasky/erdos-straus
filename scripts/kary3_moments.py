"""EXCEPTIONAL_KARY3 numerics (EVIDENCE only).

For small y, enumerate all y-smooth M = 3 (mod 4) up to X and compute
  * the smooth first moment S(y,X) = sum tau(A_M^2) * Gamma(M) / M, A = (M+1)/4,
    with Gamma(M) = prod_{p|M} gamma'(p) (W = 16 convention of K2) and also Gamma = 1;
  * the dyadic block profile  b(K) = (1/(K log^2 K)) * sum_{K<M<=2K smooth} tau(A^2),
    as a function of u = log K / log y (Lemma 2.3 predicts <= C u^{-k}; truth ~ rho(u)).
Usage: uv run --with sympy python scripts/kary3_moments.py X y1,y2,...
"""
import math
import sys

from sympy import factorint, primerange


def gamma_p(p, W=16):
    if p == 2:
        return 8.0
    if p <= W:
        return 2 * p / (p - 1)
    return 1.0 / (1 - p ** -0.5)


def smooth_numbers(primes, X):
    out = []
    stack = [(1, 0)]
    while stack:
        m, i = stack.pop()
        out.append(m)
        for j in range(i, len(primes)):
            mm = m * primes[j]
            if mm > X:
                break
            stack.append((mm, j))
    return out


def tau_sq(a):
    t = 1
    for e in factorint(a).values():
        t *= 2 * e + 1
    return t


def main():
    X = int(float(sys.argv[1]))
    ys = [int(v) for v in sys.argv[2].split(",")]
    for y in ys:
        primes = list(primerange(2, y + 1))
        sm = sorted(m for m in smooth_numbers(primes, X) if m % 4 == 3)
        S1 = 0.0
        SG = 0.0
        blocks = {}
        partial = []
        for M in sm:
            A = (M + 1) // 4
            t = tau_sq(A)
            G = 1.0
            for p in factorint(M):
                G *= gamma_p(p)
            S1 += t / M
            SG += t * G / M
            k = M.bit_length() - 1  # M in [2^k, 2^{k+1})
            blocks[k] = blocks.get(k, 0) + t
            partial.append((M, S1))
        ly = math.log(y)
        print(f"y={y} X={X:.0e} #smooth(3 mod 4)={len(sm)}")
        print(f"  S_tau(y,X)={S1:.4f}  S_tau/(log y)^3={S1 / ly**3:.4f}   "
              f"S_tauGamma(y,X)={SG:.4f}  /(log y)^3={SG / ly**3:.4f}")
        # convergence: value at X^{1/2}, X^{3/4}
        for frac in (0.5, 0.75):
            lim = X ** frac
            v = max((s for (m, s) in partial if m <= lim), default=0.0)
            print(f"  S_tau(y,X^{frac})={v:.4f}")
        print("  dyadic profile (every 2nd block shown; max over ALL complete blocks below):")
        best = (0.0, None, None)
        for k in sorted(blocks):
            K = 2 ** k
            if K < y or 2 * K > X:
                continue
            u = math.log(K) / ly
            v = u**4 * blocks[k] / (K * math.log(K) ** 2)
            if v > best[0]:
                best = (v, K, u)
        print(f"  max over complete blocks K>=y: u^4 b = {best[0]:.4f} at K={best[1]} (u={best[2]:.3f})")
        for k in sorted(blocks):
            K = 2 ** k
            if K < y or 2 * K > X:
                continue
            u = math.log(K) / ly
            b = blocks[k] / (K * math.log(K) ** 2)
            if k % 2 == 0:
                print(f"    u={u:6.2f}  b={b:.3e}  u^4 b={u**4 * b:.3e}")


if __name__ == "__main__":
    main()
