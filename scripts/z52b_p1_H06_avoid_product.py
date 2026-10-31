"""Z2433: largest product sets U x V x W ⊂ F_q^3 with no (u,B,C) satisfying 4uBC - u - B ≡ a (mod q), all a mod q.
Brute force over (U,V); W = complement of hit C's. Prints max |U||V||W| / q^3 and the trivial cube-free benchmark."""
import sys, itertools
for q in map(int, sys.argv[1:]):
    best={}
    for a in range(q):
        hit=[[0]*q for _ in range(q)]   # hit[u][B] = bitmask of C solving
        for u in range(q):
            for B in range(q):
                m=0
                for C in range(q):
                    if (4*u*B*C-u-B-a)%q==0: m|=1<<C
                hit[u][B]=m
        bv=0;arg=None
        for Um in range(1,1<<q):
            U=[u for u in range(q) if Um>>u&1]
            for Vm in range(1,1<<q):
                h=0
                for u in U:
                    for B in range(q):
                        if Vm>>B&1: h|=hit[u][B]
                w=q-bin(h).count('1')
                val=len(U)*bin(Vm).count('1')*w
                if val>bv: bv=val; arg=(U,[B for B in range(q) if Vm>>B&1],[C for C in range(q) if not h>>C&1])
        best[a]=(bv,round(bv/q**3,3),arg)
    for a in sorted(best): print('q=%d a=%d max|U||V||W|=%d (frac %.3f) e.g. %s'%(q,a,best[a][0],best[a][1],best[a][2]))
