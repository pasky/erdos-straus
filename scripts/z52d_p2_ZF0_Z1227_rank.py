"""Small learned partial-factor assignment ranker; no witness-label features."""
import json, math, itertools, time
from pathlib import Path
import numpy as np
from sympy import primerange, factorint
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
out=Path('data/z52b/pass2/ZF0/Z1227'); t=time.time()
def instances(primes):
    groups=[]
    for p in primes:
      for C in range(1,9):
        M=4*C; N=M*int(p)+1; fs=sorted(factorint(N).items())
        if len(fs)<2: continue
        cut=(len(fs)+1)//2
        def vals(f): return sorted(math.prod(a) for a in itertools.product(*[[int(q)**e for e in range(k+1)] for q,k in f]))
        left,right=vals(fs[:cut]),vals(fs[cut:]); rr={d%M for d in right}
        X=[]; y=[]
        for d in left:
          target=(-pow(d,-1,M))%M
          X.append([C,d%M/M,target/M,math.log(d)/math.log(N),len(fs),cut,len(left),len(right),math.log(N),sum(k for q,k in fs[cut:]),min(int(q)%M for q,k in fs[cut:])/M])
          y.append(int(target in rr))
        groups.append((int(p),C,np.array(X),np.array(y),left))
    return groups
train=instances(list(primerange(3,5001)))
ps=list(primerange(100001,1000001)); test=instances(ps[::max(1,len(ps)//4000)])
X=np.vstack([g[2] for g in train]); y=np.concatenate([g[3] for g in train])
model=HistGradientBoostingClassifier(max_iter=150,max_leaf_nodes=15,l2_regularization=5,random_state=1227).fit(X,y)
rng=np.random.default_rng(1227)
def score(groups):
    records=[]; ys=[]; preds=[]
    for p,C,X,y,ds in groups:
      pr=model.predict_proba(X)[:,1]; ys.extend(y); preds.extend(pr)
      if not y.any() or y.all(): continue
      orders=[np.argsort(-pr,kind='stable'),np.arange(len(y)),rng.permutation(len(y))]
      ranks=[int(np.flatnonzero(y[o])[0])+1 for o in orders]
      records.append({'p':p,'C':C,'r840':p%840,'n':len(y),'positives':int(y.sum()),'omega':int(X[0,4]),'remaining_prime_slots':int(X[0,4]-X[0,5]),'ranks':ranks})
    return {'instances':len(groups),'mixed_instances':len(records),'auc':roc_auc_score(ys,preds),'methods':['learned','smallest_partial_divisor','seeded_random'],'top1':[float(np.mean([r['ranks'][i]==1 for r in records])) for i in range(3)],'MRR':[float(np.mean([1/r['ranks'][i] for r in records])) for i in range(3)]},records
tr,_=score(train); te,records=score(test)
# Same instances are paired, hence p mod 840 and C perfectly matched.
diffs=np.array([int(r['ranks'][0]==1)-int(r['ranks'][1]==1) for r in records]); boots=[float(rng.choice(diffs,len(diffs)).mean()) for _ in range(500)]
strata=[]
for slots in sorted({r['remaining_prime_slots'] for r in records}):
    rs=[r for r in records if r['remaining_prime_slots']==slots]
    strata.append({'remaining_prime_slots':slots,'instances':len(rs),'top1':[float(np.mean([r['ranks'][i]==1 for r in rs])) for i in range(3)]})
res={'label':'EVIDENCE','definition':'select exponents of first ceil(omega(N)/2) prime factors of N=4Cp+1; label iff some assignment of remaining exponents yields d=-1 mod 4C','train_prime_max':5000,'test_prime_range':[100001,1000000],'C_max':8,'train':tr,'test':te,'test_by_remaining_slots':strata,'paired_top1_gain_CI95':np.quantile(boots,[.025,.975]).tolist(),'seconds':time.time()-t,'limitations':'No neural message passing; ranking only, exact suffix enumeration supplies labels. Factorization costs excluded from ranking quality. No ES existence claim.'}
(out/'summary.json').write_text(json.dumps(res,indent=2)); (out/'ranks.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in records)); print(json.dumps(res,indent=2))
