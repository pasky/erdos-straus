#!/usr/bin/env python3
"""POINTWISE_MN §1 brute force: for the m/n Type II atoms (M = mA-1, D | A^2, class -mD mod M)
tabulate (i) the Jacobi symbol (-mD | M_odd) (M_odd = odd part of M) by (M mod 8, m),
(ii) the atoms that are *square-consistent*: -mD is a square unit mod every prime power
l^v || M (l odd: Legendre = 1; l = 2: v=1 any, v=2 needs 1 mod 4, v>=3 needs 1 mod 8).
Square-consistent atoms would fire under square-class quarantine.
usage: mn_jacobi.py T m1 m2 ..."""
import sys
from collections import Counter
from pointwise_omega_S import spf_table, factor, divisors_from
from omega13_jacobi import jacobi


def sq_unit_mod_pp(a, l, v):
    if l == 2:
        return v == 1 or (v == 2 and a % 4 == 1) or (v >= 3 and a % 8 == 1)
    return jacobi(a, l) == 1


def main():
    T = int(sys.argv[1]); ms = [int(x) for x in sys.argv[2:]]
    spf = spf_table(T + 8)
    for m in ms:
        n = 0; jac = Counter(); sqc = 0; ex = []
        for M in range(m - 1, T + 1, m):
            if M < 3: continue
            fM = factor(M, spf); A = (M + 1) // m
            Mo = M
            while Mo % 2 == 0: Mo //= 2
            fa = {p: 2 * e for p, e in factor(A, spf).items()} if A > 1 else {}
            for D in divisors_from(fa):
                n += 1
                c = (-m * D) % M
                j = jacobi(c, Mo) if Mo > 1 else 1
                jac[(M % 8, j)] += 1
                if all(sq_unit_mod_pp(c, l, v) for l, v in fM.items()):
                    sqc += 1
                    if len(ex) < 8: ex.append((M, D, A))
        print(f"m={m} T={T} atoms={n} square-consistent={sqc} examples(M,D,A)={ex}")
        print("   (M mod 8, Jacobi(-mD|M_odd)) counts:", dict(sorted(jac.items())))


if __name__ == "__main__":
    main()
