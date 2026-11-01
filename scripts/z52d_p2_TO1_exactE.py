# z52d pass2 TO1: exact (sympy, unbounded integers) recomputation of the least slice index E(p)=min(4x-p) for given primes.
# Confirms the C enumerator (z52d_p2_TO1_es.c, mode E) on record primes. usage: uv run --with sympy python scripts/z52d_p2_TO1_exactE.py p1 p2 ...
import sys
from math import gcd
from fractions import Fraction
from sympy import factorint, divisors
def first_solution(p):
    x=p//4+1
    while 4*x<=3*p:
        if 4*x>p:
            a=4*x-p; b=p*x; g=gcd(a,b); a//=g; b//=g
            fb=factorint(b); f2={q:2*e for q,e in fb.items()}
            from sympy import divisor_count
            # enumerate divisors of b^2 directly
            ds=[1]
            for q,e in f2.items():
                ds=[d*q**k for d in ds for k in range(e+1)]
            for d in ds:
                if d>b: continue
                if (d+b)%a: continue
                e2=b*b//d
                if (e2+b)%a: continue
                y=(d+b)//a; z=(e2+b)//a
                if y>=x: return x, (x,y,z)
        x+=1
    return None, None
for p in map(int, sys.argv[1:]):
    x,s=first_solution(p)
    print(p, 'E=',None if x is None else 4*x-p, 'solution', s, 'check', None if s is None else (Fraction(1,s[0])+Fraction(1,s[1])+Fraction(1,s[2])==Fraction(4,p)))
