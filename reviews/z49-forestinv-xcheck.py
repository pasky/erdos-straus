"""Independent boundary/sign and cylinder checks for the z49 cross-review.
No imports from the submitted scripts. Run with uv run python.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from collections import Counter
import sys


def jac(a, n):
    s = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def hj(n, q):
    out = []
    while q:
        b = (n + q - 1) // q
        out.append(b)
        n, q = q, b * q - n
    return tuple(out)


def good(v, n):
    return v % 4 == 0 or v % 8 == (-n) % 8


words = witnesses = small = 0
for n in range(5, 4001, 4):
    # Unique possible smaller neighbour of v, plus the diagonal candidate.
    for v in range(1, n + 3):
        u = (-n) % v or v
        if (n + u + v) % (u * v):
            continue
        t = (n + u + v) // (u * v)
        words += 1
        g = gcd(u, v)
        assert gcd(u, n) == gcd(v, n) == g
        assert (g * t) * (u // g) * (v // g) - u // g - v // g == n // g
        for e in {u, v}:
            if good(e, n):
                A = t * e - 1
                witnesses += 1
                assert gcd(A, n) == 1 and jac(A, n) == -1
                assert A > 1 and (A != 2 or (e == 3 and n % 8 == 5))
                small += A == 2
        if n in (17, 241):
            assert u % 8 and v % 8
print(f"Unique-parent check: {words} unordered words, {witnesses} U-endpoint incidences; {small} A=2 incidences; PASS")

# Each cylinder is [Q_j/P_j, (Q_j-Q_{j-1})/(P_j-P_{j-1})) in q/p.
primes = [p for p in range(5, 400) if p % 4 == 1 and all(p % d for d in range(2, isqrt(p) + 1))]
checks = 0
for p in primes:
    expansions = {q: hj(p, q) for q in range(1, p)}
    patterns = {ds[:j] for ds in expansions.values() for j in range(1, min(4, len(ds)) + 1)}
    for beta in patterns:
        P0, P1, Q0, Q1 = 0, 1, -1, 0
        for b in beta:
            P0, P1, Q0, Q1 = P1, b * P1 - P0, Q1, b * Q1 - Q0
        lo, hi = Fraction(Q1, P1), Fraction(Q1 - Q0, P1 - P0)
        actual = {q for q, ds in expansions.items() if ds[:len(beta)] == beta}
        predicted = {q for q in expansions if lo <= Fraction(q, p) < hi}
        assert actual == predicted, (p, beta, actual, predicted)
        checks += 1
print(f"Exact rational cylinder endpoints: {checks} prime/prefix pairs, depths 1..4; PASS")

for a in range(7, 150, 8):
    for b in range(7, 2000, 8):
        if (b + 2) % a:
            continue
        n, A = a * b, b + 1
        m = A // 8
        assert Fraction(1, m * a) + Fraction(1, m * a * A) + Fraction(1, n * m * A) == Fraction(8, n)
print("Lemma 2.5 numerator-8 identity: PASS")

if len(sys.argv) == 2:
    source = Path(sys.argv[1]) / "data/z49_forestinv"
    rows = [line.split() for line in (source / "scan_105_1e9_1e10.txt").read_text().splitlines()]
    hist = Counter(int(row[3].split("=")[1]) for row in rows)
    start = 10**9 + ((105 - 10**9) % 840)
    total = (10**10 - start) // 840 + 1
    squares = sum(m % 105 == 0 for m in range(isqrt(10**9) + 1, isqrt(10**10) + 1, 1) if m % 2)
    print(f"Archived high-range records={len(rows)}, rescue-line histogram={dict(sorted(hist.items()))}")
    print(f"Independent domain count: total={total}, squares={squares}, nonsquares={total-squares}")
