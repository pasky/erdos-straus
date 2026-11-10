import math, random
from sympy import primerange, factorint, jacobi_symbol as J
def red(a,b,c):
    while True:
        if c < a or (c == a and b < 0): a,b,c = c,-b,a; continue
        if b > a or b <= -a:
            k = (a - b)//(2*a); b2 = b + 2*a*k; c = (b2*b2 - (b*b-4*a*c))//(4*a) if False else c + k*b + k*k*a; b = b2; continue
        return (a,b,c)
def divisors(n):
    ds=[1]
    for p,e in factorint(n).items(): ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def good(p, amax):
    G=set()
    for a in range(1,amax+1):
        N=p+4*a*a
        for A in divisors(N):
            if A%(4*a)==4*a-1: G.add(red(A,4*a,N//A))
    return G
def gauss(p):
    for y in range(2,int(math.isqrt(p))+1,2):
        x2=p-y*y; x=math.isqrt(x2)
        if x*x==x2: return x,y//2
hit=tot=0; rnd=0; sizes=[]
for p in primerange(1000,40000):
    if p%8!=1: continue
    G=good(p, 3*int(math.isqrt(p)))
    if not G: continue
    x,ac=gauss(p); outs=set()
    for a in (ac-1,ac+1):
        if a<1: continue
        N=p+4*a*a
        qs=[q for q in sorted(factorint(N)) if q>2 and J(p,q)==-1]
        if qs: q=qs[0]; outs|={red(q,4*a,N//q), red(q,-4*a,N//q)}
    # class group size estimate via all reduced forms of disc -4p
    h=sum(1 for a in range(1,int(math.isqrt(4*p//3))+1) for b in range(-a+1,a+1) if (b*b+4*p)%(4*a)==0 and (b*b+4*p)//(4*a)>=a and math.gcd(math.gcd(a,b),(b*b+4*p)//(4*a))==1 and not ((b*b+4*p)//(4*a)==a and b<0))
    tot+=1; hit+= bool(outs & G); rnd += min(1, len(outs)*len(G)/h); sizes.append(len(G)/h)
print(f"primes {tot}  candidate-3 hit {hit/tot:.3f}  naive null {rnd/tot:.3f}  mean |G|/h {sum(sizes)/len(sizes):.3f}")
