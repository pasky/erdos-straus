"""z1: 2-adic valuations of the pentagon entries of the chi=-1 words at p = 131, 241 (8/p failures)."""
from cf_lib import words_fast
for p in (131, 241):
    seen=set()
    for (t,u,v) in words_fast(p):
        k=(t,min(u,v),max(u,v))
        if k in seen: continue
        seen.add(k); P=(t,u,v,t*u-1,t*v-1)
        if any(x%4==0 for x in P):
            v2=lambda x:(x & -x).bit_length()-1
            print(p,k,'v2(penta)',[v2(x) for x in P],'v2(tp+1)',v2(t*p+1))
