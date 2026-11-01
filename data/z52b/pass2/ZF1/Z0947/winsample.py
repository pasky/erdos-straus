import numpy as np, sys, json
rng=np.random.default_rng(12345)
# log-spaced windows between 1e6 and 1e8: edges
edges=np.unique(np.round(np.logspace(6,8,21)).astype(np.int64))
def primes_in(lo,hi):
    s=np.ones(hi-lo,bool)
    r=int(hi**.5)+1
    small=np.ones(r+1,bool); small[:2]=False
    for i in range(2,int(r**.5)+1):
        if small[i]: small[i*i::i]=False
    for q in np.nonzero(small)[0]:
        st=max(q*q,((lo+q-1)//q)*q)
        s[st-lo::q]=False
    return lo+np.nonzero(s)[0]
info=[]; out=[]
for a,b in zip(edges[:-1],edges[1:]):
    P=primes_in(int(a),int(b))
    k=300 if b<=1e7+1 else 120
    S=np.sort(rng.choice(P,size=k,replace=False))
    info.append(dict(lo=int(a),hi=int(b),nprimes=int(len(P)),n1mod4=int((P%4==1).sum()),k=k))
    out+= [int(x) for x in S]
json.dump(info,open('win_info.json','w'))
open('win_sample.txt','w').write('\n'.join(map(str,out))+'\n')
print(len(out))
