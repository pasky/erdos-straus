"""O211 (c): prime-modulus Type II at adversarial primes (all small primes are QRs: p = 1 mod 4*prod_{q<=Q} q).
Prime-modulus Type II on slice (c,d) <=> M = p + 4c^2 d has a PRIME factor h = -1 (mod 4cd).  For each test prime,
scan slices in order of cd <= X, factor M, and report (#slices with a prime-modulus certificate, first slice found).
Odd squares (T1 control) n = r^2 near the same sizes: must give 0 (any divisor, not only prime ones).
Usage: PYTHONPATH=scripts uv run python scripts/y3_adversarial.py X"""
import sys, math
from sympy import isprime, factorint, divisors, primerange

def scan(n, X, prime_only=True):
    hits = 0; first = None
    for s in range(1, X + 1):
        for c in divisors(s):
            d = s//c; m = 4*s; M = n + 4*c*c*d
            if math.gcd(n, m) != 1: continue
            if prime_only: ok = any(q % m == m - 1 for q in factorint(M))
            else: ok = any(h % m == m - 1 for h in divisors(M))
            if ok:
                hits += 1
                if first is None: first = (c, d)
    return hits, first

if __name__ == "__main__":
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    for Q in (7, 13, 19, 23, 29):
        L = 4*math.prod(primerange(2, Q + 1)); k = 1; found = 0
        while found < 3:
            p = 1 + k*L; k += 1
            if not isprime(p): continue
            found += 1; h, f = scan(p, X)
            print(f"Q={Q} p={p} (~1e{math.log10(p):.1f}) slices cd<={X} with prime-modulus cert: {h}, first {f}")
    for r in (10**5 + 1, 10**6 + 1, 3*10**6 + 1):
        print(f"odd square n={r}^2: firing slices (any divisor) cd<={X//4}: {scan(r*r, X//4, False)[0]}")
