# z52b pass1 U00 fix: C-form divisor tests (cypari2).
# W(p,C): exists divisor a of N=4Cp+1 with 1<a<N and a ≡ -1 (mod 4C).  Cform(p) = min C with W (C<=CMAX).
# Items: Z0852 (product model for P(Cform>c)), Z1627 (409 expected vs observed), Z1529 (expected vs observed, p~1e6),
#        Z1619 (win(p,C) autocorrelation), Z1524 (Bonferroni on a random sample), Z1715 (H_{-4p}(0) factors).
import cypari2, json, random, math, time
import numpy as np
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
out = {}
def divisors_of(N):
    f = pari.factor(N)
    ps = [int(f[0][i]) for i in range(len(f[0]))]; es = [int(f[1][i]) for i in range(len(f[1]))]
    ds = [1]
    for p_, e in zip(ps, es):
        ds = [d * p_ ** k for d in ds for k in range(e + 1)]
    return ds
def phi(m):
    return int(pari.eulerphi(m))
def obs_count(p, C):
    N = 4 * C * p + 1; M = 4 * C
    return sum(1 for a in divisors_of(N) if 1 < a < N and a % M == M - 1)
def W(p, C):
    return obs_count(p, C) > 0
primes = lambda lo, hi: [int(q) for q in pari('primes([%d,%d])' % (lo, hi))]
t0 = time.time()
# ---- Z0852: P(Cform > c) vs product of marginals q_C = P(not W(p,C)), primes ≡1 (4), p ≤ 2e4, C ≤ 50
P = [q for q in primes(5, 20000) if q % 4 == 1]
CMAX = 50
Wm = np.zeros((len(P), CMAX + 1), bool)
for i, p in enumerate(P):
    for C in range(1, CMAX + 1):
        Wm[i, C] = W(p, C)
cf = np.array([next((C for C in range(1, CMAX + 1) if Wm[i, C]), 10 ** 9) for i in range(len(P))])
q = {C: 1 - Wm[:, C].mean() for C in range(1, CMAX + 1)}  # marginal failure prob at level C
res852 = []
for c in [1, 2, 3, 5, 8, 12, 20, 30, 50]:
    emp = float((cf > c).mean())
    prod = float(np.prod([q[C] for C in range(1, c + 1)]))
    res852.append({'c': c, 'emp_P(Cform>c)': round(emp, 5), 'prod_marginals': round(prod, 5), 'ratio': round(emp / prod, 3) if prod > 0 else None})
out['Z0852'] = {'n_primes': len(P), 'CMAX': CMAX, 'marginal_fail_q_C_first8': {C: round(q[C], 4) for C in range(1, 9)}, 'table': res852,
                'Cform_median': float(np.median(cf)), 'Cform_mean_capped': float(np.mean(np.minimum(cf, CMAX + 1))),
                'frac_with_Cform_le2': float((cf <= 2).mean()), 'frac_with_Cform_gt50': float((cf > CMAX).mean())}
print('Z0852 done', round(time.time() - t0), 's', flush=True)
# ---- Z1627: p = 409, C <= 60000: observed #{a} vs expected (tau(N)-2)/phi(4C)
p = 409; obs = 0; ex = 0.0; cforms = []
for C in range(1, 60001):
    N = 4 * C * p + 1
    ds = divisors_of(N)
    k = sum(1 for a in ds if 1 < a < N and a % (4 * C) == 4 * C - 1)
    obs += k; ex += (len(ds) - 2) / phi(4 * C)
    if k: cforms.append(C)
out['Z1627'] = {'p': p, 'C_max': 60000, 'observed_divisor_count_sum': obs, 'expected_sum_(tau-2)/phi(4C)': round(ex, 2), 'C_with_witness_first': cforms[:10]}
print('Z1627 done', round(time.time() - t0), 's', flush=True)
# ---- Z1529: three primes ≡1 (4) just above 10^6, X = 1000: observed vs expected, at X = 100, 300, 1000
ps1529 = [q for q in primes(10 ** 6, 10 ** 6 + 2000) if q % 4 == 1][:3]
rows = []
for p in ps1529:
    o = e = 0.0; pts = {}
    for C in range(1, 1001):
        N = 4 * C * p + 1; ds = divisors_of(N)
        o += sum(1 for a in ds if 1 < a < N and a % (4 * C) == 4 * C - 1); e += (len(ds) - 2) / phi(4 * C)
        if C in (100, 300, 1000): pts[C] = (o, round(e, 2))
    rows.append({'p': p, 'at_X': pts})
out['Z1529'] = rows
print('Z1529 done', round(time.time() - t0), 's', flush=True)
# ---- Z1619: win(p,C) for 5 primes ≡1 (4) near 10^4, C ≤ 20000: lag correlations
ps1619 = [q for q in primes(10 ** 4, 10 ** 4 + 3000) if q % 4 == 1][:5]
cors = []
for p in ps1619:
    w = np.array([1.0 if W(p, C) else 0.0 for C in range(1, 20001)])
    def ac(l):
        if w[:-l].std() == 0 or w[l:].std() == 0: return None
        return float(np.corrcoef(w[:-l], w[l:])[0, 1])
    cors.append({'p': p, 'mean_win': round(float(w.mean()), 4), 'ac_lag1': ac(1), 'ac_lag24': ac(24), 'ac_lag840': ac(840), 'n_C_with_witness': int(w.sum()),
                 'mean_win_C_in_1..840_blocks_std': round(float(np.std(w[:18480].reshape(-1, 840).mean(axis=1))), 4)})
out['Z1619'] = cors
print('Z1619 done', round(time.time() - t0), 's', flush=True)
# ---- Z1524: Bonferroni on random sample n ≡ 1 (4), n ≤ 1e6, levels C ≤ 20
random.seed(1)
S = [4 * random.randrange(1, 250000) + 1 for _ in range(4000)]
CM = 20
E = np.zeros((len(S), CM + 1), bool)
for i, nn in enumerate(S):
    for C in range(1, CM + 1):
        E[i, C] = W(nn, C)
dC = {C: float(E[:, C].mean()) for C in range(1, CM + 1)}
pair = {}
for C in range(1, CM + 1):
    for D in range(C + 1, CM + 1):
        pair[(C, D)] = float((E[:, C] & E[:, D]).mean())
bon = sum(dC.values()) - sum(pair.values())
union = float(E[:, 1:].any(axis=1).mean())
out['Z1524'] = {'sample': len(S), 'levels': CM, 'mean_single_d_C_first5': {C: round(dC[C], 4) for C in range(1, 6)},
                'Bonferroni_lower_bound(sum d_C - sum pairs)': round(bon, 4), 'empirical_union_density': round(union, 4),
                'Bonferroni_bound_valid': bool(bon <= union + 1e-9)}
print('Z1524 done', round(time.time() - t0), 's', flush=True)
# ---- Z1715: H_{-4p}(0) for p ≡ 1 (4), p < 300; check (D/q) for prime factors q of H_D(0), D = -4p
rows = []
for p in [q for q in primes(5, 300) if q % 4 == 1]:
    D = -4 * p
    H = pari('polclass(%d)' % D)
    v = int(pari('subst(%s,x,0)' % str(H)))
    if v == 0:
        continue
    f = pari.factor(abs(v))
    fs = [(int(f[0][i]), int(f[1][i])) for i in range(len(f[0]))]
    kron = [int(pari('kronecker(%d,%d)' % (D, qq))) for qq, _ in fs]
    rows.append({'p': p, 'H(0)_factors': fs, 'kronecker(-4p/q)': kron})
out['Z1715'] = {'n_p': len(rows), 'all_factors_split(kron=+1 or q|D)': all(all(k == 1 or qq in (2, p) for k, (qq, _) in zip(r['kronecker(-4p/q)'], r['H(0)_factors'])) for r in rows),
                'examples': rows[:6]}
print('Z1715 done', round(time.time() - t0), 's', flush=True)
json.dump(out, open('data/z52b/pass1/U00/fix_cform.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:5000])
