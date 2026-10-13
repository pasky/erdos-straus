"""O177 (bsD_): 'F-rational' (split-supported) Type II certificates.
Type II slice (c,d), M = 4cd: f | N = 1 + 4c^2 d p, f = -1 (mod M), f' = N/f.  Over F = Q(zeta_M)^+ the condition
f = -1 (mod M) is the quadratic ray-class character eta_{K/F} of an F-ideal of norm f PROVIDED f is a norm of an
F-ideal dividing N, e.g. all prime factors of f are = +-1 (mod M) ("split-supported").  We count, per prime p,
  A: Type II certificates with cd <= C;   B: those with f split-supported;   Bb: f and f' both split-supported.
Run: PYTHONPATH=scripts uv run python scripts/bsD_split_cert.py X C [sq]   (sq: odd squares instead of primes, T1 control)
"""
import sys
from sympy import primerange, factorint, divisors

X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
C = int(sys.argv[2]) if len(sys.argv) > 2 else 30
SQ = len(sys.argv) > 3 and sys.argv[3] == 'sq'


def split_ok(m, M, fac):
    return all(l % M in (1, M - 1) for l in fac if m % l == 0)


def run(n):
    A = B = Bb = 0
    for cd in range(1, C + 1):
        for c in divisors(cd):
            d = cd // c
            M = 4 * cd
            N = 1 + 4 * c * c * d * n
            fac = factorint(N)
            for f in divisors(N):
                if f > N // f:
                    break
                if (f + 1) % M or (N // f + 1) % M:
                    continue
                A += 1
                s1, s2 = split_ok(f, M, fac), split_ok(N // f, M, fac)
                B += s1 or s2
                Bb += s1 and s2
    return A, B, Bb


ns = [m * m for m in range(3, int(X ** 0.5) + 1, 2)] if SQ else [p for p in primerange(5, X) if p % 24 == 1]
zA = zB = zBb = 0
tot = [0, 0, 0]
worst = []
for n in ns:
    A, B, Bb = run(n)
    zA += A == 0
    zB += B == 0
    zBb += Bb == 0
    tot[0] += A
    tot[1] += B
    tot[2] += Bb
    if B == 0:
        worst.append(n)
print(('odd squares' if SQ else 'primes p=1(24)'), '<', X, 'count', len(ns), 'cd <=', C)
print('  no Type II cert:', zA, ' no split-supported (f or f\') cert:', zB, ' no fully split cert:', zBb)
print('  totals A,B,Bb:', tot, ' first n without split cert:', worst[:15])
