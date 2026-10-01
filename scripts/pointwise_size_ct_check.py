#!/usr/bin/env python3
"""POINTWISE_SIZE.md, Lemma CT (character trap) -- exhaustive check.

For every prime p = 1 (mod 4), 5 <= p <= PMAX, enumerate ALL positive solutions
4/p = 1/x + 1/y + 1/z (x <= y <= z) and check:

  (CT-a) every denominator not divisible by p has a prime factor l with (l/p) = -1;
  (CT-b) Type I (exactly one p-divisible denominator p*z0): z0 has such a factor;
  (CT-c) Type II (x, p*y', p*z'): y'*z' has such a factor.

Also reports how often, in Type II, BOTH y' and z' individually have one
(not claimed by the lemma).  Completeness of the enumeration is cross-checked
against a naive triple loop for p < BRUTE.

Usage: PYTHONPATH=scripts uv run python scripts/pointwise_size_ct_check.py [PMAX] [BRUTE]
"""
import sys
from math import gcd
from fractions import Fraction
from sympy import primerange, factorint


def divisors_from_fac(fac):
    ds = [1]
    for ell, e in fac.items():
        ds = [d * ell ** k for d in ds for k in range(e + 1)]
    return ds


def solutions(p):
    """All (x,y,z), x<=y<=z, with 4/p = 1/x+1/y+1/z."""
    sols = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        if num <= 0:
            continue
        g = gcd(num, den)
        n, m = num // g, den // g          # 1/y + 1/z = n/m, reduced
        fac = factorint(m)
        fac2 = {ell: 2 * e for ell, e in fac.items()}
        for d in divisors_from_fac(fac2):    # (n y - m)(n z - m) = m^2, d = n y - m
            if d > m:                       # y <= z  <=>  d <= m
                continue
            if (d + m) % n:
                continue
            y = (d + m) // n
            e = m * m // d
            if (e + m) % n:
                continue
            z = (e + m) // n
            if y < x:
                continue
            sols.append((x, y, z))
    return sols


def brute(p):
    out = set()
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        ylo = max(x, int(1 / r) + 1)
        yhi = int(2 / r)
        for y in range(ylo, yhi + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                out.add((x, y, s.denominator))
    return out


def has_qnr_factor(n, p):
    return any(pow(ell, (p - 1) // 2, p) == p - 1 for ell in factorint(n))


def main():
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    BRUTE = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    nprimes = nsol = n1 = n2 = both = 0
    bad = []
    for p in primerange(5, PMAX + 1):
        if p % 4 != 1:
            continue
        nprimes += 1
        sols = solutions(p)
        if p < BRUTE:
            assert set(sols) == brute(p), p
        assert len(sols) == len(set(sols)) and sols, p
        for s in sols:
            assert Fraction(1, s[0]) + Fraction(1, s[1]) + Fraction(1, s[2]) == Fraction(4, p)
            nsol += 1
            pdiv = [w for w in s if w % p == 0]
            pfree = [w for w in s if w % p]
            assert len(pdiv) in (1, 2)
            for w in pfree:                                   # (CT-a)
                if not has_qnr_factor(w, p):
                    bad.append(('a', p, s))
            if len(pdiv) == 1:                                # (CT-b)
                n1 += 1
                z0 = pdiv[0] // p
                assert z0 % p
                if not has_qnr_factor(z0, p):
                    bad.append(('b', p, s))
            else:                                             # (CT-c)
                n2 += 1
                y1, z1 = pdiv[0] // p, pdiv[1] // p
                assert y1 % p and z1 % p
                if not has_qnr_factor(y1 * z1, p):
                    bad.append(('c', p, s))
                if has_qnr_factor(y1, p) and has_qnr_factor(z1, p):
                    both += 1
    print(f"primes p=1(4), 5<=p<={PMAX}: {nprimes}; solutions (x<=y<=z): {nsol}")
    print(f"  Type I: {n1}, Type II: {n2}; brute-force completeness check for p<{BRUTE}: OK")
    print(f"  violations of CT-a/b/c: {len(bad)}")
    print(f"  Type II with BOTH y',z' having a QNR factor: {both}/{n2} (not claimed)")
    if bad:
        print("  first violations:", bad[:10])
        sys.exit(1)
    print("OK")


if __name__ == '__main__':
    main()
