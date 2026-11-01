# z52d pass2 TO1 (Z0282): local counts N_k(p) = #{(x,y,z) mod p^k : 4xyz == p(xy+yz+zx) mod p^k} for the ES surface 4/p = 1/x+1/y+1/z.
# usage: python3 scripts/z52d_p2_TO1_padic.py   (pure python, brute force; small p^k only)
from fractions import Fraction
def count(p,k):
    m=p**k; c=0
    for x in range(m):
        for y in range(m):
            # solve for z: z*(4xy - p(x+y)) == p*x*y  (mod m)
            A=(4*x*y - p*(x+y))%m; Bv=(p*x*y)%m
            # count z with z*A == Bv mod m
            from math import gcd
            g=gcd(A,m)
            if Bv%g==0:
                c+=g  # number of solutions z mod m is g when g|Bv (A,m)
    return c
for p,ks in [(5,[1,2,3]),(13,[1,2]),(17,[1,2]),(3,[1,2,3])]:
    out=[]
    for k in ks:
        N=count(p,k); m=p**k
        out.append((k,N, N/m**2))   # density normalised by m^2 (surface of dim 2 in A^3)
    print("p=",p, [(k,N, round(d,4)) for k,N,d in out])
