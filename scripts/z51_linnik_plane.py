#!/usr/bin/env python3
"""z51 linnik: word classes meeting a Pi-plane (EXSET_LINNIK §2).

Pi-plane: profinite points x with x = 1 in Z_l for every prime l not in Pi (incl. l = 2), x_q in Z_q^* free (q in Pi).
A W1 class (pivot M, u | M+1, residue -u mod M) meets the plane iff -u == 1 mod m, m := Pi-free part of M; it then
forbids the box x == -u mod h, h := Pi-part of M.  Lemma 2.3: such classes <-> words (m, a, b) of h,
h = m*a*b - a - b, with u = a*m - 1, t = b*m - 1.  W2 classes (pivot uv, residue -(u+v)) meeting the plane are
enumerated via (D*m1 - h2)(D*m2 - h1) = D + h (u = h1*m1, v = h2*m2, D*m1*m2 = u + v + 1).

Functions return labels as dicts with modulus, box residue mod h, and ES5 / U certificate status at the plane.
`brute_w1(h, Pi, MB)` and `brute_w2(...)` enumerate classes directly (independent check).
"""
import math, sys, random, json
from functools import lru_cache

_SPF = None
def set_spf(limit):
    """smallest-prime-factor table (numpy) to speed up factor(); falls back to trial division above limit."""
    global _SPF
    import numpy as np
    spf = np.zeros(limit + 1, dtype=np.int32)
    for i in range(2, math.isqrt(limit) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    _SPF = spf

def factor(n):
    if _SPF is not None and n < len(_SPF):
        f = {}
        while n > 1:
            p = int(_SPF[n])
            if p == 0:
                p = n
            f[p] = f.get(p, 0) + 1
            n //= p
        return f
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def coprime_to(m, Pi):
    return all(m % q for q in Pi)

def crt_plane(h, c, mfree, mod):
    """x mod `mod` for the plane point with x == c (mod h), x == 1 (mod mfree-part); mod = h * mfree, gcd(h,mfree)=1."""
    # x = 1 + mfree * k, need 1 + mfree*k == c mod h
    inv = pow(mfree % h, -1, h) if h > 1 else 0
    k = ((c - 1) * inv) % h if h > 1 else 0
    return (1 + mfree * k) % mod

def es5_slots_cert(t, u, v):
    return any(s % 4 == 0 for s in (t, u, v, t * u - 1, t * v - 1))

def u_cert(u, v):
    return any(s % 4 == 0 or s % 8 == 7 for s in (u, v))

def w1_labels(h, Pi):
    """W1 classes meeting the plane with Pi-part exactly h (h > 1, h a Pi-number)."""
    out = []
    amax = 1 + math.isqrt(h + 1) + 1
    seen = set()
    for a in range(1, amax + 1):
        for b in divisors(h + a):
            if b < a:
                continue
            if (h + a + b) % (a * b):
                continue
            m = (h + a + b) // (a * b)
            for (aa, bb) in ((a, b), (b, a)):
                if (aa, bb) in seen:
                    continue
                seen.add((aa, bb))
                if aa * m < 2 or bb * m < 2:
                    continue
                if not coprime_to(m, Pi):
                    continue
                u, t = aa * m - 1, bb * m - 1
                M = h * m
                assert (M + 1) % u == 0 and t * u - 1 == M
                c = (-u) % h
                # v mod 8 at the plane: x mod 8M
                mf = 8 * m
                X0 = crt_plane(h, c, mf, h * mf)
                assert (X0 + u) % M == 0
                v8 = ((X0 + u) // M) % 8
                vv = v8 + 8  # representative of v mod 8 (positive)
                out.append(dict(kind="W1", M=M, m=m, u=u, t=t, c=c, es5=es5_slots_cert(t, u, vv),
                                U=u_cert(u, vv)))
    return out

def unitary_splits(h):
    f = factor(h)
    ps = [p ** e for p, e in f.items()]
    res = []
    for mask in range(1 << len(ps)):
        h1 = 1
        for i, pp in enumerate(ps):
            if mask >> i & 1:
                h1 *= pp
        res.append((h1, h // h1))
    return res

def w2_labels(h, Pi):
    """W2 classes (pivot uv, gcd(u,v)=1) meeting the plane with Pi-part of uv exactly h."""
    out = {}
    fmax = math.isqrt(2 * h + 2) + 1
    for (h1, h2) in unitary_splits(h):
        for f in range(1, fmax + 1):
            # case f1 = f <= f2
            for D in divisors(f + h2):
                if (D + h) % f:
                    continue
                f2 = (D + h) // f
                if f2 < f or (f2 + h1) % D:
                    continue
                m1, m2 = (f + h2) // D, (f2 + h1) // D
                if m1 >= 1 and m2 >= 1:
                    _add_w2(out, h, h1, h2, m1, m2, D, Pi)
            # case f2 = f < f1
            for D in divisors(f + h1):
                if (D + h) % f:
                    continue
                f1 = (D + h) // f
                if f1 <= f or (f1 + h2) % D:
                    continue
                m1, m2 = (f1 + h2) // D, (f + h1) // D
                if m1 >= 1 and m2 >= 1:
                    _add_w2(out, h, h1, h2, m1, m2, D, Pi)
    return list(out.values())

def _add_w2(out, h, h1, h2, m1, m2, D, Pi):
    u, v = h1 * m1, h2 * m2
    m = m1 * m2
    if math.gcd(u, v) != 1 or not coprime_to(m, Pi):
        return
    assert D * m == u + v + 1
    key = (min(u, v), max(u, v))
    if key in out:
        return
    c = (-(u + v)) % h
    mf = 4 * m
    X0 = crt_plane(h, c, mf, h * mf)
    assert (X0 + u + v) % (u * v) == 0
    t4 = ((X0 + u + v) // (u * v)) % 4
    tt = t4 + 4
    # v, u are exact here; t known mod 4 (enough for slots t, tu-1, tv-1 mod 4)
    out[key] = dict(kind="W2", M=u * v, u=u, v=v, c=c, es5=es5_slots_cert(tt, u, v), U=u_cert(u, v))

def labels(h, Pi):
    return w1_labels(h, Pi) + w2_labels(h, Pi)

# ---------------- brute-force cross-checks ----------------
def brute_w1(h, Pi, mbound):
    """All W1 classes with Pi-part h and Pi-free part m <= mbound containing the plane point's box."""
    res = set()
    for m in range(1, mbound + 1):
        if not coprime_to(m, Pi):
            continue
        M = h * m
        for u in divisors(M + 1):
            if (-u - 1) % m:          # -u == 1 mod m
                continue
            res.add((M, (-u) % h, u))
    return res

def brute_w2(h, Pi, mbound):
    res = set()
    for m in range(1, mbound + 1):
        if not coprime_to(m, Pi):
            continue
        N = h * m
        for u in divisors(N):
            v = N // u
            if u > v or math.gcd(u, v) != 1:
                continue
            if (u + v + 1) % m:
                continue
            res.add((N, (-(u + v)) % h, u))
    return res

def selfcheck(cap=3000):
    """Labels with Pi-free part m <= cap must coincide with the brute-force class list (m <= cap)."""
    Pi = [11, 13, 17, 19, 23, 29, 31]
    hs = [11, 13 * 17, 11 * 23, 31, 19 * 29, 11 * 11, 11 * 13 * 17, 13 * 13 * 19]
    for h in hs:
        L1 = {(d["M"], d["c"], d["u"]) for d in w1_labels(h, Pi) if d["m"] <= cap}
        B1 = brute_w1(h, Pi, cap)
        assert L1 == B1, (h, L1 ^ B1)
        L2 = {(d["M"], d["c"], min(d["u"], d["v"])) for d in w2_labels(h, Pi) if d["M"] // h <= cap}
        B2 = brute_w2(h, Pi, cap)
        assert L2 == B2, (h, sorted(L2 ^ B2)[:5])
        print("h=%d: W1 %d, W2 %d labels with m <= %d: brute force agrees" % (h, len(L1), len(L2), cap), flush=True)

if __name__ == "__main__":
    selfcheck()
