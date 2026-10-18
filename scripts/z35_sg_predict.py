"""Naive per-level prediction sum_c 1/phi(4cd-1) (w <= p/3, p ~ 5e5), squares d=k^2 (k=10..20) vs non-squares in [100,400]."""
import sys; sys.path.insert(0,'scripts')
from z35_lib import *
from sympy import totient
import collections
pm=500000  # typical p
spf=spf_sieve(10**6)
def pred(d):
    s=0.0; c=1
    while True:
        w=4*c*d-1
        if 3*w>pm: break
        f=factor(w,spf); ph=1
        for q,e in f.items(): ph*= (q-1)*q**(e-1)
        s+=1/ph*2  # p restricted to p=1 mod 4 -> w odd coprime... factor 2 for p mod 4? keep relative
        c+=1
    return s
sq=[k*k for k in range(10,21)]
import random
random.seed(1)
ns=[d for d in range(100,401) if d not in sq]
print("mean pred squares %.5f"%(sum(map(pred,sq))/len(sq)))
print("mean pred nonsquares %.5f"%(sum(map(pred,ns))/len(ns)))
