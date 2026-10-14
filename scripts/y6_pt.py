"""y6_pt.py — explicit c-odd W_n point on fibre x with value -E (CF convergent scan). Usage: y6_pt.py n x E"""
import sys
from math import isqrt, gcd
from fractions import Fraction
from sympy import factorint
n, x, E = map(int, sys.argv[1:4]); d = x*x-16*n; s = isqrt(d)
for (P, Q) in ((x, 2), (-x, -2)):
    p0,p1,q0,q1=0,1,1,0; seen=set()
    for k in range(10**6):
        a=(P+s)//Q if Q>0 else (P+s+1)//Q
        p0,p1=p1,a*p1+p0; q0,q1=q1,a*q1+q0
        m=4*n*q1*q1-x*q1*p1+p1*p1
        if m<0 and (-E) % m == 0 and isqrt(E//(-m))**2==E//(-m):
            h=isqrt(E//(-m)); A,B=q1*h,p1*h; c=x//E; g=c*A*B-1
            print(f"root {'omega' if P>0 else 'omega_'}: k={k} a={A} B={B} (a mod 4={A%4}) f={4*n*A*A-x*A*B+B*B} g digits={len(str(g))}")
            print("   g | 4n+Q1^2:", (4*n+(c*B*B)**2)%g==0, " B sqfree:", all(v==1 for v in factorint(B).values()))
            break
        P=a*Q-P; Q=(d-P*P)//Q
        if (P,Q) in seen: break
        seen.add((P,Q))
