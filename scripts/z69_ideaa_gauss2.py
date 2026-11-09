#!/usr/bin/env python3
"""z69 IDEAA T3 follow-up (post hoc, NOT pre-registered): is the 1.46x enrichment of the Gaussian slice a
divisor-count (local density) effect?  Compare mean tau(M^2), 2-adic valuation of M, and the success rate
normalised by the naive expected number of hitting divisors (tau(M^2)-2)/phi(e), Gaussian vs control slices."""
import sys, math, random
sys.argv = [sys.argv[0], "3000000", "0"]
import importlib.util
spec = importlib.util.spec_from_file_location("g", "scripts/z69_ideaa_gauss.py")
src = open("scripts/z69_ideaa_gauss.py").read().split("ps = [p for p in primes_upto(X)")[0]
exec(src)
random.seed(691)
def phi(n):
    r = n
    for q in factor(n): r = r // q * (q - 1)
    return r
def stats(p, e):
    M = (p + e) // 4; f = factor(M)
    t = 1
    for k in f.values(): t *= 2 * k + 1
    return t, f.get(2, 0), (t - 2) / phi(e)
ps = [p for p in primes_upto(X) if p % 24 == 1 and p > 1000]
sample = random.sample(ps, 8000)
G = [0, 0, 0.0, 0.0, 0]; C = [0, 0, 0.0, 0.0, 0]   # n, ok, sum tau, sum expected, #(4|M)
for p in sample:
    a, b = two_squares(p); e = 2 * a + 1
    t, v2, ex = stats(p, e); G[0] += 1; G[1] += bool(slice_ok(p, e)); G[2] += t; G[3] += ex; G[4] += (v2 >= 2)
    for k in (1, 2, 3):
        for s in (1, -1):
            e2 = e + 4 * k * s
            if e2 < 3 or math.gcd(e2, p) != 1: continue
            t, v2, ex = stats(p, e2); C[0] += 1; C[1] += bool(slice_ok(p, e2)); C[2] += t; C[3] += ex; C[4] += (v2 >= 2)
for nm, S in (("gauss", G), ("control", C)):
    print(f"{nm:8s} n={S[0]} success={S[1]/S[0]:.4f} mean tau(M^2)={S[2]/S[0]:.2f} mean naive expectation={S[3]/S[0]:.4f} "
          f"success/expectation={S[1]/S[3]:.3f} P(4|M)={S[4]/S[0]:.3f}")
print(f"ratio of success rates {(G[1]/G[0])/(C[1]/C[0]):.3f}; ratio of mean tau(M^2) {(G[2]/G[0])/(C[2]/C[0]):.3f}; "
      f"ratio of naive expectations {(G[3]/G[0])/(C[3]/C[0]):.3f}")
