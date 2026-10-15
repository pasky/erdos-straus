import sys; sys.argv=['x','10','10','1','0']
from sympy import isprime, n_order, jacobi_symbol
exec(open('scripts/z13_window_caps.py').read().split('hist = {}')[0])
bad=0;cnt=0
for q in [11,19,23,43,47,59,67,71,79,83]:
  for n in range(5,400000,4):
    if not isprime(n) or jacobi_symbol(q,n)!=-1: continue
    K=(n+q)//4
    if K%2==0 or not isprime(K) or n_order(K,q)!=q-1: continue
    globals()['spf']=None
    import sympy
    fs={K:1}
    c=cap_at.__globals__
    cnt+=1
    r=cap_at(n,q,q)
    if r is None or r[0]!=(q-3)//4: bad+=1; print(q,n,r)
    if cnt>2000: break
print('cases',cnt,'bad',bad)
