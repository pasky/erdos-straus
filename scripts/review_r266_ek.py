"""R266 from-scratch check of Thm 2.5 (numerator models k/n = 1/x+1/y+1/z).

Complete search: WLOG x<=y<=z, so n/k < x <= 3n/k.  For fixed x the remainder r = A/B (reduced) must be
1/y + 1/z with x <= y <= z.  Writing u = A*y - B, v = A*z - B (both > 0 since 1/y < r), we get u*v = B^2,
u <= v, so u is a divisor of B^2 with u <= B and u = -B (mod A); conversely each such u gives (y, z).
Cross-checked against a naive y-loop for small n (mode 'selftest').
"""
import sys
from math import gcd
from sympy import factorint, isprime, primerange


def divs_sq(B):
    ds = [1]
    for q, e in factorint(B).items():
        ds = [d * q**t for d in ds for t in range(2 * e + 1)]
    return ds


def sols(k, n, first=False):
    out = []
    lo = n // k + 1                  # x > n/k
    for x in range(max(lo, 1), 3 * n // k + 1):
        A, B = k * x - n, n * x
        g = gcd(A, B); A //= g; B //= g
        for u in divs_sq(B):
            if u > B or (u + B) % A:
                continue
            v = B * B // u
            if (v + B) % A:
                continue
            y, z = (u + B) // A, (v + B) // A
            if y < x:
                continue
            out.append((x, y, z))
            if first:
                return out
    return out


def naive(k, n):
    from fractions import Fraction as F
    out = []
    for x in range(n // k + 1, 3 * n // k + 1):
        r = F(k, n) - F(1, x)
        if r <= 0:
            continue
        y = max(x, int(1 / r) + 1)
        while F(2, y) >= r:
            rr = r - F(1, y)
            if rr > 0 and rr.numerator == 1 and rr.denominator >= y:
                out.append((x, y, rr.denominator))
            y += 1
    return out


def soluble(k, n):
    return bool(sols(k, n, first=True))


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'selftest':
        bad = 0
        for k in range(4, 14):
            for n in range(2, 120):
                a, b = sorted(sols(k, n)), sorted(naive(k, n))
                if a != b:
                    bad += 1; print('MISMATCH', k, n, len(a), len(b))
        print('selftest mismatches:', bad)
    elif mode == 'ek':
        for k in range(8, 26):
            E = [p for p in primerange(2, 2000) if not soluble(k, p)]
            print(f'k={k} #E_k primes<2000 = {len(E)} max={max(E)} list={E}', flush=True)


def laws():
    import re
    from sympy import primefactors
    rows = {}
    for line in open('logs/review_r266_ek.txt'):
        m = re.match(r'k=(\d+) .*list=(\[.*\])', line)
        rows[int(m.group(1))] = eval(m.group(2))
    sq = []
    for k in range(8, 26):
        E = rows[k]
        sq += [(k, p) for p in E if p < 400 and not soluble(k, p * p)]
        tr = [p for p in E if p > 2 and all(soluble(k, q) for q in primefactors((p * p - 1) // 4) if q > k)]
        uv = [p for p in E if p > 3 and soluble(k, (p - 1) // 2) and soluble(k, (p + 1) // 2)]
        print(f'k={k} truncated-law fails at {tr[:8]} ; uv-law fails at {uv[:8]}', flush=True)
    print('square law: p^2 exceptional (k,p):', sq)
    print('k=10 p=61:', (61 * 61 - 1) // 4, primefactors(930), 'S(10/31)=', soluble(10, 31), 'S(10/61)=', soluble(10, 61))
    print('8/121 sols (first):', sols(8, 121)[:3], 'S(8/11)=', soluble(8, 11))
    print('k=8 p=131: S(8/65)=', soluble(8, 65), 'S(8/66)=', soluble(8, 66))


if __name__ == '__main__' and sys.argv[1] == 'laws':
    laws()
