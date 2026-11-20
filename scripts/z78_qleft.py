"""Charge only the rectangles deliberately omitted by the complementary Q scan."""
from z78_qcap import *
from sys import argv

def rest(r):
    F=r**3;E=T=r*r;M=F+2;L=(F+M)**2//(4*(E*T-1));out=0;V=F*F+4*L
    tv=min(ceildiv(rootup(V,k)*B,U) for k in range(3,13) for A,B,U in [tau_major(k)])
    for i in range(L.bit_length()//2+1):
        C=1<<i
        for j in range(L.bit_length()):
            D=1<<j;g=C*C*D
            if g>L:break
            u=4*C*D;h=min(M,(1+(F+M)**2//(4*g))//E)
            if h<T or 1+(h-T)//u<=128:continue
            n=min(C,isqrt(L//D)-C+1)*min(D,L//(C*C)-D+1);v=0;t=T
            while t<=h:
                hi=min(h,2*t-1)
                if g<=(F+hi)**2//(4*(t*E-1)):v+=cap(hi4(V),lo4(t),1+(hi-t)//u)
                t=hi+1
            out+=2*n*min(v,tv)
    return out
if __name__=='__main__':
    for r in range(int(argv[1]),int(argv[2])+1):
        if r>=17 and all(r%p for p in range(2,isqrt(r)+1)):print(r,rest(r),flush=True)
