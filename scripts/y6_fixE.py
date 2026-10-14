"""y6_fixE.py — fixed E, odd c <= C with gcd(c, En) = 1: does f_x = 4na^2 - x aB + B^2 (x = cE) primitively represent -E?
Scans one CF period of both roots (Lagrange: complete since E < sqrt(x^2-16n)/2 for c >= 3). Usage: y6_fixE.py n E C"""
import sys
from math import isqrt, gcd
n, E, C = map(int, sys.argv[1:4])
def rep(x, E):
    d=x*x-16*n
    if d<=0 or isqrt(d)**2==d: return None
    s=isqrt(d)
    for (P,Q) in ((x,2),(-x,-2)):
        p0,p1,q0,q1=0,1,1,0; seen=set()
        while True:
            a=(P+s)//Q if Q>0 else ((P+s+1)//Q if (P+s+1)%Q else (P+s+1)//Q-1)
            p0,p1=p1,a*p1+p0; q0,q1=q1,a*q1+q0
            m=4*n*q1*q1-x*q1*p1+p1*p1
            if m==-E: return (q1.bit_length(), len(seen))
            P=a*Q-P; Q=(d-P*P)//Q
            if (P,Q) in seen: break
            seen.add((P,Q))
    return False
yes=[];no=[]
for c in range(3, C+1, 2):
    if gcd(c, E*n)!=1: continue
    r=rep(c*E,E)
    (yes if r else no).append(c)
print(f"n={n} E={E}: primitive -E rep at c: yes {len(yes)} no {len(no)}; yes {yes[:30]}; no {no[:30]}")
