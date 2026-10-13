# Which values does Stern's diatomic s take at positions N with popcount k?  Compare with (W) values.
# s(2N)=s(N), s(2N+1)=s(N)+s(N+1).  Positions with popcount k and bit length <= B (values s(N) <= Fib(B) roughly).
import sys, itertools
from functools import lru_cache
sys.setrecursionlimit(10000)
@lru_cache(None)
def s(N):
    if N<2: return N
    return s(N//2) if N%2==0 else s(N//2)+s(N//2+1)
B=int(sys.argv[1]); LIM=int(sys.argv[2])
# (W) values below LIM
W=set()
for x in range(2,LIM):
    for y in range(2,LIM):
        if 2*x*y-x-2>=LIM: break
        for z in range(2,LIM):
            v=x*y*z-x-z
            if v>=LIM: break
            W.add(v)
for k in [3,4,5]:
    vals=set()
    for bits in itertools.combinations(range(B),k):
        N=sum(1<<b for b in bits); v=s(N)
        if v<LIM: vals.add(v)
    for k2 in [k]:
        miss=sorted(set(range(2,LIM))-vals)
        print("popcount",k,": values<LIM missed:",len(miss),miss[:25], " equal to (W)-complement?", set(miss)==set(range(2,LIM))-W)
