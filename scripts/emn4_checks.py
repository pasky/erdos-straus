"""EXCEPTIONAL_MN4 sanity checks (finite; not proofs).

1. Lemma 1.1: f_{I,m}(n) <= 2 sum_c w_{c,m}(n), and Type I solvable => some w_{c,m}(n) >= 1  (brute force).
2. Lemma 2.2_m: separation cosh >= 3/2 for forms [f, 2ta, te], ef - t a^2 = 1, t = md.
3. Lemma 6.1_m: quadric point counts with U = cB/2 (f-cusp) and V = t c B/2 (e-cusp).
4. Content-2 forms occur (t = 3 mod 4), as flagged in §2.5.
5. §3.2(c) gain (EVIDENCE): sum_{d~D} g(d) sum_{f~F} rho_{md}(f)/phi(f) divided by (phi(m)/m) D.
Usage: PYTHONPATH=scripts uv run python scripts/emn4_checks.py
"""
from fractions import Fraction
from math import gcd, isqrt
import itertools
import sympy


def typeI_solutions(m, n):
    """Number of ordered (x,y,z) in N^3 with m/n = 1/x+1/y+1/z, n | x, gcd(n, yz) = 1 (ET's f_I)."""
    target = Fraction(m, n)
    sols = set()
    for u in range(n // m + 1, 3 * n // m + 1):  # smallest denominator
        r = target - Fraction(1, u)
        if r <= 0:
            continue
        for v in range(max(u, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fraction(1, v)
            if s <= 0 or s.numerator != 1 or s.denominator < v:
                continue
            for x, y, z in itertools.permutations((u, v, s.denominator)):
                if x % n == 0 and gcd(n, y * z) == 1:
                    sols.add((x, y, z))
    return len(sols)


def w_total(m, n):
    tot = 0
    for c in range(1, 3 * n + 1):
        for a in range(1, 3 * n + 1):
            if m * a * c > 3 * n:
                break
            for d in range(1, 3 * n + 1):
                if m * a * c * d > 3 * n:
                    break
                f = m * a * c * d - n
                if 0 < f <= 2 * n and (m * a * a * d + 1) % f == 0:
                    tot += 1
    return tot


def check1():
    bad = 0
    tested = 0
    solvable = 0
    for m in range(4, 13):
        for n in sympy.primerange(5, 120):
            s = typeI_solutions(m, n)
            w = w_total(m, n)
            tested += 1
            solvable += s > 0
            if s > 2 * w or (s > 0 and w == 0):
                bad += 1
                print("  FAIL", m, n, s, w)
    print(f"check1 (Lemma 1.1): {tested} (m,p) pairs ({solvable} Type I solvable), failures = {bad}")


def forms(t, B):
    out = []
    for a in range(-B, B + 1):
        k = t * a * a + 1
        for f in sympy.divisors(k):
            e = k // f
            out.append((f, 2 * t * a, t * e))
    return out


def check2():
    worst = None
    pairs = 0
    for m in range(4, 13):
        for d in range(1, 5):
            t = m * d
            Q = forms(t, 6)
            for (A, B, C), (A2, B2, C2) in itertools.combinations(Q, 2):
                disc = (B - B2) ** 2 - 4 * (A - A2) * (C - C2)
                ch = 1 + Fraction(disc, 8 * t)  # Lemma 2.1 with |D| = 4t
                pairs += 1
                if worst is None or ch < worst:
                    worst = ch
    print(f"check2 (separation): {pairs} pairs, min cosh = {float(worst):.4f} (claim >= 1.5)")


def check3():
    bad = 0
    cases = 0
    for m in range(4, 13):
        for d in range(1, 4):
            t = m * d
            for l in sympy.primerange(3, 14):
                if t % l == 0:
                    continue
                chi = sympy.jacobi_symbol(-t % l, l) if (-t) % l else 0
                inv2 = pow(2, -1, l)
                for c in range(l):
                    nf = ne = 0
                    tot = 0
                    for U, B, V in itertools.product(range(l), repeat=3):
                        if (B * B - 4 * U * V + 4 * t) % l:
                            continue
                        tot += 1
                        if (U - c * B * inv2) % l == 0:
                            nf += 1
                        if (V - t * c * B * inv2) % l == 0:
                            ne += 1
                    cases += 1
                    pred = (l - 1) if c % l else l * (1 + chi)
                    if tot != l * l + chi * l or nf != pred or ne != pred:
                        bad += 1
    print(f"check3 (local densities): {cases} cases, failures = {bad}")


def check4():
    found = []
    for t in range(3, 60, 4):
        for (A, B, C) in forms(t, 5):
            if gcd(gcd(A, B), C) == 2:
                found.append((t, (A, B, C)))
                break
    print(f"check4 (content-2 forms, t = 3 mod 4): found for {len(found)} values of t, e.g. {found[:2]}")


def rho(k, f):
    return sum(1 for x in range(f) if (k * x * x + 1) % f == 0)


def check5():
    D, F = 300, 300
    print("check5 (EVIDENCE, §3.2(c) gain): ratio = sum_{d~D} g(d) sum_{f~F} rho_{md}(f)/phi(f) / ((phi(m)/m) D)")
    for m in [4, 6, 30, 210, 2310, 7, 11 * 13, 1009]:
        h = Fraction(sympy.totient(m), m)
        s = 0.0
        for d in range(D + 1, 2 * D + 1):
            gd = d / sympy.totient(d)
            inner = 0.0
            for f in range(F + 1, 2 * F + 1):
                if gcd(f, m * d) != 1:
                    continue
                r = rho(m * d, f)
                if r:
                    inner += r / sympy.totient(f)
            s += gd * inner
        print(f"  m={m:5d} phi(m)/m={float(h):.3f} ratio={s / (float(h) * D):.3f}  (raw/D={s / D:.3f})")


if __name__ == "__main__":
    check1()
    check2()
    check3()
    check4()
    check5()
