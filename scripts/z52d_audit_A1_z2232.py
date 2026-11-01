# Z2232: ES counting conventions at primes p≡1(4): unordered (x<=y<=z), increasing/distinct (x<y<z), ordered (all perms).
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
rows=[]
for p in [q for q in range(5,1200) if isprime(q) and q%4==1]:
    S=sols(p)
    rep=[s for s in S if len(set(s))<3]
    distinct=len(S)-len(rep)
    ordered=6*distinct+3*len(rep)
    tI=sum(1 for s in S if sum(v%p==0 for v in s)==1); tII=len(S)-tI
    rows.append((p,len(S),distinct,len(rep),ordered,tI,tII))
print("p unordered distinct repeated ordered typeI typeII")
for r in rows[:12]+rows[-5:]: print(*r)
print("primes with a repeated-denominator solution:",[(r[0],r[3]) for r in rows if r[3]][:30], "of",len(rows))
