import math, numpy as np, sys
rng=np.random.default_rng(1); k=int(sys.argv[1])
nus=[]
for it in range(3000):
    N=int(rng.integers(50000,100000))|1
    a=rng.integers(0,N,size=k)
    j=np.arange(1,N,dtype=np.int64); tot=np.zeros(N-1,dtype=np.int64)
    for s in a:
        r=(j*s)%N; tot+=np.minimum(r,N-r)
    order=N//np.gcd(j,N)
    m=tot[order>N**(1/k)*3]
    nus.append(m.min()/N*N**(1/k))
nus=np.array(nus)
for t in [0.05,0.1,0.2,0.3,0.5]: print(t, np.mean(nus<t))
