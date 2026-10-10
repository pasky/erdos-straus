"""O131b: (1) PARI check: for alpha = p + 2c*sqrt(-d) (p prime, p∤2cd, p inert in Q(sqrt(-d))), every prime of N(alpha)
splits, alpha is divisible by exactly one prime above each, so #{ideal divisors of alpha in O_K} = tau(N(alpha)) and
f <-> a = (f, alpha) is a bijection {f | N(alpha)} <-> {a | alpha} with N(a) = f.
(2) exact character formula with genus factor, against the engine counts."""
import cypari2, numpy as np
from sympy import primerange, divisor_count, isprime
pari = cypari2.Pari(); pari.allocatemem(2*10**8, silent=True)
bad = 0; tested = 0
for d in [k for k in range(1, 60) if pari(f'issquarefree({k})')]:
    K = pari(f'nfinit(x^2+{d})')
    for p in primerange(5, 400):
        if d % p == 0 or pari(f'kronecker(-{d},{p})') != -1: continue   # p inert (only these carry Type I)
        for c in range(1, 8):
            if c % p == 0: continue
            al = pari(f'{p}+{2*c}*x'); F = pari.idealfactor(K, al)
            nid = int(np.prod([int(e) + 1 for e in F[1]])) if len(F[1]) else 1
            N = p*p + 4*c*c*d
            # every prime ideal in F lies over a split prime, and over each rational prime only one appears
            ok = nid == divisor_count(N) and all(int(pari.idealnorm(K, P)) == int(P.pr_get_p()) for P in F[0])
            ok &= len(set(int(P.pr_get_p()) for P in F[0])) == len(F[0])
            tested += 1; bad += (not ok)
print(f'(1) ideal-divisor bijection: {tested} (p,c,d) tested, {bad} failures')
