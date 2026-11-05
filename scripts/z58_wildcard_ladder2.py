# z58 WILDCARD: numerator-ladder zero-rate law with MATCHED populations and a Poisson maximum-likelihood fit that
# INCLUDES zero bins (replaces the first, least-squares/selected-bin version after hostile review).
# Populations: P1 = primes p ≡ 1 (mod 4);  P2 = Mordell-class primes p mod 840 in {1,121,169,289,361,529}.
# lambda_K = mean N^(K)(p)/L^3 over the matching count sample (P1: every 2nd p≡1(4) in [1e6,1.1e6);
# P2: all Mordell primes in [1e6,3e6)).  Zero counts per decade from the census files (all primes ≤ 1e8 covered for
# K = 8..24); primes p with an odd prime factor of K/4 (twisted obstruction, Lemma 4.3) are excluded.
# Model: z_{K,k} ~ Poisson( pi_k * exp(A - B * lambda_K * L_k^3) ), L_k = log(10^(k+0.5)), decades k = 1..7, K = 8..24.
# Prediction for K = 4 under the same law (Assessment: a model, not a test).
import math, collections
MS={1,121,169,289,361,529}
pops={'P1 (p = 1 mod 4)':(lambda p:p%4==1,'counts_K4to24_1e6.txt'),
      'P2 (Mordell classes mod 840)':(lambda p:p%840 in MS,'counts_K4to24_mordell_1e6_3e6.txt')}
Ks=[4,8,12,16,20,24]
files={8:['census_K8_1e7.txt','census_K8_1e7_1e8.txt'],12:['census_K12_1e8.txt'],16:['census_K16_1e8.txt'],
       20:['census_K20_primes_1e8.txt'],24:['census_K24_primes_1e8.txt']}
LIM=10**8
sv=bytearray([1])*(LIM+1); sv[0]=sv[1]=0
for i in range(2,int(LIM**0.5)+1):
    if sv[i]: sv[i*i::i]=bytearray(len(range(i*i,LIM+1,i)))
pis={name:collections.Counter() for name in pops}
for p in range(3,LIM):
    if sv[p]:
        k=int(math.log10(p))
        for name,(sel,_) in pops.items():
            if sel(p): pis[name][k]+=1
zeros={K:[] for K in files}
for K,fs in files.items():
    for fn in fs:
        for l in open('data/z58/wildcard/'+fn):
            t=l.split()
            if l.startswith('ZERO') and t[2]=='P': zeros[K].append(int(t[1]))
def oddprimes(m):
    out=[]; q=3
    while m>1 and q<=m:
        if m%q==0: out.append(q)
        while m%q==0: m//=q
        q+=2
    return out
for name,(sel,cf) in pops.items():
    rows=[list(map(int,l.split())) for l in open('data/z58/wildcard/'+cf)]
    rows=[r for r in rows if sel(r[0])]
    lam={K:sum(r[1+2*i]/math.log(r[0])**3 for r in rows)/len(rows) for i,K in enumerate(Ks)}
    data=[]
    for K in files:
        bad=oddprimes(K//4); dec=collections.Counter()
        for p in zeros[K]:
            if p<LIM and sel(p) and p not in bad: dec[int(math.log10(p))]+=1
        for k in range(1,8):
            if pis[name][k]: data.append((K,k,pis[name][k],dec.get(k,0),lam[K]*((k+0.5)*math.log(10))**3))
    # Poisson MLE by Newton on (A,B)
    A,B=-1.0,0.2
    for it in range(200):
        gA=gB=hAA=hAB=hBB=0.0
        for K,k,pi,z,x in data:
            mu=pi*math.exp(A-B*x)
            gA+=z-mu; gB+=-(z-mu)*x
            hAA+=-mu; hAB+=mu*x; hBB+=-mu*x*x
        det=hAA*hBB-hAB*hAB
        dA=( hBB*gA-hAB*gB)/det; dB=(-hAB*gA+hAA*gB)/det
        A-=dA; B-=dB
        if abs(dA)+abs(dB)<1e-12: break
    dev=0.0
    for K,k,pi,z,x in data:
        mu=pi*math.exp(A-B*x); dev+=2*((z*math.log(z/mu) if z>0 else 0)-(z-mu))
    print(f'## {name}: count sample {len(rows)} primes; lambda_K =',{K:round(v,4) for K,v in lam.items()})
    print(f'   Poisson MLE on {len(data)} (K,decade) bins incl. {sum(1 for d in data if d[3]==0)} zero bins: rate = exp({A:.3f} - {B:.4f}*lambda*L^3); deviance {dev:.1f} on {len(data)-2} df')
    for K,k,pi,z,x in data:
        print(f'   K={K} dec {k}: primes {pi} zeros obs {z} fit {pi*math.exp(A-B*x):.2f} (x={x:.1f})')
    tot=0
    for k in range(1,8):
        x=lam[4]*((k+0.5)*math.log(10))**3; e=pis[name][k]*math.exp(A-B*x); tot+=e
        print(f'   K=4 dec {k}: x={x:.1f} model zeros {e:.3g}')
    print(f'   K=4 model total decades 1-7: {tot:.3g} (observed 0); fitted x-range max {max(d[4] for d in data):.1f}')
