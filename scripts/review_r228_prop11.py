"""R228 from-scratch check of the DK sign table and NEAR_SQUARE_EXIST Prop 1.1.

For every prime p = 1 (mod 4) below X, enumerate ALL words (t,u,v), tuv - u - v = p, with u <= v
(then also count the mirrored word (t,v,u)). chi = Legendre(A/p), A = tu - 1, computed by Euler.
Checks:
  (S) sign table: chi = -1 iff 4 divides one of t,u,v,A,A*;
  (P) if p+u (resp. p+v) is a sum of two coprime squares then chi = +1, and the flagged side is odd.
Independent of the author's scripts.
"""
import sys

X = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
LIM = 2 * X + 10
spf = list(range(LIM + 1))
i = 2
while i * i <= LIM:
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1


def fac(n):
    d = {}
    while n > 1:
        q = spf[n]
        d[q] = d.get(q, 0) + 1
        n //= q
    return d


def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def coprime_two_squares(n):
    # n = x^2 + y^2 with gcd(x,y)=1  <=>  4 does not divide n and all odd primes are 1 mod 4 (n>=1)
    if n % 4 == 0:
        return False
    for q in fac(n):
        if q % 2 == 1 and q % 4 == 3:
            return False
    return True


def brute_cts(n):
    # direct brute force for small n to validate coprime_two_squares
    x = 0
    while x * x <= n:
        y2 = n - x * x
        y = int(y2 ** 0.5)
        while y * y > y2:
            y -= 1
        while (y + 1) ** 2 <= y2:
            y += 1
        if y * y == y2:
            from math import gcd
            if gcd(x, y) == 1:
                return True
        x += 1
    return False


for n in range(1, 3000):
    assert coprime_two_squares(n) == brute_cts(n), n

nwords = nbad_table = nflag = nflag_bad = nflag_even = 0
nprimes = 0
for p in range(5, X, 4):
    if spf[p] != p:
        continue
    nprimes += 1
    u = 1
    while u * u <= p + 2 * u + 2:  # u <= v  =>  u^2 <= uv <= tuv = p+u+v <= p+2v ... crude bound, filtered below
        N = p + u
        for A in divisors(fac(N)):
            if (A + 1) % u:
                continue
            t = (A + 1) // u
            v = N // A
            if v < u:
                continue
            Astar = t * v - 1
            assert t * u * v - u - v == p and A * Astar == t * p + 1
            chi = pow(A % p, (p - 1) // 2, p) if A % p else 0
            chi = -1 if chi == p - 1 else chi
            assert chi in (1, -1)
            for (uu, vv, AA) in ((u, v, A), (v, u, Astar)) if u != v else ((u, v, A),):
                nwords += 1
                table = -1 if any(z % 4 == 0 for z in (t, uu, vv, A, Astar)) else 1
                if table != chi:
                    nbad_table += 1
                if coprime_two_squares(p + uu):
                    nflag += 1
                    if chi == -1:
                        nflag_bad += 1
                    if uu % 2 == 0:
                        nflag_even += 1
        u += 1
print(f"primes={nprimes} words(ordered,both orientations)={nwords} table_mismatch={nbad_table}")
print(f"words with p+u coprime-two-squares: {nflag}; with chi=-1: {nflag_bad}; with that u even: {nflag_even}")
