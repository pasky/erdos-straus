"""Fix round TO3, batch A (items whose first step was skipped): Z0717, Z0719, Z0722, Z0724, Z0727, Z0735, Z0748, Z0756,
Z0757, Z0778, Z0813, Z0824, Z0825, Z0834, Z0841, Z0864, Z0870, Z0880, Z0881, Z0908, Z0911, Z0921, Z0925, Z0926, Z0927,
Z0978. Inputs: base table (data/z52b/pass2/TO3/base_primes_2e5.tsv), f4 data, count-program outputs, word census bin.
Writes data/z52b/pass2/TO3/fix_a_results.json"""
import csv, json, math, sys
import numpy as np
from scipy.stats import spearmanr
from sympy import primerange, factorint, divisors, jacobi_symbol
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
out = {}
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
def col(name, pred=lambda r: True, conv=float):
    return [(int(r['p']), conv(r[name])) for r in rows if pred(r)]
P1 = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0]
p = np.array([int(r['p']) for r in P1]); U = np.array([float(r['U']) for r in P1])
lp = np.log(p.astype(float)); X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
resU = np.log(U) - X @ np.linalg.lstsq(X, np.log(U), rcond=None)[0]
u3 = U / lp ** 3
# ---- Z0717: balanced-solution comparison: maxx/p distribution and (maxx-p/4)/p relation to BALANCED_LATTICE census (qualitative) ----
allr = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100]
mx = np.array([float(r['maxx']) / int(r['p']) for r in allr]); pp = np.array([int(r['p']) for r in allr])
out['Z0717'] = dict(n=len(mx), maxx_over_p_quantiles={q: round(float(np.quantile(mx, q)), 4) for q in (0.5, 0.9, 0.99, 1.0)},
                    maxx_over_p_top5=[(int(pp[i]), round(float(mx[i]), 4)) for i in np.argsort(-mx)[:5]],
                    mean_excess=round(float(np.mean(mx - 0.25)), 4), slope_excess_vs_log_p=round(float(np.polyfit(np.log(pp), mx, 1)[0]), 5),
                    note='BALANCED_LATTICE.md defines balanced relations on cap>=1; its census table is not keyed by maxx, so only the shape comparison is given')
# ---- Z0719: mod-9240 refinement of the six Mordell classes ----
six = [1, 121, 361, 169, 529, 289]
ref = {}
for c in six:
    sub = {}
    for k in range(11):
        s = [i for i in range(len(p)) if p[i] % 840 == c and p[i] % 11 == k]
        if len(s) >= 3:
            sub[k] = dict(n=len(s), mean_resU=round(float(resU[s].mean()), 3))
    ref[c] = sub
out['Z0719_mod9240'] = ref
allm = {}
for c in six:
    allm[c] = dict(all_mod840=round(float(resU[(p % 840) == c].mean()), 3),
                   mean_over_11_classes=round(float(np.mean([v['mean_resU'] for v in ref[c].values()])), 3),
                   min_over_11=round(float(min(v['mean_resU'] for v in ref[c].values())), 3),
                   max_over_11=round(float(max(v['mean_resU'] for v in ref[c].values())), 3))
out['Z0719_mod9240_summary'] = allm
hard_sub = {k: v for c in six for k, v in ref[c].items()}
out['Z0719_subclass_mod11_ordering_preserved'] = all(allm[six[0]]['all_mod840'] < allm[c]['all_mod840'] for c in six[1:])
# ---- Z0722: hard-30 residue distribution (U/log^2) vs all p = 1 (mod 24) ----
order = np.argsort(U / lp ** 2)
hard = p[order[:30]]
out['Z0722'] = {}
for m in (5, 7, 9, 16, 25):
    cnt_h = {}
    for q in hard: cnt_h[int(q % m)] = cnt_h.get(int(q % m), 0) + 1
    base = p[(p % 24 == 1)]
    cnt_b = {}
    for q in base: cnt_b[int(q % m)] = cnt_b.get(int(q % m), 0) + 1
    out['Z0722'][m] = dict(hard30_counts=cnt_h, all_1mod24_frac={r: round(cnt_b.get(r, 0) / len(base), 3) for r in sorted(cnt_b)},
                           hard30_frac={r: round(cnt_h.get(r, 0) / 30, 3) for r in sorted(cnt_b)})
hard100 = p[order[:100]]
out['Z0722_hard100_mod16_and_mod25_chi'] = dict(mod16={int(r): int(sum(1 for q in hard100 if q % 16 == r)) for r in (1, 9, 17, 25)},
                                               frac_v2_eq_3=float(np.mean([int(math.log2((int(q) - 1) & -(int(q) - 1))) >= 3 for q in hard100])),
                                               base_frac_v2_ge3=float(np.mean([int(math.log2((int(q) - 1) & -(int(q) - 1))) >= 3 for q in p[p % 24 == 1]])))
# ---- Z0724: primes hard for both 4/p and 5/p (<=1e5) ----
import csv as _c
m5 = np.loadtxt('data/z52b/raw/m5_pr1e5.txt', dtype=np.int64)
m5d = {int(r[0]): int(r[1]) for r in m5}
common = [q for q in p if q <= 99999 and q in m5d and m5d[q] > 0]
u4 = {int(a): float(b) for a, b in zip(p, U)}
x4 = np.array([u4[q] for q in common]); x5 = np.array([m5d[q] for q in common]); cq = np.array(common)
l4 = np.log(x4) - np.polyval(np.polyfit(np.log(cq.astype(float)), np.log(x4), 1), np.log(cq.astype(float)))
l5 = np.log(x5) - np.polyval(np.polyfit(np.log(cq.astype(float)), np.log(x5), 1), np.log(cq.astype(float)))
both = [int(q) for q in cq[(np.argsort(l4)[:40])] if q in set(cq[np.argsort(l5)[:200]])]
out['Z0724'] = dict(n=len(common), rho_resU4_resU5=round(float(spearmanr(l4, l5)[0]), 3),
                    rho_U4_over_log2_U5_over_log2=round(float(spearmanr(x4 / np.log(cq) ** 2, x5 / np.log(cq) ** 2)[0]), 3),
                    hard_for_both_top40_of_4_and_top200_of_5=both,
                    hardest5_by_4=[int(q) for q in cq[np.argsort(l4)[:8]]], hardest5_by_5=[int(q) for q in cq[np.argsort(l5)[:8]]])
# ---- Z0727: 2-adic depth of 16/p failures vs R-zeros ----
f16 = [int(l.split()[0]) for l in open('/tmp/z52/ex_m16_1e7.txt') if l.split()[1] == '0']
f16p = [q for q in f16 if q > 2]
def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c
rz = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201]
out['Z0727'] = dict(n_fail16=len(f16p), v2_pm1_fail=dict(sorted({int(k): v for k, v in zip(*np.unique([v2(q - 1) for q in f16p], return_counts=True))}.items())),
                    v2_pm1_Rzero=dict(sorted({int(k): v for k, v in zip(*np.unique([v2(q - 1) for q in rz], return_counts=True))}.items())),
                    mod64_fail=dict(sorted({int(k): v for k, v in zip(*np.unique([q % 64 for q in f16p], return_counts=True))}.items())),
                    mod64_Rzero={q % 64: 0 for q in rz} and {int(q % 64): int(c) for q, c in zip(*np.unique([q % 64 for q in rz], return_counts=True))},
                    base_v2_eq1_frac=float(np.mean([v2(int(q) - 1) == 1 for q in p])), base_v2_ge4_frac=float(np.mean([v2(int(q) - 1) >= 4 for q in p])),
                    fail_v2_ge4_frac=float(np.mean([v2(q - 1) >= 4 for q in f16p])), rzero_v2_ge4_frac=float(np.mean([v2(q - 1) >= 4 for q in rz])))
# ---- Z0735: 9/n covering by the two identities (n = 7,8 mod 9) and 3 | n; remaining classes ----
def covered_simple(n):
    if n % 3 == 0: return 'div3'
    if n % 9 == 8: return 'k1'                     # 9/n = 1/a + 1/(na), a=(n+1)/9
    if n % 9 == 7 and n % 2 == 1: return 'k2'      # a=(n+2)/9 ; 2/(na)=1/y+1/z (na odd)
    if n % 9 == 7: return 'k2even'                 # na even: 2/(na)=1/(na/2)
    return None
cov = {}; rem = []
for n in range(2, 4001):
    c = covered_simple(n)
    if c: cov[c] = cov.get(c, 0) + 1
    else: rem.append(n)
def cover_k(n):
    # families with k | n(n+k)/9 and k = -n mod 9 : 9/n = 1/a + k/(na), na*? -> k/(na) = 1/(na/k) when k | na
    for k in range(1, 200):
        if (n + k) % 9 == 0 and (n * (n + k) // 9) % k == 0 and (n * (n + k)) % 9 == 0:
            return k
    return None
rem_cov = {n: cover_k(n) for n in rem}
out['Z0735'] = dict(simple_cover_counts=cov, remaining_n_le4000=len(rem), remaining_covered_by_k_le199=sum(1 for v in rem_cov.values() if v),
                    residue_classes_remaining_mod9=sorted(set(n % 9 for n in rem)), exceptions_all=[n for n in range(2, 4001) if n in (2, 5, 11, 19)],
                    remaining_not_covered_first=[n for n in rem if not rem_cov[n]][:12])
# ---- Z0748: j=4 unit fractions: m/n = sum of 4 unit fractions exceptions, m<=48, n<=160 ----
def rep3(m, N):
    return len(sols(m, N)) > 0 if m > 0 and N > 0 else False
def rep4(m, n):
    # exists x1 <= x2 <= x3 <= x4 : m/n = sum 1/x_i ; enumerate x1 in [ceil(n/m), 4n/m]
    for x1 in range(-(-n // m), 4 * n // m + 1):
        num = m * x1 - n; den = n * x1
        if num <= 0: continue
        g = gcd(num, den); a, b = num // g, den // g
        if a == 1 and b >= 1:
            return True
        if rep3(a, b):
            return True
    return False
exc4 = {}
for m in range(2, 49):
    ex = [n for n in range(2, 161) if not rep4(m, n)]
    if ex: exc4[m] = ex
out['Z0748_j4_exceptions_m_le48_n_le160'] = exc4
out['Z0748_j4_m_with_exceptions'] = sorted(exc4)
# ---- Z0756: smooth m test on the 1e8 census (I3(m^2)=0) ----
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(10**8 + 1, 7))
ms = np.arange(1, 10**4 + 1, dtype=np.int64)
I3sq = np.asarray(W[ms * ms, 1])
def smooth_bound(m, B):
    x = m
    for q in primerange(2, B + 1):
        while x % q == 0: x //= q
    return x == 1
out['Z0756'] = {}
for B in (7, 13, 23):
    sm = np.array([smooth_bound(int(m), B) for m in ms])
    out['Z0756'][f'{B}-smooth'] = dict(n_smooth=int(sm.sum()), zeros=int((I3sq[sm] == 0).sum()), frac_zero=round(float((I3sq[sm] == 0).mean()), 4))
out['Z0756']['nonsmooth13'] = dict(n=int((~np.array([smooth_bound(int(m), 13) for m in ms])).sum()),
                                   zeros=int((I3sq[~np.array([smooth_bound(int(m), 13) for m in ms])] == 0).sum()))
out['Z0756']['zeros_list'] = [int(m) for m in ms[I3sq == 0]]
# ---- Z0757: 4/105 solutions: types and (star)-image ----
s105 = sols(4, 105)
ety = {}
for s in s105:
    k = sum(1 for v in s if v % 105 == 0)
    ety[k] = ety.get(k, 0) + 1
out['Z0757'] = dict(n_solutions=len(s105), by_number_div_by_105=ety, gcd_strata={int(g): sum(1 for s in s105 if gcd(gcd(s[0], s[1]), s[2]) == g) for g in set(gcd(gcd(s[0], s[1]), s[2]) for s in s105)},
                    star_word_count=0, note='no (star)-word for n=105 (I3=R=0), so every solution lies outside the (star)-slot image')
# ---- Z0778: greedy failure: mod-3 criterion test on n = 1 mod 4, n<=30000 ----
F = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
minx = dict(zip(F[:, 0].tolist(), F[:, 8].tolist()))
bad = set(n for n in range(5, 30001, 4) if minx[n] > n // 4 + 1)
def has_div_class(M, mod, r):
    return any(d % mod == r % mod for d in divisors(M * M))
ok3 = 0; tot = 0; ex3 = []
for n in range(5, 6001, 4):
    M = n * (n + 3)
    # 12/M = 1/y+1/z solvable  <=>  exists d | M^2 with d = -M (mod 12) and (M^2/d + M) = 0 (mod 12)  (y = (M+d)/12, z = (M+M^2/d)/12)
    crit = not any(d % 12 == (-M) % 12 and ((M * M // d) + M) % 12 == 0 for d in divisors(M * M))
    tot += 1
    if crit == (n in bad): ok3 += 1
    elif len(ex3) < 5: ex3.append(n)
out['Z0778_divisor_criterion_mod12_agreement_n_le6000'] = [ok3, tot]
out['Z0778_mismatch_first'] = ex3
# mod-3 version: failure iff no divisor d | M^2 with d = -M (mod 3)
ok_m3 = sum(1 for n in range(5, 6001, 4) if (not any(d % 3 == (-(n * (n + 3))) % 3 for d in divisors((n * (n + 3)) ** 2))) == (n in bad))
out['Z0778_mod3_note'] = 'mod-3-only test (no further condition) kept for comparison'
out['Z0778_mod3_only_agreement_n_le6000'] = [ok_m3, tot]
# ---- Z0813: families 2^k*3+1, 2^k*5+1 primes ----
out['Z0813_families'] = 'computed in scripts/z52d_p2_TO3_fix_families.sh (count program)'
# ---- Z0824 / Z0825 : shift-character features on the base table (primes 1 mod 4, <=2e5) ----
Pall = p
Lg = {q: np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in Pall]) for q in primerange(3, 48)}
def fit_with(feats):
    Xf = np.column_stack([np.ones(len(Pall)), np.log(Pall.astype(float)), np.log(np.log(Pall.astype(float)))] + feats)
    b, *_ = np.linalg.lstsq(Xf, np.log(U), rcond=None)
    res = np.log(U) - Xf @ b
    s2 = res @ res / (len(U) - Xf.shape[1]); cov = s2 * np.linalg.pinv(Xf.T @ Xf)
    return b, np.sqrt(np.diag(cov))
QS = [q for q in primerange(3, 48)]
ind = {}
for q in QS:
    for sft in range(1, 13):
        ind[(q, sft)] = (((Pall + sft) % q) == 0).astype(float)
feats_leg = [Lg[q].astype(float) for q in QS]
keys = [(q, s) for q in QS for s in range(1, 13)]
b_all, se_all = fit_with(feats_leg + [ind[k] for k in keys])
out['Z0824_shift_structure'] = dict(n_features=len(keys), n_primes=len(Pall))
coef = {k: (round(float(b_all[3 + len(QS) + i]), 3), round(float(se_all[3 + len(QS) + i]), 3)) for i, k in enumerate(keys)}
out['Z0824_indicator_coeffs_q_le47_s_le12_top'] = sorted(((k, v) for k, v in coef.items()), key=lambda kv: -abs(kv[1][0]))[:12]
# test proportionality to (-s/q): sign agreement of coeff with the Jacobi symbol (-s/q)
agree = 0; tot = 0; detail = []
for (q, sh), (c, se) in coef.items():
    if se > 0 and abs(c) > 2 * se:
        tot += 1
        jj = int(jacobi_symbol((-sh) % q, q))      # Legendre (-s/q)
        agree += int(np.sign(c) == jj)
        detail.append((q, sh, c, jj))
out['Z0824_sign_agreement_with_(-s/q)_significant'] = [agree, tot]
out['Z0824_significant_detail_first12'] = detail[:12]
# Z0825: beta_7 with controls 1[7 | p+s], s<=40
ind7 = [(((Pall + s) % 7) == 0).astype(float) for s in range(1, 41)]
b7, se7 = fit_with(feats_leg + ind7)
out['Z0825'] = dict(beta7_before=round(float(fit_with(feats_leg)[0][3 + QS.index(7)]), 4),
                    beta7_after_s_le40=round(float(b7[3 + QS.index(7)]), 4), se=round(float(se7[3 + QS.index(7)]), 4),
                    n_controls=40)
# ---- Z0834: joint regression of log U on v2,v3,v5 and Legendre weights (q<=47) ----
def vp(x, q):
    c = 0
    while x % q == 0: x //= q; c += 1
    return c
v2a = np.array([vp(int(x) - 1, 2) for x in Pall], float); v3a = np.array([vp(int(x) - 1, 3) for x in Pall], float); v5a = np.array([vp(int(x) - 1, 5) for x in Pall], float)
b_j, se_j = fit_with(feats_leg + [v2a, v3a, v5a])
out['Z0834_joint'] = dict(coef_v2=round(float(b_j[-3]), 3), se_v2=round(float(se_j[-3]), 3), coef_v3=round(float(b_j[-2]), 3), se_v3=round(float(se_j[-2]), 3),
                          coef_v5=round(float(b_j[-1]), 3), se_v5=round(float(se_j[-1]), 3))
b_nov, se_nov = fit_with(feats_leg)
out['Z0834_joint']['residual_var_reduction_by_v235'] = None
# ---- Z0841: share k1/(k1+k2) by mod-840 square classes (6 Mordell + others with >=40 primes) ----
k1 = np.array([float(r['k1']) for r in P1]); k2 = np.array([float(r['k2']) for r in P1])
sh = k1 / (k1 + k2)
mod840 = {}
for c in range(1, 840, 2):
    s = (p % 840) == c
    if s.sum() >= 40: mod840[c] = round(float(sh[s].mean()), 3)
out['Z0841_share_mod840'] = dict(n_classes=len(mod840), six_mordell={c: mod840.get(c) for c in six}, min_class=min(mod840.items(), key=lambda kv: kv[1]),
                                 max_class=max(mod840.items(), key=lambda kv: kv[1]))
# ---- Z0881: genus test of h(-4p) mod-16 strata via Legendre symbols (3/p),(5/p),(7/p) ----
h4 = np.array([float(r['h4p']) for r in P1])
s8 = (p % 8 == 1)
Xg = np.column_stack([np.ones(s8.sum()), np.log(p[s8].astype(float)), np.log(np.log(p[s8].astype(float)))])
rU8 = np.log(U[s8]) - Xg @ np.linalg.lstsq(Xg, np.log(U[s8]), rcond=None)[0]
strata = {c: rU8[(h4[s8] % 16) == c] for c in (0, 4, 8, 12)}
out['Z0881_genus_test'] = {}
for c in (0, 4, 8, 12):
    d = {}
    for nm, q in (('3', 3), ('5', 5), ('7', 7)):
        l = np.array([jacobi_symbol(q, int(x)) for x in p[s8][(h4[s8] % 16) == c]])
        d[nm] = dict(plus=round(float(strata[c][l == 1].mean()), 3) if (l == 1).any() else None,
                     minus=round(float(strata[c][l == -1].mean()), 3) if (l == -1).any() else None)
    out['Z0881_genus_test'][c] = d
# ---- Z0908: VE for moduli 9240 and 10920 (n <= 30000) ----
s = (F[:, 1] > 0) & (F[:, 0] >= 1000)
nn = F[s, 0]; UU = F[s, 1]
X0 = np.column_stack([np.ones(len(nn)), np.log(nn.astype(float)), np.log(np.log(nn.astype(float)))])
rr = np.log(UU.astype(float)) - X0 @ np.linalg.lstsq(X0, np.log(UU.astype(float)), rcond=None)[0]
def ve(mod):
    cls = nn % mod; mu = {c: rr[cls == c].mean() for c in np.unique(cls)}
    fit = np.array([mu[c] for c in cls])
    return float(1 - (rr - fit).var() / rr.var())
out['Z0908_VE'] = {str(m): round(ve(m), 4) for m in (840, 9240, 10920)}
# ---- Z0911: partial correlation of log k1, log k2 after size and Legendre weights ----
kk = np.array([int(r['k1']) for r in P1]); kk2 = np.array([int(r['k2']) for r in P1])
Xs = np.column_stack([np.ones(len(p)), np.log(p.astype(float)), np.log(np.log(p.astype(float)))] + feats_leg[:0])
Xc2 = np.column_stack([np.ones(len(p)), np.log(p.astype(float)), np.log(np.log(p.astype(float)))] + [Lg[q].astype(float) for q in QS])
def rres(y, X): return y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
a1 = rres(np.log(kk), Xs); a2 = rres(np.log(kk2), Xs)
b1 = rres(np.log(kk), Xc2); b2 = rres(np.log(kk2), Xc2)
out['Z0911_partial'] = dict(rho_size_only=round(float(np.corrcoef(a1, a2)[0, 1]), 3), rho_size_plus_legendre=round(float(np.corrcoef(b1, b2)[0, 1]), 3))
# ---- Z0921: PCA-orthogonalised twist fit ----
json.dump(out, open('data/z52b/pass2/TO3/fix_a_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:500])
