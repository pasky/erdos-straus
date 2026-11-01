r"""z52d PELLCYCLE: failure census for size-matched RANDOM root sets (control for z52d_pellcycle_failcensus.py).
For every prime p ≡ 1 (mod 8) in [LO, HI): take R0(p) (resp. R3(p)), keep roots < 8, replace each root u >= 8 by one
uniform draw from [ceil(0.8u), floor(1.25u)] (rng seeded by p), and decide whether some component meeting the random set
contains a bichromatic edge. Prints the summary counts to compare with the cycle failure census on the same range.
Usage: uv run --with sympy python scripts/z52d_pellcycle_randfail.py LO HI OUT
"""
import random
import sys
from sympy import primerange

from z52d_pellcycle_lib import explore, root_sets

LO, HI, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
f = open(OUT, "w")
n = f0 = f3 = 0
for p in primerange(LO, HI):
    if p % 8 != 1:
        continue
    n += 1
    rng = random.Random(7919 * p + 3)
    rs = root_sets(p)
    memo = {}

    def rand_set(R):
        out = set()
        for u in sorted(R):
            if u < 8:
                out.add(u)
            else:
                lo, hi = -(-4 * u // 5), (5 * u) // 4
                x = rng.randint(lo, hi)
                if x % p:
                    out.add(x)
        return out

    def hit(S):
        for u in sorted(S):
            if u not in memo:
                memo[u] = explore(p, u, cap=100000)[0]
            if memo[u] == "hit":
                return True
        return False

    h0 = hit(rand_set(rs["R0"]))
    h3 = hit(rand_set(rs["R3"]))
    if not (h0 and h3):
        f0 += not h0
        f3 += not h3
        f.write(f"{p} {rs['periodS']} {len(rs['R0'])} {len(rs['R3'])} {int(not h0)} {int(not h3)}\n")
f.write(f"# SUMMARY primes≡1(8) in [{LO},{HI}): {n}; random-R0 failures {f0}; random-R3 failures {f3}\n")
f.close()
