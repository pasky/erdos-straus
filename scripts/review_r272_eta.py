"""R272: brute-force lower bounds for the target constant eta(G), G=(Z/t)^x (CLASS_FORCING §4):
eta = sup_S min_{H<=G, -1 notin H} #{x in S : x notin H}, over multisets S with -1 notin Sigma(S).
DFS over multisets of size <= cap (pruning: -1 in Sigma(S) is inherited by supersets)."""
import sys
from math import gcd
from itertools import combinations
def run(t, cap):
    G = [x for x in range(1, t) if gcd(x, t) == 1]; m1 = t-1
    def close(gens):
        H = {1}; fr = [1]
        while fr:
            y = fr.pop()
            for g in gens:
                z = y*g % t
                if z not in H: H.add(z); fr.append(z)
        return frozenset(H)
    subs = set()
    for r in range(0, 4):
        for gens in combinations(G, r): subs.add(close(gens))
    subs = [H for H in subs if m1 not in H]
    best = [-1, None]
    def dfs(start, S, Sig):
        if S:
            v = min(sum(1 for x in S if x not in H) for H in subs)
            if v > best[0]: best[0], best[1] = v, list(S)
        if len(S) == cap: return
        for i in range(start, len(G)):
            x = G[i]; new = Sig | {y*x % t for y in Sig}
            if m1 in new: continue
            S.append(x); dfs(i, S, new); S.pop()
    dfs(0, [], frozenset({1}))
    return best
for t, cap in [(12, 8), (20, 8), (28, 8), (44, 7), (60, 6), (76, 6)]:
    q = t//4
    lem = (q-3)//2 if q % 4 == 3 else None
    b = run(t, cap)
    print(f"t={t} cap={cap}: eta >= {b[0]} (witness {b[1]}); Lemma 4.1 bound {lem}", flush=True)
