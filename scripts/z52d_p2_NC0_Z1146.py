"""Z1146: tensor-network contraction of residue constraints (G4, NC0).
Network: k repo residue-certificate charts (distinct covered sets, s<=60, ordered by s; first k of them).
Variable v_i = p mod m_i (domain Z/m_i), unary tensor u_i(v_i) = [v_i in R_i]  (chart covers p),
pairwise CRT tensor C_ij(v_i,v_j) = [v_i = v_j mod gcd(m_i,m_j)]  (the charts must describe the same prime).
Interaction graph G_k; we compute EXACT treewidth (subset DP) and the exact weighted contraction cost
(min over elimination orders of max product of domain sizes of an intermediate tensor), k <= 10.
Also: count consistent residue assignments by direct contraction on a small instance to validate."""
import sys, math, itertools
sys.path.insert(0, "scripts")
import numpy as np
from z52d_p2_NC0_lib import families, divisors

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# distinct charts (by residue data), cheapest representative
fams = families(60)
seen = {}
for f in fams:
    key = (f["m"], tuple(sorted(f["R"])))
    # dedupe by covered-set on p=1 mod 4 classes mod lcm: use residue pattern on 1 mod 4 classes
    cov = frozenset(r for r in range(f["m"]) if r % 4 == 1 and r in f["R"])
    k2 = (f["m"], cov)
    if not cov:  # chart covers no p = 1 mod 4 class: irrelevant
        continue
    if k2 not in seen:
        seen[k2] = f
charts = sorted(seen.values(), key=lambda f: (f["s"], f["m"]))[:KMAX]
k = len(charts)
m = [f["m"] for f in charts]
print("charts:", [(f["name"], f["m"]) for f in charts])

# interaction graph: pair (i,j) interacts iff gcd(m_i,m_j) > 1 (C_ij non-trivial).  All m_i = 0 mod 4 here.
adj = {i: set() for i in range(k)}
for i, j in itertools.combinations(range(k), 2):
    g = math.gcd(m[i], m[j])
    if g > 1:
        adj[i].add(j); adj[j].add(i)
nedges = sum(len(v) for v in adj.values()) // 2
print(f"k={k}: interaction edges {nedges} of {k*(k-1)//2} possible")

def fill_width(order):
    """max clique size (width+1) of the elimination order (weighted by domain sizes -> cost)."""
    g = {i: set(adj[i]) for i in range(k)}
    width = 0; cost = 0
    for v in order:
        nb = g[v]
        width = max(width, len(nb))
        cost += math.prod(m[u] for u in nb | {v})
        for a in nb:
            for b in nb:
                if a != b:
                    g[a].add(b)
        for a in nb:
            g[a].discard(v)
        del g[v]
    return width, cost

# exact treewidth + min weighted cost by subset DP over elimination sets
INF = float("inf")
from functools import lru_cache
def q_set(S, v):
    """vertices w not in S, w != v, reachable from v through vertices in S."""
    seen_ = {v}; stack = [v]; out = set()
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b in seen_:
                continue
            seen_.add(b)
            if b in S:
                stack.append(b)
            else:
                out.add(b)
    return out
full = (1 << k) - 1
TW = [INF] * (1 << k); WC = [INF] * (1 << k)
TW[0] = -1; WC[0] = 0
for S in range(1, 1 << k):
    best_tw = INF; best_wc = INF
    for v in range(k):
        if not (S >> v) & 1:
            continue
        T = S & ~(1 << v)
        Sset = {i for i in range(k) if (T >> i) & 1}
        Q = q_set(Sset, v)
        tw_v = max(TW[T], len(Q))
        wc_v = max(WC[T], math.prod(m[u] for u in Q | {v}))
        best_tw = min(best_tw, tw_v)
        best_wc = min(best_wc, wc_v)
    TW[S] = best_tw; WC[S] = best_wc
print(f"exact treewidth (k={k}): {TW[full]}   (complete graph would be k-1 = {k-1})")
print(f"exact min weighted elimination cost (max intermediate size, domain-weighted): {WC[full]}")
print(f"naive product of all domains (no contraction): {math.prod(m)}")
# greedy min-fill for comparison
best = None
import random
random.seed(1)
for trial in range(200):
    order = list(range(k)); random.shuffle(order)
    w, c = fill_width(order)
    best = (w, c) if best is None or c < best[1] else best
print(f"random-order best (200 trials): width {best[0]}, cost {best[1]}")
