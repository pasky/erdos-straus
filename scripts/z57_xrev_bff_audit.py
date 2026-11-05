#!/usr/bin/env python3
"""Independent bounded audit; usage: uv run --with sympy SCRIPT /tmp/xrev_BFF.
Input is an archive of side-agent/z57-bff. No dense Cartesian arrays.
"""
import math
from pathlib import Path
import re
import sys

from sympy import divisors, isprime, jacobi_symbol, legendre_symbol, primerange

root = Path(sys.argv[1])
data = root / "data/z57/bff"


def gstar(p, n, m):
    return max(n, m) ** 4 > min(n, m) * p


def floor_fourth(x):
    return math.isqrt(math.isqrt(x))


def solutions(p):
    # Independent enumeration: order n <= m and bound C from m >= n.
    out = set()
    n = 1
    while 4 * n * n - 2 * n <= p:
        for c in range(1, (p + 2 * n) // (4 * n * n) + 1):
            m, rem = divmod(p + n, 4 * n * c - 1)
            if not rem and m >= n:
                assert 4 * n * m * c - n - m == p
                out.add((n, m, c))
        n += 1
    return out


def from_d(p, d):
    n = (-p) % d
    if not n or (d + 1) % (4 * n):
        return None
    m, rem = divmod(p + n, d)
    assert rem == 0
    c = (d + 1) // (4 * n)
    assert 4 * n * m * c - n - m == p
    return min(n, m), max(n, m), c


nprimes = nsolutions = 0
for p in primerange(5, 10001):
    if p % 4 != 1:
        continue
    expected = {s for s in solutions(p) if gstar(p, *s[:2])}
    got = set()
    for d in range(3, floor_fourth(p ** 3) + 2, 4):
        sol = from_d(p, d)
        if sol and gstar(p, *sol[:2]):
            got.add(sol)
    assert got == expected, (p, got, expected)
    nprimes += 1
    nsolutions += len(expected)
print("Independent complete (n,C) vs d enumeration:", nprimes, "primes;", nsolutions, "G* solutions; zero mismatches")

cases = hits = 0
for p in primerange(5, 1001):
    if p % 4 != 1:
        continue
    for d in range(3, 2001, 4):
        if d % p == 0:
            assert from_d(p, d) is None
            continue
        n = (-p) % d
        c = pow(-4 * p, -1, d)
        conditions = ((d + 1) % (4 * n) == 0,
                      (d + 1) % (4 * c) == 0,
                      4 * n * c == d + 1,
                      n * c <= (d - 1) // 2,
                      4 * n * c < 5 * d)
        assert len(set(conditions)) == 1, (p, d, conditions)
        assert (4 * n * c - 1) % d == 0
        if conditions[0]:
            assert jacobi_symbol(-n, d) == jacobi_symbol(p, d) == legendre_symbol(d, p) == -1
            if d ** 4 * (d + 1) <= 4 * p ** 3:
                assert gstar(p, n, (p + n) // d)
            hits += 1
        cases += 1
for m in range(1, 100, 2):
    assert all(from_d(m * m, d) is None for d in range(3, 2001, 4))
print("Hyperbola/branch/Jacobi checks:", cases, "cases;", hits, "hits; 50 odd-square controls")


def primitive_norm(N, k):
    for b in range(math.isqrt(N // k) + 1):
        a = math.isqrt(N - k * b * b)
        if a * a + k * b * b == N and math.gcd(a, b) == 1:
            return True
    return False


zeros = list(map(int, (data / "gstar_zeros_le1e8.txt").read_text().split())) + [564661441]
norm_cases = 0
for p in sorted(set(zeros) | {p for p in primerange(5, 1001) if p % 4 == 1}):
    for C, forms in ((1, (1,)), (2, (1, 2)), (3, (1, 3))):
        N = 4 * C * p + 1
        fails = not any(d % (4 * C) == 4 * C - 1 for d in divisors(N))
        assert fails == any(primitive_norm(N, k) for k in forms), (p, C)
        if p in zeros:
            assert fails
        norm_cases += 1
print("Primitive norm criteria:", norm_cases, "prime/level pairs; zero mismatches")
assert len(zeros) == 38 and all(isprime(p) for p in zeros)
print("Zeros with actual least prime QNR=2:", [p for p in zeros if legendre_symbol(2, p) == -1])

# Audit every summary for exact coverage, total counts, and independent minimality
# of its reported maximum's witness (NOT an independent proof of block maximum).
pattern = re.compile(r"# \[(\d+),(\d+)\] primes=1\(4\): (\d+)  G\*-zeros: (\d+)  max first-hit d: (\d+) at p=(\d+)")
records = []
for path in sorted(data.glob("decide*.txt")):
    rows = [tuple(map(int, m.groups())) for m in pattern.finditer(path.read_text())]
    assert rows, path
    records.extend(rows)
    print(path.name, "blocks=", len(rows), "prime sum=", sum(r[2] for r in rows))
records.sort()
last = 4
for lo, hi, count, nz, first, p in records:
    assert lo == last + 1, (last, lo)
    last = hi
    assert lo <= p <= hi and isprime(p) and p % 4 == 1
    assert first <= floor_fourth(p ** 3) + 1
    for d in range(3, first + 1, 4):
        sol = from_d(p, d)
        if sol and gstar(p, *sol[:2]):
            assert d == first, (p, first, d)
            break
    else:
        raise AssertionError((p, first))
assert last == 10 ** 12
assert sum(r[2] for r in records) == 18803924340
assert sum(r[3] for r in records) == 38
print("Summary coverage/counts agree; independently checked first-hit minimality for", len(records), "reported extremal primes")
rerun = (root / "rerun_le1e9.txt").read_text()
assert list(map(int, re.findall(r"^Z (\d+)$", rerun, re.M))) == zeros
assert "primes=1(4): 25423491  G*-zeros: 38  max first-hit d: 787439 at p=231507061" in rerun
print("Actual C-decider rerun [5,1e9] agrees: 25,423,491 primes, exact same 38 zeros, maximum d=787439 at p=231507061")

# Recompute sample statistics and verify every recorded unrestricted first hit
# really is a G* hit in these samples (the generator does not enforce this).
import statistics
for scale in (8, 9, 10):
    rows = [list(map(int, line.split())) for line in
            (data / f"firsthit_1e{scale}.txt").read_text().splitlines() if not line.startswith("#")]
    exponents = []
    prime_missing = prime_corner = 0
    for p, first, n, c, in_g, dp in rows:
        assert isprime(p) and in_g == 1 and first == 4 * n * c - 1
        for d in range(3, first + 1, 4):
            sol = from_d(p, d)
            if sol:
                assert d == first and gstar(p, *sol[:2])
                break
        else:
            raise AssertionError(p)
        exponents.append(math.log(first) / math.log(p))
        if not dp:
            prime_missing += 1
        else:
            sol = from_d(p, dp)
            assert sol and isprime(dp)
            prime_corner += not gstar(p, *sol[:2])
    print(f"Sample 1e{scale}: N={len(rows)}, mean={statistics.mean(exponents):.6f}, "
          f"median={statistics.median(exponents):.6f}, max={max(exponents):.6f}; "
          f"prime-d missing/corner={prime_missing}/{prime_corner}")

# Independent primality and first-hit decisions at the upper endpoint.
top_primes = [p for p in range(999999900001, 1000000000001, 4) if isprime(p)]
max_pair = (0, 0)
for p in top_primes:
    for d in range(3, 3456, 4):
        sol = from_d(p, d)
        if sol and gstar(p, *sol[:2]):
            max_pair = max(max_pair, (d, p))
            break
    else:
        raise AssertionError(p)
assert len(top_primes) == 1788 and max_pair == (3455, 999999980701)
print("Independent upper-endpoint [999999900001,1e12]: 1788 primes, no zeros, maximum", max_pair)
