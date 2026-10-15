"""R255: are there unit-square points mu != 0 of n = 15*4^mu + 1 (S_1 points) beyond mu = 0?
For modulus N, list residues t mod N such that 15*4^t + 1 is a nonzero QR mod every odd prime l with ord_l(4) | N
(these are exactly the constraints from primes l | 4^N - 1; any S_1 point reduces to a survivor mod N)."""
import sys
from sympy import factorint, legendre_symbol
c0, k = int(sys.argv[1]), int(sys.argv[2])
for N in [int(x) for x in sys.argv[3:]]:
    ps = [p for p in factorint(4**N - 1) if p % 2 == 1]
    surv = [t for t in range(N) if all((c0 * pow(4, t, p) + k) % p and legendre_symbol((c0 * pow(4, t, p) + k) % p, p) == 1 for p in ps)]
    print(N, 'primes', len(ps), 'survivors', surv[:20], '(count', len(surv), ')', flush=True)
