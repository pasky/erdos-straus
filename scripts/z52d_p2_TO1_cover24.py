# z52d pass2 TO1 (Z0461): B2 divisor coverage by fixed C (C=1..Cmax), restricted to primes p = 1 mod 24 (p<N); d<=D with d = -1 mod 4C.
# usage: uv run --with numpy python scripts/z52d_p2_TO1_cover24.py N Cmax D
import sys, numpy as np
N=int(sys.argv[1]); Cmax=int(sys.argv[2]); D=int(sys.argv[3])
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
P=np.array([p for p in range(5,N) if s[p] and p%24==1],dtype=np.int64)
cov=np.zeros(len(P),bool); cum=[]
for C in range(1,Cmax+1):
    cC=np.zeros(len(P),bool)
    for d in range(4*C-1,D+1,4*C):
        if d>1: cC |= ((4*C*P+1)%d==0)
    cov|=cC
    cum.append((C,round(cC.mean(),4),round(cov.mean(),4)))
print("primes p=1 mod 24 below",N,":",len(P))
print("(C, fraction covered by C alone, cumulative fraction covered by C'<=C):",cum)
print("uncovered by C<=%d, d<=%d:"%(Cmax,D), int((~cov).sum()), P[~cov][:10].tolist())
