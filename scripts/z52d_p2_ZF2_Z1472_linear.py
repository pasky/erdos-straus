"""Z1472: check the (+,|)-linear forms of (*) and Type II against direct enumeration.
(*)(n)    <=> exists u,m >= 1: 4u | m+1  and  m | n+u                      [m = 4uC-1, B = (n+u)/m]
TypeII(p) <=> exists e,N,a,b,y: p+e = 4N, a|N, b|N, b|y, a|y+1 (gcd(a,b)=1), e | a+b
(direct Type II for prime p: 4/p = 1/N + 1/(pY) + 1/(pZ), e = 4N-p, e/N = 1/Y+1/Z)."""
import sys, json
from math import gcd
from sympy import isprime
def star_direct(n):
    for u in range(1, n + 1):
        if 4*u - u - 1 > n: break
        for B in range(1, n + 1):
            q = 4*u*B
            if q - u - B > n: break
            if (n + u + B) % q == 0: return True
    return False
def star_linear(n):
    for u in range(1, n + 1):
        if 4*u - 1 > n + u: break
        m = 4*u - 1
        while m <= n + u:
            if (n + u) % m == 0: return True
            m += 4*u
    return False
def typeII_direct(p):
    for N in range(p // 4 + 1, p // 2 + 1):
        e = 4*N - p
        if e <= 0: continue
        for Y in range(N // e + 1, 2*N // e + 1):
            num = e*Y - N
            if num > 0 and (N*Y) % num == 0: return True
    return False
def typeII_linear(p):
    for e in range(1, 3*p):
        if (p + e) % 4: continue
        N = (p + e) // 4
        if e > 2*N: break
        divs = [d for d in range(1, N + 1) if N % d == 0]
        for a in divs:
            for b in divs:
                if gcd(a, b) == 1 and (a + b) % e == 0: return True
    return False
if __name__ == '__main__':
    X1, X2 = int(sys.argv[1]), int(sys.argv[2])
    mism1 = [n for n in range(3, X1, 2) if star_direct(n) != star_linear(n)]
    mism2 = []; cnt = 0
    for p in range(5, X2):
        if isprime(p):
            cnt += 1
            if typeII_direct(p) != typeII_linear(p): mism2.append(p)
    print(json.dumps({'star_checked_odd_n_below': X1, 'star_mismatches': mism1,
                      'typeII_checked_primes_below': X2, 'n_primes': cnt, 'typeII_mismatches': mism2}))
