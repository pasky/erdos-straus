"""R272: Haar-random failure density of the forced rule F_{B,D} on the b=1 line (from scratch).
p uniform ≡ 1 (4) in [10^16, 2*10^16], conditioned coprime to primes <= max(B,D)+1 (as in the author's setup)."""
import random, sys
from sympy import primerange
def forced(p, d, B, P):
    N = p+4*d; t = 4*d; s = 1; smalls = []
    for q in P:
        if q > B: break
        while N % q == 0: N //= q; s *= q; smalls.append(q)
    L = N % t
    divs = {1}
    for q in smalls: divs |= {x*q % t for x in divs}
    return any(u == t-1 or u*L % t == t-1 for u in divs)
def run(B, D, n, seed):
    rnd = random.Random(seed); P = list(primerange(2, max(B, D)+2)); fails = 0; k = 0
    while k < n:
        p = 4*rnd.randrange(25*10**14, 5*10**15)+1
        if any(p % q == 0 for q in P): continue
        k += 1
        if not any(forced(p, d, B, P) for d in range(1, D+1)): fails += 1
    return fails
for B, D, n in [(10, 200, 20000), (30, 200, 20000), (10, 1000, 4000), (1000, 200, 4000)]:
    f = run(B, D, n, B*7+D)
    print(f"F_{{{B},{D}}}: {f}/{n} = {100*f/n:.2f} %", flush=True)
