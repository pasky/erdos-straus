#!/usr/bin/env python3
"""POINTWISE_OMEGA13 Lemma 3.1 check: for every atom (M,D) (M<=T, M=3 mod 4, D | A_M^2),
Jacobi(-4D mod M, M) = -1, and for each prime l | M: Legendre(-4D, l) = Kronecker(-d, l), d = squarefree part of D.
usage: omega13_jacobi.py T"""
import sys
from pointwise_omega_S import spf_table, factor, divisors_from


def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


def main():
    T = int(sys.argv[1]); spf = spf_table(T + 8); n = bad = badl = 0
    for M in range(3, T + 1, 4):
        fM = factor(M, spf); A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        for D in divisors_from(fa):
            n += 1
            if jacobi(-4 * D, M) != -1: bad += 1
            d = 1
            for p in fa:
                e, x = 0, D
                while x % p == 0: x //= p; e += 1
                if e % 2: d *= p
            for l in fM:
                if jacobi(-4 * D, l) != jacobi(-d, l): badl += 1
    print(f"T={T} atoms={n} Jacobi!=-1: {bad}  Legendre(-4D,l)!=(-d|l): {badl}")


if __name__ == "__main__":
    main()
