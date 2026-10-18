"""R272 from-scratch recomputation of CLASS_FORCING §7 tiers (b=1 line, levels d<=D).
A: exists d<=D, w | n+4d, w == -1 (mod 4d).   Gen: -1 in <prime factors of n+4d> (mod 4d).
F_B: -1 in Sigma(s) ∪ Sigma(s)*[L], s = B-smooth part, L = rest (opaque).
X2: d in {1,2,3,6} actual; c-line c in {1,2,3,6}: w | cn+1, w == -1 (mod 4c);
    e=3 Type II N=(n+3)/4 and Type I N=(3n+1)/4: exist a,b, ab|N, 3 | a+b.
Usage: census.py NMAX D"""
import sys
import numpy as np
from fractions import Fraction as Fr
NMAX, D = int(sys.argv[1]), int(sys.argv[2])
LIM = 6*NMAX + 8
spf = np.zeros(LIM+1, dtype=np.int32)
for i in range(2, int(LIM**0.5)+1):
    if spf[i] == 0:
        blk = spf[i*i::i]; blk[blk == 0] = i
def fac(n):
    out = {}
    while n > 1:
        q = int(spf[n]) or n
        out[q] = out.get(q, 0)+1; n //= q
    return out
def divs(f):
    ds = [1]
    for q, e in f.items(): ds = [x*q**k for x in ds for k in range(e+1)]
    return ds
def tierA(N, t):
    return any(w % t == t-1 for w in divs(fac(N)))
def tierGen(N, t):
    gens = [q % t for q in fac(N) if t % q]
    H = {1}; fr = [1]
    while fr:
        y = fr.pop()
        for g in gens:
            z = y*g % t
            if z not in H: H.add(z); fr.append(z)
    return t-1 in H
def tierF(N, t, B):
    f = fac(N); s = {q: e for q, e in f.items() if q <= B}
    S = 1
    for q, e in s.items(): S *= q**e
    L = N//S
    return any(u % t == t-1 or (u*L) % t == t-1 for u in divs(s))
def signed3(N):
    ds = divs(fac(N)); dset = set(ds)
    return any((a+b) % 3 == 0 for a in ds for b in ds if N % (a*b) == 0)
def tiers(n):
    r = {}
    r['A'] = next((d for d in range(1, D+1) if tierA(n+4*d, 4*d)), None)
    r['Gen'] = next((d for d in range(1, D+1) if tierGen(n+4*d, 4*d)), None)
    for B in (10, 30, 1000):
        r[f'F{B}'] = next((d for d in range(1, D+1) if tierF(n+4*d, 4*d, B)), None)
    x2 = any(tierA(n+4*d, 4*d) for d in (1, 2, 3, 6)) or \
         any(any(w % (4*c) == 4*c-1 for w in divs(fac(c*n+1)) if w % 2) for c in (1, 2, 3, 6)) or \
         signed3((n+3)//4) or signed3((3*n+1)//4)
    r['X2'] = x2
    return r
def verify(p, d):  # exact ES identity from an A-certificate
    t = 4*d; w = next(w for w in divs(fac(p+t)) if w % t == t-1)
    c = (w+1)//t; a = (p + (p+t)//w)//t
    x, y, z = a*d, a*c*d*p, c*d*p
    assert Fr(4, p) == Fr(1, x)+Fr(1, y)+Fr(1, z), (p, d, w)
isp = lambda n: n > 1 and (spf[n] == 0)
for label, pop in (("primes p=1(4)", [n for n in range(5, NMAX+1) if n % 4 == 1 and isp(n)]),
                   ("odd squares", [m*m for m in range(3, int(NMAX**0.5)+1, 2)])):
    fails = {k: [] for k in ('A', 'Gen', 'F10', 'F30', 'F1000', 'X2')}
    nver = 0
    for n in pop:
        r = tiers(n)
        for k, v in r.items():
            if not v: fails[k].append(n)
        if label.startswith("primes") and r['A']: verify(n, r['A']); nver += 1
    print(f"[{label}] count {len(pop)}, D={D}; exact ES verifications: {nver}")
    for k, v in fails.items(): print(f"  {k:6s} failures {len(v):5d} first {v[:8]} last {v[-3:]}")
    sys.stdout.flush()
