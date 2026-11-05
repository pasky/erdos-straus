# z58 WILDCARD: numerator ladder statistics.  (1) mean N^(K)/L^3, R^(K)/L^2, min N/L^3 on the count sample;
# (2) prime zeros per decade for each K from the census files (twisted obstruction (K/4)*m^2 excluded: only p = K/4 itself);
# (3) zero-rate model P(N=0) ~ exp(A - B*mean), fitted on the K-ladder, extrapolated to K = 4 (Assessment only).
import math, glob, collections
rows=[list(map(int,l.split())) for l in open('data/z58/wildcard/counts_K4to24_1e6.txt')]
Ks=[4,8,12,16,20,24]
print('## count sample: %d primes p=1(4) in [1e6,1.1e6) (every 2nd)'%len(rows))
lam={}
for i,K in enumerate(Ks):
    N=[r[1+2*i] for r in rows]; R=[r[2+2*i] for r in rows]; L=[math.log(r[0]) for r in rows]
    mN=sum(n/l**3 for n,l in zip(N,L))/len(N); mR=sum(x/l**2 for x,l in zip(R,L))/len(R)
    z=sum(1 for n in N if n==0); zr=sum(1 for x in R if x==0)
    lam[K]=mN
    print(f'K={K}: mean N/L^3={mN:.4f}  min N/L^3={min(n/l**3 for n,l in zip(N,L)):.4f}  zeros(N)={z}  mean R/L^2={mR:.4f} zeros(R, c=1 line)={zr}')
files={8:['census_K8_1e7.txt','census_K8_1e7_1e8.txt','census_K8_1e8_1e9.txt'],12:['census_K12_1e8.txt'],16:['census_K16_1e8.txt'],
       20:['census_K20_primes_1e8.txt'],24:['census_K24_primes_1e8.txt'],4:['census_K4_1e8.txt','census_K4_1e8_1e9.txt','census_K4_1e9_1e10.txt']}
print('## prime zeros of N^(K) per decade (p = K/4 excluded)')
for K,fs in files.items():
    dec=collections.Counter(); last=None
    for fn in fs:
        try:
            for l in open('data/z58/wildcard/'+fn):
                if l.startswith('ZERO') and l.split()[2]=='P':
                    p=int(l.split()[1])
                    if p==K//4: continue
                    dec[int(math.log10(p))]+=1; last=p
        except FileNotFoundError: pass
    print(f'K={K}: last prime zero {last}; by decade', dict(sorted(dec.items())))
