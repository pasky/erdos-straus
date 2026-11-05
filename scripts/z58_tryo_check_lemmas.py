# z58 TRYO: numeric sanity checks of Lemma 1.1 (iii)<->(iv), Lemma 1.3 (squares) and Lemma 1.4 (QNR u).
from sympy import factorint, jacobi_symbol, isprime, divisors
import random
random.seed(1)
# Lemma 1.4
bad=0; tested=0
for p in [x for x in range(10**6, 10**6+20000) if x%8==1 and isprime(x)][:40]:
    for u in range(1,300):
        if jacobi_symbol(u,p)!=-1: continue
        tested+=1
        qs=[q for q in factorint(p+u) if (2*u)%q!=0]
        if not any(jacobi_symbol(-u,q)==-1 for q in qs): bad+=1
print("Lemma1.4 tested",tested,"bad",bad)
# Lemma 1.3: odd squares never hit, u<=200
hits=0
for m in range(3,400,2):
    n=m*m
    for u in range(1,200):
        if any(d%(4*u)==4*u-1 for d in divisors(n+u)): hits+=1
print("Lemma1.3 square hits",hits)
# Lemma 1.1 (iii)<->(iv) on n in a range: exists u,d vs exists u,B
mism=0
for n in range(5,3000,4):
    a=any(any(d%(4*u)==4*u-1 for d in divisors(n+u)) for u in range(1,n+1))
    b=any((n+u+B)%(4*u*B)==0 for u in range(1,n+1) for B in range(1,n//u+2))
    mism+= (a!=b)
print("Lemma1.1 mismatches",mism)
