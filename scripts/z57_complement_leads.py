# z57 COMPLEMENT: registered-rule lead search. For every pair of level-band sub-families of DIFFERENT certificate
# families (STAR, B1, I1, c2, c3; QR excluded as a non-certificate placebo), the residual correlation after (a) p mod 840
# strata and (b) OLS on one-hot residues of p mod 8, 16, 32, 3, 9, 27, 5, 25, 7, 49, 11 … 47. A pair is a LEAD if (a) < -4
# nominal s.e. at >= 2 scales and (b) < -2 s.e. at those scales.
# usage: python z57_complement_leads.py  (reads data/z57/complement/w_1e8_*, w_1e9_*, w_1e10_*)
import sys, glob, math, functools
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z57_complement_stats import load, onehot_design, ols_resid, corr, strata_resid
print = functools.partial(print, flush=True)
base = __file__.rsplit('/', 2)[0] + '/data/z57/complement/'
scales = {'1e8': 'w_1e8_*.txt.gz', '1e9': 'w_1e9_*.txt.gz', '1e10': 'w_1e10_*.txt.gz'}
mods = [8, 16, 32, 3, 9, 27, 5, 25, 7, 49, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
res = {}
for s, pat in scales.items():
    p, D = load(sorted(glob.glob(base + pat)))
    N = len(p); sq = math.sqrt(N)
    X = onehot_design(p, mods); s840 = p % 840
    bands = [k for k in D if k[-1].isdigit() and k[:-1] in ('STARz', 'B1z', 'I1z', 'c2z', 'c3z') and D[k].mean() > 0.05]
    A = {k: strata_resid(D[k], s840) for k in bands}; B = {k: ols_resid(D[k], X) for k in bands}
    for i, a in enumerate(bands):
        for b in bands[i + 1:]:
            if a[:-1] == b[:-1]: continue
            res.setdefault((a, b), {})[s] = (corr(A[a], A[b]) * sq, corr(B[a], B[b]) * sq)
    print(f'# {s}: N = {N}, {len(bands)} bands with mean > 0.05')
leads = []; neg = []
for k, v in res.items():
    hits = [s for s in v if v[s][0] < -4 and v[s][1] < -2]
    if any(v[s][0] < -4 for s in v): neg.append((k, v))
    if len(hits) >= 2: leads.append((k, v))
print(f'## {len(res)} cross-family certificate band pairs; with z(840) < -4 at some scale: {len(neg)}; LEADS (rule): {len(leads)}')
for k, v in sorted(neg, key=lambda kv: min(x[0] for x in kv[1].values())):
    print(f'  {k[0]:7s} {k[1]:7s} ' + '  '.join(f'{s}: z840 {v[s][0]:+6.1f} zOLS {v[s][1]:+6.1f}' for s in v) + ('   <- LEAD' if (k, v) in leads else ''))
