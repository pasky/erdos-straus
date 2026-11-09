"""z68 PC2 kill test K2: brute-force all solutions of 4XYZW = aX + bY + Z for a,b < A,B and check every case inequality of Lemma Q.
Usage: python3 scripts/z68_pc2_qcheck.py A B"""
# quick check of Lemma Q case analysis
import sys
from math import log
def sols(al,be):
    out=set()
    # case A: Y Z W <= 2al/3 ; case B: X Z W <= 2be/3
    lim=max(al,be)
    for Y in range(1,lim+1):
        for Z in range(1,lim//Y+1):
            for W in range(1,lim//(Y*Z)+1):
                P=4*Y*Z*W-al
                if P>0 and (be*Y+Z)%P==0:
                    X=(be*Y+Z)//P
                    out.add((X,Y,Z,W))
                R=4*Y*Z*W-be  # here Y plays X role
                if R>0 and (al*Y+Z)%R==0:
                    X2=(al*Y+Z)//R
                    out.add((Y,X2,Z,W))
    return out
worst=0
for al in range(1,int(sys.argv[1])):
    for be in range(1,int(sys.argv[2])):
        S=sols(al,be)
        T=(4*al*be/3)**0.4
        for (X,Y,Z,W) in S:
            assert 4*X*Y*Z*W==al*X+be*Y+Z
            E=4*X*Y*W-1; P=4*Y*Z*W-al; R=4*X*Z*W-be
            assert P>0 and R>0 and Z*E==al*X+be*Y and X*P==be*Y+Z and Y*R==al*X+Z
            assert E*P==al+4*be*Y*Y*W and E*R==be+4*al*X*X*W and P*R==al*be+4*Z*Z*W
            if al*X>=be*Y:
                assert al/4<Y*Z*W<=2*al/3
                q=[P,X*Y,Y*W,X*W] if Z>=be*Y else [P,X*Z,Z*W,X*W]
            else:
                assert be/4<X*Z*W<=2*be/3
                q=[R,X*Y,X*W,Y*W] if Z>=al*X else [R,Y*Z,Z*W,Y*W]
            assert min(q)<=T+1e-9,(al,be,X,Y,Z,W,q,T)
        if S: worst=max(worst,len(S)/(al*be)**0.4)
print("ok worst count/(ab)^0.4 =",worst)
