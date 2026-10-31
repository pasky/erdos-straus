#!/usr/bin/env python3
"""z52b pass1 U06 (final group 4): Z2151 — fraction of hard primes <= 2000 with a five-slice A (CF length <= 3) whose quotients are all <= M."""
import json
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
def cfq(a, b):
    q = []
    while b: q.append(a // b); a, b = b, a % b
    return q
HARD = {1,121,169,289,361,529}
hp = [q for q in sieve(2000) if q % 4 == 1 and q % 840 in HARD]
out = {}
for M in (5, 10, 20, 50):
    cov = 0
    for p in hp:
        if any(len(cfq(p, A)) <= 3 and max(cfq(p, A)) <= M for A in range(1, p)): cov += 1
    out[M] = round(cov / len(hp), 3)
out["n_hard"] = len(hp)
json.dump(out, open("data/z52b/pass1/U06/final_o.json", "w"))
print(out)
