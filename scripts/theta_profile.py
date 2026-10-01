"""Numerical companion for EXCEPTIONAL_THETA.md, Section 3 (supply profiles).

(a) Lemma 3.1 check: S_B(x) = sum_{M<=x, M=3 (4)} tau(A^2) M/phi(M), A=(M+1)/4,
    printed as S_B(x)/(x log^2 x)  (the lemma asserts this is bounded).
(b) Exact class masses (distinct residues) of the three forced-class families,
    against (log x)^3:
      B-M  : multiplier/M-grouping,  classes -4D mod M, D | A^2      (notes 18.1)
      B-aD : a-frame grouping,       classes -(4D+a) mod 4a g(D)     (Lemma 3.2;
             computed only for a = 3 (mod 4) [the n = 1 (mod 4) case] and
             gcd(a,D) = 1 [the witness-relevant classes]; other classes are
             forced too but excluded here by choice)
      A    : Case-A mirror,          classes -m^{-1} mod 4g(d), m | 4d+1 (Lemma 3.3)
    For B-aD and A the residue sets per modulus are built explicitly and
    deduplicated, so the printed numbers are exact union masses.
Run: uv run python scripts/theta_profile.py [xmax]
"""
import math
import sys
from collections import defaultdict


def spf_table(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def g_of(f):  # g(d) for d with factorization f
    g = 1
    for p, e in f.items():
        g *= p ** ((e + 1) // 2)
    return g


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def part_a(xmax, spf):
    print("(a) S_B(x)/(x log^2 x):")
    S = 0.0
    checkpoints = {10 ** k for k in range(2, 8)} | {xmax}
    for M in range(3, xmax + 1, 4):
        A = (M + 1) // 4
        fa = factor(A, spf)
        t = 1
        for e in fa.values():
            t *= 2 * e + 1
        fm = factor(M, spf)
        r = 1.0
        for p in fm:
            r *= p / (p - 1)
        S += t * r
        for c in list(checkpoints):
            if M <= c < M + 4:
                print(f"   x={c:>9d}  S_B/(x log^2 x) = {S / (c * math.log(c) ** 2):.4f}")
                checkpoints.discard(c)


def part_b(xmax, spf):
    print("(b) exact union masses vs (log x)^3:")
    # B-M grouping
    massBM = defaultdict(float)
    for M in range(3, xmax + 1, 4):
        A = (M + 1) // 4
        fa = factor(A, spf)
        f2 = {p: 2 * e for p, e in fa.items()}
        res = {(-4 * D) % M for D in divisors_from(f2)}
        massBM[M] = len(res) / M
    # B-aD grouping: modulus G=4 a g, class -(4D+a) mod G, a=3 (4), D any, gcd(a, D)?
    # validity: M=(n+4D)/a must be a positive integer =3 (4) with D | ((M+1)/4)^2;
    # the class n = -(4D+a) mod 4ag(D) guarantees g(D) | (M+1)/4.  We only need
    # gcd(a, 4D) | ... ; we keep all (a,D) with gcd(a,D)=1 (otherwise the class may be empty).
    resAD = defaultdict(set)
    for a in range(3, xmax // 4 + 1, 4):
        gmax = xmax // (4 * a)
        for D in range(1, gmax * gmax + 1):
            fD = factor(D, spf) if D > 1 else {}
            g = g_of(fD)
            G = 4 * a * g
            if G > xmax:
                continue
            if math.gcd(a, D) != 1:
                continue
            resAD[G].add((-(4 * D + a)) % G)
    massAD = defaultdict(float)
    for G, s in resAD.items():
        massAD[G] = len(s) / G
    # Case A: G = 4 g(d), class -m^{-1} mod G for m | 4d+1 (m odd, gcd(m,G)=1 automatic)
    resA = defaultdict(set)
    for d in range(1, xmax * xmax // 16 + 1):
        fd = factor(d, spf) if d > 1 else {}
        g = g_of(fd)
        G = 4 * g
        if G > xmax:
            continue
        n4 = 4 * d + 1
        for m in divisors_from(factor(n4, spf)):
            resA[G].add((-pow(m, -1, G)) % G)
    massA = {G: len(s) / G for G, s in resA.items()}
    for x in [10 ** k for k in range(2, 7) if 10 ** k <= xmax] + [xmax]:
        L3 = math.log(x) ** 3
        bm = sum(v for M, v in massBM.items() if M <= x)
        ad = sum(v for G, v in massAD.items() if G <= x)
        ca = sum(v for G, v in massA.items() if G <= x)
        print(f"   x={x:>8d} (log x)^3={L3:9.1f}  B-M:{bm:8.2f} ({bm / L3:.4f})  "
              f"B-aD:{ad:8.2f} ({ad / L3:.4f})  A:{ca:8.2f} ({ca / L3:.4f})")


if __name__ == "__main__":
    xa = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    spf = spf_table(max(xa, 4 * 10 ** 6) + 10)
    part_a(xa, spf)
    xb = 4000
    spf2 = spf_table(xb * xb // 4 + 10)
    part_b(xb, spf2)
