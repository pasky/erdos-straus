"""Parity statistics of global structures of the complete signed ES graph.

Input: output of windmill_signed.cpp.  For each p computes global counts
(vertices, positive vertices, components, seed component data, degrees...)
and prints the fraction of primes where each count is odd.
"""
from __future__ import annotations
import sys
from collections import defaultdict, Counter


def load(path):
    data = {}; p = None
    for line in open(path):
        if line.startswith('P'):
            p = int(line.split()[1]); data[p] = []
        else:
            data[p].append(tuple(map(int, line.split())))
    return data


def comps(V):
    par = list(range(len(V)))
    def f(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    first = {}
    for i, v in enumerate(V):
        for d in set(v):
            if d in first:
                a, b = f(i), f(first[d])
                if a != b: par[a] = b
            else:
                first[d] = i
    C = defaultdict(list)
    for i in range(len(V)):
        C[f(i)].append(i)
    return list(C.values())


def stats(p, V):
    t = (p - 1) // 4
    seed = tuple(sorted((t, -2 * p * t, -2 * p * t)))
    S = {}
    pos = [v[0] > 0 for v in V]
    typ = [sum(1 for d in v if d % p == 0) for v in V]
    S['V'] = len(V); S['Vpos'] = sum(pos)
    S['VposI'] = sum(1 for i in range(len(V)) if pos[i] and typ[i] == 1)
    S['VI'] = sum(1 for x in typ if x == 1)
    nneg = [sum(1 for d in v if d < 0) for v in V]
    for k in range(3):
        S[f'neg{k}'] = sum(1 for x in nneg if x == k)
        for T in (1, 2):
            S[f'neg{k}T{T}'] = sum(1 for i in range(len(V)) if nneg[i] == k and typ[i] == T)
    CC = comps(V)
    S['ncomp'] = len(CC)
    idx = {v: i for i, v in enumerate(V)}
    si = idx[seed]
    for C in CC:
        if si in C:
            S['seedsize'] = len(C); S['seedpos'] = sum(pos[i] for i in C)
            S['seedposI'] = sum(pos[i] and typ[i] == 1 for i in C)
            S['seedT1'] = sum(typ[i] == 1 for i in C)
    S['posfree_comps'] = sum(1 for C in CC if any(pos[i] for i in C))
    S['sterile'] = sum(1 for C in CC if not any(pos[i] for i in C))
    S['allpos_comps'] = sum(1 for C in CC if all(pos[i] for i in C))
    S['oddcomps'] = sum(1 for C in CC if len(C) % 2)
    deg = Counter()
    for v in V:
        for d in set(v): deg[d] += 1
    S['ndenoms'] = len(deg)
    S['nposdenoms'] = sum(1 for d in deg if d > 0)
    S['edges'] = sum(c * (c - 1) // 2 for c in deg.values())
    S['odd_buckets'] = sum(1 for c in deg.values() if c % 2)
    S['pos_buckets_odd'] = sum(1 for d, c in deg.items() if c % 2 and d > 0)
    # positive vertices' positive-graph components
    P = [V[i] for i in range(len(V)) if pos[i]]
    S['poscomps'] = len(comps(P)) if P else 0
    return S


def main():
    data = load(sys.argv[1])
    rows = {p: stats(p, V) for p, V in data.items()}
    keys = list(next(iter(rows.values())).keys())
    n = len(rows)
    for k in keys:
        odd = sum(r[k] % 2 for r in rows.values())
        m4 = Counter(r[k] % 4 for r in rows.values())
        print(f'{k:16s} odd {odd}/{n}  mod4 {dict(sorted(m4.items()))}')


if __name__ == '__main__':
    main()
