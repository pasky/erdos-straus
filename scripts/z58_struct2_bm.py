#!/usr/bin/env python3
"""z58 STRUCT2: numerical checks of Theorem B (Brauer group of the Type II threefold X_n).

X_n^{(K)} : K*a*b*c*d = a + b + n*c   (K = 4: full ET Type II; K = 8: d-even half / numerator 8).
Claimed generator of Br(X_n)/Br(Q):  beta_n = (1 - K a c d, -n a c) = (-f, -nac), f = K a c d - 1.
Checks (EVIDENCE; the proof is in Z58_STRUCT2.md):
 (1) local Hilbert symbol (-f,-nac)_l at random l-adic integral points of the Z-model equals the predicted formula
     (in particular +1 identically at l not dividing 2n);
 (2) at every positive integral point (n <= NMAX odd) the predicted local signs multiply to +1 with e_inf = -1, i.e.
     prod_{l | n, l not dividing ac} (-f/l)^{v_l(n)} = -1 ; N(m^2) = 0 for odd squares; list non-square zeros;
 (3) for every odd non-square n <= NMAX: explicit l-adic points (l with v_l(n) odd) realising both signs.
Usage: uv run python scripts/z58_struct2_bm.py [NMAX] [K]
"""
import random, sys
from math import isqrt, gcd
sys.path.insert(0, 'scripts')
from z58_struct_bm_check import vl, legendre, hilbert_int, primes_upto

def predicted(n, a, c, d, l, K):
    f = K * a * c * d - 1
    if l == 0:
        return -1
    if l == 2:
        if K == 8 or (a * c * d) % 2 == 0:
            return 1
        return (-1) ** vl(n, 2)
    if f % l == 0 or (a * c) % l == 0 or n % l != 0:
        return 1
    return legendre(-f, l) ** vl(n, l)

def check_local(nmax, K, trials, rng):
    P = primes_upto(40); bad = tot = 0
    for _ in range(trials):
        n = rng.randrange(1, nmax + 1)
        for l in P:
            M = l ** 5
            a, c, d = (rng.randrange(1, M) for _ in range(3))
            f = K * a * c * d - 1
            num = a + n * c
            if vl(num, l) < vl(f, l):
                continue            # b not l-integral: not a point of the Z-model over Z_l
            tot += 1
            if hilbert_int(-f, -n * a * c, l) != predicted(n, a, c, d, l, K):
                bad += 1
                print('LOCAL MISMATCH', n, a, c, d, l, K)
    return tot, bad

def positive_points(n, K):
    """all (a,b,c,d) in N^4 with K abcd = a+b+nc (exact (a,b)-loop: K a b d = n + e, e = (a+b)/c)."""
    out = []
    a = 1
    while K * a <= n + a + 1:
        b = 1
        while True:
            q = K * a * b
            if q > n + a + b:
                break
            e = (-n) % q
            if 1 <= e <= a + b and (a + b) % e == 0:
                c = (a + b) // e; d = (n + e) // q
                assert K * a * b * c * d == a + b + n * c
                out.append((a, b, c, d))
            b += 1
        a += 1
    return out

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    rng = random.Random(58)
    tot, bad = check_local(nmax, K, 4000, rng)
    print(f'K={K} (1) local formula: {tot} l-adic points, {bad} mismatches')
    P = primes_upto(nmax + 10)
    zeros = []; badg = 0; npts = 0
    for n in range(1, nmax + 1, 2):
        pts = positive_points(n, K)
        sq = isqrt(n) ** 2 == n
        if sq and pts:
            print('SQUARE WITH POINT', n, pts[0]); badg += 1
        if not pts and not sq:
            zeros.append(n)
        for (a, b, c, d) in pts:
            npts += 1
            s = 1
            for l in P:
                if l > n: break
                if n % l == 0 and l != 2:
                    s *= predicted(n, a, c, d, l, K)
            if s != -1:
                print('GLOBAL SIGN FAIL', n, (a, b, c, d)); badg += 1
    print(f'K={K} (2) {npts} positive points, n<= {nmax} odd: {badg} failures; odd non-square zeros: {zeros}')
    # (3) both signs at some l with v_l(n) odd, at the point a=c=1, d chosen mod l
    bad3 = 0
    for n in range(3, nmax + 1, 2):
        if isqrt(n) ** 2 == n: continue
        l = next(l for l in P if n % l == 0 and vl(n, l) % 2 == 1)
        signs = set()
        for d in range(1, 4 * l + 1):
            f = K * d - 1
            if f % l == 0: continue
            signs.add(predicted(n, 1, 1, d, l, K))   # b = (n+1)/f is an l-unit-denominator rational: l-integral
        if signs != {1, -1}:
            bad3 += 1; print('NO SIGN FREEDOM', n, l)
    print(f'K={K} (3) odd non-squares with both signs at an odd-valuation prime: failures {bad3}')
    sys.exit(1 if (bad or badg or bad3) else 0)

if __name__ == '__main__':
    main()
