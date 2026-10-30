# check: for coprime u,v and t>=1, the largest n with at most t-1 representations n = a*u + b*v (a,b>=0) is t*u*v - u - v
from math import gcd
def reps(n,u,v):
    return sum(1 for a in range(n//u+1) if (n-a*u)%v==0)
bad=0
for u in range(2,12):
    for v in range(2,12):
        if gcd(u,v)!=1: continue
        for t in range(1,5):
            top=(t+2)*u*v
            ns=[n for n in range(0,top) if reps(n,u,v)<=t-1]
            if max(ns)!=t*u*v-u-v: bad+=1; print(u,v,t,max(ns))
            # also: t*u*v-u-v has exactly t-1 reps
            if reps(t*u*v-u-v,u,v)!=t-1: bad+=1; print('exact',u,v,t)
print('mismatches',bad)
# symmetry check: N(n) + N(g_t - n) constant for 0<=n<=g_t ?
vals=set()
for u in range(2,9):
    for v in range(2,9):
        if gcd(u,v)!=1: continue
        for t in range(1,5):
            g=t*u*v-u-v
            vals.add((t,frozenset(reps(n,u,v)+reps(g-n,u,v) for n in range(0,g+1))))
print(sorted((t,sorted(s)) for t,s in vals))
