#!/usr/bin/env python3
"""z66 HSTARF, Prop. 3.2 caveat: verify that PSL2(F_19) has a generating pair of orders (2,5) with product of order 10
(signature (2,5,10), sum 4/5, Type II) and PSL2(F_41) one of orders (2,4) with product of order 20 (signature (2,4,20),
sum 4/5, Type I). Orders by iteration, generation by BFS over the whole group (|PSL2(F_l)| = l(l^2-1)/2).
usage: uv run scripts/z66_hstarf_psl2.py"""
def check(l, x, y):
    def mul(A,B): return tuple((A[i][0]*B[0][j]+A[i][1]*B[1][j])%l for i in range(2) for j in range(2))
    def norm(M):
        M=tuple(M)
        for s in (1,l-1):
            N=tuple((s*v)%l for v in M)
            if N[0] and N[0]<=(l-1)//2: return N
            if N[0]==0 and N[1]<=(l-1)//2: return N
        return M
    I=norm((1,0,0,1))
    def tomat(T): return ((T[0],T[1]),(T[2],T[3]))
    def order(T):
        P=T; k=1
        while norm(P)!=I: P=mul(tomat(P),tomat(T)); k+=1
        return k
    X=norm(x); Y=norm(y); XY=norm(mul(tomat(X),tomat(Y)))
    seen={I}; frontier=[I]
    while frontier:
        nf=[]
        for g in frontier:
            for h in (X,Y):
                p=norm(mul(tomat(g),tomat(h)))
                if p not in seen: seen.add(p); nf.append(p)
        frontier=nf
    return dict(orders=(order(X),order(Y),order(XY)), generated=len(seen), group_order=l*(l*l-1)//2)
print("PSL2(F_19), x=[[0,1],[18,0]], y=[[1,1],[12,13]]:", check(19,(0,1,18,0),(1,1,12,13)))
print("PSL2(F_41), x=[[0,1],[40,0]], y=[[0,6],[34,17]]:", check(41,(0,1,40,0),(0,6,34,17)))
