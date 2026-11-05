# z58 LOGIC: least u-form witness u_min(p) := least u >= 1 such that p + u has a divisor d = -1 (mod 4u)
# (equivalently the least remainder r over all hits d; Z57_SYNTH Lemma A.1), at sampled primes, by factoring p+1, p+2, ...
# Samples (decades [10^e, 10^(e+1)); sympy isprime = probable-prime test beyond 2^64): random Mordell-class primes at several sizes, and "square-mimicking" primes p = 1 (mod 8*prod_{3<=l<=y} l)
# (quadratic residues mod every prime <= y; n_p > y). Prints per row: label, size, count, mean/max u_min, argmax.
# usage: uv run --with sympy python scripts/z58_logic_umin.py
import random, math, sys
from sympy import isprime, divisors
random.seed(5858)
def umin(p, cap=10**6):
    for u in range(1, cap):
        q = 4 * u
        for d in divisors(p + u):
            if d % q == q - 1: return u
    return None
M = {1, 121, 169, 289, 361, 529}
def rand_mord(e):
    while True:
        p = random.randrange(10**e, 10**(e + 1)); p += (random.choice(sorted(M)) - p) % 840
        if isprime(p): return p
def rand_mimic(e, y):
    L = 8
    for l in range(3, y + 1):
        if isprime(l): L *= l
    while True:
        p = random.randrange(10**e // L, 10**(e + 1) // L) * L + 1
        if isprime(p): return p
rows = [('mord', e, None, k) for e, k in ((12, 60), (15, 40), (18, 25))] + \
       [('mimic', e, y, k) for e, y, k in ((15, 29, 30), (18, 37, 25), (21, 43, 15))]
for lab, e, y, k in rows:
    vals = []
    for _ in range(k):
        p = rand_mord(e) if lab == 'mord' else rand_mimic(e, y)
        vals.append((umin(p), p))
    us = [v for v, _ in vals]
    mx = max(vals)
    print(f"{lab} 1e{e} y={y} n={k} mean_umin={sum(us)/k:.1f} max_umin={mx[0]} at p={mx[1]} hist(u<=1,2..4,5..16,>16)="
          f"{sum(u<=1 for u in us)},{sum(2<=u<=4 for u in us)},{sum(5<=u<=16 for u in us)},{sum(u>16 for u in us)}", flush=True)
