# z57 COMPLEMENT: exploratory follow-up of the registered leads (not pre-registered).
# For each lead pair: residual correlation under (0) OLS residues mod 8,16,32,3,9,27,5,25,7,49,11..47 (the rule's control),
# (1) + residues mod every prime 53..199, (2) + L-proxies (quadratic), (3) + the totals INT and W of interior/all words.
# usage: python z57_complement_leadfollow.py LABEL files...
import sys, math, functools
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z57_complement_stats import load, onehot_design, ols_resid, corr
from z57_complement_lproxy import lproxies, primes_upto
print = functools.partial(print, flush=True)
LEADS = [('STARz7', 'c2z8'), ('STARz7', 'c3z8'), ('STARz6', 'c2z8'), ('STARz7', 'B1z8'), ('c2z6', 'c3z8'), ('STARz0', 'c2z6'),
         ('STARz0', 'B1z1'), ('B1z1', 'I1z0'), ('STARz0', 'c2z1'), ('STARz1', 'I1z1'), ('STARz1', 'I1z0'), ('I1z1', 'c2z0')]
label = sys.argv[1]; p, D = load(sys.argv[2:]); N = len(p); sq = math.sqrt(N)
m0 = [8, 16, 32, 3, 9, 27, 5, 25, 7, 49, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
m1 = m0 + [int(q) for q in primes_upto(199) if q > 47]
X0 = onehot_design(p, m0); X1 = onehot_design(p, m1)
Lp, L4 = lproxies(p)
X2 = np.column_stack([X1, Lp, L4, Lp * Lp, L4 * L4, Lp * L4])
X3 = np.column_stack([X2, D['W'] - D['BND'], D['W']])
print(f'# {label}: N = {N}; columns {X0.shape[1]}, {X1.shape[1]}, {X2.shape[1]}, {X3.shape[1]}')
names = sorted({x for ab in LEADS for x in ab})
Y = np.column_stack([D[k] for k in names])
RES = []
for X in (X0, X1, X2, X3):
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None); RES.append({k: (Y - X @ beta)[:, i] for i, k in enumerate(names)})
for a, b in LEADS:
    out = []
    for R in RES:
        r = corr(R[a], R[b]); out.append(f'{r:+.4f} ({r * sq:+.1f})')
    print(f'{a:7s} {b:7s} means {D[a].mean():.2f} {D[b].mean():.2f} | ' + ' | '.join(out))
