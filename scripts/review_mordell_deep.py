"""R80: deep-level count.  Lift the 6 survivors mod 720720 (Thm 3.1(b)) to L = 720720*13*17*19*23
(units only) and remove those lying in an ET class with modulus M | L, M <= Mmax.
(Compare with POINTWISE_MORDELL §1/§3: 1438 at Mmax=1e7, 1412 at 1e8.)  usage: Mmax"""
import sys
import numpy as np
from math import gcd
from sympy import divisors, sqrt_mod

Mmax = int(float(sys.argv[1]))
L0 = 720720; EXC = [112561, 352801, 380881, 418321, 473761, 483841]
L = L0*13*17*19*23
# lifts: t = e + L0*k, k in [0, L/L0), unit mod 17,19,23 (13 automatic)
K = np.arange(L//L0, dtype=np.int64)
T = np.concatenate([e + L0*K for e in EXC])
T = T[(T % 17 != 0) & (T % 19 != 0) & (T % 23 != 0)]
print('targets', len(T), flush=True)
alive = np.ones(len(T), dtype=bool)
D = [M for M in divisors(L) if M <= Mmax]
def kill(M, resid):
    if not len(resid): return
    r = np.zeros(M, dtype=bool) if M <= 5*10**7 else None
    if r is not None:
        r[np.array(sorted(resid), dtype=np.int64)] = True
        alive[:] &= ~r[T % M]
    else:
        alive[:] &= ~np.isin(T % M, np.array(sorted(resid), dtype=np.int64))
for M in D:
    res = set()
    if M % 4 == 0:
        m = M//4
        for a in divisors(m):
            d = m//a
            for f in divisors(4*a*a*d+1): res.add((-f) % M)                    # I1
            for e in divisors(a+d):                                          # I4, II1 (b=d)
                if gcd(e, M) == 1: res.add((-pow(e, -1, M)) % M); res.add((-e) % M)
            for dd in divisors(d):                                           # II3
                e = d//dd
                if gcd(4*a*dd, e) == 1: res.add((-4*a*a*dd-e) % M)
            for v in divisors(d):                                            # I2 (a,c)=(a,v), I3 (c,d)=(a,v)
                f = d//v; m4 = 4*a*v
                if gcd(m4, f) != 1: continue
                # CRT n = -f mod m4 with n = -v/a mod f  (I2, needs gcd(a,f)=1 ok since gcd(4av,f)=1)
                r2 = (-v*pow(a, -1, f)) % f if f > 1 else 0
                for rr in ([r2] + [s % f for s in (sqrt_mod((-4*a*a*v) % f, f, all_roots=True) or [])] if f > 1 else [0]):
                    pass
                cands = [r2]
                if f > 1:
                    roots = sqrt_mod((-4*a*a*v) % f, f, all_roots=True) or []
                    cands += list(roots)
                else:
                    cands = [0]
                for rr in cands:
                    x = ((-f - rr) * pow(f, -1, m4)) % m4 if m4 > 1 else 0
                    res.add((rr + f*x) % M)
    if (M+1) % 4 == 0:                                                       # II2
        q = (M+1)//4
        for a in divisors(q):
            for d in divisors(q//a): res.add((-4*a*a*d) % M)
    kill(M, res)
print(f"Mmax={Mmax:g}: survivors {int(alive.sum())} of {len(T)}; density rel. to all (p/13)=-1 hard residues {alive.sum()/len(T)*6/2160:.3g}")
