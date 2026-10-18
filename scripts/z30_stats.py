"""O260: variance decomposition of R(p) against the main terms of z30_rgen.c output
(columns: n R M0 M2 Mg Mg_small M0_small npairs [Mloc Rsmooth]).  usage: z30_stats.py file [file...]"""
import sys, numpy as np
for f in sys.argv[1:]:
    d = np.loadtxt(f); n, R = d[:, 0], d[:, 1]
    cols = [("M0", d[:, 2]), ("M2", d[:, 3]), ("Mg", d[:, 4])]
    if d.shape[1] > 8: cols.append(("Mloc", d[:, 8]))
    print("%s  N=%d  p in [%d,%d]  mean R=%.2f var R=%.2f  min R=%d" % (f, len(R), n.min(), n.max(), R.mean(), R.var(), R.min()))
    for nm, m in cols:
        e = R - m
        print("  %-5s mean=%.2f  var(R-M)=%.2f  var/meanM=%.2f  corr(R,M)=%.3f" % (nm, m.mean(), e.var(), e.var() / m.mean(), np.corrcoef(R, m)[0, 1]))
    if d.shape[1] > 9:
        Ml, Rs = d[:, 8], d[:, 9]
        print("  residual var / 2*mean(Mloc-Rsmooth) = %.3f   (mean Rsmooth %.2f)" % ((R - Ml).var() / (2 * (Ml - Rs).mean()), Rs.mean()))
