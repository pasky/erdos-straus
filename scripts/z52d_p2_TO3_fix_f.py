"""Fix round TO3, batch F: Z0959 (h(-8p) mod-16 strata, residual log U, p=1 mod 8), Z0836 (per-numerator Legendre-weight
models, cross-validated AUC), Z0978 (cleared equation z = p g a b/(4 g a b - p(a+b)) checked on all solutions p<=300).
Writes data/z52b/pass2/TO3/fix_f_results.json"""
import csv, json, math, sys
import numpy as np
import cypari2
from sympy import primerange, jacobi_symbol
from math import gcd
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
pari = cypari2.Pari(); pari.allocatemem(10**9)
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
S = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0 and int(r['p']) % 8 == 1]
p = np.array([int(r['p']) for r in S]); U = np.array([float(r['U']) for r in S]); lp = np.log(p.astype(float))
X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
rU = np.log(U) - X @ np.linalg.lstsq(X, np.log(U), rcond=None)[0]
h8 = np.array([int(pari.qfbclassno(-8 * int(q))) for q in p])
h24 = np.array([int(pari.qfbclassno(-24 * int(q))) for q in p])
h4 = np.array([int(float(r['h4p'])) for r in S])
out['Z0959_h8'] = dict(n=len(p), mean_resU_by_h8_mod16={int(c): round(float(rU[(h8 % 16) == c].mean()), 4) for c in (0, 4, 8, 12) if ((h8 % 16) == c).any()},
                       count={int(c): int(((h8 % 16) == c).sum()) for c in (0, 4, 8, 12)},
                       h8_mod8_vs_leg2_legendre3={})
# is h(-8p) mod 8 genus-determined? crosstab with (3/p) and (5/p)
l3 = np.array([int(jacobi_symbol(3, int(q))) for q in p]); l5 = np.array([int(jacobi_symbol(5, int(q))) for q in p])
out['Z0959_h8_genus_crosstab'] = {f'h8mod8={a},3/p={b}': int(((h8 % 8 == a) & (l3 == b)).sum()) for a in (0, 2, 4, 6) for b in (1, -1)}
within = {}
for b in (1, -1):
    for c in (0, 4, 8, 12):
        s = (l3 == b) & ((h8 % 16) == c)
        if s.sum() > 20: within[f'3/p={b},h8mod16={c}'] = dict(n=int(s.sum()), mean_resU=round(float(rU[s].mean()), 4))
out['Z0959_h8_within_3p_class'] = within
# ---- Z0836 : per-numerator models with Legendre weights (q<=47) and L(1,chi_p); cross-validated AUC ----
Lmap = {int(r['p']): float(r['L1real']) for r in rows if r['L1real'] != 'NA'}
QS = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def auc(pos, neg):
    allv = np.concatenate([pos, neg]); rk = allv.argsort().argsort() + 1
    return float((rk[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
cv = {}
for m in range(8, 49):
    A = np.loadtxt(f'data/z52b/raw/m{m}_pr1e5.txt', dtype=np.int64)
    A = A[(A[:, 0] > 100) & np.array([int(q) in Lmap for q in A[:, 0]])]
    pp = A[:, 0]; Um = A[:, 1].astype(float)
    Leg = np.column_stack([np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in pp]).astype(float) for q in QS])
    Lv = np.array([Lmap[int(q)] for q in pp])
    Xm = np.column_stack([np.ones(len(pp)), np.log(pp.astype(float)), np.log(np.log(pp.astype(float))), np.log(Lv), Leg])
    y = np.log1p(Um)
    tr = pp <= 30000; te = ~tr
    if (Um[te] == 0).sum() == 0 or (Um[te] > 0).sum() == 0:
        cv[m] = None; continue
    b = np.linalg.lstsq(Xm[tr], y[tr], rcond=None)[0]
    sc = Xm[te] @ b
    cv[m] = round(1 - auc(sc[Um[te] == 0], sc[Um[te] > 0]), 3)
vals = [v for v in cv.values() if v is not None]
out['Z0836_legendre_cv'] = dict(per_m=cv, median=float(np.median(vals)), n=len(vals), frac_above_0_7=round(float(np.mean([v > 0.7 for v in vals])), 3))
# ---- Z0978 : cleared equation check ----
ok = 0; tot = 0
for pq in primerange(3, 301):
    for (x, y_, z) in sols(4, pq):
        g = gcd(x, y_)
        a, b = x // g, y_ // g
        if gcd(a, b) != 1: continue
        den = 4 * g * a * b - pq * (a + b)
        tot += 1
        if den != 0 and (pq * g * a * b) % den == 0 and (pq * g * a * b) // den == z:
            ok += 1
        # also check the other ordering (x,y) and z-> solution symmetric cases skipped
out['Z0978_cleared_equation'] = dict(formula='x=g a, y=g b, gcd(a,b)=1 ⇒ z = p g a b / (4 g a b − p (a+b))', checked=tot, agree=ok)
json.dump(out, open('data/z52b/pass2/TO3/fix_f_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:700])
