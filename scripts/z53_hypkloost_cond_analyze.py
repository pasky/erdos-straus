"""Analyse z53_hypkloost_conductor.c output: variance decomposition of the conductor pieces.

For each dataset (primes, odd squares, near-square primes, random n = 1 mod 4) we report, per
relative depth bin k = floor(log2(q/d)) (k = 0: top conductor d = q) and per absolute dyadic bin
j = floor(log2 d): mean, sd, and the variance decomposition Var(N) = sum_k Var(P_k) + 2 sum_{k<l} Cov.
Usage: uv run --with numpy python scripts/z53_hypkloost_cond_analyze.py /tmp/hk  > data/z53/hypkloost/cond_stats.txt
"""
import sys, numpy as np
NA = NR = 40
d = sys.argv[1]
sets = ["p12", "rn12", "ns12", "sq12", "p10", "rn10", "sq10"]
for s in sets:
    try:
        A = np.loadtxt(f"{d}/c_{s}.tsv")
    except OSError:
        continue
    n = A[:, 0]; N = A[:, 1]; tot = A[:, 2]
    Pa = A[:, 3:3 + NA]; Pr = A[:, 3 + NA:3 + NA + NR]
    print(f"=== {s}: {len(n)} values, n in [{int(n.min())}, {int(n.max())}]")
    print(f"  mean N = {N.mean():.4f}, var N = {N.var():.4f}, max|sum-N| = {np.abs(tot-N).max():.2e}")
    for name, P in (("rel k=log2(q/d)", Pr), ("abs j=log2 d", Pa)):
        used = [i for i in range(P.shape[1]) if np.abs(P[:, i]).max() > 1e-12]
        C = np.cov(P[:, used].T, bias=True)
        diag = np.trace(C); off = C.sum() - diag
        print(f"  [{name}] sum_k Var(P_k) = {diag:.4f}; 2*sum Cov = {off:+.4f}; Var(total) = {C.sum():.4f}")
        print("   bin    mean        sd      corr(P,N)  share_of_sumVar")
        for i in used:
            sd = P[:, i].std()
            cr = np.corrcoef(P[:, i], N)[0, 1] if sd > 0 and N.std() > 0 else float('nan')
            print(f"   {i:3d} {P[:, i].mean():+.5f} {sd:.5f} {cr:+.3f} {P[:, i].var()/diag:.4f}")
        # cumulative partial sums from the top (relative) / bottom (absolute)
    # top-two relative bins vs rest
    top = Pr[:, 0] + Pr[:, 1]
    rest = Pr[:, 2:].sum(axis=1)
    print(f"  top (q/d<4): mean {top.mean():+.4f} sd {top.std():.4f};  rest (q/d>=4): mean {rest.mean():+.4f} sd {rest.std():.4f}; corr(top,rest) {np.corrcoef(top,rest)[0,1]:+.3f}")
    print()
