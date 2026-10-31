#!/usr/bin/env python3
"""U07 Z2853: for ES solutions (x,y,z) of primes p<=300 (from the solution enumeration), weights (a,b,c)=(L/x,L/y,L/z),
L=lcm(x,y,z): compute (a+b+c)/lcm(a,b,c) and check whether it is an integer. Z2877: area argument for index-d inclusions of
ES-type triangle groups: 1−4/n' = d(1−4/n) has a solution only for n < 4d/(d−1) (scan d ≤ 50, n ≤ 10^4)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
import math
from fractions import Fraction as F
from sympy import primerange, divisors
def sols(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        num, den = 4 * x - p, p * x
        if num <= 0: continue
        g = math.gcd(num, den); a, b = num // g, den // g
        for d in divisors(b * b):
            if (b + d) % a: continue
            y = (b + d) // a
            if y < x: continue
            e = b * b // d
            if (b + e) % a: continue
            z = (b + e) // a
            if z >= y: res.append((x, y, z))
    return res
integ = 0; tot = 0; ex = None
for p in primerange(5, 301):
    for x, y, z in sols(p):
        L = x * y * z // math.gcd(math.gcd(x * y, y * z), x * z)  # lcm(x,y,z)
        L = math.lcm(x, y, z)
        a, b, c = L // x, L // y, L // z
        tot += 1
        q = F(a + b + c, math.lcm(a, b, c))
        if q.denominator == 1: integ += 1
        if ex is None and q.denominator != 1: ex = (p, (x, y, z), q)
print("Z2853: solutions p<=300:", tot, " (a+b+c)/lcm(a,b,c) integer for:", integ, " example non-integer:", ex)
ok = []
for d in range(2, 51):
    for n in range(5, 10001):
        # 1 - 4/n' = d(1-4/n)  =>  4/n' = 1 - d + 4d/n  (need >0)
        r = F(1 - d, 1) + F(4 * d, n)
        if r > 0 and (4 / r).denominator == 1 if False else False: pass
        if r > 0:
            npr = 4 / r
            if npr.denominator == 1 and npr > 4:
                ok.append((d, n, int(npr)))
print("Z2877: (d,n,n') with n' integer > 4 (d<=50, n<=10^4):", ok[:20], " total:", len(ok))
