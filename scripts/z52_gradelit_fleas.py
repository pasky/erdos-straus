# Alkauskas 2508.05347 flea orbit: count positive-jump tree nodes with doubled area s <= X (multiplicity per target),
# and list missing integer areas (even s) up to X.  Geometric simulation: outward square on side AB moves A,B to
# A+n, B+n with n = rot90(B-A) pointing away from the third vertex; doubled area s -> s + |AB|^2.
import sys
def area2(P,Q,R): return abs((Q[0]-P[0])*(R[1]-P[1])-(Q[1]-P[1])*(R[0]-P[0]))
def jump(T,i,outward=True):
    A,B,C=T[i],T[(i+1)%3],T[(i+2)%3]
    d=(B[0]-A[0],B[1]-A[1]); n=(-d[1],d[0])
    side=(C[0]-A[0])*n[0]+(C[1]-A[1])*n[1]   # >0: n points towards C
    if (side>0)==outward: n=(-n[0],-n[1])
    return ((A[0]+n[0],A[1]+n[1]),(B[0]+n[0],B[1]+n[1]),C)
X=int(sys.argv[1])
G=((0,0),(2,1),(3,2))
starts=[G]+[jump(G,i,outward=False) for i in range(3)]
from collections import Counter
cnt=Counter(); nodes=0
for S in starts:
    stack=[S]
    while stack:
        T=stack.pop(); s=area2(*T)
        if s>X: continue
        cnt[s]+=1; nodes+=1
        for i in range(3): stack.append(jump(T,i,True))
even=[s for s in range(2,X+1,2)]
missing=[s//2 for s in even if cnt[s]==0 and int((s//2)**0.5)**2!=s//2]
sq_hit=[s//2 for s in even if cnt[s]>0 and int((s//2)**0.5)**2==s//2]
odd_missing=[s for s in range(1,X+1,2) if cnt[s]==0]
hit=sum(1 for s in range(1,X+1) if cnt[s]>0)
print(f"X={X} nodes={nodes} distinct_s={hit} avg_mult={nodes/hit:.2f} missing_nonsquare_int_areas={missing} squares_hit={sq_hit} odd_s_missing={odd_missing[:10]}")
