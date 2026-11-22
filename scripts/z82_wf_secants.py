"""Skew pencil certificates at the squarescreen panel; elementary 2-descent
for the one symmetric hit. Enumerate only known positive points (compatibility).
"""
from fractions import Fraction as F
from itertools import permutations
from math import isqrt,gcd
from z81_dual_family import pts
from z82_wf_fibres import image
from z82_wf_chords import third

def skew(p,R,T):
    # Pair of linear forms cuts out each surface line: their two-column
    # evaluation determinant must not vanish. Coordinates ordered x,y,z,v.
    def restrictions(P):
        v=(*P,1)
        return [ (v[i],v[j]) for i in range(4) for j in range(i) ]+[(4*P[i]-p,P[(i+1)%3]+P[(i+2)%3]) for i in range(3)]
    return all(a*d!=b*c for (a,b),(c,d) in zip(restrictions(R),restrictions(T)))

for p in (409,577,2521,3361,102001,8813281):
    b=(p+1)//2;g=p*b;W=tuple(map(F,(b,g,F(p,2))));cnt=0;first=None
    for t in sorted(pts(p)):
        for T in permutations(t):
            if skew(p,W,T) and (r:=third(p,W,T)) not in (None,W,T):
                cnt+=1
                if first is None:first=T
    print('p',p,'ordered nondegenerate skew',cnt,'example',first)

p=8813281;b=(p+1)//2;W=(F(b),F(p*b),F(p,2));T=tuple(map(F,(9253945050,194231052654450,2203845)));w=70548236
K=sum(W[:2])+w*W[2];assert K==sum(T[:2])+w*T[2]
N=4*K/p; A=(N-w)**2-4*(N+w); B=16*w*N; discr=A*A-4*B
assert discr!=0 and (discr<0 or isqrt(discr.numerator*discr.denominator)**2!=discr.numerator*discr.denominator)
u,v=4*w,4*w*(N-w); classes=[]
for R in (W,T):
    x,y=image(R,-w,N);assert y*y==x*(x*x+A*x+B)
    s=((y+v)/(x-u))**2-A-x-u;classes.append(s)
classes.append(B);rows=[]
for l in (17,23,29):
    row=[pow(c.numerator*c.denominator%l,(l-1)//2,l) for c in classes]
    assert set(row)<={1,l-1}; rows.append(sum(1<<i for i,v in enumerate(row) if v!=1))
assert all(any((r&c).bit_count()%2 for r in rows) for c in range(1,8))
print('symmetric X squareclasses',classes,'row masks',rows,'skew',skew(p,W,T))
