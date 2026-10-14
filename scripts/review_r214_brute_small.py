"""R214: naive cross-check of the C lift search (review_r214_lift.c) for odd n <= 61:
exhaustive x,y in Z^3 with |x|^2=A*, |y|^2=A, x.y=1, against Diff=={2} computed via sympy-free Hilbert symbols."""
import itertools, math, sys
def reps(m):
    r=int(math.isqrt(m)); out=[]
    for a in range(-r,r+1):
        for b in range(-r,r+1):
            c2=m-a*a-b*b
            if c2<0: continue
            c=math.isqrt(c2)
            if c*c==c2:
                out.append((a,b,c))
                if c: out.append((a,b,-c))
    return out
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def hil(a,b,p):
    al=be=0
    while a%p==0: a//=p; al+=1
    while b%p==0: b//=p; be+=1
    if p!=2:
        s=(-1)**(al*be*((p-1)//2)); 
        if be%2: s*=leg(a,p)
        if al%2: s*=leg(b,p)
        return s
    u,v=a%8,b%8; e=lambda x:((x-1)//2)%2; w=lambda x:((x*x-1)//8)%2
    return (-1)**((e(u)*e(v)+al*w(v)+be*w(u))%2)
def pf(x):
    s=set(); d=2
    while d*d<=x:
        while x%d==0: s.add(d); x//=d
        d+=1
    if x>1: s.add(x)
    return s
N=int(sys.argv[1]) if len(sys.argv)>1 else 61
tot=mis=0
for n in range(1,N+1,2):
    for t in range(1,n+3):
        for u in range(1,t*n+3):
            A=t*u-1
            if A<1 or (t*n+1)%A: continue
            As=(t*n+1)//A
            if (As+1)%t: continue
            v=(As+1)//t
            assert t*u*v-u-v==n
            ram={p for p in pf(2*As*t*n) if hil(-As,-t*n*As,p)==-1}
            assert len(ram)%2==1
            d2=(ram=={2})
            Y=reps(A); L=any(sum(a*b for a,b in zip(x,y))==1 for x in reps(As) for y in Y)
            tot+=1; mis+=(L!=d2)
print("naive: words",tot,"mismatches",mis)
