"""What drives the common part of log f_I(p) and log f_II(p) for p = 1 (mod 24)?  Nested regressions:
 M0 intercept; M1 quadratic profile (l/p), 5<=l<=100; M2 = M1 + full residue-class dummies of p mod
 m for m in {5,7,9,11,13,16,17,19,23} (congruence data); M3 = M2 + log L(1,chi_p) truncated (Euler product
 over l < 2e4) ; M4 = M3 + "shift richness" sum_{e<=40, e=-p mod 4} log tau((p+e)/4) and
 sum_{e<=40, e=-1/p...} log tau((pe+1)/4).  Reports R^2 and residual correlation for each.
Usage: bs_corr_driver.py countfile [...]"""
import sys, math
import numpy as np
from sympy import isprime, legendre_symbol, primerange, divisor_count
P = []
for fn in (sys.argv[1:] if __name__ == "__main__" else []):
    for line in open(fn):
        n, a, b = map(int, line.split())
        if n % 24 == 1 and isprime(n): P.append((n, a, b))
yI = np.array([math.log(a / math.log(n) ** 3) for n, a, b in P]); yII = np.array([math.log(b / math.log(n) ** 3) for n, a, b in P])
LS = list(primerange(3, 20000))
def logL(p):
    s = 0.0
    for l in LS:
        s -= math.log(1 - legendre_symbol(l, p) / l) if l != p else 0.0
    return s - math.log(1 - (1 if p % 8 in (1, 7) else -1) / 2)
def feats(p, level):
    f = [1.0]
    if level >= 1: f += [float(legendre_symbol(l, p)) for l in primerange(5, 101)]
    if level >= 2:
        for m in (5, 7, 9, 11, 13, 16, 17, 19, 23):
            f += [1.0 if p % m == r else 0.0 for r in range(1, m) if math.gcd(r, m) == 1][1:]
    if level >= 3: f.append(logL(p))
    if level >= 4:
        f.append(sum(math.log(divisor_count((p + e) // 4)) for e in range(3, 41, 4)))
        f.append(sum(math.log(divisor_count((p * e + 1) // 4)) for e in range(3, 41, 4)))
    return f
if __name__ == "__main__":
  print("primes p=1 (24):", len(P))
  for lev, nm in enumerate(['M0 intercept', 'M1 +profile l<=100', 'M2 +residue classes', 'M3 +log L(1,chi_p)', 'M4 +shift richness']):
    Z = np.array([feats(n, lev) for n, a, b in P], dtype=float)
    out = []
    res = []
    for y in (yI, yII):
        beta, *_ = np.linalg.lstsq(Z, y, rcond=None); r = y - Z @ beta; res.append(r); out.append(1 - r.var() / y.var())
    print('%-22s cols=%3d  R2_I=%.3f R2_II=%.3f  resid corr=%.3f' % (nm, Z.shape[1], out[0], out[1], np.corrcoef(res[0], res[1])[0, 1]))
