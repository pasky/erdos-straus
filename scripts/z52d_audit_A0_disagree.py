"""z52d audit A0, item Z1234: model-disagreement allocation. Two (★) count models from the repo:
A = M_BM (BM_CORRECTED_COUNT, characters), B = M_BM·F (RESIDUE_HARDNESS §2.3 local-density class factor, same construction as
scripts/z52c_rh_hard.py). Disagreement = log F. Look at the primes where A and B disagree most (both tails, balanced) and ask
which model predicts R there, vs. the bulk. Input: /tmp/z52dA0/mbm_1e6.txt from `scripts/z38_mbm.c 3 1000000 0`.
Usage: uv run --with numpy --with scipy python scripts/z52d_audit_A0_disagree.py"""
import numpy as np, json
from scipy.stats import poisson
MT = json.load(open('data/z52c/rh/model_tables.json')); REF = '1e6'
COMP = [(840, 1), (16, 1), (8, -1), (11, 1), (13, 1)]
def lfac(PP, fam):
    L0 = MT[REF]['L']; L = np.log(PP.astype(float)); lf = np.zeros(len(PP))
    for Q, sgn in COMP:
        d = MT[REF][str(Q)]; fac = dict(zip(d['classes'], d[fam]['model']))
        lf += sgn*np.log(1 + (np.array([fac[int(x)] for x in PP % Q]) - 1)*L0/L)
    return lf
A = np.loadtxt('/tmp/z52dA0/mbm_1e6.txt'); A = A[(A[:, 1] == 1) & (A[:, 0] % 4 == 1) & (A[:, 0] > 1000)]
P = A[:, 0].astype(np.int64); R = A[:, 2]; M0 = A[:, 3]; M = A[:, 4]; Fraw = np.exp(lfac(P, 'S'))
W = (P >= 200000); LW = np.log(np.sqrt(200000*1e6)); lbm = np.zeros(len(P))
for Q, sgn in COMP:
    cl = MT[REF][str(Q)]['classes']; mm = M[W].mean(); fac = {c: M[W & (P % Q == c)].mean()/mm for c in cl}
    lbm += sgn*np.log(1 + (np.array([fac[int(x)] for x in P % Q]) - 1)*LW/np.log(P.astype(float)))
F = Fraw/np.exp(lbm); MF = M*F; d = np.log(F)
print(f"n={len(P)} primes p≡1(4) in (1e3,1e6]; log F: sd {d.std():.3f}, 5%/95% quantiles {np.quantile(d,.05):.3f}/{np.quantile(d,.95):.3f}")
def stats(mask, name):
    out = [name, int(mask.sum())]
    for nm, Mx in [('M0', M0), ('M_BM', M), ('M_BM*F', MF)]:
        ll = poisson.logpmf(R[mask]/2, Mx[mask]/2).mean(); bias = np.mean(np.log((R[mask]+1)/(Mx[mask]+1)))
        out.append(f"{nm}: meanLL {ll:.3f} bias {bias:+.3f}")
    print(" | ".join(map(str, out)))
lo, hi = np.quantile(d, [.05, .95])
stats(np.ones(len(P), bool), 'all')
stats(d <= lo, 'B<<A (5%)'); stats(d >= hi, 'B>>A (5%)'); stats((d > np.quantile(d,.4)) & (d < np.quantile(d,.6)), 'agree (middle 20%)')
# where do the disagreement tails sit in residue terms?
for nm, msk in [('B<<A', d <= lo), ('B>>A', d >= hi)]:
    cls, cnt = np.unique(P[msk] % 840, return_counts=True); top = np.argsort(-cnt)[:6]
    print(nm, 'top classes mod 840:', [(int(cls[i]), int(cnt[i])) for i in top], ' frac p≡1 (16):', round(float((P[msk] % 16 == 1).mean()), 3),
          ' zeros of R:', int((R[msk] == 0).sum()), 'of', int((R == 0).sum()))
# swap-Poisson zero calibration in the tails
for nm, msk in [('B<<A', d <= lo), ('B>>A', d >= hi)]:
    print(nm, 'expected zeros  M_BM:', round(float(np.exp(-M[msk]/2).sum()), 2), ' M_BM*F:', round(float(np.exp(-MF[msk]/2).sum()), 2), ' observed:', int((R[msk]==0).sum()))
