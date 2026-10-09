"""For sample open nodes: complete-engine count of open children for EVERY split q (primes < Pm, or the next
power of a prime dividing L).  Prints per node: open?, min #open children, the argmin splits, time.
usage: m13d_minopen.py nodes.txt Pm   (nodes.txt: lines x:L)"""
import sys, time
from math import gcd
from sympy import primerange
from m13d_wit import Engine
E = Engine()
Pm = int(sys.argv[2])
for line in open(sys.argv[1]):
    x, L = map(int, line.split(':')); t0 = time.time()
    if E.query(x, L):
        print("covered", x, L, flush=True); continue
    res = []
    for p in primerange(2, Pm):
        L2 = L * p; rq = p
        while L2 % (rq * p) == 0: rq *= p
        Y = [y for y in ((x + L * t) % L2 for t in range(p)) if gcd(y, p) == 1]
        o = 0
        for y in Y:
            if not E.query(y, L2, rq):
                o += 1
        res.append((o, rq, len(Y)))
    m = min(r[0] for r in res)
    print("node", x, L, "minopen", m, [(r[1], r[2]) for r in res if r[0] == m], f"{time.time()-t0:.0f}s", flush=True)
