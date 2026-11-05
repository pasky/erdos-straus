# z57 BFO (EVIDENCE for Thm W's sieve rate): fraction of primes p = 1 (4) near 10^k with no hit at any level C <= K
# (no divisor d = -1 mod 4C of 4Cp+1), K = 1..8, versus the sieve-dimension prediction ~ (log p)^{-kappa_K}.
import random, math
from sympy import isprime, divisors
from sympy.ntheory import totient
random.seed(57)
Ks = range(1, 9)
kap = [sum(1/totient(4*C) for C in range(1, K+1)) for K in Ks]
def hitlevel(p, C):
    N = 4*C*p + 1
    return any((d + 1) % (4*C) == 0 for d in divisors(N))
print("kappa_K:", [round(k, 3) for k in kap])
rows = []
for e in (6, 8, 10, 12):
    lo = 10**e; n = 0; cnt = [0]*len(Ks)
    while n < 3000:
        p = random.randrange(lo, 2*lo)
        if p % 4 != 1 or not isprime(p): continue
        n += 1
        first = None
        for C in Ks:
            if hitlevel(p, C): first = C; break
        for i, K in enumerate(Ks):
            if first is None or first > K: cnt[i] += 1
    fr = [c/n for c in cnt]
    rows.append((e, fr))
    print(f"p~1e{e}: n={n} P(no hit at levels<=K), K=1..8:", [round(f, 4) for f in fr])
# empirical decay exponent between 1e6 and 1e12 vs kappa_K (log log ratio)
L = math.log(math.log(2e12)/math.log(2e6))
print("empirical exponent  -dlogP/dloglog p (1e6->1e12):", [round(-math.log(max(rows[-1][1][i],1e-9)/rows[0][1][i])/L, 2) for i in range(len(Ks))])
