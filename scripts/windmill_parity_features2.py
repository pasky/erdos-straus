"""Broader GF(2) search: square-indicators / residues of derived quantities.

A weight w(sol)=tau(N(sol)) has parity [N(sol) is a square], so these columns
test 'decorated' fixed-point sets of divisor type.  Same train/validate scheme
as windmill_parity_features.py.
"""
from __future__ import annotations
import sys
from math import gcd, isqrt
import numpy as np
from windmill_parity_features import load, gf2_solve, leg, issq


def derived(p, sol):
    x, y, z = sol
    pd = [v % p == 0 for v in sol]
    Q = {}
    if sum(pd) == 2:
        fr = [v for v in sol if v % p][0]
        Y, Z = sorted(v // p for v in sol if v % p == 0)
        q = 4 * fr - p
        D, D2 = q * Y - fr, q * Z - fr
        assert D * D2 == fr * fr
        g = gcd(Y, Z); a, b = Z // g, Y // g
        c = fr // (a * b); k = g // c if c else 0
        Q.update(T=2, u=fr, Y=Y, Z=Z, mod=q, D=D, D2=D2, g=g, a=min(a, b), b=max(a, b), c=c, k=k)
    else:
        z0 = [v for v in sol if v % p == 0][0] // p
        X, Yy = sorted(v for v in sol if v % p)
        m = (4 * z0 - 1) // p
        D, D2 = sorted((m * X - z0, m * Yy - z0))
        assert D * D2 == z0 * z0
        g = gcd(X, Yy); a, b = X // g, Yy // g
        c = z0 // (a * b); k = g // c if c else 0
        Q.update(T=1, u=z0, Y=X, Z=Yy, mod=m, D=D, D2=D2, g=g, a=a, b=b, c=c, k=k)
    Q['Y+Z'] = Q['Y'] + Q['Z']; Q['YZ'] = Q['Y'] * Q['Z']
    Q['D+D2'] = Q['D'] + Q['D2']; Q['D2-D'] = Q['D2'] - Q['D']
    Q['Z-Y'] = Q['Z'] - Q['Y']; Q['a+b'] = Q['a'] + Q['b']; Q['b-a'] = Q['b'] - Q['a']
    Q['4Y-1*4Z-1'] = (4 * Q['Y'] - 1) * (4 * Q['Z'] - 1)
    Q['uY'] = Q['u'] * Q['Y']; Q['uZ'] = Q['u'] * Q['Z']
    return Q


def features(p, sol):
    Q = derived(p, sol)
    T = Q.pop('T')
    F = {'one': 1, 'typeII': T == 2}
    for tt in (1, 2):
        for k, v in Q.items():
            pre = f'T{tt}:{k}:'
            on = T == tt
            F[pre + 'sq'] = on and v > 0 and issq(v)
            F[pre + '2sq'] = on and v > 0 and v % 2 == 0 and issq(v // 2)
            F[pre + 'even'] = on and v % 2 == 0
            F[pre + 'm3'] = on and v % 3 == 0
            F[pre + 'm4=1'] = on and v % 4 == 1
            F[pre + 'm8'] = on and v % 8 == 0
            F[pre + 'leg'] = on and leg(v, p) == 1
            F[pre + 'is1'] = on and v == 1
    return {k: int(bool(v)) for k, v in F.items()}


def main():
    data = load(sys.argv[1])
    primes = sorted(data)
    names = None; rows = []
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
    for k, d in zip(names, A.mean(axis=0)):
        if d < 0.15 or d > 0.85:
            print('  skewed', k, round(float(d), 3))
    half = len(primes) // 2
    w = gf2_solve(A[:half], np.ones(half, dtype=np.uint8))
    if w is None:
        print('no combination odd on training half')
    else:
        pred = (A[half:].astype(int) @ w.astype(int)) % 2
        print('validation odd fraction', pred.mean(), [names[i] for i in np.nonzero(w)[0]])
    print('full solvable:', gf2_solve(A, np.ones(len(primes), dtype=np.uint8)) is not None)


if __name__ == '__main__':
    main()
