r"""z52d PELLCYCLE: at primes where R0 fails, how often does a size-matched random root set (roots < 8 kept) also fail?
Also counts the bichromatic components of F_p with tree-root (least vertex) <= sqrt(p)+1 hit by nothing.
Usage: uv run --with sympy python scripts/z52d_pellcycle_failrand.py NDRAW p1 p2 ...
"""
import random
import sys
from z52d_pellcycle_lib import explore, root_sets

ND = int(sys.argv[1])
print("| p | period | |R0| | R0 roots ≥ 8 | random sets failing (of %d) |" % ND)
print("|---:|---:|---:|---:|---:|")
for p in map(int, sys.argv[2:]):
    rs = root_sets(p)
    R = sorted(rs["R0"])
    rng = random.Random(p)
    memo = {}
    def st(u):
        if u not in memo:
            memo[u] = explore(p, u, cap=100000)[0]
        return memo[u]
    assert not any(st(u) == "hit" for u in R)
    fails = 0
    for _ in range(ND):
        ok = False
        for u in R:
            x = u if u < 8 else rng.randint(-(-4 * u // 5), (5 * u) // 4)
            if x % p and st(x) == "hit":
                ok = True
                break
        fails += not ok
    print(f"| {p} | {rs['periodS']} | {len(R)} | {sum(u >= 8 for u in R)} | {fails} |")
