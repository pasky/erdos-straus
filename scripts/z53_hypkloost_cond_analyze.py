"""Analyse z53_hypkloost_conductor.c output: variance decomposition of the conductor pieces.

For each dataset (primes, odd squares, near-square primes, random n = 1 mod 4) we report, per
relative depth bin k = floor(log2(q/d)) (k = 0: top conductor d = q) and per absolute dyadic bin
j = floor(log2 d): mean, sd, and the decomposition Var(N) = sum Var(P) + sum_{k != l} Cov, with the
cross-covariance share (sum_{k!=l} Cov)/(sum Var) and a percentile bootstrap (400 resamples,
numpy default_rng(53), datasets processed in the order below, relative bins first, then absolute bins).
NOTE (review F06): only ABSOLUTE conductor bins are Parseval-orthogonal, and only under n uniform over all
residues mod L; relative bins share conductors across pairs, and primes / n = 1 (4) are conditioned measures.
Reads data/z53/hypkloost/c_<set>.tsv.gz (columns: n, N, total, 40 absolute bins, 40 relative bins).
Usage: uv run --with numpy python scripts/z53_hypkloost_cond_analyze.py data/z53/hypkloost > data/z53/hypkloost/cond_stats.txt
"""
import sys, numpy as np
NA = NR = 40
d = sys.argv[1]
sets = ["p12", "rn12", "ns12", "sq12", "p10", "rn10", "sq10"]
rng = np.random.default_rng(53)

def share(P, idx):
    C = np.cov(P[idx].T, bias=True); dg = np.trace(C)
    return (C.sum() - dg) / dg, dg, C.sum()

for s in sets:
    try:
        A = np.loadtxt(f"{d}/c_{s}.tsv.gz")
    except OSError:
        continue
    n = A[:, 0]; N = A[:, 1]; tot = A[:, 2]
    Pa = A[:, 3:3 + NA]; Pr = A[:, 3 + NA:3 + NA + NR]
    print(f"=== {s}: {len(n)} values, n in [{int(n.min())}, {int(n.max())}]")
    print(f"  mean N = {N.mean():.4f}, var N = {N.var():.4f}, frac N=0 = {(N==0).mean():.3f}, max|total-N| = {np.abs(tot-N).max():.2e}")
    for name, P in (("rel k=log2(q/d)", Pr), ("abs j=log2 d", Pa)):
        used = [i for i in range(P.shape[1]) if np.abs(P[:, i]).max() > 1e-12]
        sh, dg, tv = share(P[:, used], np.arange(len(N)))
        if N.var() > 0:
            bs = [share(P[:, used], rng.integers(0, len(N), len(N)))[0] for _ in range(400)]
            lo, hi = np.percentile(bs, [2.5, 97.5])
            ci = f"[{lo:+.3f}, {hi:+.3f}]"
        else:
            ci = "(Var N = 0)"
        print(f"  [{name}] sum Var = {dg:.4f}; Var(total) = {tv:.4f}; cross-cov share = {sh:+.3f} bootstrap95 {ci}")
        print("   bin    mean        sd      corr(P,N)  share_of_sumVar")
        for i in used:
            sd = P[:, i].std()
            cr = np.corrcoef(P[:, i], N)[0, 1] if sd > 0 and N.std() > 0 else float('nan')
            print(f"   {i:3d} {P[:, i].mean():+.5f} {sd:.5f} {cr:+.3f} {P[:, i].var()/dg:.4f}")
    if N.std() > 0:
        cum = np.cumsum(Pr, axis=1)
        print("  corr(N, P_0+..+P_k), k=0..5: " + " ".join(f"{np.corrcoef(cum[:, k], N)[0, 1]:.3f}" for k in range(6)))
    print()
