# Z1937: does R(p) ((★) ordered count) or the full unordered ES count f(p) avoid some residue mod m (m ≤ 12)
# on primes p ≡ 1 (mod 24)?  A forced nonzero residue would be an M5 count-congruence proof.
from sympy import primerange
def R(p):
    r=0; u=1
    while 4*u-1<=p+u:
        C=1
        while 4*u*C-1<=p+u:
            if (p+u)%(4*u*C-1)==0: r+=1
            C+=1
        u+=1
    return r
def f(p):
    n=0
    for x in range(p//4+1, 3*p//4+1):
        num=4*x-p; den=p*x
        for y in range(max(x,den//num+1), 2*den//num+1):
            zd=num*y-den
            if zd>0 and (den*y)%zd==0 and den*y//zd>=y: n+=1
    return n
Ps=[p for p in primerange(25,12000) if p%24==1]
Rs=[R(p) for p in Ps]
Fs=[f(p) for p in Ps if p<2500]
print("primes ≡1(24) <12000:",len(Ps),"R zeros at",[p for p,r in zip(Ps,Rs) if r==0])
for m in range(2,13):
    a=sorted(set(r%m for r in Rs)); b=sorted(set(x%m for x in Fs))
    print(m,"R residues",a,"| f residues (p<2500, %d primes)"%len(Fs),b)
