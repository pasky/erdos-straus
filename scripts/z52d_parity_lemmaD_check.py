"""z52d PARITY lane: numerical sanity check of Lemma D (memo Z52D_PARITY.md §2).
For (t,u) with t = 1 (4), u = 23 (24), q = tu-1, and primes p = 1 (24), p = -u (mod 4q):
x_p = (t, u, (p+u)/q) lies in X(p) and neither x_p nor rho(x_p) = (t, (p+u)/q, u) is in E(p) = {4 | tu - 1}.
Also checks that (p+2,1,1) is the only rho-fixed word of X(p) for these p, and the relative density 8/phi(lcm(24,4q)).
Usage: python z52d_parity_lemmaD_check.py PMAX"""
import sys
from math import gcd
from sympy import primerange, totient

def main():
    pmax = int(sys.argv[1])
    primes = [p for p in primerange(25, pmax) if p % 24 == 1]
    for t, u in [(1, 23), (5, 23), (1, 47), (9, 71), (13, 95)]:
        q = t * u - 1
        L = 24 * 4 * q // gcd(24, 4 * q)
        P = [p for p in primes if (p + u) % (4 * q) == 0]
        for p in P:
            v = (p + u) // q
            assert v % 4 == 0 and t * u * v - u - v == p
            assert (t * u - 1) % 4 != 0 and (t * v - 1) % 4 != 0
            # unique rho-fixed word: u = v, u (t u - 2) = p  =>  u = 1, t = p + 2
            fixed = [(tt, uu) for uu in (1, p) for tt in [(p // uu + 2) // uu] if uu * (tt * uu - 2) == p]
            assert fixed == [(p + 2, 1)], fixed
        dens = 8 / int(totient(L))
        print(f"(t,u)=({t},{u}) q={q} L={L}: {len(P)} primes p<{pmax} in class, observed rel. freq "
              f"{len(P)/len(primes):.4f} vs 8/phi(L) = {dens:.4f}; all checks passed")

main()
