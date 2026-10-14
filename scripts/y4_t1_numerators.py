"""O212 (FOUR_SPECIFIC / BRAINSTORM/y4_t1_numerators): which numerators M carry T1 in the M-shot family,
and is the relaxed M^box a theorem while M/p fails?

M-shot (SYNTHESIS_SPARKS3 Lemma 1.0, valid for every M >= 1): g | n + M Q^2, g = -1 (mod M) gives
M/n = 1/x + 1/y + 1/z, x, y integers, den(z) | Q^2.
Claims tested:
 (A) T1 with ODD g: no odd g > 1, g = -1 (mod M), divides k^2 + M Q^2 (gcd(Q,k)=1, k odd, gcd(k,M)=1)
     <=> M = 0 or 3 (mod 4).  (even g: possible iff M = 3 mod 8.)
 (B) M^box at every failing pair (M, p) of data/ms/prime_fail_1e8.txt (+ 1e7 for M = 21..23): explicit certificate.
 (C) For M = 1, 2 (mod 4): shots at odd squares exist (no T1).
Usage: PYTHONPATH=scripts uv run python scripts/y4_t1_numerators.py
"""
from fractions import Fraction
from math import gcd, isqrt
from sympy import isprime, sqrt_mod


def fails(M):
    for fn in ('data/ms/prime_fail_1e8.txt', 'data/ms/prime_fail_1e7.txt'):
        try:
            for line in open(fn):
                if line.startswith(f'm={M} '):
                    return [int(t) for t in line.split('failures:')[1].split('checked')[0].split()]
        except FileNotFoundError:
            pass
    return None


def shot(M, n, g, Q):
    N = n + M * Q * Q
    assert N % g == 0 and (g + 1) % M == 0
    mp = N // g
    x = Fraction(n + mp, M)
    y = Fraction(n * (g + 1), M)
    assert x.denominator == 1 and y.denominator == 1
    zinv = Fraction(M, n) - 1 / x - 1 / y
    assert zinv > 0
    return int(x), int(y), 1 / zinv


def t1_counts(M, KMAX=99, QMAX=40):
    odd = even = 0
    for k in range(3, KMAX + 1, 2):
        if gcd(k, M) != 1:
            continue
        for Q in range(1, QMAX + 1):
            if gcd(Q, k) != 1:
                continue
            N = k * k + M * Q * Q
            for g in range(M - 1, N + 1, M):
                if g > 1 and N % g == 0:
                    if g % 2:
                        odd += 1
                    else:
                        even += 1
    return odd, even


def cert(M, p):
    g = M - 1
    while True:
        if g > 2 and isprime(g) and p % g:
            a = (-p * pow(M, -1, g)) % g
            s = sqrt_mod(a, g)
            if s is not None:
                for Q in sorted({s, g - s, s + g, 2 * g - s}):
                    if Q > 0 and gcd(Q, p) == 1:
                        x, y, z = shot(M, p, g, Q)
                        d = z.denominator
                        assert isqrt(d) ** 2 == d and gcd(d, p) == 1
                        return g, Q, x, y, z
        g += M


if __name__ == '__main__':
    print('M  M%4  T1(odd g)  odd-g shots at squares  even-g shots  #fail  maxg(M^box at failures)')
    for M in range(3, 25):
        o, e = t1_counts(M)
        fl = fails(M)
        mg = None
        if fl:
            mg = max(cert(M, p)[0] for p in fl)
        print(M, M % 4, 'YES' if o == 0 else 'no', o, e, None if fl is None else len(fl), mg)
    g, Q, x, y, z = cert(11, 37)
    print('example 11/37 =', f'1/{x} + 1/{y} + 1/({z})', 'g', g, 'Q', Q)
    g, Q, x, y, z = cert(11, 3)
    print('example 11/3 =', f'1/{x} + 1/{y} + 1/({z})', 'g', g, 'Q', Q)
