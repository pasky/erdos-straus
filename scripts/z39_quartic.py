"""z39: is there a quartic analogue of the ES sign on the k | t slices (k = 8, 16)?
For primes n = p ≡ 1 (mod 8) and words (t,u,v) of p with k | t (A = tu - 1 is then a QNR mod p, QUESTION_R Prop 1.4
/ DEDEKIND Thm 4.5 for 4 | t), compute the quartic character A^{(p-1)/4} mod p in {i, -i} relative to a canonical
square root of -1 (i := a/b mod p, p = a^2 + b^2, a odd, b even, a,b > 0) -- canonical up to nothing (fixed choice).
Report, per prime, the multiset of quartic values on the slice; a quartic T1 would make it constant (or a function
of p mod small modulus).  usage: python z39_quartic.py PMAX k
"""
import sys
from sympy import primerange
from math import isqrt

PMAX = int(sys.argv[1]); k = int(sys.argv[2])


def two_squares(p):
    for b in range(2, isqrt(p) + 1, 2):
        a2 = p - b * b
        a = isqrt(a2)
        if a * a == a2:
            return a, b
    return None


const = mixed = empty = 0
pattern = {}
for p in primerange(17, PMAX):
    if p % 8 != 1:
        continue
    a, b = two_squares(p)
    I = a * pow(b, -1, p) % p
    vals = set(); cnt = [0, 0]
    for t in range(k, (p + 4) // 4 + 1, k):
        N = t * p + 1
        # divisors d = tu - 1 with u >= 2, cofactor tv - 1, v >= 2
        d = 2 * t - 1
        while d * d <= N:
            if N % d == 0 and (N // d) % t == t - 1:
                for A in (d,):  # smaller divisor only (A <-> A* conjugates the quartic value)
                    q = pow(A, (p - 1) // 4, p)
                    cnt[q == I] += 1; vals.add('i' if q == I else ('-i' if q == p - I else ('+1' if q == 1 else '-1')))
            d += t
    if not vals:
        empty += 1
    elif len(vals) == 1:
        const += 1
        key = (p % 16, p % 5, tuple(sorted(vals)))
        pattern[key] = pattern.get(key, 0) + 1
    else:
        mixed += 1
print("k=%d primes p=1(8) < %d: empty slice %d, constant quartic value %d, mixed %d" % (k, PMAX, empty, const, mixed))
tot_i = sum(v for kk, v in pattern.items() if kk[2] == ('i',)); print('constant=i:', tot_i)
print("constant cases by (p mod 16, p mod 5, value):", sorted(pattern.items())[:20])
