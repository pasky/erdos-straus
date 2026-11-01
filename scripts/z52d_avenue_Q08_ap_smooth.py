"""z52d avenue Q08 checks (timeout 60).
(1) Z0119: 4/n = 1/x + 1/(x+d) + 1/(x+2d), d >= 1, has no solution unless 4 | n
    (2-adic proof in out_Q08 note); brute force n < 2000.
(2) Z3089: smooth-divisor certificates vanish at square-mimicking primes: if p = m^2 (mod Q),
    every divisor d | Q of 4Cp+1 divides 4Cm^2+1, so by T1 d is not = -1 (mod 4C).
(3) Z3066/Z2949/Z2970: Legendre profile of the 14 (*)-failures <= 1e10.
"""
from fractions import Fraction as F
import math, random

def ap_solutions(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        r = F(4, n) - F(1, x)
        if r <= 0: continue
        a, b, c = 2 * r, 3 * r * x - 3, r * x * x - 2 * x
        D = b * b - 4 * a * c
        if D < 0: continue
        sn, sd = math.isqrt(D.numerator), math.isqrt(D.denominator)
        if sn * sn != D.numerator or sd * sd != D.denominator: continue
        s = F(sn, sd)
        for dd in ((-b + s) / (2 * a), (-b - s) / (2 * a)):
            if dd.denominator == 1 and dd >= 1: out.append((x, int(dd)))
    return out

bad = [n for n in range(2, 2000) if ap_solutions(n) and n % 4]
print("(1) n<2000 with AP solution and 4 ∤ n:", bad)

def isprime(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

PE = {2: 6, 3: 3, 5: 2, 7: 2, 11: 1, 13: 1}
Q = 1
for q, e in PE.items(): Q *= q ** e
def divisors_in_Q(N):
    ds = [1]
    for q, e in PE.items():
        k = 0
        while k < e and N % q ** (k + 1) == 0: k += 1
        ds = [d * q ** j for d in ds for j in range(k + 1)]
    return ds
random.seed(1); hits = 0; tested = 0
for m in range(1, 400, 2):
    if math.gcd(m, Q) != 1: continue
    for k in range(1, 50):
        p = m * m + k * Q
        if not isprime(p): continue
        tested += 1
        for C in range(1, 41):
            N = 4 * C * p + 1
            if any(d % (4 * C) == 4 * C - 1 for d in divisors_in_Q(N)): hits += 1
        break
print(f"(2) primes p = m^2 (mod Q={Q}) tested: {tested}; Q-smooth certificates at C<=40: {hits}")

Z = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
leg = lambda a, p: (lambda r: 0 if r == 0 else (1 if r == 1 else -1))(pow(a % p, (p - 1) // 2, p))
P = [q for q in range(3, 200) if all(q % r for r in range(2, int(q ** .5) + 1))]
for p in Z:
    print("(3)", p, "mod840", p % 840, "lnr", next(q for q in P if leg(q, p) == -1),
          "(p/l) l=11,13,17,19,23:", [leg(p, l) for l in (11, 13, 17, 19, 23)])
print("(3) pairs p<p'<p^2 among (*)-failures:", sum(1 for i, a in enumerate(Z) for b in Z[i + 1:] if b < a * a))

# (4) Z0705: in every solution of 4/p = 1/x+1/y+1/z (p prime) the largest denominator is divisible by p.
viol = 0; nsol = 0
for p in [q for q in range(5, 250) if all(q % r for r in range(2, int(q ** .5) + 1))]:
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = F(4, p) - F(1, x)                      # = 1/y + 1/z, x <= y <= z
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            s = r - F(1, y)
            if s > 0 and s.numerator == 1:
                z = s.denominator; nsol += 1
                if z % p: viol += 1
print(f"(4) solutions x<=y<=z for primes 5<=p<250: {nsol}; with p ∤ z: {viol}")
