# z57 BFII: target sets T_f = { a * c^{-1} mod f : a c | (f+1)/4 } for f = 3 (mod 4).
# (i) check every t in T_f has Jacobi (t/f) = +1  (so -p in T_f forces (p/f) = -1);
# (ii) list f for which -T_f exhausts all units u with (u/f) = -1 ("complete" moduli).
from math import gcd
def jacobi(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def divs(m): return [d for d in range(1,m+1) if m%d==0]
bad=0; complete=[]; ratio=[]
for f in range(3,4000,4):
    m=(f+1)//4; T=set()
    for c in divs(m):
        for a in divs(m//c): T.add(a*pow(c,-1,f)%f)
    for t in T:
        if jacobi(t,f)!=1: bad+=1
    target=sum(1 for u in range(1,f) if gcd(u,f)==1 and jacobi(u,f)==-1)
    if len(T)==target: complete.append(f)
    ratio.append((len(T)/target,f))
print("violations of (t/f)=+1:",bad)
print("complete moduli f<4000:",complete)
print("best coverage ratios beyond complete:",sorted(ratio,reverse=True)[len(complete):len(complete)+8])
