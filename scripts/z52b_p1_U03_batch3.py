"""z52b Pass-1 U03 batch3: all n = 1 mod 4 (n<=NMAX) divisor-form counts R_K(n), K=100 (truncated) -> sieve (Z1541),
short-interval comparison (Z2945), interval gaps (Z2002), N_C roughness (Z2587), level-count tail (Z2946), Z1542 omega(a)."""
import numpy as np, json, math
from math import isqrt, gcd, log
NMAX = 100000; K = 100
M = 4 * K * NMAX + 2
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i*i, M + 1, i):
            if spf[j] == j: spf[j] = i
def factor(n):
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
def divs(f):
    ds = [1]
    for q, e in f.items(): ds = [x * q**k for x in ds for k in range(e + 1)]
    return ds
ns = np.arange(1, NMAX + 1, 4)
RC = np.zeros((len(ns), K), np.int32)
for a, n in enumerate(ns):
    n = int(n)
    if n == 1: continue
    for C in range(1, K + 1):
        if 4 * C > 4 * n: break
        m = 4 * C
        RC[a, C-1] = sum(1 for x in divs(factor(4 * C * n + 1)) if x % m == m - 1)
RK = RC.sum(1)
np.savez_compressed("data/z52b/pass1/U03/allN1mod4_RK.npz", n=ns, RC=RC)
res = {}
# Z1541: sieve by certificates with A=10 (C<=10): survivors among n in [1,NMAX], n=1 mod 4
A = 10; surv = RC[:, :A].sum(1) == 0
rho = [float((RC[:, c] == 0).mean()) for c in range(A)]
pred = float(np.prod(rho)) * len(ns)
print(f"Z1541 survivors (C<=10 all fail) among n=1 mod 4 <= {NMAX}: {int(surv.sum())}; independence prediction {pred:.0f}")
res["Z1541"] = {"survivors": int(surv.sum()), "pred_indep": pred}
# Z2945: |R(p) - mean_{|n-p|<H, n=1 mod 4} R(n)| / mean, H = p^theta, primes sampled
pr = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")["primes"]
idx = {int(n): a for a, n in enumerate(ns)}
rows = []
for th in [0.1, 0.2, 0.3, 0.4, 0.5]:
    rel = []
    for p in pr[pr > 200][::20]:
        p = int(p); H = max(4, int(p ** th)); lo, hi = p - H, p + H
        vals = [RK[idx[n]] for n in range(lo + ((1 - lo) % 4), hi + 1, 4) if n in idx and n != p]
        if not vals: continue
        mu = np.mean(vals)
        if mu > 0: rel.append(abs(RK[idx[p]] - mu) / mu)
    rows.append((th, round(float(np.median(rel)), 3)))
print("Z2945 median |R(p)-<R>_H|/<R>_H by theta:", rows)
res["Z2945"] = rows
# Z2002: longest run of consecutive n=1 mod 4 (all n) with RK_{<=10}(n)=0 ; compare log^A
R10 = RC[:, :10].sum(1)
best = cur = 0; runs = []
for a in range(len(ns)):
    if R10[a] == 0: cur += 1
    else:
        runs.append(cur); cur = 0
runs = np.array(runs)
print("Z2002 longest run (n=1 mod 4) with no C<=10 certificate:", int(runs.max()), " at n~", int(ns[np.argmax(np.concatenate([[0]])) ]) if False else "", " median run", float(np.median(runs)))
print("   log^2(1e5)=", round(log(1e5) ** 2, 1), " log^3=", round(log(1e5) ** 3, 1))
res["Z2002"] = {"max_run_C10": int(runs.max()), "median_run": float(np.median(runs))}
# Z2587: N_C = 4Cp+1, C<=10, y-rough (no prime factor <= y) for all C<=10, primes p in data
for y in [7, 13]:
    small = [q for q in range(2, y + 1) if all(q % r for r in range(2, isqrt(q) + 1))]
    rough = []
    for p in pr:
        p = int(p)
        rough.append(all(all((4 * C * p + 1) % q for q in small) for C in range(1, 11)))
    obs = float(np.mean(rough))
    ind = float(np.prod([np.prod([1 - 1/q for q in small]) for _ in range(1)])) ** 10
    print(f"Z2587 y={y}: frac primes with N_C 'y-rough' for all C<=10: {obs:.4f}; independence {ind:.4f}")
    res[f"Z2587_y{y}"] = {"obs": obs, "indep": ind}
# Z2946: level-count tail: #{C<=100: R_C>0} vs Poisson with same mean (primes p<=1e5)
cnt = (np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")["R"] > 0).sum(1)
mu = cnt.mean(); from math import exp, factorial
tail_obs = float((cnt >= 2 * mu).mean()); tail_poi = 1 - sum(exp(-mu) * mu**k / factorial(k) for k in range(int(2 * mu)))
print(f"Z2946 mean #levels succeeding {mu:.2f}; P(>=2mu) obs {tail_obs:.4f} vs Poisson {tail_poi:.4f}")
res["Z2946"] = {"mean": float(mu), "tail_obs": tail_obs, "tail_poisson": tail_poi}
# Z1542: omega(a) = #{distinct -(4c^2 d)^{-1} mod a : c,d>=1, 4cd | a+1}, a<=1e4 odd
oms = []
for a in range(3, 10001, 2):
    cls = set(); t = a + 1
    if t % 4: oms.append(0); continue
    for c in range(1, t // 4 + 1):
        if t % (4 * c): continue
        for dd in range(1, t // (4 * c) + 1):
            if (t // (4 * c)) % dd == 0 and gcd(4 * c * c * dd, a) == 1:
                cls.add(pow(-4 * c * c * dd % a, -1, a) if a > 1 else 0)
    oms.append(len(cls))
oms = np.array(oms); aa = np.arange(3, 10001, 2)
print("Z1542 mean omega(a) over odd a<=1e4 (a+1=0 mod 4):", round(float(oms[oms > 0].mean()), 3), " vs log a:", round(float(np.mean(np.log(aa[oms > 0]))), 3))
res["Z1542"] = {"mean_omega": float(oms[oms > 0].mean()), "mean_log_a": float(np.mean(np.log(aa[oms > 0])))}
json.dump(res, open("data/z52b/pass1/U03/batch3_results.json", "w"), default=float)
