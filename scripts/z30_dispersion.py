"""O260: residual dispersion var(R - M)/(2 mean M) (swap-Poisson baseline = 1) per main term, on a p-range.
usage: z30_dispersion.py file lo hi   (z30_rgen output with MQ column)"""
import sys, numpy as np
d = np.loadtxt(sys.argv[1]); lo, hi = float(sys.argv[2]), float(sys.argv[3])
d = d[(d[:, 0] >= lo) & (d[:, 0] < hi)]; R = d[:, 1]
print("%s p in [%g,%g) N=%d mean R=%.2f" % (sys.argv[1], lo, hi, len(R), R.mean()))
for nm, c in [("M0", 2), ("M2", 3), ("Mgen", 4), ("MQ", 10)]:
    M = d[:, c]; e = R - M
    print("  %-5s mean=%.2f  var(R-M)/(2 mean M)=%.3f  corr(R,M)=%.3f  mean(R-M)=%.2f" % (nm, M.mean(), e.var() / (2 * M.mean()), np.corrcoef(R, M)[0, 1], e.mean()))
