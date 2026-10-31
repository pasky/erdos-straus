#!/usr/bin/env python3
"""z52b pass1 U06 — Z2972 fixed: do convergent denominators q_k of sqrt(p) reduced mod p hit a five-slice residue A with A > sqrt(p)
(excludes trivial small A whose CF length is <= 3 automatically)? Compare with chance rate |S5 ∩ (sqrt p, p)|/p."""
import json, math
exec(open("scripts/z52b_p1_U06_i.py").read().split("# ---- Z1462")[0])
hit = 0; chance = 0.0; n = 0
for p in PR[:150]:
    big = {A for A, q in S5[p] if A > math.isqrt(p)}
    a0 = math.isqrt(p); m, d, a = 0, 1, a0
    k0, k1 = 0, 1
    found = False
    for _ in range(40):
        m = d * a - m; d = (p - m * m) // d; a = (a0 + m) // d
        k0, k1 = k1, a * k1 + k0
        if k1 % p in big: found = True; break
    hit += found; chance += 1 - (1 - len(big) / p) ** 40; n += 1
json.dump({"n": n, "hits": hit, "expected_by_chance": round(chance, 2)}, open("data/z52b/pass1/U06/z2972_convergent_fiveslice.json", "w"))
print("Z2972 hits", hit, "of", n, "chance~", round(chance, 1))
