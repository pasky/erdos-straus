#!/usr/bin/env python3
"""Independent fixed-x divisor enumeration and squareclass-energy checks."""
import json
from fractions import Fraction
from math import isqrt
from z51_lcaps_toy import primes, factor


def order(a, q):
    t = 1
    for j in range(1, q):
        t = t*a % q
        if t == 1:
            return j
    raise AssertionError('non-unit')


def cap_direct(p, q, s):
    N = p*s
    for e in range((q-3)//4 + 1):
        for u in range(3):
            for v in list(range(3)) + list(range(4, 2*e+3, 2)):
                D = p**u * s**v
                if (N+D) % q:
                    continue
                y = (N+D)//q
                z = Fraction(N*y, D)
                assert Fraction(4, p) == Fraction(1, s)+Fraction(1, y)+1/z
                den = z.denominator
                root = isqrt(den)
                assert root*root == den and root % 2 and root % p
                ff = factor(root)
                assert all(t == s and b <= e for t, b in ff.items())
                assert all(y % t == 0 for t in ff)
                return e
    raise AssertionError('no certificate')


def main():
    P = set(primes(100000))
    rows = []
    cases = zero = positive = 0
    for q in primes(100):
        if q < 11 or q % 8 != 3:
            continue
        count = special = 0
        for s in sorted(P):
            p = 4*s-q
            if p <= q or p not in P or s == 2 or order(s % q, q) != q-1:
                continue
            expected = 0 if p % q == q-1 else (q-3)//4
            actual = cap_direct(p, q, s)
            assert actual == expected
            cases += 1
            count += 1
            if actual == 0:
                zero += 1
                special += 1
            else:
                positive += 1
        rows.append(dict(q=q, cases=count, exceptional_zero=special))
    assert zero and positive
    weights = {n: 1+n % 7 for n in range(1, 151)}
    w = {}
    for n, c in weights.items():
        d = 1
        for p, b in factor(n).items():
            if b % 2:
                d *= p
        w[d] = w.get(d, 0)+c
    energy = sum(c*b for n, c in weights.items() for m, b in weights.items()
                 if isqrt(n*m)**2 == n*m)
    assert energy == sum(c*c for c in w.values())
    assert sum(weights.values())**2 <= len(w)*energy
    print(json.dumps(dict(status='PASS', cases=cases, cap_zero=zero,
                          cap_positive=positive, rows=rows,
                          energy=energy, kernels=len(w)), indent=2))


if __name__ == '__main__':
    main()
