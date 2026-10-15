# O240: which Sophie-Germain windows m = 4*c*t^4 - k (j = 2) fire at the point mu = 0 of c*2^s + k (s == 0 mod L), c + k = 4^i?
# Near mu = 0: X = 2^((s-4)/4) == 1/2 (mod m), n == c + k (mod m).  Atoms: primes of c, f± = 2X^2 ± 2Xt + t^2.
import sys, math, itertools
from sympy import factorint, n_order
c=int(sys.argv[1]); k=int(sys.argv[2]); TMAX=int(sys.argv[3])
for t in range(1,TMAX+1,2):
    m=4*c*t**4-k
    if m<=1 or math.gcd(m,2*c)!=1: continue
    X=pow(2,-1,m); fac=[(2*X*X+2*X*t+t*t)%m,(2*X*X-2*X*t+t*t)%m]
    at=[(p%m,v) for p,v in factorint(c).items()]+[(x,1) for x in fac]
    K=(c+k+m)*pow(4,-1,m)%m
    if math.gcd(K,m)!=1 or any(math.gcd(a,m)!=1 for a,_ in at): print("t",t,"m",m,"degenerate"); continue
    sols=[ex for ex in itertools.product(*[range(2*v+1) for _,v in at]) if math.prod(pow(a,x,m) for (a,_),x in zip(at,ex))%m==(-K)%m]
    print("t=%d m=%d (m mod 8 = %d) ord_m(2)=%d  solutions: %s"%(t,m,m%8,n_order(2,m),sols[:3]))
