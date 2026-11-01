"""Fix round TO3, batch E (uses count-program outputs produced by scripts/z52d_p2_TO3_bigU.sh and the gap/neighbour lists):
Z0822 (U(m^2) vs neighbours, odd m<=599), Z0813 (2^k*3+1, 2^k*5+1 primes), Z0879 (exponent in (2e5,1e6] sample, 1e8 sample),
Z0807/Z0929/Z0885 (U/log^3 at 1e8 sample, decade minima), Z0729 (8/p failures to 1e8, from ex8_1e8.txt),
Z0806 (beta_q vs -alpha/q), Z0978 (gcd stratum = primitive count of 4g/p, p<=300), Z0924 (NB on windows, squares excluded).
Writes data/z52b/pass2/TO3/fix_e_results.json"""
import csv, json, math, sys
import numpy as np
from sympy import primerange, jacobi_symbol
from math import gcd
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
out = {}
BIG = '/tmp/z52/big/'
def load(fn):
    d = {}
    for l in open(BIG + fn):
        x = l.split()
        if len(x) >= 2: d[int(x[0])] = int(x[1])
    return d
Usq = load('Usq.txt'); Unb = load('Unb.txt'); Ufam = load('Ufam.txt'); Ugap = load('Ugap.txt'); U1e8 = load('U1e8.txt')
# ---- Z0822 ----
rat = []
for m in range(3, 600, 2):
    n2 = m * m
    if n2 not in Usq: continue
    nb = [Unb[n2 + d] for d in (-2, -1, 1, 2) if (n2 + d) in Unb]
    rat.append((m, Usq[n2], float(np.median(nb)) if nb else None))
r_sq = [u / nb for m, u, nb in rat if nb]
out['Z0822'] = dict(n_odd_m=len(rat), median_ratio_U_m2_over_nb4=round(float(np.median(r_sq)), 3),
                    mean_ratio=round(float(np.mean(r_sq)), 3), frac_below_1=round(float(np.mean([x < 1 for x in r_sq])), 3),
                    first_values={m: u for m, u, _ in rat[:10]},
                    composite_vs_prime_median={'prime_m': round(float(np.median([u / nb for m, u, nb in rat if nb and all(m % q for q in range(2, int(m ** .5) + 1)) and m > 1])), 3),
                                               'composite_m': round(float(np.median([u / nb for m, u, nb in rat if nb and not all(m % q for q in range(2, int(m ** .5) + 1))])), 3)})
# ---- Z0813 ----
out['Z0813'] = {n: dict(U=Ufam[n], U_over_log2=round(Ufam[n] / math.log(n) ** 2, 3)) for n in sorted(Ufam)}
# ---- Z0879 / Z0807 / Z0929 / Z0885: gap sample (2e5,1e6] and 1e8 sample ----
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
def L1_of(q):
    import cypari2
    return None
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
def L1(q):
    return 2 * int(pari.quadclassunit(q)[0]) * float(pari.log(pari.quadunit(q))) / math.sqrt(q)
gp = sorted(Ugap)
lp = np.log(np.array(gp, float)); lu = np.log(np.array([Ugap[q] for q in gp], float)); lL = np.log(np.array([L1(q) for q in gp]))
X = np.column_stack([np.ones(len(gp)), np.log(lp * 0 + np.exp(lp)), lp * 0 + lp, np.log(np.array([L1(q) for q in gp]))]) if False else None
X = np.column_stack([np.ones(len(gp)), np.log(np.array(gp, float)), np.log(np.log(np.array(gp, float))), lL])
b = np.linalg.lstsq(X, lu, rcond=None)[0]
res_ = lu - X @ b; s2 = res_ @ res_ / (len(gp) - 4); se = np.sqrt(np.diag(s2 * np.linalg.pinv(X.T @ X)))
out['Z0879_gap_2e5_1e6'] = dict(n=len(gp), alpha=round(float(b[3]), 3), se=round(float(se[3]), 3),
                                median_U_over_log2=round(float(np.median(np.exp(lu) / np.array(gp, float) ** 0 / np.log(gp) ** 2)), 3),
                                median_U_over_log3=round(float(np.median(np.exp(lu) / np.log(gp) ** 3)), 4),
                                min_U_over_log3=round(float(np.min(np.exp(lu) / np.log(gp) ** 3)), 4))
g1e8 = sorted(U1e8)
lL8 = np.array([L1(q) for q in g1e8])
u8 = np.array([U1e8[q] for q in g1e8], float); p8 = np.array(g1e8, float)
X8 = np.column_stack([np.ones(len(g1e8)), np.log(p8), np.log(np.log(p8)), np.log(lL8)])
b8 = np.linalg.lstsq(X8, np.log(u8), rcond=None)[0]
r8 = np.log(u8) - X8 @ b8; s28 = r8 @ r8 / (len(g1e8) - 4); se8 = np.sqrt(np.diag(s28 * np.linalg.pinv(X8.T @ X8)))
out['Z0879_1e8_sample'] = dict(n=len(g1e8), alpha=round(float(b8[3]), 3), se=round(float(se8[3]), 3))
out['Z0807_Z0929_Z0885_1e8'] = dict(n=len(g1e8), median_U_over_log2=round(float(np.median(u8 / np.log(p8) ** 2)), 3),
                                    median_U_over_log3=round(float(np.median(u8 / np.log(p8) ** 3)), 4),
                                    min_U_over_log3=round(float(np.min(u8 / np.log(p8) ** 3)), 4), argmin=int(g1e8[int(np.argmin(u8 / np.log(p8) ** 3))]),
                                    min_U_over_log2=round(float(np.min(u8 / np.log(p8) ** 2)), 3))
# decade minima of U/log^3 over the samples (1e6..1e7 windows from files, 1e7 in windows, 1e8 sample)
# ---- Z0729: 8/p failures to 1e8 ----
ex8 = [l.split() for l in open(BIG + 'ex8_1e8.txt')]
f8 = [int(x[0]) for x in ex8 if x[1] == '0']
out['Z0729_8p_to_1e8'] = dict(n_fail=len(f8), last=f8[-1], fails_gt_1e5=[q for q in f8 if q > 1e5][:10], n_primes_scanned=len(ex8))
# ---- Z0806 : beta_q proportional to 1/q ? (regression of log U on Legendre weights, fit alpha) ----
R_ = json.load(open('data/z52b/pass2/TO3/regress_results.json'))
bq = {int(q): v['beta'] for q, v in R_['Z0823_chi_p_weights_p1mod4'].items()}
qs = sorted(bq)
A_ = np.array([1 / q for q in qs]); y_ = np.array([bq[q] for q in qs])
alpha = float(np.sum(A_ * y_) / np.sum(A_ * A_))
resid_ = y_ - alpha * A_
mod3 = {r: float(np.mean([bq[q] * q for q in qs if q % 3 == r])) for r in (1, 2)}
out['Z0806'] = dict(alpha_fit_beta_eq_alpha_over_q=round(alpha, 4), rms_resid=round(float(np.sqrt(np.mean(resid_ ** 2))), 4),
                    rms_beta=round(float(np.sqrt(np.mean(y_ ** 2))), 4), frac_variance_explained=round(float(1 - np.sum(resid_ ** 2) / np.sum(y_ ** 2)), 3),
                    mean_q_beta_by_q_mod3={'1': round(mod3[1], 3), '2': round(mod3[2], 3)})
# ---- Z0978 : gcd stratum g  <->  primitive solutions of 4g/p ----
ok = 0; tot = 0; mism = []
for p in primerange(3, 301):
    S = sols(4, p)
    for g in set(gcd(gcd(s[0], s[1]), s[2]) for s in S):
        n_g = sum(1 for s in S if gcd(gcd(s[0], s[1]), s[2]) == g)
        prim = sum(1 for s in sols(4 * g, p) if gcd(gcd(s[0], s[1]), s[2]) == 1) if (4 * g) % p else None
        if prim is None: continue
        tot += 1
        if n_g == prim: ok += 1
        elif len(mism) < 5: mism.append((p, g, n_g, prim))
out['Z0978_bijection_check'] = dict(checked=tot, agree=ok, mismatches=mism)
json.dump(out, open('data/z52b/pass2/TO3/fix_e_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:600])
