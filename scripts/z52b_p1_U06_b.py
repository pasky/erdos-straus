#!/usr/bin/env python3
"""z52b pass1 U06 — Z2944 follow-up: exact R(p) (trial form) for the 21 hard primes with S1(p)=0 (q<=2e5).
R(p) = #{(u,C) : u,C>=1, (4uC-1) | (p+u)}  (FRONTIER §2.1 trial form). Sanity: the (*)-failures in the
hard classes (2521, 5569, 9601, 66529, 83449) must give R=0."""
import json, sys
sys.argv = [sys.argv[0]]
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])  # reuse sieve/factor/divisors/cert
def R_trial(p):
    tot = 0
    for u in range(1, (p + 1) // 3 + 2):
        N = p + u
        for m in divisors(factor(N)):
            if m % (4 * u) == 4 * u - 1:
                tot += 1
    return tot
zeros = [2521, 3361, 5569, 5881, 9601, 12289, 16921, 23041, 31081, 33721, 33961, 52081, 53089, 58129, 66529, 66889, 75289, 80929, 83449, 85009, 91249]
out = {}
for p in zeros:
    out[p] = R_trial(p)
    print(p, "R(p)=", out[p], flush=True)
json.dump(out, open("data/z52b/pass1/U06/R_for_S1zero_hard.json", "w"), indent=0)
