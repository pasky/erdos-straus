"""O141(c): search-complexity profile for Mordell-hard primes.
W(p)   = min M = 3 (4) with p mod M in R(M) = {-4D mod M : D | ((M+1)/4)^2}  (POINTWISE_OMEGA notation;
         a p-independent congruence-table search, no factoring of p-dependent numbers).
Tf(p)  = min t with t*p+1 = m*m'', 4|m, m = m'' = -1 (mod t)  (divisor form; one factorisation per t).
Prints record-holders of both along hard primes p <= X (p mod 840 in Mordell's six classes).
Usage: bs_logic_search.py X MMAX TMAX
"""
import sys
from sympy import primerange, divisors
X = int(sys.argv[1]); MMAX = int(sys.argv[2]); TMAX = int(sys.argv[3])
HARD = {1, 121, 169, 289, 361, 529}
R = {}
for M in range(3, MMAX + 1, 4):
    A = (M + 1) // 4
    R[M] = {(-4 * D) % M for D in divisors(A * A)}
def W(p):
    for M in range(3, MMAX + 1, 4):
        if p % M in R[M]:
            return M
    return None
def Tf(p):
    for t in range(1, TMAX + 1):
        N = t * p + 1
        for m in divisors(N):
            if m % 4 == 0 and (m + 1) % t == 0 and (N // m + 1) % t == 0:
                return t
    return None
recW = recT = 0; cnt = 0
import math
for p in primerange(5, X):
    if p % 840 not in HARD:
        continue
    cnt += 1
    w, t = W(p), Tf(p)
    if w is None or w > recW:
        recW = w if w else 10**18
        print(f"W-record p={p} log p={math.log(p):.2f} W={w}", flush=True)
    if t is None or t > recT:
        recT = t if t else 10**18
        print(f"Tf-record p={p} log p={math.log(p):.2f} Tf={t}", flush=True)
print("hard primes:", cnt)
