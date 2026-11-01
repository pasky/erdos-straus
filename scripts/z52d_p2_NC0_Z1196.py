#!/usr/bin/env python3
"""Z1196: running-time bounds for residue selection vs factor count (analysis + check).

Setting: N = M^2 = prod q_i^{2 a_i}, omega = omega(M), Omega = Omega(M), target residue mod m.
Two algorithms for 'is there a divisor d | N with d = t (mod m)?':
  (E) enumerate divisors: time Theta(tau(N)), tau(N) = prod (2a_i+1).
  (D) residue DP: R <- union_j R*q^j mod m over prime powers; time O(m * sum_i (2a_i+1)).
Analytic facts used (checked numerically below):
  * tau(N) = prod(2a_i+1) <= (2*Omega/omega + 1)^omega (AM-GM on the exponents, sum a_i = Omega).
    For fixed omega this is (log N)^omega up to constants: XP in omega, not FPT in omega alone
    (the exponents, not only the count of primes, drive the cost).
  * (D) is pseudo-polynomial in the modulus m and polynomial in log N: independent of omega.
    For ES windows m = r = 4x - p with x = ceil(p/4)+k, so m <= 4k+3 is small and (D) costs
    O(k * log N) per window.
Test: for every prime p = 1 mod 4 up to PMAX, windows x in [ceil(p/4), ceil(p/4)+K): compare
tau with the AM-GM bound, the DP cost with the enumeration cost, and check DP == enumeration.
"""
import sys, time, json, math

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def residue_dp(pps, m, t):
    R = {1 % m}
    for q, a in pps:
        pw = [pow(q, j, m) for j in range(a + 1)]
        R = {(r * c) % m for r in R for c in pw}
    return (t % m) in R

def enum_exists(pps, m, t):
    ds = [1]
    for q, a in pps:
        ds = [d * q ** j for d in ds for j in range(a + 1)]
    return any((d - t) % m == 0 for d in ds)

def main(pmax=30000, K=5):
    ps = [p for p in range(5, pmax) if p % 4 == 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))]
    worst_ratio = 0.0; mism = 0; n = 0; tot_tau = 0; tot_dp = 0
    rows = []
    for p in ps:
        x0 = -(-p // 4)
        for x in range(x0, x0 + K):
            r = 4 * x - p; M = p * x
            f = factor(M)
            pps = sorted((q, 2 * a) for q, a in f.items())
            omega = len(f); Omega = sum(f.values())
            tau = 1
            for q, a in pps:
                tau *= (a + 1)
            bound = (2 * Omega / omega + 1) ** omega
            worst_ratio = max(worst_ratio, tau / bound)
            if tau > 1:
                pass
            t = (-M) % r
            d_ans = residue_dp(pps, r, t)
            e_ans = enum_exists(pps, r, t)
            if d_ans != e_ans:
                mism += 1
            n += 1
            tot_tau += tau
            tot_dp += sum(a + 1 for q, a in pps) * r
            rows.append((p, x, omega, Omega, tau, round(bound, 1), r))
    return n, mism, worst_ratio, tot_tau, tot_dp, rows

if __name__ == "__main__":
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    t0 = time.time()
    n, mism, worst, ttau, tdp, rows = main(pmax, 5)
    print(f"windows={n} DP-vs-enumeration mismatches={mism}")
    print(f"max tau/AM-GM-bound ratio = {worst:.3f} (<=1 means the bound holds)")
    print(f"sum tau(M^2) = {ttau}; sum residue-DP ops (sum(2a+1)*r) = {tdp}")
    rows.sort(key=lambda r: -r[4])
    print("largest tau rows (p,x,omega,Omega,tau,bound,r):", rows[:3])
    print("max omega:", max(r[2] for r in rows), " max Omega:", max(r[3] for r in rows))
    print("seconds", round(time.time() - t0, 1))
    json.dump({"windows": n, "mismatches": mism, "worst_ratio": worst, "sum_tau": ttau, "sum_dp_ops": tdp,
               "top": rows[:20]}, open(f"data/z52b/pass2/NC0/sub/Z1196_fp_{pmax}.json", "w"), indent=1)
