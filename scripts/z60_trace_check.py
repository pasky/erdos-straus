# Check the conjectured Theorem 2 formula against spectral traces (json from z60_trace_identity.py on stdin).
import json, sys
from fractions import Fraction
from math import isqrt
def mu(C):
    Q=4*C; m=Q**3
    p=2; x=Q
    ps=set()
    q=Q; d=2
    while d*d<=q:
        while q%d==0: ps.add(d); q//=d
        d+=1
    if q>1: ps.add(q)
    r=Fraction(m)
    for p in ps: r*=Fraction(p*p-1,p*p)
    return r/2   # [PSL2(Z):Gamma(Q)bar]
txt=sys.stdin.read(); txt=txt[txt.index('{'):]
d=json.loads(txt); C=d['C']; k=d['k']; Q=4*C; m=mu(C)
bad=0; tot=0
for n,N,T,E,ES,TR in d['rows']:
    T=Fraction(T); E=Fraction(E)
    g = -m*E - m/(2*Q)*(ES + (-1)**k*TR)
    if k==2: g += sum(dd for dd in range(1,N+1) if N%dd==0)   # k=2 Eisenstein correction sigma(N)
    r=isqrt(N)
    if r*r==N:
        for lam in (r,-r):
            if (lam+1)%Q==0: g += Fraction(k-1,12)*m*Fraction(lam)**(k-2)
    tot+=1
    if g!=T:
        bad+=1
        if bad<=8: print("MISMATCH",n,N,T,g,E,ES,TR)
print(f"C={C} k={k} dim={d['dim']} mu={m} rows={tot} mismatches={bad}")
sys.exit(1 if bad else 0)
