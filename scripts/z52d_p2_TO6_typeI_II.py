"""z52d pass2 TO6 Z2058: for primes p<=P, classify every sorted solution of 4/p=1/x+1/y+1/z by the number of denominators
divisible by p: exactly 1 = Type I, exactly 2 = Type II (ET §2). Reports primes lacking Type I / lacking Type II."""
import sys, json
from sympy import primerange, divisors
P=int(sys.argv[1])
noI=[]; noII=[]; cnt=0
for p in primerange(3,P+1):
    cnt+=1
    hasI=hasII=False
    n=p
    for x in range(n//4+1, 3*n//4+2):
        if 4*x<=n: continue
        a=4*x-n; b=n*x
        for d in divisors(b*b):
            if d>b or (d+b)%a: continue
            e=b*b//d
            if (e+b)%a: continue
            y=(d+b)//a; z=(e+b)//a
            if not (y>=x and z>=y): continue
            k=sum(1 for t in (x,y,z) if t%p==0)
            if k==1: hasI=True
            elif k==2: hasII=True
    if not hasI: noI.append(p)
    if not hasII: noII.append(p)
print(json.dumps(dict(P=P,primes=cnt,no_typeI=noI,no_typeII=noII)))
