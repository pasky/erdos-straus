"""O236: q*(p) (least prime window) on Mordell-hard classes vs the rest, primes p = 1 (4) <= N."""
import sys
from sympy import primerange, jacobi_symbol
N = int(sys.argv[1])
Q = [q for q in primerange(3, 2000) if q % 4 == 3]
H = {1, 121, 169, 289, 361, 529}
st = {True: [], False: []}
for p in primerange(5, N + 1):
    if p % 4 != 1:
        continue
    qs = next(q for q in Q if q % 8 == (4 - p) % 8 and jacobi_symbol(q, p) == -1)
    st[p % 840 in H].append(qs)
for h in (True, False):
    v = st[h]
    print("Mordell-hard" if h else "other", len(v), "mean q*", round(sum(v) / len(v), 2), "max", max(v))
