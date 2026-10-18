"""R277: statistics from logs/review_r277_p1mod4_4e5.txt (own engine output: p R M0 M2 Mgen MQ)."""
import numpy as np, math
d = np.loadtxt('logs/review_r277_p1mod4_4e5.txt')
p, R, M0, M2, Mg, MQ = d.T
print("primes", len(p), "failures (R=0):", p[R == 0].astype(int).tolist())
sel = (p >= 1e5) & (p < 4e5)
print("N in [1e5,4e5):", sel.sum(), "mean R", R[sel].mean())
for name, M in [("M0", M0), ("M2", M2), ("Mgen", Mg), ("MQ720720", MQ)]:
    r = R[sel] - M[sel]
    print(f"{name:9s} var(R-M)/(2 mean M) = {r.var()/(2*M[sel].mean()):.3f}  mean(var/2M per-p) = {np.mean(r**2/(2*M[sel])):.3f}"
          f"  corr = {np.corrcoef(R[sel], M[sel])[0,1]:.3f}  mean(R-M) = {r.mean():.2f}")
# NB lower-tail ranking: P(0) monotone decreasing in mean for fixed D -> rank by M ascending
for name, M in [("M0", M0), ("Mgen", Mg), ("MQ", MQ)]:
    order = np.argsort(M)
    top = [(int(p[i]), round(float(M[i]), 2), int(R[i])) for i in order[:8]]
    print(name, "8 smallest main terms (p, M, R):", top)
# genus share of failures
for f in p[R == 0]:
    i = np.where(p == f)[0][0]
    print(int(f), "Mgen/M0 = %.2f  MQ/M0 = %.2f" % (Mg[i] / M0[i], MQ[i] / M0[i]))
# rank of each failure among primes within a factor-2 window around it (risk ~ smallest M / local mean)
print("rank of failures by M/median(M in [p/2, 2p]) among primes p ≡ 1 (4) in [p/2, 2p]:")
for f in p[R == 0]:
    w = (p >= f / 2) & (p <= 2 * f)
    out = []
    for name, M in [("M0", M0), ("Mgen", Mg), ("MQ", MQ)]:
        rel = M[w] / np.median(M[w])
        mine = M[p == f][0] / np.median(M[w])
        out.append(f"{name}: {int((rel < mine).sum()) + 1}/{w.sum()}")
    print(int(f), "  ".join(out))
