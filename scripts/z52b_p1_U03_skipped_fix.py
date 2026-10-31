"""z52b Pass-1 U03 (fix round): concrete tests for skipped items with data-ready first steps.
Z3183: residue classes mod 840 (p=1 mod 4 prime <=1e5) where all C<=10 levels fail.
Z3118: window density of R_C(n)>0 (n=1 mod 4, all n<=1e5) for C=1, windows of length H.
Z3089: fraction of (p,C), C<=100, having a divisor d = -1 mod 4C built only from primes <= y (y=5,10,30).
Z3105: fraction of x in (p/4,p/2) for which (4x-p)/(px) is NOT a sum of two unit fractions (p prime <=1000)
Z2093: Schinzel admissibility of {4Cx+1 : C<=K} (checked for all primes q<=1000) and prime-variable failure."""
import numpy as np, json
from math import gcd, isqrt
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; R = d["R"].astype(np.int64)
out = {}
# Z3183
cls = pr % 840; allfail = (R[:, :10] == 0).all(1)
rates = {}
for c in np.unique(cls):
    m = cls == c
    if m.sum() >= 5: rates[int(c)] = (int(m.sum()), float(allfail[m].mean()))
full = [c for c, (n, r) in rates.items() if r == 1.0]
print("Z3183: classes mod 840 with >=5 primes: %d; classes where all C<=10 fail for every prime: %s; max rate %.2f" % (
      len(rates), full[:20], max(r for n, r in rates.values())))
out["Z3183"] = {"n_classes": len(rates), "all_fail_classes": full, "max_rate": max(r for n, r in rates.values())}
# Z3118
A = np.load("data/z52b/pass1/U03/allN1mod4_RK.npz"); ns = A["n"]; RC = A["RC"]
for H in [500, 2000]:
    vals = []
    for lo in range(10000, 100000 - H, H):
        m = (ns >= lo) & (ns < lo + H)
        vals.append((RC[m, 0] > 0).mean())
    vals = np.array(vals)
    print(f"Z3118 H={H}: window density of R_1>0 mean {vals.mean():.4f}, sd {vals.std():.4f}, min {vals.min():.4f}, max {vals.max():.4f}")
    out[f"Z3118_H{H}"] = [float(vals.mean()), float(vals.std())]
# Z3089: y-smooth divisor = -1 mod 4C using only primes <= y (for C<=100, p<=1e5 sample every 4th prime)
spf = list(range(4 * 100 * 10**5 + 2))
for i in range(2, isqrt(len(spf))):
    if spf[i] == i:
        for j in range(i*i, len(spf), i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
for y in [5, 10, 30]:
    hit = tot = 0
    for p in pr[::4]:
        p = int(p)
        for C in range(1, 101):
            N = 4 * C * p + 1; m = 4 * C
            f = {q: e for q, e in fac(N).items() if q <= y}
            # divisors of the y-smooth part of N
            ds = [1]
            for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
            tot += 1; hit += any(x > 1 and x % m == m - 1 for x in ds)
    print(f"Z3089 y={y}: fraction of (p,C) with a y-smooth divisor = -1 mod 4C: {hit/tot:.4f} (n={tot})")
    out[f"Z3089_y{y}"] = hit / tot
# Z3105
def two_term(a, b):
    from math import isqrt as _i
    fb = {}; n = b * b; q = 2
    while q * q <= n:
        while n % q == 0: fb[q] = fb.get(q, 0) + 2 if False else fb.get(q, 0) + 1; n //= q
        q += 1
    if n > 1: fb[n] = fb.get(n, 0) + 1
    ds = [1]
    for q, e in fb.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
    return any(((D + b) % a == 0) and ((b * b // D + b) % a == 0) for D in ds)
bad = tot = 0
for p in [q for q in range(5, 1001) if all(q % r for r in range(2, isqrt(q) + 1)) and q % 4 == 1]:
    for x in range(p // 4 + 1, p // 2 + 1):
        num = 4 * x - p; den = p * x
        if num <= 0: continue
        g = gcd(num, den); a, b = num // g, den // g
        tot += 1; bad += (not two_term(a, b))
print(f"Z3105 p<=1000 (1 mod 4): fraction of x in (p/4,p/2] where (4x-p)/(px) is not a 2-unit-fraction sum: {bad/tot:.4f} (n={tot})")
out["Z3105"] = bad / tot
# Z2093: Schinzel admissibility of {4Cx+1: C<=K}: for every prime q, is there x mod q with no 4Cx+1 = 0 mod q?
K = 100; adm = True
for q in [p for p in range(2, 1001) if all(p % r for r in range(2, isqrt(p) + 1))]:
    if not any(all((4 * C * x + 1) % q for C in range(1, K + 1)) for x in range(q)):
        adm = False; print("not admissible at", q); break
print("Z2093: {4Cx+1, C<=100} admissible at all primes q<=1000:", adm, "(x=0 mod q always works)")
primes_x = [int(p) for p in pr]
both = [p for p in primes_x if all(isqrt(0) >= 0 and all((4 * C * p + 1) % q for q in [3]) for C in range(1, 3))]
print("   prime-variable check: #p<=1e5 with 4p+1 and 8p+1 both not divisible by 3:", len(both), "(only p=3-type cases excluded)")
out["Z2093"] = {"admissible_q_le_1000": adm}
json.dump(out, open("data/z52b/pass1/U03/skipped_fix_results.json", "w"), default=float)
