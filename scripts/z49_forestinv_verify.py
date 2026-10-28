#!/usr/bin/env python3
"""z49 forestinv — independent numerical checks of the identities used in FOREST_INVERSE.md.

(1) HJ dictionary: for prime p, the interior words (t,u,v ≥ 2) of p correspond bijectively to q = tv−1 ∈ [1,p−1] with
    negative-CF (HJ) length exactly 3 and first digit u; length ≤ 2 ⟺ q | p+1.
(2) Barkan–Hickerson–Knuth: 12 s(q,p) = Σ(b_i − 3) + (q + q*)/p,  q q* ≡ 1 (mod p).
(3) Rademacher: for odd k, 12 k s(h,k) ≡ k + 1 − 2 (h/k) (mod 8).
(4) Σ_{0<a<p/4} (a/p) = h(−4p)/2 for primes p ≡ 1 (mod 4).
(5) Theorem E′ at n ≡ 1 (mod 8): every U-witness A has gcd(A,n)=1, A_odd > 1 and (n/A_odd) = −1; (5b) at n ≡ 1 (mod 4):
    Jacobi (A/n) = −1 with the 2-part; (5c) the witnesses with A ≤ 2 are exactly A = 2, v = 3, n ≡ 5 (mod 8).
(7) Prop 4.3 exceptions: A ≤ 10⁵ with τ(A+1) ≥ φ(A)/2.  (8) Σ_(p/4<q<p/2)(q/p) = −h(−4p)/2, Σ_(p/2<q<p)(q/p) = 0.
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
    bad = badb = 0
    for p in P:
        interior = {}
        for v in range(1, p + 3):
            for (t, u, vv) in words_at_vertex(p, v):
                if min(t, u, vv) >= 2:
                    interior[t * vv - 1] = u          # q = tv−1 (no reduction mod p), first digit should be u
        len3 = {q: hj(p, q)[0] for q in range(1, p) if len(hj(p, q)) == 3}
        if set(interior) != set(len3):
            bad += 1; print("HJ mismatch", p, sorted(set(interior) ^ set(len3))[:10])
        badb += sum(1 for q in interior if q in len3 and len3[q] != interior[q])
        # boundary: length ≤ 2 ⟺ q | p+1 (q = 1 is length 1)
        short2 = set(q for q in range(1, p) if len(hj(p, q)) <= 2)
        if short2 != set(q for q in range(1, p) if (p + 1) % q == 0): bad += 1; print("boundary mismatch", p)
    print(f"(1) HJ: interior words (t,u,v ≥ 2) ⟷ q = tv−1 ∈ [1,p−1] of length exactly 3 with first digit u: {len(P)} primes, {bad} set mismatches, {badb} first-digit mismatches; length ≤ 2 ⟺ q | p+1")
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
                if gcd(A, n) != 1 or Ao == 1 or jacobi_symbol(n, Ao) != -1 or isqrt(n) ** 2 == n:
                    bad5 += 1
    print(f"(5) U-witnesses at n ≡ 1 (8), n ≤ 4000: {tot} witnesses, {bad5} with gcd(A,n)>1 or A_odd = 1 or (n/A_odd) ≠ −1 or n square")
    # (5b) Theorem E′ in Jacobi form, both classes mod 8: (A/n) = −1 with the 2-part included
    bad5b = tot5b = 0
    for n in range(5, 2001, 4):
        for v in range(1, n + 3):
            if not inV(v, n): continue
            for (t, u, vv) in words_at_vertex(n, v):
                A = t * vv - 1; tot5b += 1
                if gcd(A, n) != 1 or jacobi_symbol(A, n) != -1: bad5b += 1
    print(f"(5b) U-witnesses at n ≡ 1 (4), n ≤ 2000: {tot5b} witnesses, {bad5b} with gcd(A,n)>1 or Jacobi (A/n) ≠ −1")
    small = set()
    for n in range(5, 2001, 4):
        for v in range(1, n + 3):
            if not inV(v, n): continue
            for (t, u, vv) in words_at_vertex(n, v):
                A = t * vv - 1
                if A <= 2: small.add((A, vv, n % 8))
    print(f"(5c) witnesses with A ∈ {{1,2}}: {sorted(small)[:5]}{'...' if len(small) > 5 else ''} (expected: only A=2, v=3, n ≡ 5 (8))")
    bad5c = any(not (A == 2 and vv == 3 and r == 5) for (A, vv, r) in small)
    bad5b += bad5c
    # (4.3) τ(A+1) ≥ φ(A)/2 exceptions
    from sympy import divisor_count, totient
    exc = [A for A in range(3, 100001) if divisor_count(A + 1) >= totient(A) / 2]
    print(f"(7) A ≤ 10⁵ with τ(A+1) ≥ φ(A)/2 (Prop 4.3 exceptions): {exc}")
    bad7 = exc != [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 20]
    # (8) two-cylinder signed sums: Σ_{p/4<q<p/2} (q/p) = −h(−4p)/2 and Σ_{p/2<q<p} (q/p) = 0
    bad8 = 0
    for p in P:
        s34 = sum(int(jacobi_symbol(q, p)) for q in range(1, p) if 4 * q > p and 2 * q < p)
        s2 = sum(int(jacobi_symbol(q, p)) for q in range(1, p) if 2 * q > p)
        if 2 * s34 != -class_number_neg4p(p) or s2 != 0: bad8 += 1
    print(f"(8) Σ_(p/4<q<p/2)(q/p) = −h(−4p)/2 and Σ_(p/2<q<p)(q/p) = 0: {len(P)} primes, {bad8} failures")
    # (6) n ≡ 5 (mod 8)
    bad6 = 0
    for n in range(5, 4001, 8):
        u = (n + 3) // 2
        if 1 * u * 3 - u - 3 != n or not inV(3, n): bad6 += 1
        x = ((n + 3) // 8)
        if F(1, 2 * x) + F(1, n * x) + F(1, 2 * n * x) != F(4, n): bad6 += 1
    print(f"(6) n ≡ 5 (8): word (1,(n+3)/2,3) and 4/n = 1/(2d)+1/(nd)+1/(2nd), d=(n+3)/8: {bad6} failures")
    total_bad = bad + badb + bad2 + bad3 + bad4 + bad5 + bad5b + bad6 + bad7 + bad8
    print("ALL CHECKS PASSED" if total_bad == 0 else f"FAILURES: {total_bad}")
    sys.exit(0 if total_bad == 0 else 1)

if __name__ == "__main__":
    main()
