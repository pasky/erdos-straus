"""Meta-fingerprint: for many sub-families F of ES solutions at primes, compare the typical count (mean at p in [5e4,1e5], p≡1 mod 4)
with the largest exception (last prime ≤ 1e5 with count 0; or known campaign values). Test log(last) vs 1/mean."""
import numpy as np, json
R='data/z52b/raw/'
A=np.loadtxt(R+'var_pr_1e5.txt',dtype=np.int64); B=np.loadtxt(R+'var2_pr_1e5.txt',dtype=np.int64)
fam={}
def add(name,P,cnt,last=None):
    s=(P%4==1)&(P>50000)&(P<100000)
    z=P[(cnt==0)&(P>5)]
    fam[name]=dict(mean=float(cnt[s].mean()),median=float(np.median(cnt[s])),last=int(last if last else (z.max() if len(z) else 0)),n_exc=int(len(z)))
P=A[:,0]
add('all solutions U',P,A[:,1],last=1)
add('all even (8/p)',P,A[:,2+3]); add('x|z (lcm-closed)',P,A[:,2+5]); add('all squarefree',P,A[:,2+8]); add('no 3 | xyz',P,A[:,2+14])
add('some 4 | denominator',P,A[:,2+15]); add('primitive',P,A[:,2+4]); add('chain x|y|z',B[:,0],B[:,2+0]); add('z<=p^1.75',B[:,0],B[:,2+6])
for m in (12,16,20,24,28,32,36,40):
    M=np.loadtxt(R+f'm{m}_pr1e5.txt',dtype=np.int64); add(f'{m}/p (k={m//4} divides all)',M[:,0],M[:,1])
W=np.load(R+'words_3e6.npy'); pr=np.load(R+'isprime_3e6.npy')
Pw=W[pr[:len(W)],0]; 
add('(★) R(p)',Pw,W[Pw-1,3],last=8813281)
for k,v in sorted(fam.items(),key=lambda kv:kv[1]['mean']): print(f"{k:28s} mean={v['mean']:8.2f} median={v['median']:6.1f} last={v['last']:9d} n_exc={v['n_exc']}")
json.dump(fam,open('data/z52b/lastexc.json','w'),indent=1)
