"""Fix round TO3, batch D: Z0836 (cross-validated AUC), Z0864 (variant families for 241/2521/193), Z0870 (ladder levels),
Z0905 (tail comparison of residual log U with the regulator / L-value law), Z0906 (R analogue of the lognormal heuristic),
Z0924 (negative binomial over windows of R), Z0925 (5/p Legendre weights), Z0926 (cluster of residual vectors m=4..13),
Z0927 (denominator factorisations at 12601), Z0928 (6/p vs 4/p counts), Z0797 (non-diagonal ternary forms).
Writes data/z52b/pass2/TO3/fix_d_results.json"""
import csv, json, math, sys
import numpy as np
from scipy.stats import spearmanr, ks_2samp, norm
from scipy.special import gammaln
from scipy.optimize import minimize
from sympy import factorint, primerange, jacobi_symbol
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
# ---- Z0836: cross-validated AUC: fit on primes <= 3e4, test on (3e4,1e5] ----
def auc(pos, neg):
    allv = np.concatenate([pos, neg]); rk = allv.argsort().argsort() + 1
    return float((rk[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
Lmap = {int(r['p']): float(r['L1real']) for r in rows if r['L1real'] != 'NA'}
cv = {}
for m in range(8, 49):
    A = np.loadtxt(f'data/z52b/raw/m{m}_pr1e5.txt', dtype=np.int64)
    A = A[(A[:, 0] > 100) & np.array([int(q) in Lmap for q in A[:, 0]])]
    p_ = A[:, 0]; U_ = A[:, 1].astype(float); Lv = np.array([Lmap[int(q)] for q in p_])
    X_ = np.column_stack([np.ones(len(p_)), np.log(p_.astype(float)), np.log(np.log(p_.astype(float))), np.log(Lv)])
    y_ = np.log1p(U_)
    tr = p_ <= 30000; te = ~tr
    if (U_[te] == 0).sum() == 0 or (U_[te] > 0).sum() == 0:
        cv[m] = dict(n_test_fail=int((U_[te] == 0).sum()), auc=None); continue
    b = np.linalg.lstsq(X_[tr], y_[tr], rcond=None)[0]
    sc = X_[te] @ b
    cv[m] = dict(n_test_fail=int((U_[te] == 0).sum()), auc=round(1 - auc(sc[U_[te] == 0], sc[U_[te] > 0]), 3))
out['Z0836_cv'] = cv
av = [v['auc'] for v in cv.values() if v['auc'] is not None]
out['Z0836_cv_median_auc'] = float(np.median(av)) if av else None
out['Z0836_cv_n_numerators_with_test_failures'] = len(av)
# ---- Z0864: membership of 241, 2521, 193 in the variant families (variants.json, computed by the repo) ----
V = json.load(open('data/z52b/variants.json'))
memb = {}
for key in V:
    if isinstance(V[key], dict) and 'fail_primes_head' in V[key]:
        memb[key] = dict(n_fail=V[key]['n_fail_primes'], head=V[key]['fail_primes_head'][:0])
out['Z0864_variant_keys'] = list(V.keys())[:40]
out['Z0864_variant_fail_counts'] = {k: v['n_fail'] for k, v in memb.items()}
# direct test of 241, 2521, 193 against each family (families: lcm-closed, squarefree, no-3, 4|denominators ...) using exact sols
tests = {}
for q in (193, 241, 2521):
    S_ = sols(4, q)
    fam = {}
    fam['exists_solution'] = len(S_) > 0
    fam['all_squarefree_denominators'] = any(all(all(e == 1 for e in factorint(v).values()) for v in s) for s in S_)
    fam['no_denominator_div_by_3'] = any(all(v % 3 for v in s) for s in S_)
    fam['some_denominator_div_by_4'] = any(any(v % 4 == 0 for v in s) for s in S_)
    fam['primitive_gcd1'] = any(gcd(gcd(s[0], s[1]), s[2]) == 1 for s in S_)
    fam['lcm_closed_style_x_divides_z'] = any(s[2] % s[0] == 0 for s in S_)
    tests[q] = dict(n_solutions=len(S_), **fam)
out['Z0864_family_tests'] = tests
# ---- Z0870: ladder levels of the 2-power denominator primes (minimal a with 2^a a denominator) ----
def exists_pow2_level(pp):
    for a in range(1, 40):
        t = 2 ** a; num = 4 * t - pp
        if num <= 0: continue
        den = pp * t; g = gcd(num, den); A, B = num // g, den // g
        fB = factorint(B); divs = [1]
        for q, e in fB.items(): divs = [d * q ** j for d in divs for j in range(2 * e + 1)]
        for d in divs:
            if (d + B) % A == 0 and ((B * B // d) + B) % A == 0: return a
    return None
lev = {}
for pp in primerange(3, 100001):
    a = exists_pow2_level(pp)
    if a is not None: lev.setdefault(a, []).append(pp)
out['Z0870_levels'] = {a: dict(count=len(v), first=v[:6]) for a, v in sorted(lev.items())}
out['Z0870_total_odd'] = sum(len(v) for v in lev.values())
# ---- Z0905 : empirical tail comparison: residual log U vs the L-value law log U ~ -alpha log L (alpha from data) ----
R0 = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0 and r['L1real'] != 'NA']
p = np.array([int(r['p']) for r in R0]); U = np.array([float(r['U']) for r in R0]); L = np.array([float(r['L1real']) for r in R0])
lp = np.log(p.astype(float))
Xl = np.column_stack([np.ones(len(p)), lp, np.log(lp), np.log(L)])
bb = np.linalg.lstsq(Xl, np.log(U), rcond=None)[0]
pred = Xl @ bb
res = np.log(U) - pred
ks = ks_2samp(res, np.random.default_rng(0).normal(0, res.std(), size=len(res)))
qs = [0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]
out['Z0905'] = dict(alpha=round(float(bb[3]), 4), sd_resid=round(float(res.std()), 4),
                    empirical_lower_tail_quantiles={q: round(float(np.quantile(res, q)), 3) for q in qs},
                    gaussian_quantiles={q: round(float(norm.ppf(q) * res.std()), 3) for q in qs},
                    ks_vs_gaussian_stat=round(float(ks.statistic), 4), ks_p=round(float(ks.pvalue), 4),
                    skew=round(float(((res - res.mean()) ** 3).mean() / res.std() ** 3), 3),
                    note='GS-type L(1,chi) distribution not fitted; comparison uses the empirical L-distribution law (log U = a + b log p + c loglog p + d log L) and its residual tails')
# ---- Z0906 : R analogue of the lognormal heuristic (primes <= 3e6) using the logit table ----
T = np.load('/tmp/z52/big/primes_1mod4.npz'); PT = T['p']; L1T = T['L1']; H4T = T['h4'].astype(float)
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(10**8 + 1, 7))
RT = np.asarray(W[PT, 2]).astype(float)
mk = RT > 0
XT = np.column_stack([np.ones(mk.sum()), np.log(PT[mk].astype(float)), np.log(np.log(PT[mk].astype(float))), np.log(L1T[mk])])
bR = np.linalg.lstsq(XT, np.log(RT[mk]), rcond=None)[0]; sdR = np.std(np.log(RT[mk]) - XT @ bR)
XA = np.column_stack([np.ones(len(PT)), np.log(PT.astype(float)), np.log(np.log(PT.astype(float))), np.log(L1T)])
muA = XA @ bR
pz = norm.cdf((math.log(1.5) - muA) / sdR)
out['Z0906_R_analogue'] = dict(coef=[round(float(c), 3) for c in bR], sd_logR=round(float(sdR), 3), expected_R0_primes_le3e6=round(float(pz.sum()), 3),
                               observed_R0=int((RT == 0).sum()))
# ---- Z0924 : negative binomial over windows of R (all n = 1 mod 4 in windows [1e6,1e7)) ----
Nn = 10**7
Rall = np.asarray(W[1:Nn + 1, 2]).astype(float)
nn = np.arange(1, Nn + 1)
s_ = (nn % 4 == 1)
sq_mask = np.zeros(Nn + 1, bool); sq_mask[np.arange(1, 3163) ** 2] = True
s_ = s_ & ~sq_mask[1:Nn + 1]                 # exclude squares (R=0 by T1)
Rw = Rall[s_]
mu = Rw.mean(); var = Rw.var(); kdisp = mu ** 2 / max(var - mu, 1e-9)
p0_emp = float((Rw == 0).mean())
p0_nb = float((1 + mu / kdisp) ** (-kdisp))
out['Z0924_nb_window_1e6_1e7_n1mod4'] = dict(mean=round(float(mu), 3), var=round(float(var), 3), k=round(float(kdisp), 3),
                                              P0_emp=p0_emp, P0_nb=p0_nb, n=int(len(Rw)), zeros=int((Rw == 0).sum()))
# predicted zeros in [1e7,1e8) under NB with mean scaled by log^2 growth (mean_R/log^2 n ~ 0.132): mean ~ c*log^2 n
Wm = np.asarray(W[10**7:10**8 + 1, 2]).astype(float)
nw = np.arange(10**7, 10**8 + 1)
s2 = (nw % 4 == 1) & ~np.isin(nw, np.arange(1, 10001) ** 2)   # exclude squares
mu2 = Wm[s2].mean(); var2 = Wm[s2].var(); k2 = mu2 ** 2 / max(var2 - mu2, 1e-9)
out['Z0924_window_1e7_1e8_n1mod4'] = dict(mean=round(float(mu2), 3), var=round(float(var2), 3), k=round(float(k2), 3),
                                           P0_emp=float((Wm[s2] == 0).mean()), P0_nb=float((1 + mu2 / k2) ** (-k2)), zeros=int((Wm[s2] == 0).sum()))
# ---- Z0925 : 5/p Legendre weights (m5 counts) vs 4/p ----
m5 = np.loadtxt('data/z52b/raw/m5_pr1e5.txt', dtype=np.int64)
m5 = m5[(m5[:, 0] > 100) & (m5[:, 0] % 4 == 1) & (m5[:, 1] > 0)]
p5 = m5[:, 0]; U5 = m5[:, 1].astype(float); lp5 = np.log(p5.astype(float))
r5 = np.log(U5) - np.column_stack([np.ones(len(p5)), lp5, np.log(lp5)]) @ np.linalg.lstsq(np.column_stack([np.ones(len(p5)), lp5, np.log(lp5)]), np.log(U5), rcond=None)[0]
QS = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Lg5 = np.column_stack([np.array([int(jacobi_symbol(q, int(x))) for x in p5]).astype(float) for q in QS])
B5 = np.linalg.lstsq(np.column_stack([np.ones(len(p5)), lp5, np.log(lp5), Lg5]), np.log(U5), rcond=None)[0]
out['Z0925_weights_5over_p'] = {q: round(float(B5[3 + i]), 4) for i, q in enumerate(QS)}
out['Z0925_qbeta_5'] = {q: round(float(q * B5[3 + i]), 3) for i, q in enumerate(QS)}
# ---- Z0926 : residual vectors m=4..13 over common primes; cluster by correlation ----
import numpy as _np
fam = {}
for k in range(4, 14):
    if k == 4:
        d = {int(r['p']): float(r['U']) for r in rows if int(r['mod4']) == 1 and 2 < int(r['p']) <= 99999}
    else:
        A = np.loadtxt(f'data/z52b/raw/m{k}_pr1e5.txt', dtype=np.int64)
        d = {int(a): float(b) for a, b in A[:, :2] if a > 2}
    fam[k] = {q: u for q, u in d.items() if u > 0}
common = sorted(set.intersection(*[set(v.keys()) for v in fam.values()]))
common = [q for q in common if q % 4 == 1]
Rm = {}
cq = np.array(common, float); lcq = np.log(cq)
for k in range(4, 14):
    u = np.log(np.array([fam[k][q] for q in common]))
    Rm[k] = u - np.column_stack([np.ones(len(cq)), lcq, np.log(lcq)]) @ np.linalg.lstsq(np.column_stack([np.ones(len(cq)), lcq, np.log(lcq)]), u, rcond=None)[0]
Mx = np.vstack([Rm[k] for k in range(4, 14)])
avg = Mx.mean(axis=0)
hard_all = [common[i] for i in np.argsort(avg)[:12]]
out['Z0926_cluster'] = dict(n_common=len(common), mean_residual_hardest12_across_m=hard_all,
                            corr_eigs=[round(float(v), 3) for v in np.sort(np.linalg.eigvalsh(np.corrcoef(Mx)))[::-1][:4]],
                            frac_variance_first_pc=round(float(np.linalg.eigvalsh(np.corrcoef(Mx))[-1] / 10), 3))
# ---- Z0927 : factorisations of the denominators for 4/12601, 5/12601, 7/12601 ----
out['Z0927'] = {}
for m in (4, 5, 7):
    S_ = sols(m, 12601)
    fac = Counter_ = {}
    for s in S_:
        for v in s:
            key = tuple(sorted(factorint(v).items()))
            fac[key] = fac.get(key, 0) + 1
    common_primes = {q: sum(1 for s in S_ for v in s if v % q == 0) for q in (2, 3, 5, 7, 12601)}
    out['Z0927'][m] = dict(nsol=len(S_), prime_support_counts=common_primes,
                           most_common_denominator_factorisations=[(str(k), c) for k, c in sorted(fac.items(), key=lambda kv: -kv[1])[:5]])
# ---- Z0928 : 6/p vs 4/p solution counts ----
ratio = {}
for c in (1, 5, 7, 11):
    pass
rat = {}
for q in primerange(100, 3000):
    if q % 12 not in (1, 5, 7, 11): continue
    u4 = len(sols(4, q)); u6 = len(sols(6, q))
    rat.setdefault(q % 12, []).append(u6 / u4 if u4 else None)
out['Z0928_U6_over_U4_by_p_mod12'] = {k: round(float(np.mean([x for x in v if x is not None])), 3) for k, v in rat.items()}
out['Z0928_U6_zero_count_p_le3000'] = sum(1 for q in primerange(3, 3000) if len(sols(6, q)) == 0)
json.dump(out, open('data/z52b/pass2/TO3/fix_d_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:400])
