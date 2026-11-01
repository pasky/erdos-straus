"""Brute-force check of the engine's genus count g(u) = #{d | n+u : d ∈ (-n)·(Z/u)^{×2}} (Lemma G).
Usage: Z53DBG=1 /tmp/z53fc < list | uv run --with sympy python scripts/z53_forestclass_genuscheck.py"""
import sys
from sympy import divisors
from math import gcd
bad = tot = 0
sqcache = {}
for line in sys.stdin:
    if not line.startswith("G "):
        continue
    n, u, g, phi = map(int, line.split()[1:])
    if u not in sqcache:
        sqcache[u] = {(y * y) % u for y in range(1, u + 1) if gcd(y, u) == 1}
    sq = sqcache[u]
    c = (-n) % u
    cinv = pow(c, -1, u)
    cnt = sum(1 for d in divisors(n + u) if (d * cinv) % u in sq)
    tot += 1
    if cnt != g:
        bad += 1
        if bad < 5:
            print("MISMATCH", n, u, g, cnt)
print(f"checked {tot} (n,u) pairs, mismatches {bad}")
