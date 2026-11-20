#!/usr/bin/env python3
"""z74 Opus cross-review (lane PIDEXT): independent finite sanity checks.

None of these is load-bearing for the PROVED claims (all are algebraic); they
recompute the finite inputs quoted in the PIDEXT notes.

A. LOGIC_PRESCRIBED_FIELD_AT_P: for q = 3 (4) and p = -4 (q), c=(q+1)/4,
   b=(1+pc)/q are integers and 4/p = 1/(pbc) + 1/(pc) + 1/b.  Also exhibit,
   for j <= 7, primes p_j > 2^j with p_j = 1 mod j! and p_j = -4 mod q_j.
B. LOGIC_PID_TAG_AUDIT item 4: p = 4k-1 gives 4/p = 1/k + 2/(2kp).
C. LOGIC_RESIDUE_PRESCRIPTION_COMMENT "Separation": x^3 + t y^3 + t^2 z^3 = 0
   has a nontrivial solution over F_p for every t != 0 (p != 3); and a
   Z-valued valuation with v(t)=1 cannot allow one (term valuations 0,1,2 mod 3).
D. LOGIC_PID_DIRICHLET_AUDIT NR check / TAG_AUDIT kill test 1: for odd t and
   standard d = 3 (4) with gcd(d,t)=1, d never divides x^2 + t^2.
E. LOGIC_PID_INTERVAL_AUDIT item 2: the marked-cylinder fraction
   ((l-1)/2)^k l^(d-k) / l^d >= 3^-k, exact count by enumeration.
F. LOGIC_PID_INTERVAL_AUDIT boundary: (b+1)!+2 .. (b+1)!+b+1 composite,
   also after adding m*(b+1)! (gap beyond any bound).

Usage: python z74_xrev_pidext_checks.py [PMAX_A=20000] [PMAX_C=97] [DMAX_D=1500]
"""
import sys
from fractions import Fraction
from math import factorial, gcd, isqrt
from itertools import product


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def check_A(pmax):
    ps = primes_upto(pmax)
    qs = [q for q in ps if q % 4 == 3 and q < 400]
    n = 0
    for q in qs:
        for p in ps:
            if p == q or p % q != (-4) % q:
                continue
            c = (q + 1) // 4
            assert (q + 1) % 4 == 0 and (1 + p * c) % q == 0
            b = (1 + p * c) // q
            assert 4 * b * c == 1 + b + p * c
            assert Fraction(4, p) == Fraction(1, p * b * c) + Fraction(1, p * c) + Fraction(1, b)
            n += 1
    print(f"A. identity 4/p=1/(pbc)+1/(pc)+1/b verified for {n} pairs (q<400, p<={pmax}, p=-4 mod q)")
    for j in range(1, 8):
        M = factorial(j)
        q = next(q for q in primes_upto(1000) if q % 4 == 3 and M % q != 0)
        # CRT: p = 1 mod M, p = -4 mod q
        x = 1
        while x % q != (-4) % q:
            x += M
        p = x
        while not (p > 2 ** j and is_prime(p)):
            p += M * q
        c = (q + 1) // 4
        b = (1 + p * c) // q
        assert Fraction(4, p) == Fraction(1, p * b * c) + Fraction(1, p * c) + Fraction(1, b)
        print(f"   j={j}: q_j={q}, p_j={p} (=1 mod {M}, =-4 mod {q}); 4/p = 1/{p*b*c} + 1/{p*c} + 1/{b}")


def check_B(pmax):
    n = 0
    for p in primes_upto(pmax):
        if p % 4 == 3:
            k = (p + 1) // 4
            assert Fraction(4, p) == Fraction(1, k) + Fraction(2, 2 * k * p)
            n += 1
    print(f"B. 4/p = 1/k + 2/(2kp) verified at all {n} primes p=3 mod 4 up to {pmax}")


def check_C(pmax):
    worst = None
    for p in primes_upto(pmax):
        if p == 3:
            continue
        cubes = {}
        for z in range(p):
            cubes.setdefault(pow(z, 3, p), []).append(z)
        for t in range(1, p):
            t2inv = pow(t * t % p, p - 2, p)
            cnt = 0  # affine solutions (x,y,z) incl. 0, count projective later
            for x in range(p):
                x3 = x * x * x % p
                for y in range(p):
                    r = (-(x3 + t * pow(y, 3, p)) * t2inv) % p
                    cnt += len(cubes.get(r, ()))
            proj = (cnt - 1) // (p - 1)
            assert proj >= 1, (p, t)
            if worst is None or proj - (p + 1) < worst[0]:
                worst = (proj - (p + 1), p, t, proj)
            assert abs(proj - (p + 1)) <= 2 * isqrt(p) + 2, (p, t, proj)  # Hasse
    print(f"C. x^3+ty^3+t^2z^3=0 has a projective F_p-point for all t!=0, 2<=p<={pmax}, p!=3;"
          f" worst deficit vs p+1: {worst[0]} at p={worst[1]}, t={worst[2]} ({worst[3]} points); Hasse bound respected")
    # valuation incompatibility: v(x^3), v(t y^3), v(t^2 z^3) are 0,1,2 mod 3 -> distinct
    for vx, vy, vz in product(range(6), repeat=3):
        vals = {3 * vx % 3, (1 + 3 * vy) % 3, (2 + 3 * vz) % 3}
        assert len(vals) == 3
    print("   term valuations 3v(x), 1+3v(y), 2+3v(z) are pairwise distinct mod 3 (no cancellation)")


def check_D(dmax, tmax=301):
    n = 0
    for d in range(3, dmax + 1, 4):
        sq = {x * x % d for x in range(d)}
        for t in range(1, tmax + 1, 2):
            if gcd(d, t) == 1:
                assert (-t * t) % d not in sq, (d, t)
                n += 1
    print(f"D. no d=3 mod 4 (d<={dmax}) coprime to odd t (t<={tmax}) divides x^2+t^2: {n} pairs checked")


def check_E():
    for l in (3, 5, 7, 11, 13):
        sqs = {x * x % l for x in range(1, l)}
        for dd in range(1, 4):
            for k in range(0, dd + 1):
                cnt = sum(1 for tup in product(range(l), repeat=dd) if all(tup[i] in sqs for i in range(k)))
                assert cnt == ((l - 1) // 2) ** k * l ** (dd - k)
                assert Fraction(cnt, l ** dd) >= Fraction(1, 3 ** k)
    print("E. marked-cylinder counts ((l-1)/2)^k l^(d-k) and the 3^-k lower bound verified (l<=13, d<=3)")


def check_F():
    for b in range(1, 13):
        F = factorial(b + 1)
        for m in (1, 7, 10 ** 6 + 3):
            a = m * F + 1
            for j in range(1, b + 1):
                n = a + j
                assert n % (j + 1) == 0 and n > j + 1
    print("F. (a, a+b) with a = m(b+1)!+1 contains only composites (b<=12, m in {1,7,10^6+3})")


if __name__ == "__main__":
    pa = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    pc = int(sys.argv[2]) if len(sys.argv) > 2 else 97
    dd = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
    check_A(pa)
    check_B(10 ** 5)
    check_C(pc)
    check_D(dd)
    check_E()
    check_F()
    print("ALL CHECKS PASSED")
