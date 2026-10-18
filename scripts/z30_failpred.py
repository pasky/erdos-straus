"""O260: predicted vs observed (★)-failures (R(p)=0) for all primes p ≡ 1 (4), 13 <= p < 4e5, from z30_rgen 30 output.
Models for the unordered count R/2 (negative binomial, mean mu, variance D*mu):
  A: mu = M0/2, D fitted on [1e5,4e5] as var(R-M0)/(2 mean M0)  (no arithmetic of p)
  B: mu = Mg/2, D likewise with Mg
  C: mu = (Mloc30 - Rsmooth)/2, P(fail)=0 if Rsmooth>0, D likewise with residual of Mloc (semi-circular: uses exact smooth hits)
  D: mu = MQ/2 (p mod gcd(q,Q) + genus; bounded modulus Q, non-circular), D likewise."""
import sys, numpy as np
d = np.loadtxt(sys.argv[1]); n, R, M0, Mg, Ml, Rs = d[:, 0], d[:, 1], d[:, 2], d[:, 4], d[:, 8], d[:, 9]
MQ = d[:, 10] if d.shape[1] > 10 else None
obs = n[R == 0].astype(int); print("observed failures:", list(obs))
big = n >= 1e5
def nb0(mu, D):
    # NB with mean mu, var D*mu (D>1): P(0) = (1/D)^(mu/(D-1))
    return np.where(D > 1, D ** (-mu / (D - 1)), np.exp(-mu))
for name, mu, resid, mask0 in [("A M0", M0 / 2, R - M0, None), ("B Mg", Mg / 2, R - Mg, None),
                               ("C Mloc30", np.maximum(Ml - Rs, 1e-9) / 2, R - Ml, Rs > 0)] + \
                              ([("D MQ", MQ / 2, R - MQ, None)] if MQ is not None else []):
    D = (resid[big] / 2).var() / mu[big].mean()
    P = nb0(mu, D)
    if mask0 is not None: P = np.where(mask0, 0.0, P)
    for lo, hi in [(0, 1e4), (1e4, 1e5), (1e5, 4e5)]:
        m = (n >= lo) & (n < hi)
        print("%-9s D=%.2f  [%6d,%6d): predicted %.2f  observed %d" % (name, D, lo, hi, P[m].sum(), (R[m] == 0).sum()))
    top = np.argsort(-P)[:8]; print("   highest-risk p:", [(int(n[i]), round(float(P[i]), 3), int(R[i])) for i in top])
    print("   P at observed failures:", [round(float(P[n == f][0]), 4) for f in obs])
