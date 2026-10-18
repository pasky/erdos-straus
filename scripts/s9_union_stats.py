"""s9_union_stats.py (O271): (★) vs b = 1 in word coordinates, from s9_words output (p W A B U A1), p == 1 (mod 4).
Residuals: within each (window of 2000 consecutive primes == 1 mod 4) x (p mod 24 class), standardise A and B.
Reports: Pearson/Spearman correlation of residuals; conditional mean of B/E[B|cell] for low-A primes and of A for low-B;
min U/W; p with smallest U/W.   usage: python s9_union_stats.py FILE
"""
import sys
import numpy as np

def main():
    d = np.loadtxt(sys.argv[1], dtype=np.int64)
    d = d[d[:, 0] % 4 == 1]
    p, W, A, B, U = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4]
    win = np.arange(len(p)) // 2000
    cls = p % 24
    zA = np.zeros(len(p)); zB = np.zeros(len(p)); rA = np.zeros(len(p)); rB = np.zeros(len(p))
    for w in np.unique(win):
        for c in np.unique(cls):
            m = (win == w) & (cls == c)
            if m.sum() < 20:
                continue
            for x, z, r in ((A, zA, rA), (B, zB, rB)):
                mu, sd = x[m].mean(), x[m].std()
                z[m] = (x[m] - mu) / sd; r[m] = x[m] / mu
    ok = (zA != 0) | (zB != 0)
    print(f"primes p == 1 (4) <= {p.max()}: {len(p)};  cells used: {ok.sum()}")
    print(f"Pearson corr(zA, zB) = {np.corrcoef(zA[ok], zB[ok])[0,1]:.3f}")
    rk = lambda x: np.argsort(np.argsort(x))
    print(f"Spearman corr(A/E, B/E) = {np.corrcoef(rk(rA[ok]), rk(rB[ok]))[0,1]:.3f}")
    for thr in (0, 2, 4, 8):
        m = ok & (A <= thr)
        print(f"A <= {thr}: {m.sum()} primes, mean B/E[B|cell] = {rB[m].mean():.3f}, frac B/E < 0.5: {(rB[m] < 0.5).mean():.3f}")
    for thr in (0, 2, 4, 8):
        m = ok & (B <= thr)
        print(f"B <= {thr}: {m.sum()} primes, mean A/E[A|cell] = {rA[m].mean():.3f}")
    q = np.quantile(rA[ok], 0.01)
    m = ok & (rA <= q)
    print(f"bottom 1% of A/E (<= {q:.3f}): mean B/E = {rB[m].mean():.3f}; overall mean B/E = {rB[ok].mean():.3f}")
    fr = U / W
    i = np.argsort(fr)[:8]
    print("smallest U/W:", [(int(p[j]), int(W[j]), int(U[j]), round(float(fr[j]), 3)) for j in i])
    print(f"mean U/W = {fr.mean():.3f}; mean A/W = {(A/W).mean():.3f}; mean B/W = {(B/W).mean():.3f}; overlap mean (A+B-U)/W = {((A+B-U)/W).mean():.3f}")

if __name__ == "__main__":
    main()

def partial(fname):
    """partial correlations: residualise A, B on features by least squares; features = one-hot(p mod 840), log p,
    log of 50-smooth parts of p-1 and p+1, and (optionally) log W (total words)."""
    d = np.loadtxt(fname, dtype=np.int64); d = d[d[:, 0] % 4 == 1]
    p, W, A, B = d[:, 0], d[:, 1].astype(float), d[:, 2].astype(float), d[:, 3].astype(float)
    def smooth(x):
        s = np.ones(len(x))
        for l in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            y = x.copy()
            while True:
                m = (y % l == 0)
                if not m.any(): break
                s[m] *= l; y[m] //= l
        return np.log(s)
    cl = p % 840; cats = np.unique(cl)
    oh = (cl[:, None] == cats[None, :]).astype(float)
    L = np.log(p)
    base = [oh, (L**2)[:, None], L[:, None], smooth(p - 1)[:, None], smooth(p + 1)[:, None]]
    for tag, extra in (("class mod 840 + log p + smooth(p+-1)", []), ("... + log W", [np.log(W)[:, None]])):
        X = np.hstack(base + extra)
        res = []
        for y in (A / L**2, B / L**2):
            beta, *_ = np.linalg.lstsq(X, y, rcond=None); res.append(y - X @ beta)
        print(f"partial corr(A, B | {tag}) = {np.corrcoef(res[0], res[1])[0,1]:.3f}")

if len(sys.argv) > 2 and sys.argv[2] == "partial":
    partial(sys.argv[1])
