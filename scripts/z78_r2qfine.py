"""Uniform Q upper bounds on F in (n/2,n]; all operations integer."""
from z77_routes import *

def qbound(n):
    B=n.bit_length();es=[1];out=0
    while es[-1]<n+4:es.append(es[-1]+max(1,es[-1]//2))
    for ic,C in enumerate(es[:-1]):
        C1=es[ic+1]-1;wc=C1-C+1
        for id,D in enumerate(es[:-1]):
            if 4*C*D>2*n+2:break
            D1=es[id+1]-1;wd=D1-D+1;u=4*C*D;V=hi4(n*n+4*C1*C1*D1); row=0
            A=max(1,ceildiv(n//2+1,4*C1*D1));A1=(2*n+2)//u;wa=A1-A+1
            if wa<=0:continue
            for j in range((n+2).bit_length()):
                T=1<<j;hi=min(2*T-1,n+2);lo=max(A,ceildiv(n//2+T,4*C1*D1));aa=min(A1,(n+hi)//u);w=aa-lo+1
                if w<=0:continue
                F=4*j;bd=wc*wd*cap(V,F,1+(hi-T)//u)
                bd=min(bd,w*wc*cap(hi4(aa*n+C1),F,1+(hi-T)//(4*lo*C)))
                # f + F = 4acd; fix c (or a), then f≡−F mod 4c (4a).
                # Once c,f fixed, ad=M/c and a lies in one unit class mod f
                # c≡−aF mod f; choose the a or d class.
                for E,W,xv,yv,lx,ly in ((C,wc,w,wd,lo,D),(lo,w,wc,wd,C,D)):
                    pairs=W*(1+(hi-T)//(4*E));v=hi4((n+hi)//(4*E));
                    bd=min(bd,pairs*min(cap(v,lo4(lx),1+(xv-1)//T),cap(v,lo4(ly),1+(yv-1)//T)))
                row+=bd
            # Whole row also comes from fixed (a,d): <=2 per pair (no sum over f).
            # Optional tau bound fixed c,d
            tv=min(ceildiv(rootup(n*n+4*C1*C1*D1,k)*M,U) for k in range(3,12) for _,M,U in [tau_major(k)])
            out+=2*min(row,2*wa*wd,wc*wd*tv)
    return out
if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):print(b,qbound(1<<b),flush=True)
