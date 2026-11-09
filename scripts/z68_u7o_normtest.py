# Rule G2 (norm-chain-adaptive letters) vs control.  For a chain survivor p (Lemma N), take ALL representations
# p = a^2+b^2, p+1 = e^2+f^2, p+4 = c^2+d^2 (a,b,... >= 0) and p+2 = u^2+2v^2; candidate letters = divisors >= 2,
# <= sqrt(2p), of every coordinate and of sums/differences of the two coordinates of each rep.
# Control: the same number of random coordinate pairs of the same magnitude (not representations).  NOTE: candidate-set
# sizes are not matched (control sets come out larger); this is a descriptive comparison only.
import sys, random, math
from sympy import divisors
def v2(n):
    v=0
    while n%2==0: n//=2; v+=1
    return v
def is_letter(p,L):
    Lx=8*L//math.gcd(8,L); N1=p+L
    for d in divisors(N1):
        if (d+1)%Lx==0: return True
        if (d+1)%L==0 and v2(N1//d)+v2((d+1)//L)>=3: return True
    for D in divisors(L*p+1):
        if (D+1)%Lx==0: return True
    return False
def reps(n,k):  # n = X^2 + k Y^2, X,Y >= 0
    out=[]
    for Y in range(0,math.isqrt(n//k)+1):
        r=n-k*Y*Y; X=math.isqrt(r)
        if X*X==r: out.append((X,Y))
    return out
def cands_from(pairs,p):
    S=set(); lim=math.isqrt(2*p)
    for X,Y in pairs:
        for v in (X,Y,X+Y,abs(X-Y)):
            if v>0:
                for d in divisors(v):
                    if 2<=d<=lim: S.add(d)
    return S
random.seed(int(sys.argv[1]))
ps=[int(l.split()[0]) for l in sys.stdin if l.strip()]
hitG=hitC=nC=0; szG=szC=0; lG=lC=0
for p in ps:
    raw=reps(p,1)+reps(p+1,1)+reps(p+4,1)
    pairs=sorted({tuple(sorted(q)) for q in raw})+reps(p+2,2)   # dedupe (X,Y)~(Y,X) for the sums of two squares
    S=cands_from(pairs,p); szG+=len(S)
    g=sorted(L for L in S if is_letter(p,L)); hitG+=bool(g); lG+=len(g)
    for rep in range(3):
        fake=[(random.randrange(1,math.isqrt(p)),random.randrange(1,math.isqrt(p))) for _ in pairs]
        Sc=cands_from(fake,p); szC+=len(Sc); nC+=1; hc=sum(1 for L in Sc if is_letter(p,L)); lC+=hc; hitC+=hc>0
    print(p,len(pairs),len(S),g[:6],flush=True)
print(f"RULE G2: success {hitG}/{len(ps)} mean|S|={szG/len(ps):.1f};  CONTROL: success {hitC}/{nC} mean|S|={szC/nC:.1f};  per-letter rate G2 {lG/szG:.4f} vs control {lC/szC:.4f}")
