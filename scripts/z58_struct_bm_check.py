#!/usr/bin/env python3
"""z58 STRUCT: numerical checks of Theorem A (Brauer group of the (★) surface S_n).

S_n^{(k)} : k*u*B*C - u - B = n   (k = 4: full (★); k = 8: C-even sub-line, C = 2C').
Claimed generator of Br(S_n)/Br(Q):  beta_n = (1 - k u C, -n u)  (quaternion algebra).
Checks:
 (1) local invariants of beta_n at random l-adic integral points equal the predicted formula
     (constant 0 at l not dividing 2n -> consistent with unramifiedness on the integral model);
 (2) at every positive integral point (n <= NMAX) the predicted Jacobi identity holds;
     R(m^2) = 0 for all squares; list the non-square zeros (non-BM failures);
 (3) for every non-square n <= NMAX, explicit local points at one place l with v_l(n) odd realising both
     invariant values -> positive-integral BM set non-empty.
Usage: uv run python scripts/z58_struct_bm_check.py [NMAX]
"""
import random, sys
from math import isqrt

def vl(x, l):
    if x == 0:
        return 10**9
    v = 0
    while x % l == 0:
        x //= l; v += 1
    return v

def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1

def hilbert_int(a, b, l):
    """Hilbert symbol (a,b)_l for nonzero integers a,b; l prime or 0 (=infinity)."""
    if l == 0:
        return -1 if (a < 0 and b < 0) else 1
    va, vb = vl(a, l), vl(b, l)
    a1, b1 = a // l**va, b // l**vb
    if l != 2:
        s = (-1) ** (va * vb * ((l - 1) // 2) % 2)
        return s * legendre(a1, l) ** vb * legendre(b1, l) ** va
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(a1) * eps(b1) + va * om(b1) + vb * om(a1)) % 2
    return -1 if e else 1

def hilbert_rat(a, b, l):
    """(a,b)_l for nonzero rationals given as (num, den) pairs: multiply by den^2."""
    (an, ad), (bn, bd) = a, b
    return hilbert_int(an * ad, bn * bd, l)

def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(m) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(m + 1) if s[i]]

def predicted_inv(n, u, C, B, l, k):
    """Predicted inv_l of beta_n at a point (u,C,B) integral at l (B rational num/den with l-unit den)."""
    d = k * u * C - 1
    if l == 0:
        return -1 if (d > 0 and n * u > 0) else (1 if (d > 0) != (n * u > 0) else -1)
    if l == 2:
        if (u * C) % 2 == 0 or k == 8:
            return 1
        return (-1) ** vl(n, 2)
    if n % l != 0:
        return 1
    if u % l == 0:
        return 1
    Bn, Bd = B
    return legendre(-u * Bn * Bd, l) ** vl(n, l)

def check_local(nmax, k, trials=40, rng=random.Random(1)):
    P = primes_upto(60)
    bad = 0; tot = 0
    for n in list(range(1, nmax + 1)) + [-7, -13, -45]:
        for l in P:
            M = l ** 6
            for _ in range(trials):
                u = rng.randrange(1, M) * rng.choice([1, l, l * l])
                C = rng.randrange(1, M) * rng.choice([1, 1, l])
                d = k * u * C - 1
                num = n + u
                if num == 0 or vl(d, l) > vl(num, l):
                    continue  # not an l-adic integral point
                # B = num/d as a rational (reduced l-adically: only its l-adic class matters)
                g = l ** vl(d, l)
                B = (num // g, d // g)
                if B[0] == 0:
                    continue
                inv = hilbert_rat((-d, 1), (-n * u, 1), l)
                pred = predicted_inv(n, u, C, B, l, k) if n > 0 else None
                tot += 1
                if pred is not None and inv != pred:
                    bad += 1
                    if bad < 5:
                        print("MISMATCH", k, n, l, u, C, inv, pred)
    return tot, bad

def positive_points(n, k):
    """All (u,B,C) >= 1 with k u B C - u - B = n."""
    out = []
    u = 1
    while True:
        # B >= 1, C >= 1: d = k u C - 1 divides n + u, d >= k u - 1
        if k * u - 1 > n + u:
            break
        N = n + u
        C = 1
        while k * u * C - 1 <= N:
            d = k * u * C - 1
            if N % d == 0:
                out.append((u, N // d, C))
            C += 1
        u += 1
    return out

def jacobi(a, m):
    a %= m; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                r = -r
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            r = -r
        a %= m
    return r if m == 1 else 0

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    for k in (4, 8):
        tot, bad = check_local(min(nmax, 120), k)
        print(f"[k={k}] (1) local invariant formula: {tot} l-adic points tested, {bad} mismatches")
        sq_bad = 0; jac_bad = 0; zeros = []
        for n in range(1, nmax + 1):
            pts = positive_points(n, k)
            m = isqrt(n)
            if m * m == n and pts:
                sq_bad += 1
            for (u, B, C) in pts:
                prod = 1
                for l in [0] + [p for p in primes_upto(n) if n % p == 0] if n > 1 else [0]:
                    prod *= hilbert_int(-(k * u * C - 1), -n * u, l)
                if prod != 1:
                    jac_bad += 1
                if n % 2 == 1:
                    n1 = n  # part of n coprime to u (primes dividing u and n contribute +1)
                    for p in primes_upto(min(u, n)):
                        if u % p == 0:
                            while n1 % p == 0:
                                n1 //= p
                    if jacobi(-u * B, n1) != -1:
                        jac_bad += 1
            if not pts and m * m != n and n % 4 == 1:
                zeros.append(n)
        print(f"[k={k}] (2) n<={nmax}: squares with points: {sq_bad}; product-formula/Jacobi failures: {jac_bad}")
        print(f"[k={k}]     non-square n=1(4) with no positive point (non-BM failures): {len(zeros)}; first {zeros[:12]}")
        # (3) explicit local points realising both invariants at some l with v_l(n) odd
        fail3 = 0
        for n in range(2, nmax + 1):
            m = isqrt(n)
            if m * m == n:
                continue
            ls = [p for p in primes_upto(n) if n % p == 0 and vl(n, p) % 2 == 1]
            ok = False
            for l in ls:
                vals = set()
                for u in range(1, 4 * l + 3):
                    for C in range(1, 4 * l + 3):
                        d = k * u * C - 1
                        if d % l == 0:
                            continue
                        g = 1
                        inv = hilbert_rat((-d, 1), (-n * u, 1), l)
                        vals.add(inv)
                if vals == {1, -1}:
                    ok = True; break
            if not ok:
                fail3 += 1
                if fail3 < 6:
                    print(f"[k={k}] (3) no sign freedom found at n={n} (odd-valuation primes {ls})")
        print(f"[k={k}] (3) non-square n in [2,{nmax}] without local sign freedom: {fail3}")

if __name__ == "__main__":
    main()
