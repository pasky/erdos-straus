# z58 WILDCARD: ladder law, (A) checked against K=4 at small decades, (B) restricted to "Mordell-hard" primes
# (p a quadratic residue mod 3, 5 and 7, the classes where Mordell's complete moduli f = 3, 7, 15 give nothing).
import math, collections
def qr105(p): return all(pow(p%q,(q-1)//2,q)==1 for q in (3,5,7))
rows=[list(map(int,l.split())) for l in open('data/z58/wildcard/counts_K4to24_1e6.txt')]
Ks=[4,8,12,16,20,24]
files={8:['census_K8_1e7.txt','census_K8_1e7_1e8.txt','census_K8_1e8_1e9.txt'],12:['census_K12_1e8.txt'],16:['census_K16_1e8.txt'],
       20:['census_K20_primes_1e8.txt'],24:['census_K24_primes_1e8.txt']}
# primes per decade, all and QR mod 105 (exact count by sieve up to 1e8; decade 8 only for K=8 -> skip restricted)
LIM=10**8
sieve=bytearray([1])*(LIM+1); sieve[0]=sieve[1]=0
for i in range(2,int(LIM**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(range(i*i,LIM+1,i)))
pi_all=collections.Counter(); pi_qr=collections.Counter()
for p in range(3,LIM):
    if sieve[p]:
        k=int(math.log10(p)); pi_all[k]+=1
        if qr105(p): pi_qr[k]+=1
for restricted in (False,True):
    sel=[r for r in rows if (qr105(r[0]) or not restricted)]
    lam={K:sum(r[1+2*i]/math.log(r[0])**3 for r in sel)/len(sel) for i,K in enumerate(Ks)}
    pts=[]
    for K,fs in files.items():
        dec=collections.Counter()
        for fn in fs:
            for l in open('data/z58/wildcard/'+fn):
                t=l.split()
                if l.startswith('ZERO') and t[2]=='P':
                    p=int(t[1])
                    if p==K//4 or p>=LIM: continue
                    if restricted and not qr105(p): continue
                    dec[int(math.log10(p))]+=1
        for k in range(2,8):
            z=dec.get(k,0); den=(pi_qr if restricted else pi_all)[k]
            if z>=3: pts.append((K,k,lam[K]*((k+0.5)*math.log(10))**3, math.log(z/den)))
    n=len(pts); mx=sum(p[2] for p in pts)/n; my=sum(p[3] for p in pts)/n
    B=-sum((p[2]-mx)*(p[3]-my) for p in pts)/sum((p[2]-mx)**2 for p in pts); A=my+B*mx
    dev=max(abs(p[3]-(A-B*p[2])) for p in pts)
    print(f'## {"QR mod 3,5,7 primes" if restricted else "all primes"}: sample {len(sel)}; lambda_K =',{K:round(v,4) for K,v in lam.items()})
    print(f'   fit on {n} points (K=8..24, decades 2..7): log rate = {A:.3f} - {B:.3f} * lambda*L^3; max |dev| {dev:.2f}')
    tot=0
    for k in range(1,8):
        x=lam[4]*((k+0.5)*math.log(10))**3; den=(pi_qr if restricted else pi_all)[k]; e=den*math.exp(min(0,A-B*x)); tot+=e
        print(f'   K=4 decade {k}: x={x:.1f} predicted zeros {e:.3g} (observed 0)')
    print(f'   K=4 predicted total decades 1-7: {tot:.2f}; Poisson P(0 observed) = {math.exp(-tot):.2g}')
