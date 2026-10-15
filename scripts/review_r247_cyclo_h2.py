"""R247: h = 2 cyclotomic tuples (s = 10, v1 = -1) from the brute-force census; dep_c = v_T(E + 1 + cT)."""
import sys
from collections import Counter
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return [x%3 for x in r]
def add(a,b):
    n=max(len(a),len(b)); return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%3 for i in range(n)]
for c in (1,2):
    H=Counter(); n=0
    for l in open(sys.argv[1]):
        s,m,g,w,C,v=l.split()
        if s!='10' or v!='2': continue
        n+=1; f=lambda x:[int(ch) for ch in x]
        E=add(mul(mul(mul(f(g),f(m)),[0,1]),f(w)),[2])
        d=add(E,[1,c]); dep=next(i for i,x in enumerate(d) if x)
        H[dep]+=1
    print('c',c,'tuples',n,'dep histogram',sorted(H.items()))
