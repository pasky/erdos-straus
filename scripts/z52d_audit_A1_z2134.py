# Z2134: Dagal (arXiv:2003.13229) Thm 5.1 rewriter 1/s + 1/(rs) = 1/(qr) + 1/(qs), r=q+d, s=qr-d (q>1,d>=1).
# Apply to every pair of denominators of every ES solution 4/p = 1/x+1/y+1/z (x<=y<=z), p<300 prime.
from fractions import Fraction as F
def isprime(n): return n>1 and all(n%k for k in range(2,int(n**.5)+1))
def sols(n):
    S=set()
    for x in range(n//4+1, 3*n//4+2):
        r1=F(4,n)-F(1,x)
        if r1<=0: continue
        for y in range(max(x,int(1/r1)), int(2/r1)+2):
            r2=r1-F(1,y)
            if r2>0 and r2.numerator==1 and r2.denominator>=y: S.add((x,y,r2.denominator))
    return S
applic=0; new_outside=0; typechg=0; tot=0
for p in [q for q in range(5,300) if isprime(q)]:
    S=sols(p); tot+=len(S)
    for sol in S:
        for i in range(3):
            for j in range(3):
                if i==j: continue
                s,big=sol[i],sol[j]
                if big%s: continue
                r=big//s
                if (s+r)%(r+1): continue
                q=(s+r)//(r+1); d=r-q
                if q<=1 or d<1 or q*r-d!=s: continue
                applic+=1
                k=[t for t in range(3) if t not in (i,j)][0]
                new=tuple(sorted((sol[k],q*r,q*s)))
                assert F(4,p)==sum(F(1,t) for t in new)
                if new not in S: new_outside+=1
                tp=lambda t: sum(1 for v in t if v%p==0)
                if tp(new)!=tp(sol): typechg+=1
print("primes<300: solutions",tot,"rewriter applications",applic,"images outside solution set",new_outside,"type changes (I<->II)",typechg)
