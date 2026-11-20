"""Opus hostile review: independent no-shortcut verifier for k*u*B*C - u - B = p.
Own code; shares nothing with repository engines.  For each u with
k*u^2-2u <= p (WLOG u<=B; u=B impossible since p odd), fully factor N=p+u by a
sieve over all primes <= sqrt(p+U) (factorization verified by re-multiplying),
enumerate every divisor f of N, and accept f = k*u*C-1 (C>=1) with N/f >= u.
Also a second partial method: for u >= U2 iterate C directly."""
import sys
from math import isqrt

p = int(sys.argv[1]) if len(sys.argv) > 1 else 1590284203561

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(range(i*i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]

def umax(k):
    u = isqrt(p // k) + 2
    while k*u*u - 2*u > p: u -= 1
    return u

U = umax(4)
L = isqrt(p + U) + 1
P = primes_upto(L)
assert all(p % q for q in P if q*q <= p), 'p composite'
print('p', p, 'prime (trial division to', isqrt(p), ') mod840', p % 840)

rem = [p + u for u in range(U + 1)]
fac = [[] for _ in range(U + 1)]
for q in P:
    u0 = (-p) % q
    if u0 == 0: u0 = q
    for u in range(u0, U + 1, q):
        e = 0
        while rem[u] % q == 0:
            rem[u] //= q; e += 1
        fac[u].append((q, e))
for u in range(1, U + 1):
    if rem[u] > 1:
        assert rem[u] > L  # remaining cofactor is a prime > sqrt(N)
        fac[u].append((rem[u], 1))
    prod = 1
    for q, e in fac[u]: prod *= q**e
    assert prod == p + u

def divisors(fl):
    ds = [1]
    for q, e in fl:
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds

sols = {4: [], 8: []}
for k in (4, 8):
    Uk = umax(k)
    for u in range(1, Uk + 1):
        N = p + u; m = k*u
        for f in divisors(fac[u]):
            if f % m == m - 1 and N // f >= u:
                B = N // f; C = (f + 1) // m
                assert k*u*B*C - u - B == p
                sols[k].append((u, B, C))
    print('k', k, 'U', Uk, 'unordered', len(sols[k]), 'ordered', 2*len(sols[k]),
          'first', sorted(sols[k])[:3])

# Second, partial, method: u >= U2, iterate C directly (C <= (p+2u)/(k u^2)).
U2 = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
for k in (4, 8):
    cnt = 0
    for u in range(U2, umax(k) + 1):
        N = p + u; m = k*u
        for C in range(1, (N // u + 1) // m + 1):
            f = m*C - 1
            if N % f == 0 and N // f >= u: cnt += 1
    ref = sum(1 for s in sols[k] if s[0] >= U2)
    print('k', k, 'direct-C check u>=', U2, cnt, 'vs sieve', ref)
    assert cnt == ref
