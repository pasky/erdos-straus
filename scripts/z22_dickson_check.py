"""O250 CAP_BOUNDED Thm 1.3 sanity check: build primes p = L t + 1 with all R_m = L/(m+1) t + 1 prime (m <= M,
m = 3 mod 4) and confirm exhaustively that no window m <= M carries a Lemma-3.1 certificate at any cap
(cap searched up to lambda(m), beyond which the box residues repeat), delta_p included.
usage: z22_dickson_check.py M TMAX NWANT
"""
import sys
from math import lcm, prod
from sympy import isprime, primerange, factorint
from sympy.ntheory import reduced_totient
from z22_common import best_cap

M, TMAX, NWANT = map(int, sys.argv[1:4])
Lam = 1
for k in range(1, M + 2):
    Lam = lcm(Lam, k)
L = 16 * Lam * prod(primerange(2, M + 2))
wins = [m for m in range(3, M + 1, 4)]
found = 0
for t in range(1, TMAX + 1):
    p = L * t + 1
    if not all(isprime(L // (m + 1) * t + 1) for m in wins):
        continue
    if not isprime(p):
        continue
    found += 1
    dead = 0
    for m in wins:
        lam = int(reduced_totient(m))
        K = (p + m) // 4
        c = best_cap(p, m, lam + 2, usep=True, fK=factorint(K))
        dead += c is None
    # control: the least forced prime window q (q = 3 mod 4, (q/p) = -1) must exceed M
    q = next(q for q in primerange(3, 10 ** 7) if q % 4 == 3 and pow(p, (q - 1) // 2, q) == q - 1)
    print('t', t, 'p', p, 'windows', len(wins), 'dead', dead, 'least forced window', q)
    if found >= NWANT:
        break
print('M', M, 'L', L, 'found', found)
