# R136 from-scratch: growth exponent of #{g in PSL2(Z): max|coeff of (Q∘g, S∘g)| <= H} for the F4 pair
# Q=[3,4,11] (disc -4*29), S=[0,2,1] (disc 4). Doc claims ≍ H^2; lattice-point heuristics give ≍ H.
from math import gcd, isqrt
def comp(F,g):
    A,B,C=F; a,b,c,d=g  # F(ax+by, cx+dy)
    return (A*a*a+B*a*c+C*c*c, 2*A*a*b+B*(a*d+b*c)+2*C*c*d, A*b*b+B*b*d+C*d*d)
Q=(3,4,11); S=(0,2,1)
def count(H):
    n=0; R=isqrt(H)+2
    for a in range(-R,R+1):
        for c in range(-R,R+1):
            if gcd(a,c)!=1 or Q[0]*a*a+Q[1]*a*c+Q[2]*c*c>H: continue
            # one solution of a*d-b*c=1
            # extended gcd
            def eg(x,y):
                if y==0: return (1,0) if x>0 else (-1,0)
                u,v=eg(y,x%y); return (v,u-(x//y)*v)
            d0,mb0=eg(a,c)   # a*d0 + c*mb0 = 1  => b0 = -mb0
            b0=-mb0
            for t in range(-4*R-5,4*R+6):
                b=b0+t*a; d=d0+t*c
                g=(a,b,c,d)
                q=comp(Q,g); s=comp(S,g)
                if max(map(abs,q+s))<=H: n+=1
    return n//2   # ±g
import sys
for H in [250,500,1000,2000]:
    N=count(H); print(H,N,N/H)
