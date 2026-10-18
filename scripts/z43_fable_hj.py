"""z43 (FABLE): verify the Legendre form of ES at primes p ≡ 1 (mod 4):

   ES(p)  <=>  exists r >= 1 and a divisor A of p + r with A ≡ -1 (mod r) and (A/p) = -1 (Kronecker).

Equivalently (HJ form, DEDEKIND_ES Thm 4.5 / Cor 4.6 in arithmetic clothing):
   ES(p) <=> exists A with (A/p) = -1 and (-p mod A) | (A + 1).

Also verify the 2-adic reading for odd A, r:  (A/p) = -1  <=>  A ≡ 3 (4) or r ≡ 3 (4).
Compare with brute force on 4/p = 1/x+1/y+1/z (any type).
"""
import sys
from sympy import primerange, divisors, jacobi_symbol

def kron(a, p):            # (a/p) for prime p>2, a>0 — Legendre
    return jacobi_symbol(a % p, p) if a % p else 0

def brute(p):
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        for y in range(den // num + 1, 2 * den // num + 1):
            n2 = num * y - den
            if n2 > 0 and (den * y) % n2 == 0:
                return True
    return False

def legendre_form(p, R):
    for r in range(1, R + 1):
        for A in divisors(p + r):
            if A >= 2 and (A + 1) % r == 0 and kron(A, p) == -1:
                return (r, A)
    return None

if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    R = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    bad = 0; twoadic_bad = 0; n = 0
    for p in primerange(5, P):
        if p % 4 != 1:
            continue
        n += 1
        b = brute(p)
        c = legendre_form(p, R)
        if b != (c is not None):
            bad += 1; print("mismatch", p, b, c)
        # 2-adic reading check over all odd (r, A) with A | p+r, A ≡ -1 (r), A>=2
        for r in range(1, R + 1, 2):
            for A in divisors(p + r):
                if A >= 2 and A % 2 == 1 and (A + 1) % r == 0:
                    pred = -1 if (A % 4 == 3 or r % 4 == 3) else 1
                    if pred != kron(A, p):
                        twoadic_bad += 1
    print("primes", n, "mismatches", bad, "2-adic-reading violations", twoadic_bad)
