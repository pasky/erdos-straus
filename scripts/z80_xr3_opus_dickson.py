"""Opus R3 sanity test of EXTREME.md §10 Dickson construction for small J (T=4J-1):
search u with p=1+Qu, p=-1 mod b, all 1+Qu/(4j) prime; check windows 3..T fail and g<b."""
from math import lcm, prod, gcd
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
def jac(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0
def fac(n):
    out = []; d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0: n //= d; e += 1
            out.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1: out.append((n, 1))
    return out
def window_ok(p,k):
    x=(p+k)//4; R={1}
    for q,e in fac(x): R={(a*pow(q,i,k))%k for a in R for i in range(e+1)}
    R|={(p*a)%k for a in R}; return any((-a)%k in R for a in R)
for J in (1,2,3):
    T=4*J-1; Q=3360*lcm(*range(1,T+1))*prod(l for l in range(2,T+1) if isprime(l))
    b=next(q for q in range(2*T+1,4*T) if isprime(q) and q%4==3 and Q%q)
    found=0
    for u in range(1,3*10**6):
        p=1+Q*u
        if (p+1)%b or not isprime(p): continue
        if all(isprime(1+Q*u//(4*j)) for j in range(1,J+1)):
            g=next(k for k in range(3,10**6,4) if window_ok(p,k))
            assert g>T and g<=b and p%840==1,(J,p,g)
            found+=1
            if found<=2: print('J',J,'T',T,'b',b,'p',p,'g',g)
            if found>=20: break
    print('J',J,'instances',found)
