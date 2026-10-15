# Forced windows for numerator nu at odd squares n = a^2: m = q1 (or q1*q2), q_i = 3 (4) prime, K = (n+m)/nu integer,
# gcd(K, m n) = 1, (K/q_i) = -1 for all i  (then -1 in <primes of K> mod m and -K a square there: the CAP_POINTWISE
# Thm 1.1' mechanism for nu/n). Report, per nu, how many squares a^2 (a odd, coprime to 6nu... ) have such a window m <= MMAX.
import sys, math
from sympy import primerange, jacobi_symbol as J
NU=int(sys.argv[1]); AMAX=int(sys.argv[2]); MMAX=int(sys.argv[3])
ps=[q for q in primerange(3,MMAX) if q%4==3]
wins=[(q,) for q in ps]+[(q1,q2) for i,q1 in enumerate(ps) for q2 in ps[i+1:] if q1*q2<=MMAX]
for nu in range(2,NU+1):
    tot=hit=0
    for a in range(5,AMAX,2):
        if math.gcd(a,nu)>1: continue
        n=a*a; tot+=1
        for w in wins:
            m=math.prod(w)
            if (n+m)%nu or math.gcd(m,n)>1: continue
            K=(n+m)//nu
            if math.gcd(K,m*n)>1: continue
            if all(J(K,q)==-1 for q in w): hit+=1; break
    print(nu, nu%8, "squares with a forced window:",hit,"/",tot)
