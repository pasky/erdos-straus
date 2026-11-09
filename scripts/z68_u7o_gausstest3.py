# Same-p matched control for rule G: for each p compute the full letter indicator h(L), 10 <= L <= LMAX.
# For each Gaussian candidate L (divisor of a, b, a+b, |a-b| in [10, LMAX]) the expected hit probability is the mean
# of h over L' != L with L' = L (mod 120) and L' in the same dyadic block as L.  Reports observed vs expected.
import sys, math
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
def twosq(p):
    for a in range(1,math.isqrt(p)+1,2):
        b2=p-a*a; b=math.isqrt(b2)
        if b*b==b2: return a,b
LMAX=int(sys.argv[1])
ps=[int(l.split()[0]) for l in sys.stdin if l.strip()]
obs=0; exp=0.0; n=0
for p in ps:
    h={L:is_letter(p,L) for L in range(10,LMAX+1)}
    a,b=twosq(p); S=set()
    for v in (a,b,a+b,abs(a-b)):
        for d in divisors(v):
            if 10<=d<=LMAX: S.add(d)
    for L in S:
        blk=L.bit_length(); pool=[h[M] for M in h if M!=L and M%120==L%120 and M.bit_length()==blk]
        if not pool: continue
        n+=1; obs+=h[L]; exp+=sum(pool)/len(pool)
    print(p,len(S),obs,round(exp,2),flush=True)
sd=math.sqrt(exp)
print(f"G candidates n={n}: observed hits {obs}, same-p matched expectation {exp:.1f} (Poisson sd ~{sd:.1f})")
