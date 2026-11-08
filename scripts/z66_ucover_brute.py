"""z66 UCOVER: brute-force which ET Prop 1.9 family classes contain the profile e_g.

e_g in Zhat^x has components 1 at every prime p != ell and g at ell.  A family class r mod m (m = ell^k m',
ell not dividing m') contains e_g iff r = 1 (mod m') and r = g (mod ell^k).  If k = 0 the class would contain the
square 1, impossible (ET Prop 1.6 / Schinzel); the script only enumerates moduli divisible by ell.

Enumerates every family class (all seven families of ET Prop 1.9, literal parameterisation) with modulus <= MMAX,
directly from the parameters (independent of the derived word equations of Z66_UCOVER.md), and prints the events
(family, parameters, modulus, k, g mod ell^k).
Usage: uv run --with sympy python scripts/z66_ucover_brute.py ELL MMAX
"""
import sys
from math import gcd, isqrt

from sympy import divisors
from sympy.ntheory.residue_ntheory import sqrt_mod


def vpart(m, ell):
    k = 0
    while m % ell == 0:
        m //= ell
        k += 1
    return k, m


def main():
    ell, MMAX = int(sys.argv[1]), int(sys.argv[2])
    events = []
    bad_k0 = []

    def test(fam, params, r, m):
        r %= m
        if gcd(r, m) != 1:
            return
        k, mp = vpart(m, ell)
        if r % mp != 1 % mp:
            return
        if k == 0:
            bad_k0.append((fam, params, r, m))
            return
        events.append((fam, params, m, k, r % ell**k))

    # (A) I-1: n = -f mod 4ad, f | 4a^2 d + 1
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * d
            if m % ell:  # cannot catch e_g unless ell | m (k=0 classes contain 1; checked separately below)
                continue
            for f in divisors(4 * a * a * d + 1):
                test("A", (a, d, f), -f, m)
    # (B) I-2: n = -f mod 4ac, n = -c/a mod f, (4ac, f) = 1; modulus 4acf
    for a in range(1, MMAX // 4 + 1):
        for c in range(1, MMAX // (4 * a) + 1):
            for f in range(1, MMAX // (4 * a * c) + 1):
                if gcd(4 * a * c, f) != 1:
                    continue
                m = 4 * a * c * f
                if m % ell:
                    continue
                M1 = 4 * a * c
                r2 = (-c * pow(a, -1, f)) % f if f > 1 else 0
                # CRT: r = -f mod M1, r = r2 mod f
                r = (-f + M1 * (((r2 + f) * pow(M1, -1, f)) % f)) % m if f > 1 else (-f) % m
                test("B", (a, c, f), r, m)
    # (C) I-3: n = -f mod 4cd, n^2 = -4c^2 d mod f, (4cd, f) = 1; modulus 4cdf
    for c in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * c) + 1):
            for f in range(1, MMAX // (4 * c * d) + 1):
                if gcd(4 * c * d, f) != 1:
                    continue
                m = 4 * c * d * f
                if m % ell:
                    continue
                M1 = 4 * c * d
                if f == 1:
                    test("C", (c, d, f, 0), -f, m)
                    continue
                roots = sqrt_mod((-4 * c * c * d) % f, f, all_roots=True) or []
                for x in roots:
                    r = (-f + M1 * (((x + f) * pow(M1, -1, f)) % f)) % m
                    test("C", (c, d, f, x), r, m)
    # (D) I-4 and (E) II-1: e | a+b, (e, 4ab) = 1; D: n = -1/e mod 4ab; E: n = -e mod 4ab
    for a in range(1, MMAX // 4 + 1):
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            if m % ell:
                continue
            for e in divisors(a + b):
                if gcd(e, m) != 1:
                    continue
                test("D", (a, b, e), -pow(e, -1, m), m)
                test("E", (a, b, e), -e, m)
    # (F) II-2: n = -4a^2 d mod f, 4ad = f + 1
    for f in range(3, MMAX + 1, 4):
        if f % ell:
            continue
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):              # 4ad | f + 1 (c = (f+1)/(4ad) arbitrary)
                test("F", (a, d, f), -4 * a * a * d, f)
    # (G) II-3: n = -4a^2 d - e mod 4ade, (4ad, e) = 1
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            for e in range(1, MMAX // (4 * a * d) + 1):
                if gcd(4 * a * d, e) != 1:
                    continue
                m = 4 * a * d * e
                if m % ell:
                    continue
                test("G", (a, d, e), -4 * a * a * d - e, m)

    print(f"# ell={ell} MMAX={MMAX} events={len(events)} k0-classes-containing-1={len(bad_k0)}")
    for ev in sorted(events, key=lambda t: (t[3], t[2], t[0])):
        fam, params, m, k, g = ev
        res = "R" if pow(g, (ell - 1) // 2, ell) == 1 else "N"
        print(f"{fam} params={params} m={m} k={k} g={g} ({res})")


if __name__ == "__main__":
    main()
