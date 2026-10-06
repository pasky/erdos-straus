"""R80: all ET Prop 1.9 classes with modulus dividing L; list Mordell-hard unit residues mod L
not in any of them.  Used (i) to compare with Salez's sieve count #R_4 = 192 at G_4 = 120120
(arXiv:1406.6307 Sec. 4.1), (ii) to see whether Thm 3.1's exception list is already minimal
over ALL classes of modulus | L (not just the certificate).  usage: review_mordell_level.py L"""
import sys
from math import gcd
from sympy import divisors

L = int(sys.argv[1]); D = divisors(L)
units = [t for t in range(1, L) if gcd(t, L) == 1]
def hard(t):
    return t % 24 == 1 and pow(t, 2, 5) == 1 and pow(t, 3, 7) == 1
H = [t for t in units if hard(t)]
# conditions as functions (residue t mod L) -> bool, grouped by modulus M | L
conds = []
for M in D:
    if M % 4: continue
    m = M // 4
    for a in divisors(m):
        d = m // a                                        # I1, II1/I4 (a,b=d), II3 needs 3 factors
        for f in divisors(4*a*a*d+1):
            conds.append(('I1', (a, d, f), M, lambda t, M=M, f=f: (t+f) % M == 0))
        b = d
        for e in divisors(a+b):
            if gcd(e, M) == 1:
                conds.append(('I4', (a, b, e), M, lambda t, M=M, e=e: (t*e+1) % M == 0))
                conds.append(('II1', (a, b, e), M, lambda t, M=M, e=e: (t+e) % M == 0))
        for dd in divisors(d):                           # II3: M = 4 a dd e
            e = d // dd
            if gcd(4*a*dd, e) == 1:
                conds.append(('II3', (a, dd, e), M, lambda t, M=M, a=a, dd=dd, e=e: (t+4*a*a*dd+e) % M == 0))
        # I2 (a,c,f), I3 (c,d,f): M = 4 u v f with gcd(4uv,f)=1
        for v in divisors(d):
            f = d // v; u = a
            if gcd(4*u*v, f) != 1: continue
            conds.append(('I2', (u, v, f), M, lambda t, u=u, v=v, f=f: (t+f) % (4*u*v) == 0 and (u*t+v) % f == 0))
            conds.append(('I3', (u, v, f), M, lambda t, u=u, v=v, f=f: (t+f) % (4*u*v) == 0 and (t*t+4*u*u*v) % f == 0))
for f in D:                                               # II2: modulus f, 4ad | f+1
    if (f+1) % 4: continue
    q = (f+1)//4
    for a in divisors(q):
        for d in divisors(q//a):
            conds.append(('II2', (a, d, f), f, lambda t, a=a, d=d, f=f: (t+4*a*a*d) % f == 0))
unc = [t for t in H if not any(c[3](t) for c in conds)]
leg = lambda t, p: pow(t, (p-1)//2, p)
print(f'L={L} classes={len(conds)} hard={len(H)} uncovered={len(unc)}')
nr13 = [t for t in unc if leg(t, 13) == 12] if L % 13 == 0 else []
print('uncovered with (t/13)=-1:', len(nr13), nr13[:20])
if L % 11 == 0 and L % 13 == 0:
    print('  of which (t/11)=+1:', [t for t in nr13 if leg(t, 11) == 1])
