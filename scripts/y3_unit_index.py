"""O211 §6: index of the reduced fundamental unit of K = Q(sqrt 2) (m = 8) in F_h^*, h = 7 mod 8 prime (h splits in K
and is inert in Q(zeta_8)/K, i.e. h = -1 mod 8).  Reports the distribution of [F_h^* : <rho(1+sqrt2)>] and the share
of h for which the unit-twisted Type II firing set on the slice cd = 2 is all of F_h^* (index 1).
Usage: PYTHONPATH=scripts uv run python scripts/y3_unit_index.py H"""
import sys
from sympy import primerange, sqrt_mod, n_order
H = int(sys.argv[1]); dist = {}; n = 0
for h in primerange(7, H):
    if h % 8 != 7: continue
    r = sqrt_mod(2, h); idx = (h - 1)//n_order((1 + r) % h, h); n += 1
    dist[idx] = dist.get(idx, 0) + 1
print(f"h=7 mod 8 < {H}: n={n}; index distribution (top): {sorted(dist.items(), key=lambda x: -x[1])[:8]}")
