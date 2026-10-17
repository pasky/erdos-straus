"""O255 PARITY_AUDIT Lemma 2.1 check: R(p) = #{(u,B,C): 4uBC-u-B=p} via (u,C) region; M(p) vs (log p)^2/8."""
import math, sys
from sympy import primerange

def R_direct(p):
    # enumerate (u,C), B=(p+u)/(4uC-1)
    r = 0; M = 0.0; npairs = 0
    u = 1
    while 4*u - 1 <= p + u:
        C = 1
        while 4*u*C - 1 <= p + u:
            m = 4*u*C - 1
            npairs += 1; M += 1.0/m
            if (p + u) % m == 0: r += 1
            C += 1
        u += 1
    return r, M, npairs

def R_brute(p):
    r = 0
    for u in range(1, p+1):
        for B in range(1, p+1):
            if 4*u*B - u - B > p: break
            num = p + u + B
            if num % (4*u*B) == 0: r += 1
    return r

for p in list(primerange(3, 400)):
    a = R_direct(p)[0]; b = R_brute(p)
    assert a == b, (p, a, b)
print("identity R_direct == R_brute for primes < 400: OK")
for p in [10007, 100003, 1000003, 10000019]:
    r, M, n = R_direct(p)
    L = math.log(p)
    print(p, "R=", r, "M=%.2f" % M, "(logp)^2/8=%.2f" % (L*L/8), "|R|=", n, "(p/4)logp=%.0f" % (p/4*L))
