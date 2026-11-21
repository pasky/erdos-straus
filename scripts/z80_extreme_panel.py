"""Record-list coverage, primality, 1024-window lower bounds, initial word minima.
Cauchy estimates in the note are independent of this panel. Stdout CSV.
"""
from math import isqrt,gcd
from cypari2 import Pari
from pathlib import Path
import sys
P=Pari();P.allocatemem(128000000,silent=True);P.default('factor_proven',1)
records=list(map(int,Path('data/z60/ms105/pseudo/A002189.txt').read_text().split()))
Q=[int(i) for i in P.primes([2,1000])]
def windows(p):
    I=II=0; w=None
    for x in range(p//4+1,min(p//4+1024,3*p//4)+1):
        g=4*x-p;s=p*x
        for delta in P.divisors(x*x).python():
            for i in (0,1,2):
                h=p**i*delta
                if h>s or (s+h)%g:continue
                y=(s+h)//g
                if y<x:continue
                z,r=divmod(s+s*s//h,g);assert not r and 4*x*y*z==p*(x*y+x*z+y*z) and y<=z
                if i==1:II+=1
                else:I+=1
                if w is None:w=(x,y,z)
    return I,II,w

def wordmins(p):
    mins=[0]*4;rows=[None]*4
    for f in range(2,250001):
        u=(-p)%f
        if not u:continue
        for v0 in (u,u+f):
            if (f+1)%v0:continue
            u0=v0;t=(f+1)//u0;v=(p+u0)//f
            assert t*u0*v-u0-v==p
            tests=[t%4==0,t%8==0,(t*u0)%8==0,min(t,u0,v)>=2 and int(P.kronecker(f,p))==-1]
            for j,test in enumerate(tests):
                if test and not mins[j]:mins[j]=f;rows[j]=(u0,t,v)
        if all(mins):break
    return mins,rows

def report(tag,n):
    fs=P.factor(n);fac='*'.join(str(q) for q,e in zip(fs[0],fs[1]) for _ in range(int(e)))
    prime=int(P.isprime(n));qnr=next(q for q in Q if int(P.kronecker(n,q))==-1)
    if not prime:
        print(tag,n,fac,prime,qnr,*['NA']*7,sep=',',flush=True);return
    lo,hi,w=windows(n);mins,rows=wordmins(n)
    print(tag,n,fac,prime,qnr,lo,hi,*mins,':'.join(map(str,w)) if w else '-',sep=',',flush=True)

if __name__=='__main__':
    print('family,n,factorization,prime,first_inert,I_x1024,II_x1024,R_first,R8_first,U7_first,HJ_first,first_xyz',flush=True)
    for n in records:report('L',n)
    # Paired sample: first p=j²+840 (j=1 mod 840) after each threshold and
    # nearest OTHER prime in its 1 mod 840 class, ties up, excluding same shift.
    for i in (6,8,10,12,14,16,18,20,22,24):
        j=isqrt(10**i)//840*840+1
        while j*j+840<10**i or not P.isprime(j*j+840):j+=840
        p=j*j+840;report('sq'+str(i),p)
        done=False;k=0
        while not done:
            k+=1
            for q in (p+840*k,p-840*k):
                if q>840 and isqrt(q-840)**2!=q-840 and P.isprime(q):
                    report('ct'+str(i),q);done=True;break
