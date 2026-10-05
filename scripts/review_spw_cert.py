"""R40 from-scratch local certificate on Z/e (Lemma 3.1 / §3 of EXCEPTIONAL_SPW).
Primal: rho >= 0 on Z/e, class sums mod every d|e, d<=D equal c(b,d), and
rho(s) <= 1 - sigma on all classes mod e'|e with e' > C N.  max sigma.
Dual certificate: g = sum a_{d,b} 1_{b mod d} (d|e, d<=D), z_{e',s} >= 0 with
sum_s z 1_s >= g pointwise; then for any SPW R: sum_{n<=N} g(n) <= (1-sigma) sum z.
Usage: review_spw_cert.py N C e [maxden]"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

N = int(sys.argv[1]); C = Fr(sys.argv[2]); e = int(sys.argv[3])
maxden = int(sys.argv[4]) if len(sys.argv) > 4 else 10**6
D = N // 2
assert e > C * N
small = [d for d in range(1, D + 1) if e % d == 0]
big = [d for d in range(1, e + 1) if e % d == 0 and d > C * N]
W = np.zeros(e); W[[n % e for n in range(1, N + 1)]] = 1
cnt = lambda b, d: sum(1 for n in range(1, N + 1) if n % d == b)

# dual LP: vars a_{d,b} (free), z_{e',s} >= 0.  max sum_W g  s.t. sum z = 1,
# g(x) - sum_{e'} z_{e', x mod e'} <= 0 for all x.
A_idx = [(d, b) for d in small for b in range(d)]
Z_idx = [(d, s) for d in big for s in range(d)]
na, nz = len(A_idx), len(Z_idx)
obj = np.zeros(na + nz)
for i, (d, b) in enumerate(A_idx):
    obj[i] = -cnt(b, d)
Aub = lil_matrix((e, na + nz))
for x in range(e):
    for i, (d, b) in enumerate(A_idx):
        if x % d == b:
            Aub[x, i] = 1
    for j, (d, s) in enumerate(Z_idx):
        if x % d == s:
            Aub[x, na + j] = -1
Aeq = np.zeros((1, na + nz)); Aeq[0, na:] = 1
bounds = [(-50, 50)] * na + [(0, None)] * nz
res = linprog(obj, A_ub=Aub.tocsr(), b_ub=np.zeros(e), A_eq=Aeq, b_eq=[1],
              bounds=bounds, method="highs")
assert res.status == 0, res.message
print(f"N={N} C={C} e={e} D={D} #small={len(small)} big={big}  LP sigma <= {1 + res.fun:.6f}")

# exact rounding and verification
a = [Fr(v).limit_denominator(maxden) for v in res.x[:na]]
g = [Fr(0)] * e
for (d, b), ai in zip(A_idx, a):
    if ai:
        for x in range(b, e, d):
            g[x] += ai
lhs = sum(g[n % e] for n in range(1, N + 1))
# optimal z for fixed g: if only e itself is big, z = g^+; otherwise use LP z rounded up and patched
if big == [e]:
    Zsum = sum(max(v, Fr(0)) for v in g)
else:
    z = {k: max(Fr(v).limit_denominator(maxden), Fr(0)) for k, v in zip(Z_idx, res.x[na:])}
    cover = [sum(z[(d, x % d)] for d in big if d != e) for x in range(e)]
    for x in range(e):  # patch with point classes (mod e) so the cover is exact
        z[(e, x)] = max(z[(e, x)], g[x] - (cover[x]))
    for x in range(e):
        assert sum(z[(d, x % d)] for d in big) >= g[x]
    Zsum = sum(z.values())
assert Zsum > 0 and lhs > 0
bound = 1 - lhs / Zsum
import math
up = math.ceil(bound * 10**9) / 10**9
txt = str(bound) if bound.denominator < 10**12 else f"<rational, {len(str(bound.denominator))}-digit denominator>"
print(f"exact certificate: sigma <= {txt} <= {up:.9f} (rounded up)")
