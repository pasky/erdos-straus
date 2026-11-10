# z69 TWIST triage I23: "twisted trace at sqrt(p)".
# A solution 4/sqrt(p) = sum 1/alpha_i, alpha_i = x_i + y_i sqrt(p) in Z[sqrt p], gives
#   4/p = sum y_i/D_i  and  0 = sum x_i/D_i,   D_i = p y_i^2 - x_i^2.
# With w_i = x_i/y_i = g_i/h_i (lowest terms; w = 0 iff x = 0) and n_i = D_i/y_i:
#   y_i/D_i = 1/n_i is a unit fraction  <=>  m_i := p h_i^2 - g_i^2 > 0 divides n_i   (then y = n h^2/m, x = n g h/m)
#   twist equation: sum_i w_i/n_i = 0.
# Test K-I23: for each prime p == 1 (4) below P, does some ES triple (n1<=n2<=n3) admit lifts (w1,w2,w3)?
# Enumerate lifts of two of the n_i with h <= H; the third w is then forced and is tested exactly.
import sys, math
from fractions import Fraction as Fr
from sympy import primerange, divisors
def es_triples(p):
    out=[]
    for n1 in range(p//4+1, 3*p//4+1):
        num=4*n1-p; den=p*n1            # num/den = 1/n2+1/n3
        g=math.gcd(num,den); num//=g; den//=g
        for n2 in range(max(n1,den//num+1), 2*den//num+1):
            a=num*n2-den
            if a>0 and (den*n2)%a==0:
                n3=den*n2//a
                if n3>=n2: out.append((n1,n2,n3))
    return out
def lifts(n,p,H):
    L=[]
    if n%p==0: L.append(Fr(0))
    for h in range(1,H+1):
        g=1; lim=math.isqrt(p*h*h)
        for g in range(1,lim+1):
            if math.gcd(g,h)!=1: continue
            m=p*h*h-g*g
            if m>0 and n%m==0: L.append(Fr(g,h)); L.append(Fr(-g,h))
    return L
def valid(w,n,p):
    g,h=w.numerator,w.denominator; m=p*h*h-g*g
    return m>0 and n%m==0 and (g!=0 or n%p==0)
P=int(sys.argv[1]); H=int(sys.argv[2]); fails=[]; npr=0
for p in primerange(5,P):
    if p%4!=1: continue
    npr+=1; T=es_triples(p); hits=0; ex=None
    for (n1,n2,n3) in T:
        ns=(n1,n2,n3)
        for (i,j,k) in ((0,1,2),(0,2,1),(1,2,0)):
            Li=lifts(ns[i],p,H); Lj=lifts(ns[j],p,H)
            for wi in Li:
                for wj in Lj:
                    wk=-ns[k]*(wi/ns[i]+wj/ns[j])
                    if valid(wk,ns[k],p):
                        hits+=1; ex=ex or (ns,(i,j,k),(str(wi),str(wj),str(wk)))
    print(p,len(T),hits,ex,flush=True)
    if hits==0: fails.append(p)
print(f"primes p==1(4) < {P}: {npr}; with ES triples but no twisted lift (h<={H} on two terms): {len(fails)}: {fails[:40]}")
