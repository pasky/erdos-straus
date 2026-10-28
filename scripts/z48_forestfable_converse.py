#!/usr/bin/env python3
"""z48 forestfable — Theorem A certificate.

For a prime p ≡ 1 (mod 4) and an edge {u,v} (u<v) of the forest F_p
(uv | p+u+v, t=(p+u+v)/(uv)) the edge colour (uv/p) is, by quadratic
reciprocity alone (no Dedekind sums, no Rademacher congruence), the function

    S(u,v,p) = (2/p)^{a+b} (2/u')^b (2/v')^a eps(u',v')
    u = 2^a u', v = 2^b v', eps(x,y) = (-1)^{(x-1)/2+(y-1)/2+(x-1)(y-1)/4},

which depends only on (u, v, p) mod 8 (with the convention that for a>=3 the
factor (2/p)^a(2/v')^a is 1, which is forced by p ≡ -v (mod 8)).  This script

 (1) enumerates every (t,u,v) in (Z/8)^3 with p := tuv-u-v ≡ 1 (mod 4) and
     gcd-admissible parity (not both u,v even), evaluates S from the residues
     and compares with the five-slot predicate
        4 | t  or 4 | u or 4 | v or 4 | tu-1 or 4 | tv-1 ;
 (2) brute-forces every edge of F_p for all primes p ≡ 1 (4), p < LIMIT,
     computing the Legendre symbol by Euler's criterion (independent of (1))
     and compares with the slot predicate;
 (3) prints the monochromatic cells in the (u mod 8, v mod 8, t mod 4)
     coordinates used in Theorem B.
"""
import sys
from math import gcd, isqrt


def jac2(m):
    """(2/m) for odd m."""
    return 1 if m % 8 in (1, 7) else -1


def eps(x, y):
    return (-1) ** (((x - 1) // 2 + (y - 1) // 2 + ((x - 1) // 2) * ((y - 1) // 2)) % 2)


def S_from_residues(u8, v8, p8):
    """Reciprocity formula for (uv/p) from residues mod 8 (p ≡ 1 mod 4).
    For an endpoint ≡ 0 (mod 8) the a>=3 convention is used."""
    def split(x8):
        if x8 % 2:
            return 0, x8
        if x8 % 4:
            return 1, (x8 // 2) % 8
        if x8 % 8:
            return 2, (x8 // 4) % 8  # x' = odd part mod 2 only; see below
        return 3, None
    a, up = split(u8)
    b, vp = split(v8)
    assert not (a and b), "two even endpoints cannot be coprime"
    # odd parts mod 8: for a=1, u' = u/2 mod 4 only is determined by u mod 8,
    # which is all eps needs (eps depends on residues mod 4) and (2/u')^b with
    # b=0 is not needed.  For a=2, u'=u/4 mod 2 only: eps needs u' mod 4 -- but
    # then 4|u is a slot and the value is forced to -1 (Case 2 of the proof),
    # which we check separately.  So return None for the forced cases.
    if a >= 2 or b >= 2:
        return None
    if a == 0 and b == 0:
        return eps(u8, v8)
    if a == 1:  # u = 2u', v odd
        return jac2(p8) * jac2(v8) * eps(up, v8)
    # b == 1
    return jac2(p8) * jac2(u8) * eps(u8, vp)


def slot(t, u, v):
    return t % 4 == 0 or u % 4 == 0 or v % 4 == 0 or (t * u - 1) % 4 == 0 or (t * v - 1) % 4 == 0


def part1():
    mism = 0
    cells = 0
    mono = set()
    for t in range(8):
        for u in range(8):
            for v in range(8):
                if u % 2 == 0 and v % 2 == 0:
                    continue
                p8 = (t * u * v - u - v) % 8
                if p8 % 4 != 1:
                    continue
                cells += 1
                s = S_from_residues(u, v, p8)
                sl = slot(t, u, v)
                if s is None:
                    # 4 | u or 4 | v: Case 2 of the proof gives -1; slot holds
                    assert sl
                    continue
                if (s == -1) != sl:
                    mism += 1
                    print("MISMATCH cell", t, u, v, p8, s, sl)
                if s == +1:
                    mono.add((u, v, t % 4, p8))
    print(f"part1: admissible cells mod 8: {cells}, mismatches: {mism}")
    print("monochromatic cells (u mod 8, v mod 8, t mod 4, p mod 8):")
    for c in sorted(mono):
        print("  ", c)
    return mism


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def edges(p):
    """All edges {u,v}, u<v, of F_p by the smaller endpoint."""
    out = []
    umax = isqrt(p + 1) + 1
    for u in range(1, umax + 1):
        n = p + u
        r = (-p) % u
        # divisors v of n with v ≡ r (mod u), v > u
        d = 1
        divs = []
        while d * d <= n:
            if n % d == 0:
                divs.append(d)
                if d * d != n:
                    divs.append(n // d)
            d += 1
        for v in divs:
            if v > u and v % u == r and (p + u + v) % (u * v) == 0:
                out.append((u, v))
    return out


def part2(limit):
    bad = 0
    tot = 0
    for p in primes_upto(limit):
        if p % 4 != 1:
            continue
        for u, v in edges(p):
            t = (p + u + v) // (u * v)
            bi = legendre(u, p) * legendre(v, p) == -1
            if bi != slot(t, u, v):
                bad += 1
                print("MISMATCH edge", p, u, v, t)
            tot += 1
    print(f"part2: primes p ≡ 1 (4) below {limit}: {tot} edges, mismatches {bad}")
    return bad


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    m1 = part1()
    m2 = part2(limit)
    print("OK" if m1 == 0 and m2 == 0 else "FAIL")
