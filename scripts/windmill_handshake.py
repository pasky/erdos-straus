"""Handshake-lemma scan on the signed refactor graph (WINDMILL.md §3.4).

For a canonically defined subgraph H (edges through denominators of a given
bucket class), sum_{v nonpositive} deg_H(v) = E_H(pos,nonpos) (mod 2) once the
pos-pos edges are discounted, so a handshake proof needs E_H(pos,nonpos) odd for
every p.  Per bucket d this is a_d*b_d (a=#positive, b=#nonpositive vertices
containing d).  We GF(2)-search over bucket classes.
"""
import sys
from collections import defaultdict
import numpy as np
from windmill_signed_parity import load
from windmill_parity_features import gf2_solve


def bucket_classes(p, d, verts):
    t = (p - 1) // 4
    C = {}
    pd = d % p == 0
    m = d // p if pd else None
    C['all'] = True
    C['pdiv'] = pd
    C['pfree'] = not pd
    C['neg'] = d < 0
    C['pos'] = d > 0
    C['pfree_small'] = (not pd) and 1 <= d <= 2 * t
    C['pfree_mid'] = (not pd) and 2 * t < d < p
    C['pfree_big'] = (not pd) and d >= p
    C['pfree_neg'] = (not pd) and d < 0
    C['pdiv_typeI'] = pd and (4 * m - 1) % p == 0
    C['pdiv_typeII'] = pd and (4 * m - 1) % p != 0
    C['pdiv_neg'] = pd and d < 0
    C['hub_t'] = d == t
    C['hub_-pt'] = d == -p * t
    C['d_even'] = d % 2 == 0
    C['d_3'] = d % 3 == 0
    C['size2'] = len(verts) == 2
    C['size_odd'] = len(verts) % 2 == 1
    return C


def main():
    data = load(sys.argv[1])
    primes = sorted(data)
    names = None; rows = []
    for p in primes:
        V = data[p]
        B = defaultdict(list)
        for v in V:
            for d in set(v):
                B[d].append(v)
        acc = None
        for d, L in B.items():
            a = sum(1 for v in L if v[0] > 0); b = len(L) - a
            C = bucket_classes(p, d, L)
            names = names or list(C)
            vec = np.array([int(C[k]) * (a * b % 2) for k in names], dtype=np.int64)
            acc = vec if acc is None else acc + vec
        rows.append(acc % 2)
    A = np.array(rows, dtype=np.uint8)
    for k, c in zip(names, A.mean(axis=0)):
        print(f'{k:14s} odd fraction {c:.3f}')
    half = len(primes) // 2
    w = gf2_solve(A[:half], np.ones(half, dtype=np.uint8))
    print('GF2 combo on training half:', None if w is None else [names[i] for i in np.nonzero(w)[0]])
    if w is not None:
        print('validation', ((A[half:].astype(int) @ w.astype(int)) % 2).mean())


if __name__ == '__main__':
    main()
