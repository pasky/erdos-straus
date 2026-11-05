"""Independent, streaming checks for the z57 COMPLEMENT cross-review.

Run with uv run --no-project, under an external timeout and memory limit.
ROOT is an archive of the reviewed branch; prime_census.txt is a fresh run of
z57_complement_words.c range 5 4000000 3, not the archived zero-only data.
Optional --stats recomputes the 1e9 table using one multi-response OLS fit.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import gzip
from itertools import combinations
from math import isqrt, sqrt
from pathlib import Path

LIMIT = 4_000_000
FAMILIES = {'STAR': 2, 'B1': 3, 'I1': 4, 'c2': 11, 'c3': 12, 'G': 7, 'K': 8}
PAIRS = list(combinations(FAMILIES, 2))


def prime_sieve():
    sieve = bytearray(b'\x01') * (LIMIT + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p * p::p] = b'\x00' * ((LIMIT - p * p) // p + 1)
    return sieve


def census(root):
    sieve = prime_sieve()
    denom = Counter()
    for n in range(5, LIMIT + 1, 4):
        kind = 'prime' if sieve[n] else ('square' if isqrt(n) ** 2 == n else 'composite')
        denom[kind, len(str(n)) - 1] += 1
    for name, path in [('fresh primes', root / 'prime_census.txt'),
                       ('archived sparse census', root / 'data/z57/complement/census_le4e6_anyzero.txt.gz')]:
        zero = defaultdict(Counter)
        joint = defaultdict(Counter)
        marginal = Counter()
        union3 = defaultdict(list)
        union5 = defaultdict(list)
        local = Counter()
        local_zero = Counter()
        rows = 0
        previous = 0
        op = gzip.open if path.suffix == '.gz' else open
        with op(path, 'rt') as fh:
            for line in fh:
                row = list(map(int, line.split()[:13]))
                n = row[0]
                assert n > previous and n % 4 == 1
                previous = n
                if n > LIMIT:
                    print('excluded out-of-range row:', n)
                    continue
                kind = 'prime' if sieve[n] else ('square' if isqrt(n) ** 2 == n else 'composite')
                if name == 'fresh primes':
                    assert kind == 'prime'
                rows += 1
                d = len(str(n)) - 1
                events = {f: row[c] == 0 for f, c in FAMILIES.items()}
                for f, event in events.items():
                    if event:
                        zero[kind][f] += 1
                        marginal[kind, d, f] += 1
                        local_zero[d, n % 840, f] += 1
                local[d, n % 840] += 1
                for a, b in PAIRS:
                    joint[kind][a, b] += events[a] and events[b]
                if all(events[f] for f in ('STAR', 'B1', 'I1')):
                    union3[kind].append(n)
                if all(events[f] for f in ('STAR', 'B1', 'I1', 'c2', 'c3')):
                    union5[kind].append(n)
        print('\n' + name, 'rows:', rows)
        if name == 'fresh primes':
            assert rows == sum(v for (k, d), v in denom.items() if k == 'prime')
        for kind in ('prime', 'composite', 'square'):
            if not zero[kind]:
                continue
            print(kind, 'population', sum(v for (k, d), v in denom.items() if k == kind), 'zeros', dict(zero[kind]))
            for a, b in PAIRS:
                pred = sum(marginal[kind, d, a] * marginal[kind, d, b] / N
                           for (k, d), N in denom.items() if k == kind)
                print(f'  {a}&{b}: {joint[kind][a,b]} / decade-pred {pred:.6f}')
            print('  three/five union zeros:', len(union3[kind]), len(union5[kind]),
                  union3[kind][:10], union5[kind][:10])
        if name == 'fresh primes':
            for a, b in [('c2', 'c3'), ('G', 'K')]:
                pred = sum(local_zero[d, r, a] * local_zero[d, r, b] / N
                           for (d, r), N in local.items())
                variance = sum(local_zero[d, r, a] * local_zero[d, r, b]
                               * (N - local_zero[d, r, a]) * (N - local_zero[d, r, b])
                               / (N * N * (N - 1))
                               for (d, r), N in local.items() if N > 1)
                print(f'  {a}&{b} decade+mod840 prediction: {pred:.6f}; '
                      f'conditional-null SD={sqrt(variance):.6f}; '
                      f'z={(joint["prime"][a,b] - pred) / sqrt(variance):.6f}')


def direct_certificates():
    # Independent pair enumeration: no factoring, no imported lane routines.
    for n in (105, 193, 577, 2521, 102001):
        counts = Counter({f: 0 for f in ('STAR', 'B1', 'I1', 'c2', 'c3')})
        for c in (1, 2, 3):
            N = c * n
            for u in range(1, isqrt(N + 1) + 2):
                # t>=1; for u=1, t>=2 since N>0, hence v<=N+1.
                vmax = N + 1 if u == 1 else (N + u) // (u - 1)
                for v in range(u, vmax + 1):
                    if (N + u + v) % (u * v):
                        continue
                    t = (N + u + v) // (u * v)
                    weight = 1 if u == v else 2
                    if c == 1:
                        counts['STAR'] += weight * (t % 4 == 0)
                        counts['B1'] += weight * (u % 4 == 0 or v % 4 == 0)
                        counts['I1'] += weight * (t * u % 4 == 1 or t * v % 4 == 1)
                    elif t % (4 * c) == 0:
                        counts[f'c{c}'] += weight
                        if n == 105:
                            d = t // (4 * c)
                            triple = (u * v * d, u * c * d * n, v * c * d * n)
                            assert sum(Fraction(1, x) for x in triple) == Fraction(4, n)
                            print('105 certificate:', (t, u, v), 'c=', c, 'denominators=', triple)
        print('direct pair enumeration:', n, dict(counts))
    # The purported unit residue in C(ii) need not be a unit.
    print('C(ii) counterexample: U=1, M=4, u=c=1, b=3, m=1, mprime=3;')
    print('  p=1 mod 4 and 3 | p+3 forces p=3, which is not 1 mod 4: probability 0, not 1/phi(3).')


def proof_checks(root):
    jacobi_path = root / 'jacobi_check.txt'
    if jacobi_path.exists():
        with jacobi_path.open() as fh:
            rows = 0
            for line in fh:
                assert line.split()[-1] == 'jacfail=0'
                rows += 1
        print('Fresh engine Jacobi check: prime rows', rows, 'failures 0')
    # C1's exact identity misses v=1 at small primes in the averaging range.
    p, u, y = 17, 2, 39  # x=10^8, theta=1/5 gives floor(y)=39.
    classes = []
    for residue in (1, 3, 5, 7):
        t = (residue + 1) // u
        v = (p + u) * pow(residue, -1, 4) % 4
        if not (t % 4 == 0 or u % 4 == 0 or v % 4 == 0
                or t * u % 4 == 1 or t * v % 4 == 1):
            classes.append(residue)
    divisors = [m for m in range(1, y + 1) if (p + u) % m == 0 and m % 8 in classes]
    qr = [(m, (m + 1) // u, (p + u) // m) for m in divisors
          if min(u, (m + 1) // u, (p + u) // m) >= 2]
    print('C1 counterexample: QR classes', classes, 'divisors', divisors,
          'D-delta=', len(divisors) - 1, 'actual QR=', len(qr))


def stats(root):
    import numpy as np
    files = sorted((root / 'data/z57/complement').glob('w_1e9_*.txt.gz'))
    data = []
    for path in files:
        with gzip.open(path, 'rt') as fh:
            data.extend([int(x) for x in line.split()[:13]] for line in fh)
    A = np.asarray(data, dtype=np.int64)
    del data
    p = A[:, 0]
    mods = [8, 3, 9, 5, 25, 7, 49, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    columns = [np.ones(len(p))]
    for q in mods:
        r = p % q
        columns.extend((r == v).astype(float) for v in np.unique(r)[1:])
    X = np.column_stack(columns)
    del columns
    families = list(FAMILIES)
    Y = A[:, [FAMILIES[f] for f in families]].astype(float)
    print('OLS shapes:', X.shape, Y.shape, 'design bytes:', X.nbytes)
    residual = Y - X @ np.linalg.lstsq(X, Y, rcond=None)[0]
    correlations = np.corrcoef(residual, rowvar=False)
    events = np.zeros(Y.shape, dtype=bool)
    predicted = np.zeros((len(families), len(families)))
    for r in np.unique(p % 840):
        mask = p % 840 == r
        events[mask] = Y[mask] <= np.quantile(Y[mask], .05, axis=0)
        sizes = events[mask].sum(axis=0)
        predicted += np.outer(sizes, sizes) / mask.sum()
    observed = events.astype(np.int64).T @ events.astype(np.int64)
    for i, a in enumerate(families):
        for j in range(i + 1, len(families)):
            print(f'{a}-{families[j]}: r={correlations[i,j]:+.6f}, tail={observed[i,j]/predicted[i,j]:.6f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('--stats', action='store_true')
    args = parser.parse_args()
    direct_certificates()
    proof_checks(args.root)
    census(args.root)
    if args.stats:
        stats(args.root)
