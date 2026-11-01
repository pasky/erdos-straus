"""z52d pass2 TO6 Z2367: all solutions 4/n = 1/x+1/y+1/z (x<=y<=z) for n = m^2, m odd <= MMAX, classified by which
denominators are divisible by primes of m. Memory: small (solutions list only).
Divisor method: for x in [n/4, 3n/4]: a=4x-n, b=nx, (ay-b)(az-b)=b^2 ."""
import sys
from sympy import divisors, factorint
from math import gcd
MMAX = int(sys.argv[1]) if len(sys.argv)>1 else 101
def sols(n):
    out=set()
    for x in range((n)//4+1, 3*n//4+2):
        if 4*x<=n: continue
        a=4*x-n; b=n*x
        for d in divisors(b*b):
            if d>b: continue
            if (d+b)%a: continue
            e=b*b//d
            if (e+b)%a: continue
            y=(d+b)//a; z=(e+b)//a
            if y>=x and z>=y: out.add((x,y,z))
    return out
rows=[]
for m in range(3, MMAX+1, 2):
    n=m*m
    S=sols(n)
    pf=list(factorint(m).keys())
    cls={}
    for (x,y,z) in S:
        # number of denominators divisible by m
        dm=sum(1 for t in (x,y,z) if t%m==0)
        # denominators coprime to m
        cop=sum(1 for t in (x,y,z) if gcd(t,m)==1)
        key=(dm,cop)
        cls[key]=cls.get(key,0)+1
    # all-scaled solutions correspond to solutions of 4/m
    scaled=sum(1 for (x,y,z) in S if x%m==0 and y%m==0 and z%m==0)
    rows.append((m,len(S),scaled,dict(sorted(cls.items()))))
    print(m, 'N_sol(sorted)=',len(S), 'all-divisible-by-m=',scaled, 'class(#div_by_m,#coprime_to_m)=',dict(sorted(cls.items())), flush=True)
