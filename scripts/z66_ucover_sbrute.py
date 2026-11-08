"""z66 UCOVER: brute-force check of scripts/z66_ucover_swords.c (independent: direct Jacobi on representatives).

Enumerates fixed-(t,u) words with A = tu - 1 <= AMAX and fixed-(u,v) words with uv <= UVMAX; for each class decides
whether it contains the profile e_rho (1 at p != ell, rho at ell) for some rho, and whether the word is good there,
by evaluating the Jacobi symbol (A/n0) for an explicit large integer representative n0 of the class.
Prints the set of (k, rho mod ell^k) caught (good) by words with ell-level k.
Usage: uv run --with sympy python scripts/z66_ucover_sbrute.py ELL AMAX UVMAX
"""
import sys
from math import gcd
from sympy import jacobi_symbol


def vpart(m, ell):
    k = 0
    while m % ell == 0:
        m //= ell
        k += 1
    return k, m


def crt(r1, m1, r2, m2):
    # m1, m2 coprime
    return (r1 + m1 * (((r2 - r1) * pow(m1, -1, m2)) % m2)) % (m1 * m2)


def main():
    ell, AMAX, UVMAX = map(int, sys.argv[1:4])
    caught = set()
    # W1: fixed (t,u)
    for A in range(3, AMAX + 1):
        k, Ap = vpart(A, ell)
        if k == 0:
            continue
        for u in range(2, (A + 1) // 2 + 1):
            if (A + 1) % u:
                continue
            t = (A + 1) // u
            if (-u - 1) % Ap:
                continue  # need -u = 1 mod A'
            N = ell ** k
            rho = (-u) % N
            # representative n0: n0 = 1 mod 8A', n0 = rho mod ell^k, large enough
            M = 8 * Ap
            n0 = crt(1 % M, M, rho, N)
            n0 += M * N * 10 ** 6
            assert (n0 + u) % A == 0
            v = (n0 + u) // A
            assert t * u * v - u - v == n0
            if jacobi_symbol(A, n0) == -1:
                caught.add((k, rho, "W1"))
    # W2: fixed (u, v)
    for u in range(2, UVMAX + 1):
        for v in range(2, UVMAX // u + 1):
            uv = u * v
            k, mp = vpart(uv, ell)
            if k == 0:
                continue
            if (u + v + 1) % mp:
                continue
            N = ell ** k
            rho = (-(u + v)) % N
            a = 0
            while (mp >> a) % 2 == 0:
                a += 1
            M = 8 * mp  # n0 = 1 mod 8 m' (covers the 2-part to 2^{3+a})
            n0 = crt(1, M, rho, N) + M * N * 10 ** 6
            assert (n0 + u + v) % uv == 0
            t = (n0 + u + v) // uv
            A = t * u - 1
            if jacobi_symbol(A, n0) == -1:
                caught.add((k, rho, "W2"))
    for k, rho, w in sorted(caught):
        print(k, rho, w)


if __name__ == "__main__":
    main()
