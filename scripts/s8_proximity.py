"""O258 s8_profinite_proximity: do primes p with a large 11-smooth part of p - 1 (profinitely close to the T1 point 1)
have fewer b=1 / c=1 line solutions?  Usage: PYTHONPATH=scripts uv run python scripts/s8_proximity.py P0 P1"""
import sys
from s8_check_b1 import line_counts_k
def isp(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
def smooth_part(n, B=11):
    s = 1
    for q in (2, 3, 5, 7, 11):
        while n % q == 0: n //= q; s *= q
    return s
P0, P1 = int(sys.argv[1]), int(sys.argv[2])
bins = {}
for p in range(P0 + (1 - P0) % 4, P1, 4):
    if not isp(p): continue
    S = smooth_part(p - 1); key = 0 if S < 50 else (1 if S < 500 else 2)
    b, c = line_counts_k(p, 4)
    bins.setdefault(key, []).append((b, c))
for key, lab in ((0, "S<50"), (1, "50<=S<500"), (2, "S>=500")):
    v = bins.get(key, [])
    if v: print(f"{lab:10s} n={len(v):4d}  mean b1={sum(x for x,_ in v)/len(v):.2f}  mean c1={sum(y for _,y in v)/len(v):.2f}  min b1={min(x for x,_ in v)} min c1={min(y for _,y in v)}")
