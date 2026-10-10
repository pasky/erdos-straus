"""O126 §5.3: complete fixed-level Type I search.
Type I(p) at level d  <=>  exists a >= 1, f | 4a^2 d + 1, f = -p (mod 4ad), c = (p+f)/(4ad) >= 1, p does not divide c.
Completeness: by the reflection a<->b we may take a <= b, and then ET Lemma 2.8 gives acd <= 3p/4, so a <= 3p/(4d).
Divisors of 4a^2 d + 1 do not depend on p, so they are computed once per level.
Usage: PYTHONPATH=scripts uv run python scripts/geo_levelsI.py PMAX d1,d2,...  (primes p = 1 mod 24)"""
import sys
from sympy import factorint, primerange, legendre_symbol
from geo_levels import divisors_from

pmax = int(sys.argv[1]); levels = [int(x) for x in sys.argv[2].split(',')]
primes = [p for p in primerange(5, pmax) if p % 24 == 1]
for d in levels:
    A = 3 * pmax // (4 * d) + 1
    divs = [None] + [divisors_from(factorint(4*a*a*d + 1)) for a in range(1, A + 1)]
    tested = 0; fails = []; worst = (0, None)
    for p in primes:
        if legendre_symbol((-d) % p, p) != -1:
            continue
        tested += 1
        found = None
        for a in range(1, 3 * p // (4 * d) + 2):
            m = 4 * a * d
            for f in divs[a]:
                if (p + f) % m == 0 and ((p + f) // m) % p:
                    found = a; break
            if found:
                break
        if found is None:
            fails.append(p)
        elif found > worst[0]:
            worst = (found, p)
    print(f"level d={d}: primes p=1 mod 24, p<{pmax}, (-d/p)=-1: {tested}; failures {len(fails)} {fails[:12]}{'...' if len(fails)>12 else ''}; worst minimal a {worst}")
