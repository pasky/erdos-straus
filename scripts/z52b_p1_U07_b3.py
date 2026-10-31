#!/usr/bin/env python3
"""U07 Z1171: Hessian of z(x,y)=p x y/(4xy-p(x+y)) at the integer (x,y) of real ES solutions (p=409, 1009); sign of det
(z is the third denominator, so (x,y) with 4xy>p(x+y) are the admissible region). Capped: p<=1009, one prime each."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
import math
from fractions import Fraction as F
from sympy import symbols, hessian, lambdify, divisors
x, y = symbols('x y')
def sols(p):
    res = []
    for xx in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * xx - p, p * xx
        if num <= 0: continue
        g = math.gcd(num, den); a, b = num // g, den // g
        for d in divisors(b * b):
            if (b + d) % a: continue
            yy = (b + d) // a
            if yy < xx: continue
            e = b * b // d
            if (b + e) % a: continue
            zz = (b + e) // a
            if zz >= yy: res.append((xx, yy, zz))
    return res
for p in [409, 1009]:
    p_ = p
    z = p_*x*y/(4*x*y - p_*(x+y))
    H = hessian(z, (x, y))
    f = lambdify((x, y), H.det(), 'math')
    for (a, b, c) in sols(p)[:4]:
        # the (x,y) pair of the solution; z(x,y) reproduces c only for the solution's own third term
        print("p", p, "sol", (a, b, c), "det Hess at (x,y)=(a,b):", round(f(a, b), 6), " z(a,b)=", round(z.subs({x: a, y: b}).evalf(), 3))
