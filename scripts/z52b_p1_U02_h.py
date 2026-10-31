"""U02 confound check for Z0919/Z0968/Z0701: control for quadratic characters (2/p),(-3/p),(5/p),(-7/p) and mod 8."""
import json, math, numpy as np
from sympy import jacobi_symbol
exec(open('scripts/z52b_p1_U02_g.py').read().split('# Z0796:')[0])  # reuse loaders, residuals, L1, rq-free parts
pl = [int(p) for p in P if p <= 2000]
idx = np.array([i for i, p in enumerate(P) if p <= 2000]); resU = res_all[idx]; Pl = np.array(pl)
def leg(a, p): return kron(a, p)
X2 = np.array([leg(2, p) for p in pl], float)
X3 = np.array([leg(-3, p) for p in pl], float)
X5 = np.array([leg(5, p) for p in pl], float)
X7 = np.array([leg(-7, p) for p in pl], float)
def pc(x, y, Z=()):
    Zm = np.column_stack([np.ones(len(x))] + [np.asarray(z, float) for z in Z])
    ex = x - Zm @ np.linalg.lstsq(Zm, x, rcond=None)[0]
    ey = y - Zm @ np.linalg.lstsq(Zm, y, rcond=None)[0]
    return float(np.corrcoef(ex, ey)[0, 1])
A = rq((1, 2, 8)) if False else None
# Tunnell A(p)=r_{1,2,8}(p) for p<=2000 directly
Nm = 2000
Acnt = np.zeros(Nm + 1, int); Bcnt = np.zeros(Nm + 1, int)
for x in range(-45, 46):
    for y in range(-32, 33):
        for z in range(-16, 17):
            v = x*x + 2*y*y + 8*z*z
            if v <= Nm: Acnt[v] += 1
            v2 = x*x + 2*y*y + 32*z*z
            if v2 <= Nm: Bcnt[v2] += 1
Ap = Acnt[Pl].astype(float); Bp = Bcnt[Pl].astype(float)
h8 = np.array([hD(-8 * p) for p in pl]); h4 = np.array([hD(-4 * p) for p in pl])
ds = {}
ds['Z0919_corr_A_resU'] = pc(Ap, resU)
ds['Z0919_partial_A_resU_given_leg2'] = pc(Ap, resU, [X2])
ds['Z0919_partial_A_resU_given_leg2_leg-3_leg5_leg-7'] = pc(Ap, resU, [X2, X3, X5, X7])
ds['Z0919_A-2B_resU'] = pc(Ap - 2 * Bp, resU)
ds['frac_A_zero_given_p_mod8_5'] = float(np.mean(Ap[Pl % 8 == 5] == 0)), float(np.mean(Ap[Pl % 8 == 1] == 0))
ds['Z0968_partial_A_resU_given_leg2_logh8_logh4'] = pc(Ap, resU, [X2, np.log(h8), np.log(h4)])
ds['Z0968_partial_B_resU_given_leg2_logh8_logh4'] = pc(Bp, resU, [X2, np.log(h8), np.log(h4)])
# Z0701: R^2 with and without quadratic characters
Ls = {d: np.array([math.log(abs(L1(d * p if d != 1 else p))) for p in pl]) for d in (1, -4, -8, -3, 5, -7)}
def r2(cols):
    Z = np.column_stack([np.ones(len(resU))] + cols); c = np.linalg.lstsq(Z, resU, rcond=None)[0]
    return 1 - np.sum((resU - Z @ c)**2) / np.sum((resU - resU.mean())**2)
ds['Z0701_R2_logL_only'] = r2(list(Ls.values()))
ds['Z0701_R2_logL_plus_legendre'] = r2(list(Ls.values()) + [X2, X3, X5, X7])
ds['Z0701_R2_legendre_only'] = r2([X2, X3, X5, X7])
json.dump(ds, open('data/z52b/pass1/U02/fix_h.json', 'w'), indent=1, default=float)
for k, v in ds.items(): print(k, v)
