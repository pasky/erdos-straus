# z52d pass2 TO1 lint-fix part 3: is the Legendre-symbol residual effect on log #ES(p) significant?
# model: log #ES(p) = class effect (p mod 24) + b5*(p/5) + b7*(p/7) + b3*(p/3) + noise; OLS with SE, primes 1 mod 4 > 1000 below 1e5.
import numpy as np
from sympy import legendre_symbol
rows = [l.split() for l in open('data/z52b/pass2/TO1/es_100000.tsv')]
P = np.array([int(r[0]) for r in rows]); C = np.array([int(r[1]) for r in rows])
m = P > 1000; P = P[m]; y = np.log(C[m])
cls = P % 24
D = np.zeros((len(P), 24)); D[np.arange(len(P)), cls] = 1
L = {q: np.array([legendre_symbol(int(p) % q, q) if int(p) % q else 0 for p in P]) for q in (3,5,7,11,13)}
def fit(cols, names):
    X = np.column_stack([D] + cols)
    beta, res, rk, sv = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    s2 = (r @ r) / (len(y) - X.shape[1])
    cov = s2 * np.linalg.pinv(X.T @ X)
    k = D.shape[1]
    out = {}
    for i, nm in enumerate(names):
        out[nm] = (round(float(beta[k+i]),4), round(float(np.sqrt(cov[k+i,k+i])),4))
    return out, round(float(1 - (r@r)/((y-y.mean())@(y-y.mean()))),4)
print('p mod 24 classes only (R^2 baseline):', fit([], [])[1])
print('+ (p/5),(p/7),(p/11),(p/13):', fit([L[5].astype(float), L[7].astype(float), L[11].astype(float), L[13].astype(float)], ['(p/5)','(p/7)','(p/11)','(p/13)']))
# control: same symbols after absorbing p mod 120 (or mod 840) classes; if symbols are congruence effects they should vanish
for MOD in (120, 840):
    cls2 = P % MOD
    cl_ids = {c:i for i,c in enumerate(sorted(set(cls2)))}
    D2 = np.zeros((len(P), len(cl_ids))); 
    for i,c in enumerate(cls2): D2[i, cl_ids[c]] = 1
    X = np.column_stack([D2] + [L[5].astype(float), L[7].astype(float), L[11].astype(float)])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]; r = y - X@beta
    s2 = (r@r)/(len(y)-X.shape[1]); cov = s2*np.linalg.pinv(X.T@X); k = D2.shape[1]
    print(f'p mod {MOD} classes ({len(cl_ids)} used, mean size {len(P)/len(cl_ids):.1f}) + (p/5),(p/7),(p/11):',
          {n:(round(float(beta[k+i]),4), round(float(np.sqrt(cov[k+i,k+i])),4)) for i,n in enumerate(['(p/5)','(p/7)','(p/11)'])})
