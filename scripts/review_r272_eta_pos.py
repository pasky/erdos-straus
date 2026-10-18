"""R272: is eta(G) >= 1 for every G=(Z/4d)^x of exponent > 2 (Prop 4.2's 'i.e.')?
eta>=1 iff some multiset S has -1 in <S> but -1 notin Sigma(S). Search |S|<=3."""
from math import gcd
from itertools import combinations_with_replacement as cwr
def gen(S, t):
    H = {1}; fr = [1]
    while fr:
        y = fr.pop()
        for g in S:
            z = y*g % t
            if z not in H: H.add(z); fr.append(z)
    return H
bad = []
for d in range(1, 151):
    t = 4*d; G = [x for x in range(1, t) if gcd(x, t) == 1]
    exp2 = all(x*x % t == 1 for x in G)
    ok = False
    for r in (1, 2, 3):
        for S in cwr(G, r):
            Sig = {1}
            for x in S: Sig |= {y*x % t for y in Sig}
            if t-1 not in Sig and t-1 in gen(S, t): ok = True; break
        if ok: break
    if ok == exp2: bad.append((d, exp2, ok))
print("d<=150: levels where (eta>=1) != (exp(G)>2):", bad)
