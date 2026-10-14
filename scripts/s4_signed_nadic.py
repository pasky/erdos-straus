r"""s4_signed_nadic: positive vs signed integral points of X_n: t*u*v - u - v = n (t,u,v nonzero).
For each odd n <= N reports, per class (prime / odd square / other):
  POS  : positive word with chi = (-(tu-1)/n) = -1           (ES-five(n))
  CERT2: signed word that is a 2-adic five-slice certificate (4 | tu-1, tv-1, t, u or v)
  SGNn : signed word with chi = -1                            (the n-adic signed relaxation)
and checks (i) definiteness of the path form <=> positive word, (ii) chi*cert relation with the real sign.
Enumeration: t != 0, |t| <= n+3, tn+1 = A*B, A = B = -1 (mod t), A,B != -1 (u,v != 0).
usage: s4_signed_nadic.py N"""
import sys
from math import isqrt

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

SPF = None
def build_spf(L):
    global SPF
    SPF = list(range(L + 1))
    for i in range(2, isqrt(L) + 1):
        if SPF[i] == i:
            for j in range(i * i, L + 1, i):
                if SPF[j] == j: SPF[j] = i

def divisors(m):
    m = abs(m); ds = [1]
    while m > 1:
        q = SPF[m]; e = 0
        while m % q == 0: m //= q; e += 1
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds

def words(n):
    for t in range(-(n + 3), n + 4):
        if t == 0: continue
        M = t * n + 1
        if M == 0: continue
        for a in divisors(M):
            for A in (a, -a):
                B = M // A
                if A == -1 or B == -1: continue
                if (A + 1) % t or (B + 1) % t: continue
                u, v = (A + 1) // t, (B + 1) // t
                if u == 0 or v == 0: continue
                yield t, u, v, A, B

def isprime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))

N = int(sys.argv[1])
build_spf((N + 3) * N + 2)
stats = {}
TOT = [0, 0, 0]
bad_def = 0; bad_rel = 0
for n in range(3, N + 1, 2):
    cls = 'prime' if isprime(n) else ('square' if isqrt(n) ** 2 == n else 'other')
    pos = cert2 = sgn = 0
    for t, u, v, A, B in words(n):
        assert t * u * v - u - v == n
        if A % n == 0 or (n > 1 and jacobi(A, n) == 0): continue
        chi = jacobi(-A, n)
        positive = t > 0 and u > 0 and v > 0
        definite = v > 0 and t * v - 1 > 0          # leading minors v, tv-1, n of [[v,-1,0],[-1,t,-1],[0,-1,u]]
        bad_def += positive != definite
        c4 = any(x % 4 == 0 for x in (A, B, t, u, v))
        if positive and chi == -1: pos += 1
        if c4: cert2 += 1
        if chi == -1: sgn += 1
        # relation: for definite words cert <=> chi=-1 (MODEL_SPECIFIC 3.1a); record failures of naive transfer
        if definite and (c4 != (chi == -1)): bad_rel += 1
    if cls == 'prime': TOT[0] += pos; TOT[1] += sgn; TOT[2] += 1
    s = stats.setdefault(cls, [0, 0, 0, 0, []])
    s[0] += 1; s[1] += pos > 0; s[2] += cert2 > 0; s[3] += sgn > 0
    if sgn == 0 and cls != 'square': s[4].append(n)
for k, (cnt, p, c, g, fails) in stats.items():
    print(f"{k:7s} n={cnt:5d}  POS>0:{p:5d}  CERT2>0:{c:5d}  SGNn>0:{g:5d}  SGNn-failures(non-square): {fails[:20]}")
print("positivity != definiteness:", bad_def, "| definite words violating cert<=>chi=-1:", bad_rel)
print("primes: mean #positive chi=-1 words %.2f, mean #signed chi=-1 words %.2f" % (TOT[0]/TOT[2], TOT[1]/TOT[2]))
