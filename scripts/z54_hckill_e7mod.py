# z54 HCKILL: residues of E7 points (U,W) and of A' = (U^2-W^2 with 2,3,5 removed) mod 4: is there a congruence obstruction to integral admissibility?
import cypari2, math
from fractions import Fraction
pari=cypari2.Pari(); pari.allocatemem(10**9)
E=pari.ellinit([0,532,0,-1599360,553190400]); H=pari('[480,-4320]')
tg=pari.elltors(E)[2]; T=[pari('[0]'),tg[0],tg[1],pari.elladd(E,tg[0],tg[1])]
c3=-672
seen={}
for n in range(-20,21):
  for t in T:
    P=pari.elladd(E,pari.ellmul(E,H,n),t)
    if P==pari('[0]'): continue
    X=Fraction(int(pari.numerator(P[0])),int(pari.denominator(P[0])))
    z=X/c3
    if z==0: continue
    m=1+1/z; nn,dd=m.numerator,m.denominator
    U=abs(4*(5*nn*nn-5*nn*dd-dd*dd)); W=5*nn*nn+dd*dd; g=math.gcd(U,W); U//=g; W//=g
    if (U,W) in seen: continue
    A=U*U-W*W; B=16*W*W-U*U
    real = A>0 and B>0
    Ap=abs(A)
    for q in (2,3,5):
        while Ap%q==0: Ap//=q
    seen[(U,W)]=(n,real,Ap%4, U%8, W%8, U%3, W%3, U%5, W%5)
for k,v in sorted(seen.items(), key=lambda kv: abs(kv[1][0])):
    print("n=%d real=%s A'mod4=%d U,W mod8=(%d,%d) mod3=(%d,%d) mod5=(%d,%d)"%v)
