"""z52b Pass-1 U03 final2: Z1049 (is a prime factor = -1 mod 4C necessary for success?), Z1066 (joint survival S_1,S_2,S_3),
Z1067 (divisor classes mod 4C of all divisors of N_C, C<=30: chi-square vs uniform on units), Z1928 (p+B factorisation for
(*)-failures, B<=50), Z2051 (p = x^2+n y^2 for n<=100 vs R_K), Z3062 (sum of 1/p over FRONTIER's 14 (*)-failures <=1e10)."""
import numpy as np, json, math
from math import gcd, isqrt, log
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64); hm1 = d["hm1"]; S = R == 0
out = {}
# Z1049
succ = R > 0
print("Z1049: P(succ & no prime factor = -1 mod 4C)=%.5f ; P(succ)=%.4f ; P(succ | hm1)=%.4f" % (
      (succ & ~hm1).mean(), succ.mean(), succ[hm1].mean()))
out["Z1049"] = {"succ_without_prime_m1": float((succ & ~hm1).mean()), "P_succ": float(succ.mean())}
# Z1066
J = S[:, 0] & S[:, 1] & S[:, 2]
print("Z1066: P(S1&S2&S3)=%.4f vs product %.4f; P(S1&S2)=%.4f P(S1&S3)=%.4f P(S2&S3)=%.4f" % (
      J.mean(), S[:, 0].mean()*S[:, 1].mean()*S[:, 2].mean(), (S[:,0]&S[:,1]).mean(), (S[:,0]&S[:,2]).mean(), (S[:,1]&S[:,2]).mean()))
# Z1067 divisor classes mod 4C of all divisors of N_C (p<=2000 to keep it light)
spf = list(range(4 * 30 * 2000 + 2))
for i in range(2, isqrt(len(spf))):
    if spf[i] == i:
        for j in range(i*i, len(spf), i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
chis = []
for C in [1, 2, 3, 5, 6, 10, 15, 30]:
    m = 4 * C; cnt = {}
    for p in pr[pr <= 2000]:
        f = fac(4 * C * int(p) + 1); ds = [1]
        for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
        for x in ds:
            if gcd(x, m) == 1: cnt[x % m] = cnt.get(x % m, 0) + 1
    units = [a for a in range(1, m) if gcd(a, m) == 1]; tot = sum(cnt.values())
    exp = tot / len(units); chi2 = sum((cnt.get(a, 0) - exp) ** 2 / exp for a in units)
    chis.append((C, round(chi2, 1), len(units) - 1))
print("Z1067 chi-square of divisor classes mod 4C (C, chi2, df) for C in [1,2,3,5,6,10,15,30]:", chis)
out["Z1067"] = chis
# Z1928: p+B factor check for the 14 known (*)-failures (<=1e10) that are <=1e6, B<=50 : is each p+B class-constrained mod 4B?
fails = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]
def tdiv(n):
    f = {}; q = 2
    while q * q <= n:
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
        q += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
rows = []
for p in fails[:4]:
    slow = None
    for B in range(1, 51):
        f = tdiv(p + B)
        # does p+B have a divisor = -1 mod 4B ? (the b=1-type check)
        ds = [1]
        for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
        hit = any(x % (4 * B) == 4 * B - 1 for x in ds if x > 1 and gcd(x, 4 * B) == 1)
        if not hit and slow is None: slow = B
    rows.append((p, slow))
print("Z1928 first B<=50 with no divisor of p+B ≡ -1 (mod 4B) for (*)-failures:", rows)
out["Z1928"] = rows
# Z2051: n <= 100 with p = x^2 + n y^2 ; compare with log1p R_K
RK = R.sum(1)
cnt = []
for p in pr:
    p = int(p); c = 0
    for n in range(1, 101):
        ok = False
        y = 1
        while n * y * y < p:
            r = p - n * y * y
            x = isqrt(r)
            if x * x == r and x > 0: ok = True; break
            y += 1
        c += ok
    cnt.append(c)
cnt = np.array(cnt)
print("Z2051 corr(#{n<=100: p=x^2+ny^2}, log1p R_K) = %.4f ; mean reps %.2f" % (np.corrcoef(cnt, np.log1p(RK))[0, 1], cnt.mean()))
out["Z2051"] = float(np.corrcoef(cnt, np.log1p(RK))[0, 1])
# Z3062: sum 1/p over the 14 FRONTIER (*)-failures <=1e10 (list: 409,577,5569,9601,23929,83449,102001,329617,712321 known; rest not listed in repo text here)
print("Z3062 partial sum 1/p over the 9 listed (*)-failures:", round(sum(1/p for p in fails), 6))
json.dump(out, open("data/z52b/pass1/U03/final2_results.json", "w"), default=float)
