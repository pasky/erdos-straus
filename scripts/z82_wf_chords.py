"""Fix R=Q or W and a positive integral T. Exact third intersections of the
proper lines R,T. Census is complete only relative to the z80 ET input list.
"""
from fractions import Fraction as F
from itertools import permutations
from math import lcm
from z81_dual_family import pts

def third(p,R,T):
    U=tuple(F(t-r) for t,r in zip(T,R));assert all(U)
    c=F(p,4)*sum(1/u for u in U)-sum(r/u for r,u in zip(R,U))-1
    A=tuple(r+c*u for r,u in zip(R,U))
    if not all(A):return None
    assert sum(1/a for a in A)==F(4,p)
    return A

if __name__=='__main__':
    for p,k in zip((409,577,2521,3361,102001,8813281),(8219,11579,15137,20177,1632047,141012527)):
        b=(p+1)//2;g=p*b;Z=(k*g+1)//(p+2);points=pts(p)
        for label,R in [('Q',(F(b),F(g*Z),F(Z,k))),('W',(F(b),F(g),F(p,2)))]:
            cnt=naxis=0;mint=None;best=None
            for t in points:
                for T in permutations(t):
                    A=third(p,R,T)
                    if A is None:naxis+=1;continue
                    den=lcm(*(a.denominator for a in A));cnt+=1
                    if mint is None or den<mint:mint=den;best=(T,A)
            print(p,label,'finite off axes',cnt,'axis',naxis,'smallest joint den of third input',mint,'best',best if mint==1 else None)
