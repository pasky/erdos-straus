# R31: concrete instance of the Thm 2.1 construction (H replaced by search), then direct check of n_p and ck_min>g*r.
import sys
from sympy import primerange, isprime, factorint, legendre_symbol, divisors
from math import prod
g,r=int(sys.argv[1]),int(sys.argv[2])
F=[(r*cp,k) for cp in range(1,g+1) for k in range(1,g+1) if cp*k<=g]
A={ck:1+4*ck[0]*ck[1]**2 for ck in F}
B=max(g*r,2*len(F)+2,max(A.values()))
P=1
for l in primerange(2,B+1):
    if l==r: continue
    E=1
    while l**E<=max(A.values()): E+=1
    P*=l**E
Q=P*r
Dset=set()
for (c,k),a_ in A.items():
    for D in divisors(a_):
        if (D+1)%(4*(c//r)*k)==0: Dset.add(D%r)
assert len(Dset)<(r-1)/2, "(2.1)-type count fails"
b=next(b for b in range(1,r) if legendre_symbol(b,r)==-1 and (-b)%r not in Dset)
a=(1+P*(((b-1)*pow(P,-1,r))%r))%Q
assert a%P==1 and a%r==b
print(f"g={g} r={r} |F|={len(F)} B={B} b={b} Q~10^{len(str(Q))-1}")
t=0
while True:
    t+=1; p=Q*t+a
    if not isprime(p): continue
    if all(isprime((p*p+4*c*k*k)//A[(c,k)]) for (c,k) in F): break
print("t=",t,"p=",p)
q=2
while legendre_symbol(q,p)==1: q+=1
print("n_p =",q)
def sf(c): return prod(qq for qq,e in factorint(c).items() if e%2)
first=None
for m in range(1,g*r+1):
    for k in divisors(m):
        c=m//k; s=sf(c)
        if s in (1,2,3,6): continue
        chi=legendre_symbol((-s)%p,p)
        if chi==1: continue  # forced (notes Thm 48.1)
        N=p*p+4*c*k*k; Ms=sum(1 for D in divisors(N) if (D+p)%(4*c*k)==0)
        print(" unforced slice",(c,k),"M=",Ms)
        if Ms>0 and first is None: first=m
print("ck_min <= g*r?", first, "(None means ck_min > g*r)")
