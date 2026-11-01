"""Pass-2 SK2 Z1311: valuation distribution of u among local solutions of F(u,B,C)=4uBC-u-B = a (mod q^k).
Solutions mod q^k with v_q(u) in {0,1,...,k} (u=0 mod q^k counted as k). Proportions per a-class.
Also verifies the closed form N_1(a) = q^2 + 1 - q*[a==0] (mod q) used in Z1310 (proof: case split on uB mod q).
Memory: q^(3k) loops; q=3,k=3 -> 19683; q=5,k=2 -> 15625; q=7,k=2 -> 117649; fine.
"""
import json
from collections import Counter, defaultdict
out = {}
for q, k in [(3, 2), (3, 3), (5, 2), (7, 2)]:
    m = q ** k
    byval = defaultdict(Counter)   # a -> Counter of v_q(u) (capped at k)
    tot = Counter()
    for u in range(m):
        vu = k if u == 0 else next(j for j in range(k) if u % (q ** (j + 1)) != 0) if False else None
        if u == 0: vu = k
        else:
            vu = 0; x = u
            while x % q == 0: x //= q; vu += 1
        for B in range(m):
            for C in range(m):
                a = (4 * u * B * C - u - B) % m
                byval[a][vu] += 1
    res = {}
    for a in [1, 2] if q == 3 else [1, 2]:
        tot_a = sum(byval[a].values())
        res[str(a)] = {str(j): round(byval[a][j] / tot_a, 5) for j in range(k + 1)}
    out[f"q={q},k={k}"] = {"proportion_v_q(u)_by_a": res,
                          "note": "classes a with q | a not shown; uniform-in-u prediction is (1-1/q)q^-j style"}
# closed form check N_1(a) = q^2 + 1 - q[a==0] for several primes
chk = {}
for q in [3, 5, 7, 11, 13]:
    cnt = Counter()
    for u in range(q):
        for B in range(q):
            for C in range(q):
                cnt[(4 * u * B * C - u - B) % q] += 1
    chk[str(q)] = all(cnt[a] == (q * q + 1 - (q if a == 0 else 0)) for a in range(q))
out["closed_form_N1_ok"] = chk
json.dump(out, open("data/z52b/pass2/SK2/valuation_checks.json", "w"), indent=1)
print(json.dumps(out, indent=1))
