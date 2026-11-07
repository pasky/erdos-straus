# Sanity: every identity class (c,D) produced by classes(M) for M=840*11 must consist of primes with an actual ES solution
# of the stated family. Check: for each class, take the first 3 primes p = c (mod D), p > 8 D^2, and construct the solution.
from fractions import Fraction as F
from sympy import divisors, isprime, nextprime
from math import gcd
from z62_inversef_cover import classes
def has_sol(p,c,D,fam):
    if fam=='A':   # p = -s mod 4YZ, s | Y+Z
        L=D//4
        for Y in divisors(L):
            Z=L//Y
            for s in divisors(Y+Z):
                if (p+s)%D==0:
                    g=(p+s)//D; m=(Y+Z)//s
                    return F(1,g*Y*Z)+F(1,p*m*g*Y)+F(1,p*m*g*Z)==F(4,p)
    if fam=='C':
        L=D//4
        for Y in divisors(L):
            Z=L//Y
            for s in divisors(Z):
                g=Z//s
                if (p+s+4*g*Y*Y)%D==0:
                    m=(p+s+4*g*Y*Y)//D; ZZ=m*s-Y
                    return ZZ>0 and F(1,g*Y*ZZ)+F(1,p*m*g*Y)+F(1,p*m*g*ZZ)==F(4,p)
    if fam=='B':
        e=(D+1)//4
        for Y in divisors(e):
            for m in divisors(e//Y):
                if (m*p+Y)%D==0:
                    g=e//(Y*m); s=(p+4*g*Y*Y)//D; Z=m*s-Y
                    return Z>0 and (p+s)==4*g*Y*Z and F(1,g*Y*Z)+F(1,p*m*g*Y)+F(1,p*m*g*Z)==F(4,p)
    if fam=="A'":
        L=D//4
        for a in divisors(L):
            b=L//a
            if gcd(a,b)!=1: continue
            for t in divisors(a+b):
                if t%4==3 and gcd(t,2*L)==1 and (p*t+1)%D==0:
                    w=(p*t+1)//4
                    return w%a==0 and w%b==0 and F(1,(w//a)*(a+b)//t)+F(1,(w//b)*(a+b)//t)+F(1,p*w)==F(4,p)
    if fam=="B'":
        L=D//4
        for a in divisors(L):
            h=L//a
            for t in divisors(4*a*a*h+1):
                if t%4==3 and (p+(4*a*a*h+1)//t)%D==0:
                    e=(p+(4*a*a*h+1)//t)//D; b=t*e-a
                    w=(p*t+1)//4
                    return b>0 and (p*t+1)%4==0 and w%a==0 and w%b==0 and (a+b)%t==0 and F(1,(w//a)*(a+b)//t)+F(1,(w//b)*(a+b)//t)+F(1,p*w)==F(4,p)
    return False
import sys
DMAX=int(sys.argv[1]) if len(sys.argv)>1 else 400
cl=[x for x in classes(9240) if x[1]<=DMAX and gcd(x[0],x[1])==1 and x[2] in ('A','B','C',"A'","B'")]  # F1/F3 validated separately by z62_inversef_f1f3.py
bad=0
for c,D,fam in sorted(cl):
    p=c+D*((8*D*D)//D+1)
    n=0
    while n<3:
        if isprime(p):
            if not has_sol(p,c,D,fam): bad+=1; print("FAIL",c,D,fam,p)
            n+=1
        p+=D
print("classes checked:",len(cl),"failures:",bad)
sys.exit(1 if bad else 0)
