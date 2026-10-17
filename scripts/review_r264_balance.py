"""R264 from-scratch check of the 'balance' numerics of FORCED_WINDOW §6 (Hypothesis W, balance part).
For primes q ≡ 3 (8) in (QLO, QHI), generators g_s = s^2 (s odd prime ≤ y) in U_q (cyclic, order n = (q-1)/2 odd):
L_min(q) = least L with {prod g_s^{j_s} : 0 ≤ j_s ≤ L} = U_q (cube box), rho = (L_min + 1)/n^{1/k}.
Bitset (Python int) sumsets over discrete logs.  Reports non-generating count, rho quantiles, and per reduced class
mod 8P (q ≡ 3 (8)) the minimal rho.
Usage: python review_r264_balance.py y QLO QHI
"""
import sys
from math import gcd, isqrt

y, QLO, QHI = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


S = [s for s in range(3, y + 1) if isprime(s)]
k = len(S)
P = 1
for s in S:
    P *= s


def pfac(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def logs(q):
    n = (q - 1) // 2
    # generator h of U_q: h = g^2 for a primitive root g
    fs = pfac(q - 1)
    g = 2
    while any(pow(g, (q - 1) // f, q) == 1 for f in fs):
        g += 1
    h = g * g % q
    table = {}
    x = 1
    for i in range(n):
        table[x] = i
        x = x * h % q
    return n, [table[s * s % q] for s in S]


def covers(n, a, L):
    full = (1 << n) - 1
    cur = 1  # bit 0 = identity
    for ai in a:
        acc = cur
        sh = cur
        for _ in range(L):
            sh = ((sh << ai) | (sh >> (n - ai))) & full if ai else sh
            acc |= sh
        cur = acc
        if cur == full:
            return True
    return cur == full


rows = []
nongen = 0
for q in range(QLO + 1, QHI):
    if q % 8 != 3 or not isprime(q) or P % q == 0:
        continue
    n, a = logs(q)
    gg = n
    for ai in a:
        gg = gcd(gg, ai)
    if gg != 1:
        nongen += 1
        continue
    lo, hi = 0, 1
    while not covers(n, a, hi):
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if covers(n, a, mid):
            hi = mid
        else:
            lo = mid
    rows.append((q, hi, (hi + 1) / n ** (1 / k)))
rho = sorted(r[2] for r in rows)
qs = [rho[min(len(rho) - 1, int(f * len(rho)))] for f in (0, 0.1, 0.5, 0.9, 0.99)] + [rho[-1]]
print(f"y={y} k={k} 8P={8*P}: {len(rows)+nongen} primes q≡3(8) in ({QLO},{QHI}); non-generating {nongen}")
print("rho quantiles 0/10/50/90/99/100%:", [round(x, 3) for x in qs])
cls = {}
for q, L, r in rows:
    c = q % (8 * P)
    cls[c] = min(cls.get(c, 99), r)
adm = [c for c in range(3, 8 * P, 8) if gcd(c, P) == 1]
print(f"admissible classes: {len(adm)}; classes hit: {len(cls)}; max over classes of min rho: {max(cls.values()):.4f}")
worst = max(rows, key=lambda r: r[2])
print("worst q:", worst)
