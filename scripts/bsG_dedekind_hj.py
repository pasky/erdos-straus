# check Hirzebruch-Zagier/Myerson: for n/q = [[b_1..b_r]] (HJ), 12 s(q,n) = (q + q*)/n + sum(b_i - 3), q q* = 1 (mod n)
from fractions import Fraction as F
from math import gcd, floor
def saw(x): return 0 if x.denominator==1 else x-floor(x)-F(1,2)
def ded(q,n): return sum(saw(F(k,n))*saw(F(k*q,n)) for k in range(1,n))
def hj(n,q):
    b=[]
    while q>0:
        c=-(-n//q); b.append(c); n,q=q,c*q-n
    return b
bad=0;cnt=0
for n in range(2,120):
    for q in range(1,n):
        if gcd(q,n)!=1: continue
        qs=pow(q,-1,n); b=hj(n,q); cnt+=1
        if 12*ded(q,n)!=F(q+qs,n)+sum(x-3 for x in b): bad+=1
print("pairs",cnt,"failures",bad)
