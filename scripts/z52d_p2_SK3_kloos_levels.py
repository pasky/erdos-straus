# z52d pass2 SK3 fix, item Z2929: level-sum fluctuation of D_t^-(tp+1) = #{d | tp+1 : d = -1 mod t} (FRONTIER 2.3 convention).
# Naive main term: tau(N)/phi(t) (each unit class of t gets an equal share of the divisors of N).
# E_T(p) = sum_{t<=T} [D_t^-(tp+1) - tau(tp+1)/phi(t)].  If the level errors cancelled like independent
# mean-zero terms, std_p E_T ~ T^{1/2}; systematic (non-cancelling) errors give ~T.  We fit the exponent.
import numpy as np, math
from math import gcd
TMAX = 400
PLO, PHI = 100000, 102500
NMAX = TMAX*PHI + 1
spf = np.zeros(NMAX+1, dtype=np.int32)
for i in range(2, int(NMAX**0.5)+1):
    if spf[i] == 0:
        s = spf[i*i::i]; m = (s == 0); s[m] = i; spf[i*i::i] = s
def factor(n):
    f = {}
    while n > 1:
        q = int(spf[n]) if spf[n] else n
        f[q] = f.get(q, 0) + 1; n //= q
    return f
def divisors(n):
    ds = [1]
    for q, e in factor(n).items():
        ds = [d * q**k for d in ds for k in range(e+1)]
    return ds
def phi(n):
    r = n
    for q in factor(n): r = r // q * (q-1)
    return r
sv = np.ones(PHI+1, dtype=bool); sv[:2] = False
for i in range(2, int(PHI**0.5)+1):
    if sv[i]: sv[i*i::i] = False
primes = [int(p) for p in np.nonzero(sv)[0] if int(p) >= PLO and int(p) % 4 == 1]
print("primes:", len(primes))
# per prime: cumulative error curve over t
curves = []
for p in primes:
    cum = 0.0; row = []
    for t in range(1, TMAX+1):
        N = t*p + 1
        ds = divisors(N)
        dm = sum(1 for d in ds if d % t == (t-1) % t and (d % t) == (t - 1))  # d == -1 mod t (t>=2); t=1: all d
        if t == 1: dm = len(ds)
        cum += dm - len(ds)/phi(t)
        row.append(cum)
    curves.append(row)
C = np.array(curves)
out = []
for T in (25, 50, 100, 200, 400):
    col = C[:, T-1]
    out.append((T, col.mean(), col.std()))
    print(f"T={T:4d}: mean E_T = {col.mean():9.3f}  std E_T = {col.std():8.3f}")
Ts = np.array([o[0] for o in out], float); sd = np.array([o[2] for o in out])
alpha = np.polyfit(np.log(Ts), np.log(sd), 1)[0]
print(f"fitted exponent of std_p E_T vs T: {alpha:.3f}  (0.5 = independent level errors; 1.0 = no cancellation)")
