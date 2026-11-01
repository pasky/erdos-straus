# z52d pass2 NC1 Z1363: partial Dirichlet series of f(n) (f from z52d_p2_NC1_fn.c, n ≤ 3000)
import math
from sympy import zeta
f = {}
for l in open('data/z52b/pass2/NC1/fn_1_3000.txt'):
    n, c = map(int, l.split()); f[n] = c
out = {'mean_f_over_log3n_N3000': round(sum(f[n] for n in range(2, 3001))/sum(math.log(n)**3 for n in range(2, 3001)), 4),
       'n_with_f0': sum(1 for n in range(2, 3001) if f[n] == 0), 'max_f': max(f.values())}
res = {}
for s in [2, 3]:
    z = float(zeta(s))
    for N in [300, 1000, 3000]:
        F = sum(f[n]/n**s for n in range(2, N+1))
        res[f's={s},N={N}'] = {'partial_F': round(F, 6), 'partial_F/zeta^3': round(F/z**3, 6)}
out['partial_dirichlet'] = res
import json; print(json.dumps(out, indent=1))
