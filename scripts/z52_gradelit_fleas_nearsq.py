# Near-square multiplicity profile in the Alkauskas flea orbit (integer areas A = s/2), cf. QUESTION_R §3.2 for ES.
import sys, math
from collections import Counter
sys.setrecursionlimit(10000)
exec(open('scripts/z52_gradelit_fleas.py').read().split("X=int(sys.argv[1])")[0])
X=int(sys.argv[1])
G=((0,0),(2,1),(3,2))
starts=[G]+[jump(G,i,outward=False) for i in range(3)]
cnt=Counter()
for S in starts:
    stack=[S]
    while stack:
        T=stack.pop(); s=area2(*T)
        if s>X: continue
        cnt[s]+=1
        for i in range(3): stack.append(jump(T,i,True))
Amax=X//2; Amin=Amax//4
# local normaliser: mean multiplicity of integer areas in a window, by A mod 8 class (local densities differ by residue)
import statistics
def mult(A): return cnt[2*A]
base={}
MOD=int(sys.argv[2]) if len(sys.argv)>2 else 8
for r in range(MOD):
    vals=[mult(A) for A in range(Amin,Amax) if A%MOD==r]
    base[r]=statistics.mean(vals)
print("X",X,"A in",(Amin,Amax),"MOD",MOD,"class-mean range",round(min(base.values()),2),round(max(base.values()),2))
for K in [-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,12,16,25]:
    rs=[mult(m*m+K)/base[(m*m+K)%MOD] for m in range(math.isqrt(Amin)+1, math.isqrt(Amax-K)) if Amin<=m*m+K<Amax and base[(m*m+K)%MOD]>0]
    if rs: print(f"K={K:+d} n={len(rs)} mean_ratio={statistics.mean(rs):.3f} sd/sqrt(n)={statistics.pstdev(rs)/len(rs)**0.5:.3f}")
