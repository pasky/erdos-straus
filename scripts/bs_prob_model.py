"""O142(b) brainstorm: statistics of f_II(p) and of g(p) = #distinct (a,d) clusters, primes <= 1e8.
Input: /tmp/fII_1e8.bin from scripts/bs_prob_fII.c (triples uint32 p, f_II(p), g(p)).
Prints dyadic summaries, local-data (mod 840 / 9240 / 120120) explained variance, dispersion
indices inside cells, and Poisson-cluster predictions for min and for #{f=0}.
Run: PYTHONPATH=scripts uv run python scripts/bs_prob_model.py [file]"""
import sys
import numpy as np

fn = sys.argv[1] if len(sys.argv) > 1 else '/tmp/fII_1e8.bin'
A = np.fromfile(fn, dtype=np.uint32).reshape(-1, 3)
p = A[:, 0].astype(np.int64); f = A[:, 1].astype(float); g = A[:, 2].astype(float)
L = np.log(p.astype(float))
sel = p >= 10**4
p, f, g, L = p[sel], f[sel], g[sel], L[sel]
k = np.floor(np.log2(p)).astype(int)

print("== dyadic: n, mean f/L^3, CV(f/L^3), min f/L^3, mean g/L^2, CV(g/L^2), min g/L^2, min g, Var(g)/E(g)")
for kk in range(14, 27):
    m = k == kk
    if m.sum() < 100: continue
    r = f[m]/L[m]**3; s = g[m]/L[m]**2
    print(f"2^{kk}: {m.sum():8d} {r.mean():.4f} {r.std()/r.mean():.3f} {r.min():.4f} | "
          f"{s.mean():.4f} {s.std()/s.mean():.3f} {s.min():.4f} {int(g[m].min()):4d} {g[m].var()/g[m].mean():.2f}")

def cell_stats(Q, kk_lo, kk_hi, x, label):
    """Fraction of variance of x explained by p mod Q within dyadic ranges; residual dispersion."""
    tot = 0.0; res = 0.0; disp_num = 0.0; disp_den = 0.0
    for kk in range(kk_lo, kk_hi+1):
        m = k == kk
        xs = x[m]; cls = p[m] % Q
        uniq, inv, cnt = np.unique(cls, return_inverse=True, return_counts=True)
        sums = np.bincount(inv, weights=xs); means = sums/cnt
        fit = means[inv]
        tot += ((xs - xs.mean())**2).sum(); res += ((xs - fit)**2).sum()
        ok = cnt[inv] >= 20
        disp_num += ((xs - fit)[ok]**2).sum(); disp_den += fit[ok].sum()
    print(f"  {label} Q={Q}: R^2={1-res/tot:.3f}  within-cell Var/Mean={disp_num/disp_den:.2f}")

print("== local data: share of variance explained by p mod Q (2^22..2^26), raw counts")
for Q in (24, 840, 9240, 120120):
    cell_stats(Q, 22, 26, f, "f")
    cell_stats(Q, 22, 26, g, "g")
