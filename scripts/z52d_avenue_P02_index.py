"""z52d avenue P02 / Z2952: classify failing levels C as 'algebraic' (−1 not in H = <prime factors of 4Cp+1> mod 4C)
or 'combinatorial' (−1 in H but no divisor of 4Cp+1 is ≡ −1 mod 4C). Cheap check; EVIDENCE only."""
import sys, random
from sympy import factorint, isprime, divisors
from math import gcd
ZEROS=[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]
CMAX=int(sys.argv[1]) if len(sys.argv)>1 else 200
def subgroup(gens,m):
    H={1}; frontier=[1]
    while frontier:
        new=[]
        for h in frontier:
            for g in gens:
                x=h*g%m
                if x not in H: H.add(x); new.append(x)
        frontier=new
    return H
def stats(p):
    alg=comb=hit=0; combC=[]
    for C in range(1,CMAX+1):
        m=4*C; N=m*p+1; f=factorint(N)
        H=subgroup([q%m for q in f],m)
        h=any(d%m==m-1 for d in divisors(N))
        if h: hit+=1
        elif (m-1) in H: comb+=1; combC.append(C)
        else: alg+=1
    return alg,comb,hit,combC[:8]
random.seed(1)
ctrl=[]
for z in ZEROS:
    while True:
        q=z+24*random.randint(-2000,2000)
        if q>100 and q%24==z%24 and isprime(q) and q not in ZEROS: ctrl.append(q); break
print("CMAX",CMAX)
for lab,L in (("zero",ZEROS),("ctrl",ctrl)):
    A=B=Hh=0
    for p in L:
        a,b,h,cc=stats(p); A+=a;B+=b;Hh+=h
        print(lab,p,"alg",a,"comb",b,"hit",h,"comb-levels",cc)
    print(lab,"TOTAL alg",A,"comb",B,"hit",Hh)
