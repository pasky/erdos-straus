"""R53 from-scratch recomputation of the SPW2 §6 sawtooth table (exact ints).
g(x) = sum_{d<=D} (d*c(x mod d, d) - N)."""
import sys, numpy as np
def table(N, C=2):
    D = N//2
    xs = np.arange(N - C*N, C*N + 2)          # covers W and Z
    g = np.zeros(len(xs), dtype=np.int64)
    for d in range(1, D+1):
        cnt = np.bincount(np.arange(1, N+1) % d, minlength=d)
        g += d*cnt[np.mod(xs, d)] - N
    W = (xs >= 1) & (xs <= N); Z = ~W
    gw = g[W]
    return gw.sum(), D**3/27, gw[gw > 0].sum(), -gw[gw < 0].sum(), g[Z].max(), D*D/25
for N in map(int, sys.argv[1:] or ["100", "1000", "10000"]):
    print(N, *[f"{v:.4g}" if isinstance(v, float) else int(v) for v in table(N)])
