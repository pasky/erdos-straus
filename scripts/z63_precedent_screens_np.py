#!/usr/bin/env python3
"""z63 PRECEDENT (cross-model review fix 3): non-residue layer on all F2-F4 screen inputs.

For every input n of data/z58/screens/{star_prime_zeros, r8_zeros_1e10, composite_zeros_le8e6, gstar_zeros}.txt
compute ell(n) = least prime ell with Jacobi (ell/n) = -1 (for n = 1 mod 4 and odd ell this equals (n/ell) = -1),
plus primality and squareness. Zero status of each input (R = 0, R_8 = 0, R_G* = 0) is INHERITED from the screen
files, not recomputed here.
Run: ulimit -v 4000000; timeout 600 uv run --with sympy python scripts/z63_precedent_screens_np.py
"""
from math import isqrt
from sympy import jacobi_symbol, isprime, primerange


def ell(n):
    for q in primerange(2, 10**6):
        if n % q == 0:
            continue
        if jacobi_symbol(q, n) == -1:
            return q
    return None


for name in ('star_prime_zeros', 'r8_zeros_1e10', 'composite_zeros_le8e6', 'gstar_zeros'):
    ns = [int(l.split()[0]) for l in open(f'data/z58/screens/{name}.txt') if l.strip() and not l.startswith('#')]
    ls = [ell(n) for n in ns]
    nprime = sum(isprime(n) for n in ns)
    nsq = sum(isqrt(n) ** 2 == n for n in ns)
    print(f'{name}: count={len(ns)} prime={nprime} square={nsq} all_n1mod4={all(n % 4 == 1 for n in ns)} '
          f'max_ell={max(ls)} none={ls.count(None)}')
    print('  ell list:', ','.join(map(str, ls)))
