"""R272 §5 checks (from scratch).
(1) Prop 5.1(a): l | p+4d, l prime, l∤2dp  =>  kronecker(-4d, l) == legendre(l, p).
(2) Prop 5.1(c) Sophie-Germain: d=b^2, l | p+4b^2, l==1 mod 4  =>  (p/l)_4 == (b/l).
(3) Cor 5.3 vs WINDMILL 10.2: for N=tp+1 and m|N, m<=sqrt(N), the form [m,2,N/m] (disc -4tp) is REDUCED,
    so the ideal class of the divisor determines m (hence m mod t) exactly -- not only modulo squares."""
from sympy import primerange, factorint, jacobi_symbol as J
from math import isqrt
viol = n1 = 0
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    for d in range(1, 61):
        for l in factorint(p+4*d):
            if l == 2 or d % l == 0 or l == p: continue
            n1 += 1
            # kronecker(-4d,l) for odd prime l equals Legendre(-4d mod l, l)
            if J((-4*d) % l, l) != J(l, p): viol += 1
print(f"(1) Prop 5.1(a): {n1} triples, {viol} violations")
v2 = n2 = 0
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    for b in range(1, 8):
        for l in factorint(p+4*b*b):
            if l % 4 != 1 or b % l == 0 or l == p: continue
            n2 += 1
            q4 = pow(p, (l-1)//4, l)   # quartic symbol as element of F_l (a 4th root of 1)
            leg = J(b % l, l) % l
            if q4 != leg: v2 += 1
print(f"(2) (p/l)_4 = (b/l) at d=b^2: {n2} cases, {v2} violations")
def reduced(a, b, c): return abs(b) <= a <= c and not (b < 0 and (abs(b) == a or a == c))
n3 = bad3 = 0
for t in (3, 7, 11, 15, 19):
    for p in primerange(5, 3000):
        N = t*p+1
        for m in range(1, isqrt(N)+1):
            if N % m: continue
            n3 += 1
            if not reduced(m, 2, N//m) and m > 2: bad3 += 1
print(f"(3) divisors m<=sqrt(N), m>2 with [m,2,N/m] reduced: {n3-bad3} of {n3} (m=1,2 trivially fine)")
