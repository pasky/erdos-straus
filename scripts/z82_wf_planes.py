"""Exhaust integral z-weights k' through Q at u=1, not just small k'.
Uses z80 proven-factor ET enumeration, z81 point conversion. Replay ENV in note.
"""
from itertools import permutations
from z81_dual_family import pts

for p,k in zip((409,577,2521,3361,102001,8813281),(8219,11579,15137,20177,1632047,141012527)):
    points=pts(p);b=(p+1)//2;g=p*b;j=p+2;Z=(k*g+1)//j;good=set();mx=0
    for P in points:
        for x,y,z in permutations(P):
            if x>y:continue
            S=x+y-b;D=j*z-g;M=j*S-g
            R=g*g-M*D
            assert D!=0 and R!=0 and k*D!=1
            if R%(k*D-1)==0:
                m,r=divmod(M-k*g*g,k*D-1);assert r==0
                assert x+y-m*k*z==b+g*Z-m*Z
                good.add((m,x,y,z))
            mx=max(mx,abs(M)+(g*g+1)//abs(D))
    print('p',p,'k',k,'unordered',len(points),'all signed-integer kprime/k hits',sorted(good),'individual upper bound',mx,flush=True)
