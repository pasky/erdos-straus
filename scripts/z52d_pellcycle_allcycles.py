r"""z52d PELLCYCLE: the all-cycles ("class-group") root set S(p) = {1 <= a < sqrt p : x^2 ≡ p (mod a) solvable}
(Prop 2.4(b): S(p) ⊆ Q-values of the union of all reduction cycles of discriminant 4p).
For every prime p ≡ 1 (mod 8) in [LO, HI): does some component of F_p meeting S(p) contain a bichromatic edge?
Roots tried in increasing order, stop at first hit. Prints failures and a summary.
Usage: uv run --with sympy python scripts/z52d_pellcycle_allcycles.py LO HI
"""
import math
import sys
from sympy import primerange, sqrt_mod

from z52d_pellcycle_lib import explore

LO, HI = int(sys.argv[1]), int(sys.argv[2])
n = fails = 0
maxrank = (0, 0)
for p in primerange(LO, HI):
    if p % 8 != 1:
        continue
    n += 1
    s = math.isqrt(p)
    ok = False
    rank = 0
    for a in range(1, s + 1):
        if a > 1 and sqrt_mod(p % a, a) is None:
            continue
        rank += 1
        if explore(p, a, cap=100000)[0] == "hit":
            ok = True
            break
    if not ok:
        fails += 1
        print("FAIL", p)
    elif rank > maxrank[0]:
        maxrank = (rank, p)
print(f"# SUMMARY primes≡1(8) in [{LO},{HI}): {n}; S(p)-root failures {fails}; "
      f"max number of S(p)-roots tried before the first hit: {maxrank[0]} (at p={maxrank[1]})")
