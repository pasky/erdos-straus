"""rt_modeltest.py (O125 red team, Phase 1(c)).

What does a Type II counting route "see" at primes approximating the campaign's special profinite
points?  For each prime p we compute, for multiplier moduli M <= T, M = 3 (mod 4), A = (M+1)/4:
  N_M(p) = #{D | A^2 : p = -4D (mod M)}          (exact Type II witness count, notes (51.1))
  W(p)   = least M with N_M(p) >= 1  (or None if > T)
  N_T(p) = sum_{M<=T} N_M(p)
  Mloc   = sum_M E[N_M | p mod Q]  -- the 'conditional Haar' main term: exact on the Q-part of M,
           uniform on (Z/M')^* for the Q-coprime part M' (independence heuristic; this is the best
           main term any route using only p mod Q can have).
  M0     = same with Q = 840 (a low-conductor singular series: the 'typical' main term).
Point classes (Q = 8 * prod odd primes <= y, raised to small powers at the special primes):
  one   : p = 1 mod Q                                  (square-mimicking approximant)
  xss   : p = 1 mod Q/(11*13), p = 2 mod 11^a, p = 15 mod 13^b   (x** approximant)
  x9    : p = 9 mod 16, p = -1 mod 7^b, p = 1 otherwise           (x_hat_9 approximant)
  ctrl  : random Mordell-hard primes (p mod 840 a square class) of the same size.
usage: rt_modeltest.py T y nprimes seed
"""
import sys, random
from math import gcd
from sympy import isprime, primerange
from sympy.ntheory.modular import crt

T, y, NP, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
random.seed(seed)
Amax = (T + 1) // 4 + 1
spf = list(range(Amax + 1))
for i in range(2, int(Amax ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, Amax + 1, i):
            if spf[j] == j:
                spf[j] = i

def fac(n):
    out = {}
    while n > 1:
        q = spf[n]; out[q] = out.get(q, 0) + 1; n //= q
    return out

def divisors_sq(A):
    ds = [1]
    for q, e in fac(A).items():
        ds = [d * q ** k for d in ds for k in range(2 * e + 1)]
    return ds

def phi(n):
    r = n; m = n; q = 2
    while q * q <= m:
        if m % q == 0:
            r -= r // q
            while m % q == 0: m //= q
        q += 1
    if m > 1: r -= r // m
    return r

MS = [(M, divisors_sq((M + 1) // 4)) for M in range(3, T + 1, 4)]

def split(M, Q):
    """M = MQ * M' with MQ | Q^infinity, gcd(M', Q) = 1."""
    MQ = 1
    g = gcd(M, Q)
    while g > 1:
        MQ *= g; M //= g; g = gcd(M, Q)
    return MQ, M

SPL = {}
def stats(p, Q):
    N = 0; W = None; loc = 0.0
    for M, Ds in MS:
        r = p % M
        n = sum(1 for D in Ds if (-4 * D - r) % M == 0)
        if n and W is None: W = M
        N += n
        key = (M, Q)
        if key not in SPL: SPL[key] = split(M, Q)
        MQ, Mp = SPL[key]
        c = sum(1 for D in Ds if (-4 * D - p) % MQ == 0 and gcd(4 * D, Mp) == 1)
        loc += c / phi(Mp)
    return N, W, loc

def np_(p):
    for q in primerange(2, 10 ** 6):
        if pow(q, (p - 1) // 2, p) == p - 1: return q

odd = [q for q in primerange(3, y + 1)]
def classes():
    base = {2: (1, 8)}
    for q in odd: base[q] = (1, q)
    one = dict(base)
    xss = dict(base); xss[11] = (2, 11 ** 3); xss[13] = (15, 13 ** 3)
    x9 = dict(base); x9[2] = (9, 16); x9[7] = (-1 % 7 ** 3, 7 ** 3)
    return {'one': one, 'xss': xss, 'x9': x9}

def primes_in(cls, n, lo_mult):
    mods = [m for _, m in cls.values()]; res = [r for r, _ in cls.values()]
    r, Q = crt(mods, res); r, Q = int(r), int(Q)
    out = []; k = lo_mult
    while len(out) < n:
        k += random.randint(1, 50)
        p = r + k * Q
        if isprime(p): out.append(p)
    return out, Q

print(f'T={T} y={y}')
sq840 = sorted({(x * x) % 840 for x in range(840) if gcd(x, 840) == 1})
for name, cls in classes().items():
    ps, Q = primes_in(cls, NP, 10 ** 3)
    for p in ps:
        N, W, loc = stats(p, Q); _, _, m0 = stats(p, 840)
        print(f'{name:5s} p~10^{len(str(p))-1} n_p={np_(p):3d} W={W} N_T={N} Mloc={loc:.2f} M0={m0:.2f}', flush=True)
    P0 = ps[0]
ctrl = []
while len(ctrl) < NP:
    p = random.randrange(P0 // 2, 2 * P0)
    if p % 840 in sq840 and isprime(p): ctrl.append(p)
for p in ctrl:
    N, W, loc = stats(p, 840)
    print(f'ctrl  p~10^{len(str(p))-1} n_p={np_(p):3d} W={W} N_T={N} M0={loc:.2f}', flush=True)
