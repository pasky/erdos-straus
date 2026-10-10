"""O123 §2 Lemma 2.5 check: every Type I solution (a,c,d,f) of a prime p has kronecker(-4d, -p) = +1
(the d-genus condition), and counts how many d<=D satisfy it. Also: distribution of solutions over d."""
import sys, math
from sympy import isprime, divisors
from sympy.ntheory import legendre_symbol
from sympy.functions.combinatorial.numbers import jacobi_symbol
def kron(D, n):  # Kronecker symbol (D/n), n odd positive
    return jacobi_symbol(D % n, n) if n > 1 else 1
P = int(sys.argv[1]); viol = 0; tot = 0; from collections import Counter; dd = Counter()
for p in range(5, P + 1):
    if not isprime(p): continue
    for c in range(1, p):
        for d in range(1, p // c + 1):
            if (c * d) % p == 0: continue
            q = 4 * c * d; m = p * p + 4 * c * c * d
            for f in divisors(m):
                if (f + p) % q: continue
                a = (f + p) // q; b = (p * a + c) // f
                if a > b or math.gcd(math.gcd(a, b), c) != 1: continue
                tot += 1; dd[d] += 1
                # chi_{-4d}(-p) via chi_{-4d}(f) with f odd: Kronecker(-4d, f) = jacobi(-4d mod f, f)
                # f = -p (mod 4d), f odd and coprime to d, so Kronecker(-4d, f) = chi_{-4d}(-p)
                if kron(-4 * d, f) != 1:
                    viol += 1
print("solutions", tot, "violations of chi_{-4d}(f)=1:", viol)
print("share of solutions by d (top):", [(d, round(v / tot, 3)) for d, v in sorted(dd.items())[:12]])
