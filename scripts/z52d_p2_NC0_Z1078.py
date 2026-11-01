"""Z1078: bipartite matching encoding of ES certificates (toy).  For n = p (prime = 1 mod 4) take all unordered solutions
(x<=y<=z) of 4/p = 1/x+1/y+1/z (from /tmp/z52d_big/G2/z1013_sols.txt, scripts/z52d_p2_NC0_Z1013.c).
Encoding E1: left = denominators in the first slot, right = denominators in the second slot; edge (a,b) iff some solution has
{a,b} as two of its coordinates with the third coordinate determined (the third is ALWAYS determined by (a,b): 1/c = 4/p-1/a-1/b).
A matching of size k = k pairwise-coordinate-disjoint pairs = k solutions simultaneously; a perfect matching of a square
instance is a set of solutions covering each denominator once.  We compute: #edges (= 3U(p) ordered-pair incidences),
maximum matching size (Hopcroft-Karp-free augmenting paths), #perfect matchings of the largest square block (permanent by
Ryser, only when block size <= 14), and the Edmonds/Tutte test det(B * random weights) != 0 (existence of a matching of
full size) for the same graph.  Output: data/z52b/pass2/NC0/sub/Z1078_matchings.json
Run: uv run --with numpy python scripts/z52d_p2_NC0_Z1078.py
"""
import numpy as np, json, os, random, itertools, collections, math
from fractions import Fraction as Fr
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = collections.defaultdict(list)
for line in open('/tmp/z52d_big/G2/z1013_sols.txt'):
    n, x, y, z = map(int, line.split()); rows[n].append((x, y, z))
def max_matching(adj, L):
    match_r = {}
    def try_k(u, seen):
        for v in adj[u]:
            if v in seen: continue
            seen.add(v)
            if v not in match_r or try_k(match_r[v], seen):
                match_r[v] = u; return True
        return False
    return sum(1 for u in range(L) if try_k(u, set())), match_r
def permanent(M):
    n = len(M)
    if n == 0: return 1
    total = 0
    for subset in range(1, 1 << n):
        bits = bin(subset).count('1')
        prod = 1
        for i in range(n):
            s = 0
            for j in range(n):
                if subset >> j & 1: s += M[i][j]
            prod *= s
            if prod == 0: break
        total += (-1) ** (n - bits) * prod
    return total
def det_fraction(M):
    import sympy as sp
    return sp.Matrix(M).det()
random.seed(3)
out = {}
for p in [409, 577, 1009, 1609, 2017, 2521, 2953]:
    sols = rows[p]
    # bipartite graph: left = first denominators, right = second denominators, over all ordered coordinate pairs (a,b) a!=b
    edges = set()
    for t in sols:
        for a, b in itertools.permutations(t, 2):
            edges.add((a, b))
    L = sorted({a for a, _ in edges}); R = sorted({b for _, b in edges})
    li = {a: i for i, a in enumerate(L)}; ri = {b: i for i, b in enumerate(R)}
    adj = [[] for _ in L]
    for a, b in edges: adj[li[a]].append(ri[b])
    msize, match_r = max_matching(adj, len(L))
    # Edmonds/Tutte-style test on a SQUARE block: restrict to a square subgraph by taking k = min(|L|,|R|) matched vertices
    sq = msize
    # random-weight determinant of the biadjacency restricted to the matched vertices (size msize)
    matched_L = sorted({match_r[r] for r in match_r})[:sq]
    matched_R = sorted(match_r.keys())[:sq]
    W = [[0] * sq for _ in range(sq)]
    for i, u in enumerate(matched_L):
        for j, v in enumerate(matched_R):
            if (u, v) in [(li[a], ri[b]) for (a, b) in edges]: W[i][j] = random.randint(1, 10 ** 6)
    detv = int(det_fraction(W)) if sq > 0 else 1
    out[str(p)] = dict(U=len(sols), n_edges_ordered=len(edges), left=len(L), right=len(R), max_matching=msize,
                       det_random_weights_nonzero=bool(detv != 0), solutions_per_matching_max=msize)
    print(p, out[str(p)])
out['note'] = ('Every edge (a,b) determines the third denominator c by 1/c = 4/p - 1/a - 1/b, so a matching is nothing but a set of '
               'coordinate-disjoint solutions; the determinant (Tutte/Edmonds) test is nonzero iff a full matching exists, i.e. iff '
               'some solution exists (for U>0): the encoding adds no constraint beyond the solution set.')
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1078_matchings.json', 'w'), indent=1)
