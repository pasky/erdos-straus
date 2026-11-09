# Gaussian-adaptive letter rule vs control (pre-registered kill test for rule G).
# Rule G(p): candidate letters = divisors >= 2 of a, b, a+b, |a-b| (p = a^2 + b^2, a odd) that are <= sqrt(2p);
# success if some candidate is a letter (x, y or z) of a U7 word.  Control: same construction from a random pair
# (a', b') with a'^2 + b'^2 in [0.9p, 1.1p] (not a representation of p).  Input: list of primes (stdin, one per line).
import sys, random, math
from sympy import divisors, factorint
from sympy.solvers.diophantine.diophantine import cornacchia
def v2(n):
    v=0
    while n%2==0: n//=2; v+=1
    return v
def is_letter(p,L):
    Lx=8*L//math.gcd(8,L); N1=p+L
    for d in divisors(N1):
        if (d+1)%Lx==0: return 'x'
        if (d+1)%L==0:
            x=N1//d; y=(d+1)//L
            if v2(x)+v2(y)>=3: return 'z'
    for D in divisors(L*p+1):
        if (D+1)%Lx==0: return 'y'
    return None
def twosq(p):
    for a in range(1,math.isqrt(p)+1,2):
        b2=p-a*a; b=math.isqrt(b2)
        if b*b==b2: return a,b
def cands(a,b,p):
    S=set(); lim=math.isqrt(2*p)
    for v in (a,b,a+b,abs(a-b)):
        if v>0:
            for d in divisors(v):
                if 2<=d<=lim: S.add(d)
    return sorted(S)
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
ps=[int(l.split()[0]) for l in sys.stdin if l.strip()]
hitG=0; hitC=0; nC=0; sizeG=0; sizeC=0; lG=lC=0
for p in ps:
    a,b=twosq(p); S=cands(a,b,p); sizeG+=len(S)
    g=[L for L in S if is_letter(p,L)]
    hitG+= bool(g); lG+=len(g)
    for rep in range(5):
        while True:
            a2=random.randrange(1,math.isqrt(p)); b2=random.randrange(1,math.isqrt(p))
            if 0.9*p<=a2*a2+b2*b2<=1.1*p and a2*a2+b2*b2!=p: break
        Sc=cands(a2,b2,p); sizeC+=len(Sc); nC+=1
        hc=sum(1 for L in Sc if is_letter(p,L)); lC+=hc; hitC+= hc>0
    print(p,a,b,len(S),g[:6],flush=True)
print(f"RULE G: success {hitG}/{len(ps)}  mean|S|={sizeG/len(ps):.1f};  CONTROL: success {hitC}/{nC}  mean|S|={sizeC/nC:.1f};  per-letter rate G {lG/sizeG:.4f} vs control {lC/sizeC:.4f}")
