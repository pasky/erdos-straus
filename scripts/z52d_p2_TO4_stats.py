# z52d pass2 TO4: distributional statistics on C-form win data (/tmp/cf_1e7_K400.txt: p≤1e7, C≤400).
# Items: Z1039 (moments), Z1040 (factorial moments), Z1141 (quenched vs annealed), Z1041/Z1043/Z1044 (pairwise
# event dependence for win(p,C), C≤30), Z1048 (least QNR vs smallest winning C), Z1620 check (log-growth of N(X)).
import math, statistics, random
from collections import Counter
from sympy import legendre_symbol
rows=[]
for line in open('/tmp/cf_1e7_K400.txt'):
    t=list(map(int,line.split())); 
    if t[0]>=10**4 and t[0]%24==1 and t[0]<=10**6: rows.append((t[0],t[2:2+t[1]]))
print("sample primes p≡1 mod 24 in [1e4,1e6]:",len(rows))
N=[len(w) for p,w in rows]
m=[statistics.mean(N)]
mu=statistics.mean(N)
for k in (2,3,4): m.append(statistics.mean([(x-mu)**k for x in N]))
m=[None]+m if False else m
print("Z1039 mean %.3f var %.3f 3rd central %.3f 4th central %.3f"%(mu,m[1],m[2],m[3]))
# factorial moments over distinct winners: E[N(N-1)], E[N(N-1)(N-2)] (N counts distinct C, so falling factorial is the natural test)
F2=statistics.mean([x*(x-1) for x in N]); F3=statistics.mean([x*(x-1)*(x-2) for x in N])
print("Z1040 falling moments: E[N]=%.3f E[N(N-1)]=%.3f E[N(N-1)(N-2)]=%.3f ; Poisson would give %.3f %.3f %.3f"%(mu,F2,F3,mu,mu*mu,mu**3))
# Z1141 quenched vs annealed: mean log(1+N) vs log(1+mean N)
print("Z1141 quenched E[log(1+N)]=%.4f  annealed log(1+E[N])=%.4f  gap=%.4f"%(statistics.mean([math.log(1+x) for x in N]), math.log(1+mu), math.log(1+mu)-statistics.mean([math.log(1+x) for x in N])))
# Z1041/1043/1044: pairwise dependence of win(p,C) over C ≤ 30, p in sample (p≡1 mod 24)
Cs=range(1,31)
W=[set(w) for p,w in rows]
n=len(W)
P={C: sum(1 for s in W if C in s)/n for C in Cs}
worst=[]
ratios=[]
for C1 in Cs:
    for C2 in Cs:
        if C2<=C1: continue
        j=sum(1 for s in W if C1 in s and C2 in s)/n
        if P[C1]*P[C2]>0: ratios.append((j/(P[C1]*P[C2]),C1,C2,round(P[C1],3),round(P[C2],3)))
ratios.sort()
print("Z1043/1041 pairwise P(A∩B)/(P(A)P(B)) over C1<C2≤30: min %.3f max %.3f median %.3f"%(ratios[0][0],ratios[-1][0],statistics.median([r[0] for r in ratios])))
print(" most-positive pairs:", [(round(r[0],2),r[1],r[2]) for r in ratios[-5:]], "most-negative:", [(round(r[0],2),r[1],r[2]) for r in ratios[:5]])
# triple dependence sample (Z1044): P(A∩B∩C)/(P(A)P(B)P(C)) for C in {1,2,3,4,6}
T=[1,2,3,4,6]; tr=[]
for i in range(len(T)):
    for j in range(i+1,len(T)):
        for k in range(j+1,len(T)):
            a,b,c=T[i],T[j],T[k]
            pabc=sum(1 for s in W if a in s and b in s and c in s)/n
            if P[a]*P[b]*P[c]>0: tr.append((round(pabc/(P[a]*P[b]*P[c]),3),a,b,c))
print("Z1044 triple ratios (C in 1,2,3,4,6):", tr)
# Z1048: least quadratic nonresidue q(p) vs smallest winning C
def lqnr(p):
    q=2
    while legendre_symbol(q,p)!=-1: q+=1
    return q
pairs=[]
for p,w in rows[:3000]:
    if w: pairs.append((lqnr(p), w[0]))
xs=[a for a,b in pairs]; ys=[b for a,b in pairs]
import numpy as np
print("Z1048 n=%d corr(log least-QNR, log smallest winning C) = %.3f"%(len(pairs), np.corrcoef(np.log(xs),np.log(ys))[0,1]))
# Z1620 (log-growth): N(X)/log X over X
for X in (30,100,300,400):
    v=[sum(1 for c in w if c<=X) for p,w in rows]
    print("Z1620 X=%d mean N(X)=%.3f  mean N(X)/log X=%.3f"%(X,statistics.mean(v),statistics.mean(v)/math.log(X)))
