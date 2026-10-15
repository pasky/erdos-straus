"""O234 §4: the certifying prime of Thm 4.2(a) (k = 1, s = 3).  For primes p ≡ 1 (mod 4), p ≤ N: least prime
r ≡ 11 (mod 12) with (p/r) = −1 and <3> ⊇ (F_r^*)^2 (i.e. ord_r(3) ∈ {(r−1)/2, r−1}); then 9^a ≡ −p/4 (mod r)
for some a < (r−1)/2 and the shot Q = 3^a gives an ES^{(y, a−1)} solution (verified exactly for a sample).
Reports max r, max r/log(p)^2, and the adversarial family p ≡ 1 (mod 8·∏_{3≤q≤R} q).
usage: z10_grh_r.py N R"""
import sys, math, random
from fractions import Fraction as Fr
from sympy import primerange, isprime, n_order, factorint, legendre_symbol, nextprime
N, Rad = int(sys.argv[1]), int(sys.argv[2])
rs = [r for r in primerange(11, 200000) if r % 12 == 11 and n_order(3, r) >= (r - 1) // 2]
def least_r(p):
    for r in rs:
        if r != p and legendre_symbol(p % r, r) == -1: return r
def verify(p, r):
    t = (-p * pow(4, -1, r)) % r; a = 0; v = 1
    while v != t: v = v * 9 % r; a += 1
    Q = 3 ** a; assert (p + 4 * Q * Q) % r == 0
    m = (p + 4 * Q * Q) // r; x = Fr(p + m, 4); y = Fr(p * (r + 1), 4); z = p * x * (r + 1) / (4 * Q * Q)
    assert x.denominator == 1 and Fr(4, p) == 1 / x + 1 / y + 1 / z
    d = z.denominator; q = math.isqrt(d); assert q * q == d and all(s == 3 for s in factorint(q))
    return a, (factorint(q).get(3, 0))
worst = (0, 0); mr = 0; ver = 0
for p in primerange(5, N):
    if p % 4 != 1: continue
    r = least_r(p); mr = max(mr, r)
    ratio = r / math.log(p) ** 2
    if ratio > worst[0]: worst = (ratio, p, r)
    if random.random() < 0.01: verify(p, r); ver += 1
print(f"N={N}: max least r = {mr}; max r/log^2 p = {worst[0]:.2f} at p={worst[1]} (r={worst[2]}); {ver} solutions verified")
W = 8
for q in primerange(3, Rad + 1): W *= q
cnt = 0; k = 1
while cnt < 5:
    p = W * k + 1; k += 1
    if not isprime(p): continue
    r = least_r(p); a, ov = verify(p, r); cnt += 1
    print(f"adversarial p=W*{k-1}+1 (log p={math.log(p):.1f}): least r={r}, r/log^2 p={r/math.log(p)**2:.2f}, overflow exponent {ov}")
