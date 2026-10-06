"""O53 §6: sawtooth test function g(x) = sum_{d<=D} d*(c(x,d) - N/d): window sum, its
positive part, max over the near zone Z (C=2), and E|g| (RMS bound sqrt(E g^2) <= D^1.5/2)."""
import sys
import numpy as np
for N in map(int, sys.argv[1:]):
    D = N // 2; C = 2
    xs = np.arange(int(N - C * N) - 1, int(C * N) + 3)
    g = np.zeros(len(xs))
    for d in range(1, D + 1):
        r = N % d
        b = xs % d
        c = N // d + ((b >= 1) & (b <= r))
        g += d * (c - N / d)
    W = (xs >= 1) & (xs <= N); Z = ~W
    print(f"N={N}: sum_W g={g[W].sum():.0f} (D^3/27={D**3/27:.0f}) sum_W g+={np.clip(g[W],0,None).sum():.0f} "
          f"sum_W g-={np.clip(-g[W],0,None).sum():.0f}  max_Z g={g[Z].max():.0f} (D^1.5={D**1.5:.0f}, D^2/54={D*D/54:.0f})")
