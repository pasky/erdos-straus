"""z52b Pass-1 U03: Z0940 — coverage of primes p=1 mod 4 (<=1e5) by the OEIS bilinear families
A213340: 5+8t+12k+16kt ; A213686: 13+20t+24k+32kt  (t,k>=0; OEIS names fetched 2026-10-31).
Compare with the (star)-zero set S_100 (R_100(p)=0) from feat_P100000_K100.npz."""
import numpy as np
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64); RK = R.sum(1)
def covered(p, a, b, c, dd):
    t = np.arange(0, (p - a) // b + 1)
    num = p - a - b * t; den = c + dd * t
    return bool(np.any((num >= 0) & (num % den == 0)))
fam = {"A213340": (5, 8, 12, 16), "A213686": (13, 20, 24, 32)}
cov = {k: np.array([covered(int(p), *v) for p in pr]) for k, v in fam.items()}
u = cov["A213340"] | cov["A213686"]
print("covered by A213340:", int(cov["A213340"].sum()), " by A213686:", int(cov["A213686"].sum()), " by union:", int(u.sum()), "of", len(pr))
unc = pr[~u]
print("uncovered primes (<=1e5):", unc.tolist()[:40], "count", len(unc))
print("R_100 on uncovered primes:", [int(RK[i]) for i in np.nonzero(~u)[0]][:40])
print("star-zero (R_100=0) primes not covered by union:", int(((RK == 0) & ~u).sum()), " star-zero total:", int((RK == 0).sum()))
