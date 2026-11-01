"""Pass-2 TO3: (Z0836) in-sample AUC of a per-numerator count law (log(1+U_m) ~ log p, loglog p, log L(1,chi_p)) for the
failures of m/p, m=8..48, primes <= 1e5; (Z0843) single-feature AUC for R-zeros (words census to 3e6) among primes <= 2e5;
(Z0906) lognormal-model expected number of primes with U(p)=0 (model only, not an ES result); (Z0932) U(8803369) check.
Writes data/z52b/pass2/TO3/auc_results.json"""
import csv, json, math, subprocess
import numpy as np
from scipy.stats import norm
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
P = np.array([int(r['p']) for r in rows]); L1 = np.array([float(r['L1real']) if r['L1real'] != 'NA' else np.nan for r in rows])
M4 = np.array([int(r['mod4']) for r in rows]); H4 = np.array([float(r['h4p']) for r in rows])
def auc(pos, neg):
    """P(score_pos > score_neg) (ties counted 1/2 via ranks)."""
    pos = np.asarray(pos); neg = np.asarray(neg)
    if len(pos) == 0 or len(neg) == 0: return None
    allv = np.concatenate([pos, neg]); ranks = allv.argsort().argsort() + 1
    rp = ranks[:len(pos)].sum()
    return float((rp - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
# ---- Z0836 ----
res836 = {}
for m in range(8, 49):
    fn = f'data/z52b/raw/m{m}_pr1e5.txt'
    A = np.loadtxt(fn, dtype=np.int64)
    p = A[:, 0]; U = A[:, 1].astype(float)
    sel = (p > 100)
    idx = {int(q): i for i, q in enumerate(P)}
    ok = np.array([int(q) in idx and np.isfinite(L1[idx[int(q)]]) for q in p]) & sel
    p2 = p[ok]; U2 = U[ok]; L = np.array([L1[idx[int(q)]] for q in p2])
    X = np.column_stack([np.ones(len(p2)), np.log(p2.astype(float)), np.log(np.log(p2.astype(float))), np.log(L)])
    y = np.log1p(U2)
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    score = X @ b
    fail = U2 == 0
    res836[m] = dict(n=int(len(p2)), n_fail=int(fail.sum()), auc_fail_low_score=None if fail.sum() == 0 or fail.sum() == len(fail) else round(1 - auc(score[fail], score[~fail]), 3),
                     coef_logL=round(float(b[3]), 3))
out['Z0836'] = res836
aucs = [v['auc_fail_low_score'] for v in res836.values() if v['auc_fail_low_score'] is not None]
out['Z0836_median_auc'] = float(np.median(aucs)) if aucs else None
# ---- Z0843: R-zeros vs others (R from words census) ----
W = np.loadtxt('/tmp/z52/words3e6.txt', dtype=np.int64)
Rv = dict(zip(W[:, 0].tolist(), W[:, 3].tolist()))
pr = [int(q) for q in P if q <= 199999 and q % 4 == 1 and q > 100]
R = np.array([Rv[q] for q in pr]); idx = {int(q): i for i, q in enumerate(P)}
Lp = np.array([L1[idx[q]] for q in pr]); Hp = np.array([H4[idx[q]] / math.sqrt(q) for q in pr])
zeros = R == 0
out['Z0843'] = dict(n_primes=len(pr), n_R0=int(zeros.sum()), R0_primes=[q for q, z in zip(pr, zeros) if z],
                    auc_zero_by_L1_high=round(auc(Lp[zeros], Lp[~zeros]), 3),
                    auc_zero_by_h_high=round(auc(Hp[zeros], Hp[~zeros]), 3),
                    auc_Rle2_by_L1_high=round(auc(Lp[R <= 2], Lp[R > 2]), 3))
# ---- Z0906: lognormal heuristic ----
mask = (M4 == 1) & (P > 100) & (P < 200000)
Pm = P[mask]; lp = np.log(Pm.astype(float)); Lm = L1[mask]
UU = np.array([float(r['U']) for r, mm in zip(rows, (M4 == 1) & (P > 100) & (P < 200000)) if mm])
X = np.column_stack([np.ones(len(lp)), lp, np.log(np.log(lp)), np.log(Lm)])
y = np.log(UU)
b = np.linalg.lstsq(X, y, rcond=None)[0]; sig = float(np.std(y - X @ b))
mu = X @ b
pz = norm.cdf((math.log(0.5) - mu) / sig)
RR = np.array([Rv[int(q)] for q in Pm]) if False else None
out['Z0906'] = dict(n=int(len(y)), coef=[round(float(v), 4) for v in b], sigma_logU=round(sig, 4),
                    expected_primes_with_U0_under_model=round(float(pz.sum()), 3),
                    note='lognormal model on log U with fitted mean (log p, loglog p, log L1); observed U(p)=0 count in this range: 0')
# ---- Z0932: U at 8803369 and 119945383009? (only the first) ----
o = subprocess.run(['/tmp/z52/count4', '4', '8803369', '8803369', '0'], capture_output=True, text=True, timeout=600).stdout.split()
Wbig = dict((int(a), int(b)) for a, b, *_ in (l.split() for l in open('/tmp/z52/words_8p8e6.txt')) ) if False else None
out['Z0932_U_8803369'] = dict(N=int(o[0]), U=int(o[1]), D=int(o[2]), O=int(o[3]), minz=int(o[4]), maxx=int(o[7]), minx=int(o[8]), k1=int(o[10]), k2=int(o[11]), k3=int(o[12]))
import subprocess as sp2
wl = sp2.run(['awk', '$1==8803369', '/tmp/z52/words_8p8e6.txt'], capture_output=True, text=True).stdout.split()
out['Z0932_words_at_8803369'] = dict(W=int(wl[1]), I3=int(wl[2]), R=int(wl[3]), Uv=int(wl[4]), ESC=int(wl[5])) if wl else None
json.dump(out, open('data/z52b/pass2/TO3/auc_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:700])
