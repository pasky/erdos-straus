# Verify: for odd n, TypeII(n) [exists solution 4/n=1/x+1/(n y')+1/(n z') with n∤x] <=> exists coprime a,m: m n + a has divisor = -1 mod 4am.
# and TypeI(n) [solution 4/n = 1/x+1/y+1/(n z'), n∤x, n∤y] <=> exists a,w,m: 4aw | m n+1 and m | 4a^2 w+1.   (For prime n these are exact
# classifications; for composite n only the "<=" direction is claimed by the identities, so compare on primes, and report composites separately.)
from fractions import Fraction as Fr
from sympy import isprime, divisors
def sols(n):
    out=[]
    for x in range(n//4+1, 3*n//4+1):
        r=Fr(4,n)-Fr(1,x)
        for y in range(max(x,int(1/r)), int(2/r)+2):
            s=r-Fr(1,y)
            if s>0 and s.numerator==1: out.append((x,y,s.denominator))
    return out
def typeII_bf(n):
    return any(sum(1 for v in s if v%n==0)==2 for s in sols(n))
def typeI_bf(n):
    return any(sum(1 for v in s if v%n==0)==1 for s in sols(n))
def typeII_crit(n, witness=False):
    # m n + a has divisor g = -1 mod 4am; g <= mn+a; bound: g>=4am-1 so 4am-1 <= mn+a -> a(4m-1) <= mn+1
    for m in range(1, n+2):
        for a in range(1, (m*n+1)//(4*m-1)+1):
            N=m*n+a
            for g in range(4*a*m-1, N+1, 4*a*m):
                if N%g==0: return (a,m,g) if witness else True
    return False
def typeI_crit(n):
    # 4aw | m n + 1, m | 4a^2 w + 1  (m = 3 mod 4). bound m: need existence of a,w>=1 with 4aw | mn+1 and m | 4a^2w+1 -> m <= 4a^2w+1 <= a(mn+1)+1 ... search m<=? use m up to 4n (heuristic but report)
    for m in range(3, 4*n, 4):
        N=m*n+1
        if N%4: continue
        for aw in divisors(N//4):
            for a in divisors(aw):
                w=aw//a
                if (4*a*a*w+1)%m==0: return True
    return False
bad=0
for n in range(5, 700, 4):
    II=typeII_bf(n); IIc=typeII_crit(n); I=typeI_bf(n); Ic=typeI_crit(n)
    if isprime(n):
        if II!=IIc or I!=Ic: print("MISMATCH prime",n,II,IIc,I,Ic); bad+=1
    else:
        if IIc and not II: print("MISMATCH composite (crit=>sol fails)",n); bad+=1
        if Ic and not I: print("MISMATCH composite I",n); bad+=1
print("done, mismatches:",bad)
print("105 typeII witness (a,m,g):", typeII_crit(105,True), "typeI_crit(105):", typeI_crit(105))
print("4545 typeII:", typeII_crit(4545,True))
