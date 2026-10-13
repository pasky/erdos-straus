"""R176 from scratch: DIFF_DEEP Prop 2.2 identities on all Type II tuples of odd n <= X (own enumerator).
(a) f X^2 + 2XY + f'Y^2 = M(aX^2+bY^2) - (X-Y)^2 (polynomial identity check on coefficients);
(b) (2ad + k)(2bd + k) = de(1+2ck) with k^2 = -d n  [bsC_typeII_commutative Lemma 1];
(c) the SAME identity with k = xy+1, k^2 = -4c^2 d n  [DIFF_DEEP Prop 2.2 text] -- expected to FAIL;
(d) nrd(xy+1) = ff'-1 for trace-zero x,y with <x,y>=1 (realised in (-f, -f*det) basis), i.e. k^2 = -4c^2 d n."""
import sys
sys.path.insert(0,'scripts')
from review_dd_hilbert import typeII  # noqa  (module guarded below)
from fractions import Fraction as Fr
def qmul(u,v,A,B):  # quaternion (A,B): i^2=A, j^2=B, k=ij; u=(t,x,y,z)
    a1,b1,c1,d1=u; a2,b2,c2,d2=v
    return (a1*a2+A*b1*b2+B*c1*c2-A*B*d1*d2, a1*b2+b1*a2-B*c1*d2+B*d1*c2,
            a1*c2+c1*a2+A*b1*d2-A*d1*b2, a1*d2+d1*a2+b1*c2-c1*b2)
X=int(sys.argv[1]); cnt=[0,0,0,0]; tot=0
for n in range(3,X+1,2):
    for f,g,c in typeII(n):
        tot+=1; h=(f*g-1)//n; d=h//(4*c*c); M=4*c*d; a=(f+1)//M; b=(g+1)//M; e=(a+b)//c
        # (a): coefficients of X^2, XY, Y^2
        cnt[0]+= (f, 2, g) != (M*a-1, 2, M*b-1)
        # (b),(c): (x1+k)(x2+k) = x1x2+K + (x1+x2)k vs de + 2cde k
        for K,j in ((-d*n,1),(-4*c*c*d*n,2)):
            cnt[j]+= not (2*a*d*2*b*d+K==d*e and 2*a*d+2*b*d==2*c*d*e)
        # (d): x = i in (A,B) with A=-f; y = -x/f + w*j part with nrd(y_perp)=det/f: take B=-f*det, y = (0,-1/f? ...)
        A=-f; det=f*g-1; Bq=-f*det
        x=(0,1,0,0); y=(0,Fr(1,f),Fr(1,f),0)   # <x,y> = trd(x ybar)/2 = -trd(xy)/2 = 1; nrd(y)=1/f + f*det/f^2 = g
        xy=qmul(x,y,A,Bq); k=(xy[0]+1,)+xy[1:]
        k2=qmul(k,k,A,Bq)
        nrdy=Fr(1,f)+(-Bq)*Fr(1,f*f)
        cnt[3]+= not (nrdy==g and k[0]==0 and k2==(-4*c*c*d*n,0,0,0))
print(f"Type II tuples, odd n<={X}: {tot}; failures (a) {cnt[0]}, (b) {cnt[1]}, (c: DIFF_DEEP's k) {cnt[2]}, (d) {cnt[3]}")
