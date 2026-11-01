# Q(sqrt5): for each class c of (O_K/4)^*, find a totally positive prime pi = a+b*w (w=(1+sqrt5)/2)
# with pi ≡ c mod 4 and -1 in <eps^2> mod pi (eps = w).  Then Lemma 3.1 (other_rings.md) gives positive ES
# for all totally positive n ≡ -c mod 4 (x=(n+pi)/4).
import math
from sympy import isprime, n_order
s5=math.sqrt(5); w=(1+s5)/2; wc=(1-s5)/2
def N(a,b): return a*a+a*b-b*b
classes={}
for a in range(4):
    for b in range(4):
        if N(a,b)%2: classes[(a,b)]=None
B=60
for a in range(-B,B):
    for b in range(-B,B):
        if (a%4,b%4) not in classes or classes[(a%4,b%4)]: continue
        if not (a+b*w>0 and a+b*wc>0): continue
        n=N(a,b)
        if b==0:
            l=abs(a)
            if not (isprime(l) and l%5 in (2,3)): continue
            # inert: eps^(l+1) = N(eps) = -1 mod l, eps^2 power: ord(eps^2) even always -> ok (Prop 3.3)
            classes[(a%4,b%4)]=(a,b,'inert'); continue
        if not isprime(n) or b%n==0: continue
        l=n; r=(-a*pow(b,-1,l))%l
        assert (r*r-r-1)%l==0
        o=n_order(r*r%l,l)
        if o%2==0: classes[(a%4,b%4)]=(a,b,l,o)
for c,v in sorted(classes.items()): print(c,v)
print('uncovered:',[c for c,v in classes.items() if v is None])
