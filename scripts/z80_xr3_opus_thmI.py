"""Opus R3 falsification test of EXTREME.md Theorem I construction:
p=(k+1)F(U,V)-k, F=U^2+UV+sV^2, s=(k+1)/4, gcd(U,V)=1, p prime, p=1 mod m
(m = product of l in {3,5,7} not dividing k(k+1)). Claims: p in M (mod 840) and
window k fails at p (no divisors u,v of p*x with u+v=0 mod k), x=(p+k)/4.
Also checks the Jacobi-kernel property of all prime factors of x."""
from math import gcd
RS = {1, 121, 169, 289, 361, 529}
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
tot = 0
for k in [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 63, 75, 99, 119, 147, 175, 231, 243, 343]:
    s = (k + 1) // 4; m = 1
    for l in (3, 5, 7):
        if (k * (k + 1)) % l: m *= l
    cnt = bad = notM = 0
    for U in range(-300, 301):
        for V in range(1, 301):
            if gcd(U, V) != 1: continue
            F = U * U + U * V + s * V * V; p = (k + 1) * F - k
            if p <= k or p % m != 1 % m or not isprime(p): continue
            cnt += 1; x = (p + k) // 4; assert x == s * F
            fs = fac(x)
            if p % 840 not in RS: notM += 1
            assert all(jac(q, k) == 1 for q, _ in fs), (k, p, fs)
            R = {1}
            for q, e in fs: R = {(a * pow(q, i, k)) % k for a in R for i in range(e + 1)}
            R |= {(p * a) % k for a in R}
            if any((-a) % k in R for a in R): bad += 1
    tot += cnt
    print(f'k={k} m={m} primes={cnt} notInM={notM} windowSucceeds={bad}')
print('total', tot)
