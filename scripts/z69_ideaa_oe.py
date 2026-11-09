#!/usr/bin/env python3
"""z69 IDEAA test T1: odd/even (theta-quotient / divisor) decomposition summed over ALL levels.

A^-_t(n) = #{(u,v)>=1 : t u v - u - v = n}   (words; divisors of tn+1 that are == -1 mod t)
A^+_t(n) = #{(u,v)>=1 : t u v + u + v = n}   (divisors of tn+1 that are == +1 mod t, excluding 1 and tn+1)
For a residue set T of levels:  Wm_T(n) = sum_{t in T} A^-_t(n),  Wp_T(n) = sum_{t in T} A^+_t(n),
O_T = Wm_T - Wp_T (odd-character / theta-quotient part),  E_T = Wm_T + Wp_T (even part).
R(n) (the (*) count) = Wm_{4|t}(n).

Question (identity route with a concrete candidate): does O_T(n) have a closed form / small dictionary
expression (it is a sum over t of weight-1 Eisenstein coefficients at the moving argument tn+1)?
Kill test (pre-registered, memo §2): exact rational least squares of O_T on the dictionary below, on
n in [N/2, N]; KILL if the residual is not identically 0 and R^2 < 0.9 for every T.
"""
import sys, json
import numpy as np
from fractions import Fraction

N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
UMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 1   # 1 = all words; 2 = interior words only (u,v>=2)

def tau_table(M):
    t = np.zeros(M + 1, dtype=np.int64)
    for d in range(1, M + 1):
        t[d::d] += 1
    return t

def tau_class(M, q, a):
    """#divisors of n that are == a mod q, for n<=M"""
    t = np.zeros(M + 1, dtype=np.int64)
    for d in range(1, M + 1):
        if d % q == a % q:
            t[d::d] += 1
    return t

levels = {"all": lambda t: True, "t=0(4)": lambda t: t % 4 == 0, "t=2(4)": lambda t: t % 4 == 2,
          "t=1(4)": lambda t: t % 4 == 1, "t=3(4)": lambda t: t % 4 == 3, "t>=3": lambda t: t >= 3}
Wm = {k: np.zeros(N + 1, dtype=np.int64) for k in levels}
Wp = {k: np.zeros(N + 1, dtype=np.int64) for k in levels}
# minus: n = t u v - u - v  (u,v>=1, n>=1)
for u in range(UMIN, N + 2):
    for v in range(UMIN, N + 2):
        uv = u * v
        if uv - u - v > N:
            break
        t = 1
        while True:
            n = t * uv - u - v
            if n > N:
                break
            if n >= 1:
                for k, f in levels.items():
                    if f(t):
                        Wm[k][n] += 1
            t += 1
    if u * UMIN - u - UMIN > N:
        break
for u in range(UMIN, N + 1):
    for v in range(UMIN, N + 1):
        uv = u * v
        if uv + u + v > N:
            break
        t = 1
        while True:
            n = t * uv + u + v
            if n > N:
                break
            for k, f in levels.items():
                if f(t):
                    Wp[k][n] += 1
            t += 1

M = 4 * N + 8
tau = tau_table(M)
t1_4 = tau_class(M, 4, 1); t3_4 = tau_class(M, 4, 3)
ns = np.arange(N // 2, N + 1)
ns = ns[ns % 4 == 1]
dic = {
    "1": np.ones(len(ns)),
    "tau(n)": tau[ns], "tau(n+1)": tau[ns + 1], "tau(n-1)": tau[ns - 1], "tau(n+2)": tau[ns + 2],
    "tau(n-2)": tau[ns - 2], "tau(2n+1)": tau[2 * ns + 1], "tau(2n-1)": tau[2 * ns - 1],
    "tau(4n+1)": tau[4 * ns + 1], "tau(4n-1)": tau[4 * ns - 1], "tau(n+4)": tau[ns + 4], "tau(n-4)": tau[ns - 4],
    "d1-d3(n)": (t1_4 - t3_4)[ns], "d1-d3(n+2)": (t1_4 - t3_4)[ns + 2], "d1-d3(4n+1)": (t1_4 - t3_4)[4 * ns + 1],
    "d1-d3(n+4)": (t1_4 - t3_4)[ns + 4], "d3(n+1 odd part)": t3_4[ns + 1], "d3(4n+1)": t3_4[4 * ns + 1],
    "log n": np.log(ns), "log^2 n": np.log(ns) ** 2,
}
A = np.column_stack([dic[k].astype(float) for k in dic])
out = {"N": N, "n_used": int(len(ns)), "dictionary": list(dic), "fits": {}}
print(f"N={N}, n = 1 (4) in [N/2,N]: {len(ns)} points")
for k in levels:
    O = (Wm[k] - Wp[k])[ns].astype(float); E = (Wm[k] + Wp[k])[ns].astype(float)
    for name, y in (("O", O), ("E", E), ("Wm", Wm[k][ns].astype(float))):
        coef, res, rk, sv = np.linalg.lstsq(A, y, rcond=None)
        pred = A @ coef
        ss = float(((y - pred) ** 2).sum()); st = float(((y - y.mean()) ** 2).sum())
        r2 = 1 - ss / st if st > 0 else 1.0
        out["fits"][f"{name}[{k}]"] = {"mean": float(y.mean()), "var": float(y.var()), "R2": r2,
                                       "max_abs_resid": float(np.abs(y - pred).max())}
        if name == "O":
            top = sorted(zip(np.abs(coef * A.std(axis=0)), list(dic), coef), reverse=True)[:3]
            out["fits"][f"{name}[{k}]"]["top3"] = [(nm, float(c)) for _, nm, c in top]
            print("      top terms:", [(nm, round(float(c), 3)) for _, nm, c in top])
        print(f"{name}[{k:7s}] mean={y.mean():9.3f} var={y.var():10.3f}  R2={r2:6.3f}  max|resid|={np.abs(y-pred).max():8.2f}")
# squares: T1 check   O_{4|t}(m^2) = -E_{4|t}(m^2)  <=> Wm = 0
sq = [m * m for m in range(3, int(N ** 0.5) + 1, 2)]
print("T1 check: max Wm[t=0(4)] over odd squares =", max(int(Wm["t=0(4)"][s]) for s in sq))
# print a small table for eyeballing
print("\n n   Wm_all Wp_all O_all | Wm_4 Wp_4 O_4 | O_t=3(4) O_t=1(4) O_t=2(4)")
for n in list(range(1, 60, 4)) + [m * m for m in (9, 11, 13)]:
    print(f"{n:4d} {Wm['all'][n]:6d} {Wp['all'][n]:6d} {Wm['all'][n]-Wp['all'][n]:5d} | {Wm['t=0(4)'][n]:4d} {Wp['t=0(4)'][n]:4d} {Wm['t=0(4)'][n]-Wp['t=0(4)'][n]:4d} |"
          f" {Wm['t=3(4)'][n]-Wp['t=3(4)'][n]:5d} {Wm['t=1(4)'][n]-Wp['t=1(4)'][n]:5d} {Wm['t=2(4)'][n]-Wp['t=2(4)'][n]:5d}")
# correlation between O and E on primes n=1(8)
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
pm = np.array([n for n in ns if isprime(int(n))])
for k in ("t=0(4)", "all"):
    O = (Wm[k] - Wp[k])[pm].astype(float); E = (Wm[k] + Wp[k])[pm].astype(float)
    c = float(np.corrcoef(O, E)[0, 1])
    out["fits"][f"corr(O,E)[{k}] primes"] = c
    print(f"primes n=1(4): corr(O,E)[{k}] = {c:.3f}; mean O={O.mean():.3f}, mean E={E.mean():.3f}, P(O<=-E)={(O<=-E).mean():.4f}")
json.dump(out, open(f"data/z69/ideaa/oe_fit_umin{UMIN}.json", "w"), indent=1)
