"""R94 review A (from scratch): toy fibre masses mu_c for the m-atom family.
Toy deviations from the note (stated): z_j = x_j^{zexp} (default 1/4, keeps z_j^2 < l so
Lemma 1.3 distinctness still holds), floor u,v >= 1 but m*u*v > K enforced (Lemma 1.3(iii)),
no omega cutoff, no pruning. K small. Counts every (k,l,u,v) once; optional dedup check.
Usage: uv run --with numpy python scripts/review_emnA_mass.py X K [zexp] [dedup_m]
"""
import sys, math, random
import numpy as np
from math import gcd

X = int(float(sys.argv[1])); K = int(sys.argv[2])
zexp = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
dedup_m = int(sys.argv[4]) if len(sys.argv) > 4 else 0
F = int(sys.argv[5]) if len(sys.argv) > 5 else 0   # floor: u,v > F (same for all m, like H)
MS = [int(a) for a in sys.argv[6].split(',')] if len(sys.argv) > 6 else [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 30, 60, 210]
sv = np.ones(X + 1, dtype=bool); sv[:2] = False
for i in range(2, int(X ** .5) + 1):
    if sv[i]: sv[i*i::i] = False
inv = 1.0 / np.arange(1, X + 2, dtype=np.float64); inv[0] = 0
x0 = int(math.isqrt(X))
blocks = []
x = x0
while x < X:
    blocks.append((x, min(2 * x, X))); x *= 2

def phi(n):
    r, p, y = n, 2, n
    while p * p <= y:
        if y % p == 0:
            while y % p == 0: y //= p
            r -= r // p
        p += 1
    if y > 1: r -= r // y
    return r

def mu_c(m, c, kset, dedup=False):
    tot = 0.0; seen = set(); dup = 0
    for (lo, hi) in blocks:
        z = int(lo ** zexp)
        for k in kset:
            if gcd(c, k) != 1: continue
            cinv = pow(c, -1, k) if k > 1 else 0
            for u in range(F + 1, z + 1):
                if gcd(u, k) != 1: continue
                v0 = (-u * cinv) % k if k > 1 else 0
                vst = v0 + k * max(0, -(-(F + 1 - v0) // k))
                for v in range(vst, z + 1, k):
                    if v <= F or gcd(u, v) != 1 or gcd(v, k) != 1: continue
                    assert (u + c * v) % k == 0
                    q = m * u * v
                    if q <= K: continue
                    a = (-pow(k, -1, q)) % q
                    st = lo + 1 + ((a - lo - 1) % q)
                    ls = np.arange(st, hi + 1, q)
                    ls = ls[sv[ls]]
                    tot += inv[ls - 1].sum()   # inv[i-1]=1/i
                    if dedup:
                        for l in ls.tolist():
                            key = (l, (-u * pow(v, -1, l)) % l)
                            if key in seen: dup += 1
                            seen.add(key)
    return tot, dup

t = math.log(X)
random.seed(1)
print(f"X={X} K={K} zexp={zexp} F={F} t={t:.2f} blocks={len(blocks)}")
print(" m  phi  #k  c-type    mu_c     m*mu  phi*mu")
for m in MS:
    kset = [k for k in range(1, K + 1) if gcd(k, m) == 1]
    L = 1
    for k in kset: L = L * k // gcd(L, k)
    res = []
    for trial in range(3):
        while True:
            c = random.randrange(L)
            if gcd(c, L) == 1: break
        mu, dup = mu_c(m, c, kset, dedup=(m == dedup_m and trial == 0))
        res.append(mu)
        if m == dedup_m and trial == 0: print(f"   dedup check m={m}: duplicates={dup}")
    mu = sum(res) / len(res)
    mu0, _ = mu_c(m, 0, kset)
    print(f"{m:3d} {phi(m):4d} {len(kset):3d}  reduced {mu:9.4f} {m*mu:8.3f} {phi(m)*mu:8.3f}   c=0: mu={mu0:.4f} phi*mu0={phi(m)*mu0:.3f}")
    sys.stdout.flush()
