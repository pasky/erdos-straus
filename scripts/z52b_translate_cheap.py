"""Cheap tests for lane translate (z52b). Memory-light, bounded loops.
(a) altitude variant: ES solution with p/2 < x <= 3p/4 for primes p ≡ 1 (4) <= P_A.
(b) quartic symbol of A over ES5 words with (A/p) = -1, p ≡ 1 (8) <= P_B.
(c) mean HJ length over QR vs QNR a, p ≡ 1 (4) <= P_C.
(d) Montesinos rung beta_i in {1,2}: 4/p = e1/x + e2/y + e3/z, at least one e_i = 2, for primes p ≡ 1 (4) <= P_D that FAIL the altitude variant (just to see).
"""
import sys
from sympy import primerange, divisors, legendre_symbol
P_A, P_B, P_C = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def two_term(a, b, ymin=0):
    """is a/b = 1/y + 1/z (y<=z positive ints)?  (ay-b)(az-b)=b^2 with ay-b>0: need divisor d of b^2, d<=b, d ≡ -b mod a."""
    from math import gcd
    g = gcd(a, b); a //= g; b //= g
    for d in divisors(b * b):
        if d > b: break
        if (d + b) % a == 0 and (d + b) // a >= ymin:
            return True
    return False

# (a)
fails_alt = []
for p in primerange(5, P_A):
    if p % 4 != 1: continue
    ok = False
    for x in range(p // 2 + 1, 3 * p // 4 + 1):
        if two_term(4 * x - p, p * x, ymin=x):  # x is the smallest denominator (review fix)
            ok = True; break
    if not ok: fails_alt.append(p)
print('(a) primes p≡1(4) <', P_A, 'with no ES solution having p/2 < x <= 3p/4:', len(fails_alt), fails_alt[:40])

# (b) words t,u,v>=2, tuv-u-v=p, A=tu-1
def words(p):
    for t in range(2, p):
        if 4 * t - 2 > p + 4: pass
        u = 2
        while t * u * 2 - u - 2 <= p:
            # need v = (p+u)/(tu-1) integer >= 2
            A = t * u - 1
            if (p + u) % A == 0:
                v = (p + u) // A
                if v >= 2: yield t, u, v, A
            u += 1
        if t * 4 - 4 > p: break
from collections import Counter
qc = Counter()
for p in primerange(17, P_B):
    if p % 8 != 1: continue
    for t, u, v, A in words(p):
        if legendre_symbol(A % p, p) == -1:
            e = pow(A, (p - 1) // 4, p)
            qc['-i_or_i' if e not in (1, p - 1) else ('1' if e == 1 else '-1')] += 1
print('(b) quartic residue values pow(A,(p-1)/4) over sign(-1) ES5 words, p≡1(8) <', P_B, dict(qc))

# (c) HJ length
def hj_len(p, a):
    r = 0
    while a:
        b = -(-p // a)
        p, a = a, b * a - p
        r += 1
    return r
import statistics
diffs = []
for p in primerange(5, P_C):
    if p % 4 != 1: continue
    qr = []; qn = []
    for a in range(1, p):
        (qr if legendre_symbol(a, p) == 1 else qn).append(hj_len(p, a))
    diffs.append((p, statistics.mean(qr) - statistics.mean(qn)))
print('(c) mean HJ length QR minus QNR, sample:', [(p, round(d, 3)) for p, d in diffs[-8:]],
      'overall mean diff', round(statistics.mean(d for _, d in diffs), 4))
