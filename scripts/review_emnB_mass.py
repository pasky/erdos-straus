"""R94 review B, from scratch (EVIDENCE, toy scale): DEDUPLICATED fibre mass
mu_c = sum_{l in (x,2x] prime} #{distinct classes -u v^{-1} mod l over active atoms}/l
for the m-family (k<=K, (k,m)=1, (k,c)=1, k | u+cv, m uv | k l + 1, (u,v)=(uv,k)=1,
Hfl < u,v <= z), and the BV main-term prediction sum 1/phi(m u v) * (li-weight).
Tests the claimed scaling mu ~ t^3/m (vs t^3/phi(m)) on reduced fibres.
Usage: uv run --with numpy python scripts/review_emnB_mass.py x K zexp Hfl
"""
import sys, random
from math import gcd, log
import numpy as np

def spf_np(n):
    s = np.zeros(n + 1, dtype=np.int32)
    for p in range(2, int(n ** 0.5) + 1):
        if s[p] == 0:
            blk = s[p * p::p]
            blk[blk == 0] = p
            s[p * p::p] = blk
    idx = np.nonzero(s == 0)[0]
    s[idx] = idx.astype(np.int32)
    return s

def factor(n, spf):
    f = []
    while n > 1:
        p = int(spf[n]); e = 0
        while n % p == 0: n //= p; e += 1
        f.append((p, e))
    return f

def divisors(f):
    ds = [1]
    for p, e in f:
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds

def phi(n, spf, parts=None):
    ps = set()
    for a in (parts or [n]):
        ps |= {p for p, _ in factor(a, spf)}
    r = n
    for p in ps: r = r // p * (p - 1)
    return r

def main():
    x = int(float(sys.argv[1])); K = int(sys.argv[2]); zexp = float(sys.argv[3]); Hfl = int(sys.argv[4])
    z = int(x ** zexp)
    ms = [4, 5, 6, 7, 8, 9, 10, 12, 13, 30, 60, 105, 210]
    spf = spf_np(K * 2 * x + 2)
    primes = [l for l in range(x + 1, 2 * x + 1) if spf[l] == l]
    rng = random.Random(1)
    print(f"x={x} K={K} z={z} Hfl={Hfl} #primes={len(primes)}")
    for m in ms:
        L = 1
        for k in range(1, K + 1):
            if gcd(k, m) == 1: L = L * k // gcd(L, k)
        res = []
        for trial in range(3):
            while True:
                c = rng.randrange(L)
                if gcd(c, L) == 1: break
            J = [k for k in range(1, K + 1) if gcd(k, m) == 1]
            mu = 0.0; inc = 0; tot = 0
            for l in primes:
                cls = set()
                for k in J:
                    N = k * l + 1
                    if N % m: continue
                    A = N // m
                    for u in divisors(factor(A, spf)):
                        if u <= Hfl or u > z or gcd(u, k) != 1: continue
                        for v in divisors(factor(A // u, spf)):
                            if v <= Hfl or v > z or gcd(u, v) != 1 or gcd(v, k) != 1: continue
                            if (u + c * v) % k: continue
                            inc += 1
                            cls.add((-u * pow(v, -1, l)) % l)
                mu += len(cls) / l
                tot += len(cls)
            # BV main-term prediction for this fibre
            pred = 0.0
            wt = sum(1.0 / (t * log(t)) for t in range(x + 1, 2 * x + 1))  # = int_x^2x dt/(t log t)
            for k in J:
                for v in range(Hfl + 1, z + 1):
                    if gcd(v, k) != 1: continue
                    u0 = (-c * v) % k
                    u = u0 if u0 > Hfl else u0 + k * ((Hfl - u0) // k + 1)
                    while u <= z:
                        if gcd(u, v) == 1:
                            pred += wt / phi(m * u * v, spf, [m, u, v])
                        u += k
            res.append((mu, pred, inc, tot))
        mu = sum(r[0] for r in res) / 3; pred = sum(r[1] for r in res) / 3
        ph = phi(m, spf)
        print(f"m={m:4d} phi={ph:3d} mu={mu:.5f} pred={pred:.5f} mu/pred={mu/pred:.3f} "
              f"m*mu={m*mu:.4f} phi*mu={ph*mu:.4f} dedup_loss={1-sum(r[3] for r in res)/sum(r[2] for r in res):.3f}", flush=True)

main()
