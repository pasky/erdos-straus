"""Z2983: explained variance of residual log U (p=1 mod 4, 100<p<=30000) by residue-class indicators mod q (equivalently all
Dirichlet characters mod q), cumulative over q = 3,4,...,24 ; sample the fit with a train/test split."""
import sys, json, numpy as np
exec(open('scripts/z52b_p1_U02_m.py').read().split('sel = isp')[0])  # loaders: n_all, U, isp
sel = isp[n_all] & (n_all % 4 == 1) & (n_all > 100)
P = n_all[sel]; lU = np.log(U[sel]); lp = np.log(P)
X = np.column_stack([np.ones_like(lp), lp, np.log(lp)])
res = lU - X @ np.linalg.lstsq(X, lU, rcond=None)[0]
rng = np.random.default_rng(0); perm = rng.permutation(len(P)); tr = perm[: len(P) // 2]; te = perm[len(P) // 2:]
out = []
cols = [np.ones(len(P))]
for q in range(3, 25):
    for r in range(q):
        if np.gcd(r, q) != 1: continue
    # residue-class indicators mod q (units only are enough for characters; use all classes r with gcd(r,q)=1 minus one)
    units = [r for r in range(1, q) if np.gcd(r, q) == 1]
    for r in units[:-1]:
        cols.append((P % q == r).astype(float))
    Z = np.column_stack(cols)
    c = np.linalg.lstsq(Z[tr], res[tr], rcond=None)[0]
    pred = Z @ c
    r2_test = 1 - np.sum((res[te] - pred[te])**2) / np.sum((res[te] - res[te].mean())**2)
    r2_in = 1 - np.sum((res[tr] - pred[tr])**2) / np.sum((res[tr] - res[tr].mean())**2)
    out.append((q, Z.shape[1], round(float(r2_in), 4), round(float(r2_test), 4)))
print(out)
json.dump(out, open('data/z52b/pass1/U02/Z2983_var.json', 'w'))
