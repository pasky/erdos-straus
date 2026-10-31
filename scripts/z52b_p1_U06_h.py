#!/usr/bin/env python3
"""z52b pass1 U06 — Z2001 cap sweep at k=4 (primes ≡ 1 (24) in [10^4, 2·10^4)): greedy menu size for u-caps 100/400/1500."""
import json
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
def menu_items(p, Umax):
    out = []
    for u in range(1, Umax + 1):
        for m in divisors(factor(p + u)):
            if m % (4 * u) == 4 * u - 1: out.append((u, (m + 1) // (4 * u)))
    return out
primes = [q for q in sieve(20000) if q >= 10000 and q % 24 == 1]
res = {}
for cap in (100, 400, 1500):
    cover = {}
    for p in primes:
        for it in set(menu_items(p, cap)): cover.setdefault(it, set()).add(p)
    left = set(primes); k = 0
    while left:
        best = max(cover.items(), key=lambda kv: len(kv[1] & left))
        g = best[1] & left
        if not g: break
        left -= g; k += 1
    res[cap] = (k, len(left))
print("primes", len(primes), "menu size / uncovered by u-cap:", res)
json.dump({"n_primes": len(primes), "by_cap": {str(c): v for c, v in res.items()}}, open("data/z52b/pass1/U06/z2001_capsweep_k4.json", "w"))
