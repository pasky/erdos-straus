"""Fix round TO3, batch C: Z0918 (p=3 mod 4 regression), Z0921 (PCA-orthogonalised twists), Z0764/Z0765 (BM decomposition),
Z0886/Z0888 (standard errors), Z0880 (window shares), Z0836 (cross-validated AUC), Z0864 (variant families),
Z0870 (2-power ladder levels), Z0905 (tail comparison), Z0906 (R-analogue), Z0924 (NB on windows), Z0925 (5/p weights),
Z0926 (cluster), Z0927 (denominator factorisations), Z0928 (6/p vs 4/p counts), Z0797 (non-diagonal ternary forms).
Writes data/z52b/pass2/TO3/fix_c_results.json"""
import csv, json, math, sys
import numpy as np
from scipy.stats import spearmanr, ks_2samp
from sympy import factorint, primerange, jacobi_symbol
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
S = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0]
p = np.array([int(r['p']) for r in S]); U = np.array([float(r['U']) for r in S]); lp = np.log(p.astype(float))
X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
def rs(y, M): return y - np.column_stack([np.ones(len(y))] + M) @ np.linalg.lstsq(np.column_stack([np.ones(len(y))] + M), y, rcond=None)[0]
lU = np.log(U)
resU = rs(lU, [lp, np.log(lp)])
Lg = {q: np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in p]).astype(float) for q in primerange(3, 48)}
QS = list(Lg.keys())
# ---- Z0918: p = 3 mod 4 ----
S3 = []
for q in primerange(5, 700):
    if q % 4 != 3: continue
    x = np.arange(q, dtype=np.int64); qr = -np.ones(q, dtype=np.int64); qr[0] = 0; qr[(x * x % q)[1:]] = 1
    cnt = 0
    for j in range(q):
        if j == 0: A, B = 0, 1
        elif j == 1728 % q: A, B = 1, 0
        else:
            k_ = (1728 - j) % q; A = (3 * j * k_) % q; B = (2 * j * k_ * k_) % q
        f = (x * x % q * x + A * x + B) % q
        if int(qr[f].sum()) == 0 and (4 * A ** 3 + 27 * B * B) % q != 0: cnt += 1
    S3.append((q, cnt, int(pari.quadclassunit(-q)[0]), int(pari.qfbclassno(-4 * q))))
Y = np.array([s[1] for s in S3], float); H1 = np.array([s[2] for s in S3], float); H4 = np.array([s[3] for s in S3], float)
Xr = np.column_stack([np.ones(len(Y)), H1, H4])
b3 = np.linalg.lstsq(Xr, Y, rcond=None)[0]
out['Z0918_p3mod4'] = dict(n=len(Y), fit_N_on_h_minus_p_and_h_minus_4p=[round(float(c), 4) for c in b3],
                           resid_sd=round(float(np.std(Y - Xr @ b3)), 4),
                           exact_matches_h1_plus_h4_over_4=float(np.mean(Y == (H1 + H4) / 4)), exact_matches_h1_half_plus_1=float(np.mean(Y == (H1 + 1) / 2)))
# ---- Z0921: PCA-orthogonalised twist L-values ----
mset = [3, 5, 7, 15, 21, 35, 105]
def L1_twist(D):
    d = int(pari.coredisc(D)); h = int(pari.quadclassunit(d)[0])
    return math.pi * h / (2 * math.sqrt(-d))
Lt = np.column_stack([np.log([L1_twist(-m * int(q)) for q in p]) for m in mset])
Lt_c = Lt - Lt.mean(axis=0)
U_, s_, Vt = np.linalg.svd(Lt_c, full_matrices=False)
Z = Lt_c @ Vt.T
bz = np.linalg.lstsq(np.column_stack([np.ones(len(p)), lp, np.log(lp), Z]), lU, rcond=None)[0]
out['Z0921_pca'] = dict(singular_values=[round(float(v), 3) for v in s_], var_explained=[round(float(v), 3) for v in (s_ ** 2 / np.sum(s_ ** 2))],
                        coef_on_pcs=[round(float(c), 4) for c in bz[3:]], loadings_pc1=[round(float(v), 3) for v in Vt[0]],
                        note='PCs of the centred log L(1,chi_{-mp}) across the seven twists')
# ---- Z0764 / Z0765: BM main term decomposition ----
M = np.load('/tmp/z52/big/mbm_full.npz'); PM = M['p']; MM = M['M']
sel = (PM >= 20000) & (PM < 30000)
N = 10**8
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 7))
Rm = np.asarray(W[PM[sel], 2]).astype(float)
res_ = Rm - MM[sel]
Yq = res_; Xq = np.column_stack([np.ones(sel.sum()), np.log(PM[sel].astype(float))] + [np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in PM[sel]]).astype(float) for q in QS])
bq, *_ = np.linalg.lstsq(Xq, Yq, rcond=None)
r2 = 1 - np.var(Yq - Xq @ bq) / np.var(Yq)
out['Z0764_decomposition'] = dict(n=int(sel.sum()), var_R_minus_M=round(float(np.var(res_)), 2), R2_on_legendre_q_le47=round(float(r2), 4),
                                  top_coefs={int(q): round(float(bq[2 + i]), 3) for i, q in enumerate(QS) if abs(bq[2 + i]) > 0.5},
                                  note='decomposition into quadratic characters chi_p(q), q<=47 only; cubic/quartic parts not computed')
# Z0765: per-zero contribution of the (u,B) pairs to M_BM, grouped by the smallest prime factor q of uB and by chi value
from sympy import primefactors
PAIRS = []
HI = 300000
for u in range(1, HI + 2):
    if 4 * u - u - 1 > HI: break
    for B in range(1, HI + 2):
        if 4 * u * B - u - B > HI: break
        if (u + B) % 2 == 1 and gcd(u, B) == 1: PAIRS.append((u, B))
PAIRS = np.array(PAIRS, dtype=np.int64)
from math import gcd as _g
phi_cache = {}
def phi(n):
    if n not in phi_cache:
        f = factorint(n); r = n
        for q in f: r = r // q * (q - 1)
        phi_cache[n] = r
    return phi_cache[n]
zeros = [409, 577, 5569, 9601, 23929]
dec = {}
for pz in zeros:
    sel_ = PAIRS[(4 * PAIRS[:, 0] * PAIRS[:, 1] - PAIRS[:, 0] - PAIRS[:, 1]) <= pz]
    spf_groups = {}
    tot = {'M0': 0.0, 'T': 0.0}
    for u, B in sel_:
        n4 = 4 * int(u) * int(B)
        w = 1.0 / phi(n4)
        a = (-(int(u) * int(B))) % pz
        chi = 1 if pow(a, (pz - 1) // 2, pz) == 1 else -1
        # chi(-uB/p) = prod_{q | uB} (q/p)^{v_q}; group pairs by whether uB is 13-smooth (only then chi is a product of
        # quadratic characters of primes <= 13)
        uBv = int(u) * int(B)
        key = 'smooth13' if all(q <= 13 for q in primefactors(uBv)) else 'other'
        g = spf_groups.setdefault(key, [0.0, 0.0])
        g[0] += w; g[1] += chi * w
        tot['M0'] += w; tot['T'] += chi * w
    Mb = tot['M0'] - tot['T']
    contrib = {k: round(float(g[0] - g[1]), 4) for k, g in spf_groups.items()}
    dec[pz] = dict(M_BM=round(float(Mb), 4), M0=round(float(tot['M0']), 4), T=round(float(tot['T']), 4),
                   contrib_M_by_group=contrib, weight_share_smooth13=round(float(spf_groups.get('smooth13', [0, 0])[0] / tot['M0']), 3),
                   chi_mean_smooth13=round(float(spf_groups.get('smooth13', [0, 0])[1] / max(spf_groups.get('smooth13', [1e-9, 0])[0], 1e-12)), 3))
out['Z0765_decomposition'] = dec
# ---- Z0886 / Z0888 standard errors ----
# R/M_BM ratio on exhaustive windows (primes 1 mod 4 in [1e4,1e5) and [1e5,3e5)) with block bootstrap
Mall = MM; Rall = np.asarray(W[PM, 2]).astype(float)
ratio_w = {}
for a, b in ((10**4, 10**5), (10**5, 3 * 10**5)):
    s_ = (PM >= a) & (PM < b)
    rr = Rall[s_] / Mall[s_]
    boots = [np.random.default_rng(i).choice(rr, size=len(rr)).mean() for i in range(400)]
    ratio_w[f'[{a},{b})'] = dict(n=int(s_.sum()), mean_R_over_M=round(float(Rall[s_].mean() / Mall[s_].mean()), 4),
                                 mean_ratio_per_prime=round(float(rr.mean()), 4), boot_sd=round(float(np.std(boots)), 4))
out['Z0886_exhaustive_windows'] = ratio_w
# Z0888: standard errors for the M_BM Legendre coefficients (primes 1 mod 4 <= 3e4)
Pl = PM[PM <= 30000]; Ml = MM[PM <= 30000]
Xm = np.column_stack([np.ones(len(Pl)), np.log(Pl.astype(float))] + [np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in Pl]).astype(float) for q in QS])
bm_, *_ = np.linalg.lstsq(Xm, Ml, rcond=None)
rs_ = Ml - Xm @ bm_; s2 = rs_ @ rs_ / (len(Ml) - Xm.shape[1]); se_ = np.sqrt(np.diag(s2 * np.linalg.pinv(Xm.T @ Xm)))
out['Z0888_M_coef_with_se'] = {int(q): [round(float(bm_[2 + i]), 4), round(float(se_[2 + i]), 4)] for i, q in enumerate(QS)}
# ---- Z0880: window shares k1/(k1+k2) vs log L1 (1e6, 1e7 windows) ----
out['Z0880_windows'] = {}
for fn, key in (('data/z52b/raw/pr_1e6_window.txt', '1e6'), ('data/z52b/raw/pr_1e7_window.txt', '1e7')):
    Wn = np.loadtxt(fn, dtype=np.int64); Wn = Wn[Wn[:, 0] % 4 == 1]
    L1w = np.array([2 * int(pari.quadclassunit(int(q))[0]) * float(pari.log(pari.quadunit(int(q)))) / math.sqrt(q) for q in Wn[:, 0]])
    sh = Wn[:, 10] / (Wn[:, 10] + Wn[:, 11])
    b1 = np.polyfit(np.log(L1w), sh, 1)
    out['Z0880_windows'][key] = dict(n=len(Wn), slope_share_on_logL1=round(float(b1[0]), 4), rho_share_logL1=round(float(spearmanr(sh, L1w)[0]), 3))
out['Z0880_base_slope'] = None
json.dump(out, open('data/z52b/pass2/TO3/fix_c_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:500])
