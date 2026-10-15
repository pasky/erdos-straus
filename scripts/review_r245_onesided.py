"""R245: reproduce s6_witness_onesided cap-0 counts: p = 1 (4) prime < P, prime windows q = 3 (4) < Q, q != p;
cap 0 <=> -1 in Sigma_q(K), K = (p+q)/4. Split by (q/p)."""
import sys
from sympy import primerange, factorint, legendre_symbol
P, Q = int(sys.argv[1]), int(sys.argv[2])
c = {1: [0, 0, 0], -1: [0, 0, 0]}  # pairs, cap0, cap0 with K odd
for p in primerange(5, P):
    if p % 4 != 1: continue
    for q in primerange(3, Q):
        if q % 4 != 3 or q == p: continue
        K = (p + q) // 4; S = {1}
        for s, b in factorint(K).items():
            S = {x * pow(s, e, q) % q for x in S for e in range(b + 1)}
        ch = legendre_symbol(q % p, p); c0 = any((-x) % q in S for x in S)
        c[ch][0] += 1; c[ch][1] += c0; c[ch][2] += c0 and K % 2 == 1
print('(q/p)=-1: pairs, cap0, cap0&Kodd =', c[-1]); print('(q/p)=+1: pairs, cap0, cap0&Kodd =', c[1])
