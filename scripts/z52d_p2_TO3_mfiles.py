"""Pass-2 TO3: numerator-family checks from the repo's count outputs (data/z52b/raw/m<k>_pr1e5.txt, m<k>_4000.txt)
and the exists-scan (scripts/z52d_p2_TO3_exists.c). Writes data/z52b/pass2/TO3/mfiles_results.json."""
import numpy as np, json, math, subprocess, os
from scipy.stats import spearmanr
R = 'data/z52b/raw/'
out = {}
def load(k, kind='pr1e5'):
    fn = R + f'm{k}_{kind}.txt'
    return np.loadtxt(fn, dtype=np.int64)
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
# ---- Z0733: failing primes in (m^2, 2m^2) for m = 20..48 ----
cnt = {}
for m in range(20, 49):
    A = load(m)
    s = (A[:, 0] > m * m) & (A[:, 0] < 2 * m * m)
    cnt[m] = int(((A[s, 1]) == 0).sum())
out['Z0733_fail_counts_m20_48'] = cnt
out['Z0733_all_m_have_failure_in_window'] = all(v > 0 for v in cnt.values())
# ---- Z0735: 9/n exceptions (n <= 4000, all n) ----
A9 = load(9, '4000')
out['Z0735_9n_fail_all_n_le4000'] = [int(x) for x in A9[A9[:, 1] == 0, 0]]
A9p = load(9)
out['Z0735_9n_fail_primes_le1e5'] = [int(x) for x in A9p[A9p[:, 1] == 0, 0]]
# ---- Z0724: 5/n, 6/n ----
A5 = load(5); A6 = load(6); A5n = load(5, '4000'); A6n = load(6, '4000')
out['Z0724'] = dict(m5_fail_primes=[int(x) for x in A5[A5[:, 1] == 0, 0]], m6_fail_primes=[int(x) for x in A6[A6[:, 1] == 0, 0]],
                    m5_fail_n_le4000=[int(x) for x in A5n[A5n[:, 1] == 0, 0]], m6_fail_n_le4000=[int(x) for x in A6n[A6n[:, 1] == 0, 0]],
                    min_U5_primes=int(A5[:, 1].min()), min_U6_primes=int(A6[:, 1].min()))
# joint: U4 (base table) vs U5 among primes 1 mod 4
base = {}
import csv
for r in csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'):
    base[int(r['p'])] = int(r['U'])
def resid_of(p_arr, u_arr):
    lp = np.log(p_arr.astype(float)); y = np.log(u_arr.astype(float))
    X = np.column_stack([np.ones_like(lp), lp, np.log(lp)])
    return y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
fam = {}
for k in range(4, 14):
    if k == 4:
        p_arr = np.array([p for p in base if p <= 99999 and p > 2 and p % 4 == 1]); u_arr = np.array([base[p] for p in p_arr])
    else:
        A = load(k); mk = A[:, 0] > 2
        p_arr = A[mk, 0]; u_arr = A[mk, 1]
    m_ = u_arr > 0
    fam[k] = dict(p=p_arr[m_], u=u_arr[m_])
common = set(fam[4]['p'].tolist())
for k in range(5, 14):
    common &= set(fam[k]['p'].tolist())
common = np.array(sorted(common))
R4 = {}
for k in range(4, 14):
    d = dict(zip(fam[k]['p'].tolist(), fam[k]['u'].tolist()))
    u = np.array([d[p] for p in common])
    R4[k] = resid_of(common, u)
mat = np.corrcoef(np.vstack([R4[k] for k in range(4, 14)]))
out['Z0926_resid_corr_matrix_m4_13_primes_common'] = dict(n=len(common), ks=list(range(4, 14)), M=np.round(mat, 3).tolist())
out['Z0926_resid_corr_U4_U5'] = float(mat[0, 1]); out['Z0926_resid_corr_U4_U6'] = float(mat[0, 2])
out['Z0926_resid_corr_U4_U7'] = float(mat[0, 3]); out['Z0926_resid_corr_U4_U9'] = float(mat[0, 5]); out['Z0926_resid_corr_U4_U13'] = float(mat[0, 9])
# hardest primes for 5 (residual)
i5 = np.argsort(R4[5])[:12]
out['Z0925_hardest5_by_resid'] = [int(common[i]) for i in i5]
out['Z0925_hardest5_mod20'] = {int(common[i]) % 20: 0 for i in i5}
out['Z0925_hardest5_all_1mod20'] = all(int(common[i]) % 20 == 1 for i in i5)
i6 = np.argsort(R4[6])[:12]
out['Z0928_hardest6'] = [int(common[i]) for i in i6]
out['Z0928_hardest6_overlap_with_4_top30'] = sorted(set(int(common[i]) for i in i6) & set(int(common[j]) for j in np.argsort(R4[4])[:30]))
i4 = np.argsort(R4[4])[:30]
out['Z0928_hardest4_top30_overlap_6'] = sorted(set(int(common[i]) for i in i4) & set(int(common[i]) for i in i6))
out['Z0928_rho_U4_U6_residuals'] = float(spearmanr(R4[4], R4[6])[0])
# ---- Z0741: U8 (count of 8/p) vs U4 by p mod 8 and 16 ----
A8 = load(8); d8 = dict(zip(A8[:, 0].tolist(), A8[:, 1].tolist()))
ratio = {}
for c in [1, 5]:
    rs = [d8[p] / base[p] for p in common_primes] if False else None
ratio8 = {}
pl = [p for p in base if p > 100 and p % 4 == 1 and p in d8 and base[p] > 0]
for mod in (8, 16):
    ratio8[mod] = {}
    for c in range(1, mod, 2 if mod == 8 else 2):
        s = [d8[p] / base[p] for p in pl if p % mod == c]
        if len(s) > 20: ratio8[mod][c] = round(float(np.mean(s)), 4)
out['Z0741_mean_U8_over_U4_by_p_mod'] = ratio8
out['Z0741_mean_U8_over_U4_all'] = float(np.mean([d8[p] / base[p] for p in pl]))
out['Z0741_U8_first_values'] = [int(d8[p]) for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43] if p in d8]
out['Z0741_U8_fail_count_le1e5'] = int(sum(1 for p in d8 if d8[p] == 0))
# ---- Z0864 : 241 membership ----
memb = {}
for k in range(8, 49):
    A = load(k); memb[k] = int(A[A[:, 0] == 241, 1][0]) if (A[:, 0] == 241).any() else None
out['Z0864_U_at_241_by_numerator'] = {k: memb[k] for k in memb if memb[k] is not None and memb[k] <= 3}
out['Z0864_fail_last_by_numerator_le1e5'] = {}
for k in (8, 12, 16, 20, 24):
    A = load(k); f = A[A[:, 1] == 0, 0]
    out['Z0864_fail_last_by_numerator_le1e5'][k] = dict(last=int(f.max()) if len(f) else None, n_fail=int(len(f)), has241=bool((f == 241).any()))
json.dump(out, open('data/z52b/pass2/TO3/mfiles_results.json', 'w'), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
for k, v in out.items():
    print(k, json.dumps(v, default=str)[:700])
