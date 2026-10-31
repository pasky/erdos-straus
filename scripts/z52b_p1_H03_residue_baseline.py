# Z1383 cheap proxy: how much of "(★) has a C=1 certificate" (4p+1 has a prime factor ≡ 3 mod 4) and of R(p)
# is predictable from residues of p mod small primes (the information a digit-level model can easily extract)?
# Train on p < 4e6, test out of range p in [2e7, 2.2e7]. Logistic regression on one-hot residues mod primes ≤ 97.
import numpy as np, json
from sympy import primerange, isprime, factorint
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
Q=list(primerange(3,98))
def feats(p): 
    v=[]
    for q in Q:
        o=np.zeros(q); o[p%q]=1; v.append(o)
    v.append(np.eye(3)[(p//4)%3]*0)  # pad
    return np.concatenate(v)
def target(p):
    return int(any(q%4==3 for q in factorint(4*p+1)))
def data(lo,hi,step=1):
    ps=[p for p in range(lo+1-(lo%4)+ (0 if lo%4==0 else 4),hi,4) if isprime(p)][::step]
    X=np.array([feats(p) for p in ps]); y=np.array([target(p) for p in ps]); return X,y
Xtr,ytr=data(100,4_000_000,2); Xte,yte=data(20_000_000,22_000_000)
clf=LogisticRegression(max_iter=2000,C=1.0).fit(Xtr,ytr)
auc=roc_auc_score(yte,clf.predict_proba(Xte)[:,1])
# oracle: smallest prime factor of 4p+1 info only via q<=97 (same info) -> exact Bayes: if a q≡3 mod 4, q<=97 divides 4p+1 -> 1
def oracle(X,ps=None): pass
out=dict(n_train=len(ytr),n_test=len(yte),base_rate_test=float(yte.mean()),auc_test=float(auc),
         acc_test=float((clf.predict(Xte)==yte).mean()), acc_majority=float(max(yte.mean(),1-yte.mean())))
print(json.dumps(out)); json.dump(out,open('data/z52b/pass1/H03/residue_baseline.json','w'))
