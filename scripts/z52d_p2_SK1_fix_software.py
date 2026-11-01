# z52d pass2 SK1 fix round (software-type items, each with a concrete test):
# Z1193 fair diagonal schedule coverage; Z1203 fingerprint collisions on ES triples; Z1182 interval-congruence
# soundness fuzz (+, *); Z1205 straight-line size vs expanded digits; Z1225 cache-key failure demo (Vmin search bound).
import random, math
from fractions import Fraction
random.seed(5)
# Z1193: Cantor-diagonal schedule over (family i, height h): first D(D+1)/2 steps must cover all i+h<D
D=200; seen=set()
for s in range(D*(D+1)//2):
    d=int((math.isqrt(8*s+1)-1)//2); k=s-d*(d+1)//2
    i,h=k,d-k
    seen.add((i,h))
need={(i,h) for i in range(D) for h in range(D) if i+h<D}
print("Z1193 steps:",D*(D+1)//2,"covered all pairs with i+h<D:", need<=seen, "pairs:",len(need))
# Z1203: fingerprint (p, sorted triple) mod 2^61-1 over all ES triples p<=2000 ; collisions between distinct keys
def isp(m): return m>1 and all(m%d for d in range(2,int(m**.5)+1))
M=(1<<61)-1; fp={}; keys=0; coll=0
for p in range(3,2001,2):
    if not isp(p): continue
    for x in range(p//4+1,3*p//4+1):
        a=4*x-p
        if a<=0: continue
        for y in range(x,2*p*x//a+1):
            d=a*y-p*x
            if d<=0 or (p*x*y)%d: continue
            z=p*x*y//d
            if z<y: continue
            key=(p,x,y,z); keys+=1
            h=(p*1000003+x*998244353+y*19260817+z*1000000007)%M
            if h in fp and fp[h]!=key: coll+=1
            fp.setdefault(h,key)
print(f"Z1203 triples hashed: {keys}; fingerprint collisions between distinct triples: {coll}")
# Z1182: interval-congruence domain: value = (lo,hi,r,m) meaning x in [lo,hi], x = r mod m. Sound transfer for + and *.
def gcd(a,b): return math.gcd(a,b)
def mk(lo,hi,r,m): return (lo,hi,r%m if m else r,m)
def add(a,b):
    lo,hi,r1,m1=a; lo2,hi2,r2,m2=b; m=gcd(m1,m2)
    return mk(lo+lo2,hi+hi2,r1+r2,m)
def mul(a,b):
    lo,hi,r1,m1=a; lo2,hi2,r2,m2=b
    cands=[lo*lo2,lo*hi2,hi*lo2,hi*hi2]
    m=gcd(gcd(m1*r2,m2*r1),m1*m2)
    return mk(min(cands),max(cands),r1*r2,m)
def member(v,a): lo,hi,r,m=a; return lo<=v<=hi and (v-r)%m==0 if m else lo<=v<=hi and v==r
viol=0; tests=0
for _ in range(20000):
    def rnd():
        lo=random.randint(-30,30); hi=lo+random.randint(0,30); m=random.choice([1,2,3,4,6,12]); r=random.randint(0,m-1)
        return (lo,hi,r,m)
    A=rnd(); Bv=rnd()
    for _ in range(3):
        x=random.randint(A[0],A[1]); x=x-((x-A[2])%A[3]) + (A[2]%A[3]) if A[3] else x
        if not(A[0]<=x<=A[1] and (x-A[2])%A[3]==0): continue
        y=random.randint(Bv[0],Bv[1]); y=y-((y-Bv[2])%Bv[3]) + (Bv[2]%Bv[3]) if Bv[3] else y
        if not(Bv[0]<=y<=Bv[1] and (y-Bv[2])%Bv[3]==0): continue
        tests+=1
        if not member(x+y,add(A,Bv)): viol+=1
        if not member(x*y,mul(A,Bv)): viol+=1
print(f"Z1182 abstract add/mul soundness: {tests} concrete pairs, violations {viol}")
# Z1205: straight-line size vs expanded digits for the Type-II denominators uBC, nBC, nuC at primes <= 1e5 (smallest word)
def isp2(m): return isp(m)
dig=[]; ops=[]
cnt=0
for n in range(5,100001,4):
    if not isp2(n): continue
    best=None
    for C in range(1,60):
        for u in range(1,60):
            # n = 4uBC - u - B  -> B = (n+u)/(4uC-1)
            m=4*u*C-1
            if (n+u)%m==0:
                B=(n+u)//m
                if B>=1: best=(u,B,C); break
        if best: break
    if best:
        u,B,C=best; dig.append(len(str(u*B*C))+len(str(n*B*C))+len(str(n*u*C))); cnt+=1
        ops.append(6)  # 3 products, each 2 multiplications with shared factors (straight-line ops count)
print(f"Z1205 Type-II words found for {cnt} primes <=1e5 (small C): mean decimal digits of the three denominators {sum(dig)/len(dig):.1f}, SLP ops {ops[0]}")
# Z1225: cache keyed only by p vs keyed by (p, bound). Vmin with search bound 50 vs 4000 at p=2521 (Vmin=87) and 3361 (Vmin=116)
def vmin(p,VS):
    for v in range(3,VS+1):
        if not((v%4==0) or ((v+p)%8==0)): continue
        n=p+v; ds=[d for d in range(1,int(n**.5)+1) if n%d==0]
        divs=set(ds+[n//d for d in ds])
        if any(d%v==v-1 for d in divs): return v
    return None
cache={}
def cached_bad(p,VS):
    if p not in cache: cache[p]=vmin(p,VS)
    return cache[p]
a=cached_bad(2521,50); b=vmin(2521,4000)
print(f"Z1225 cache keyed by p only: first query bound 50 gives {a}; correct bound 4000 gives {b}  -> stale entry")
cache2={}
def cached_good(p,VS):
    k=(p,VS)
    if k not in cache2: cache2[k]=vmin(p,VS)
    return cache2[k]
print(f"Z1225 cache keyed by (p,bound): bound 50 -> {cached_good(2521,50)}, bound 4000 -> {cached_good(2521,4000)}")
