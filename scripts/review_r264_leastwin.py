"""R264 from-scratch recheck of FORCED_WINDOW §6 numerics (no author code used).

For every prime p ≡ 1 (4) ≤ N: least window m0 (m ≡ 3 (4), gcd(m,p)=1, m ≤ MMAX) with a cap-0 certificate, i.e. divisors
d1, d2 | K = (p+m)/4 with d1 + d2 ≡ 0 (mod m).  At m0 we enumerate the full delta-box to get the minimum over
certificates of max|delta| and of support size.  Exact ES rebuild (Type II) for every CHECK-th p.
Stats (hard primes p mod 840 in {1,121,169,289,361,529}): kind of m0, Omega/omega/u/log tau(K^2) at m0 vs failed windows,
success rate per kind and floor(log2(tau(K^2)/m)).
Usage: python review_r264_leastwin.py N MMAX CHECK [sample_seed sample_size]
"""
import sys
import random
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, log, log2, floor

import numpy as np

N, MMAX, CHECK = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
SAMPLE = None
if len(sys.argv) > 5:
    random.seed(int(sys.argv[4]))
    SAMPLE = int(sys.argv[5])

LIM = (N + MMAX) // 4 + 2
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, int(LIM**0.5) + 1):
    if spf[i] == 0:
        blk = spf[i * i :: i]
        blk[blk == 0] = i
spf_l = spf.tolist()


def fac(n):
    f = {}
    while n > 1:
        s = spf_l[n] or n
        f[s] = f.get(s, 0) + 1
        n //= s
    return f


sv = np.ones(N + 1, dtype=bool)
sv[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sv[i]:
        sv[i * i :: i] = False
small_primes = set(np.nonzero(sv[: MMAX + 1])[0].tolist())
P = [int(x) for x in np.nonzero(sv)[0] if x % 4 == 1]
if SAMPLE:
    P = sorted(random.sample(P, SAMPLE))


def jac_leg(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


def has_cert(K, f, m):
    divs = {1}
    for s, b in f.items():
        sm = s % m
        new = set()
        for d in divs:
            x = d
            for _ in range(b + 1):
                new.add(x)
                x = x * sm % m
        divs = new
    return any((-d) % m in divs for d in divs)


def best_cert(f, m):
    S = sorted(f)
    best_max, best_sup, cert = 99, 99, None
    for dl in product(*[range(-f[s], f[s] + 1) for s in S]):
        v = 1
        for s, e in zip(S, dl):
            v = v * pow(s, e, m) % m if e >= 0 else v * pow(pow(s, -e, m), -1, m) % m
        if v == m - 1:
            mx = max(abs(e) for e in dl)
            sp = sum(1 for e in dl if e)
            if mx < best_max:
                best_max, cert = mx, dict(zip(S, dl))
            best_sup = min(best_sup, sp)
    return best_max, best_sup, cert


def rebuild(p, m, cert):
    K = (p + m) // 4
    u = v = 1
    for s, e in cert.items():
        if e > 0:
            u *= s**e
        elif e < 0:
            v *= s ** (-e)
    # 4/p = 1/K + m/(pK); m/K = 1/a + 1/b with u+v = m*g: a = K(u+v)/(m u)?? derive: u/v ≡ -1 (m), uv | K
    g = (u + v) // m
    # m/K = (u+v)/(gK) = u/(gK) + v/(gK) = 1/(gK/u) + 1/(gK/v); integers since u,v | K
    y, z = p * (g * K // u), p * (g * K // v)
    assert (g * K) % u == 0 and (g * K) % v == 0
    assert Fraction(4, p) == Fraction(1, K) + Fraction(1, y) + Fraction(1, z)


HARD = {1, 121, 169, 289, 361, 529}
hist_all, hist_hard = Counter(), Counter()
maxd = Counter()
sup = Counter()
maxd_h, sup_h = Counter(), Counter()
kind_h = Counter()
succ_feat, fail_feat = [], []
rate = defaultdict(lambda: [0, 0])
record = (0, 0)
nchk = 0
m3_forced = m3_unforced = 0
for idx, p in enumerate(P):
    hard = p % 840 in HARD
    m = 3
    while True:
        if m > MMAX:
            raise SystemExit(f"no window <= {MMAX} for p={p}")
        if p % m == 0:
            m += 4
            continue
        K = (p + m) // 4
        f = fac(K)
        ok = has_cert(K, f, m)
        if hard:
            Om = sum(f.values())
            om = len(f)
            Pp = max(f)
            tau2 = 1
            for b in f.values():
                tau2 *= 2 * b + 1
            feat = (Om, om, log(K) / log(Pp), log(tau2))
            if m in small_primes:
                kd = "F" if jac_leg(p, m) == -1 else "U"
            else:
                kd = "C"
            bin_ = floor(log2(tau2 / m))
            rate[(kd, bin_)][0] += 1
            rate[(kd, bin_)][1] += ok
            (succ_feat if ok else fail_feat).append(feat)
        if ok:
            break
        m += 4
    if m == 3:
        if p % 3 == 2:
            m3_forced += 1
        else:
            m3_unforced += 1
    hist_all[m] += 1
    if m > record[1]:
        record = (p, m)
    bm, bs, cert = best_cert(f, m)
    maxd[min(bm, 3)] += 1
    sup[min(bs, 3)] += 1
    if hard:
        hist_hard[m] += 1
        maxd_h[min(bm, 3)] += 1
        sup_h[min(bs, 3)] += 1
        kind_h[kd] += 1
    if idx % CHECK == 0:
        rebuild(p, m, cert)
        nchk += 1

n = len(P)
nh = sum(hist_hard.values())
print(f"primes p≡1(4) checked: {n}; exact rebuilds: {nchk}; max m0 = {record[1]} at p = {record[0]}")
print(f"m0=3: {hist_all[3]} (forced p≡2(3): {m3_forced}, unforced: {m3_unforced})")
print("hist all:", sorted(hist_all.items()))
print(f"hard primes: {nh}; hist:", sorted(hist_hard.items()))
print("kind of m0 (hard):", dict(kind_h))
print("ALL: min-over-certs max|delta| distribution (3 = >=3):", sorted(maxd.items()), f"share<=1: {maxd[1]/n:.4f}")
print("ALL: min support:", sorted(sup.items()), f"share 1: {sup[1]/n:.4f}, <=2: {(sup[1]+sup[2])/n:.4f}")
if nh:
    print("HARD: max|delta|:", sorted(maxd_h.items()), f"share<=1: {maxd_h[1]/nh:.4f}")
    print("HARD: support:", sorted(sup_h.items()), f"share 1: {sup_h[1]/nh:.4f} <=2: {(sup_h[1]+sup_h[2])/nh:.4f}")
    sf = np.array(succ_feat)
    ff = np.array(fail_feat)
    al = np.vstack([sf, ff])
    print("HARD means (Omega, omega, u, log tau2): at m0", sf.mean(0).round(3), " failed windows", ff.mean(0).round(3),
          " all scanned (incl m0)", al.mean(0).round(3))
    for kd in "FUC":
        row = [(b, rate[(kd, b)][0], round(rate[(kd, b)][1] / rate[(kd, b)][0], 3)) for b in range(-4, 8) if rate[(kd, b)][0]]
        print(f"  rate {kd}: (bin, tries, success)", row)
    tries = sum(rate[("F", b)][0] for b in range(2, 30))
    fails = sum(rate[("F", b)][0] - rate[("F", b)][1] for b in range(2, 30))
    print(f"  forced windows with tau(K^2) >= 4m: {tries} tries, {fails} failures")
