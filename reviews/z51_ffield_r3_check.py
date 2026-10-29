#!/usr/bin/env python3
"""Independent, bounded R3 audit: product-bucket overlap counts and class constants.
Run: ulimit -v 8000000; timeout 120s uv run --no-project reviews/z51_ffield_r3_check.py
No imports from the author's check; prime fields only. No Cartesian-product arrays.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import log


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return tuple(a)


def plus(a, b, p):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim([x % p for x in out])


def times(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return trim(out)


def rem(a, b, p):
    a = list(a)
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, p) % p
        k = len(a) - len(b)
        for j, y in enumerate(b):
            a[k+j] = (a[k+j] - c*y) % p
        while a and not a[-1]:
            a.pop()
    return tuple(a)


def gcd(a, b, p):
    while b:
        a, b = b, rem(a, b, p)
    return tuple(x * pow(a[-1], -1, p) % p for x in a)


def overlaps(p, D):
    buckets = defaultdict(list)
    monics = {d: [tuple(c)+(1,) for c in product(range(p), repeat=d)]
              for d in range(1, D)}
    for a in range(1, D):
        for b in range(a, D-a+1):
            pairs = (combinations_with_replacement(monics[a], 2) if a == b
                     else product(monics[a], monics[b]))
            for u, v in pairs:
                buckets[times(u, v, p)].append((plus(u, v, p), a, b))
    hist = defaultdict(Counter)
    strata = Counter()
    # Distinct factorizations of the same product cannot have the same sum.
    for entries in buckets.values():
        assert len({entry[0] for entry in entries}) == len(entries)
    for M, N in combinations(buckets, 2):
        h = gcd(M, N, p)
        gamma = len(h)-1
        if not gamma:
            continue
        deriv = trim([i*h[i] % p for i in range(1, len(h))])
        nonsq = len(gcd(h, deriv, p)) > 1
        case = ('nonsquarefree' if nonsq else
                'containment' if gamma == min(len(M), len(N))-1 else 'proper')
        lcmdegree = len(M)+len(N)-2-gamma
        left = defaultdict(list)
        right = defaultdict(list)
        for S, a, b in buckets[M]:
            left[rem(S, h, p)].append((a, b))
        for S, a, b in buckets[N]:
            right[rem(S, h, p)].append((a, b))
        for residue in left.keys() & right.keys():
            for a, b in left[residue]:
                for c, d in right[residue]:
                    hist[case][lcmdegree] += 2  # ordered classes, unlike author script
                    strata[a,b,c,d,gamma] += 1
                    strata[c,d,a,b,gamma] += 1
    total = Fraction(0)
    sums = {}
    for case, counts in sorted(hist.items()):
        sums[case] = sum((Fraction(count, p**degree) for degree, count in counts.items()), Fraction(0))
        total += sums[case]
    worst = max((Fraction(count, p**(a+b+c+d-g-1)), (a,b,c,d,g))
                for (a,b,c,d,g), count in strata.items())
    print(f'p={p} D={D} classes={sum(map(len, buckets.values()))} '
          f'ordered q*S={float(p*total):.9f} exact S={total} '
          f'per-case q*S={ {k: round(float(p*v), 9) for k,v in sums.items()} } '
          f'max N_gamma/q^(d+dprime-gamma-1)={worst}', flush=True)


def F(m):
    return (m-1)**2 // 4


def count(n):
    m = n//4
    return F(m) - (F(m//2) if n % 2 == 0 else 0)


def constants():
    # Independent direct enumeration checks the exact closed formula.
    for n in range(12, 1201):
        m = n//4
        brute = sum(1 for a in range(1, m) for b in range(a+1, m-a+1)
                    if n % 2 or a % 2 or b % 2)
        assert brute == count(n)
    for lo, hi in [(12,1200), (100,1200), (12,1000000), (100,1000000)]:
        ratio, n = min((Fraction(count(n), n*n), n) for n in range(lo, hi+1))
        print(f'n={lo}..{hi}: min C/n²={ratio} at n={n}; '
              f'exponent={-log(.38)*float(ratio):.12f}', flush=True)
    print('asymptotic exponents even/odd:', -log(.38)*3/256, -log(.38)/64)


if __name__ == '__main__':
    for p, D in [(3,3), (7,3), (11,3), (3,4), (5,4)]:
        overlaps(p, D)
    constants()
