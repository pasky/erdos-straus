"""Z2983 follow-up: does the conductor-24 step come from the quadratic character (6/p) = (2/p)(3/p)?"""
import json, numpy as np
exec(open('scripts/z52b_p1_U02_o.py').read().split('rng = ')[0])  # P, res, tr/te are defined there
def kr(D, n):
    from sympy import jacobi_symbol
    r = 1; m = n
    while m % 2 == 0:
        m //= 2
        if D % 2 == 0: return 0
        r *= 1 if D % 8 in (1, 7) else -1
    return r if m == 1 else r * jacobi_symbol(D % m, m)
rng2 = np.random.default_rng(0); perm = rng2.permutation(len(P)); tr = perm[: len(P)//2]; te = perm[len(P)//2:]
base_cols = [np.ones(len(P))]
units = lambda q: [r for r in range(1, q) if np.gcd(r, q) == 1]
for q in (8, 3):
    for r in units(q)[:-1]:
        base_cols.append((P % q == r).astype(float))
def fit(cols):
    Z = np.column_stack(cols)
    c = np.linalg.lstsq(Z[tr], res[tr], rcond=None)[0]; pred = Z @ c
    return round(float(1 - np.sum((res[te] - pred[te])**2) / np.sum((res[te] - res[te].mean())**2)), 4)
chi6 = np.array([kr(6, int(p)) for p in P], float)
chi2 = np.array([kr(2, int(p)) for p in P], float); chi3 = np.array([kr(-3, int(p)) for p in P], float)
out = {'mod8+mod3 additive': fit(base_cols), 'plus (6/p)': fit(base_cols + [chi6]),
       'plus (2/p)(-3/p) (same as (6/p) for p=1 mod 4)': fit(base_cols + [chi2 * chi3]),
       'plus (2/p) only': fit(base_cols + [chi2]), 'plus (-3/p) only': fit(base_cols + [chi3]),
       'corr(resU, (6/p))': round(float(np.corrcoef(res, chi6)[0, 1]), 4)}
print(out); json.dump(out, open('data/z52b/pass1/U02/Z2983_chi6.json', 'w'), indent=1)
