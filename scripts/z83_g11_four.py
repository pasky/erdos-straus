"""Certified simplex charge with all 4 variables explicit: via the exact
H recurrence, not a Monte Carlo simplex sample. Compare in *fixed* row-A units."""
from fractions import Fraction as Q
import z82_gap11_r2_cert as z
S=z.S
prev=[S]*(z.T+1)
for h in range(1,5):
    cur=[0]*(z.T+1)
    for i in range(h*z.N,z.T):cur[i+1]=cur[i]+z.down(z.W[i-z.N][0],prev[i-z.N])
    prev=cur
b0=Q(7,100);a=Q(1453,4000);p=Q(1999,4000);r=a*b0*2/p
l=Q(3,2)*Q(z.El,S)*2/p*Q(z.sq(r.numerator,r.denominator),S)
u=Q(3,2)*Q(z.Eu,S)*2/p*Q(z.sq(r.numerator,r.denominator)+1,S)
for b in (b0,Q(187,1000),Q(188,1000),Q(189,1000)):
    n=z.N*b.denominator;k=b.numerator;lo=prev[n//k];hi=z.Hhi[4][z.ceildiv(n,k)];print(b,'H and Pan C4 in fixed A units (outward, scale 1e12)',lo,hi,int(lo*l),z.ceildiv((hi*u).numerator,(hi*u).denominator))
