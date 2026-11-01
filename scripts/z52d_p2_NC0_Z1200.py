#!/usr/bin/env python3
"""Z1200: bitset vs set-based propagation of attainable residues (moduli < 1000).

Task: R = set of residues mod m reachable as prod_i q_i^{j_i} (j_i in [0,a_i]) for N = M^2,
computed by the update R <- union_j { r * q^j mod m : r in R } over prime powers (the same
DP as the subset-product propagation). Three implementations on identical factorisations:
  (S) Python set comprehension,
  (B) Python int bitmask: multiplication by c is NOT a shift, so each set bit is moved
      individually (the bitset gives no bit-parallel speedup for a multiplicative action),
  (N) numpy boolean array with a gather index (vectorised 'bitset' surrogate).
Also measured: the additive analogue (R <- R | rotate(R, c)) where a bitset IS a shift, to
show where bit-parallelism applies. Verified: all implementations give identical sets.
"""
import time, json, random
import numpy as np

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def dp_set(pps, m):
    R = {1 % m}
    for q, a in pps:
        pw = [pow(q, j, m) for j in range(a + 1)]
        R = {(r * c) % m for r in R for c in pw}
    return R

def dp_bigint(pps, m):
    R = 1 << (1 % m)
    for q, a in pps:
        pw = [pow(q, j, m) for j in range(a + 1)]
        new = 0
        for c in pw:
            x = R; out = 0
            while x:
                low = x & -x
                r = low.bit_length() - 1
                out |= 1 << ((r * c) % m)
                x ^= low
            new |= out
        R = new
    return {i for i in range(m) if (R >> i) & 1}

def dp_numpy(pps, m):
    R = np.zeros(m, bool); R[1 % m] = True
    ar = np.arange(m)
    for q, a in pps:
        pw = [pow(q, j, m) for j in range(a + 1)]
        new = np.zeros(m, bool)
        idx = np.nonzero(R)[0]
        for c in pw:
            new[(idx * c) % m] = True
        R = new
    return set(np.nonzero(R)[0].tolist())

def additive_bitset(pps, m):
    """additive analogue: sums of a_i * q_i-type shifts; bitset rotate is a single shift"""
    R = 1
    mask = (1 << m) - 1
    for q, a in pps:
        new = 0
        for j in range(a + 1):
            s = (q * j) % m
            new |= ((R << s) | (R >> (m - s))) & mask if s else R
        R = new
    return R

def bench(seed=5, trials=300, mmax=999):
    rnd = random.Random(seed)
    cases = []
    while len(cases) < trials:
        m = rnd.randint(50, mmax)
        p = rnd.choice([q for q in range(5, 3000) if q % 4 == 1 and all(q % d for d in range(2, int(q ** 0.5) + 1))])
        x = rnd.randint(-(-p // 4), p)
        M = p * x
        pps = sorted(factor(M * M).items())
        cases.append((m, pps))
    res = {"set": 0.0, "bigint": 0.0, "numpy": 0.0}
    mism = 0
    for m, pps in cases:
        t = time.perf_counter(); A = dp_set(pps, m); res["set"] += time.perf_counter() - t
        t = time.perf_counter(); B = dp_bigint(pps, m); res["bigint"] += time.perf_counter() - t
        t = time.perf_counter(); C = dp_numpy(pps, m); res["numpy"] += time.perf_counter() - t
        if not (A == B == C):
            mism += 1
    addt = 0.0
    for m, pps in cases:
        t = time.perf_counter(); additive_bitset(pps, m); addt += time.perf_counter() - t
    return res, mism, len(cases), addt

if __name__ == "__main__":
    res, mism, n, addt = bench()
    print(f"cases={n} set-vs-bigint-vs-numpy mismatches={mism}")
    for k, v in res.items():
        print(f"  {k}: total {v:.3f} s  ({v / n * 1e3:.3f} ms/case)  speedup vs set {res['set'] / v:.2f}x")
    print(f"  additive bitset (shift) total {addt:.3f} s")
    json.dump({"cases": n, "mismatches": mism, "seconds": res, "additive_bitset_s": addt},
              open("data/z52b/pass2/NC0/sub/Z1200_bitset.json", "w"), indent=1)
