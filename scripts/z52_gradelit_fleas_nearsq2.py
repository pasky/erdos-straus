# Height-matched near-square profile in the Alkauskas flea orbit (positive-word multiplicities; the start congruent
# to G is not duplicated).  r(A) = mult(A)/A^beta (beta fitted), class means of r by A mod MOD, ratio at A = m^2+K.
import sys, math, statistics
from collections import Counter
exec(open('scripts/z52_gradelit_fleas.py').read().split("X=int(sys.argv[1])")[0])
X=int(sys.argv[1]); MOD=int(sys.argv[2])
G=((0,0),(2,1),(3,2))
starts=[G]+[T for T in (jump(G,i,outward=False) for i in range(3)) if area2(*T)!=1]
cnt=Counter()
for S in starts:
    stack=[S]
    while stack:
        T=stack.pop(); s=area2(*T)
        if s>X: continue
        cnt[s]+=1
        for i in range(3): stack.append(jump(T,i,True))
Amax=X//2; Amin=Amax//4
xs=[];ys=[]
for b in range(20):
    lo=Amin+b*(Amax-Amin)//20; hi=Amin+(b+1)*(Amax-Amin)//20
    xs.append(math.log((lo+hi)/2)); ys.append(math.log(statistics.mean(cnt[2*A] for A in range(lo,hi))))
mx=statistics.mean(xs); my=statistics.mean(ys)
beta=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
r=lambda A: cnt[2*A]/A**beta
base={c:statistics.mean(r(A) for A in range(Amin+((c-Amin)%MOD),Amax,MOD)) for c in range(MOD)}
print(f"X={X} MOD={MOD} beta={beta:.3f} starts_s={[area2(*S) for S in starts]}")
for K in [-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,12,16,24,25]:
    rs=[r(m*m+K)/base[(m*m+K)%MOD] for m in range(math.isqrt(Amin)+1, math.isqrt(Amax-K)) if Amin<=m*m+K<Amax]
    print(f"K={K:+d} n={len(rs)} mean_ratio={statistics.mean(rs):.3f} se={statistics.pstdev(rs)/len(rs)**0.5:.3f}")
