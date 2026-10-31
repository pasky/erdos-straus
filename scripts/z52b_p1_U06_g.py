#!/usr/bin/env python3
"""z52b pass1 U06 — Z3146 fix: multiplicative energy of divisor classes of N=(p+e)/4 mod e, e ≡ 3 (4) (so 4 | p+e).
E(D) = #{(a,b,c,d) in D^4 : ab ≡ cd (mod e)} / |D|^4 * |D|^2 ... reported as raw count / |D|^2 for comparability; random N of same size as control."""
import json, random
from collections import Counter
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
def energy(N, e):
    cnt = Counter(d % e for d in divisors(factor(N)))
    keys = list(cnt); E = 0
    for a in keys:
        for b in keys:
            ab = a * b % e
            for c in keys:
                for d in keys:
                    if ab == c * d % e: E += cnt[a] * cnt[b] * cnt[c] * cnt[d]
    return E, sum(cnt.values())
random.seed(3)
HARD = {1, 121, 169, 289, 361, 529}
hp = [q for q in sieve(20000) if q % 4 == 1 and q % 840 in HARD][:25]
res = []
for p in hp:
    e = 7  # e = 3 mod 4 so that 4 | p+e
    N = (p + e) // 4
    E, n = energy(N, e)
    rr = [energy(random.randint(N // 2, N), e) for _ in range(5)]
    res.append((p, N, E / n ** 2, sum(x / m ** 2 for x, m in rr) / len(rr)))
mean_h = sum(r[2] for r in res) / len(res); mean_r = sum(r[3] for r in res) / len(res)
print("Z3146 hard primes:", len(res), "mean normalised energy (hard N):", round(mean_h, 3), "(random N):", round(mean_r, 3))
json.dump({"rows": res, "mean_hard": mean_h, "mean_random": mean_r}, open("data/z52b/pass1/U06/z3146_energy.json", "w"), indent=1)
