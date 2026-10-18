"""Check: for odd primes q != p, (q/p)_4 (as an element of {1,i,-1,-i} via i <-> i_p = a/b mod p, p=a^2+b^2, a odd>0, b even>0)
is a function of (a mod q, b mod q, sign data); also for q=2 a function of (a mod 16, b mod 16).  Prints #conflicts."""
from sympy import primerange
def rep(p):
    a=1
    while a*a<p:
        b2=p-a*a; b=int(round(b2**.5))
        if b*b==b2 and b%2==0: return a,b
        a+=2
def q4(q,p,a,b):
    ip=a*pow(b,-1,p)%p; r=pow(q,(p-1)//4,p)
    return {1:0, ip:1, p-1:2, p-ip:3}[r]
for q in [2,3,5,7,11,13,17,19,23,29,31,37]:
    mod = 16 if q==2 else q
    tab={}; conf=0; n=0
    for p in primerange(5,300000):
        if p%4!=1 or p==q: continue
        a,b=rep(p); key=(a%mod,b%mod, p%16 if q==2 else (a%4, b%8)); v=q4(q,p,a,b); n+=1
        if key in tab and tab[key]!=v: conf+=1
        tab.setdefault(key,v)
    print("q=%d: %d primes, %d keys, conflicts %d"%(q,n,len(tab),conf))
