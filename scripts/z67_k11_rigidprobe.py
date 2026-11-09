"""z67 K11: which ET family classes (modulus <= MMAX) contain a fully RIGID two-value profile (EVIDENCE probe).

Profile pi(q1, q2): pi_p = q2 for p in T = {2,3,5,7}, pi_p = q1 for every prime p >= 11, where q1 is a
{2,3,5,7}-unit (so a unit at every p >= 11) and q2 = u/v a rational unit at 2,3,5,7 with q2 = 1 mod 840.
pi lies in K-bar iff (q1/11) = -1.  A class r mod m (m = mT * m'', mT the {2,3,5,7}-part) contains pi iff
r = q2 mod mT and r = q1 mod m''.  Prints the number of catching parameter/family occurrences, the number of distinct classes (m, r),
and the first 12 occurrences (family, parameters, modulus, residue).
Usage: uv run --with sympy python scripts/z67_k11_rigidprobe.py MMAX q1 q2 [q1 q2 ...]   (q as u/v)
"""
import sys
from fractions import Fraction
from math import gcd

from sympy import divisors
from sympy.ntheory.residue_ntheory import sqrt_mod


def tsplit(m):
    mt = 1
    for p in (2, 3, 5, 7):
        while m % p == 0:
            m //= p
            mt *= p
    return mt, m


def contains(r, m, q1, q2):
    r %= m
    if gcd(r, m) != 1:
        return False
    mt, mo = tsplit(m)
    for q, mm in ((q2, mt), (q1, mo)):
        if mm == 1:
            continue
        u, v = q.numerator, q.denominator
        if gcd(v, mm) != 1 or (r * v - u) % mm:
            return False
    return True


def main():
    MMAX = int(sys.argv[1])
    profs = [(Fraction(sys.argv[i]), Fraction(sys.argv[i + 1])) for i in range(2, len(sys.argv), 2)]
    hits = {p: [] for p in profs}

    def test(r, m, tag):
        for p in profs:
            if contains(r, m, *p):
                hits[p].append((tag, m, r % m))
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * d
            for f in divisors(4 * a * a * d + 1):
                test(-f, m, f"I1 a={a} d={d} f={f}")
    for a in range(1, MMAX // 4 + 1):
        for c in range(1, MMAX // (4 * a) + 1):
            M1 = 4 * a * c
            for f in range(2, MMAX // M1 + 1):
                if gcd(M1, f) != 1:
                    continue
                m = M1 * f
                inv = pow(M1, -1, f)
                r2 = (-c * pow(a, -1, f)) % f
                test(-f + M1 * (((r2 + f) * inv) % f), m, f"I2 a={a} c={c} f={f}")
                for x in sqrt_mod((-4 * a * a * c) % f, f, all_roots=True) or []:
                    test(-f + M1 * (((x + f) * inv) % f), m, f"I3 c={a} d={c} f={f} root={x}")
    for a in range(1, MMAX // 4 + 1):
        for b in range(1, MMAX // (4 * a) + 1):
            m = 4 * a * b
            for e in divisors(a + b):
                if gcd(e, m) == 1:
                    test(-pow(e, -1, m), m, f"I4 a={a} b={b} e={e}")
                    test(-e, m, f"II1 a={a} b={b} e={e}")
    for f in range(3, MMAX + 1, 4):
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):
                test(-4 * a * a * d, f, f"II2 a={a} d={d} c={P // (a * d)}")
    for a in range(1, MMAX // 4 + 1):
        for d in range(1, MMAX // (4 * a) + 1):
            for e in range(1, MMAX // (4 * a * d) + 1):
                if gcd(4 * a * d, e) == 1:
                    test(-4 * a * a * d - e, 4 * a * d * e, f"II3 a={a} d={d} e={e}")
    for p in profs:
        h = hits[p]
        dist = len(set((x[1], x[2]) for x in h))
        nr = "non-residue" if pow((p[0].numerator * pow(p[0].denominator, -1, 11)) % 11, 5, 11) == 10 else "RESIDUE (outside K, control)"
        print(f"q1={p[0]} q2={p[1]} [q1 mod 11 {nr}]: {len(h)} catching parameter/family occurrences, "
              f"{dist} distinct classes (m, r) (modulus <= {MMAX}); first 12 occurrences:")
        for x in sorted(h, key=lambda t: t[1])[:12]:
            print("   ", x)


if __name__ == "__main__":
    main()
