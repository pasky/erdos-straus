"""Z0759: compare R(2^k-1) (exact, k<=61) with residue-matched controls n = 2^k-1+840j (j=1..200 for k<=44, 1..40 for 45..50).
Writes data/z52b/pass2/ZF0/Z0759/summary.json"""
import json, re, statistics as st, math
D='data/z52b/pass2/ZF0/Z0759/'
M={}
for f in ['R_mersenne_k2_50.txt','R_mersenne_k51_58.txt','R_mersenne_k59_60.txt','R_mersenne_k61.txt']:
    for l in open(D+f):
        m=re.match(r'k=(\d+) n=(\d+) U=\d+ R=(\d+)',l); M[int(m[1])]=int(m[3])
ctrl={}
import itertools
blocks=[(f,k0,k1,J) for f,k0,k1,J in [('ctrl_k6_44.txt',6,44,200),('ctrl_k45_50.txt',45,50,40)]]
for f,k0,k1,J in blocks:
    L=open(D+f).read().split('\n')[:-1]; assert len(L)==(k1-k0+1)*J
    for i,l in enumerate(L):
        n,R,R12=map(int,l.split()); k=k0+i//J; assert (n-(2**k-1))%840==0
        ctrl.setdefault(k,[]).append((R,R12))
for _ in []:
    for l in []:
        n,R,R12=map(int,l.split())
        k=max(kk for kk in range(2,62) if 2**kk-1 < n)   # n = 2^k-1+840j, j<=200 (840*200 < 2^k-1 only for k>=18; small k handled by j-block below)
        ctrl.setdefault(k,[]).append((R,R12))
out={'R_mersenne':M,'zeros':[k for k in sorted(M) if M[k]==0],'per_k':{}}
rows=[]
for k in sorted(ctrl):
    Rs=[a for a,b in ctrl[k]]; R12=[b for a,b in ctrl[k]]
    mean=st.mean(Rs); frac12=sum(R12)/max(1,sum(Rs))
    pct=sum(1 for r in Rs if r<=M[k])/len(Rs)
    out['per_k'][k]=dict(R=M[k],ctrl_n=len(Rs),ctrl_mean=round(mean,2),ctrl_zero_frac=round(sum(r==0 for r in Rs)/len(Rs),3),
        ctrl_frac_from_minuv_le2=round(frac12,3),pctile_of_mersenne=round(pct,3),ratio=round(M[k]/mean,3))
    rows.append((k,M[k],mean,pct,frac12))
import numpy as np
r=np.array([x[1]/x[2] for x in rows if x[0]>=14]); f12=np.array([x[4] for x in rows if x[0]>=14])
out['mean_ratio_k14_50']=float(r.mean()); out['median_pctile_k14_50']=float(np.median([x[3] for x in rows if x[0]>=14]))
out['mean_ctrl_frac_minuv_le2_k14_50']=float(f12.mean())
json.dump(out,open(D+'summary.json','w'),indent=1)
for x in rows: print('k=%2d R=%4d ctrl_mean=%7.2f pct=%.2f frac12=%.3f'%x)
print('mean ratio k>=14:',r.mean(),' mean ctrl frac(min(u,v)<=2):',f12.mean())
