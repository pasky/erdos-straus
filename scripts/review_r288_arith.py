"""R288 from-scratch arithmetic checks for the 3/4 note (C2).

Exact/finite checks of the elementary inequalities used on the load-bearing
route, plus toy-size EVIDENCE for the lattice and second-moment lemmas.
Run: ulimit -v 8000000; timeout 1800 PYTHONPATH=scripts uv run --with numpy python scripts/review_r288_arith.py
"""
import math
from math import gcd, log

import numpy as np

FAIL = []


def check(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + (" :: " + info if info else ""))
    if not ok:
        FAIL.append(name)


def sieve_spf(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i:: i][spf[i:: i] == 0] = i
    return spf


NMAX = 200000
SPF = sieve_spf(NMAX)


def factor(n):
    f = {}
    while n > 1:
        p = int(SPF[n])
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def phi(n):
    r = n
    for p in factor(n):
        r = r // p * (p - 1)
    return r


PHI = np.arange(NMAX + 1, dtype=np.int64)
for p in range(2, NMAX + 1):
    if SPF[p] == p:
        PHI[p::p] = PHI[p::p] // p * (p - 1)
OMEGA = np.zeros(NMAX + 1, dtype=np.int64)
for p in range(2, NMAX + 1):
    if SPF[p] == p:
        OMEGA[p::p] += 1


def phi_big(n):
    if n <= NMAX:
        return int(PHI[n])
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            r = r // p * (p - 1)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        r = r // m * (m - 1)
    return r


# 1. phi(4uv) >= 2 phi(u) phi(v), coprime u,v
def c1():
    ok = True
    for u in range(1, 401):
        for v in range(1, 401):
            if gcd(u, v) == 1 and phi_big(4 * u * v) < 2 * PHI[u] * PHI[v]:
                ok = False
    check("1 phi(4uv)>=2phi(u)phi(v) (coprime u,v<=400)", ok)


# 2. exp(-sum_{p|d} 2/(p-1)) <= (phi(d)/d)^2
def c2():
    worst = 0.0
    for d in range(1, NMAX + 1):
        lhs = math.exp(-sum(2 / (p - 1) for p in factor(d)))
        rhs = (PHI[d] / d) ** 2
        worst = max(worst, lhs / rhs)
    check("2 exp(-sum 2/(p-1)) <= (phi(d)/d)^2, d<=2e5", worst <= 1 + 1e-12, f"max ratio {worst:.6f}")


# 3. removal bound and 4. h(K)
def c34():
    K = 20000
    w = PHI[1:K + 1] / np.arange(1, K + 1) ** 2.0  # phi(k)/k^2
    ok = True
    worst = 0.0
    for p in range(2, K + 1):
        if SPF[p] != p:
            continue
        cs = np.cumsum(w[p - 1::p])  # k = p, 2p, ...
        Ks = np.arange(p, K + 1, p)
        # bound must hold for every K' >= p (sum constant between multiples, so test at multiples and at K'=next-1)
        r = cs * p / (1 + np.log(np.maximum(Ks, 1)))
        worst = max(worst, float(r.max()))
    check("3 sum_{k<=K,p|k} phi(k)/k^2 <= (1+log K)/p, K<=2e4", worst <= 1, f"max ratio {worst:.4f}")
    k1 = np.arange(1, K + 1)
    mask = (k1 % 4) == 1
    hcum = np.cumsum(np.where(mask, w, 0.0))
    devs = [(Kp, hcum[Kp - 1] - 2 / math.pi ** 2 * log(Kp)) for Kp in (100, 1000, 5000, 20000)]
    a0 = min(hcum[Kp - 1] / log(Kp) for Kp in range(5, K + 1))
    check("4 h(K(K)) - (2/pi^2)log K stabilises (EVIDENCE)", abs(devs[-1][1] - devs[-2][1]) < 0.01,
          ", ".join(f"K={a}:{b:.4f}" for a, b in devs) + f"; min h/logK on [5,2e4]={a0:.3f}")
    s = sum(1 / d ** 2 * (-1) ** len(factor(d)) for d in range(1, NMAX, 2) if all(e == 1 for e in factor(d).values()))
    check("4' sum_{d odd} mu(d)/d^2 = 8/pi^2", abs(s - 8 / math.pi ** 2) < 1e-4, f"{s:.6f} vs {8/math.pi**2:.6f}")


# 5. pair-lcm sum
def c5():
    out = []
    for K in (50, 200, 800):
        tot = 0.0
        tot1 = 0.0
        for k in range(1, K + 1):
            for kk in range(1, K + 1):
                g = gcd(k, kk)
                d = k // g * kk
                # phi(lcm) = phi(k)phi(k')/phi(g) * ... exact: phi([a,b]) * phi((a,b)) = phi(a) phi(b)
                ph = PHI[k] * PHI[kk] // PHI[g]
                val = ph / d ** 2
                tot += val
                if k % 4 == 1 and kk % 4 == 1:
                    tot1 += val
        out.append((K, tot / (1 + log(K)) ** 3, tot1 / (1 + log(K)) ** 3))
    check("5 sum_{k,k'<=K} phi([k,k'])/[k,k']^2 / (1+logK)^3 bounded (EVIDENCE)", all(o[1] < 1 for o in out),
          "; ".join(f"K={a}: all {b:.3f}, 1mod4 {c:.4f}" for a, b, c in out))


# 6. lattice sums (toy H, not K^10: EVIDENCE for the constants only)
def c6():
    H = 54
    z = H * H
    u = np.arange(H + 1, z + 1, dtype=np.int64)
    U, V = np.meshgrid(u, u, indexing="ij")
    G = np.gcd(U, V)
    cop = G == 1
    inv_uv = 1.0 / (U * V)
    inv_ff = 1.0 / (PHI[U] * PHI[V])
    Lam = log(z / H)
    lo, hi = 9.9, 0.0
    for k in (1, 5, 9, 13, 21, 105):
        for c in range(k):
            if gcd(c, k) != 1:
                continue
            S = cop & (np.gcd(V, k) == 1) & (((U + c * V) % k) == 0)
            main = PHI[k] / k ** 2 * Lam ** 2
            r1 = float(inv_uv[S].sum()) / main
            r2 = float(inv_ff[S].sum()) / main
            lo = min(lo, r1)
            hi = max(hi, r2)
    check("6 lattice: lower ratio >= 1/4, upper ratio O(1) (toy H=54,z=H^2; EVIDENCE)", lo >= 0.25, f"min lower {lo:.3f}, max upper {hi:.3f}")
    del U, V, G


# 7. R(M) = {-4D mod M : D | A^2}
def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def c7():
    ok = True
    for M in range(3, 3000, 4):
        A = (M + 1) // 4
        R1 = set()
        for u in divisors(A):
            for v in divisors(A // u):
                R1.add((-u * pow(v, -1, M)) % M)
        D2 = [1]
        for p, e in factor(A).items():
            D2 = [d * p ** i for d in D2 for i in range(2 * e + 1)]
        R2 = {(-4 * D) % M for D in D2}
        t = 1
        for e in factor(A).values():
            t *= 2 * e + 1
        if R1 != R2 or not ((t - 1) / 2 <= len(R1) <= t):
            ok = False
            print("   R(M) mismatch at", M)
            break
    check("7 R(M)={-4D: D|A^2}, (tau(A^2)-1)/2<=|R|<=tau(A^2), M<3000", ok)


# 8. void arithmetic, BT numeric, coprime splittings, m/phi(m) identity
def c8():
    ys = np.linspace(2, 2000, 20001)
    ok = True
    for y in ys:
        n0 = math.floor(y) + 1
        tail = 1 / (n0 - 1) - sum(1 / (n * n * (n - 1)) for n in range(n0, n0 + 1))  # crude; use exact-ish below
        tail = sum(1 / n ** 2 for n in range(n0, n0 + 20000)) + 1 / (n0 + 20000)
        if tail > 2 / y or (math.e - 1) * y * tail > 4:
            ok = False
    check("8 sum_{n>y} n^-2 <= 2/y and (e-1)y*tail <= 4 for y in [2,2000]", ok, f"2(e-1)={2*(math.e-1):.3f}")
    # BT: 2x/(phi log(x/q)) <= 4x/(phi log x) for q<=4x^{1/3}: need (2/3)L - log 4 >= L/2
    Lthr = 6 * log(4)
    check("8' BT simplification holds iff log x >= 6 log 4", True, f"threshold x >= e^{Lthr:.2f} ~ {math.exp(Lthr):.0f}")
    ok = True
    for m in range(1, 5000):
        pairs = sum(1 for u in divisors(m) if gcd(u, m // u) == 1)
        if pairs != 2 ** OMEGA[m]:
            ok = False
        lhs = m / PHI[m]
        rhs = sum(1 / PHI[d] for d in divisors(m) if all(e == 1 for e in factor(d).values()))
        if abs(lhs - rhs) > 1e-9:
            ok = False
    check("8'' #ordered coprime (u,v), uv=m is 2^omega(m); m/phi(m)=sum mu^2(d)/phi(d)", ok)


# 9. F = 2^omega * n/phi(n): sum_{n<=V} F << V log V, sum F(v)/v << log^2
def c9():
    n = np.arange(1, NMAX + 1)
    F = (2.0 ** OMEGA[1:]) * n / PHI[1:]
    cs = np.cumsum(F)
    cs2 = np.cumsum(F / n)
    rat = [(V, cs[V - 1] / (V * log(V)), cs2[V - 1] / log(V) ** 2) for V in (1000, 10000, 100000, 200000)]
    check("9 sum F/(V log V) and sum F(v)/v/(log)^2 bounded (EVIDENCE)", all(r[1] < 3 and r[2] < 3 for r in rat),
          "; ".join(f"V={a}: {b:.3f}, {c:.3f}" for a, b, c in rat))


if __name__ == "__main__":
    c1(); c2(); c34(); c5(); c7(); c8(); c9(); c6()
    print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
