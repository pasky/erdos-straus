"""MN3 §4 numerics (EVIDENCE): share of U_1(q) (K=1) in the residual where all four linear routes
are short:  c < q,  d < f*q,  d < e*q,  a < f*q   (constants 1, exponents delta = 0).
Atoms (M,D), D <= A, M <= X, M in C_q (q = largest prime power exactly dividing M).
usage: uv run python mn3_resid.py m X
"""
import sys
from math import gcd, isqrt
from mn3_u1 import spf_sieve, factor, divisors_from, phi_f


def main():
    m, X = int(sys.argv[1]), int(sys.argv[2])
    spf = spf_sieve(X + 2)
    tot, res, resq = {}, {}, {}
    M = m - 1
    while M <= X:
        fM = factor(M, spf)
        q = max(p ** e for p, e in fM.items())
        A = (M + 1) // m
        fA = factor(A, spf) if A > 1 else {}
        for D in divisors_from({p: 2 * e for p, e in fA.items()}):
            if D > A:
                continue
            fD = factor(D, spf) if D > 1 else {}
            a = 1
            for p, e in fD.items():
                a *= p ** (e // 2)
            d = D // (a * a)
            b = A // (d * a)
            P = m * D + 1
            g = gcd(M, P)
            N = M // g
            c, f = (a + b) // g, P // g
            w = 1.0 / phi_f(factor(N, spf)) if N > 1 else 1.0
            tot[q] = tot.get(q, 0) + w
            if c < q and d < f * q and d < g * q and a < f * q:
                res[q] = res.get(q, 0) + w
                if N % q == 0:
                    resq[q] = resq.get(q, 0) + w
        M += m
    print("m=%d X=%d" % (m, X))
    for q in sorted(tot):
        if 7 <= q <= 200 and q in tot:
            t = tot[q]
            print("q=%4d U1=%.4f residual share=%.3f (of which q|N: %.3f)" % (
                q, t, res.get(q, 0) / t, resq.get(q, 0) / t))


if __name__ == "__main__":
    main()
