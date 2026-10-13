"""ES-forms of discriminant -4n (O164 §2-3).

ES-form: [a, B, c], B^2 - 4ac = -4n, B>0, 4|B, B | a+1  (Cor 2.2).
For each odd n in a list, report:
  red   = # reduced forms (|B|<=a<=c) that are ES-forms
  any_a = smallest a carrying an ES-form (search a <= AMAX), or 0
Usage: python wr_esforms.py MODE NMAX [AMAX]
  MODE=primes : p = 1 mod 24 primes up to NMAX ;  MODE=squares : odd m^2 <= NMAX
"""
import sys
from math import isqrt, gcd


def sqrt_mod_all(r, a):
    """all beta in [0,a) with beta^2 = r mod a (brute for small a)."""
    return [x for x in range(a) if (x * x - r) % a == 0]


def reduced_forms(n):
    D = 4 * n
    out = []
    for a in range(1, isqrt(D // 3) + 2):
        for B in range(-a + 1, a + 1):
            if (B * B + D) % (4 * a):
                continue
            c = (B * B + D) // (4 * a)
            if c < a or (c == a and B < 0):
                continue
            out.append((a, B, c))
    return out


def is_es(f):
    a, B, c = f
    return B > 0 and B % 4 == 0 and (a + 1) % B == 0


def first_es_a(n, amax):
    """exhaustive: b <= (n+1)/3 (forced by e | n+4b^2, 4b | n+e, k=(n+4b^2)/e >= 4b-1);
    returns (b, e) with smallest b, or (0,0)."""
    from sympy import divisors
    for b in range(1, (n + 1) // 3 + 1):
        for e in divisors(n + 4 * b * b):
            if (n + e) % (4 * b) == 0:
                return b, e
    return 0, 0


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    mode, nmax = sys.argv[1], int(sys.argv[2])
    amax = 0
    if mode == "primes":
        ns = [p for p in range(25, nmax + 1, 24) if isprime(p)]
    elif mode == "list":
        ns = [int(x) for x in sys.argv[3].split(",")]
        amax = 0
    else:
        ns = [m * m for m in range(3, isqrt(nmax) + 1, 2)]
    nored = 0
    noany = []
    for n in ns:
        R = reduced_forms(n)
        r = sum(is_es(f) for f in R)
        nored += (r == 0)
        a, beta = first_es_a(n, amax)
        if a == 0:
            noany.append(n)
    print(mode, "count", len(ns), "no reduced ES-form:", nored,
          "no ES-form at all (exhaustive b<=(n+1)/3):", len(noany), noany[:12])


if __name__ == "__main__":
    main()
