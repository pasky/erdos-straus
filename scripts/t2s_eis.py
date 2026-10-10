"""O128b §9: Eisenstein/genus main term vs actual Type II counts on the sample primes.

For each prime p in the sample and each (c,d) with c <= C0, d <= D0 (M = 4cd, N = 4c^2 d p + 1):
  act  = #{f | N : f ≡ -1 (mod M)}                       (Prop 8.1, F-version: no gcd condition)
  naive= (1/phi(M)) #{f | N : M-1 <= f <= N/(M-1)}         (eta = 1 term only, with the size window)
  MT   = (2/phi(M)) #{f | N : (p/f) = -1, M-1 <= f <= N/(M-1)}   (eta = 1 and eta = psi = chi_{-4d}, Prop 9.2)
Sums over the box are printed per p, with the sample split into the 10 hard and 20 random primes.
Usage: t2s_eis.py SAMPLEFILE C0 D0
"""
import sys
from sympy import factorint, jacobi_symbol, totient
from itertools import product

fn, C0, D0 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ps = [int(x) for x in open(fn).read().split()]


def divs_from(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [x * q ** k for x in ds for k in range(e + 1)]
    return ds


print("# p   act   naive   MT    act/naive  act/MT")
for idx, p in enumerate(ps):
    act = naive = MT = 0.0
    for c in range(1, C0 + 1):
        for d in range(1, D0 + 1):
            M = 4 * c * d; N = 4 * c * c * d * p + 1
            ph = int(totient(M))
            ds = divs_from(factorint(N))
            win = [f for f in ds if M - 1 <= f <= N // (M - 1)]
            act += sum(1 for f in ds if f % M == M - 1)
            naive += len(win) / ph
            MT += 2 * sum(1 for f in win if jacobi_symbol(p, f) == -1) / ph
    tag = "hard" if idx < 10 else "rand"
    print(f"{p} {tag} {act:.0f} {naive:.2f} {MT:.2f}  {act / naive:.3f}  {act / MT:.3f}", flush=True)
