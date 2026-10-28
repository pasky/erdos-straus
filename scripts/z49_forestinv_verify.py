#!/usr/bin/env python3
"""z49 forestinv — independent numerical checks of the identities used in FOREST_INVERSE.md.

(1) HJ dictionary: for prime p, q ∈ [1,p−1] has negative-CF (HJ) length ≤ 3  ⟺  q = tv−1 for a word (t,u,v) of p.
(2) Barkan–Hickerson–Knuth: 12 s(q,p) = Σ(b_i − 3) + (q + q*)/p,  q q* ≡ 1 (mod p).
(3) Rademacher: for odd k, 12 k s(h,k) ≡ k + 1 − 2 (h/k) (mod 8).
(4) Σ_{0<a<p/4} (a/p) = h(−4p)/2 for primes p ≡ 1 (mod 4).
(5) Generalised Theorem E: every U-witness A at any n ≡ 1 (mod 8) has gcd(A,n)=1 and (n/A_odd) = −1.
(6) n ≡ 5 (mod 8): the word (1,(n+3)/2,3) always exists and has endpoint 3 ∈ V.
"""
import sys
from fractions import Fraction as F
from math import isqrt, gcd
from sympy import primerange, jacobi_symbol, factorint
from sympy.ntheory import qs
sys.path.insert(0, "scripts")
from z49_forestinv_words import words_at_vertex, divisors, inV, cls

def hj(p, q):
    """Negative continued fraction digits of p/q (p > q ≥ 1): p/q = b1 − 1/(b2 − 1/(...))."""
    out = []
    while q:
        b = -(-p // q)           # ceil
        out.append(b)
        p, q = q, b * q - p
    return out

def dedekind(h, k):
    s = F(0)
    for i in range(1, k):
        x = F(i, k); y = F(h * i % k, k)
        if y: s += (x - F(1, 2)) * (y - F(1, 2))
    return s

def class_number_neg4p(p):
    """h(−4p) by counting reduced forms of discriminant −4p."""
    D = -4 * p; h = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a and gcd(gcd(a, abs(b)), c) == 1:
                    if not (a == c and b < 0):
                        h += 1
        a += 1
    return h

def main():
    P = [p for p in primerange(5, 400) if p % 4 == 1]
    # (1) HJ dictionary
    bad = 0
    for p in P:
        words = set()
        for v in range(1, p + 3):
            for (t, u, vv) in words_at_vertex(p, v):
                words.add((t * vv - 1) % p)   # q = tv−1 = A* (numerator opposite u)
                words.add((t * u - 1) % p)
        short = set(q for q in range(1, p) if len(hj(p, q)) <= 3)
        if short != words - {0}:
            bad += 1; print("HJ mismatch", p, sorted(short ^ (words - {0}))[:10])
    print(f"(1) HJ length≤3 ⟺ word numerator: {len(P)} primes, {bad} mismatches")
    # (2) BHK, (3) Rademacher
    bad2 = bad3 = 0; cnt = 0
    for p in P[:25]:
        for q in range(1, p):
            s = dedekind(q, p); digs = hj(p, q); qs_ = pow(q, -1, p)
            if 12 * s != sum(b - 3 for b in digs) + F(q + qs_, p): bad2 += 1
            if (12 * p * s - (p + 1 - 2 * jacobi_symbol(q, p))) % 8 != 0: bad3 += 1
            cnt += 1
    print(f"(2) BHK 12 s(q,p) = Σ(b_i−3) + (q+q*)/p: {cnt} pairs, {bad2} failures")
    print(f"(3) Rademacher 12 p s(q,p) ≡ p+1−2(q/p) (mod 8): {bad3} failures")
    # (4) class number sum
    bad4 = 0
    for p in P:
        S = sum(int(jacobi_symbol(a, p)) for a in range(1, (p + 3) // 4) if 4 * a < p)
        if 2 * S != class_number_neg4p(p): bad4 += 1; print("h mismatch", p, S, class_number_neg4p(p))
    print(f"(4) Σ_(a<p/4)(a/p) = h(−4p)/2: {len(P)} primes, {bad4} failures")
    # (5) generalised Theorem E
    bad5 = tot = 0
    for n in range(9, 4001, 8):
        for v in range(1, n + 3):
            if not inV(v, n): continue
            for (t, u, vv) in words_at_vertex(n, v):
                A = t * vv - 1; tot += 1
                Ao = A >> ((A & -A).bit_length() - 1)
                if gcd(A, n) != 1 or (Ao > 1 and jacobi_symbol(n, Ao) != -1) or isqrt(n) ** 2 == n:
                    bad5 += 1
    print(f"(5) U-witnesses at n ≡ 1 (8), n ≤ 4000: {tot} witnesses, {bad5} with gcd(A,n)>1 or (n/A_odd) ≠ −1 or n square")
    # (5b) Theorem E′ in Jacobi form, both classes mod 8: (A/n) = −1 with the 2-part included
    bad5b = tot5b = 0
    for n in range(5, 2001, 4):
        for v in range(1, n + 3):
            if not inV(v, n): continue
            for (t, u, vv) in words_at_vertex(n, v):
                A = t * vv - 1; tot5b += 1
                if gcd(A, n) != 1 or jacobi_symbol(A, n) != -1: bad5b += 1
    print(f"(5b) U-witnesses at n ≡ 1 (4), n ≤ 2000: {tot5b} witnesses, {bad5b} with gcd(A,n)>1 or Jacobi (A/n) ≠ −1")
    # (6) n ≡ 5 (mod 8)
    bad6 = 0
    for n in range(5, 4001, 8):
        u = (n + 3) // 2
        if 1 * u * 3 - u - 3 != n or not inV(3, n): bad6 += 1
        x = ((n + 3) // 8)
        if F(1, 2 * x) + F(1, n * x) + F(1, 2 * n * x) != F(4, n): bad6 += 1
    print(f"(6) n ≡ 5 (8): word (1,(n+3)/2,3) and 4/n = 1/(2d)+1/(nd)+1/(2nd), d=(n+3)/8: {bad6} failures")

if __name__ == "__main__":
    main()
