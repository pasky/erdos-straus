"""R275 from-scratch spot-check of MODP_RECIPROCITY EVIDENCE 2.3.
(A) per-level hit rates vs quartic symbols (q/p)_4 (on (q/p)=1), stratified by p mod lcm(4d,16,q): Cochran-Mantel-Haenszel z.
(B) canonical quartic bit (2w/p)_4 of all b=1 witnesses, p = 5 mod 8.
Usage: review_r275_quartic.py PMAX_A DMAX PMAX_B"""
import sys
from math import isqrt, gcd
import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, isqrt(n) + 1):
        if s[i] == 0:
            blk = s[i*i::i]; blk[blk == 0] = i
    idx = np.nonzero(s == 0)[0]; s[idx] = idx
    return s


def factor(n, spf):
    f = {}
    while n > 1:
        q = int(spf[n]); f[q] = f.get(q, 0) + 1; n //= q
    return f


def divs(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def lcm(*a):
    r = 1
    for x in a: r = r * x // gcd(r, x)
    return r


def main():
    PA = int(sys.argv[1]); DM = int(sys.argv[2]); PB = int(sys.argv[3])
    spf = spf_sieve(PA + 4 * DM + 10)
    P = [p for p in range(5, PA + 1, 4) if spf[p] == p]
    hit = {}
    for p in P:
        for d in range(1, DM + 1):
            n = p + 4 * d
            hit[(p, d)] = any(w % (4 * d) == 4 * d - 1 and w < n for w in divs(factor(n, spf)))
    Qs = [2, 3, 5, 7, 11, 13]
    zs = []
    for q in Qs:
        for d in range(1, DM + 1):
            M = lcm(4 * d, 16, q)
            strata = {}
            for p in P:
                if p == q or pow(q, (p - 1) // 2, p) != 1: continue
                s = 1 if pow(q, (p - 1) // 4, p) == 1 else 0
                st = strata.setdefault(p % M, [0, 0, 0])  # n, n_plus, hits... store list
                st[0] += 1; st[1] += s
                strata[p % M] = st
                strata.setdefault(('h', p % M), []).append((s, hit[(p, d)]))
            # CMH: within each stratum, hypergeometric
            O = E = V = 0.0
            for key, lst in strata.items():
                if not (isinstance(key, tuple)): continue
                n = len(lst)
                if n < 2: continue
                n1 = sum(s for s, _ in lst); h = sum(1 for _, x in lst if x)
                a = sum(1 for s, x in lst if s and x)
                O += a; E += n1 * h / n
                V += n1 * (n - n1) * h * (n - h) / (n * n * (n - 1))
            z = (O - E) / V**0.5 if V > 0 else 0.0
            zs.append((abs(z), q, d, z))
    zs.sort(reverse=True)
    k = len(zs)
    print(f"(A) p<={PA}, {len(P)} primes p=1(4), d<={DM}, q in {Qs}: {k} CMH tests; "
          f"max |z| = {zs[0][0]:.2f} (q={zs[0][1]}, d={zs[0][2]}); #|z|>2 = {sum(1 for t in zs if t[0] > 2)} "
          f"({100*sum(1 for t in zs if t[0] > 2)/k:.1f} %); #|z|>3 = {sum(1 for t in zs if t[0] > 3)}")
    print("   top 5:", [(q, d, round(z, 2)) for _, q, d, z in zs[:5]])
    sq = [t for t in zs if isqrt(t[2])**2 == t[2]]
    print(f"   square levels d=k^2: max |z| = {max(t[0] for t in sq):.2f} over {len(sq)} tests")
    # (B) canonical bit, all certificates of p = 5 mod 8
    plus = minus = 0; npr = 0
    for p in range(5, PB + 1, 8):
        if not all(p % r for r in range(3, isqrt(p) + 1, 2)): continue
        npr += 1
        m = np.arange(1, (p + 1) // 3 + 2, dtype=np.int64)
        g = (-p) % (4 * m)
        ok = (g > 0) & ((m + 1) % np.where(g > 0, g, 1) == 0)
        for mm, gg in zip(m[ok].tolist(), g[ok].tolist()):
            d = (p + gg) // (4 * mm); c = (mm + 1) // gg; w = 4 * c * d - 1
            t = pow(2 * w, (p - 1) // 4, p)
            assert t in (1, p - 1)
            if t == 1: plus += 1
            else: minus += 1
    tot = plus + minus
    print(f"(B) p = 5 (8), p<={PB}: {npr} primes, {tot} witnesses: (2w/p)_4 = +1: {plus} ({100*plus/tot:.2f} %), "
          f"-1: {minus} ({100*minus/tot:.2f} %); z = {(plus - minus)/tot**0.5:.2f} (naive)")


if __name__ == "__main__":
    main()
