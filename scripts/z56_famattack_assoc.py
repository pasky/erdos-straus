# z56 FAMATTACK falsifier F1: cross-window association of exact (★) window counts across primes.
# Input: wcount output lines "p R g00..g44" (g[ia*5+ic]); ia = u-bin (a = log u/log p in steps of .1), ic = C-bin.
# Pre-registered primary statistic: pooled within-stratum (p mod 840) Pearson correlation of u-window counts W_k.
# Secondary: OLS residual correlation after one-hot residues of p mod l (l in 8,3,5,7,11,...,31);
#            Mantel-Haenszel odds ratios of the zero events [W_k = 0] within p mod 840 strata;
#            same for C-windows V_c.
import sys, numpy as np

def load(fn):
    a = np.loadtxt(fn, dtype=np.int64)
    p = a[:, 0]; R = a[:, 1]; g = a[:, 2:27].reshape(-1, 5, 5)
    return p, R, g

def within_center(X, strata):
    Xc = X.astype(float).copy()
    for s in np.unique(strata):
        m = strata == s
        Xc[m] -= Xc[m].mean(axis=0)
    return Xc

def corr_matrix(Xc):
    sd = Xc.std(axis=0)
    C = (Xc.T @ Xc) / len(Xc) / np.outer(sd, sd)
    return C

def ols_resid(X, p, ells=(8, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)):
    cols = [np.ones(len(p))]
    for l in ells:
        r = p % l
        vals = np.unique(r)
        for v in vals[1:]:
            cols.append((r == v).astype(float))
    A = np.column_stack(cols)
    coef, *_ = np.linalg.lstsq(A, X.astype(float), rcond=None)
    return X - A @ coef, A.shape[1]

def mh_odds(z1, z2, strata):
    num = den = 0.0
    for s in np.unique(strata):
        m = strata == s; n = m.sum()
        a = np.sum(z1[m] & z2[m]); b = np.sum(z1[m] & ~z2[m]); c = np.sum(~z1[m] & z2[m]); d = np.sum(~z1[m] & ~z2[m])
        num += a * d / n; den += b * c / n
    return num / den if den > 0 else float('nan')

def main(fn):
    p, R, g = load(fn)
    N = len(p)
    W = g.sum(axis=2)  # u-windows
    V = g.sum(axis=1)  # C-windows
    strata = p % 840
    print(f"# file {fn}: N = {N} primes, p in [{p.min()}, {p.max()}], zeros R=0: {(R == 0).sum()}")
    print("# mean u-window counts W_k:", np.round(W.mean(0), 3), " var/mean:", np.round(W.var(0) / W.mean(0), 3))
    print("# mean C-window counts V_c:", np.round(V.mean(0), 3), " var/mean:", np.round(V.var(0) / V.mean(0), 3))
    print("# mean unordered total:", round((R / 2).mean(), 3), " var/mean:", round((R / 2).var() / (R / 2).mean(), 3))
    se = 1 / np.sqrt(N)
    for name, X in (("u-windows", W), ("C-windows", V)):
        raw = np.corrcoef(X.T.astype(float))
        Cw = corr_matrix(within_center(X, strata))
        Xr, k = ols_resid(X, p)
        Co = corr_matrix(Xr - Xr.mean(0))
        print(f"## {name}: pairwise correlations  raw | within p mod 840 | OLS({k} cols); s.e. ~ {se:.4f}")
        for i in range(5):
            for j in range(i + 1, 5):
                print(f"  ({i},{j})  {raw[i,j]:+.4f} | {Cw[i,j]:+.4f} (z={Cw[i,j]/se:+.1f}) | {Co[i,j]:+.4f} (z={Co[i,j]/se:+.1f})")
        Z = X == 0
        print(f"## {name}: zero-event rates", np.round(Z.mean(0), 4))
        for i in range(5):
            for j in range(i + 1, 5):
                if 0.01 < Z[:, i].mean() < 0.99 and 0.01 < Z[:, j].mean() < 0.99:
                    pi, pj, pij = Z[:, i].mean(), Z[:, j].mean(), (Z[:, i] & Z[:, j]).mean()
                    print(f"  zero ({i},{j}): P(both)={pij:.4f} prod={pi*pj:.4f} ratio={pij/(pi*pj):.3f}  MH-OR(mod 840)={mh_odds(Z[:, i], Z[:, j], strata):.3f}")
    # sum-of-windows vs total variance decomposition
    tot = W.sum(1).astype(float)
    Wc = within_center(W, strata)
    cov_off = (Wc.T @ Wc / N); offsum = cov_off.sum() - np.trace(cov_off)
    print(f"# within-stratum var(total) = {Wc.sum(1).var():.3f}; sum of window vars = {np.trace(cov_off):.3f}; off-diagonal cov sum = {offsum:+.3f}")

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        main(fn)
