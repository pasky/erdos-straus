"""R210 check of PHASE_DIAGRAM §6 B1 statement.

(1) Core lemma, brute force: for every g <= GMAX, g = 3 (mod 4), every Q mod g, and r in RS (primes = 1 mod 4):
    the class n = -4Q^2 (mod g) never contains the point x(u) (x_l = 1 for l != r, x_r = u), for ANY unit u mod r
    (residue or not) — i.e. the non-residue hypothesis is not needed.
(2) Illustration: the union of all shot classes with g <= G0 misses primes p = u (mod r) for every unit u, residue
    or non-residue; print the least such p for r = 5, 13.
"""
import sys
from math import gcd
from sympy import isprime, primerange


def in_class_at_point(g, Q, r, u):
    # x(u) is in {n : g | n + 4Q^2} iff for every prime power l^a || g: x_l = -4Q^2 mod l^a
    m = g
    l = 2
    fac = {}
    while l * l <= m:
        while m % l == 0:
            fac[l] = fac.get(l, 0) + 1
            m //= l
        l += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    for l, a in fac.items():
        pa = l ** a
        xl = u if l == r else 1
        if (xl + 4 * Q * Q) % pa:
            return False
    return True


def main(GMAX, G0, PMAX):
    RS = [5, 13, 17, 29]
    hits = 0
    for g in range(3, GMAX + 1, 4):
        for Q in range(g):
            for r in RS:
                for u in range(1, r):
                    if in_class_at_point(g, Q, r, u):
                        hits += 1
    print(f"(1) g <= {GMAX}: points x(u) inside a shot class: {hits} (expected 0, for ALL units u)")
    gs = list(range(3, G0 + 1, 4))
    for r in (5, 13):
        least = {}
        for p in primerange(3, PMAX):
            u = p % r
            if u == 0 or u in least:
                continue
            covered = any(((-p) * pow(4, -1, g)) % g in {(q * q) % g for q in range(g)} for g in gs if gcd(g, p) == 1)
            if not covered:
                least[u] = p
        print(f"(2) r={r}: least prime p = u (mod r) uncovered by all shot classes with g <= {G0}: {dict(sorted(least.items()))}")


if __name__ == "__main__":
    main(*[int(t) for t in sys.argv[1:4]])
