# z57 BFII: statistics of exact Type II counts (from z57_bfii_enum.c output).
import sys, numpy as np
def load(path):
    with open(path,'rb') as f:
        X=int(np.frombuffer(f.read(8),dtype=np.int64)[0])
        arr=np.frombuffer(f.read(),dtype=np.uint32).reshape(5,X+1)
    return X,arr
X,A=load(sys.argv[1]); tot,c1,prim,cmax,emin=[a.astype(np.int64) for a in A]
sieve=np.ones(X+1,bool); sieve[:2]=False
for i in range(2,int(X**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
n=np.arange(X+1)
P1=np.where(sieve&(n%4==1))[0]; P3=np.where(sieve&(n%4==3))[0]
odd=n[(n%2==1)&(n>1)]
sq=np.array([m*m for m in range(3,int(X**0.5)+1,2)])
print("X",X)
print("odd squares: max tot",tot[sq].max(),"(count",len(sq),")")
print("odd n>1 with tot==0:",int((tot[odd]==0).sum()),"of which squares:",int(np.isin(odd[tot[odd]==0],sq).sum()))
z=odd[tot[odd]==0]; nonsq=z[~np.isin(z,sq)]
print("  non-square odd n with no Type II N-point (first 30):",nonsq[:30].tolist(), "count",len(nonsq))
for name,P in (("p=1(4)",P1),("p=3(4)",P3)):
    print(name,"count",len(P),"min tot",tot[P].min(),"min prim",prim[P].min(),"#c1==0",int((c1[P]==0).sum()))
    if (c1[P]==0).sum(): print("   last p with R(p)=c1=0:",P[c1[P]==0][-5:].tolist(),"tot there",tot[P[c1[P]==0][-5:]].tolist())
    print("   max emin over p:",emin[P].max(),"at",P[np.argmax(emin[P])])
# normalized
L=np.log(P1.astype(float))
for lo,hi in [(1e3,1e4),(1e4,1e5),(1e5,1e6),(1e6,1e7)]:
    m=(P1>=lo)&(P1<hi)
    if m.sum()==0: continue
    t=tot[P1[m]]; l=L[m]; pr=prim[P1[m]]; cc=c1[P1[m]]
    print(f"[{lo:.0e},{hi:.0e}) N={m.sum()} mean tot/L^3={np.mean(t/l**3):.4f} mean prim/L^3={np.mean(pr/l**3):.4f} mean c1/L^2={np.mean(cc/l**2):.4f}"
          f" min tot/L^3={np.min(t/l**3):.4f} min tot={t.min()} at p={P1[m][np.argmin(t)]}  var/mean(tot)={np.var(t)/np.mean(t):.2f}"
          f" frac c>=2 ={1-cc.sum()/t.sum():.3f}")
# the smallest counts overall
idx=np.argsort(prim[P1])[:15]
print("15 smallest prim among p=1(4):",[(int(P1[i]),int(prim[P1[i]]),int(c1[P1[i]])) for i in idx])
# among large p: smallest normalized
m=P1>1e5
t=prim[P1[m]]/L[m]**3; idx=np.argsort(t)[:10]
print("10 smallest prim/L^3 for p>1e5:",[(int(P1[m][i]),int(prim[P1[m][i]]),round(float(t[i]),4)) for i in idx])
