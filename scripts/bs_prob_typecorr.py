"""O142(b) add-on: is there a 'conservation law' (negative correlation) between f_I(p) and f_II(p)?
Inputs: /tmp/fII5_3e7.bin (scripts/bs_prob_fII.c, 5 fields) and /tmp/r123_3e7_fI.bin
(scripts/review_r123_count.c 30000000 /tmp/r123_3e7: uint32 f_I(n) for all n <= 3e7, R123 normalisation).
Correlations of log-ratios after removing cell means (class mod 120120 x dyadic range).
Run: uv run python scripts/bs_prob_typecorr.py"""
import numpy as np
A = np.fromfile('/tmp/fII5_3e7.bin', dtype=np.uint32).reshape(-1, 5).astype(np.int64)
fI_all = np.fromfile('/tmp/r123_3e7_fI.bin', dtype=np.uint32)
p, f2 = A[:, 0], A[:, 1].astype(float)
m = p >= 2**20; p, f2 = p[m], f2[m]; f1 = fI_all[p].astype(float)
k = np.floor(np.log2(p)).astype(int)
def resid(x, Q):
    out = np.zeros(len(x))
    for kk in np.unique(k):
        mm = k == kk; u, inv, c = np.unique(p[mm] % Q, return_inverse=True, return_counts=True)
        out[mm] = x[mm] - (np.bincount(inv, weights=x[mm]) / c)[inv]
    return out
x1, x2 = np.log(f1), np.log(f2)
print("raw corr(log f_I, log f_II) = %.3f" % np.corrcoef(x1, x2)[0, 1])
for Q in (24, 840, 120120):
    print("within cells mod %d: corr = %.3f" % (Q, np.corrcoef(resid(x1, Q), resid(x2, Q))[0, 1]))
s = f1 + f2; print("CV: f_I %.3f  f_II %.3f  f_I+f_II %.3f" % (f1.std()/f1.mean(), f2.std()/f2.mean(), s.std()/s.mean()))
i = np.argmin(f1); j = np.argmin(f2)
print("argmin f_I: p=%d f_I=%d f_II=%d ; argmin f_II: p=%d f_I=%d f_II=%d" % (p[i], f1[i], f2[i], p[j], f1[j], f2[j]))
# --- common driver? truncated L(1, chi_p) with chi_p(l) = (l/p) Legendre, via reciprocity
def primes_upto(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
for Y in (30, 300, 3000):
    logL = np.zeros(len(p))
    for l in primes_upto(Y):
        l = int(l)
        if l == 2:
            chi = np.where((p % 8 == 1) | (p % 8 == 7), 1.0, -1.0)
        else:
            qr = np.zeros(l, bool); qr[(np.arange(1, l)**2) % l] = True
            leg = np.where(qr[p % l], 1.0, -1.0)            # (p/l)
            sign = np.where(((l-1)//2) * ((p-1)//2) % 2 == 1, -1.0, 1.0)
            chi = leg * sign                                 # (l/p)
        logL += -np.log1p(-chi / l)
    for nm, x in (("log f_I", x1), ("log f_II", x2)):
        print("Y=%d corr(%s, log L_Y(1,chi_p)): raw %.3f, within mod-24 cells %.3f" %
              (Y, nm, np.corrcoef(x, logL)[0, 1], np.corrcoef(resid(x, 24), resid(logL, 24))[0, 1]))
