"""U04 extra checks: Z1086 (rectangle count vs independence null), Z1056 (C -> C+1 persistence of witnesses),
Z2523 (murmuration-style bins of U(p)/log^2 p by p mod 840 on existing per-prime table)."""
import json, math, numpy as np
from collections import defaultdict
PMAX, CMAX = 20000, 30
exec(open('scripts/z52b_p1_U04_witness.py').read().split("ps = [p for p")[0].split("PMAX = int")[0])  # imports only
import sys
sys.argv = ['x', str(PMAX), str(CMAX)]
src = open('scripts/z52b_p1_U04_witness.py').read()
ns = {}
exec(src.split("res = {}")[0], ns)  # builds W, ps, OM, REACH, wit_pc
W, ps = ns['W'], ns['ps']
rates = {C: sum(W[(p, C)] for p in ps) / len(ps) for C in range(1, CMAX + 1)}
# Z1086: rectangles with C1<C2 (both witnessed for p1,p2), observed vs independence null using per-C rates
obs = 0; exp_ = 0.0
Cs = range(1, CMAX + 1)
for C1 in range(1, 6):
    for C2 in range(C1 + 1, 11):
        n11 = sum(1 for p in ps if W[(p, C1)] and W[(p, C2)])
        obs += n11 * (n11 - 1) // 2
        exp_ += (len(ps) * (len(ps) - 1) / 2) * (rates[C1] * rates[C2]) ** 2
# Z1056: P(W(p,C+1)|W(p,C)) vs base rate
pers = {}
for C in range(1, CMAX):
    a = [p for p in ps if W[(p, C)]]
    pers[C] = round(sum(W[(p, C + 1)] for p in a) / max(1, len(a)), 3)
# Z2523: U(p)/log^2 p by p mod 840 from the per-prime table (cols: p,U,...)
A = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
def _isp(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))
A = A[(A[:, 0] % 4 == 1)]
A = A[np.array([_isp(int(v)) for v in A[:, 0]])]
p = A[:, 0].astype(float); y = A[:, 1] / np.log(p) ** 2
cls = defaultdict(list)
for pp, yy in zip(A[:, 0], y): cls[int(pp % 840)].append(yy)
top = sorted(((k, round(float(np.mean(v)), 3), len(v)) for k, v in cls.items() if len(v) >= 8), key=lambda t: t[1])
bins = {}
for lo, hi in [(0, 5000), (5000, 10000), (10000, 20000), (20000, 30000)]:
    m = (p >= lo) & (p < hi)
    bins[f'{lo}-{hi}'] = round(float(np.mean(y[m])), 3)
res = dict(Z1086_rect_obs=obs, Z1086_rect_indep_null=round(exp_, 1), Z1056_persistence_C_to_C1=pers,
           Z2523_bins=bins, Z2523_lowest_classes_mod840=top[:5], Z2523_highest_classes_mod840=top[-5:],
           Z2523_spread=round(top[-1][1] - top[0][1], 3))
print(json.dumps(res))
json.dump(res, open('data/z52b/pass1/U04/extra_checks.json', 'w'), indent=1)
