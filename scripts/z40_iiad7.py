# z40_iiad7.py (O270): limit-level search for menu II-ad at mu = 0 of c0*2^s + 1 (c0 = 4^J - 1), all branches.
# (C1) 4a^2 d + 1 = c0 u^p (p odd prime; Capelli), (C2) X | N := c0(1 + u^p) = 4^J + 4a^2 d with X = -4^J, N/X = -1 mod q,
# q = odd part of a*d (with multiplicity). Root degree D and factor shape are NOT used: (C1)+(C2) are necessary for every D.
# Usage: z40_iiad7.py c0 PMAX UMAX_p3 [residue filter u mod 8, e.g. 7]
import sys
from sympy import factorint, divisors, primerange
from math import isqrt
c0 = int(sys.argv[1]); PMAX = int(sys.argv[2]); U3 = int(sys.argv[3]); RES = int(sys.argv[4]) if len(sys.argv) > 4 else None
FJ = c0 + 1; J = FJ.bit_length() // 2; assert 4 ** J == FJ
def sqdivs(F):          # all a with a^2 | N, from factorisation F
    out = [1]
    for pr, e in F.items():
        out = [x * pr ** i for x in out for i in range(e // 2 + 1)]
    return out
tot = 0; hits = []
for p in primerange(3, PMAX + 1):
    UM = max(3, int(round(U3 ** (3.0 / p))))
    for u in range(3, UM + 1, 2):
        if (c0 * u ** p - 1) % 4: continue
        if RES is not None and u % 8 != RES: continue
        M = (c0 * u ** p - 1) // 4; FM = factorint(M)
        N = c0 * (1 + u ** p); Nd = None
        for a in sqdivs(FM):
            d = M // (a * a); q = a * d
            while q % 2 == 0: q //= 2
            tot += 1
            # (C2): X = j q - 4^J > 0, X' = N/X = j' q - 1; X <= N
            if q * q > 4 * N + 64:      # then X, X' >= q - 4^J force a product > N unless q small: direct check via j=1..
                pass
            if Nd is None: Nd = divisors(N)
            for X in Nd:
                if (X + FJ) % q == 0 and (N // X + 1) % q == 0:
                    hits.append((p, u, a, d, X, N // X)); print('HIT', hits[-1], flush=True)
print('c0=%d p<=%d (u-range ~ %d^(3/p)) res=%s: %d (u,p,a,d) tested, %d satisfy (C1)+(C2)' % (c0, PMAX, U3, RES, tot, len(hits)))
