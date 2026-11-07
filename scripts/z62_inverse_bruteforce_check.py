#!/usr/bin/env python3
"""z62 INVERSE: brute-force R(n) vs slice classifier (hit/no-hit, both slicings) for n = 1 (4), 5 <= n < 1200."""
import sys
import importlib.util
spec=importlib.util.spec_from_file_location('s','scripts/z62_inverse_slices.py'); s=importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
def R(n):
    c=0
    for u in range(1,n+1):
        for C in range(1,n+1):
            d=4*u*C-1
            if d-u>n: break
            if (n+u)%d==0: c+=1
    return c
bad=0
for n in range(5,1200,4):
    U=(n+1)//3+1
    us=''.join(s.classify(n+u,4*u,u) for u in range(1,U+1))
    cs=''.join(s.classify(4*C*n+1,4*C,C) for C in range(1,U+1))
    r=R(n)
    if (r>0)!=('h' in us) or (r>0)!=('h' in cs): bad+=1; print(n,r,us.count('h'),cs.count('h'))
print("bad",bad)
