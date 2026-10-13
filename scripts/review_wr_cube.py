"""R164 from-scratch checks for WINDMILL_REDUCTION §10.
(a) Comp 10.2: for p = 1 (24) <= P, t = 3 (4) <= T, N = tp+1: the forms [m, 2, N/m] (m | N) are pairwise
    inequivalent (definite Gauss reduction) except {1,N} and {2,N/2}; also count certificates
    (m | N, m = -1 mod t, 4 | m), how many are non-primitive (m, N/m both even), and classes containing one.
(b) Prop 10.3 demo: for a few (p,t,l | t) and every reduced form Q of disc -4tp f^2 (f = 1 and f = l: ring class
    group of conductor l), the set {Q(x,y) mod l : gcd(x,y)=1, l does not divide Q(x,y)} is exactly one square class.
"""
import sys
from math import gcd, isqrt
from review_wr_zagier import primes


def reduce_def(a, b, c):
    """Gauss reduction of a positive definite form (any content): |b| <= a <= c, b >= 0 if |b| = a or a = c."""
    D = b * b - 4 * a * c
    while True:
        k = (a - b) // (2 * a)          # b + 2ak in (-a, a]
        b = b + 2 * a * k
        c = (b * b - D) // (4 * a)
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)


def divisors(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(small + [n // d for d in small]))


def part_a(P, T):
    bad = 0; certs = 0; nonprim = 0; cert_classes = set(); cases = 0
    for p in primes(P):
        if p % 24 != 1:
            continue
        for t in range(3, T + 1, 4):
            N = t * p + 1; cases += 1
            ds = divisors(N)
            cls = {}
            for m in ds:
                f = reduce_def(m, 2, N // m)
                assert 4 - 4 * m * (N // m) == -4 * t * p
                cls.setdefault(f, []).append(m)
            for f, ms in cls.items():
                if len(ms) > 1 and set(ms) not in ({1, N}, {2, N // 2}):
                    bad += 1; print("collision", p, t, ms)
            for m in ds:
                if (m + 1) % t == 0 and m % 4 == 0:
                    certs += 1
                    nonprim += (N // m) % 2 == 0
                    cert_classes.add((p, t, reduce_def(m, 2, N // m)))
    print(f"(a) {cases} (p,t) cases; non-trivial class collisions among divisor forms: {bad}; "
          f"certificates {certs} (non-primitive form: {nonprim}); classes containing a certificate: {len(cert_classes)}")


def reduced_forms(D):  # D < 0, all reduced forms (any content)
    out = []
    A = isqrt(-D // 3) + 1
    for a in range(1, A + 1):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            out.append((a, b, c))
    return out


def part_b():
    for (p, t, l) in [(73, 3, 3), (97, 7, 7), (193, 11, 11), (73, 15, 5), (241, 19, 19)]:
        sq = {(x * x) % l for x in range(1, l)}
        for f in (1, l):
            D = -4 * t * p * f * f
            ok = True; nprim = 0
            for (a, b, c) in reduced_forms(D):
                if gcd(gcd(a, b), c) != 1:
                    continue
                nprim += 1
                vals = set()
                R = 3 * l + 3
                for x in range(-R, R + 1):
                    for y in range(-R, R + 1):
                        if gcd(x, y) == 1:
                            v = a * x * x + b * x * y + c * y * y
                            if v % l:
                                vals.add(v % l)
                v0 = next(iter(vals))
                if vals != {(v0 * s) % l for s in sq}:
                    ok = False
            print(f"(b) p={p} t={t} l={l} conductor f={f}: {nprim} primitive classes; each sees exactly one square class mod l: {ok}")


if __name__ == "__main__":
    part_a(int(sys.argv[1]), int(sys.argv[2]))
    part_b()
