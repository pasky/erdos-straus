#!/usr/bin/env python3
"""z56 K4TRY §4.1: identities of the polynomial family on the det-15 quadric, and Theorem Q as a line.
Checks (symbolic + numeric):
  p(m,n) = (n^2 - m^2 + 4)^2 + m^2 - 4;  p+4 = (n^2-m^2+4)^2 + m^2;  4p+1 = (2n^2-2m^2+7)^2 + 4n^2;
  quadric 4A^2+4B^2-C^2-D^2 = 15 with A = 4-m^2+n^2, B = m, C = 7-2m^2+2n^2, D = -2n; (u,v,s,t) = (1, 15-st, 2(m+n), 2(m-n));
  Theorem Q line: A = 2m-1, B = m+2, C = 4m-1, D = 2m+2 gives p = 5m^2+1 and (u,s) = (-1, 2).
  p(m,n) = 1 mod 8 iff m = 2 mod 4 and n odd (checked over residues).
  Point count: #{(m,n): 0 < p(m,n) <= x} for x = 1e6, 1e8 (thinness ~ sqrt(x) log x).
Usage: uv run --with sympy python z56_k4try_family.py
"""
import math
from sympy import symbols, expand, simplify

m, n = symbols('m n', integer=True)
A = 4 - m**2 + n**2; B = m; C = 7 - 2*m**2 + 2*n**2; D = -2*n
p = A**2 + B**2 - 4
assert expand(4*A**2 + 4*B**2 - C**2 - D**2 - 15) == 0
assert expand(p + 4 - ((n**2 - m**2 + 4)**2 + m**2)) == 0
assert expand(4*p + 1 - ((2*n**2 - 2*m**2 + 7)**2 + 4*n**2)) == 0
u, v, s, t = 2*A - C, 2*A + C, 2*B - D, 2*B + D
assert expand(u) == 1 and expand(s - 2*(m + n)) == 0 and expand(t - 2*(m - n)) == 0 and expand(u*v + s*t - 15) == 0
# Theorem Q line
AQ, BQ, CQ, DQ = 2*m - 1, m + 2, 4*m - 1, 2*m + 2
assert expand(4*AQ**2 + 4*BQ**2 - CQ**2 - DQ**2 - 15) == 0
assert expand(AQ**2 + BQ**2 - 4 - (5*m**2 + 1)) == 0
assert expand(2*AQ - CQ) == -1 and expand(2*BQ - DQ) == 2
print("symbolic identities OK")

def P(mm, nn): return (nn*nn - mm*mm + 4)**2 + mm*mm - 4
# residue check mod 8
cls = {}
for mm in range(8):
    for nn in range(8):
        cls[(mm, nn)] = P(mm, nn) % 8
ok = all((cls[(mm, nn)] == 1) == (mm % 4 == 2 and nn % 2 == 1) for mm in range(8) for nn in range(8))
print("p = 1 (mod 8) iff m = 2 (4), n odd:", ok)
# numeric S-check on small members: both shifts have no prime factor 3 mod 4 when the gcd conditions hold
def bad(x):
    q = 2; 
    while q * q <= x:
        if x % q == 0:
            if q % 4 == 3: return True
            while x % q == 0: x //= q
        q += 1
    return x % 4 == 3
cnt = 0; viol = 0
for mm in range(-50, 51):
    for nn in range(-50, 51):
        pp = P(mm, nn)
        if pp <= 1: continue
        g1 = math.gcd(4 + nn*nn, mm); g2 = math.gcd(7 - 2*mm*mm, nn)
        if bad(g1) or bad(g2): continue
        cnt += 1
        if bad(pp + 4) or bad(4*pp + 1): viol += 1
print(f"members |m|,|n|<=50 with clean gcds: {cnt}; shifts with a Q-factor: {viol}")
for x in (10**6, 10**8):
    c = 0
    M = int(math.isqrt(x)) + 3
    for mm in range(0, M + 1):
        for nn in range(0, M + 1):
            if 0 < P(mm, nn) <= x: c += 1
    print(f"x={x}: #(m,n)>=0 with 0<p<=x: {c}   sqrt(x)log(x)={math.sqrt(x)*math.log(x):.0f}")
