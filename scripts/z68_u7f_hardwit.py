#!/usr/bin/env python3
"""z68 U7F: for given primes p (args or the NOPRIME list in a wit_*.txt), list ALL U7 witnesses f <= 2p+1 with
omega(f) <= 2 (and all witnesses up to a bound), with factorisation, Legendre symbols (p/q) of the prime factors,
the word (x,y,z), and the least prime non-residue n_p of p (and least nonresidue = 7 mod 8).
usage: hardwit.py [--all] p1 p2 ...   |  hardwit.py --file data/z68/u7f/wit_1e8.txt.gz [--max K]
"""
import sys, gzip
from sympy import factorint, isprime, primerange
from sympy import jacobi_symbol as legendre_symbol

def least_nonres(p, cond=lambda q: True):
    for q in primerange(3, 10**6):
        if cond(q) and legendre_symbol(p, q) == -1:
            return q

def witnesses(p, fmax=None, om_max=2):
    out = []
    F = 2 * p + 1 if fmax is None else fmax
    for f in range(7, F + 1, 8):
        r = (-p) % f
        if r == 0 or (f + 1) % r: continue
        fa = factorint(f)
        if len(fa) > om_max: continue
        out.append((f, r, fa))
    return out

args = sys.argv[1:]
ps = []
if args and args[0] == '--file':
    opener = gzip.open if args[1].endswith('.gz') else open
    with opener(args[1], 'rt') as fh:
        for line in fh:
            if line.startswith('NOPRIME'):
                ps.append(int(line.split()[1].split('=')[1]))
    args = args[2:]
else:
    ps = [int(a) for a in args if a.isdigit()]
K = 4
if '--max' in args: K = int(args[args.index('--max') + 1])

for p in ps:
    assert isprime(p) and p % 8 == 1
    np_ = least_nonres(p); np7 = least_nonres(p, lambda q: q % 8 == 7)
    ws = witnesses(p)
    print(f"p={p} p%840={p%840} n_p={np_} n_p^(7)={np7} #wit(om<=2)={len(ws)}")
    for f, r, fa in ws[:K]:
        s = (f + 1) // r; t = (p + r) // f
        syms = {q: legendre_symbol(p, q) for q in fa}
        print(f"   f={f}={fa} (p/q)={syms} r=x={r} y={s} z={t}  x+z mod 8={(r+t)%8}")
