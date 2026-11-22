"""Check full closure at large controls without visiting O(p) vertices.
For H0 a subgroup certified inside the stabilizer, y^|H0| labels cosets.
Only bounded scans; a failure to enlarge isn't a proof of nonsaturation.
"""
from math import lcm
from sympy import isprime,factorint
for p in (409,577,2521,3361,21841,76441,102001,8813281,113035442521,183783601,2238327841,4367159449,3153419441929,6955940568721,1590284203561):
    assert isprime(p) and p%8==1
    q=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
    fac=factorint(p-1);assert all(isprime(l) for l in fac)
    def order(x):
        n=p-1
        for l in fac:
            while n%l==0 and pow(x,n//l,p)==1:n//=l
        return n
    h=lcm(*(order(x) for x in range(2,q)));proof=[('index',(p-1)//h)]
    while 2*h!=p-1:
        labels=set()
        for y in range(1,min(200000,p)):
            labels.add(pow(y,h,p))
            if len(labels)==(p-1)//h:break
        else:break
        old=h
        for m in range(2,min(1+(2*p-1)//y,200000,p)):
            if pow(m,(p-1)//2,p)==1:h=lcm(h,order(m))
            if h!=old:proof.append(('B',y,'m',m,'new index',(p-1)//h));break
        if h==old:break
    print(p,'q',q,proof,'full',2*h==p-1);assert 2*h==p-1
