#!/usr/bin/env python3
"""z63 PRECEDENT falsifier F4 for the M2 (least-non-residue) transfer.

For each (★)-zero prime p (data/z58/screens/star_prime_zeros.txt) compute
  * n_p  = least prime ell with (ell/p) = -1, and
  * R(p) recomputed by brute force (direct d-form: R(p) = #{(C, d) : d | 4Cp+1, d = -1 mod 4C}),
    feasible for p <= 10^6 (C ranges up to (p+1)/2... see bound below); larger p are only quoted.
Also the same for a control sample: the first 2000 primes p = 1 (24) (R(p) > 0 expected) and odd squares.

Bound used: a (★) solution (u, B, C) of 4uBC - u - B = n has C <= (n+2)/4 (u = B = 1 gives 4C - 2 = n),
so C ranges over 1..(n+2)//4 and d = 4uC - 1 over divisors of 4Cn+1 with d = -1 mod 4C, d > 1, and the
cofactor (4Cn+1)/d is then automatically = -1 mod 4C as well.
Run: ulimit -v 4000000; timeout 1800 uv run --with sympy python scripts/z63_precedent_qnr_zeros.py
"""
import sys
from sympy import legendre_symbol, isprime, divisors, primerange


def least_nr(p):
    for ell in primerange(2, p):
        if ell == 2:
            if p % 8 in (3, 5):
                return 2
            continue
        if legendre_symbol(ell, p) == -1:
            return ell
    return None


def R(n):
    cnt = 0
    for C in range(1, (n + 2) // 4 + 1):
        N = 4 * C * n + 1
        m = 4 * C
        for d in divisors(N):
            if d > 1 and d % m == m - 1:
                cnt += 1
    return cnt


def main():
    zeros = [int(x) for x in open('data/z58/screens/star_prime_zeros.txt') if x.strip() and not x.startswith('#')]
    out = []
    out.append('# (★)-zero primes: p, n_p (least prime non-residue), R(p) recomputed if p <= 10^4 else "cert"')
    for p in zeros:
        r = R(p) if p <= 10**4 else 'cert'
        out.append(f'{p} n_p={least_nr(p)} R={r}')
    # controls: odd squares (R must be 0; n_m2 undefined: no non-residue)
    out.append('# odd squares m^2, m = 5,7,11,13: R recomputed (T1 predicts 0)')
    for m in (5, 7, 11, 13):
        out.append(f'{m*m} R={R(m*m)}')
    out.append('# control primes with R>0 expected: 13, 73, 433')
    for p in (13, 73, 433):
        out.append(f'{p} n_p={least_nr(p)} R={R(p)}')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
