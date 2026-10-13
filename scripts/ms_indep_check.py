"""O197 independent check (uses O194's tf_schinzel.count, sympy divisors, not ms_census.c):
confirm 0 solutions at the largest listed failures, and >= 1 solution at the next 20 primes after each."""
import sys, time
from sympy import nextprime
from tf_schinzel import count

cases = [(8, 241), (12, 12241), (16, 83449), (15, 20521), (18, 35281), (24, 620929), (20, 2763601)]
for m, p in cases:
    t = time.time()
    c = count(m, p, stop_at_first=True)
    q, ok = p, 0
    for _ in range(20):
        q = nextprime(q)
        ok += count(m, q, stop_at_first=True) > 0
    print(f"m={m} p={p}: solutions {c} ({time.time()-t:.0f}s); next 20 primes solvable: {ok}/20", flush=True)
