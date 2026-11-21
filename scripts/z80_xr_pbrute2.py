"""Opus cross-review of R17_WALK (NOT a certificate): fast ground truth for positive controls.
All x=5 P hits (both orientations) at prime r, level L, with e<=e0=466 ceil(sqrt U) (complete for U>=1e6 by
z78 (2.3)), by factoring every M=(N+e)/4 with GNU factor (used only to FIND control hits; every hit is
re-verified exactly here).  Prints HIT p a b d e J HZ Hd.
usage: python scripts/z80_xr_pbrute2.py r L
"""
import sys,subprocess
from math import isqrt
r,L=int(sys.argv[1]),int(sys.argv[2]);U=r**L;B=U//r;N=U*B;e0=466*(isqrt(U-1)+1)
es=[e for e in range((-N)%4 or 4,e0+1,4) if e%r]
inp='\n'.join(str((N+e)//4) for e in es)+'\n'
out=subprocess.run(['factor'],input=inp,capture_output=True,text=True,check=True,timeout=1700).stdout.splitlines()
assert len(out)==len(es)
n=0
for e,line in zip(es,out):
    M,fs=line.split(':');M=int(M);fs=list(map(int,fs.split()));assert M==(N+e)//4
    pr={}
    for f in fs:pr[f]=pr.get(f,0)+1
    P=1
    for f,k in pr.items():P*=f**k
    assert P==M
    ds=[1]
    for f,k in pr.items():ds=[d*f**j for d in ds for j in range(k+1)]
    ds.sort()
    for a in ds:
        if a*a>M:break
        R=M//a
        for b in ds:
            if b<a or R%b:continue
            d=R//b
            if (a+b)%e:continue
            c=(a+b)//e
            if any(z%r==0 for z in (a,b,c,d)):continue
            for p,q in ((1,5),(5,1)):
                if (p*a+q*b)%U:continue
                assert 4*a*b*d==N+e
                H=(p*a+q*b)//U;J=(4*p*a*a*d+q*e)//U;zn=r*H*J-(q-p)*p*a;assert zn%e==0 and zn>0
                print('HIT',r,L,p,a,b,d,e,J,H*zn//e,H*d,flush=True);n+=1
print('brute2',r,L,'keys',len(es),'hits',n,flush=True)
