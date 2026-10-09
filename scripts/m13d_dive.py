"""Random dives below open nodes (task O103): estimates the offspring mean of the 'best split' policy.

usage: m13d_dive.py nodes.txt Pm maxsteps seed
At each step the current node x mod L is open w.r.t. all classes M | L (complete engine).  For every split q
(primes < Pm, or the next power of a prime of L) count the children open w.r.t. all M | L*q; print
(bits of L, min #open, argmin q, #children); if min = 0 the dive ends ('closed'), else continue with a random
open child of a random argmin split (ties broken by smaller open fraction).
"""
import sys, time, random
from math import gcd
from sympy import primerange
from m13d_wit import Engine

E = Engine()
Pm, maxsteps = int(sys.argv[2]), int(sys.argv[3])
random.seed(int(sys.argv[4]))
PR = list(primerange(2, Pm))
for k, line in enumerate(open(sys.argv[1])):
    x, L = map(int, line.split(':'))
    if E.query(x, L):
        print("start covered", flush=True); continue
    for step in range(maxsteps):
        t0 = time.time(); best = None
        for p in PR:
            L2 = L * p; rq = p
            while L2 % (rq * p) == 0: rq *= p
            if L2.bit_length() > 124: continue
            Y = [y for y in ((x + L * t) % L2 for t in range(p)) if gcd(y, p) == 1]
            op = []
            for y in Y:
                if not E.query(y, L2, rq):
                    op.append(y)
                    if best is not None and len(op) > best[0][0]: break
            key = (len(op), len(op) / len(Y))
            if best is None or key < best[0]:
                best = (key, rq, L2, op, len(Y))
        (o, fr), rq, L2, op, ny = best
        print(f"dive {k} step {step} bits {L.bit_length()} minopen {o} q {rq} n {ny} t {time.time()-t0:.0f}s", flush=True)
        if o == 0:
            print(f"dive {k} closed", flush=True); break
        x, L = random.choice(op), L2
    else:
        print(f"dive {k} maxsteps", flush=True)
