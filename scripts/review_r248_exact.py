# review_r248_exact.py (R248): exact-case tuples (rho_tau of small height, w1/C1 with common factor). usage: python3 scripts/review_r248_exact.py FULLFILE  (FULL=1 review_r248_caseB 17)
import sys; sys.path.insert(0,'scripts')
from review_r248_liouville import *
from collections import Counter
cnt=Counter()
for line in open(sys.argv[1]):
    t=line.split(); s=int(t[0]); kv=dict(x.split("=") for x in t[3:])
    a,b=int(kv["a"]),int(kv["b"]); w1=[int(c) for c in kv["w1"]]; C1=[int(c) for c in kv["C1"]]
    g=gcd(w1,C1); hr=max(len(divmod_(w1,g)[0]),len(divmod_(C1,g)[0]))-1
    N=(s+1)//2; Ht=max(a-1,b-1)
    cnt[(s,N,Ht,hr)]+=1
for k in sorted(cnt):
    s,N,Ht,hr=k
    if hr< Ht or 3*hr < N+1: print("s=%d N=%d H_tau=%d H(rho_tau)=%d  #%d"%(s,N,Ht,hr,cnt[k]))
print("examples:")
for line in open(sys.argv[1]):
    t=line.split(); s=int(t[0]); kv=dict(x.split("=") for x in t[3:])
    a,b=int(kv["a"]),int(kv["b"]); w1=[int(c) for c in kv["w1"]]; C1=[int(c) for c in kv["C1"]]
    g=gcd(w1,C1); r1=divmod_(w1,g)[0]; r2=divmod_(C1,g)[0]; hr=max(len(r1),len(r2))-1
    if s==14 and max(a-1,b-1)==5 and hr==1: print(line.strip(), "gcd",g,"rho=-",r1,"/",r2)
