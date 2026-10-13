# CERTIFICATE: every n = 2^m - 2 with m odd, m >= 11 is a value of xyz - x - z (x,y,z >= 2).
# Greedy covering of odd m mod 36 by fixed-pair families; explicit (x,y,z) verified with exact integers for all odd m <= 4001.
from math import gcd
L=36; D=20000
def info(d,c):
    s=0; dd=d
    while dd%2==0: dd//=2; s+=1
    if (c+2)%(2**s): return None
    o=1; v=2%dd if dd>1 else 0
    if dd>1:
        while v!=1:
            v=v*2%dd; o+=1
            if o>L: return None
    if L%o: return None
    t=(c+2)%dd
    ms={m for m in range(L) if pow(2,m,dd)==t%dd} if dd>1 else set(range(L))
    ms={m for m in ms if (m-min(ms))%o==0 or True}
    return s,o,ms
fams=[]
for x in range(2,D):
    for y in range(2,D):
        d=x*y-1
        if d>D: break
        r=info(d,(-x)%d)
        if r: fams.append(('xy',x,y,d,r))
    for z in range(x,D):
        d=x*z
        if d>D: break
        r=info(d,(-(x+z))%d)
        if r: fams.append(('xz',x,z,d,r))
unc=set(range(1,L,2)); chosen=[]
while unc:
    best=max(fams,key=lambda f:(len(unc&f[4][2]),-f[3]))
    got=unc&best[4][2]
    if not got: raise SystemExit("no cover")
    chosen.append(best); unc-=got
for f in chosen: print(f[0],"(%d,%d)"%(f[1],f[2]),"modulus",f[3],"covers odd m mod 36 in",sorted(set(range(1,36,2))&f[4][2]),"needs m >=",f[4][0])
def sol(m):
    n=2**m-2
    for ty,a,b,d,(s,o,ms) in chosen:
        if m%L in ms and m>=s and (n-((-a)%d if ty=='xy' else (-(a+b))%d))%d==0:
            if ty=='xy': x,y,z=a,b,(n+a)//d
            else: x,z=a,b; y=(n+x+z)//(x*z)
            if min(x,y,z)>=2 and x*y*z-x-z==n: return (x,y,z)
    return None
bad=[m for m in range(11,4002,2) if sol(m) is None]
print("odd m in [11,4001] without explicit family solution:",bad)
