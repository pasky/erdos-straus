"""GF(2) search for an always-odd weighted count of positive ES solutions.

Reads the output of windmill_enum.cpp.  For every prime p and every boolean
feature f of an unordered positive solution, c_f(p) = #{sol : f(sol)} mod 2.
Counts mod 2 are GF(2)-linear in f, so we look for a GF(2) combination of the
feature columns equal to the all-ones vector (always-odd count).  Features are
trained on the first half of the primes and validated on the second half.

uv run python scripts/windmill_parity_features.py /tmp/wm/pos60k.txt
"""
from __future__ import annotations
import sys
from math import gcd, isqrt
import numpy as np


def load(path):
    data = {}
    p = None
    for line in open(path):
        if line.startswith('P'):
            p = int(line.split()[1]); data[p] = []
        else:
            data[p].append(tuple(map(int, line.split())))
    return data


def leg(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def issq(n):
    return n >= 0 and isqrt(n) ** 2 == n


def features(p, sol):
    x, y, z = sol
    t = (p - 1) // 4
    pd = [v % p == 0 for v in sol]
    typ = 2 if sum(pd) == 2 else 1
    F = {}
    F['one'] = 1
    F['typeII'] = typ == 2
    F['pattern'] = None
    for i in range(3):
        F[f'pdiv{i}'] = pd[i]
    red = [v // p if v % p == 0 else v for v in sol]
    for i, v in enumerate(sol):
        for m in (2, 3, 4, 8, 5, 7):
            for r in range(m):
                if m == 2 and r == 1:
                    continue
                F[f'v{i}%{m}=={r}'] = v % m == r
        F[f'sq{i}'] = issq(red[i])
        F[f'leg{i}'] = leg(red[i], p) == 1
        F[f'red_even{i}'] = red[i] % 2 == 0
    F['x|y'] = y % x == 0
    F['y|z'] = z % y == 0
    F['x|z'] = z % x == 0
    F['g>1'] = gcd(gcd(x, y), z) > 1
    F['gxy>1'] = gcd(x, y) > 1
    F['gyz>1'] = gcd(y, z) > 1
    F['gxz>1'] = gcd(x, z) > 1
    L = x * y // gcd(x, y)
    F['z=lcm(xy)'] = z == L
    F['z|lcm'] = L % z == 0
    F['x<=2t'] = x <= 2 * t
    F['x<=t+t/2'] = 2 * x <= 3 * t
    F['x==y'] = x == y
    F['y==z'] = y == z
    q = 4 * x - p
    F['q%8==3'] = q % 8 == 3
    F['q_sq'] = issq(q)
    F['q_prime_like'] = all(q % d for d in range(2, isqrt(q) + 1)) and q > 1
    del F['pattern']
    return {k: int(bool(v)) for k, v in F.items()}


def gf2_solve(A, b):
    """Solve A w = b over GF(2); return w or None. A: (n,m) uint8."""
    A = A.copy() % 2
    b = b.copy() % 2
    n, m = A.shape
    M = np.concatenate([A, b[:, None]], axis=1).astype(np.uint8)
    piv = []
    r = 0
    for c in range(m):
        rows = np.nonzero(M[r:, c])[0]
        if len(rows) == 0:
            continue
        k = r + rows[0]
        M[[r, k]] = M[[k, r]]
        others = np.nonzero(M[:, c])[0]
        others = others[others != r]
        M[others] ^= M[r]
        piv.append(c)
        r += 1
        if r == n:
            break
    # consistency
    for i in range(r, n):
        if M[i, m]:
            return None
    w = np.zeros(m, dtype=np.uint8)
    for i, c in enumerate(piv):
        w[c] = M[i, m]
    return w


def gf2_rank(A):
    M = A.copy() % 2
    r = 0
    for c in range(M.shape[1]):
        rows = np.nonzero(M[r:, c])[0]
        if len(rows) == 0:
            continue
        k = r + rows[0]
        M[[r, k]] = M[[k, r]]
        others = np.nonzero(M[:, c])[0]
        others = others[others != r]
        M[others] ^= M[r]
        r += 1
        if r == M.shape[0]:
            break
    return r


def main():
    data = load(sys.argv[1])
    primes = sorted(data)
    names = None
    rows = []
    for p in primes:
        acc = None
        for s in data[p]:
            F = features(p, s)
            if names is None:
                names = list(F)
            v = np.array([F[k] for k in names], dtype=np.int64)
            acc = v if acc is None else acc + v
        rows.append(acc % 2)
    A = np.array(rows, dtype=np.uint8)
    print('primes', len(primes), 'features', len(names))
    dens = A.mean(axis=0)
    for k, d in zip(names, dens):
        if d < 0.1 or d > 0.9:
            print('  skewed feature parity', k, d)
    half = len(primes) // 2
    w = gf2_solve(A[:half], np.ones(half, dtype=np.uint8))
    if w is None:
        print('no combination odd on training half')
    else:
        pred = (A[half:].astype(int) @ w.astype(int)) % 2
        print('train-solvable; validation odd fraction', pred.mean(),
              'combo', [names[i] for i in np.nonzero(w)[0]])
    w = gf2_solve(A, np.ones(len(primes), dtype=np.uint8))
    print('full solvable:', w is not None)
    print('GF(2) rank', gf2_rank(A))


if __name__ == '__main__':
    main()
