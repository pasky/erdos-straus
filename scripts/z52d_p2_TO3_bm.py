"""Pass-2 TO3: Brauer-Manin-type main term M_BM(p) (same formula as scripts/z52b_fingerprint_bm.py) on
(a) random samples of primes in windows (Z0781 Poisson-type zero count, Z0886 R/M_BM ratio drift),
(b) all primes 1 mod 4 <= 3e4 (Z0888: regression of M_BM on Legendre symbols (q/p), q<=47, vs the U-Euler weights).
R(p) from the words census (/tmp/z52/words3e6.txt, column R = (*) count); U from the base table.
Writes data/z52b/pass2/TO3/bm_results.json"""
import numpy as np, json, math, csv, sys
from math import gcd
from sympy import primerange
from scipy.stats import spearmanr
rng = np.random.default_rng(12345)
HI = 3 * 10**6
N = 4 * HI + 10
pairs = []
for u in range(1, HI + 2):
    if 4 * u - u - 1 > HI: break
    for B in range(1, HI + 2):
        if 4 * u * B - u - B > HI: break
        if (u + B) % 2 == 1 and gcd(u, B) == 1: pairs.append((u, B))
pairs = np.array(pairs, dtype=np.int64)
print('pairs', len(pairs), flush=True)
phi = None
def phi_of(q):
    # phi(q) for array q (4uB) via sympy-free sieve up to 4*max
    return np.array([int(_phi(int(x))) for x in q], dtype=np.float64)
from sympy import totient
_phi = totient
qarr = 4 * pairs[:, 0] * pairs[:, 1]
lim = qarr // 4 * 0 + (4 * pairs[:, 0] * pairs[:, 1] - pairs[:, 0] - pairs[:, 1])
# phi(4uB) via prime factorisation of u and B (cheap: use a sieve of phi up to 4*max uB)
MAXQ = int(qarr.max())
phis = np.arange(MAXQ + 1, dtype=np.int64)
for i in range(2, MAXQ + 1):
    if phis[i] == i:
        phis[i::i] -= phis[i::i] // i
w = 1.0 / phis[qarr]
order = np.argsort(lim)
lim_s = lim[order]; w_s = w[order]; pr_s = pairs[order]
cum_w = np.cumsum(w_s)
def Mbm(p):
    k = np.searchsorted(lim_s, p, side='right')   # pairs with lim <= p
    a = (-(pr_s[:k, 0] * pr_s[:k, 1])) % p
    # Legendre(-uB / p) via Euler criterion
    leg = np.array([pow(int(x), (p - 1) // 2, p) for x in a]) if False else None
    e = (p - 1) // 2
    r = np.ones(k, dtype=np.int64); base = a.copy(); ee = e
    while ee:
        if ee & 1: r = (r * base) % p
        base = (base * base) % p; ee >>= 1
    chi = np.where(r == 1, 1, -1)
    M0 = w_s[:k].sum(); T = (chi * w_s[:k]).sum()
    return M0 - T, M0
W = np.loadtxt('/tmp/z52/words3e6.txt', dtype=np.int64)
Rarr = W[:, 3]
out = {}
def isprime(n): return n >= 2 and all(n % q for q in range(2, int(n ** .5) + 1))
# ---- (a) window samples ----
wins = [(10**4, 10**5, 80), (10**5, 10**6, 80), (10**6, 3 * 10**6, 80)]
recs = []
for lo, hi, ns in wins:
    cand = [p for p in primerange(lo, hi) if p % 4 == 1]
    samp = rng.choice(cand, size=ns, replace=False)
    for p in samp:
        mb, m0 = Mbm(int(p))
        recs.append((int(p), float(mb), float(m0), int(Rarr[int(p) - 1]), lo))
    print('window', lo, hi, flush=True)
recs = np.array(recs, dtype=float)
out['Z0886'] = {}
for lo, hi, _ in wins:
    s = (recs[:, 4] == lo)
    R = recs[s, 3]; M = recs[s, 1]; M0 = recs[s, 2]
    out['Z0886'][f'[{lo},{hi})'] = dict(n_sample=int(s.sum()), mean_R_over_Mbm=round(float(R.mean() / M.mean()), 4),
                                        mean_ratio_per_prime=round(float(np.mean(R / M)), 4), mean_R_over_M0=round(float(R.mean() / M0.mean()), 4),
                                        mean_R=round(float(R.mean()), 3), mean_Mbm=round(float(M.mean()), 3))
# Z0781: expected zeros under Poisson(M_BM) per window (sample-based estimator) vs observed (all primes 1 mod 4 in window)
out['Z0781'] = {}
for lo, hi, _ in wins:
    s = (recs[:, 4] == lo)
    M = recs[s, 1]
    allp = [p for p in primerange(lo, hi) if p % 4 == 1]
    est = len(allp) * float(np.mean(np.exp(-np.maximum(M, 0))))
    obs = int(sum(1 for p in allp if Rarr[p - 1] == 0))
    out['Z0781'][f'[{lo},{hi})'] = dict(n_primes=len(allp), observed_R0=obs, expected_R0_poisson_Mbm_sample_est=round(est, 3),
                                         mean_Mbm_sample=round(float(M.mean()), 3))
# ---- (b) Z0888: all primes 1 mod 4 <= 3e4: M_BM and Legendre symbols ----
Pl = [p for p in primerange(101, 30001) if p % 4 == 1]
Ms = []; Ls = []
Qs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for p in Pl:
    mb, m0 = Mbm(p)
    Ms.append(mb)
    Ls.append([1 if pow(q, (p - 1) // 2, p) == 1 else -1 for q in Qs])
Ms = np.array(Ms); Ls = np.array(Ls, dtype=float)
X = np.column_stack([np.ones(len(Pl)), np.log(np.array(Pl, dtype=float)), Ls])
b = np.linalg.lstsq(X, Ms, rcond=None)[0]
# compare with U-weights (base table, same primes): regression of resid log U on Legendre
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
Ud = {int(r['p']): float(r['U']) for r in rows}
lu = np.array([math.log(Ud[p]) for p in Pl]); lp = np.log(np.array(Pl, dtype=float))
Xu = np.column_stack([np.ones(len(Pl)), lp, np.log(lp), Ls])
bu = np.linalg.lstsq(Xu, lu, rcond=None)[0]
out['Z0888'] = dict(n=len(Pl), mbm_coef_per_q={q: round(float(b[2 + i]), 4) for i, q in enumerate(Qs)},
                    logU_coef_per_q={q: round(float(bu[3 + i]), 4) for i, q in enumerate(Qs)},
                    spearman_across_q=round(float(spearmanr(b[2:], bu[3:])[0]), 3),
                    sign_agreement=int(sum(np.sign(b[2 + i]) == np.sign(bu[3 + i]) for i in range(len(Qs)))), of=len(Qs))
json.dump(out, open('data/z52b/pass2/TO3/bm_results.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:4000])
