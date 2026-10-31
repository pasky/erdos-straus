"""z52b pass1 U05 follow-up: (Z1521) does the d∈{1,2,3} Type I failure set stabilise as c grows? primes p≡1(4), p≤2e4
failing for c≤30 are re-tested for c∈(30,120]; (Z1943) near-miss gap distribution (fixed None handling)."""
import math, sys
from collections import Counter
sys.argv = sys.argv
exec(open("scripts/z52b_p1_U05_typeI.py").read().split("TI = {}")[0])   # reuse helpers (factoring, divisors, typeI_ok)
fails30 = [p for p in primes if not any(typeI_ok(p, c, d) for c in range(1, 31) for d in (1, 2, 3))]
log(f"Z1521 re-test: {len(fails30)} primes fail for c≤30, d∈{{1,2,3}}")
rescued = {}
for p in fails30:
    for c in range(31, 121):
        if any(typeI_ok(p, c, d) for d in (1, 2, 3)):
            rescued[p] = c; break
log(f"  rescued by some c∈(30,120]: {len(rescued)} of {len(fails30)}; still failing up to c=120: {len(fails30)-len(rescued)}")
log("  first rescues (p,c):", sorted(rescued.items(), key=lambda t: t[1])[:10])
# Z1943 near-miss gap, p≡1(4) ≤400, x,y ≤ 12p

def near_gap(p, B=12):
    """min over x≤B·p, y≥x of 4/p-1/x-1/y - 1/z, z = ceil(1/r) (greedy last term); None if no positive r."""
    best = None
    for x in range(math.ceil(p/4), B*p + 1):
        r1 = 4*x - p
        if r1 <= 0: continue
        y0 = x
        for y in range(y0, B*p + 1):
            num = r1*y - p*x
            if num <= 0: continue
            z = -(-p*x*y // num)
            gap = num/(p*x*y) - 1/z
            if best is None or gap < best: best = gap
            if y > 4*x: break
    return best
gs = {p: near_gap(p, 8) for p in primes if p <= 400}
gs = {p: g for p, g in gs.items() if g is not None}
log("Z1943 min positive near-miss gap (x≤8p, y≤8p, greedy 3rd term) for p≡1(4)≤400, 8 smallest:",
    [(p, round(g, 8)) for p, g in sorted(gs.items(), key=lambda t: t[1])[:8]])
log("  gap·p^2 quantiles (hard primes 409,577,5569 vs median):", {q: round(gs[q]*q*q, 4) for q in (409,577,5569) if q in gs},
    "median", round(sorted(g*p*p for p, g in gs.items())[len(gs)//2], 4))
open("data/z52b/pass1/U05/2nd/typeI2_out.txt","w").write("\n".join(out)+"\n")
