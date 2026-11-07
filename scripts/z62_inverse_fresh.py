#!/usr/bin/env python3
"""z62 INVERSE pre-registered kill test data: near-zeros (primes = 1 (24) in (1.2e7, 1e8], R <= 2) and class-matched
controls (3 nearest primes of the same class mod 840 with R >= median R of the +-50-prime class window).
Needs /tmp/z62_R1e8.bin (scripts/z62_inverse_rsieve.c 100000000)."""
import numpy as np, sympy
R = np.fromfile('/tmp/z62_R1e8.bin', dtype=np.uint16)
N = len(R) - 1
from sympy import isprime
start = 12000000 + ((1 - 12000000) % 24)
near = [n for n in range(start, N + 1, 24) if R[n] <= 2 and isprime(n)]
rows = [(n, 'n', int(R[n])) for n in near]
for p in near:
    win = []
    for sgn in (1, -1):
        q, c = p, 0
        while c < 50:
            q += sgn * 840
            if q < 5 or q > N: break
            if isprime(q): win.append(q); c += 1
    med = np.median([R[q] for q in win])
    ctl = sorted([q for q in win if R[q] >= med], key=lambda q: abs(q - p))[:3]
    rows += [(q, 'c', int(R[q])) for q in ctl]
with open('data/z62/inverse/fresh_sets.txt', 'w') as f:
    f.write('# z62 INVERSE kill-test sets: n = primes = 1 (24) in (1.2e7,1e8] with R<=2 (all); c = 3 class-matched controls each (R >= window median). cols n tag R\n')
    for r in rows: f.write('%d %s %d\n' % r)
print(len(near), len(rows))
