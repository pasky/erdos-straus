"""z52b pass1 U05 Z1547/Z1748: C-form win rates at large primes p≈1e12 (Pollard-rho factoring of N=4Cp+1, C≤CMAX).
(a) random primes p≡1 (mod 840); (b) profile-matched primes p≡409 (mod 60060) (same Legendre symbols (q/p), q≤13, as 409).
Win(C) iff a divisor d of N has d≡-1 (mod 4C). Compare win rates per C (C≤CMAX) with the p≤1e5 rates."""
import random, math, sys
from collections import Counter
random.seed(11)
def is_prime(n):
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d = n-1; s = 0
    while d % 2 == 0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
def rho(n):
    if n % 2 == 0: return 2
    while True:
        c = random.randrange(1, n); f = lambda x: (x*x + c) % n
        x = y = random.randrange(2, n); d = 1
        while d == 1:
            x = f(x); y = f(f(y)); d = math.gcd(abs(x-y), n)
        if d != n: return d
def factor(n):
    out = Counter()
    for q in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
        while n % q == 0: out[q] += 1; n //= q
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1: continue
        if is_prime(m): out[m] += 1; continue
        d = rho(m); stack += [d, m//d]
    return out
def wins(p, CMAX):
    res = []
    for C in range(1, CMAX+1):
        m = 4*C; N = m*p+1
        f = factor(N)
        ds = [1]
        for q, e in f.items():
            ds = [d*q**k % m for d in ds for k in range(e+1)] if False else [ (d*pow(q,k,m)) % m for d in ds for k in range(e+1)]
        if (m-1) % m in set(ds): res.append(C)
    return res
CMAX = 40
def rand_prime_in_class(mod, r, lo, hi):
    while True:
        x = random.randrange(lo, hi)//mod*mod + r
        if x > 2 and is_prime(x): return x
A = [rand_prime_in_class(840, 1, 10**12, 2*10**12) for _ in range(40)]
B = [rand_prime_in_class(60060, 409 % 60060, 10**12, 2*10**12) for _ in range(40)]
ra = [wins(p, CMAX) for p in A]; rb = [wins(p, CMAX) for p in B]
def rate(rs): return {C: round(sum(1 for w in rs if C in w)/len(rs),2) for C in (1,2,3,5,10,20,40)}
print(f"(a) random p≡1(840) near 1e12: 40 primes; #with win C≤{CMAX}: {sum(1 for w in ra if w)}; mean wins/p = {sum(len(w) for w in ra)/len(ra):.2f}; per-C rates {rate(ra)}")
print(f"(b) profile-matched (p≡409 mod 60060) near 1e12: 40 primes; #with win C≤{CMAX}: {sum(1 for w in rb if w)}; mean wins/p = {sum(len(w) for w in rb)/len(rb):.2f}; per-C rates {rate(rb)}")
