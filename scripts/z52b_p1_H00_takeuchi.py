"""Z0168 pass-1: reconstruct Takeuchi's list of arithmetic hyperbolic triangle groups Δ(a,b,c) (a ≤ b ≤ c ≤ 60 or ∞)
via Takeuchi's criterion: for every Galois conjugation σ (cos(π/m) ↦ cos(πj/m), j ∈ (Z/2L)^*) that is non-trivial on
K = Q(cos²(π/a), cos²(π/b), cos²(π/c), cos(π/a)cos(π/b)cos(π/c)), σ(λ) < 0 where
λ = cos²(π/a) + cos²(π/b) + cos²(π/c) + 2cos(π/a)cos(π/b)cos(π/c) − 1 (= −det Gram; λ > 0 ⇔ hyperbolic). Sanity: expect 85 groups (76 cocompact).
Then list triples with 1/a + 1/b + 1/c = 4/n (n integer; ∞ entries contribute 0)."""
import json
from math import cos, pi, gcd
from fractions import Fraction as F
INF = 0
def lcm(a, b): return a*b//gcd(a, b)
def arithmetic(t):
    L = 1
    for m in t:
        if m: L = lcm(L, m)
    M = 2*L
    def vals(j):
        cs = [1.0 if m == 0 else cos(pi*j/m) for m in t]
        return [cs[0]**2, cs[1]**2, cs[2]**2, cs[0]*cs[1]*cs[2]]
    base = vals(1)
    lam = lambda v: v[0] + v[1] + v[2] + 2*v[3] - 1
    if lam(base) <= 0: return False          # not hyperbolic
    for j in range(1, M):
        if gcd(j, M) != 1: continue
        v = vals(j)
        if all(abs(x - y) < 1e-9 for x, y in zip(v, base)): continue
        if lam(v) >= -1e-12: return False
    return True
ms = list(range(2, 61)) + [INF]
key = lambda m: 10**9 if m == 0 else m
res = []
for a in ms:
    for b in ms:
        for c in ms:
            if not (key(a) <= key(b) <= key(c)): continue
            s = sum(F(1, m) for m in (a, b, c) if m)
            if (a and b and c) and s >= 1: continue
            if arithmetic((a, b, c)): res.append((a, b, c))
print('arithmetic triangle groups found:', len(res), ' cocompact:', sum(1 for t in res if INF not in t))
es = []
for t in res:
    s = sum(F(1, m) for m in t if m)
    if s > 0 and (4/s).denominator == 1: es.append((t, int(4/s)))
print('ES triples (1/a+1/b+1/c = 4/n):', es)
json.dump(dict(groups=[['inf' if m == 0 else m for m in t] for t in res], es=[(['inf' if m == 0 else m for m in t], n) for t, n in es]),
          open('data/z52b/pass1/H00/takeuchi.json', 'w'))
