"""Correlate parities of ES solution counts with arithmetic invariants of p.

For each p = 1 mod 24 (from windmill_enum.cpp output) compute the count
parities f (all positive, unordered), f_I, f_II and a battery of invariants:
Legendre symbols (l/p), quartic character of small primes, representation by
x^2+32y^2 / x^2+64y^2, class numbers h(D) mod 2^k of D=-4p,-8p,-3p,-24p,...,
tau(t^2) mod 4, omega(t), etc.  Then GF(2)-solve target = combination.
"""
from __future__ import annotations
import sys
from math import isqrt, gcd
import numpy as np
from sympy import factorint
from windmill_parity_features import load, gf2_solve


def h_disc(D):
    """number of primitive reduced forms of negative discriminant D"""
    assert D < 0 and D % 4 in (0, 1)
    n = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if c == a and b < 0:
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            n += 1
        a += 1
    return n


def rep(p, k):
    y = 1
    while k * y * y < p:
        r = p - k * y * y
        if isqrt(r) ** 2 == r:
            return 1
        y += 1
    return 0


def invariants(p):
    t = (p - 1) // 4
    I = {}
    for l in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        I[f'leg{l}'] = pow(l, (p - 1) // 2, p) == 1
    for l in (2, 3, 5, 7):
        I[f'quart{l}'] = pow(l, (p - 1) // 4, p) == 1
    I['oct2'] = pow(2, (p - 1) // 8, p) == 1
    for k in (32, 64, 48, 72, 27, 16):
        I[f'rep{k}'] = rep(p, k)
    for D in (-4 * p, -8 * p, -3 * p, -24 * p, -12 * p, -7 * p, -20 * p):
        h = h_disc(D)
        for j in (1, 2, 3, 4):
            I[f'h{D // p}p_bit{j}'] = (h >> j) & 1
    f = factorint(t)
    tau = 1
    for e in f.values():
        tau *= 2 * e + 1
    I['tau_t2_mod4'] = (tau % 4) == 3
    I['omega_t_odd'] = len(f) % 2
    I['Omega_t_odd'] = sum(f.values()) % 2
    for m in (5, 7, 11, 13):
        for r in range(1, m):
            I[f'p%{m}=={r}'] = p % m == r
    for r in (1, 49, 97, 145):
        I[f'p%192=={r}'] = p % 192 == r
    I['one'] = 1
    return {k: int(bool(v)) for k, v in I.items()}


def main():
    data = load(sys.argv[1])
    primes = sorted(data)[: int(sys.argv[2]) if len(sys.argv) > 2 else None]
    targets = {'f': [], 'fI': [], 'fII': []}
    rows = []; names = None
    for p in primes:
        sols = data[p]
        nII = sum(1 for s in sols if sum(v % p == 0 for v in s) == 2)
        targets['f'].append(len(sols) % 2)
        targets['fII'].append(nII % 2)
        targets['fI'].append((len(sols) - nII) % 2)
        I = invariants(p)
        names = names or list(I)
        rows.append([I[k] for k in names])
    A = np.array(rows, dtype=np.uint8)
    print('primes', len(primes), 'invariants', len(names))
    half = len(primes) // 2
    for tn, tv in targets.items():
        b = np.array(tv, dtype=np.uint8)
        print(tn, 'odd fraction', b.mean())
        # single-invariant correlation
        best = sorted(((abs((A[:, i] == b).mean() - 0.5), names[i]) for i in range(len(names))), reverse=True)[:3]
        print('   best single agreement dev', [(round(d, 3), n) for d, n in best])
        w = gf2_solve(A[:half], b[:half])
        if w is None:
            print('   no GF2 combination on training half')
        else:
            pred = (A[half:].astype(int) @ w.astype(int)) % 2
            print('   GF2 combo validation accuracy', (pred == b[half:]).mean(), [names[i] for i in np.nonzero(w)[0]])


if __name__ == '__main__':
    main()
