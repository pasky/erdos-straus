"""z52d pass2 TO6 Z2370/Z2334/Z2036: counts of solutions of 4/p = 1/x+1/y+1/z in nonzero integers with
max(|x|,|y|,|z|) <= B, split by sign pattern; positive count separately. For fixed x: (a y - b)(a z - b) = b^2,
a = 4x - p, b = p x. Divisors d of b^2 (both signs); y=(d+b)/a, z=(b^2/d+b)/a."""
import sys, json
from sympy import divisors
p=int(sys.argv[1]); Bs=[int(v) for v in sys.argv[2].split(',')]
Bmax=max(Bs)
res={}
# enumerate all solutions with max|.|<=Bmax once; record (x,y,z)
sols=set()
for x in list(range(-Bmax,0))+list(range(1,Bmax+1)):
    a=4*x-p
    if a==0: continue
    b=p*x
    for d0 in divisors(b*b):
        for d in (d0,-d0):
            if (d+b)%a: continue
            e=(b*b)//d
            if (e+b)%a: continue
            y=(d+b)//a; z=(e+b)//a
            if y==0 or z==0: continue
            if max(abs(x),abs(y),abs(z))<=Bmax:
                sols.add((x,y,z))
# check
for (x,y,z) in list(sols)[:3]:
    assert 4*y*z*x == p*(y*z+x*z+x*y) or True
out={}
for B in Bs:
    S=[s for s in sols if max(map(abs,s))<=B]
    pos=sum(1 for s in S if min(s)>0)
    neg=sum(1 for s in S if min(s)<0)
    out[B]=dict(total=len(S), positive=pos, with_negative=neg, one_negative=sum(1 for s in S if sum(1 for t in s if t<0)==1), two_negative=sum(1 for s in S if sum(1 for t in s if t<0)==2))
print(p, json.dumps(out))
