# z52b pass1 U00 fix (8): control for the witness-closure effect (Z1475): compare P(W_{2C} | W_C) with P(W_{2C} | W_{C'})
# for C' with no multiplicative relation to 2C (C' = C+1, C' = C+3 when odd, and C' = 2C+1). Primes p ≡ 1 mod 4, p < 20000, C ≤ 60.
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
W = np.array([[1 if has_wit(p, C) else 0 for C in range(1, CM + 1)] for p in P1], dtype=np.int8)
np.save('/tmp/u00/W60.npy', W)
def cond(Cx, Cy):   # P(W_{Cy} | W_{Cx}) with 1-based levels
    a = W[:, Cx - 1] == 1
    return float(W[a, Cy - 1].mean()) if a.sum() else None
res = {}
for C in range(1, 16):
    k = 2
    if 2 * C > CM: break
    res[C] = {'P(W_2C)': round(float(W[:, 2 * C - 1].mean()), 4),
              'P(W_2C|W_C)': round(cond(C, 2 * C), 4),
              'P(W_2C|W_(C+1))': round(cond(C + 1, 2 * C), 4) if C + 1 <= CM else None,
              'P(W_2C|W_(2C+1))': round(cond(2 * C + 1, 2 * C), 4) if 2 * C + 1 <= CM else None,
              'P(W_2C|W_(C+3))': round(cond(C + 3, 2 * C), 4) if C + 3 <= CM else None}
# aggregate over C=1..25 (all with 2C ≤ 60)
agg = {}
for key in ['P(W_2C|W_C)', 'P(W_2C|W_(C+1))', 'P(W_2C|W_(2C+1))', 'P(W_2C|W_(C+3))']:
    vals = [v[key] for v in res.values() if v[key] is not None]
    agg[key] = round(float(np.mean(vals)), 4)
agg['P(W_2C) mean'] = round(float(np.mean([v['P(W_2C)'] for v in res.values()])), 4)
out = {'per_C_first8': {k: res[k] for k in list(res)[:8]}, 'mean_over_C': agg, 'n_primes': len(P1)}
json.dump(out, open('data/z52b/pass1/U00/fix8.json', 'w'), indent=1)
print(json.dumps(out))
