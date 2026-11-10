# z69 TWIST triage I17: the set G(p) of classes of Cl(-4p) containing a "good" form
#   [4ac-1, 4a, 4ab-p]  (Type II, d=1: 4ab = p+e, ce = a+b);  equivalently class of the ideal (e, (b-a)+sqrt(-p)).
# Tests: stability of G(p) under multiplication by the ambiguous class J=[2,2,(p+1)/2] and by the class of a
# prime ideal of the least split prime l == 1 (mod 4); overlap compared with the chance value |G|^2/|genus|.
import sys, math
from sympy import primerange, divisors, jacobi_symbol
def reduce(a,b,c):
    while True:
        if b>a or b<=-a:
            k=(a-b)//(2*a) if b<=-a else -((b+a-1)//(2*a))
            # normalize b into (-a, a]
            k=(a - b)//(2*a); b2=b+2*k*a; c=a*k*k+b*k+c; b=b2
        if a>c: a,c=c,a; b=-b; continue
        if a==c and b<0: b=-b
        if -a<b<=a and a<=c: return (a,b,c)
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x,y=egcd(b,a%b); return (g,y,x-(a//b)*y)
def compose_std(f,g,D):
    a1,b1,c1=f; a2,b2,c2=g
    if a1>a2: a1,b1,c1,a2,b2,c2=a2,b2,c2,a1,b1,c1
    s=(b1+b2)//2; n=b2-s
    if a2%a1==0: y1=0; d=a1
    else: d,u,v=egcd(a2,a1); y1=u
    if s%d==0: y2=-1; x2=0; d1=d
    else: d1,x2,y2=egcd(s,d); y2=-y2
    v1=a1//d1; v2=a2//d1
    r=(y1*y2*n - x2*c2) % v1
    b3=b2+2*v2*r; a3=v1*v2; c3=(b3*b3-D)//(4*a3)
    return reduce(a3,b3,c3)
def classgroup_elems(D):
    out=[]; 
    b=D%2; B=math.isqrt(-D//3)
    while b<=B:
        q=(b*b-D)//4; a=max(b,1)
        while a*a<=q:
            if q%a==0:
                c=q//a
                if math.gcd(math.gcd(a,b),c)==1:
                    out.append((a,b,c))
                    if 0<b<a<c: out.append((a,-b,c))
            a+=1
        b+=2
    return out
def good_classes(p):
    D=-4*p; G={}
    e=3
    while 3*e<=p+4:
        x=(p+e)//4
        if (p+e)%4==0:
            for a in divisors(x):
                b=x//a
                if (a+b)%e==0:
                    c=(a+b)//e
                    G.setdefault(reduce(4*a*c-1,4*a,4*a*b-p),[]).append((a,b,c,e))
        e+=4
    return G
P0=int(sys.argv[1]); P1=int(sys.argv[2])
tot=dict(n=0,G=0,gen=0,J=0,Jexp=0.0,L=0,Lexp=0.0,sq=0)
for p in primerange(P0,P1):
    if p%8!=1: continue
    D=-4*p; cl=classgroup_elems(D); h=len(cl); G=good_classes(p); S=set(G)
    # sanity: inversion closed, non-principal genus (a form class is in the principal genus iff it represents an odd number == 1 mod 4 prime to p)
    assert all((a,-b,c) in S or b in (0,a) or a==c for (a,b,c) in S), p
    J=reduce(2,2,(p+1)//2)
    l=5
    while not (l%4==1 and jacobi_symbol(-p,l)==1 and all(l%q for q in range(2,int(l**.5)+1))): l+=4
    r=next(t for t in range(l) if (t*t+p)%l==0); Lf=reduce(l,2*r,(r*r+p)//l)
    nJ=sum(1 for g in S if compose_std(g,J,D) in S); nL=sum(1 for g in S if compose_std(g,Lf,D) in S)
    tot['n']+=1; tot['G']+=len(S); tot['gen']+=h//2; tot['J']+=nJ; tot['L']+=nL
    tot['Jexp']+=len(S)**2/(h/2); tot['Lexp']+=len(S)**2/(h/2)
    if len(sys.argv)>3: print(p,h,len(S),nJ,nL,l)
print(f"primes p==1(8) in [{P0},{P1}): {tot['n']}; sum|G|={tot['G']} sum|genus|={tot['gen']} (mean fill {tot['G']/tot['gen']:.3f}); "
      f"J-stable members {tot['J']} (chance {tot['Jexp']:.0f}); l-stable members {tot['L']} (chance {tot['Lexp']:.0f})")
