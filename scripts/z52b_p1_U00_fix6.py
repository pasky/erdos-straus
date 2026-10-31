# z52b pass1 U00 fix (6): is the cross-level witness dependence (Z1475 closure, Z2559 consecutive levels) a class effect?
# Conditioning on p mod 24 (same classes as Z0852). And Z1492: witness-count growth (S(X)/E(X)) over 30 primes near 1e6.
import json, numpy as np
from cypari2 import Pari
from sympy import primerange
pari = Pari(); pari.allocatemem(10**9)
def divisors_of(N):
    f = pari.factor(N); ds = [1]
    for i in range(len(f[0])):
        q, e = int(f[0][i]), int(f[1][i]); ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def has_wit(p, C):
    N = 4 * C * p + 1; M = 4 * C
    return any(1 < a < N and a % M == M - 1 for a in divisors_of(N))
P1 = [q for q in primerange(5, 20000) if q % 4 == 1]
CM = 60
W = np.array([[1 if has_wit(p, C) else 0 for C in range(1, CM + 1)] for p in P1], float)
out = {}
for r in [1, 5, 13, 17]:
    idx = [i for i, p in enumerate(P1) if p % 24 == r]
    w = W[idx]
    cov = [(w[:, C - 1] * w[:, C]).mean() - w[:, C - 1].mean() * w[:, C].mean() for C in range(1, 40)]
    clo = {}
    for k in [2, 3]:
        a = np.array([(W[i, C - 1], W[i, k * C - 1]) for i in idx for C in range(1, CM // k + 1)])
        clo[k] = round(float(a[a[:, 0] == 1][:, 1].mean() / max(1e-9, a[:, 1].mean())), 3) if a[a[:, 0] == 1].size else None
    out[f'mod24={r}'] = {'n': len(idx), 'mean_cov_consecutive_levels': round(float(np.mean(cov)), 5), 'closure_ratio_P(W_kC|W_C)/P(W_kC)': clo}
# Z1492 over 30 primes near 1e6 (≡1 mod 4): S(X)/E(X) at X=100, 1000
ps = [q for q in primerange(10 ** 6, 10 ** 6 + 20000) if q % 4 == 1][:30]
rows = []
for p in ps:
    S = {}; E = {}; s = 0.0; e = 0.0
    for C in range(1, 1001):
        N = 4 * C * p + 1; M = 4 * C; ds = divisors_of(N)
        s += sum(1 for a in ds if 1 < a < N and a % M == M - 1); e += (len(ds) - 2) / int(pari.eulerphi(M))
        if C == 100: S[100], E[100] = s, e
    rows.append((p, S[100], round(E[100], 1), s, round(e, 1)))
r100 = np.array([r[1] / r[2] for r in rows]); r1000 = np.array([r[3] / r[4] for r in rows])
growth_obs = np.array([r[3] - r[1] for r in rows]); growth_exp = np.array([r[4] - r[2] for r in rows])
out['Z1492_30primes'] = {'median_S/E@100': round(float(np.median(r100)), 3), 'median_S/E@1000': round(float(np.median(r1000)), 3),
                         'sum_growth_obs_(100→1000)': int(growth_obs.sum()), 'sum_growth_exp': round(float(growth_exp.sum()), 1),
                         'primes_with_zero_growth': int((growth_obs == 0).sum()), 'of': len(rows), 'rows(p,S100,E100,S1000,E1000)': rows[:6]}
json.dump(out, open('data/z52b/pass1/U00/fix6.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str))
