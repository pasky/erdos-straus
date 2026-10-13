"""R187: asymptotic growth rate of the 'fine' Case B pattern bound of Lemma 2.2's proof (EVIDENCE / optimisation aid).
Per unit s, in units of log q (l2 = log2/log q, l3 = log3/log q), pattern fractions m=min(a,b), M=max(a,b), z, y, t
(m+M+z = 1, y+t <= M, m <= M):
  e1 = t + l3, e2 = (y+z)(1+l2) + l2(1+2y+z), e3 = m+y + l2(1+y), e4 = m+z + l2*max(1, z+2m);
rate(q) = max over patterns of min(e1..e4) - 1/2 (the cylinder weight q^{-s/2}).  The Case B series converges
(geometrically) iff rate < 0.  Grid search."""
import numpy as np
from math import log
G = 120
for r in ([] if __import__("sys").argv[1:] else [10, 12, 14, 16, 18, 20, 22, 24, 26, 27]):
    l2, l3 = log(2) / (r * log(3)), log(3) / (r * log(3))
    best = -9
    g = np.linspace(0, 1, G + 1)
    for m in g:
        for z in g:
            M = 1 - m - z
            if M < m - 1e-12:
                continue
            y = g[g <= M + 1e-12][:, None]
            t = g[None, :]
            ok = (y + t <= M + 1e-12)
            e1 = t + l3 + 0 * y
            e2 = (y + z) * (1 + l2) + l2 * (1 + 2 * y + z) + 0 * t
            e3 = m + y + l2 * (1 + y) + 0 * t
            e4 = m + z + l2 * max(1, z + 2 * m) + 0 * y + 0 * t
            v = np.minimum(np.minimum(e1, e2), np.minimum(e3, e4))
            v = np.where(ok, v, -9)
            best = max(best, v.max())
    print(f"q = 3^{r}: rate = {best - 0.5:+.4f}  (stated-B rate: {4 * log(2) / (r * log(3)) - 0.1:+.4f})")


def fine_sum(r, SMAX):
    """numpy version of review_da2_largeq.caseB_s(fine=True), summed over 3 <= s <= SMAX; returns per-s list."""
    lq = r * log(3)
    L2, L3 = log(2), log(3)
    out = []
    for s in range(3, SMAX + 1):
        off = (1 - (s + 1) // 2) * lq
        acc = 0.0
        for a in range(1, s):
            for b in range(1, s - a + 1):
                z = s - a - b
                m, M = min(a, b), max(a, b)
                y = np.arange(0, M - 1)[:, None]
                t = np.arange(2, M + 1)[None, :]
                ok = (y + t <= M)
                e = np.minimum(np.minimum(L2 + (t - 2) * lq + s * L3,
                                          (y + z) * lq + (y + z) * L2 + (s + 2 * y + z) * L2),
                               np.minimum((m - 1 + y) * lq + (s + y) * L2,
                                          (m - 1 + z) * lq + max(s, z + 2 * m) * L2 + 0 * y))
                acc += np.exp(np.where(ok, e + off, -1e9)).sum()
        out.append(acc)
    return out


if __name__ == '__main__':
    import sys
    SM = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    for r in ([int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else []):
        ps = fine_sum(r, SM)
        print(f"q=3^{r}: fine Case B sum s<= {SM}: {sum(ps):.3e}; last per-s terms {ps[-3]:.2e} {ps[-2]:.2e} {ps[-1]:.2e}",
              flush=True)
