"""O152(a): the odd set X(p) = {(t,u,v) >= 1 : (tu-1)(tv-1) = tp+1} (u<->v swap fixes only (p+2,1,1)).
ES(p) <=> some element has 4 | tu-1 (divisor form, CONDITIONAL_ES Lemma 1.1).  Parities of ES-parts.
Usage: PYTHONPATH=scripts uv run python scripts/bs_invol_uvt.py 4000"""
import sys
from sympy import isprime, divisors
P = int(sys.argv[1])
stats = {}
for p in range(25, P, 24):
    if not isprime(p):
        continue
    tot = A = B = 0
    for t in range(1, p + 3):
        N = t * p + 1
        for d in divisors(N):
            if (d + 1) % t == 0 and d >= t - 1 and d > 0:
                tot += 1
                if d % 4 == 0:
                    A += 1
                    if ((N // d) % 4 == 0):
                        B += 1
    stats[p] = (tot, A, B)
odd = lambda i: sum(v[i] & 1 for v in stats.values())
print(f'{len(stats)} primes p=1 (24) < {P}: |X| odd {odd(0)}; ES-part A odd {odd(1)}; both-4|: {odd(2)}; '
      f'A>0 all: {all(v[1] > 0 for v in stats.values())}')
