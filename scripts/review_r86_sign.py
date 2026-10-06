"""R86 from-scratch: certificates (c,k,F) at the residue-one / sign points (Sec. 4.4).
A point is given by a dict of components {q: value} (default 1) and a 2-adic value w.
Class Cl(c,k,F): x = -F mod 4ck and x^2 = -4ck^2 mod F (componentwise, CRT)."""
from sympy import factorint, divisors
from math import gcd, isqrt

def sqf(c):
    s = 1
    for q, e in factorint(c).items():
        if e % 2: s *= q
    return s

def in_cl(c, k, F, comp):
    m = 4*c*k
    if gcd(F, m) != 1 or sqf(c) in (1, 2, 3, 6): return False
    for q, e in factorint(m).items():
        if (comp(q) + F) % q**e: return False
    for q, e in factorint(F).items():
        if (comp(q)**2 + 4*c*k*k) % q**e: return False
    return True

def sign_comp(r, w):
    return lambda q: w if q == 2 else (-1 if q == r else 1)

# Prop 4.6(b): r = 3 mod 8
for r in [11, 19, 43, 59, 67, 83]:
    for w in [9, 25, -7, 9 + 16*12345]:
        assert in_cl(r*(r+1)//4, 2, 2*r+1, sign_comp(r, w)), (r, w)
print("Prop 4.6(b) certificate OK for r in 11,19,43,59,67,83")
# residue-one point r=7: every non-square x7 covered by (7,3,11),(7,3,23),(14,2,15)
for x7 in [3, 5, 6]:
    comp = lambda q, x7=x7: x7 if q == 7 else 1
    hit = [t for t in [(7, 3, 11), (7, 3, 23), (14, 2, 15)] if in_cl(*t, comp)]
    print("residue-one x7 =", x7, "covered by", hit); assert hit
# small exhaustive search at the sign point x^_9, r=7 (sanity of the formulation)
H = 6000; found = []
for c in range(1, H+1):
    for k in range(1, H//c + 1):
        N = 1 + 4*c*k*k
        for F in divisors(N):
            if in_cl(c, k, F, sign_comp(7, 9)): found.append((c, k, F))
print("certificates at x^_9 with ck <=", H, ":", found)
