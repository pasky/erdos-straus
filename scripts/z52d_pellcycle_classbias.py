r"""z52d PELLCYCLE: are principal-cycle Q-values over- or under-represented among vertices of bichromatic components?
For NP seeded random primes p ≡ 1 (mod 8) in [LO, HI): enumerate all edges of F_p (children of u <= sqrt(p)+2), the components
(union-find), and the set B(p) of vertices u <= sqrt p lying in a bichromatic component. With S(p) = split a <= sqrt p
(p □ mod a) and Q0(p) = Q-values of the sqrt(p) cycle, report
   cov   = |Q0 ∩ S| / |S|                 (coverage of split vertices by the cycle)
   obs   = |Q0 ∩ S ∩ B|,  exp = cov·|S ∩ B| (expected if cycle membership were independent of bichromaticity)
and the same restricted to vertices of monochromatic non-trivial components (M).
Usage: uv run --with sympy python scripts/z52d_pellcycle_classbias.py LO HI NP SEED
"""
import math
import random
import sys
from sympy import isprime, sqrt_mod

from z52d_pellcycle_lib import children, chi, cycle_data

LO, HI, NP, SEED = map(int, sys.argv[1:5])
rng = random.Random(SEED)
ps = []
while len(ps) < NP:
    x = rng.randrange(LO, HI)
    x -= (x - 1) % 8
    if isprime(x) and x not in ps:
        ps.append(x)
tot = dict(obsB=0, expB=0.0, nSB=0, obsM=0, expM=0.0, nSM=0)
lowc = dict(obsB=0, expB=0.0)
for p in ps:
    s = math.isqrt(p)
    par = {}

    def f(x):
        while par.get(x, x) != x:
            par[x] = par.get(par[x], par[x])
            x = par[x]
        return x
    edges = []
    for u in range(1, s + 3):
        for v in children(p, u):
            edges.append((u, v))
            a, b = f(u), f(v)
            if a != b:
                par[a] = b
    comps = {}
    for u, v in edges:
        comps.setdefault(f(u), set()).update((u, v))
    B, M = set(), set()
    for c in comps.values():
        (B if len({chi(p, x) for x in c}) > 1 else M).update(x for x in c if x <= s)
    S = {a for a in range(1, s + 1) if a == 1 or sqrt_mod(p % a, a) is not None}
    Q0 = {q for _, q, _ in cycle_data(p)["S"]["cyc"]} | {1}
    cov = len(Q0 & S) / len(S)
    SB, SM = S & B, S & M
    tot["obsB"] += len(Q0 & SB); tot["expB"] += cov * len(SB); tot["nSB"] += len(SB)
    tot["obsM"] += len(Q0 & SM); tot["expM"] += cov * len(SM); tot["nSM"] += len(SM)
    if cov < 0.4:
        lowc["obsB"] += len(Q0 & SB); lowc["expB"] += cov * len(SB)
print(f"{NP} primes ≡ 1 (8) in [{LO},{HI}) seed {SEED}")
print(f"split vertices in bichromatic components: {tot['nSB']}; in the sqrt(p) cycle: observed {tot['obsB']}, "
      f"expected {tot['expB']:.1f} (ratio {tot['obsB'] / tot['expB']:.3f})")
print(f"split vertices in monochromatic non-trivial components: {tot['nSM']}; in the cycle: observed {tot['obsM']}, "
      f"expected {tot['expM']:.1f} (ratio {tot['obsM'] / max(tot['expM'], 1e-9):.3f})")
print(f"primes with coverage < 0.4 (several cycles): bichromatic split vertices in cycle observed {lowc['obsB']}, "
      f"expected {lowc['expB']:.1f}")
