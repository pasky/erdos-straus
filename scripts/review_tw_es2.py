"""R182: check of TWISTED_T1 Prop 2.3(iii)/Principle(beta): for ES 4/n = 1/x+1/y+1/z (n odd, x,y,z > 0),
the quaternion class alpha = (-x/z, -y/z)_{-1} has inv_inf = 1/2 and inv_2 = 0 on every solution
(from-scratch 2-adic Hilbert symbol), so sum_{p | n} inv_p = 1/2."""
from fractions import Fraction
from sympy import factorint

def v2split(a):
    a = Fraction(a); v = 0; num, den = a.numerator, a.denominator
    while num % 2 == 0: num //= 2; v += 1
    while den % 2 == 0: den //= 2; v -= 1
    return v, num * den  # unit part mod squares ~ num*den (odd)

def hilb2(a, b):
    """(a,b)_2 in {0,1} (1 = -1)"""
    va, ua = v2split(a); vb, ub = v2split(b)
    eps = lambda u: ((u - 1) // 2) % 2
    om = lambda u: ((u * u - 1) // 8) % 2
    return (eps(ua) * eps(ub) + va * om(ub) + vb * om(ua)) % 2

def hilbp(a, b, p):
    a = Fraction(a); b = Fraction(b)
    def vu(x):
        num, den, v = x.numerator, x.denominator, 0
        while num % p == 0: num //= p; v += 1
        while den % p == 0: den //= p; v -= 1
        return v, num * pow(den, -1, p) % p
    va, ua = vu(a); vb, ub = vu(b)
    t = (-1 if (va * vb) % 2 else 1) * pow(ua, vb % (p - 1), p) * pow(pow(ub, -1, p), va % (p - 1), p) % p
    return 0 if pow(t, (p - 1) // 2, p) == 1 else 1

bad2 = 0; tot = 0; badsum = 0
for n in range(3, 400, 2):
    q = Fraction(4, n)
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r = q - Fraction(1, x)
        if r <= 0: continue
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fraction(1, y)
            if s <= 0 or s.numerator != 1: continue
            z = s.denominator
            if z < y: continue
            for (a1, a2, a3) in ((x, y, z), (y, z, x), (x, z, y)):
                a, b = Fraction(-a1, a3), Fraction(-a2, a3)
                tot += 1
                if hilb2(a, b): bad2 += 1
                sp = sum(hilbp(a, b, p) for p in factorint(n)) % 2
                if sp != 1: badsum += 1
print(f"ES n odd < 400: {tot} labelled solutions; inv_2 != 0 on {bad2}; sum_(p|n) inv_p != 1/2 on {badsum}")
