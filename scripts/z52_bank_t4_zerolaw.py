"""T4 helper (z52 bank): run from the repo root."""
import math
from sympy import primerange
P0=lambda mu: math.exp(-0.535*mu**0.91)
# Gaussian: class means c/L^2 at logN ~ 9.0, 11.5, 13.8  (classes keyed by (Re mod 4, Im mod 4) after normalising Re even)
tab={(0,1):(0.118,0.160,0.190),(2,1):(0.135,0.167,0.184),(2,3):(0.157,0.164,0.203),(0,3):(0.346,0.347,0.436)}
Ls=(9.0,11.53,13.81)
def alpha(k,L):
    a=tab[k]
    if L<=Ls[0]: return a[0]
    if L>=Ls[2]: return a[2]
    i=0 if L<Ls[1] else 1
    return a[i]+(a[i+1]-a[i])*(L-Ls[i])/(Ls[i+1]-Ls[i])
two={}
def sq2(p):
    for a in range(1,int(p**.5)+1):
        b=int(round((p-a*a)**.5))
        if b>0 and a*a+b*b==p: return a,b
pred={'<=1e4':0,'1e4-1e6':0}
for p in primerange(30,10**6):
    if p%4!=1: continue
    a,b=sq2(p); A,B=(a,b) if a%2==0 else (b,a)
    L=math.log(p); mu=alpha((A%4,B%4),L)*L*L
    pred['<=1e4' if p<=10**4 else '1e4-1e6']+=P0(mu)
print('Gaussian ES_Q1 zero-law prediction (P0=exp(-0.535 mu^0.91), mu=class mean):',{k:round(v,2) for k,v in pred.items()},' observed: 6 (29..5393), 0')
# k=-4: n=1 (4) classes 3|n (alpha~0.14) and 3 not| n (alpha~0.30-0.39 depending on n mod 8)
al={(1,0):0.131,(5,0):0.146,(1,1):0.301,(5,1):0.389}
pr={'1000-1e5':0,'<=1000':0}
for n in range(13,10**5+1,4):
    L=math.log(n); k=(n%8, 0 if n%3==0 else 1); mu=al[k]*L*L
    pr['<=1000' if n<=1000 else '1000-1e5']+=P0(mu)
print('S_{n,-4} zero-law prediction, n=1(4):',{k:round(v,2) for k,v in pr.items()},' observed: 4 (9,21,165,945) <=1000, 1 (1197) above')
