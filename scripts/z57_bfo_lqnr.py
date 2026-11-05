# z57 BFO: least prime quadratic non-residue q(p) of the G*-zero primes vs all primes in matching ranges (EVIDENCE).
import sys, math, random
from sympy import isprime, primerange, legendre_symbol
zs = [int(x) for x in open('data/z57/bfo/F4zeros.txt').read().split()]
def lq(p):
    for q in primerange(2, 10**6):
        if q == 2:
            if p % 8 in (3, 5): return 2
            continue
        if legendre_symbol(p % q, q) == -1: return q
print("G*-zero primes: p, least prime QNR q(p), log q / log p")
for p in zs: q = lq(p); print(p, q, round(math.log(q)/math.log(p), 3))
random.seed(1)
for lo in (10**3, 10**5, 10**7):
    qs = []
    while len(qs) < 2000:
        p = random.randrange(lo, 10*lo)
        if p % 4 == 1 and isprime(p): qs.append(lq(p))
    print(f"random p=1(4) in [{lo},{10*lo}): mean q={sum(qs)/len(qs):.2f}, P(q>=11)={sum(q>=11 for q in qs)/len(qs):.3f}, P(q>=17)={sum(q>=17 for q in qs)/len(qs):.3f}")
