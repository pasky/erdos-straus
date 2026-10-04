#!/usr/bin/env python3
"""TWIN4 numerics (EVIDENCE).

Part A: exact check of Lemma 2.3 (rough-partner Brun-Titchmarsh):
  sum_{R in R_s(w), x<R<=2x, R=b (q)} 1/R  <=  3(s+1)(1+H+...+H^{s-1}) / (phi(q) log(x/q)).
Part B: toy ternary system: vertex residues mod a prime j of classes -4D mod jR,
  R = l_a l_b (primes >= w0), split into TW3's proved part (l_b >= w0*q) and the
  former residual (l_b < w0*q). Reports mass, second moment, max, and the
  random prediction (mass^2/j).

Usage: uv run --with numpy python scripts/twin4_rough_bt.py A [xmax]
       uv run --with numpy python scripts/twin4_rough_bt.py B X j1 j2 ...
"""
import sys, math, random
import numpy as np


def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            blk = spf[p * p::p]
            blk[blk == 0] = p
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        f[p] = e
    return f


def phi(n, spf):
    r = n
    for p in factor(n, spf):
        r = r // p * (p - 1)
    return r


def part_a(xmax=2_000_000, seed=1):
    random.seed(seed)
    spf = spf_sieve(2 * xmax)
    n = np.arange(2 * xmax + 1)
    # Omega and least prime factor
    om = np.zeros(2 * xmax + 1, dtype=np.int8)
    lpf = spf.copy()
    m = n.copy()
    m[0] = 1
    while True:
        mask = m > 1
        if not mask.any():
            break
        om[mask] += 1
        m[mask] //= spf[m[mask]]
    primes = np.nonzero((spf == n) & (n >= 2))[0]
    worst = 0.0
    rows = 0
    for s in (1, 2, 3):
        for w in (2, 5, 30, 100):
            ok = (lpf > w) & (om >= 1) & (om <= s)
            for q in (1, 3, 7, 30, 101, 210, 1009, 2310, 10007):
                for x in (xmax // 64, xmax // 8, xmax):
                    Y = x / q
                    if Y < 2 ** (s + 1):
                        continue
                    Z = Y ** (1.0 / (s + 1))
                    H = sum(1.0 / (p - 1) for p in primes if w < p <= Z)
                    bound = 3 * (s + 1) * sum(H ** i for i in range(s)) / (phi(q, spf) * math.log(Y))
                    units = [b for b in range(q) if math.gcd(b, q) == 1] or [0]
                    for b in random.sample(units, min(5, len(units))):
                        start = x + 1 + ((b - x - 1) % q)
                        R = np.arange(start, 2 * x + 1, q)
                        R = R[ok[R]]
                        lhs = float(np.sum(1.0 / R)) if len(R) else 0.0
                        worst = max(worst, lhs / bound)
                        rows += 1
            print(f"s={s} w={w}: cumulative worst lhs/bound = {worst:.4f} over {rows} cases", flush=True)
    print(f"PART A: worst ratio {worst:.4f} (Lemma 2.3 predicts <= 1)")


def part_b(X, js, w0=11):
    Amax = X // 4 + 1
    spf = spf_sieve(Amax)
    for j in js:
        Rmax = X // j
        sp = spf_sieve(Rmax // w0 + 1) if Rmax // w0 + 1 > 2 else None
        prs = [p for p in range(w0, Rmax // w0 + 1) if sp[p] == p and p != j]
        Vp = np.zeros(j)
        Vr = np.zeros(j)
        nR = 0
        for ia, la in enumerate(prs):
            if la * la > Rmax:
                break
            for lb in prs[ia:]:
                R = la * lb
                if R > Rmax:
                    break
                if R <= j or (j * R) % 4 != 3:   # toy C0 = 1: large means R > j
                    continue
                nR += 1
                A = (j * R + 1) // 4
                f = list(factor(A, spf).items())
                trip = [(1, 1, 1)]
                for p, e in f:
                    new = []
                    for (u, v, t) in trip:
                        for i in range(e + 1):
                            new.append((u * p ** i, v, t * p ** (e - i)))
                        for i in range(1, e + 1):
                            new.append((u, v * p ** i, t * p ** (e - i)))
                    trip = new
                for (u, v, t) in trip:
                    a = (-u * pow(v, -1, j)) % j
                    srt = sorted((u, v, t))
                    q = 4 * srt[0] * srt[1]
                    if lb >= w0 * q:
                        Vp[a] += 1.0 / R
                    else:
                        Vr[a] += 1.0 / R
        for name, V in (("proved(l_b>=w0 q)", Vp), ("residual(l_b<w0 q)", Vr)):
            S1, S2 = V.sum(), (V ** 2).sum()
            print(f"j={j} {name}: #R={nR} mass={S1:.3f} sum V^2={S2:.4f} max={V.max():.4f} rand={S1*S1/j:.4f}", flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "A":
        part_a(int(float(sys.argv[2])) if len(sys.argv) > 2 else 2_000_000)
    else:
        part_b(int(float(sys.argv[2])), [int(a) for a in sys.argv[3:]])
