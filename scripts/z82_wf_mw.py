"""Exact rational additions, origin O on x-axis as in §4, followed by affine
normalization. Output joint and component denominators, sign sector, linkage.
"""
from fractions import Fraction as F
from math import lcm,gcd
from z82_wf_fibres import image

def run(p,k):
    b=(p+1)//2;g=p*b;Z=(k*g+1)//(p+2);Q=(F(b),F(g*Z),F(Z,k));W=(F(b),F(g),F(p,2))
    w=k*g*(p+1);K=sum(W[:2])+w*W[2];N=4*K/p; A=(N-w)**2-4*(N+w); B=16*w*N
    O=(F(4*w),4*w*(N-w));eQ=image(Q,-w,N);eW=image(W,-w,N)
    def add(P,R):
        if P is None:return R
        if R is None:return P
        x,y=P;u,v=R
        if x==u and y==-v:return None
        h=(v-y)/(u-x) if x!=u else (3*x*x+2*A*x+B)/(2*y)
        X=h*h-A-x-u;Y=h*(x-X)-y;assert Y*Y==X*(X*X+A*X+B);return X,Y
    def mul(n,P):
        if n<0:return mul(-n,(P[0],-P[1]))
        R=None
        for _ in range(n):R=add(P,R)
        return R
    counts={}; small=[];link=[]
    for i in range(-3,4):
        for j in range(-3+abs(i),4-abs(i)):
            R=add(mul(1-i-j,O),add(mul(i,eQ),mul(j,eW)))
            if R is None:proj=(0,0,1)
            elif R==(0,0):proj=(1,-1,0)
            else:
                x,y=R;proj=(2*w*((N-w)*x+y),2*w*((N-w)*x-y),x*(4*w-x));assert any(proj)
            L=sum(proj[:2])+w*proj[2]
            if L==0:typ='infinity';den=None
            else:
                T=tuple(K*v/L for v in proj)
                if not all(T):typ='axis';den=None
                else:
                    assert sum(1/v for v in T)==F(4,p) and sum(T[:2])+w*T[2]==K and image(T,-w,N)==R
                    if (i,j)==(1,0):assert T==Q
                    if (i,j)==(0,1):assert T==W
                    ds=tuple(v.denominator for v in T);den=lcm(*ds);typ='positive' if min(T)>0 else 'signed'
                    if typ=='positive':
                        if den<=k:small.append((i,j,den))
                        units=[v.numerator for v in T if v.denominator==1]
                        if len(units)==2 and gcd(den,2*p)==1 and gcd(*units)%den==0:link.append((i,j,den))
            counts[typ]=counts.get(typ,0)+1
            print(p,i,j,typ,'joint',den,'components',ds if den else None)
    print('summary',p,counts,'positive joint <=k',small,'odd linked',link)
if __name__=='__main__':
    for p,k in zip((409,577,2521,3361),(8219,11579,15137,20177)):run(p,k)
