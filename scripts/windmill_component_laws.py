"""Search for GF(2) linear relations that hold on EVERY component of the signed
graph (a Chen-type 'size congruence' mod 2).  Rows = components (all p=1 mod 24
below the data bound), columns = parities of component statistics.  The GF(2)
left-nullspace of the column space restricted to... we compute relations
w with A w = 0 (mod 2) for all rows, i.e. the nullspace of A.
"""
import sys
from collections import defaultdict
import numpy as np
from windmill_signed_parity import load, comps


def gf2_nullspace(A):
    A = A.copy() % 2
    n, m = A.shape
    piv = []; r = 0
    for c in range(m):
        rows = np.nonzero(A[r:, c])[0]
        if len(rows) == 0: continue
        k = r + rows[0]; A[[r, k]] = A[[k, r]]
        others = np.nonzero(A[:, c])[0]; others = others[others != r]
        A[others] ^= A[r]; piv.append(c); r += 1
        if r == n: break
    free = [c for c in range(m) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(m, dtype=np.uint8); v[f] = 1
        for i, c in enumerate(piv):
            v[c] = A[i, f]
        basis.append(v)
    return basis


def comp_stats(p, V, C):
    t = (p - 1) // 4
    S = {}
    vs = [V[i] for i in C]
    pos = [v[0] > 0 for v in vs]
    typ = [sum(1 for d in v if d % p == 0) for v in vs]
    nneg = [sum(1 for d in v if d < 0) for v in vs]
    S['size'] = len(vs); S['pos'] = sum(pos)
    S['T1'] = sum(1 for x in typ if x == 1)
    S['posT1'] = sum(1 for i in range(len(vs)) if pos[i] and typ[i] == 1)
    for k in (1, 2):
        S[f'neg{k}'] = sum(1 for x in nneg if x == k)
        S[f'neg{k}T1'] = sum(1 for i in range(len(vs)) if nneg[i] == k and typ[i] == 1)
    den = defaultdict(int)
    for v in vs:
        for d in set(v): den[d] += 1
    S['nden'] = len(den)
    S['npdiv'] = sum(1 for d in den if d % p == 0)
    S['npdivI'] = sum(1 for d in den if d % p == 0 and (4 * (d // p) - 1) % p == 0)
    S['npfree_small'] = sum(1 for d in den if d % p and 1 <= d <= 2 * t)
    S['npfree_other'] = sum(1 for d in den if d % p and not 1 <= d <= 2 * t)
    S['nposden'] = sum(1 for d in den if d > 0)
    S['edges'] = sum(c * (c - 1) // 2 for c in den.values())
    S['incid'] = sum(den.values())
    S['oddbuckets'] = sum(1 for c in den.values() if c % 2)
    S['has_seed'] = int(tuple(sorted((t, -2 * p * t, -2 * p * t))) in vs)
    S['has_2t'] = int(tuple(sorted((2 * t, 2 * t, -p * t))) in vs)
    S['one'] = 1
    return S


def main():
    data = load(sys.argv[1])
    rows = []; names = None
    for p, V in sorted(data.items()):
        for C in comps(V):
            S = comp_stats(p, V, C)
            names = names or list(S)
            rows.append([S[k] % 2 for k in names])
    A = np.array(rows, dtype=np.uint8)
    A = np.unique(A, axis=0)
    print('distinct parity rows', A.shape)
    for v in gf2_nullspace(A):
        print('relation: sum of', [names[i] for i in np.nonzero(v)[0]], '= 0 on every component')


if __name__ == '__main__':
    main()
