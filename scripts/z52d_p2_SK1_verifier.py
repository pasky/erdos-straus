# z52d pass2 SK1 (Z1187): two-route verifier for ES triples (cleared integer identity and exact Fraction sum)
# tested on genuine solutions of 4/p (p prime <= 2000, from brute force) and on deliberately corrupted triples.
from fractions import Fraction
import random
def route_cleared(p,x,y,z): return 4*x*y*z == p*(x*y+y*z+z*x) and min(x,y,z)>=1
def route_fraction(p,x,y,z): return Fraction(1,x)+Fraction(1,y)+Fraction(1,z)==Fraction(4,p)
def isp(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
sols=[]
for p in range(3,2001,2):
    if not isp(p): continue
    for x in range(p//4+1,3*p//4+1):
        a=4*x-p
        if a<=0: continue
        for y in range(x,2*p*x//a+1):
            d=a*y-p*x
            if d<=0 or (p*x*y)%d: continue
            z=p*x*y//d
            if z>=y: sols.append((p,x,y,z))
print("genuine triples:",len(sols))
assert all(route_cleared(*s) and route_fraction(*s) for s in sols)
random.seed(0); tot=0; caught=0; both_pass=0
for p,x,y,z in sols:
    for _ in range(3):
        c=[x,y,z]; i=random.randrange(3); c[i]+=random.choice([-2,-1,1,2])
        if c[i]<1: continue
        tot+=1
        a=route_cleared(p,*c); b=route_fraction(p,*c)
        if not a and not b: caught+=1
        if a and b: both_pass+=1
print("corrupted triples:",tot,"rejected by both routes:",caught,"accepted by both routes:",both_pass)
