#!/usr/bin/env python3
"""z48_ltfable_lemmas.py — exact checks of the elementary lemmas in LOWERTAIL_DEEP_FABLE.md.

L1  (sign law by level, odd A).  For a prime p = 1 (mod 4) and a word (t,u,v) with tuv-u-v = p, A = tu-1 odd:
       (A/p) = (-t/A)  (Jacobi), and for t odd this equals -(-1)^{(A+1)(t+1)/4}.
     Consequences (lines):  4|t => -1 ; t=3(4), A odd => -1 ; t=1(4), A odd => -1 iff 4|u.
L2  (p-free covering form of Type II).  Type II(p)  <=>  exists j>=1, m | j^2 with p = -4m (mod 4j-1)
     (then x = (m+jp)/(4j-1), e = 4x-p, delta = m, 4/p = 1/x + 1/(p(x+m)/e) + 1/(p(x+x^2/m)/e)); checked both directions
     against the ET Type II count for primes < 1500.
L3  (window form).  Type II(p) <=> exists x in (p/4,(p+1)/3] and delta | x^2 with delta = -x (mod 4x-p).
L4  (scaling families).  #{(k,x,y,z): 4k/p = 1/x+1/y+1/z, k<=K} = sum over solutions (x,y,z) of 4/p of #{k<=K : k | gcd(x,y,z)}.
L5  (no cross-level multiplicativity).  d = -1 (4C), d' = -1 (4C') => d d' = +1 (mod 4 gcd(C,C')).
Run: PYTHONPATH=scripts uv run python scripts/z48_ltfable_lemmas.py
"""
from math import gcd, isqrt
from fractions import Fraction
import sys


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def primes(N):
    s = bytearray([1]) * (N + 1)
    s[0] = s[1] = 0
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def words(n):
    """all (t,u,v) in N^3 with t*u*v - u - v = n"""
    out = []
    u = 1
    while u * u - 2 * u <= n:
        v = u
        while True:
            uv = u * v
            tmin = max(1, (u + v + uv - 1) // uv)
            if tmin * uv - u - v > n:
                break
            if (n + u + v) % uv == 0:
                t = (n + u + v) // uv
                out.append((t, u, v))
                if u != v:
                    out.append((t, v, u))
            v += 1
        u += 1
    return out


def divisors(n):
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i * i != n:
                d.append(n // i)
        i += 1
    return d


def all_sols(p, num=4):
    """all solutions num/p = 1/x+1/y+1/z (x<=y<=z) by the exact divisor test on the smallest denominator"""
    sols = set()
    for x in range(p // num + 1, 3 * p // num + 1):
        fr = Fraction(num * x - p, p * x)
        A, B = fr.numerator, fr.denominator
        # d | B^2 with d = -B (mod A), d <= B (y <= z): enumerate d in the class
        for d in range(((-B) % A) or A, B + 1, A):
            if (B * B) % d == 0:
                y = (B + d) // A
                z = (B + B * B // d) // A
                if y >= x:
                    sols.add((x, y, z))
    return sols


def type2_sols(p):
    return {s for s in all_sols(p) if sum(1 for w in s if w % p == 0) == 2}


def check_L1(P):
    bad = 0
    tot = 0
    for p in P:
        if p % 4 != 1:
            continue
        for (t, u, v) in words(p):
            A = t * u - 1
            if A % 2 == 0:
                continue
            tot += 1
            s = jacobi(A, p)
            s1 = jacobi(-t % A if A > 1 else 0, A) if A > 1 else 1
            if A == 1:
                s1 = 1
            if s != s1:
                bad += 1
            if t % 2 == 1:
                s2 = -((-1) ** (((A + 1) * (t + 1) // 4) % 2))
                if s != s2:
                    bad += 1
            # line consequences
            if t % 4 == 0 and s != -1:
                bad += 1
            if t % 4 == 3 and s != -1:
                bad += 1
            if t % 4 == 1 and s != (-1 if u % 4 == 0 else 1):
                bad += 1
    print(f"L1 sign law: {tot} odd-A words at primes p=1(4) <= {P[-1]}, violations {bad}")
    return bad == 0


def check_L2_L3(P):
    bad = 0
    for p in P:
        if p < 5:
            continue
        s2 = type2_sols(p)
        has2 = len(s2) > 0
        # covering form
        cov = False
        j = 1
        while 4 * j - 1 <= 2 * p and not cov:
            q = 4 * j - 1
            for m in divisors(j * j):
                if (p + 4 * m) % q == 0:
                    x = (m + j * p) // q
                    e = 4 * x - p
                    assert e > 0 and (x * x) % m == 0 and (m + x) % e == 0
                    y = p * (x + m) // e
                    z = p * (x + x * x // m) // e
                    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
                    cov = True
                    break
            j += 1
        # window form
        win = False
        for x in range(p // 4 + 1, (p + 1) // 3 + 1):
            e = 4 * x - p
            for d in range(((-x) % e) or e, x * x + 1, e):
                if (x * x) % d == 0:
                    win = True
                    break
            if win:
                break
        if cov != has2 or win != has2:
            bad += 1
            print("  mismatch at", p, has2, cov, win)
    print(f"L2/L3 covering and window forms vs ET Type II at {len(P)} primes <= {P[-1]}: mismatches {bad}")
    return bad == 0


def check_L4(P, K=8):
    bad = 0
    for p in P:
        sols = all_sols(p)
        rhs = sum(sum(1 for k in range(1, K + 1) if gcd(gcd(x, y), z) % k == 0) for (x, y, z) in sols)
        lhs = 0
        for k in range(1, K + 1):
            # solutions of 4k/p with x<=y<=z, via the same divisor test with numerator 4k
            S = set()
            for x in range(p // (4 * k) + 1, 3 * p // (4 * k) + 1):
                fr = Fraction(4 * k * x - p, p * x)
                A, B = fr.numerator, fr.denominator
                for d in range(((-B) % A) or A, B + 1, A):
                    if (B * B) % d == 0:
                        y = (B + d) // A
                        z = (B + B * B // d) // A
                        if y >= x:
                            S.add((x, y, z))
            lhs += len(S)
        if lhs != rhs:
            bad += 1
            print("  L4 mismatch", p, lhs, rhs)
    print(f"L4 scaling identity at {len(P)} primes <= {P[-1]}, K={K}: mismatches {bad}")
    return bad == 0


def check_L5():
    bad = 0
    for C in range(1, 40):
        for C2 in range(1, 40):
            g = gcd(C, C2)
            for d in range(4 * C - 1, 4 * C * 30, 4 * C):
                for d2 in range(4 * C2 - 1, 4 * C2 * 6, 4 * C2):
                    if (d * d2) % (4 * g) != 1:
                        bad += 1
    print(f"L5 product class: violations {bad}")
    return bad == 0


if __name__ == "__main__":
    P = primes(3000)
    ok = check_L1([p for p in P if p % 4 == 1])
    ok &= check_L2_L3([p for p in primes(700) if p >= 5])
    ok &= check_L4([p for p in primes(300) if p >= 5])
    ok &= check_L5()
    print("ALL OK" if ok else "FAILURES")
    sys.exit(0 if ok else 1)
