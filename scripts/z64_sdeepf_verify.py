#!/usr/bin/env python3
"""F4 / F2 screen: for every n listed in the z58 screen files (and any extra n on the command line),
find a length-3 word (t,u,v), A = tu-1, with Jacobi (A/n) = -1, by DIRECT Jacobi evaluation
(no local rule used).  Words are searched by u (divisors of n+u in class -1 mod u) and by t
(divisors of tn+1 in class -1 mod t), small parameters first.  Also reports the local-rule class.
"""
import sys
from math import gcd, isqrt
from sympy import factorint, divisors, isprime

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

def words_by_u(n, umax):
    for u in range(2, umax + 1):
        m = n + u
        for A in divisors(m):
            if A % u == u - 1 and 2 * u - 1 <= A and 2 * A <= m:
                t, v = (A + 1) // u, m // A
                assert t * u * v - u - v == n and t >= 2 and v >= 2
                yield t, u, v

def words_by_t(n, tmax):
    for t in range(2, tmax + 1):
        m = t * n + 1
        for A in divisors(m):
            if A % t == t - 1 and 2 * t - 1 <= A and A * (2 * t - 1) <= m:
                B = m // A
                u, v = (A + 1) // t, (B + 1) // t
                assert t * u * v - u - v == n and u >= 2 and v >= 2
                yield t, u, v

def first_good(n, lim=3000):
    seen = set()
    nw = 0
    for gen in (words_by_u(n, lim), words_by_t(n, lim)):
        for t, u, v in gen:
            if (t, u, v) in seen: continue
            seen.add((t, u, v)); nw += 1
            A = t * u - 1
            if gcd(A, n) == 1 and jacobi(A, n) == -1:
                return (t, u, v, A), nw
    return None, nw

def load(p):
    return [int(l.split()[0]) for l in open(p) if l.strip() and not l.startswith('#')]

def main():
    base = 'data/z58/screens/'
    sets = {
        'star_prime_zeros': load(base + 'star_prime_zeros.txt'),
        'gstar_zeros': load(base + 'gstar_zeros.txt'),
        'r8_zeros_1e10': load(base + 'r8_zeros_1e10.txt'),
        'composite_zeros_le8e6': load(base + 'composite_zeros_le8e6.txt'),
    }
    if len(sys.argv) > 1:
        sets['extra'] = [int(x) for x in sys.argv[1:]]
    for name, ns in sets.items():
        fails = []
        print(f"== {name}: {len(ns)} values")
        for n in ns:
            assert n % 4 == 1 and isqrt(n) ** 2 != n
            w, nw = first_good(n)
            if w is None:
                fails.append(n)
                print(f"  n={n} prime={isprime(n)}: NO GOOD WORD FOUND among {nw} words searched (lim)")
            else:
                t, u, v, A = w
                print(f"  n={n} n%8={n%8} prime={isprime(n)}: good word t,u,v={t},{u},{v} A={A} (A/n)={jacobi(A,n)}  [searched {nw} words]")
        print(f"   -> {name}: {len(ns)-len(fails)}/{len(ns)} satisfy (S) by explicit witness; failures: {fails}")

if __name__ == '__main__':
    main()
