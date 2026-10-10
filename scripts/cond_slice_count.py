"""O127 §3: exact count S(p) of the Type I a=1 slice, #{(c,f,g): cfg-c-f=p, fg=1 mod 4},
via g <= p+2 and divisors m of gp+1 with m = -1 (mod g), 4 | m.  Compares with log^2 p and
records the smallest g.  Usage: PYTHONPATH=scripts uv run python scripts/cond_slice_count.py P0 K
(first K primes >= P0, plus the first K Mordell-hard primes >= P0)."""
import sys, math
from sympy import nextprime, divisors

def S(p):
    tot, gmin = 0, None
    for g in range(1, p + 3, 2):
        N = g * p + 1
        if N % 4:
            continue
        k = sum(1 for m in divisors(N) if m % 4 == 0 and m % g == g - 1)
        if k and gmin is None:
            gmin = g
        tot += k
    return tot, gmin

P0, K = int(sys.argv[1]), int(sys.argv[2])
sq = {(x * x) % 840 for x in range(840)}
for label, cond in (("all", lambda p: True), ("hard", lambda p: p % 840 in sq)):
    p, n, rows = P0, 0, []
    while n < K:
        p = nextprime(p)
        if not cond(p):
            continue
        n += 1
        s, gm = S(p)
        rows.append((p, s, round(s / math.log(p) ** 2, 3), gm))
    print(label, rows)
