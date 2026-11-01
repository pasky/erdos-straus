import sys
sys.path.insert(0,'scripts')
from z52d_p2_TO0b_ff import *
def verify(p,A,P,X,Y,Z,H):
    f=F(p)
    lhs=f.mul(f.mul(A,X),f.mul(Y,Z))
    rhs=f.mul(P,f.add(f.add(f.mul(X,Y),f.mul(Y,Z)),f.mul(X,Z)))
    return lhs==rhs and all(T[-1] in H for T in (X,Y,Z))
for p,n in [(5,2),(5,3),(7,2),(7,3)]:
    H={(x*x)%p for x in range(1,p)}
    A=str2poly("10"); ok=0; tot=0; ex=[]
    for P in monic_irreducibles(p,n):
        r,w=exists_general(p,A,P,H=H,return_witness=True)
        if r:
            tot+=1; ok+=verify(p,A,P,*w,H)
            if len(ex)<2: ex.append((s2str(P),[s2str(t) for t in w]))
    print(p,n,'witnesses verified',ok,'/',tot, ex)
