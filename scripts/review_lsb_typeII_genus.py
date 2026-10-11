# R136: for each Type II quadruple (a,b,c,d) at prime p (4abcd = a+b+pc), form Q=[e,4ad,df] (e=(a+b)/c, f=4acd-1),
# disc -4dp, and evaluate chi_{-4d}(Q). Does every Type II point land in G^-_d? Also tabulate F_d(p) vs (d/p).
from math import gcd
import sys
sys.path.insert(0,'scripts')
from review_lsb_genus import jacobi, chi
def quads(d,n):
    out=[]; a=1
    while 4*a*d-1<=n+a:
        for b in range(1,(n+a)//(4*a*d-1)+1):
            t=4*a*b*d-n
            if t>0 and (a+b)%t==0: out.append((a,b,(a+b)//t))
        a+=1
    return out
from sympy import primerange
stats={}
for p in [q for q in primerange(1000,6000) if q%4==1][:60]:
    for d in range(1,9):
        Qs=quads(d,p); leg=jacobi(d,p)
        chis=set()
        for (a,b,c) in Qs:
            e=(a+b)//c; f=4*a*c*d-1
            for Q in [(e,4*a*d,d*f),(f,4*a*d,d*e)]:   # e-form (non-canonical) and O128's f-form
                g=gcd(gcd(Q[0],Q[1]),Q[2])
                chis.add((Q[0]==f, g, chi(d,Q,4*d*p) if g==1 else None))
        key=(d,leg); s=stats.setdefault(key,[0,0,set()]); s[0]+=1; s[1]+=(len(Qs)>0); s[2]|=chis
for k in sorted(stats): print("d,(d/p)=",k," #p:",stats[k][0]," #p with F>0:",stats[k][1]," (gcd,chi) seen:",stats[k][2])
