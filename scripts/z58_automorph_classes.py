#!/usr/bin/env python3
"""z58 AUTOMORPH: (1) local square classes of the known R-zeros (for Prop C, escape E1);
(2) global check of the sign-form example a(n) = 5 sigma_2(n) - (2 n^2 + 3) tau(n):
    a(m^2) <= 0 for all odd m <= MMAX, a(p) = p^2 - 1 > 0 at primes (so it is invalid at the prime zeros, F4).
"""
import sys
from sympy import factorint, primerange, divisor_sigma, divisor_count, isprime

def load(fn):
    return [int(x.split()[0]) for x in open(fn) if x.strip() and x[0] != '#']

def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1

def locally_square(n, P):
    """n is an l-adic square unit for every odd prime l <= P, and n ≡ 1 (mod 8)."""
    if n % 8 != 1:
        return False
    return all(legendre(n, l) == 1 for l in primerange(3, P + 1))

def main():
    D = 'data/z58/screens/'
    comp = load(D + 'composite_zeros_le8e6.txt')
    star = load(D + 'star_prime_zeros.txt')
    gst = load(D + 'gstar_zeros.txt')
    r8 = load(D + 'r8_zeros_1e10.txt')
    print("# local square classes: count of zeros n that are l-adic square units for all odd l <= P and n ≡ 1 (8)")
    print("# columns: P, composite(all), composite(squarefree), composite(sqf, n>1e6), star primes, G* primes, R8 primes")
    for P in (3, 5, 7, 11, 13, 17, 19, 23):
        c_all = [n for n in comp if locally_square(n, P)]
        c_sqf = [n for n in c_all if all(e == 1 for e in factorint(n).values())]
        c_big = [n for n in c_sqf if n > 10**6]
        print(P, len(c_all), len(c_sqf), len(c_big), sum(locally_square(p, P) for p in star),
              sum(locally_square(p, P) for p in gst), sum(locally_square(p, P) for p in r8),
              "examples(sqf):", c_sqf[-3:])
    # composite zeros per range, for growth
    print("# composite zeros per range [10^k, 10^(k+1)) and locally-square-at-7 among them")
    for k in range(1, 7):
        lo, hi = 10**k, 10**(k + 1)
        s = [n for n in comp if lo <= n < hi]
        print(k, len(s), sum(locally_square(n, 7) for n in s))
    # (2) sign example
    MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20001
    worst = None
    for m in range(1, MMAX + 1, 2):
        n = m * m
        a = 5 * divisor_sigma(n, 2) - (2 * n * n + 3) * divisor_count(n)
        if a > 0:
            print("VIOLATION a(m^2)>0 at m =", m, a)
            break
        r = a / (n * n)
        if worst is None or r > worst[1]:
            worst = (m, r)
    print("sign example: max over odd m <=", MMAX, "of a(m^2)/m^4 =", worst)

if __name__ == "__main__":
    main()
