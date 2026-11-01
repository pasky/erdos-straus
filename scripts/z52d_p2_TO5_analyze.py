"""z52d_p2_TO5_analyze.py — per-item statistics for Pass-2 batch TO5 (reads data produced by z38_mbm.c and
scripts/z52d_p2_TO5_certs.c). Inputs: data/z52b/pass2/TO5/mbm_1e6.txt (n isprime R M0 MBM MBM8),
data/z52b/pass2/TO5/certs2_1e6.txt (p R Rbox minuB n1 nD nE minD). usage: python3 scripts/z52d_p2_TO5_analyze.py"""
import math, sys, collections
D='data/z52b/pass2/TO5/'
mbm={}
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6: continue
    n,isp,R,M0,MB,MB8=int(a[0]),int(a[1]),int(a[2]),float(a[3]),float(a[4]),float(a[5])
    if isp: mbm[n]=(R,M0,MB)
cert={}
for l in open(D+'certs2_1e6.txt'):
    a=list(map(int,l.split()))
    cert[a[0]]=a  # p R Rbox minuB n1 nD nE minD
P=sorted(p for p in cert if p%4==1 and p>=5)
print("primes p≡1(4) ≤1e6:",len(P))
# ---- Z1706: Thue-size box uB <= sqrt(p) ----
for lo,hi in [(5,10**3),(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    S=[p for p in P if lo<=p<hi]
    z=sum(1 for p in S if cert[p][2]==0)
    print("Z1706 box uB<=sqrt p: p in [%d,%d): %d primes, no box cert: %d (%.4f)"%(lo,hi,len(S),z,z/len(S)))
# ---- Z1821: prime-d certificates ----
for lo,hi in [(5,10**3),(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    S=[p for p in P if lo<=p<hi]
    unc=[p for p in S if cert[p][5]==0]
    frac_cert=sum(cert[p][5] for p in S)/max(1,sum(cert[p][1] for p in S))
    print("Z1821 prime-d cover: p in [%d,%d): uncovered(no prime-d cert) %d (%.4f); share of certs with d prime %.3f"%(lo,hi,len(unc),len(unc)/len(S),frac_cert))
# least prime d: distribution vs log^2 prediction
ls=[cert[p][7] for p in P if cert[p][7]>0]
for lo,hi in [(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    S=[p for p in P if lo<=p<hi and cert[p][7]>0]
    if S:
        med=sorted(cert[p][7] for p in S)[len(S)//2]
        print("least prime d (ell(p)) median in [%d,%d): %d  (log of median = %.2f)"%(lo,hi,med,math.log(med)))
# ---- Z1937: residues of R mod 3,5,8 for p≡1 mod 24 ----
S=[p for p in P if p%24==1]
for m in (3,5,8,7,9,16):
    cnt=collections.Counter(mbm[p][0]%m for p in S if p in mbm)
    print("Z1937 R(p) mod %d over p≡1(24), %d primes: residues %s"%(m,len(S),dict(sorted(cnt.items()))))
# ---- Z1808/1809: T/M0 ----
rat=[(mbm[p][1]-mbm[p][2])/mbm[p][1] for p in P if p in mbm and mbm[p][1]>0]
print("Z1808 T/M0 over p≡1(4): mean %.4f max %.4f min %.4f count %d"%(sum(rat)/len(rat),max(rat),min(rat),len(rat)))
# ---- Z1857/Z1925: B-slice composition ----
print("Z1925 fraction of primes p≡1(4) with B=1 cert:", round(sum(1 for p in P if cert[p][4]>0)/len(P),4))
# ---- Z1845: near-squares k=4,16,36 ----
def ratio(p): R,M0,MB=mbm[p]; return R/MB if MB>0 else float('nan')
allr=[ratio(p) for p in P if p in mbm and mbm[p][2]>0]
for k in (4,16,36,100,144):
    S=[]
    for m in range(3,1000):
        p=m*m+k
        if p>10**6: break
        if p in mbm and mbm[p][2]>0 and p%4==1: S.append(mbm[p][0]/mbm[p][2])
    if S: print("Z1845 p=m^2+%d (3<=m<1000): n=%d mean R/M_BM=%.3f  frac R=0 %.4f"%(k,len(S),sum(S)/len(S),sum(1 for x in S if x==0)/len(S)))
print("all p≡1(4) mean R/M_BM=%.3f"%(sum(allr)/len(allr)))

# ---- Z1808: where is max T/M0 attained; by range ----
best=max(((mbm[p][1]-mbm[p][2])/mbm[p][1],p) for p in P if p in mbm and mbm[p][1]>0)
print("Z1808 argmax T/M0 = %.4f at p=%d"%best)
for lo,hi in [(5,10**3),(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    v=[(mbm[p][1]-mbm[p][2])/mbm[p][1] for p in P if lo<=p<hi and p in mbm and mbm[p][1]>0]
    print("Z1808 range [%d,%d): max T/M0 %.4f  mean %.4f  sd %.4f"%(lo,hi,max(v),sum(v)/len(v),(sum(x*x for x in v)/len(v)-(sum(v)/len(v))**2)**0.5))
# ---- Z1821: CDF of least prime d (ell(p)) ----
for L in (3,7,11,31,101,1001,10001):
    f=sum(1 for p in P if 0<cert[p][7]<=L)/len(P)
    print("Z1821 P(exists prime-d cert with d<=%d) over p≡1(4): %.4f"%(L,f))
# ---- Z1925: B=1 failure by range, vs 1/sqrt(log p) ----
for lo,hi in [(5,10**3),(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    S=[p for p in P if lo<=p<hi]
    f=sum(1 for p in S if cert[p][4]==0)/len(S)
    mid=(lo*hi)**0.5
    print("Z1925 B=1 failure fraction in [%d,%d): %.4f ; c/sqrt(log p) with c=%.3f"%(lo,hi,f, f*math.sqrt(math.log(mid))))
