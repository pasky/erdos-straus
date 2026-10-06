#!/usr/bin/env python3
"""POINTWISE_MN §2: Type-II-hard unit classes for m/n modulo Q.
H_m(Q) = { r in (Z/Q)^x : r mod M not in R_m(M) for every M | Q, M = -1 (m), M >= 3 },
R_m(M) = { -mD mod M : D | A^2 }, A = (M+1)/m.
Prints |H|, |H|/phi(Q), whether H is a subgroup / union of square cosets, and the distinct
residues of H mod each prime power of Q.
usage: mn_hard.py m Q"""
import sys
from math import gcd
from pointwise_omega_S import spf_table, factor, divisors_from


def classes(m, M, spf):
    A = (M + 1) // m
    fa = {p: 2 * e for p, e in factor(A, spf).items()} if A > 1 else {}
    return {(-m * D) % M for D in divisors_from(fa)}


def hard(m, Q, spf):
    Ms = [M for M in divisors_from(factor(Q, spf)) if M >= 3 and M % m == m - 1]
    R = {M: classes(m, M, spf) for M in Ms}
    H = [r for r in range(1, Q) if gcd(r, Q) == 1 and all(r % M not in R[M] for M in Ms)]
    return H, Ms


def main():
    m, Q = int(sys.argv[1]), int(sys.argv[2])
    spf = spf_table(Q + 8)
    H, Ms = hard(m, Q, spf)
    phi = sum(1 for r in range(1, Q) if gcd(r, Q) == 1)
    Hs = set(H)
    sub = all((a * b) % Q in Hs for a in H[:200] for b in H[:200])
    sq = {(x * x) % Q for x in range(1, Q) if gcd(x, Q) == 1}
    print(f"m={m} Q={Q} moduli M|Q: {Ms}")
    print(f"|H|={len(H)} phi(Q)={phi} fraction={len(H)/phi:.5f}  closed(sample)={sub}  "
          f"H subset of squares={Hs <= sq}  1 in H={1 in Hs}")
    for p, e in factor(Q, spf).items():
        q = p ** e
        print(f"   mod {q}: {sorted({r % q for r in H})}")
    if len(H) <= 40: print("   H =", H)


if __name__ == "__main__":
    main()
