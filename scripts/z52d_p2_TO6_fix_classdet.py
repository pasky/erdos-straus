"""z52d pass2 TO6 fix (Z2409 control): is each witness line's indicator determined by p mod 8, p mod 840, or p mod 840*k?
purity(mod M) = sum over classes of max(#witness, #nonwitness) / #primes."""
import json, numpy as np
D='data/z52b/pass2/TO6/'
rows=[l.split() for l in open(D+'witmask_p1mod4_2e5.txt')]
P=np.array([int(a) for a,b in rows]); M=[int(b,16) for a,b in rows]
W=np.array([[ (m>>j)&1 for j in range(64)] for m in M],dtype=np.int8)
def purity(mod,j):
    cls=P%mod; tot=0
    for c in np.unique(cls):
        s=W[cls==c,j]; tot+=max(s.sum(), len(s)-s.sum())
    return round(float(tot/len(P)),4), int(len(np.unique(cls)))
out={}
for j in [0,1,2,3,4,5,7]:
    out[f't={3+4*j}']={'mod8':purity(8,j),'mod105':purity(105,j),'mod840':purity(840,j),'mod1680':purity(1680,j)}
print(json.dumps(out))
json.dump(out, open(D+'class_determinacy_TO6.json','w'), indent=1)
