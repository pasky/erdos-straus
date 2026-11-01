r"""z52d PELLCYCLE: complete census of cycle-root failures.
For every prime p ≡ 1 (mod 8) in [LO, HI) (p ≡ 5 (8) is automatic: the cycle root Q_0 = 1 has the bichromatic edge {1,2}),
decide whether some component of F_p meeting R0(p) (resp. R3(p)) contains a bichromatic edge (full components, cap 1e5,
censored reported). Roots are tried in increasing order; stop at the first hit.
Output: one line per FAILURE: "p periodS periodW |R0| |R3| R0fail R3fail p%24", plus a summary line with counts.
Usage: uv run --with sympy python scripts/z52d_pellcycle_failcensus.py LO HI SHARD NSHARD OUT
"""
import math
import sys
from sympy import primerange

from z52d_pellcycle_lib import explore, root_sets

LO, HI, SH, NSH, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
f = open(OUT, "w")
n = f0 = f3 = cen = 0
i = 0
for p in primerange(LO, HI):
    if p % 8 != 1:
        continue
    i += 1
    if i % NSH != SH:
        continue
    n += 1
    rs = root_sets(p)
    memo = {}

    def hit(R):
        global cen
        for u in sorted(R):
            if u in memo:
                s = memo[u]
            else:
                s = explore(p, u, cap=100000)[0]
                memo[u] = s
            if s == "censored":
                cen += 1
            if s == "hit":
                return True
        return False

    h0 = hit(rs["R0"])
    h3 = h0 or hit(rs["R3"] - rs["R0"])
    if not h0 or not h3:
        f0 += not h0
        f3 += not h3
        f.write(f"{p} {rs['periodS']} {rs['periodW']} {len(rs['R0'])} {len(rs['R3'])} {int(not h0)} {int(not h3)} {p % 24}\n")
        f.flush()
f.write(f"# SUMMARY primes≡1(8) in [{LO},{HI}) shard {SH}/{NSH}: {n}; R0 failures {f0}; R3 failures {f3}; censored roots {cen}\n")
f.close()
