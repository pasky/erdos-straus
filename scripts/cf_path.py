import sys
sys.argv=['x','60','100000']
exec(open('cf_groupoid.py').read().split("seen = {}")[0])
from collections import deque
def path(a,b):
    prev={a:None}; q=deque([a])
    while q:
        x=q.popleft()
        if x==b: break
        for y in nbrs(x):
            if y not in prev: prev[y]=x; q.append(y)
    p=[];x=b
    while x: p.append(x); x=prev[x]
    return p[::-1]
for a,b in [((6,18,1),(8,3,4)),((24,5,2),(1,10,27)),((6,16,1),(2,27,2))]:
    p=path(a,b); print([(w,K(w),chi(w,K(w)) if K(w)%2 else None) for w in p])
