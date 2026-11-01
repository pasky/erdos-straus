# For primes p ≡ 1 (4) < N: does 4/p = 1/x+1/y+1/z have a solution with some pair coprime?
from math import gcd
from sympy import primerange, divisors, factorint
def sols(p):
    out=[]
    for x in range(p//4+1, 3*p//4+1):
        num=4*x-p; den=p*x       # num/den = 1/y+1/z, y<=z, y in (den/num, 2den/num]
        if num<=0: continue
        g=gcd(num,den); a,b=num//g,den//g
        # 1/y+1/z=a/b: (ay-b)(az-b)=b^2
        for d in divisors(b*b):
            if d>b: break
            if (d+b)%a==0 and (b*b//d+b)%a==0:
                y=(d+b)//a; z=(b*b//d+b)//a
                if y>=x: out.append((x,y,z))
    return out
fails=[]
import sys
N=int(sys.argv[1])
for p in primerange(5,N):
    if p%4!=1: continue
    S=sols(p)
    ok=any(gcd(x,y)==1 or gcd(x,z)==1 or gcd(y,z)==1 for x,y,z in S)
    if not ok: fails.append(p)
print(len(fails), fails[:40])
print('mod 12', sorted(set(p%12 for p in fails)), 'mod 24',sorted(set(p%24 for p in fails)))
for p in fails[:25]: print(p, factorint((p+3)//4), factorint(p+1), factorint((p-1)//4))
print('--- survivors ≡1 mod 12')
from math import gcd
for p in [q for q in primerange(13,N) if q%12==1 and q not in fails][:12]:
    S=[s for s in sols(p) if gcd(s[0],s[1])==1 or gcd(s[0],s[2])==1 or gcd(s[1],s[2])==1]
    print(p, S[:4], factorint(p+2), factorint((p+3)//4))
print('--- criterion: fail iff all prime factors of p+4 are ≡ 1 mod 4')
pred=[p for p in primerange(5,N) if p%4==1 and all(q%4==1 for q in factorint(p+4))]
print('match', pred==fails, len(pred))
