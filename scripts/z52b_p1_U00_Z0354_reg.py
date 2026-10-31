# z52b pass1 U00 Z0354: does D(p) (# of M ≤ 1000 with p a square mod M) add to the character model for log(U+1)?
import numpy as np, json
from sympy import primerange, legendre_symbol
from scipy.stats import spearmanr
R = '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
Ud = dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))
P = [p for p in primerange(5, 30001) if p % 4 == 1]
Qs = [q for q in primerange(3, 80)]
D = []
sqs = {M: set((x * x) % M for x in range(M)) for M in range(2, 1001)}
for p in P:
    D.append(sum(1 for M in range(2, 1001) if p % M in sqs[M]))
D = np.array(D, float)
y = np.log(np.array([Ud[p] for p in P], float) + 1)
lp = np.log(P)
base = [np.ones(len(P)), lp, np.log(lp)]
chars = []
for q in Qs:
    chars.append(np.array([legendre_symbol(p % q, q) if p % q else 0 for p in P], float))
def fit(cols):
    X = np.column_stack(cols)
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    return b, 1 - r.var() / y.var()
b0, r2_0 = fit(base + chars)
b1, r2_1 = fit(base + chars + [D])
b2, r2_2 = fit(base + [D])
sdD = D.std()
res = {'n_primes': len(P), 'R2_base_chars': r2_0, 'R2_base_chars_plus_D': r2_1, 'R2_gain_D': r2_1 - r2_0,
       'coef_D_per_sd': float(b1[-1] * sdD), 'R2_D_plus_logp_only': r2_2,
       'spearman_D_resid': float(spearmanr(D, y - np.column_stack(base + chars) @ b0).correlation)}
json.dump(res, open('data/z52b/pass1/U00/Z0354_reg.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
# control: divisors of p-1 up to 1000 (the 'class of one' count) and of p+... ; does D add beyond it?
Dv = np.array([sum(1 for M in range(2, 1001) if (p - 1) % M == 0) for p in P], float)
b3, r2_3 = fit(base + chars + [Dv])
b4, r2_4 = fit(base + chars + [Dv, D])
res2 = {'R2_base_chars_plus_divisors_of_p-1_le1000': r2_3, 'R2_plus_both': r2_4, 'gain_D_beyond_divisors': r2_4 - r2_3,
        'spearman_D_vs_divisors_of_p-1': float(spearmanr(D, Dv).correlation)}
json.dump({**res, **res2}, open('data/z52b/pass1/U00/Z0354_reg.json', 'w'), indent=1)
print(json.dumps(res2, indent=1))
# control 2: add 2-adic classes (p mod 8, 16, 32 indicators) and prime-power characters q^2 ≤ 80 (= same as q); does D still add?
tw = [np.array([1.0 if p % m == 1 else 0.0 for p in P]) for m in (8, 16, 32)] + [np.array([1.0 if p % m == 1 else 0.0 for p in P]) for m in (3, 5, 7, 9, 11, 13, 17, 19, 23, 25)]
b5, r2_5 = fit(base + chars + tw)
b6, r2_6 = fit(base + chars + tw + [D])
res3 = {'R2_chars_plus_2adic_and_classes_of_one': r2_5, 'R2_plus_D': r2_6, 'gain_D_after_2adic_classes': r2_6 - r2_5,
        'coef_D_per_sd_after_controls': float(b6[-1] * sdD)}
json.dump({**res, **res2, **res3}, open('data/z52b/pass1/U00/Z0354_reg.json', 'w'), indent=1)
print(json.dumps(res3, indent=1))
