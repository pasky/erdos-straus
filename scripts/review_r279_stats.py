import sys
import math
rows=[];sq=[]
for l in open(sys.argv[1]):
    s=l.split()
    if s[0]=='SQ': sq.append((int(s[1]),int(s[2]))); continue
    rows.append((int(s[0]),int(s[1]),float(s[2]),float(s[3])))
print("squares",len(sq),"nonzero R",sum(1 for n,r in sq if r))
print("primes",len(rows))
L=lambda p: math.log(p)
mn=min(rows,key=lambda r:r[3]/L(r[0])**2); print("min MBM/L^2",mn, mn[3]/L(mn[0])**2)
for lo,hi in [(5,100),(100,1000),(1000,10**4),(10**4,10**5),(10**5,10**6)]:
    sub=[r for r in rows if lo<=r[0]<hi]
    v=[r[3]/L(r[0])**2 for r in sub]; v0=[r[2]/L(r[0])**2 for r in sub]
    print(lo,hi,len(sub),"min %.4f mean %.4f  M0/L2 mean %.4f"%(min(v),sum(v)/len(v),sum(v0)/len(v0)))
big=[r for r in rows if r[0]>5e5]; print("mean MBM/L2 p>5e5 %.4f"%(sum(r[3]/L(r[0])**2 for r in big)/len(big)))
fails=[r for r in rows if r[1]==0]; print("R=0 primes",len(fails),[ (r[0],round(r[3],2)) for r in fails])
p1=[r for r in rows if r[0]%4==1 and 3e5<=r[0]<1e6]
print("p=1(4) [3e5,1e6)",len(p1),"R>2M",sum(r[1]>2*r[3] for r in p1),"R<M/2",sum(r[1]<r[3]/2 for r in p1),
  "max X/M %.2f"%max((r[1]-r[3])/r[3] for r in p1), "min z %.2f"%min((r[1]-r[3])/math.sqrt(2*r[3]) for r in p1))
for P in [131,241,409,17,102001,712321]:
    r=[x for x in rows if x[0]==P][0]; print(P,r, "MBM/L2 %.4f"%(r[3]/L(P)**2))
