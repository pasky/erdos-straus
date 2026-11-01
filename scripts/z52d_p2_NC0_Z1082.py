# z52d Pass 2 NC0 — Z1082 epsilon-net search portfolios over the family-prime incidence (data/z52b/raw/var_pr_1e5.txt).
# Ground set = the 16 solution-family indicators (names as in scripts/z52d_p2_NC0_families.py). Witness set of prime p:
# W_p = {k : family k has >=1 solution at p}. A portfolio P is a net for threshold t if P ∩ W_p != ∅ for every prime with |W_p| >= t.
# Compare greedy (set-cover) nets with random portfolios of equal size.  Primes p ≡ 1 (mod 4), 5 < p <= 1e5.
import numpy as np, random, json
R='data/z52b/raw/'
A=np.loadtxt(R+'var_pr_1e5.txt',dtype=np.int64)
names=['0 even','1 even','2 even','3 all even','primitive','x,y|z','x|y','isosceles','all squarefree','z<=n^2','z<=n^1.5','some power of 2','x or y prime','some coprime pair','no denom div 3','some denom div 4']
P=A[:,0]; sel=(P%4==1)&(P>5)
W=(A[sel,2:18]>0)                   # primes x 16 families
ns=W.shape[0]; print('primes',ns,'families',W.shape[1])
sizes=W.sum(1)
print('|W_p| distribution (0..16):',np.bincount(sizes,minlength=17).tolist())
rng=random.Random(7)
def greedy_net(rows):
    """greedy set cover: pick families hitting the most not-yet-hit witness sets until all hit."""
    left=np.ones(rows.shape[0],bool); P_=[]
    while left.any():
        k=int(np.argmax((rows[left]).sum(0)))
        if rows[left][:,k].sum()==0: break
        P_.append(k); left&=~rows[:,k]
    return P_
out={}
for t in (1,2,3,4,5,6):
    rows=W[sizes>=t]
    if rows.shape[0]==0: continue
    g=greedy_net(rows); k=len(g)
    # random portfolios of size k: fraction of ranges (|W_p|>=t) they miss
    miss=[]
    for _ in range(2000):
        S=rng.sample(range(16),k)
        miss.append(int((~rows[:,S].any(1)).sum()))
    gmiss=int((~rows[:,g].any(1)).sum())
    out[t]=dict(ranges=int(rows.shape[0]),greedy_size=k,greedy_missed=gmiss,
                random_missed_mean=float(np.mean(miss)),random_missed_min=int(np.min(miss)),
                random_frac_zero_miss=float(np.mean(np.array(miss)==0)))
    print('threshold |W|>=%d: ranges %d | greedy net size %d (misses %d) | random size-%d portfolios: mean misses %.2f, min %d, P(no miss)=%.4f'%(
        t,rows.shape[0],k,gmiss,k,np.mean(miss),np.min(miss),np.mean(np.array(miss)==0)))
    print('   greedy net families:',[names[i] for i in g])
json.dump({str(k):v for k,v in out.items()},open('data/z52b/pass2/NC0/sub/Z1082_nets.json','w'))
