#!/usr/bin/env python3
"""POINTWISE_OMEGA12 (EVIDENCE + exact checks of the bookkeeping identities).

For every atom (M,D) with D <= A_M (M <= T, M = 3 mod 4, D | A^2):
  * Lemma 2.1: D = d a^2 (d squarefree), A = d a b, e = g = gcd(M,4D+1), f = P/e, P = 4a^2 d+1,
    c = (a+b)/e integer, N = M/e = 4acd - f, N >= acd, a^2 d <= T          (asserted)
  * h(M) <= h(e) + h(N)                                                    (asserted)
  * Omega_0' = sum g h(M)/M over D <= A, Sigma_I = sum h(e)/N, Sigma_II = sum h(N)/N, S_0'
  * Lemma 3.1 profile per c-scale C=2^j: mass, mean h(N), its split q<=C / q>C,
    and the pointwise bound L/log max(C,2) for the large part             (asserted)
Lemma 4.1: R(A,B) over all (a,d) with a^2 d <= T, ratio R/(log(Z+2) loglog(Z+16)).

usage: omega12_blocks.py T
"""
import sys
from math import log, gcd
from collections import defaultdict

from pointwise_omega_S import spf_table, factor, divisors_from


def hq(fac, Y=None, upto=True):
    """sum over prime powers q=l^i | n of 1/i, restricted to q<=Y (upto) or q>Y (not upto)."""
    s = 0.0
    for p, v in fac.items():
        for i in range(1, v + 1):
            if Y is None or ((p ** i <= Y) == upto):
                s += 1.0 / i
    return s


def sqfree_split(D, spf):
    d, a = 1, 1
    for p, v in factor(D, spf).items():
        if v % 2:
            d *= p
        a *= p ** (v // 2)
    return d, a


def run(T):
    L = log(T)
    spf = spf_table(4 * T + 8)
    S0 = Om = SI = SII = 0.0
    prof = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])  # j -> mass, sum h(N)/N, small part, large part
    natoms = 0
    for M in range(3, T + 1, 4):
        fM = factor(M, spf)
        hM = hq(fM)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        for D in divisors_from(fa):
            if D > A:
                continue
            natoms += 1
            g = gcd(M, 4 * D + 1)
            d, a = sqfree_split(D, spf)
            assert A % (d * a) == 0
            b = A // (d * a)
            assert b >= a and a * a * d <= T
            P = 4 * a * a * d + 1
            e = g
            f = P // e
            assert P % e == 0 and (a + b) % e == 0
            c = (a + b) // e
            N = M // e
            assert N * e == M and N == 4 * a * c * d - f and N >= a * c * d
            he = hq(factor(e, spf)) if e > 1 else 0.0
            fN = factor(N, spf) if N > 1 else {}
            hN = hq(fN)
            assert hM <= he + hN + 1e-12
            w = 1.0 / N
            S0 += w
            Om += w * hM
            SI += w * he
            SII += w * hN
            j = c.bit_length() - 1
            C = 1 << j
            Y = max(C, 2)
            small = hq(fN, C, True) if C >= 2 else 0.0
            large = hN - small
            assert large <= L / log(Y) + 1e-9
            pr = prof[j]
            pr[0] += w; pr[1] += w * hN; pr[2] += w * small; pr[3] += w * large
    print(f"T={T} L={L:.3f} loglogT={log(L):.3f} atoms(D<=A)={natoms}")
    print(f"  S0'={S0:.3f} Omega0'={Om:.3f} mean h={Om/S0:.3f}  Sigma_I={SI:.3f} Sigma_II={SII:.3f} "
          f"(Sigma_I+II)/Omega0'={(SI+SII)/Om:.3f}")
    print("  Lemma 3.1 profile: j  mass  mean h(N)  small(q<=C)  large(q>C)  bound L/log max(C,2)")
    for j in sorted(prof):
        m, hs, sm, lg = prof[j]
        print(f"   {j:3d} {m:9.4f} {hs/m:8.3f} {sm/m:8.3f} {lg/m:8.3f} {L/log(max(2, 1 << j)):8.3f}")
    # Lemma 4.1: R(A,B)
    R = defaultdict(float)
    for a in range(1, int(T ** 0.5) + 1):
        for d in range(1, T // (a * a) + 1):
            P = 4 * a * a * d + 1
            fP = factor(P, spf)
            tau = 1
            for v in fP.values():
                tau *= v + 1
            s = 0.0
            for p, v in fP.items():
                for i in range(1, v + 1):
                    s += tau * (v - i + 1) / (v + 1) / i  # tau(P/q) = tau(P)(v-i+1)/(v+1)
            R[(a.bit_length() - 1, d.bit_length() - 1)] += s / (a * d)
    worst = max(R.items(), key=lambda kv: kv[1] / (log((1 << max(kv[0])) + 2) * log(log((1 << max(kv[0])) + 16))))
    (ja, jd), r = worst
    Z = 1 << max(ja, jd)
    print(f"  Lemma 4.1: {len(R)} blocks, max R/(log(Z+2)loglog(Z+16)) = "
          f"{r/(log(Z+2)*log(log(Z+16))):.3f} at (A,B)=(2^{ja},2^{jd}); "
          f"sum_(A,B) R = {sum(R.values()):.2f}")


if __name__ == "__main__":
    run(int(sys.argv[1]))
