# y7 (O215): does the Hecke "angle" of pi (p = N(pi), pi = x + y*theta, theta=(1+sqrt(-7))/2, N = x^2+xy+2y^2)
# predict the e=6 double failure at p ≡ 1 (mod 21) beyond p mod q?  (x, y) mod q up to ±1 and conjugation
# (conj: (x, y) -> (x + y, -y)).  usage: y7_split_norm.py X q
import sys, math
from collections import defaultdict
X=int(sys.argv[1]); q=int(sys.argv[2])
N=X+8
spf=list(range(N))
for i in range(2,int(N**.5)+1):
    if spf[i]==i:
        for j in range(i*i,N,i):
            if spf[j]==j: spf[j]=i
def only1mod3(n):
    while n%3==0: n//=3
    while n>1:
        r=spf[n]
        if r%3==2: return False
        n//=r
    return True
rep={}
Y=int(math.isqrt(X))+2
for y in range(0,Y):
    for x in range(-Y,2*Y):
        n=x*x+x*y+2*y*y
        if 2<=n<=X and spf[n]==n and n not in rep: rep[n]=(x,y)
def canon(x,y):
    c=[]
    for (a,b) in [(x,y),(-x,-y),(x+y,-y),(-x-y,y)]:
        c.append((a%q,b%q))
    return min(c)
tab=defaultdict(lambda:[0,0])
for p,(x,y) in rep.items():
    if p%21!=1: continue
    d=only1mod3((p+6)//7) and only1mod3((6*p+1)//7)
    k=(p%q,canon(x,y)); tab[k][0]+=1; tab[k][1]+=d
byp=defaultdict(list)
for (pm,c),(a,b) in tab.items(): byp[pm].append((c,a,b))
chi2=0; dof=0
for pm in sorted(byp):
    L=byp[pm]; A=sum(a for _,a,_ in L); B=sum(b for _,_,b in L); r=B/A
    used=[(c,a,b) for c,a,b in L if a>=30]
    if len(used)>=2 and 0<r<1:
        Au=sum(a for _,a,_ in used); Bu=sum(b for _,_,b in used); ru=Bu/Au
        for c,a,b in used: chi2+=(b-a*ru)**2/(a*ru*(1-ru))
        dof+=len(used)-1   # one fitted rate per tested stratum
    print(pm, f"n={A} rate={r:.3f}", " ".join(f"{c}:{b}/{a}" for c,a,b in sorted(L)))
print(f"total primes {sum(a for v in tab.values() for a in [v[0]])}, double failures {sum(v[1] for v in tab.values())}")
print(f"chi2={chi2:.1f} on {dof} degrees of freedom (strata with >=2 cells of >=30 primes and 0<rate<1)")
