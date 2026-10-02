"""Numerical companion for EXCEPTIONAL_THETA.md §3.8 (weighted share of balanced moduli).

For M = 3 (mod 4), A = (M+1)/4, weight w(M) = tau(A^2)/M  (the Case-B class mass
up to the factor 1/2..1 of Lemma 18.1).  Classify M by its largest prime factor:
  dominant(C):  P(M) >= M^{1/(1+C)}   (covered by Cor 3.6 for C<1)
  balanced:     P(M) <= M^{1/2}
and print the share of the cumulative weight sum_{M<=x} w(M) carried by each class,
together with the unweighted logarithmic densities sum 1/M, against Dickman:
  dominant(C) unweighted log-density -> log(1+C),  balanced -> rho(2) = 1 - log 2.
Also the exact union mass |R(M)|/M (deduplicated classes) for x <= 10^6.
Run: uv run python scripts/theta_balanced_share.py [xmax]
"""
import math
import sys

import numpy as np


def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, n + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    return spf


def main(xmax):
    nA = (xmax + 1) // 4 + 2
    spf = spf_sieve(max(xmax, nA) + 1)
    # largest prime factor table via spf
    def factor(n):
        f = {}
        while n > 1:
            p = int(spf[n])
            f[p] = f.get(p, 0) + 1
            n //= p
        return f

    checkpoints = sorted({10 ** k for k in range(3, 9) if 10 ** k <= xmax} | {xmax})
    tot = dom_half = dom_C = bal = 0.0
    utot = udom_half = udom_C = ubal = 0.0
    exact_tot = exact_bal = 0.0
    C1 = 0.5  # dominant with C = 1/2: P(M) >= M^{2/3}
    ci = 0
    print(f"{'x':>10} {'share dom(P>=M^1/2)':>20} {'share dom(P>=M^2/3)':>20} {'share bal(P<=M^1/2)':>20}"
          f" {'unweighted bal':>15} {'exact-union bal share':>22}")
    for M in range(3, xmax + 1, 4):
        fM = factor(M)
        P = max(fM)
        A = (M + 1) // 4
        t = 1
        for e in factor(A).values():
            t *= 2 * e + 1
        w = t / M
        lP, lM = math.log(P), math.log(M)
        tot += w
        utot += 1 / M
        if lP >= lM / 2:
            dom_half += w
        if lP >= lM / (1 + C1):
            dom_C += w
        if lP <= lM / 2:
            bal += w
            ubal += 1 / M
        if M <= 10 ** 6:
            f2 = {p: 2 * e for p, e in factor(A).items()}
            divs = [1]
            for p, e in f2.items():
                divs = [d * p ** k for d in divs for k in range(e + 1)]
            r = len({(-4 * D) % M for D in divs}) / M
            exact_tot += r
            if lP <= lM / 2:
                exact_bal += r
        while ci < len(checkpoints) and M + 4 > checkpoints[ci]:
            x = checkpoints[ci]
            ex = f"{exact_bal / exact_tot:22.4f}" if x <= 10 ** 6 else f"{'-':>22}"
            print(f"{x:>10} {dom_half / tot:20.4f} {dom_C / tot:20.4f} {bal / tot:20.4f}"
                  f" {ubal / utot:15.4f}{ex}")
            ci += 1
    print(f"Dickman (unweighted, limit): dom(1/2)->1-rho(2)=log2={math.log(2):.4f};"
          f" dom(2/3)->log(1.5)={math.log(1.5):.4f}; bal->1-log2={1 - math.log(2):.4f}")
    print("(convergence of logarithmic densities to Dickman values is slow, ~1/log x)")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6)
