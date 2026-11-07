#!/usr/bin/env python3
"""z62 INVERSE: build the test-integer lists (zeros, falsifier sets, matched controls) with exact R where n <= 1.2e7.
Needs /tmp/z62_R12e6.bin from scripts/z62_inverse_rsieve.c (N = 12 000 000)."""
import numpy as np, sympy, random
R = np.fromfile('/tmp/z62_R12e6.bin', dtype=np.uint16)
NMAX = len(R) - 1
def rd(fn):
    out = []
    for l in open(fn):
        l = l.strip()
        if l and not l.startswith('#'): out.append(int(l.split()[0]))
    return out
S = 'data/z58/screens/'
Z = rd(S + 'star_prime_zeros.txt'); G = rd(S + 'gstar_zeros.txt'); E = rd(S + 'r8_zeros_1e10.txt'); K = rd(S + 'composite_zeros_le8e6.txt')
rows = []
def r(n): return int(R[n]) if n <= NMAX else -1
for n in Z: rows.append((n, 'Z', r(n)))
for n in G:
    if n not in Z: rows.append((n, 'G', r(n)))
for n in E: rows.append((n, 'E', -1))
for n in K: rows.append((n, 'K', r(n)))
for m in [21, 23, 77, 101, 301, 1001, 2001, 2969]: rows.append((m * m, 'Q', r(m * m)))
# matched controls: 15 primes of the same class mod 840 on each side of each zero prime
for p in Z:
    for sgn in (1, -1):
        q, c = p, 0
        while c < 15:
            q += sgn * 840
            if q < 5: break
            if sympy.isprime(q): rows.append((q, 'c', r(q))); c += 1
# near-zeros: primes p = 1 (24), 10^5 < p <= 1.2e7, 1 <= R <= 4 (all), and a typical-R random sample
near = [n for n in range(100009, NMAX + 1, 24) if 1 <= R[n] <= 4 and sympy.isprime(n)]
for n in near: rows.append((n, 'n', r(n)))
random.seed(62)
typ = []
while len(typ) < 400:
    n = random.randrange(100009, NMAX, 24)  # = 1 (24)
    if sympy.isprime(n) and R[n] > 4: typ.append(n)
for n in typ: rows.append((n, 't', r(n)))
with open('data/z62/inverse/sets.txt', 'w') as f:
    f.write('# z62 INVERSE test integers: n tag R(n) (R=-1: not computed, n > 1.2e7). Tags: Z (★)-zero primes, G G*-zeros with R>0,\n')
    f.write('# E R8-zero primes near 1e10, K composite zeros <= 8e6, Q odd squares, c matched controls (same class mod 840, 15 each side of each Z),\n')
    f.write('# n near-zeros (primes = 1 (24) in (1e5, 1.2e7] with 1<=R<=4, all), t typical (400 random primes = 1 (24), R>4, seed 62)\n')
    for n, t, rr in rows: f.write(f'{n} {t} {rr}\n')
print(len(rows), 'near', len(near))
