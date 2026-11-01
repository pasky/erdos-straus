# TO2 part 5: Z0692 (log R vs class numbers h(-4p), h(-8p), h(-3p)), Z0690 (per-q weights of L-value proxy for U(p)), primes p≡1 mod 4, p<=2e5
import numpy as np, json, math
out = {}
H = np.loadtxt('data/z52b/pass2/TO2/hD_p1mod4_2e5.txt', dtype=np.int64)  # p h(-4p) h(-8p) h(-3p) h(-20p)[ignore]
p = H[:, 0]; h4, h8, h3 = H[:, 1].astype(float), H[:, 2].astype(float), H[:, 3].astype(float)
Rf = np.loadtxt('/tmp/r1e7.txt', dtype=np.int64)
Rmap = np.zeros(10**7 + 1, np.int64); Rmap[Rf[:, 0]] = Rf[:, 1]
R = Rmap[p].astype(float)
ok = (p > 5) & (R > 0) & (h4 > 0) & (h8 > 0) & (h3 > 0)
y = np.log(R[ok]); lp = np.log(p[ok].astype(float))
def fit(cols, names):
    A = np.column_stack(cols + [np.ones(len(y))])
    c, *_ = np.linalg.lstsq(A, y, rcond=None); res = y - A @ c
    r2 = 1 - (res**2).sum() / ((y - y.mean())**2).sum()
    return dict(zip(names + ['const'], [float(v) for v in c])), float(r2)
out['n'] = int(ok.sum())
out['logR_on_logp'] = fit([lp], ['logp'])
out['logR_on_loglogp'] = fit([np.log(lp)], ['loglogp'])
out['logR_on_log_h4_minus_half_log_p'] = fit([np.log(h4[ok]) - 0.5*lp], ['logL4'])
out['logR_on_logp_and_logh4'] = fit([lp, np.log(h4[ok])], ['logp', 'logh4'])
out['logR_on_logp_and_logh4_h8_h3'] = fit([lp, np.log(h4[ok]), np.log(h8[ok]), np.log(h3[ok])], ['logp', 'logh4', 'logh8', 'logh3'])
out['logR_on_logp_and_logh8'] = fit([lp, np.log(h8[ok])], ['logp', 'logh8'])
out['logR_on_logp_and_logh3'] = fit([lp, np.log(h3[ok])], ['logp', 'logh3'])
out['corr_logR_loghs_resid'] = None
# ---- Z0690 / Z0689: Euler-factor regressors for U(p) (repo counts), p≡1 mod 4, 1000<p<=2e5
D = 'data/z52b/raw/'
a = np.loadtxt(D + 'f4_all_30000.txt', dtype=np.int64); b = np.loadtxt(D + 'pr_20001_200000.txt', dtype=np.int64)
A_ = np.vstack([a, b]); pr = A_[:, 0]
s = np.ones(pr.max()+1, bool); s[:2] = False
for i in range(2, int(pr.max()**0.5)+1):
    if s[i]: s[i*i::i] = False
sel = s[pr] & (pr > 1000) & (pr % 4 == 1)
U = A_[sel, 1].astype(float); P = pr[sel]; k1 = A_[sel, 10].astype(float)
yU = np.log(U)
def leg(a, q):
    return 0 if a % q == 0 else (1 if pow(a % q, (q-1)//2, q) == 1 else -1)
qs = [2, 3, 5, 7, 11, 13]
feats = []
for q in qs:
    # log Euler factor of L(1,chi_p) at q: -log(1 - chi_p(q)/q), chi_p(q) = (p/q) (Legendre, p≡1 mod 4)
    f = np.array([-math.log(1 - leg(int(x), q)/q) if q > 2 else -math.log(1 - (1 if int(x) % 8 in (1, 7) else -1)/2) for x in P])
    feats.append(f)
Llp = np.log(np.log(P.astype(float)))
A = np.column_stack(feats + [Llp, np.ones(len(P))])
c, *_ = np.linalg.lstsq(A, yU, rcond=None); res = yU - A @ c
out['U_per_q_weights_q2_3_5_7_11_13_plus_loglogp'] = {str(q): float(v) for q, v in zip(qs, c[:len(qs)])}
out['U_per_q_weights_loglogp_coef'] = float(c[len(qs)])
out['U_per_q_R2'] = float(1 - (res**2).sum()/((yU - yU.mean())**2).sum())
# single-Q proxies
for Q in [2, 3, 5, 7, 13, 31, 100, 1000]:
    L = np.zeros(len(P))
    for q in primes_upto if False else []:
        pass
out['n_primes_1000_2e5_1mod4'] = int(len(P))
json.dump(out, open('data/z52b/pass2/TO2/an5.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
