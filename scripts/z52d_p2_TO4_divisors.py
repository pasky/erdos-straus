# z52d pass2 TO4: winning divisors a | 4Cp+1, a ≡ -1 (mod 4C), for p≡1 (24), p ≤ 2e4, C ≤ 100 (exact, sympy).
# Z1011: size of least positive winning representative a/N (lift-size proxy);  Z1023: parity of #winning divisors
# (complement involution a ↦ N/a preserves the class; fixed point only a=√N);  Z1631: symbol entropies of winners;
# Z1043: pairwise dependence ratio vs gcd(C1,C2).
import math, statistics, sys
from collections import Counter, defaultdict
from sympy import factorint, primerange, jacobi_symbol, legendre_symbol
PM=20000; CM=100
data=defaultdict(dict)   # p -> C -> list of winning a
sizes=[]; parity=Counter(); symcount=defaultdict(Counter); tot_wins=0; forced_bad=0
for p in primerange(5,PM+1):
    if p%24!=1: continue
    for C in range(1,CM+1):
        N=4*C*p+1; m=4*C
        f=factorint(N); divs=[1]
        for q,k in f.items(): divs=[d*q**j for d in divs for j in range(k+1)]
        W=sorted(a for a in divs if a>1 and a%m==m-1)
        if not W: continue
        data[p][C]=W
        tot_wins+=len(W)
        parity[(len(W)%2, math.isqrt(N)**2==N)]+=1
        sizes.append(W[0]/N)
        for a in W:
            if jacobi_symbol(a%p,p)!=-1: forced_bad+=1
            for name,val in (('(a/3)',jacobi_symbol(a%3,3) if a%3 else 0),('(a/5)',jacobi_symbol(a%5,5) if a%5 else 0),
                             ('(a/7)',jacobi_symbol(a%7,7) if a%7 else 0),('(2/a)',jacobi_symbol(2,a) if a%2 else 0),
                             ('(3/a)',jacobi_symbol(3,a) if a%2 else 0),('(5/a)',jacobi_symbol(5,a) if a%2 else 0),
                             ('(a/p)', jacobi_symbol(a%p,p)), ('(-1/a)', jacobi_symbol(-1,a) if a%2 else 0)):
                symcount[name][val]+=1
print("winning (p,C,a) triples:",tot_wins," violations of (a/p)=-1 (Lean jacobi_a_of_cform):",forced_bad)
print("Z1023 parity of #winning divisors by (count mod 2, N is square):",dict(parity))
print("Z1011 least winning rep a/N: median %.4f, 10%% %.4f, 90%% %.4f"%(statistics.median(sizes),sorted(sizes)[len(sizes)//10],sorted(sizes)[9*len(sizes)//10]))
def H(c):
    t=sum(c.values()); return -sum(v/t*math.log2(v/t) for v in c.values() if v)
print("Z1631 entropies (bits) of symbol values over all winning a:")
for k,c in symcount.items(): print("  ",k,dict(c),"H=%.3f"%H(c))
# Z1043: dependence ratio vs gcd
def ratio_by_gcd():
    stats=defaultdict(list)
    ps=list(data.keys())
    for C1 in range(1,31):
        for C2 in range(C1+1,31):
            n=len(ps); A=sum(1 for p in ps if C1 in data[p]); B=sum(1 for p in ps if C2 in data[p])
            AB=sum(1 for p in ps if C1 in data[p] and C2 in data[p])
            if A*B>0: stats[math.gcd(C1,C2)].append(AB*n/(A*B))
    return {g:(round(statistics.mean(v),3),len(v)) for g,v in sorted(stats.items())}
print("Z1043 mean ratio P(A∩B)/(P(A)P(B)) by gcd(C1,C2) (C1<C2≤30):", ratio_by_gcd())
