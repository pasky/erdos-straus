#!/usr/bin/env python3
"""Review check for POINTWISE_OMEGA6 Thm 3.2: compute FT^{>mu}(Z) for given classes.

FT = sum_{(s,a): 4sa^2=kappa (q), 4sa>yZ, sa<=T} sum_{m | 4sa^2+1, m>mu, m y-smooth} 2/nu,
nu = least nu>=y with q m nu = -1 (mod 4sa).
Prints FT (all s), FT over squarefree s, and FT restricted to nu<=T/(qm)
(i.e. the fibre's first element exists below T).
usage: review_omega6_ft.py T y l1 l2 Z mu kappa...
"""
import sys
from math import gcd, isqrt
from sympy import primerange, factorint
from sympy.ntheory import sqrt_mod


def pairs(T, q, kap):
    r = isqrt(T)
    for a in range(1, r + 1):            # a <= sqrt T
        if gcd(a, q) != 1:
            continue
        s = kap * pow(4 * a * a % q, -1, q) % q or q
        while s * a <= T:
            yield s, a
            s += q
    for s in range(1, r + 1):            # a > sqrt T, so s < sqrt T
        if gcd(s, q) != 1:
            continue
        w = kap * pow(4 * s % q, -1, q) % q
        for c in sqrt_mod(w, q, all_roots=True) or []:
            a = c if c > r else c + q * ((r - c) // q + 1)
            while s * a <= T:
                yield s, a
                a += q


def main():
    T, y, l1, l2 = (int(x) for x in sys.argv[1:5])
    q = l1 * l2
    Z = float(sys.argv[5])
    mu = int(sys.argv[6])
    P = list(primerange(2, y + 1))
    for kap in (int(x) for x in sys.argv[7:]):
        ft = ft_sf = ft_ex = 0.0
        npairs = 0
        for s, a in pairs(T, q, kap):
            X = 4 * s * a
            if X <= y * Z:
                continue
            npairs += 1
            G = 4 * s * a * a + 1
            divs = [1]
            for p in P:
                if G % p == 0:
                    e = 0
                    while G % p == 0:
                        G //= p
                        e += 1
                    divs = [d * p ** i for d in divs for i in range(e + 1)]
            issf = all(e == 1 for e in factorint(s).values())
            for m in divs:
                if m <= mu:
                    continue
                nu = (-pow(q * m, -1, X)) % X
                if nu < y:
                    nu += ((y - nu + X - 1) // X) * X
                w = 2.0 / nu
                ft += w
                if issf:
                    ft_sf += w
                    if nu <= T // (q * m):
                        ft_ex += w
        print(f"kappa={kap} Z={Z} mu={mu} pairs={npairs} FT={ft:.5f} "
              f"FT_sqfree={ft_sf:.5f} FT_sqfree_exists={ft_ex:.5f}")


if __name__ == "__main__":
    main()
