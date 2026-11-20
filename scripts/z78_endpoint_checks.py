"""Exact regression for R17_ENDPOINT. Pass --lane /path/to/worktree-0041 to audit depth-11 logs."""
from pathlib import Path
from fractions import Fraction as Fr
from math import gcd
from collections import Counter
import argparse, gzip
st=Counter({'P third gap':0, 'P combined gap':0, 'P point5 deep checks':0})

def check(kind,r,U,a,b,c,d,p,q):
    assert a<=b and (a+b)%c==0
    e=(a+b)//c; m=4*d; M=m*a; C=p+q; D=q-p; u=p*q
    if kind=='P': B=U//r; v=e; g=c
    else: B=e; v=1; g=c*e
    assert M*b==U*B+v and gcd(a*b*c*d*e,r)==1
    if (p*a+q*b)%U:return False
    st[kind+' positive controls']+=1
    def div(x,y):
        z,t=divmod(x,y);assert t==0;return z
    H=div(p*a+q*b,U);J=div(p*M*a+q*v,U);S=div(p*M*g+D,U);Y=div(U*S*J+D*q*B,M)
    assert M*H==q*B+J and v*S==p*B+J and min(H,J,S)>0
    assert Y==p*a*S+q*H and v*Y==U*H*J-D*p*B*a and U*S*H-Y==u*B*g and p*g*J==Y-D*H
    assert p*M*Y+U*q*m*H*H==D*u*B+U*(m*H*Y-u*B*S)
    t=p*a-q*b
    if kind=='Q':
        f=M*c-U; fs=m*b*c-U
        assert e*f==m*a*a+1 and b*f==U*a+c and f*fs==U**2+m*c*c
        assert 0<f<=U+2 and U<=p*m*a*a+q and m*(U-q)*U**2<=p*C**2*(e*U+1)**2
        assert not (p*f*f+q*m*c*c)%U and not ((p*f-q*fs)**2+4*u*m*c*c)%U**2
        if Y%e: st['Q non-integral Z']+=1
        return True
    N=U*B; A=M*a; Z=div(Y,B); I=m*H*Z-u*S
    assert e<=2*b and M*b<=2*N and M*H<=2*C*B
    assert m*t*t+4*u*e==N*(r*m*H*H-4*u)
    assert (D*D+r*m*H*H)%e==0 and e*A<=4*C*C*N+D*D*A
    assert M*e*Z<=M*p*(2*C+abs(D))*a+2*C*q*e
    C1=p*p*(2*C+abs(D)); C2=Fr(4*q*C*C,r); C3=2*u*C+abs(D)*u
    assert I*U<=Fr(C1*A,e)+C2*U**2/A+C3
    assert gcd(m*t*t,4*u*e)<=4*u*C*C and m*t*t+4*u*e<=(C*C+4*u)*N*N
    if 5*q*e<3*U: assert 5*p*A>=2*U;st['P first gap']+=1
    if M>=4*C*q: assert e<=2*p*(2*C+abs(D))*a;st['P Z bound']+=1
    if I>=1 and 4*C3<=U:
        assert A<=4*C2*U or e*U<=2*C1*A;st['P third gap']+=1
        if M>=4*C*q:
            assert (e<=2*D*D or e*e<=4*p*p*(2*C+abs(D))**2*C2*U or e*e<=16*C1*C*C*B)
            st['P combined gap']+=1
    if u==5 and r>=17 and U>=10**6:
        assert e*e<=466**2*U;st['P point5 deep checks']+=1
    return True

def testrow(kind,r,U,a,b,c,d):
    if (a*b*c*d*(a+b)//c)%r==0:return
    st[kind+' rows']+=1
    for p,q in [(1,5),(5,1)]:
        if check(kind,r,U,a,b,c,d,p,q): st[f'{kind} actual five r={r}']+=1
    # Non-vacuous proportional identities: force q to be a positive endpoint
    # for each real row. Also try centred small pairs found among first 16 p's.
    for p in range(1,17):
        if p%r==0:continue
        q=-p*a*pow(b,-1,U)%U
        g=gcd(p,q);check(kind,r,U,a,b,c,d,p//g,q//g)

def small(r):
    for kind in 'PQ':
        for k in (1,3):
            n=r**k;U=r**((k+1)//2) if kind=='P' else n
            for a in range(1,n//2+2):
                for d in range(1,(n+1)//(2*a)+2):
                    m=4*d
                    lo=1 if kind=='P' else n//(m*a)+1
                    hi=(2*n+2)//(m*a)
                    for c in range(lo,hi+1):
                        den=m*a*c-(1 if kind=='P' else n);num=(n*c+a if kind=='P' else n*a+c)
                        if den<=0 or num%den:continue
                        b=num//den
                        if b<a or (a+b)%c or (a*b*c*d*((a+b)//c))%r==0:continue
                        testrow(kind,r,U,a,b,c,d)
                        if r==13 and k==1 and (a+2*b)%U==0: print('13 single-line exact witness',kind,a,b,c,d)
                        if r==13 and k==1 and (2*a+b)%U==0: print('13 single-line inverse witness',kind,a,b,c,d)

if __name__=='__main__':
    arg=argparse.ArgumentParser();arg.add_argument('--lane',type=Path);lane=arg.parse_args().lane
    for K in range(1,16,2):
        l=(K+1)//2;fn=Path(f'data/m17b/p{K}.txt') if K<15 else Path('data/z17/p15_r17.txt.gz')
        with (gzip.open(fn,'rt') if K==15 else fn.open()) as f:
            for line in f:testrow('P',17,17**l,*map(int,line.split()))
    small(13);small(17)
    R=12650497; mod=12670944
    assert mod==4*8*33*11999 and R%11==2 and R%169==2 and R%(mod//(11*169))==1
    print('two-prime witness',R,mod,'residues mod 11,169:',R%11,R%169)
    if lane:
        for pn in (1,5):
            for mode in ('Ha','Hd','J'):
                row=(lane/f'data/z78/point/11_{pn}_{mode}.txt').read_text().split()
                assert row[:6]==['end','17','11',str(pn),str(6-pn),mode] and list(map(int,row[6:]))==[4258519,1,4258519,1064630 if mode=='J' else 65661461,0]; print('depth-11 Lane2 output',*row)
    print('counts',dict(sorted(st.items())))
