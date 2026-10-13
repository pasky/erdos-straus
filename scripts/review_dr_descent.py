"""R181: from-scratch check of DRINFELD_ES Prop 4.1 numerics: for 4 | M, 4 < M <= 120, enumerate all subgroups H of
G = (Z/M)^* of odd index (F' = fixed field of H has odd degree) and all index-2 subgroups H' of H (K'/F' quadratic);
check H \\ H' != {-1 mod M}.  Also Prop 4.2 identity N(b)N(b') = (1+4c^2dp)^r on random cubic-field elements is
trivial algebra and not re-tested.  Also: FF parity formula [K_M^+ : F] = (q^d-1)/(q-1) = d mod 2."""
from math import gcd

def subgroups(M):
    G = [a for a in range(1, M) if gcd(a, M) == 1]
    def close(gens):
        S = {1}; frontier = [1]
        while frontier:
            x = frontier.pop(); 
            for g in gens:
                y = x * g % M
                if y not in S: S.add(y); frontier.append(y)
        return frozenset(S)
    subs = {frozenset([1])}; frontier = [frozenset([1])]
    while frontier:
        H = frontier.pop()
        for g in G:
            if g not in H:
                K = close(list(H) + [g])
                if K not in subs: subs.add(K); frontier.append(K)
    return G, subs

total = 0; bad = 0; perM = {}
for M in range(8, 121, 4):
    G, subs = subgroups(M); phi = len(G)
    for H in subs:
        if (phi // len(H)) % 2 == 0 or len(H) % 2: continue
        for H2 in subs:
            if len(H2) * 2 == len(H) and H2 <= H:
                total += 1; perM[M] = perM.get(M, 0) + 1
                if H - H2 == {M - 1}: bad += 1
print("pairs (odd-degree F', quadratic K'/F' in Q(zeta_M)), 4|M, 8<=M<=120:", total, " with H\\H' = {-1}:", bad)
print("per M:", perM)
for q in (3, 5, 7, 9, 11, 13):
    for d in range(1, 9):
        assert ((q ** d - 1) // (q - 1)) % 2 == d % 2
print("FF parity formula ok")
