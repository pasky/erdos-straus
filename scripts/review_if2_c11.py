"""R25 C11: universal upper bound on sigma in SPW from one small class split into large classes.
For q <= N/2 and residue b with c = c(b,q), the class b mod q is the disjoint union of k classes mod kq;
if kq > C N then (P1)+(P2) force c <= k(1 - sigma), i.e. sigma <= 1 - c/k. Minimise over q, b, k."""
import sys
from fractions import Fraction
def bound(N, C):
    best = Fraction(1)
    for q in range(1, N // 2 + 1):
        c = -(-N // q)          # max count of a class mod q in [1,N]
        k = int(C * N) // q + 1  # least k with k q > C N
        best = min(best, 1 - Fraction(c, k))
    return best
for C in (1, 1.5, 2, 3):
    print(f"C={C}: " + " ".join(f"N={N}:{float(bound(N, C)):.4f}" for N in (12, 13, 16, 20, 21, 30, 40, 60, 80, 1000, 10**5)))
