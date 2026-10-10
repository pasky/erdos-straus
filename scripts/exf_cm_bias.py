"""O131b (4): class bias of Type I ideals (fixed d) vs p-range; and vs the 'small-norm' prediction
 share_C ∝ sum_{a in C, N a <= X} 1/N a  (log-uniform divisor weight; Kronecker-limit constant)."""
import numpy as np
from sympy import isprime
from exf_load import load
from exf_cm_classes import reduce, classes   # noqa (module runs its own main when imported -> avoid)
T1, _ = load('data/exf/n2e4')
n = T1['n'].astype(np.int64)
isp = np.array([isprime(x) for x in range(int(n.max()) + 1)])
for d in (14, 26, 29, 41):
    cl = classes(4 * d); idx = {f: i for i, f in enumerate(cl)}
    R = T1[(T1['d'] == d) & isp[n]]
    a = R['a'].astype(np.int64); c = R['c'].astype(np.int64); p = R['n'].astype(np.int64)
    f = 4 * a * c * d - p; e = (4 * a * a * d + 1) // f
    lab = np.array([idx[reduce(int(F), int(4 * A * d), int(E * d))] for F, A, E in zip(f, a, e)])
    i0 = idx[(1, 0, d)]
    for lo, hi in ((5, 2000), (2000, 8000), (8000, 20001)):
        s = (p >= lo) & (p < hi)
        sh = np.bincount(lab[s], minlength=len(cl)) / s.sum()
        print(f'd={d} p in [{lo},{hi}): n_sol={s.sum()}, principal share {sh[i0]:.3f}, uniform {1/len(cl):.3f}, '
              f'share of f<=10: {np.mean(f[s] <= 10):.2f}, principal share among f>100: '
              f'{np.mean(lab[s & (f > 100)] == i0) if (s & (f > 100)).any() else float("nan"):.3f}')
