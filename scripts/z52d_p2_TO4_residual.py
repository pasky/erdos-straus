# z52d pass2 TO4: residual-fraction experiments.
# r_x = 4/p - 1/x = (4x-p)/(px);  two-term(a/b): exists y,z with 1/y+1/z = a/b  <=> divisor e of b^2 with e ≡ -b (mod a)
#   and e*(b^2/e) = b^2 with both ≡ -b (mod a); (ay-b)(az-b)=b^2.
import sys, math, random
from collections import Counter
from sympy import primerange, factorint, divisors
def reduce(num,den):
    g=math.gcd(num,den); return num//g, den//g
def two_term(a,b):
    # return list of (y,z) with 1/y+1/z=a/b, y<=z
    out=[]
    for e in divisors(b*b):
        f=(b*b)//e
        if (e+b)%a==0 and (f+b)%a==0:
            y=(e+b)//a; z=(f+b)//a
            if y>0 and z>0 and y<=z: out.append((y,z))
    return out
def cf_path(a,b):
    # Stern–Brocot / continued fraction direction string of a/b (for suffix stats)
    path=[]; x,y=a,b
    while y:
        q=x//y; path.append(q); x,y=y,x-q*y
    return path
# ---- Z0996 Pell: y=z-h families, count solutions with |z-y|=h<=20 for primes p≤PM
PM=int(sys.argv[1]) if len(sys.argv)>1 else 2000
hits=Counter(); tot=0; anyh=0
for p in primerange(5,PM):
    if p%4!=1: continue
    tot+=1; found=False
    for x in range(p//4+1, (3*p)//4+1):
        a,b=reduce(4*x-p, p*x)
        if a<=0: continue
        for (y,z) in two_term(a,b):
            if z-y<=20 and z>y: hits[z-y]+=1; found=True
    anyh+= found
print("Z0996: primes checked",tot,"; primes with a solution having 1<=z-y<=20:",anyh)
print("  count by h (solutions over all x):",sorted(hits.items())[:20])
# ---- Z0985 Farey adjacency of consecutive residuals r_x, r_{x+1}
adj=0; pairs=0; twot=0; twot_runs=[]
for p in primerange(1000,1400):
    if p%24!=1: continue
    prev=None; run=0
    for x in range(p//4+1,(3*p)//4):
        a,b=reduce(4*x-p,p*x); a2,b2=reduce(4*(x+1)-p,p*(x+1))
        pairs+=1
        if abs(a*b2-a2*b)==1: adj+=1
        ok = bool(two_term(a,b))
        twot+=ok
print("Z0985: consecutive pairs",pairs,"Farey-adjacent (|a b' - a' b|=1):",adj, round(adj/pairs,4),"; two-term fraction of residuals:",round(twot/pairs,4))
# ---- Z1006 Stern–Brocot suffixes (length<=8 of CF partial quotients as path) for two-term vs not
suf_ok=Counter(); suf_no=Counter()
for p in primerange(1000,2000):
    if p%24!=1: continue
    for x in range(p//4+1,(3*p)//4):
        a,b=reduce(4*x-p,p*x)
        if a<=0 or b<=1: continue
        s=tuple(cf_path(a,b)[-8:][-3:])  # last up-to-3 partial quotients as suffix (shorter cell counts)
        (suf_ok if two_term(a,b) else suf_no)[s]+=1
nok=sum(suf_ok.values()); nno=sum(suf_no.values())
print("Z1006: suffix(last 3 CF quotients) counts: two-term",nok,"non-two-term",nno)
top=set([k for k,v in suf_ok.most_common(8)]+[k for k,v in suf_no.most_common(8)])
for k in sorted(top,key=lambda t:-(suf_ok[t]+suf_no[t]))[:8]:
    print("  suffix",k,"two-term rate", round(suf_ok[k]/max(1,suf_ok[k]+suf_no[k]),3), "n=",suf_ok[k]+suf_no[k])
