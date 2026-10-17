import sys, math, numpy as np
sys.path.insert(0,'scripts')
from review_r269_fejer import logs
from sympy import primerange
y=int(sys.argv[1]); lo=int(sys.argv[2]); hi=int(sys.argv[3])
S=list(primerange(3,y+1)); k=len(S)
nus=[]
for q in primerange(lo,hi):
    N,a=logs(q,S)
    j=np.arange(1,N,dtype=np.int64); tot=np.zeros(N-1,dtype=np.int64)
    for s in a:
        r=(j*s)%N; tot+=np.minimum(r,N-r)
    order=N//np.gcd(j,N)
    m=tot[order>N**(1/k)*3]   # large-order only
    nus.append(m.min()/N*N**(1/k))
nus=np.array(nus); n=len(nus)
vol=2**k/math.factorial(k)
for t in [0.05,0.1,0.2,0.3,0.5]:
    print(f"t={t}: empirical P(nu<t)={np.mean(nus<t):.4f}  random-model ~ 1-exp(-vol t^k/2)={1-math.exp(-vol*t**k/2):.4f}")
print(n)
