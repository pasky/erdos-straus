"""Fix round TO3 (Z0797): all reduced positive ternary quadratic forms with small determinant (Eisenstein-type reduction
conditions 0 < a <= b <= c, |2f| <= a, |2e| <= a, |2d| <= b, det <= DMAX) and their representation numbers r_Q(p) at primes
1 mod 4 <= NMAX, Spearman with the residual log U(p) (base table). Writes data/z52b/pass2/TO3/forms2_results.json"""
import csv, json, math, itertools
import numpy as np
from scipy.stats import spearmanr
DMAX = 12; NMAX = 6000
forms = []
for a in range(1, 13):
    for b in range(a, 13):
        for c in range(b, 13):
            for f in range(-(a // 2), a // 2 + 1):      # |2f|<=a
                for e in range(-(a // 2), a // 2 + 1):  # |2e|<=a
                    for d in range(-(b // 2), b // 2 + 1):  # |2d|<=b
                        M = np.array([[a, f, e], [f, b, d], [e, d, c]], dtype=float)
                        det = round(np.linalg.det(M))
                        if det <= 0 or det > DMAX: continue
                        if np.any(np.linalg.eigvalsh(M) <= 0): continue
                        forms.append(((a, b, c, f, e, d), M, det))
print('forms', len(forms))
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
pr = [int(r['p']) for r in rows if int(r['mod4']) == 1 and 100 < int(r['p']) <= NMAX]
U = np.array([float(r['U']) for r in rows if int(r['mod4']) == 1 and 100 < int(r['p']) <= NMAX])
lp = np.log(np.array(pr, float)); Xr = np.column_stack([np.ones(len(pr)), lp, np.log(lp)])
resU = np.log(U) - Xr @ np.linalg.lstsq(Xr, np.log(U), rcond=None)[0]
Lm = {int(r['p']): float(r['L1real']) for r in rows if r['L1real'] != 'NA'}
resL = np.log([Lm[q] for q in pr]); resL = resL - Xr @ np.linalg.lstsq(Xr, resL, rcond=None)[0]
res = []
for key, M, det in forms:
    Mi = np.linalg.inv(M)
    # Q(x) = x^T M x with the half-integer convention: x^T M x = a x^2+... + 2f xy + ...  (off-diagonal entries are f,e,d)
    # bounds: |x_i| <= sqrt(N * (M^{-1})_ii)
    bx = [int(math.isqrt(int(NMAX * Mi[i, i]) + 1)) + 1 for i in range(3)]
    xs = np.arange(-bx[0], bx[0] + 1); ys = np.arange(-bx[1], bx[1] + 1); zs = np.arange(-bx[2], bx[2] + 1)
    X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')
    A_, B_, C_, F_, E_, D_ = key
    Q = A_ * X * X + B_ * Y * Y + C_ * Z * Z + 2 * F_ * X * Y + 2 * E_ * X * Z + 2 * D_ * Y * Z
    Q = Q[(Q > 0) & (Q <= NMAX)]
    cnt = np.bincount(Q, minlength=NMAX + 1)
    r = cnt[np.array(pr)].astype(float)
    if r.std() == 0: continue
    rho = float(spearmanr(r, resU)[0]); rhoL = float(spearmanr(r, resL)[0])
    res.append((key, det, rho, rhoL))
best = sorted(res, key=lambda t: -abs(t[2]))[:8]
out = dict(n_forms=len(forms), n_forms_nonconstant=len(res), DMAX=DMAX, NMAX=NMAX, n_primes=len(pr),
           baseline_rho_resU_resL1=round(float(spearmanr(resU, resL)[0]), 3),
           best_by_abs_rho=[dict(form=list(k), det=d, rho_resU=round(r_, 3), rho_resL1=round(rl, 3)) for k, d, r_, rl in best],
           median_abs_rho=round(float(np.median([abs(t[2]) for t in res])), 3),
           frac_abs_rho_gt_0_3=round(float(np.mean([abs(t[2]) > 0.3 for t in res])), 3),
           n_forms_beating_L1_baseline=sum(1 for t in res if abs(t[2]) > abs(spearmanr(resU, resL)[0])))
json.dump(out, open('data/z52b/pass2/TO3/forms2_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1)[:2500])
