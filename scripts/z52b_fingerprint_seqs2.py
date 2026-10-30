"""Second OEIS batch: numerator-m failure sets, hard-prime transforms, word-sieve sets."""
import numpy as np, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from z52b_fingerprint_oeis import lookup
from sympy import isprime, primepi
R='data/z52b/raw/'
S={}
def add(name,desc,seq): S[name]=(desc,[int(x) for x in seq])
fails={}
for m in range(5,49):
    a=np.loadtxt(R+f'm{m}_pr1e5.txt',dtype=np.int64); fails[m]=sorted(a[a[:,1]==0,0].tolist())
for m in range(8,49):
    if len(fails[m])>=4: add(f'fail{m}',f'primes p<=1e5 with {m}/p not a sum of 3 unit fractions',fails[m])
    big=[p for p in fails[m] if p>m]
    if len(big)>=4: add(f'fail{m}_gt_m',f'primes p>{m} with {m}/p not 3-term',big)
add('nfail_by_m','#primes p<=1e5 failing m/p, m=5..48',[len(fails[m]) for m in range(5,49)])
add('lastfail_by_m','largest prime p<=1e5 failing m/p, m=7..48',[max(fails[m]) for m in range(7,49)])
add('fail4k_count','#primes<=1e5 failing 4k/p (no ES sol with k|x,y,z), k=2..12',[len(fails[4*k]) for k in range(2,13)])
for m in range(5,14):
    a=np.loadtxt(R+f'm{m}_4000.txt',dtype=np.int64); z=a[a[:,1]==0,0]
    if len(z)>=4: add(f'failall{m}',f'n<=4000 with {m}/n not 3-term',z)
add('lqnr_least_p1mod4','least prime p≡1(4) whose least QNR is the k-th prime',[5,17,73,241,1009,2689,8089,33049,53881,87481,483289,515761,1083289,7921489,3818929])
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
P=FP[:,0]; U=FP[:,1]; s=(P%4==1)&(P>100)
order=np.argsort(U[s]/np.log(P[s])**2); add('hard_ratio','primes p≡1(4) sorted by U(p)/log^2 p ascending',P[s][order[:30]])
add('hard_ratio_sorted','30 hardest p≡1(4)<2e5 by U/log^2p, sorted',sorted(P[s][order[:30]].tolist()))
pm1=P[(P%4==1)]; Um1=U[(P%4==1)]
add('p1_U_min_by_k','min U(p) over p≡1(4) with U(p) attained: primes where U(p) < U(q) for all larger q≡1(4) (backwards low records)',[])
add('minx_excess_primes','primes p with no solution having x=(p+3)/4',[x for x in F[F[:,8]>F[:,0]//4+1,0] if isprime(int(x))][:40])
mx=F[F[:,8]>F[:,0]//4+1,0]; add('minx_excess_comp','composite n with no solution with x=ceil((n+1)/4)',[x for x in mx if not isprime(int(x))][:40])
add('minx_excess_delta','min x - floor(n/4) for n≡1 mod 24',(F[:,8]-F[:,0]//4)[F[:,0]%24==1])
W=np.load(R+'words_3e6.npy'); wn=W[:,0]
sq=np.array([int(round(x**0.5))**2==x for x in wn])
add('R_zero_nonsq_odd','odd non-square n with R(n)=0 (first 50)',wn[(wn%2==1)&(W[:,3]==0)&~sq][:50])
add('R_zero_1mod4_nonsq_comp','composite non-square n≡1(4) with R(n)=0',[x for x in wn[(wn%4==1)&(W[:,3]==0)&~sq][:200] if not isprime(int(x))][:40])
add('ESC_zero_nonsq','non-square n with ESC(n)=0',wn[(W[:,5]==0)&~sq][:40])
i3z=wn[W[:,2]==0]; add('I3_zero_tail','I3 zeros > 100',i3z[i3z>100])
add('I3_zero_odd_gt50','odd I3 zeros >50',i3z[(i3z>50)&(i3z%2==1)])
add('I3_ones_gt1000','n>1000 with I3(n)=1',wn[(W[:,2]==1)&(wn>1000)][:40])
add('Uv_zero_nonsq_all','non-square n with Uv(n)=0 (any residue)',wn[(W[:,4]==0)&~sq][:40])
add('R_at_primes1mod4','R(p) at primes p≡1(4)',[W[p-1,3] for p in range(5,3000) if p%4==1 and isprime(p)])
add('R_half_at_primes1mod4','R(p)/2 at primes p≡1(4)',[W[p-1,3]//2 for p in range(5,3000) if p%4==1 and isprime(p)])
add('W_at_primes','W(p) at primes',[W[p-1,1] for p in range(2,300) if isprime(p)])
add('I3_at_primes','I3(p) at primes p>=29',[W[p-1,2] for p in range(29,800) if isprime(p)])
U_all=F[:,1]; nn=F[:,0]
add('U_low_comp','composite n>100 with U(n) <= 2*log(n)',[x for x,u in zip(nn,U_all) if x>100 and not isprime(int(x)) and u<=2*np.log(x)][:40])
add('U_over_d','n where U(n) equals number of divisors of n... (positions)',[x for x,u in zip(nn,U_all) if u==len([d for d in range(1,x+1) if x%d==0])][:30])
json.dump(S,open('data/z52b/seqs2.json','w'))
out={}
for name,(desc,seq) in S.items():
    if len(seq)<4: continue
    hits=lookup(seq,n=min(len(seq),20))
    out[name]=dict(desc=desc,terms=seq[:24],hits=hits)
    print(name,'|',desc,'|',seq[:14],'->',[h[0]+':'+h[1][:80] for h in hits[:3]],flush=True)
json.dump(out,open('data/z52b/oeis_hits2.json','w'),indent=1)
