"""bsB_redei_oddpart: for prime t = 3 mod 4, divisors m'' of tn+1 with 4 | (tn+1)/m'' have (m''/n) = (m''/t)
(genus product formula). Tabulate m'' mod t among the 'sign-odd' divisors ((m''/t) = -1) at primes n = 1 mod 4,
to see that the class -1 is one of (t-1)/2 QNR classes, separated from the others only by odd-order characters.
usage: python bsB_oddpart.py NLO NHI"""
import sys
from collections import Counter
from sympy import primerange, divisors, jacobi_symbol as J
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for t in (7,11,19,23,31):
    C=Counter(); bad=0
    for n in primerange(lo,hi):
        if n%4!=1: continue
        N=t*n+1
        for d in divisors(N):
            if (N//d)%4: continue
            if J(d%n,n)!=J(d%t,t): bad+=1
            if J(d%t,t)==-1: C[d%t]+=1
    tot=sum(C.values())
    print(t, "violations",bad, "QNR-class shares:", {a:round(C[a]/tot,3) for a in sorted(C)})
