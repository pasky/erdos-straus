"""Small exact controls for the reverse allocation and complementary-divisor steps."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, prod


def counts(q, primes):
    out = Counter({1: 1})
    for r in primes:
        nxt = Counter()
        for a, n in out.items():
            for mul in (1, r, pow(r, -1, q)):
                nxt[a*mul % q] += n
        out = nxt
    return out


def divisors(n):
    small = [d for d in range(1, isqrt(n)+1) if n % d == 0]
    return set(small) | {n//d for d in small}


def harris():
    qs, rs = (3, 7, 11), (13, 17, 19, 23)
    k = len(qs)
    # Compare three separate sums: exclusive allocation, independent odds
    # tilted to r-k, and literal enumeration of the progression digits.
    void = F(0)
    upper, lower = [], []
    for q in qs:
        miss = [F(0), F(0)]
        for mask in product((0, 1), repeat=len(rs)):
            if q-1 in counts(q, [r for r, b in zip(rs, mask) if b]):
                continue
            for j, shift in enumerate((0, k-1)):
                miss[j] += prod(F(1 if b else r-shift-1, r-shift)
                                for r, b in zip(rs, mask))
        upper.append(miss[0]); lower.append(miss[1])
    for code in product(range(-1, k), repeat=len(rs)):
        if all(q-1 not in counts(q, [r for r,c in zip(rs, code) if c == i])
               for i,q in enumerate(qs)):
            void += prod(F(r-k if c == -1 else 1, r) for r,c in zip(rs, code))
    assert prod(lower) <= void <= prod(upper)
    period = prod(rs)
    # Direct unit-divisor pairs rather than ternary exponent enumeration.
    total = 0
    for t in range(period):
        for q in qs:
            m = t + (q+1)//4
            ds = divisors(prod(r for r in rs if m % r == 0))
            if any((a+b) % q == 0 for a in ds for b in ds): break
        else:
            total += 1
    assert F(total, period) == void
    print('independent lower, exact interval void, independent upper:',
          prod(lower), void, prod(upper), 'period', period)


def phase():
    n = recovered = new = 0
    for q in (3, 7, 11, 15, 19, 23, 27):
        for t in range(1, 2049):
            m = t + (q+1)//4
            if gcd(q, m) != 1: continue
            n += 1
            ps = [r for r in (5, 7, 11, 13, 17, 19) if m % r == 0]
            b = prod(ps)
            box = counts(q, ps)
            if (-b * pow(m, -1, q)) % q not in box: continue
            ds = divisors(m)
            assert any((a+d) % q == 0 for a in ds for d in ds)
            recovered += 1; new += q-1 not in box
    assert 0 < new < recovered
    print('complementary-phase checks: rows, recovered hits, new vs band alone:',
          n, recovered, new)


if __name__ == '__main__':
    print('Engine: scripts/z82_b34_controls.py | exact integer and Fraction arithmetic | deterministic')
    harris()
    phase()
