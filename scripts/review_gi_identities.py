"""R170 from-scratch checks for GROWING_IDENTITIES.md Lemma 1.1, 1.2, 1.3 / Prop 4.1, §5 item 4 formulas.
No author code reused.  Usage: PYTHONPATH=scripts uv run python scripts/review_gi_identities.py [NMAX]
"""
import sys
from fractions import Fraction
from math import gcd, isqrt


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def cubic_points(n):
    """All (c,f,g) in N^3 with c f g - c - f = n, by brute force on c,g (f solved)."""
    pts = []
    # f(cg-1) = n + c ; need cg >= 2.  c <= ? : f>=1 => cg-1 <= n+c => c(g-1) <= n+1.
    # g = 1: (c-1) | n+1 so c <= n+2; g >= 2: 2c-1 <= cg-1 <= n+c so c <= n+1.
    for c in range(1, n + 3):
        g = 1
        while True:
            e = c * g - 1
            if e <= 0:
                g += 1
                continue
            if e > n + c:
                break
            if (n + c) % e == 0:
                pts.append((c, (n + c) // e, g))
            g += 1
    return pts


def hj(n, m):
    """Hirzebruch-Jung (negative) continued fraction of n/m, n>m>=1 coprime."""
    out = []
    while m:
        a = -(-n // m)  # ceil
        out.append(a)
        n, m = m, a * m - n
    return out


def dedekind(m, n):
    s = Fraction(0)
    for k in range(1, n):
        x = Fraction(k, n)
        y = Fraction(k * m % n, n)
        if y == 0:
            continue
        s += (x - Fraction(1, 2)) * (y - Fraction(1, 2))
    return s


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    bad = 0
    nW = 0
    for n in range(1, NMAX + 1):
        pts = cubic_points(n)
        R = len(pts)
        Wp = [p for p in pts if (p[1] * p[2]) % 4 == 1]
        W = len(Wp)
        nW += W
        # Lemma 1.2: fibre by g and by c
        Rg = Wg = 0
        for g in range(1, n + 3):
            N = g * n + 1
            for m in range(1, N + 1):
                if N % m == 0 and (m + 1) % g == 0:
                    Rg += 1
                    if m % 4 == 0:
                        Wg += 1
        Rc = Wc = 0
        for c in range(1, n + 3):
            N = n + c
            for e in range(1, N + 1):
                if N % e == 0 and (e + 1) % c == 0:
                    Rc += 1
                    if ((N // e) * ((e + 1) // c)) % 4 == 1:
                        Wc += 1
        if not (R == Rg == Rc and W == Wg == Wc):
            print("L1.2 FAIL", n, R, Rg, Rc, W, Wg, Wc); bad += 1
        # Lemma 1.1 HJ bijection, entries >= 2
        inner = sorted((c, g, f) for (c, f, g) in Wp if min(c, f, g) >= 2)
        hjset = []
        for m in range(1, n):
            if m % 4 == 0 and gcd(m, n) == 1:
                w = hj(n, m)
                if len(w) == 3:
                    hjset.append(tuple(w))
                    c, g, f = w
                    assert g * f - 1 == m and c * g * f - c - f == n
        if sorted(hjset) != inner:
            print("L1.1 FAIL", n, inner, hjset); bad += 1
        if n % 4 == 1 and W > 0 and len(inner) == 0 and n < 2000:
            print("  note: n=%d has W=%d but no HJ-length-3 m (only boundary certificates)" % (n, W))
        # squares
        r = isqrt(n)
        if r * r == n and n % 2 == 1 and W:
            print("T1 FAIL W(k^2)", n); bad += 1
        # Prop 4.1 on all t = 3 mod 4 up to n+2 and beyond (t <= 3n+10, any divisor)
        if n % 4 == 1:
            for t in range(3, 3 * n + 12, 4):
                N = t * n + 1
                for m2 in range(1, isqrt(N) + 1):
                    for mm in {m2, N // m2} if N % m2 == 0 else ():
                        m = N // mm
                        if m % 4:
                            continue
                        if mm % t in (1, t - 1):
                            eps = 1 if mm % t == 1 else -1
                            if jacobi(mm, n) != eps:
                                print("P4.1 FAIL", n, t, mm); bad += 1
                        # class -1 pairs must have t <= n+2 ; non-trivial class +1 pairs too
                        if mm % t in (1, t - 1) and mm != 1 and t > n + 2:
                            print("D(n) finiteness note FAIL", n, t, mm); bad += 1
    print("cubic/fibration/HJ/Prop4.1 checks to n=%d: %d failures; total W certs %d" % (NMAX, bad, nW))
    # Hirzebruch formula and Riemenschneider-derived r - s formula
    fb = 0
    for n in range(2, 90):
        for m in range(1, n):
            if gcd(m, n) != 1:
                continue
            a = hj(n, m)
            ms = pow(m, -1, n)
            lhs = 12 * dedekind(m, n)
            rhs = sum(x - 3 for x in a) + Fraction(m + ms, n)
            if lhs != rhs:
                fb += 1
            if m < n - 0 and n - m >= 1:
                s = len(hj(n, n - m))
                if len(a) - s != Fraction(m + ms, n) - 1 - lhs:
                    fb += 1
    print("Hirzebruch 12s and r-s formulas, n<90: %d failures" % fb)


if __name__ == "__main__":
    main()


def prop41_large(lo=10**6, cnt=400, tmax=400):
    """Prop 4.1 at larger n (both classes, all divisor pairs), using sympy.divisors."""
    from sympy import divisors
    bad = tot = 0
    for n in range(lo + (1 - lo) % 4, lo + 4 * cnt, 4):
        for t in range(3, tmax, 4):
            N = t * n + 1
            for mm in divisors(N):
                if (N // mm) % 4 == 0 and mm % t in (1, t - 1):
                    tot += 1
                    eps = 1 if mm % t == 1 else -1
                    bad += jacobi(mm, n) != eps
    print("Prop 4.1 large-n check: n in [%d,%d), t<%d: %d pairs, %d failures" % (lo, lo + 4 * cnt, tmax, tot, bad))


def swapped_sum(NMAX=120):
    """Lemma 1.2 'sum over m first': W(n) = sum_{4|m,(m,n)=1} ([r_m | m+1] + [r_m == 1]), r_m = -n^{-1} mod m."""
    bad = 0
    for n in range(1, NMAX + 1):
        W = sum(1 for (c, f, g) in cubic_points(n) if (f * g) % 4 == 1)
        s = b = 0
        for m in range(4, (n + 2) * n + 2, 4):
            if gcd(m, n) != 1:
                continue
            r = (-pow(n, -1, m)) % m
            s += (m + 1) % r == 0 if r else 0
            b += r == 1
        if W != s + b or (n % 4 == 1 and b):
            bad += 1
            print("swap FAIL", n, W, s, b)
    print("swapped-sum formula n<=%d: %d failures" % (NMAX, bad))
