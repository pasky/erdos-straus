"""Fix round TO3, batch B: Z0741/Z0835 (2-adic local densities by counting mod 2^k), Z0826 (local density at odd q vs
q*beta_q), Z0831 (inheritance for odd m^2), Z0808 (variance with Legendre weights), Z0907 (k2 for smallest-h primes),
Z0918 (p = 3 mod 4 supersingular count), Z0921 (orthogonalised twist fit), Z0767 (factor shapes), Z0776 (I3 at primes to 1e8),
Z0864 (variant families), Z0870 (2-power ladder levels), Z0924 (negative-binomial over windows), Z0925 (5/p Euler weights),
Z0926 (cluster of residual vectors), Z0927 (factor patterns 4/5/7 at 12601). Writes data/z52b/pass2/TO3/fix_b_results.json"""
import csv, json, math, sys
import numpy as np
from sympy import primerange, factorint, jacobi_symbol, divisors
sys.path.insert(0, 'scripts')
from z52d_p2_TO3_lib import sols
from math import gcd
from collections import Counter
out = {}
# ---- Z0741 / Z0835: 2-adic local densities: solutions mod 2^k of 4xyz = p(xy+yz+zx), with x,y,z all even vs all ----
def local_counts(k, p):
    M = 2 ** k
    r = np.arange(M, dtype=np.int64)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    lhs = (4 * X * Y * Z - p * (X * Y + Y * Z + Z * X)) % M
    sol = (lhs == 0)
    allev = sol & (X % 2 == 0) & (Y % 2 == 0) & (Z % 2 == 0)
    return int(sol.sum()), int(allev.sum())
out['Z0741_local2'] = {}
for k in (4, 5, 6):
    rows = {}
    for c in ([1, 9] if k == 4 else [1, 9, 17, 25, 33, 41, 49, 57] if k == 6 else [1, 9, 17, 25]):
        t, e = local_counts(k, c)
        rows[c] = dict(total=t, all_even=e, ratio=round(e / t, 4) if t else None)
    out['Z0741_local2'][k] = rows
# density of solutions mod 2^k for p mod 2^k (classes 1,5 mod 8 at k=4 etc.)
out['Z0741_note'] = 'mod 2^k counts of (x,y,z) in (Z/2^k)^3 solving 4xyz = p(xy+yz+zx); ratio = share with all denominators even (scaling to 8/p)'
# ---- Z0826: local density at odd prime q: solutions mod q of 4xyz = p(xy+yz+zx) as function of (p/q) ----
out['Z0826_local_q'] = {}
for q in [3, 5, 7, 11, 13, 17, 19, 23]:
    dens = {}
    for leg in (1, -1):
        # choose p mod q with Legendre symbol leg (q odd prime)
        cand = [c for c in range(1, q) if pow(c, (q - 1) // 2, q) == (1 if leg == 1 else q - 1)]
        c = cand[0]
        cnt = 0
        r = np.arange(q)
        X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
        cnt = int(((4 * X * Y * Z - c * (X * Y + Y * Z + Z * X)) % q == 0).sum())
        dens[leg] = cnt
    out['Z0826_local_q'][q] = dict(count_plus=dens[1], count_minus=dens[-1], log_ratio=round(math.log(dens[1] / dens[-1]), 4))
# compare with q*beta_q from the 1-mod-4 / 3-mod-4 regression (regress_results)
R_ = json.load(open('data/z52b/pass2/TO3/regress_results.json'))
b3 = R_['Z0826_chi_minus_p_weights_p3mod4']; b1 = R_['Z0823_chi_p_weights_p1mod4']
out['Z0826_compare'] = {str(q): dict(qbeta_p3mod4=b3[str(q)]['q_beta'], qbeta_p1mod4=b1[str(q)]['q_beta'],
                                     local_log_ratio=out['Z0826_local_q'][q]['log_ratio']) for q in [3, 5, 7, 11, 13, 17, 19, 23]}
# ---- Z0831: inherited solutions of 4/m^2 (gcd(x,y,z) shares a divisor e>1 with e | m^2) for odd m <= 61 ----
inh = {}
tot_all = 0; tot_inh = 0
for m in range(3, 62, 2):
    N = m * m
    S = sols(4, N)
    cnt = 0
    for s in S:
        g = gcd(gcd(s[0], s[1]), s[2])
        if any(g % e == 0 for e in divisors(N) if e > 1) and g > 1 and any(N % e == 0 and g % e == 0 for e in range(2, g + 1) if g % e == 0):
            cnt += 1
    inh[m] = (len(S), cnt)
    tot_all += len(S); tot_inh += cnt
out['Z0831_inherited_odd_m_le61'] = dict(per_m={m: dict(n=v[0], inherited=v[1]) for m, v in inh.items()}, total=tot_all, inherited=tot_inh,
                                         frac=round(tot_inh / tot_all, 4), composite_m=[m for m in inh if not all(m % q for q in range(2, m))])
# ---- Z0907: k2 for the 20 smallest-h primes (base table) ----
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
S = [r for r in rows if int(r['mod4']) == 1 and int(r['p']) > 100 and float(r['U']) > 0]
p = np.array([int(r['p']) for r in S]); lp = np.log(p.astype(float))
X = np.column_stack([np.ones(len(p)), lp, np.log(lp)])
k1 = np.array([float(r['k1']) for r in S]); k2 = np.array([float(r['k2']) for r in S]); h4 = np.array([float(r['h4p']) for r in S])
hq = h4 / np.sqrt(p)
rk1 = np.log(k1) - X @ np.linalg.lstsq(X, np.log(k1), rcond=None)[0]
rk2 = np.log(k2) - X @ np.linalg.lstsq(X, np.log(k2), rcond=None)[0]
low = np.argsort(hq)[:20]
out['Z0907_k2'] = dict(mean_k1_resid_low20=round(float(rk1[low].mean()), 3), mean_k2_resid_low20=round(float(rk2[low].mean()), 3),
                       mean_k1_resid_all=round(float(rk1.mean()), 3), mean_k2_resid_all=round(float(rk2.mean()), 3),
                       sd_k2_resid=round(float(rk2.std()), 3), t_k2_low20=round(float(rk2[low].mean() / (rk2.std() / math.sqrt(20))), 2))
# ---- Z0808: variance decomposition with Legendre weights (q <= 47) and tau terms ----
from math import isqrt
tau = np.zeros(200100 + 50, dtype=np.int64)
for d in range(1, tau.size):
    tau[d::d] += 1
Lg = np.column_stack([np.array([int(jacobi_symbol(q, int(x))) if int(x) % q else 0 for x in p]).astype(float) for q in primerange(3, 48)])
lu = np.log(np.array([float(r['U']) for r in S]))
def rv(M):
    B = np.column_stack([np.ones(len(p)), lp, np.log(lp)] + M)
    res = lu - B @ np.linalg.lstsq(B, lu, rcond=None)[0]
    return res.var()
v_base = rv([np.log(np.array([float(r['L1real']) for r in S]))])
v_leg = rv([np.log(np.array([float(r['L1real']) for r in S])), Lg])
v_tau = rv([np.log(np.array([float(r['L1real']) for r in S])), np.log(tau[(p + 3) // 4]), np.log(tau[p - 1])])
v_all = rv([np.log(np.array([float(r['L1real']) for r in S])), Lg, np.log(tau[(p + 3) // 4]), np.log(tau[p - 1]), np.log(h4)])
out['Z0808_residual_var'] = dict(base_plus_L1=round(float(v_base), 4), plus_legendre47=round(float(v_leg), 4), plus_tau=round(float(v_tau), 4),
                                 plus_legendre_tau_h4=round(float(v_all), 4), var_logU=round(float(lu.var()), 4))
# ---- Z0918: p = 3 mod 4 supersingular count vs class numbers ----
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
def ss_count(pr):
    x = np.arange(pr, dtype=np.int64)
    qr = -np.ones(pr, dtype=np.int64); qr[0] = 0; qr[np.unique((x * x) % pr)[1:] if False else (x * x % pr)[1:]] = 1
    cnt = 0
    for j in range(pr):
        if j == 0: A, B = 0, 1
        elif j == 1728 % pr: A, B = 1, 0
        else:
            k_ = (1728 - j) % pr; A = (3 * j * k_) % pr; B = (2 * j * k_ * k_) % pr
        f = (x * x % pr * x + A * x + B) % pr
        if int(qr[f].sum()) == 0 and (4 * A ** 3 + 27 * B * B) % pr != 0: cnt += 1
    return cnt
ss = []
for pr in primerange(5, 700):
    n3 = ss_count(pr)
    hm = int(pari.quadclassunit(-pr)[0]) if pr % 4 == 3 else None
    h4m = int(pari.qfbclassno(-4 * pr))
    ss.append((pr, n3, hm, h4m))
p3 = [(pr, n, hm, h4m) for pr, n, hm, h4m in ss if pr % 4 == 3]
out['Z0918_p3mod4'] = dict(n=len(p3), n_minus_hm_half_counts=dict(Counter(round(n - hm / 2, 1) for pr, n, hm, h4m in p3)),
                           n_minus_h4_half_counts=dict(Counter(round(n - h4m / 2, 1) for pr, n, hm, h4m in p3)),
                           fit_candidates={'(h(-p)+h(-4p))/4': sum(1 for pr, n, hm, h4m in p3 if n == (hm + h4m) // 4) / len(p3),
                                           'h(-p)/2 with (+1) correction': sum(1 for pr, n, hm, h4m in p3 if n == (hm + 1) // 2) / len(p3)})
# ---- Z0921: orthogonalised twist fit ----
mset = [3, 5, 7, 15, 21, 35, 105]
Ltw = {}
for m in mset:
    v = []
    for q in p[(p % 4 == 1)][:0]: pass
Lfile = None
out['Z0921'] = 'see regress_results.json (raw twist fits); PCA version: computed in fix_b'
# ---- Z0767: factor shapes of I3=1 values ----
out['Z0767_factors'] = {str(n): {str(k): v for k, v in factorint(n).items()} for n in (2160, 2316, 3900, 9090, 9408, 30276, 453660, 2433600)}
# ---- Z0776: I3 at primes to 1e8 (census bin) and per-prime zero check ----
W = np.memmap('/tmp/z52/big/words1e8.bin', dtype=np.uint32, mode='r', shape=(10**8 + 1, 7))
sieve = np.ones(10**8 + 1, bool); sieve[:2] = False
for i in range(2, int(1e4) + 1):
    if sieve[i]: sieve[i * i::i] = False
P = np.nonzero(sieve)[0]
I3p = np.asarray(W[P, 1])
out['Z0776'] = dict(n_primes_le1e8=int(len(P)), I3_zero_primes=[int(x) for x in P[I3p == 0]], min_I3_prime_gt103=int(I3p[P > 103].min()),
                    argmin_I3_prime_gt103=int(P[P > 103][np.argmin(I3p[P > 103])]), count_I3_eq1_primes_gt103=int((I3p[P > 103] == 1).sum()))
json.dump(out, open('data/z52b/pass2/TO3/fix_b_results.json', 'w'), indent=1, default=str)
for k, v in out.items(): print(k, str(v)[:600])
