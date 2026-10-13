#!/usr/bin/env python3
"""R185 independent necessary-condition screen for §4.2. For n_m = k 2^m + 1 (k ≡ 3 mod 6), a finite ET/divisor covering
with period L and moduli built from primes q <= QMAX, ord_q(2) | L, can only exist if every m mod L is 'killed' by such a q:
q | n_m or (n_m/q) = -1 (Thm 1.4 + Mordell/Schinzel: classes solvable by polynomials avoid unit squares).
Reports, per k, the least L in LS that is square-clear, or 'SURVIVES' (unit-square-mimicking exponent classes remain)."""
import sys
from sympy import primerange, n_order
QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 600
LS = [12, 24, 36, 48, 60, 72, 84, 120, 132, 144, 180, 240, 252, 360, 396, 420, 504, 720, 840, 1260, 2520]
ordq = {q: n_order(2, q) for q in primerange(3, QMAX)}
def qr_table(q):
    t = bytearray(q)
    for a in range(1, q): t[a * a % q] = 1
    return t
cache = {}
res = {}
for k in range(3, KMAX + 1, 6):
    found = None
    for L in LS:
        Q = [q for q, o in ordq.items() if L % o == 0 and k % q != 0]
        alive = set(range(L))
        for q in Q:
            if q not in cache: cache[q] = qr_table(q)
            t = cache[q]; o = ordq[q]
            kill = {m for m in range(o) if t[(k * pow(2, m, q) + 1) % q] == 0}   # 0 residue or non-residue
            alive = {m for m in alive if (m % o) not in kill}
            if not alive: break
        if not alive:
            found = L; break
    res[k] = found
    print(k, found if found else 'SURVIVES(sample m mod %d: %s)' % (LS[-1], sorted(alive)[:4]), flush=True)
clear = [k for k in res if res[k]]
print('square-clear:', len(clear), ' surviving:', [k for k in res if not res[k]])
