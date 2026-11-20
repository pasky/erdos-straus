from functools import cache
from math import isqrt
@cache
def factors(n):
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out
@cache
def order(b,n):
    if n==1:return 1
    t=n
    for p,e in factors(n):t=t//p*(p-1)
    for p,e in factors(t):
        while t%p==0 and pow(b,t//p,n)==1:t//=p
    return t
@cache
def divisors(n):return sorted(d for d in range(1,n+1) if n%d==0)
def primes(B):return [i for i in range(2,B+1) if factors(i)==[(i,1)]]
