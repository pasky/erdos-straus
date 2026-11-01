"""Pass-2 batch TO3: analyses on the base table data/z52b/pass2/TO3/base_primes_2e5.tsv
(built by scripts/z52d_p2_TO3_base.py; all primes <= 2e5; U = #unordered solutions of 4/p).
Prints the numbers used in the outcome records; writes data/z52b/pass2/TO3/base_results.json.
Run: uv run --with numpy --with scipy --with cypari2 python scripts/z52d_p2_TO3_base_analysis.py
"""
import numpy as np, json, math, sys
from scipy.stats import spearmanr
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
T = 'data/z52b/pass2/TO3/base_primes_2e5.tsv'
OUT = 'data/z52b/pass2/TO3/base_results.json'
import csv
rows = list(csv.DictReader(open(T), delimiter='\t'))
res = {}
def col(name, sel=None, conv=float):
    v = [conv(r[name]) if r[name] not in ('NA', 'nan') else np.nan for r in rows]
    return np.array(v)
p = col('p', conv=int); mod4 = col('mod4', conv=int)
U = col('U', conv=float); k1 = col('k1'); k2 = col('k2'); k3 = col('k3'); D = col('D'); nx = col('nx')
minz = col('minz'); maxx = col('maxx', conv=float); minx = col('minx')
h4p = col('h4p'); hreal = col('hreal'); Rreal = col('Rreal'); L1r = col('L1real'); L1m = col('L1m4p')
lqnr = col('leastQNR', conv=float); g = col('leastprimroot'); o2 = col('ord2')
leg = {q: col(f'leg{q}') for q in (2, 3, 5, 7)}
P1 = (mod4 == 1) & (p > 100) & (p < 200000)
lp = np.log(p.astype(float))
def sp(a, b):
    m = np.isfinite(a) & np.isfinite(b)
    return float(spearmanr(a[m], b[m])[0])
def resid(y, X):
    X = np.column_stack([np.ones(len(y))] + X)
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return y - X @ beta
def partial_sp(a, b, c):
    ra = resid(np.argsort(np.argsort(a)).astype(float), [np.argsort(np.argsort(c)).astype(float)])
    rb = resid(np.argsort(np.argsort(b)).astype(float), [np.argsort(np.argsort(c)).astype(float)])
    return float(np.corrcoef(ra, rb)[0, 1])

# ---------- common residual: log U - fit on log p, loglog p (p = 1 mod 4) -------------
m = P1 & (U > 0)
y = np.log(U[m]); X = [np.log(p[m].astype(float)), np.log(np.log(p[m].astype(float)))]
R_U = resid(y, X)                       # residual log U (after log p, loglog p)
Ufull = np.full(len(p), np.nan); Ufull[m] = R_U
u_norm = np.log(U[m] / np.log(p[m].astype(float)) ** 2)   # log(U/log^2 p)
u_norm3 = np.log(U[m] / np.log(p[m].astype(float)) ** 3)

# ---------- Z0697: partial corr of U with least primitive root given least QNR --------
mm = m & np.isfinite(lqnr) & np.isfinite(g)
res['Z0697'] = dict(
    rho_U_g=sp(U[mm], g[mm]), rho_U_lqnr=sp(U[mm], lqnr[mm]), rho_U_ord2frac=sp(U[mm], (o2[mm] / (p[mm] - 1))),
    partial_U_g_given_lqnr=partial_sp(U[mm], g[mm], lqnr[mm]),
    partial_U_ord2frac_given_lqnr=partial_sp(U[mm], o2[mm] / (p[mm] - 1), lqnr[mm]),
    n=int(mm.sum()))

# ---------- Z0700: regulator / class number vs U ----------
mr = m & np.isfinite(Rreal)
res['Z0700'] = dict(n=int(mr.sum()), rho_U_logeps=sp(U[mr], Rreal[mr]), rho_U_h=sp(U[mr], hreal[mr]),
                    rho_U_L1=sp(U[mr], L1r[mr]), rho_U_logeps_over_sqrtp=sp(U[mr], Rreal[mr] / np.sqrt(p[mr])),
                    rho_h_logeps=sp(hreal[mr], Rreal[mr]))
# CF period of sqrt(p) (p = 1 mod 4 primes)
def cfperiod(n):
    a0 = math.isqrt(n); m_, d, a = 0, 1, a0; per = 0
    while True:
        m_ = d * a - m_; d = (n - m_ * m_) // d; a = (a0 + m_) // d; per += 1
        if a == 2 * a0: break
    return per
idx = np.where(m)[0]
CF = np.full(len(p), np.nan)
for i in idx: CF[i] = cfperiod(int(p[i]))
res['Z0700']['rho_U_cfperiod'] = sp(U[m], CF[m])
res['Z0700']['rho_U_cfperiod_resid'] = sp(R_U, resid(CF[m], [lp[m]]))
res['Z0904'] = dict(rho_U_cf=sp(U[m], CF[m]), rho_L1_cf=sp(L1r[m], CF[m]), rho_logeps_cf=sp(Rreal[m], CF[m]))
hard = {193: 'hard', 241: 'hard', 1201: 'hard', 2521: 'hard', 3361: 'hard', 66529: 'hard', 12601: 'hard', 21169: 'hard', 577: 'R0', 409: 'R0'}
for q in (193, 2521, 66529, 12601, 1201, 3361, 21169, 577, 409, 241, 5569, 9601, 83449):
    if q <= 199999 and q % 4 == 1:
        i = np.where(p == q)[0][0]
        res['Z0904'].setdefault('quantiles', {})[str(q)] = dict(
            CF=float(CF[i]), CF_quantile=float((CF[m] < CF[i]).mean()), L1_quantile=float((L1r[m] < L1r[i]).mean()),
            U_quantile=float((U[m] < U[i]).mean()), logeps_quantile=float((Rreal[m] < Rreal[i]).mean()))

# ---------- Z0717: maxx - p/4 ----------
mx = (mod4 == 1) & (p > 100)
res['Z0717'] = dict(max_ratio=float(np.max(maxx[mx] / p[mx])), frac_le_3over4=float((maxx[mx] <= 0.75 * p[mx]).mean()),
                    rho_excess_lqnr=sp((maxx[mx] - p[mx] / 4) / p[mx], lqnr[mx]),
                    excess_over_p_mean=float(np.mean((maxx[mx] - p[mx] / 4) / p[mx])))

# ---------- Z0719 / Z0816 : mean residual by p mod 840 ----------
pm = p.astype(int)
meanres = {}
for c in (1, 121, 169, 289, 361, 529, 481, 601, 649, 241, 557, 277, 653, 53, 317):
    s = m & (pm % 840 == c) & (p > 100)
    if s.sum() > 0:
        meanres[c] = dict(n=int(s.sum()), mean_logUnorm=float(u_norm[(pm[m] % 840 == c) & (p[m] > 100)].mean()))
res['Z0719_mean_logU_over_log2'] = meanres
mres = {}
for c in range(1, 841, 4):
    s = m & (pm % 840 == c) & (p > 100)
    if s.sum() >= 40: mres[c] = float(u_norm[(pm[m] % 840 == c) & (p[m] > 100)].mean())
ranked = sorted(mres.items(), key=lambda kv: kv[1])
res['Z0719_lowest_classes'] = ranked[:10]
res['Z0719_highest_classes'] = ranked[-5:]
res['Z0719_nclasses_with_n40'] = len(mres)
# residual-based ranking (after log p, loglog p) for the six Mordell classes
mm2 = m & (p > 100)
r_on = R_U[(pm[m] > 0) & (p[m] > 100)]
means_resid = {c: float(R_U[(pm[m] % 840 == c) & (p[m] > 100)].mean()) for c in (1, 121, 169, 289, 361, 529)}
res['Z0719_resid_means_six'] = means_resid
res['Z0816'] = dict(rho_resid_p_mod5=sp(R_U, (pm[m] % 5).astype(float)), rho_resid_p_mod7=sp(R_U, (pm[m] % 7).astype(float)),
                    rho_resid_leg5=sp(R_U, leg[5][m]), rho_resid_leg7=sp(R_U, leg[7][m]))

# ---------- Z0722 / Z0885 / Z0929: hardest primes ----------
order = np.argsort(u_norm3)
top = [int(p[m][i]) for i in order[:30]]
res['Z0722_hardest30_U_over_log2'] = [int(p[m][i]) for i in np.argsort(u_norm)[:30]]
res['Z0722_hardest30_mod24_all1'] = all(q % 24 == 1 for q in res['Z0722_hardest30_U_over_log2'])
res['Z0885_hardest10_U_over_log3'] = [(int(p[m][i]), round(float(np.exp(u_norm3[i])), 4)) for i in order[:10]]
res['Z0885_U_over_log3_2521'] = float(U[p == 2521][0] / math.log(2521) ** 3)
res['Z0885_rank_2521_by_U_over_log3'] = int(np.where(p[m][order] == 2521)[0][0]) + 1

# ---------- Z0807 / Z0882 / Z0947 : normalisations and dyadic medians ----------
dy = {}
for lo in [10**3, 10**4, 10**5]:
    s = m & (p >= lo) & (p < 10 * lo)
    dy[f'[{lo},{10*lo})'] = dict(n=int(s.sum()),
        median_U_over_log2=float(np.median(U[s] / np.log(p[s].astype(float)) ** 2)),
        median_U_over_log3=float(np.median(U[s] / np.log(p[s].astype(float)) ** 3)),
        min_U_over_log3=float(np.min(U[s] / np.log(p[s].astype(float)) ** 3)),
        argmin_p=int(p[s][np.argmin(U[s] / np.log(p[s].astype(float)) ** 3)]))
res['Z0807_dyadic'] = dy
# ET ordered sums (all primes incl. 3 mod 4? ET: all p), reproduce Z0947 ratios
pall = (p > 2)
cum = []
for N in [10**3, 10**4, 3 * 10**4, 10**5, 2 * 10**5 - 1]:
    s = (p <= N) & (p > 2) & (U > 0)
    S = float(U[s].sum())
    cum.append(dict(N=N, ratio_NlogN2=S / (N * math.log(N) ** 2), ratio_NlogN2_llog=S / (N * math.log(N) ** 2 * math.log(math.log(N)))))
res['Z0947'] = cum
# Z0882 / Z0885 windows
def window_stats(fn):
    W = np.loadtxt(fn, dtype=np.int64)
    W = W[W[:, 0] % 4 == 1]
    lpp = np.log(W[:, 0].astype(float))
    return dict(n=len(W), median_U_log2=float(np.median(W[:, 1] / lpp ** 2)), min_U_log2=float(np.min(W[:, 1] / lpp ** 2)),
                median_U_log3=float(np.median(W[:, 1] / lpp ** 3)), min_U_log3=float(np.min(W[:, 1] / lpp ** 3)),
                argmin_log3=int(W[np.argmin(W[:, 1] / lpp ** 3), 0]))
res['Z0882_windows'] = {'1e6': window_stats('data/z52b/raw/pr_1e6_window.txt'), '1e7': window_stats('data/z52b/raw/pr_1e7_window.txt')}
res['Z0929_decade_minima_U_over_log3'] = {k: v['min_U_over_log3'] for k, v in dy.items()}

# ---------- Z0841 / Z0880 / Z0911 : Type I / II split ----------
mt = m & (k1 + k2 > 0)
ratio = k1[mt] / (k1[mt] + k2[mt])
res['Z0841'] = dict(mean_share_mod8_1=float(ratio[(pm[mt] % 8 == 1)].mean()), mean_share_mod8_5=float(ratio[(pm[mt] % 8 == 5)].mean()),
                    mean_share_mod24={int(c): round(float(ratio[pm[mt] % 24 == c].mean()), 4) for c in (1, 13, 17, 5, 9, 21)},
                    mean_k1_over_k2=float(np.mean(k1[mt] / k2[mt])), median_k1_over_k2=float(np.median(k1[mt] / k2[mt])))
# share vs log L1
Lm = mt & np.isfinite(L1r)
fit = np.polyfit(np.log(L1r[Lm]), k1[Lm] / (k1[Lm] + k2[Lm]), 1)
res['Z0880'] = dict(n=int(Lm.sum()), slope_share_on_logL1=float(fit[0]), intercept=float(fit[1]),
                    rho_share_logL1=sp(k1[Lm] / (k1[Lm] + k2[Lm]), np.log(L1r[Lm])),
                    rho_logk1_logL1=sp(k1[Lm], L1r[Lm]), rho_logk2_logL1=sp(k2[Lm], L1r[Lm]))
# power-law exponent of k1 and k2 on L1
def loglog_slope(cnt):
    s = Lm & (cnt > 0)
    X = np.column_stack([np.ones(s.sum()), np.log(L1r[s]), np.log(lp[s])])
    return float(np.linalg.lstsq(X, np.log(cnt[s]), rcond=None)[0][1])
res['Z0880']['slope_logk1_logL1_with_logp'] = loglog_slope(k1)
res['Z0880']['slope_logk2_logL1_with_logp'] = loglog_slope(k2)
res['Z0880']['slope_logU_logL1_with_logp'] = loglog_slope(U)
mk = m & (k1 > 0) & (k2 > 0)
lk1 = resid(np.log(k1[mk]), [lp[mk], np.log(np.log(p[mk].astype(float)))])
lk2 = resid(np.log(k2[mk]), [lp[mk], np.log(np.log(p[mk].astype(float)))])
res['Z0911'] = dict(n=int(mk.sum()), rho_resid_logk1_logk2=float(np.corrcoef(lk1, lk2)[0, 1]),
                    rho_logk1_logk2_raw=sp(k1[mk], k2[mk]))
q5k1 = np.quantile(lk1, 0.05); q5k2 = np.quantile(lk2, 0.05)
both = int(((lk1 < q5k1) & (lk2 < q5k2)).sum())
res['Z0911']['both_below_5pct'] = both
res['Z0911']['expected_indep'] = round(len(lk1) * 0.05 * 0.05, 2)
# partial after chi_p Euler product (per-q Legendre features q<=47 stored only for 2,3,5,7 -> use pari below)

# ---------- Z0908: n mod 840 explains log U variance (all n <= 30000 from f4) ----------
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
nn = F[:, 0]; UU = F[:, 1]
s = (UU > 0) & (nn >= 1000)
X0 = [np.log(nn[s].astype(float)), np.log(np.log(nn[s].astype(float)))]
rr = resid(np.log(UU[s].astype(float)), X0)
tot = rr.var()
def ve(mod):
    means = {}
    cls = nn[s] % mod
    out = np.zeros_like(rr)
    for c in np.unique(cls):
        mk_ = cls == c; out[mk_] = rr[mk_].mean()
    return float(1 - (rr - out).var() / tot)
res['Z0908'] = {str(mo): round(ve(mo), 3) for mo in (2, 4, 12, 24, 30, 840)}
res['Z0908']['note'] = 'n in [1000,30000], UU>0, residual of log U after log n, loglog n; variance explained by class mod q'

# ---------- Z0834 / Z0813 / Z0835 : 2-adic depth / Proth primes ----------
v2 = np.array([0 if x % 2 else int(math.log2(x & -x)) for x in (p - 1)])
def vp(x, q):
    c = 0
    while x % q == 0: x //= q; c += 1
    return c
v3 = np.array([vp(int(x), 3) for x in (p - 1)]); v5 = np.array([vp(int(x), 5) for x in (p - 1)])
resU = R_U
mm3 = m
r16 = resid(np.log(U[mm3]), [lp[mm3], np.log(np.log(p[mm3].astype(float))), np.log(np.abs(L1r[mm3]))]) if False else None
X3 = [np.log(p[mm3].astype(float)), np.log(np.log(p[mm3].astype(float))), np.log(L1r[mm3])]
rr3 = resid(np.log(U[mm3]), X3)
pm3 = pm[mm3]
d16 = rr3[(pm3 % 16 == 1)].mean() - rr3[(pm3 % 16 == 9)].mean()
d32 = rr3[(pm3 % 32 == 1)].mean() - rr3[(pm3 % 32 == 17)].mean()
n16 = (int((pm3 % 16 == 1).sum()), int((pm3 % 16 == 9).sum()))
res['Z0835'] = dict(delta_1mod16_minus_9mod16=float(d16), delta_1mod32_minus_17mod32=float(d32), n16=n16,
                    delta_1mod16_minus_9mod16_at_p_gt_1e4=float(rr3[(pm3 % 16 == 1) & (p[mm3] > 1e4)].mean() - rr3[(pm3 % 16 == 9) & (p[mm3] > 1e4)].mean()))
# regression of residual on v2, v3, v5 with L1 controls
Xv = [np.log(p[mm3].astype(float)), np.log(np.log(p[mm3].astype(float))), np.log(L1r[mm3]), v2[mm3].astype(float), v3[mm3].astype(float), v5[mm3].astype(float)]
rr4 = resid(np.log(U[mm3]), Xv)
Xb = np.column_stack([np.ones(mm3.sum())] + [x for x in Xv])
beta = np.linalg.lstsq(Xb, np.log(U[mm3]), rcond=None)[0]
res['Z0834'] = dict(coef_v2=float(beta[4]), coef_v3=float(beta[5]), coef_v5=float(beta[6]), coef_logL1=float(beta[3]))
# Proth primes
proth = {}
for q in (65537, 257, 17, 786433, 3 * 2**6 + 1, 97, 769):
    if q <= 199999:
        i = np.where(p == q)[0]
        if len(i):
            i = i[0]; lpq = math.log(q)
            proth[str(q)] = dict(U=float(U[i]), U_over_log2=float(U[i] / lpq ** 2), U_over_log3=float(U[i] / lpq ** 3),
                                 resid=float(rr3[np.where(np.where(mm3)[0] == i)[0][0]]) if mm3[i] else None)
res['Z0834']['fermat_proth'] = proth
res['Z0813'] = {k: v for k, v in proth.items() if k in ('17', '257', '65537')}

# ---------- Z0807 : fit U/log^3 flatness ----------
res['Z0807_flatness'] = {k: dict(median_U_log3=v['median_U_over_log3'], min_U_log3=v['min_U_over_log3']) for k, v in dy.items()}

# ---------- Z0881 : h(-4p) mod 16 strata (p = 1 mod 8) ----------
s8 = m & (pm % 8 == 1) & (p > 100)
r8 = resid(np.log(U[s8]), [np.log(p[s8].astype(float)), np.log(np.log(p[s8].astype(float)))])
strata = {int(c): float(r8[(h4p[s8] % 16) == c].mean()) for c in (0, 4, 8, 12)}
nst = {int(c): int(((h4p[s8] % 16) == c).sum()) for c in (0, 4, 8, 12)}
kk1 = resid(np.log(k1[s8]), [np.log(p[s8].astype(float)), np.log(np.log(p[s8].astype(float)))])
kk2 = resid(np.log(k2[s8]), [np.log(p[s8].astype(float)), np.log(np.log(p[s8].astype(float)))])
res['Z0881'] = dict(U_resid_by_h4p_mod16=strata, n=nst, maxdiff_U=max(strata.values()) - min(strata.values()),
                    k1_resid_by_h4p_mod16={int(c): float(kk1[(h4p[s8] % 16) == c].mean()) for c in (0, 4, 8, 12)},
                    k2_resid_by_h4p_mod16={int(c): float(kk2[(h4p[s8] % 16) == c].mean()) for c in (0, 4, 8, 12)})
res['Z0881']['maxdiff_k1'] = max(res['Z0881']['k1_resid_by_h4p_mod16'].values()) - min(res['Z0881']['k1_resid_by_h4p_mod16'].values())

# ---------- Z0907 : small h(-4p)/sqrt p primes: k1 normality ----------
hq = h4p / np.sqrt(p)
sm = np.where(mm3 & np.isfinite(hq))[0]
order_h = sm[np.argsort(hq[sm])][:20]
rk1 = resid(np.log(k1[mm3]), [np.log(p[mm3].astype(float)), np.log(np.log(p[mm3].astype(float)))])
pos = {int(i): j for j, i in enumerate(np.where(mm3)[0])}
res['Z0907'] = dict(smallest_h4p_over_sqrtp=[(int(p[i]), round(float(hq[i]), 3), round(float(np.mean(rk1 < rk1[pos[int(i)]])), 3),
                                              round(float(rk1[pos[int(i)]]), 3)) for i in order_h[:10]],
                    mean_k1_resid_bottom20=float(np.mean([rk1[pos[int(i)]] for i in order_h])),
                    mean_k1_resid_all=float(rk1.mean()))

# ---------- Z0820 / Z0826 / Z0827 : p = 3 mod 4 (chi_{-p}) ----------
m3 = (mod4 == 3) & (p > 100) & (U > 0)
lh = np.log(L1m[m3])
Xp3 = [np.log(p[m3].astype(float)), np.log(np.log(p[m3].astype(float)))]
r3 = resid(np.log(U[m3]), Xp3)
res['Z0820'] = dict(n=int(m3.sum()), rho_U_L1m_3mod4=sp(U[m3], L1m[m3]),
                    rho_resid_logL1m=float(np.corrcoef(resid(np.log(U[m3]), Xp3 + [lh]) if False else r3, resid(lh, Xp3))[0, 1]),
                    slope_logU_on_logLm=float(np.polyfit(lh, np.log(U[m3]) - np.log(np.log(p[m3].astype(float))) * 0, 1)[0]))
m1 = m & np.isfinite(L1r) & (p > 100)
res['Z0820']['slope_p1_mod4_logU_on_logL1real'] = float(np.polyfit(np.log(L1r[m1]), np.log(U[m1]), 1)[0])
res['Z0827'] = dict(slope_logU_on_logL1m_p3mod4=float(np.polyfit(lh, np.log(U[m3]), 1)[0]),
                    slope_logU_on_logL1real_p1mod4=float(np.polyfit(np.log(L1r[m1]), np.log(U[m1]), 1)[0]),
                    residual_slope_p3_with_logp=float(np.linalg.lstsq(np.column_stack([np.ones(m3.sum()), lh, np.log(p[m3].astype(float))]), np.log(U[m3]), rcond=None)[0][1]),
                    residual_slope_p1_with_logp=float(np.linalg.lstsq(np.column_stack([np.ones(m1.sum()), np.log(L1r[m1]), np.log(p[m1].astype(float))]), np.log(U[m1]), rcond=None)[0][1]))

# ---------- Z0802-Z0804 : quantiles of least QNR, L1, h(-4p) at R-zeros ----------
Rz = [409, 577, 5569, 9601, 23929, 83449, 102001]
quant = {}
for q in Rz:
    if q <= 199999:
        i = np.where(p == q)[0][0]
        s = m & (np.abs(lp - lp[i]) < 0.1)
        quant[str(q)] = dict(leastQNR=float(lqnr[i]), qnr_quantile_sameSize=float(np.mean(lqnr[s] < lqnr[i])),
                             L1_quantile_sameSize=float(np.mean(L1r[s] < L1r[i])),
                             h4p_over_sqrtp=float(h4p[i] / math.sqrt(q)), h_quantile_sameSize_mod8=float(np.mean((h4p[s & (pm % 8 == q % 8)] / np.sqrt(p[s & (pm % 8 == q % 8)])) < h4p[i] / math.sqrt(q))))
res['Z0802_Z0803_Rzeros'] = quant
# Type-A / hardness primes quantiles (Z0804)
ta = {}
for q in (193, 2521, 66529, 12601, 1201, 3361):
    i = np.where(p == q)[0][0]
    s = m & (np.abs(lp - lp[i]) < 0.1)
    ta[str(q)] = dict(leastQNR=float(lqnr[i]), L1_quantile=float(np.mean(L1r[s] < L1r[i])),
                      h_quantile=float(np.mean((h4p[s & (pm % 8 == q % 8)] / np.sqrt(p[s & (pm % 8 == q % 8)])) < h4p[i] / math.sqrt(q))))
res['Z0804'] = ta

# ---------- Z0805 : joint of two lines ----------
res['Z0805'] = dict(rho_logL1real_logL1m4p_all=sp(np.log(L1r[m]), np.log(L1m[m])))
# ---------- Z0841 bis, Z0853 etc in other script ----------

# ---------- Z0808 : variance after chi effects & shift-divisor richness ----------
tau = np.zeros(200100 + 50, dtype=np.int64)
ss = np.arange(1, tau.size)
for d in range(1, tau.size):
    tau[d::d] += 1
s = m & (p > 100)
X_base = [np.log(p[s].astype(float)), np.log(np.log(p[s].astype(float)))]
lu = np.log(U[s])
rA = resid(lu, X_base + [np.log(L1r[s])])
rB = resid(lu, X_base + [np.log(L1r[s]), np.log(tau[(p[s] + 3) // 4]), np.log(tau[p[s] - 1])])
res['Z0808'] = dict(var_resid_base=float(rA.var()), var_resid_with_tau=float(rB.var()),
                    frac_reduction=float(1 - rB.var() / rA.var()), var_logU=float(lu.var()),
                    R2_base=float(1 - rA.var() / lu.var()), R2_with_tau=float(1 - rB.var() / lu.var()))

# ---------- Z0830 : shift spectrum stratified by p mod 3 ----------
sh = {}
for sft in range(1, 41):
    ss_ = m & (p > 100)
    tv = np.log(tau[p[ss_] + sft])
    yv = np.log(U[ss_]) - resid(np.log(U[ss_]), [np.log(p[ss_].astype(float))]) + 0  # placeholder
    yv = resid(np.log(U[ss_]), [np.log(p[ss_].astype(float)), np.log(np.log(p[ss_].astype(float)))])
    out = []
    for c in (1, 2):
        sc = (p[ss_] % 3 == c)
        out.append(round(sp(yv[sc], tv[sc]), 3))
    sh[sft] = dict(all=round(sp(yv, tv), 3), p1mod3=out[0], p2mod3=out[1])
res['Z0830'] = {str(k): v for k, v in sh.items() if k in (1, 2, 3, 4, 5, 7, 9, 11, 13, 17, 19, 23)}
res['Z0830_s3'] = sh[3]

# ---------- Z0853 : slice events E_C = not F_C (divisor of 4Cp+1 that is = -1 mod 4C) ----------
# computed in separate pass (see z52d_p2_TO3_slices.py)

json.dump(res, open(OUT, 'w'), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
for k, v in res.items():
    s_ = json.dumps(v, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
    print(k, s_[:600])
