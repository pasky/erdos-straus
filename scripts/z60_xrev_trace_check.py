"""Independent z60 TRACE audit. Run under timeout and ulimit -v 4000000.

uv run --with cypari2 python scripts/z60_xrev_trace_check.py /tmp/xrev_TRACE
The argument is an archive of side-agent/z60-trace with optional fresh_*.json.
Hurwitz numbers use reduced-form enumeration, NOT PARI's class-number engine.
PARI is used only for integer divisor lists. No large arrays are allocated.
"""
import csv
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt, prod
from pathlib import Path
from statistics import median

from cypari2 import Pari

pari = Pari()
root = Path(sys.argv[1])


@lru_cache(maxsize=10000)
def hurwitz(D):
    result = F(0)
    for a in range(1, isqrt(D // 3) + 1):
        for b in range(-a, a + 1):
            if (b * b + D) % (4 * a):
                continue
            c = (b * b + D) // (4 * a)
            if c < a or (b < 0 and (abs(b) == a or a == c)):
                continue
            result += F(1, 3 if a == b == c else 2 if b == 0 and a == c else 1)
    return result


def polynomial(k, t, N):
    # Closed polynomial, independent of the memo's recurrence.
    from math import comb
    return sum((-N) ** j * comb(k - 2 - j, j) * t ** (k - 2 - 2 * j)
               for j in range((k - 2) // 2 + 1))


def geometric(C, k, n):
    Q, N = 4 * C, 4 * C * n + 1
    primes = [int(p) for p in pari.factor(Q)[0]]
    mu = F(Q ** 3, 2) * prod(F(p * p - 1, p * p) for p in primes)
    ds = [int(d) for d in pari.divisors(N)]
    ES = sum(min(d, N // d) ** (k - 1) for d in ds if d % Q == Q - 1)
    TR = sum(min(d, N // d) ** (k - 1) for d in ds if d % Q == 1)
    E, L = F(0), isqrt(4 * N - 1)
    first = -L + (-2 - Q * n + L) % (Q * Q)
    for t in range(first, L + 1, Q * Q):
        E += polynomial(k, t, N) * hurwitz((4 * N - t * t) // (Q * Q))
    scalar = F(0)
    r = isqrt(N)
    if r * r == N:
        scalar = F(k - 1, 12) * mu * sum(
            lam ** (k - 2) for lam in (r, -r) if lam % Q == Q - 1)
    trace = -mu * E - mu / (2 * Q) * (ES + (-1) ** k * TR) + scalar
    if k == 2:
        trace += sum(ds)
    return trace, E, ES, TR, mu, len(ds), scalar


assert hurwitz(3) == F(1, 3) and hurwitz(4) == F(1, 2)
count = 0
for path in sorted((root / 'data/z60/trace').glob('*.json')) + sorted(root.glob('fresh_*.json')):
    text = path.read_text()
    data = json.loads(text[text.index('{'):])
    C, k = data['C'], data['k']
    for n, N, T, E, ES, TR in data['rows']:
        got = geometric(C, k, n)
        assert got[:4] == (F(T), F(E), ES, TR), (path, n, got)
        assert N == 4 * C * n + 1
        count += 1
    print('JSON', path.name, len(data['rows']), 'OK', flush=True)
print('JSON total', count, flush=True)

# The explicit family: also check the claimed empty window and absent scalar.
for C in range(2, 501):
    Q = 4 * C
    for k in (3, 5):
        T, E, ES, TR, mu, _, S = geometric(C, k, 2 * Q - 3)
        assert (E, ES, TR, S) == (0, 2 * (Q - 1) ** (k - 1), 2, 0)
        assert T == -(mu / Q) * ((Q - 1) ** (k - 1) - 1)
print('Family C=2..500, k=3,5: 998 geometric checks OK', flush=True)

# Aggregate the stored evidence using integer trace/ES fields, not rounded r.
for name, C in [('screen_C1_k3.tsv', 1), ('screen_C2_k3_range.tsv', 2),
                ('screen_C3_k3_range.tsv', 3)]:
    path = root / 'data/z60/trace' / name
    with path.open() as stream:
        rows = list(csv.DictReader((line for line in stream
                                    if not line.startswith(('PARI ', '#'))), delimiter='\t'))
    print('TSV columns', name, list(rows[0]), flush=True)
    ratios = []
    for row in rows:
        n = int(row['n'])
        T, E, ES, TR, mu, tau, _ = geometric(C, 3, n)
        # Column spelling is kept explicit so a changed schema fails loudly.
        assert T == F(row['Tr']) and ES == int(row['ES']) and TR == int(row['TRIV'])
        dim = mu / 6 - mu / (8 * C)
        D = dim * tau * (4 * C * n + 1)
        if ES:
            ratios.append(((D - T) / (mu / (8 * C) * ES), n))
    print('SCREEN', name, 'rows', len(rows), 'positive', len(ratios),
          'fires', sum(r < 1 for r, _ in ratios), 'min', min(ratios),
          'median', float(median(r for r, _ in ratios)), flush=True)

# Exhaustive root-pair enumeration at each n, using u <= B and divisors of n+u.
def pairs(n):
    for u in range(1, (1 + isqrt(1 + 4 * n)) // 4 + 1):
        for d0 in pari.divisors(n + u):
            d = int(d0)
            if (d + 1) % (4 * u) == 0:
                C, B = (d + 1) // (4 * u), (n + u) // d
                if C >= 1 and B >= u:
                    assert 4 * u * B * C - u - B == n
                    yield u, B, C


def screen_numbers(name):
    return [int(line.split()[0]) for line in (Path('data/z58/screens') / name).read_text().splitlines()
            if line and not line.startswith('#')]

for name in ('composite_zeros_le8e6.txt', 'star_prime_zeros.txt'):
    ns = screen_numbers(name)
    for n in ns:
        assert not list(pairs(n)), (name, n)
    print('GLOBAL ZERO', name, len(ns), 'OK', flush=True)

ns = screen_numbers('gstar_zeros.txt')
positive = []
for n in ns:
    hits = list(pairs(n))
    if hits:
        positive.append((n, hits[0]))
print('GSTAR zeros with global hits', len(positive), 'of', len(ns), flush=True)
print('GSTAR first global witness', positive[0], flush=True)
assert len(positive) == 24

for n in screen_numbers('r8_zeros_1e10.txt')[:1]:
    hits = list(pairs(n))
    assert hits and all(C % 2 for _, _, C in hits)
    print('R8 first zero independently checked', n, 'ordered R',
          sum(1 if u == B else 2 for u, B, C in hits), 'all C odd', flush=True)
print('ALL CHECKS PASSED', flush=True)
